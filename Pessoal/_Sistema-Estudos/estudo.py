#!/usr/bin/env python3
"""
estudo.py — Sistema de transcrição de estudos para Obsidian.

Transcreve conteúdo de 3 fontes, sempre com Whisper LOCAL (grátis):
  - YouTube       : pega a legenda direto (instantâneo) ou áudio via Whisper
  - Arquivo local : qualquer .mp4/.mkv/.mp3/.wav -> Whisper
  - Gravação      : captura o áudio do sistema (cursos) ou do microfone (aula
                    presencial) AO VIVO, transcrevendo em pedaços enquanto você
                    assiste, e mostra o texto aparecendo na tela.

A saída é SEMPRE uma transcrição BRUTA salva em `_inbox/` do vault. Depois,
no Claude Code, você roda  /nota-video  e eu transformo essa transcrição em
uma nota didática completa, organizada por módulos e tópicos.

Uso:
    python estudo.py youtube "<url>"           --tema "Tema do vídeo"
    python estudo.py local   "<arquivo>"        --tema "Tema do vídeo"
    python estudo.py gravar                      --tema "Tema do vídeo"  [--fonte sistema|mic]
    python estudo.py listar                      # mostra fontes de áudio disponíveis

Pare a gravação com Ctrl+C (ou Enter) — a transcrição final é montada na hora.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG_PATH = HERE / "config.json"


# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #
def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def slugify(texto: str) -> str:
    texto = texto.strip().lower()
    texto = re.sub(r"[^\w\s-]", "", texto, flags=re.UNICODE)
    texto = re.sub(r"[\s_-]+", "-", texto)
    return texto.strip("-")[:60] or "sem-tema"


def now_stamp() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d-%H%M")


def have(cmd: str) -> bool:
    return subprocess.run(["which", cmd], capture_output=True).returncode == 0


def die(msg: str, code: int = 1):
    print(f"\n❌ {msg}", file=sys.stderr)
    sys.exit(code)


def inbox_dir(cfg: dict) -> Path:
    p = Path(cfg["vault_path"]) / cfg["inbox_dir"]
    p.mkdir(parents=True, exist_ok=True)
    return p


def audio_dir(cfg: dict) -> Path:
    p = Path(cfg["vault_path"]) / cfg["audio_dir"]
    p.mkdir(parents=True, exist_ok=True)
    return p


def salvar_inbox(cfg: dict, tema: str, fonte: str, origem: str,
                 texto: str, extra: dict | None = None) -> Path:
    """Grava a transcrição bruta com frontmatter no _inbox e devolve o caminho."""
    stamp = now_stamp()
    destino = inbox_dir(cfg) / f"{slugify(tema)}__{stamp}.md"

    fm = {
        "tema": tema,
        "fonte": fonte,
        "origem": origem,
        "data": dt.date.today().isoformat(),
        "palavras": len(texto.split()),
        "status": "bruto",
    }
    if extra:
        fm.update(extra)

    linhas = ["---"]
    for k, v in fm.items():
        if isinstance(v, str):
            linhas.append(f'{k}: "{v}"')
        else:
            linhas.append(f"{k}: {v}")
    linhas.append("---\n")
    linhas.append(f"# Transcrição bruta — {tema}\n")
    linhas.append(texto.strip() + "\n")

    destino.write_text("\n".join(linhas), encoding="utf-8")
    return destino


# --------------------------------------------------------------------------- #
# Whisper (carregado só quando precisa, pois é pesado)
# --------------------------------------------------------------------------- #
_MODEL = None


def whisper_lang(cfg: dict):
    """'auto' -> None (Whisper detecta o idioma sozinho)."""
    lang = cfg["whisper"].get("language", "auto")
    return None if lang in (None, "", "auto") else lang


def get_model(cfg: dict):
    global _MODEL
    if _MODEL is None:
        try:
            from faster_whisper import WhisperModel
        except ImportError:
            die("faster-whisper não instalado. Rode:  ./setup.sh")
        w = cfg["whisper"]
        print(f"⏳ Carregando modelo Whisper '{w['model']}' "
              f"({w['device']}/{w['compute_type']})… (só na 1ª vez)")
        _MODEL = WhisperModel(w["model"], device=w["device"],
                              compute_type=w["compute_type"])
    return _MODEL


def transcrever_arquivo(cfg: dict, caminho: str, verbose: bool = True) -> str:
    """Transcreve um arquivo de áudio/vídeo inteiro e devolve o texto."""
    model = get_model(cfg)
    segments, _ = model.transcribe(
        caminho, language=whisper_lang(cfg), vad_filter=True
    )
    partes = []
    for seg in segments:
        partes.append(seg.text.strip())
        if verbose:
            print(f"  [{seg.start:6.0f}s] {seg.text.strip()}")
    return " ".join(partes).strip()


# --------------------------------------------------------------------------- #
# Fonte: YouTube
# --------------------------------------------------------------------------- #
def youtube_id(url: str) -> str | None:
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([\w-]{11})", url)
    return m.group(1) if m else (url if re.fullmatch(r"[\w-]{11}", url) else None)


def _extra_curso(curso: str | None, base: dict | None = None) -> dict:
    extra = dict(base or {})
    if curso:
        extra["curso"] = curso
    return extra


def from_youtube(cfg: dict, url: str, tema: str, curso: str | None = None) -> Path:
    vid = youtube_id(url)
    if not vid:
        die(f"Não consegui extrair o ID do vídeo de: {url}")

    texto = None
    # 1) Tenta legenda pronta (instantâneo, sem baixar nada) — API v1.x
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        idiomas = cfg["youtube"]["idiomas_preferidos"]
        try:
            fetched = api.fetch(vid, languages=idiomas)
        except Exception:
            # qualquer legenda disponível
            fetched = next(iter(api.list(vid))).fetch()
        texto = " ".join(s.text for s in fetched if s.text.strip())
        print(f"✅ Legenda do YouTube obtida ({len(texto.split())} palavras).")
    except Exception as e:
        print(f"⚠️  Sem legenda acessível ({e}). Vou baixar o áudio e transcrever…")

    # 2) Fallback: baixa áudio com yt-dlp e usa Whisper
    if not texto:
        if not have("yt-dlp"):
            die("yt-dlp não instalado e o vídeo não tem legenda. Rode ./setup.sh")
        if not have("ffmpeg"):
            die("ffmpeg não instalado (necessário para baixar/transcrever áudio). Rode ./setup.sh")
        saida = audio_dir(cfg) / f"yt_{vid}.m4a"
        print("⬇️  Baixando áudio…")
        subprocess.run(
            ["yt-dlp", "-x", "--audio-format", "m4a", "-o", str(saida),
             f"https://www.youtube.com/watch?v={vid}"],
            check=True,
        )
        print("🎧 Transcrevendo com Whisper…")
        texto = transcrever_arquivo(cfg, str(saida))
        saida.unlink(missing_ok=True)

    destino = salvar_inbox(cfg, tema, "youtube",
                           f"https://www.youtube.com/watch?v={vid}", texto,
                           extra=_extra_curso(curso))
    return destino


# --------------------------------------------------------------------------- #
# Fonte: Arquivo local
# --------------------------------------------------------------------------- #
def from_local(cfg: dict, caminho: str, tema: str, curso: str | None = None) -> Path:
    arq = Path(caminho).expanduser()
    if not arq.exists():
        die(f"Arquivo não encontrado: {arq}")
    if not have("ffmpeg"):
        die("ffmpeg não instalado (necessário para ler o áudio). Rode ./setup.sh")
    print(f"🎧 Transcrevendo {arq.name} com Whisper…")
    texto = transcrever_arquivo(cfg, str(arq))
    return salvar_inbox(cfg, tema, "local", str(arq), texto,
                        extra=_extra_curso(curso))


# --------------------------------------------------------------------------- #
# Fonte: Gravação ao vivo (sistema ou microfone) com transcrição em pedaços
# --------------------------------------------------------------------------- #
def pulse_source(fonte: str) -> str:
    """Descobre o device PulseAudio/PipeWire: 'sistema' = monitor do sink."""
    try:
        if fonte == "sistema":
            sink = subprocess.check_output(
                ["pactl", "get-default-sink"], text=True).strip()
            return f"{sink}.monitor"
        else:  # microfone
            return subprocess.check_output(
                ["pactl", "get-default-source"], text=True).strip()
    except Exception as e:
        die(f"Não consegui detectar a fonte de áudio ({e}). "
            f"Rode: python estudo.py listar")


def listar_fontes():
    if not have("pactl"):
        die("pactl não encontrado (PulseAudio/PipeWire).")
    print("=== SINKS (saídas — o '.monitor' delas captura o áudio do sistema) ===")
    subprocess.run(["pactl", "list", "short", "sinks"])
    print("\n=== SOURCES (entradas — microfones) ===")
    subprocess.run(["pactl", "list", "short", "sources"])
    print(f"\nSink padrão : {subprocess.check_output(['pactl','get-default-sink'],text=True).strip()}")
    print(f"Source padrão: {subprocess.check_output(['pactl','get-default-source'],text=True).strip()}")


def from_gravacao(cfg: dict, tema: str, fonte: str, curso: str | None = None) -> Path:
    if not have("ffmpeg"):
        die("ffmpeg não instalado. Rode ./setup.sh")
    if not have("pactl"):
        die("pactl não encontrado (PulseAudio/PipeWire).")

    device = pulse_source(fonte)
    chunk_sec = int(cfg["gravacao"]["segundos_por_chunk"])
    stamp = now_stamp()
    sessao = audio_dir(cfg) / f"sessao_{slugify(tema)}_{stamp}"
    sessao.mkdir(parents=True, exist_ok=True)
    padrao = str(sessao / "chunk_%05d.wav")

    fonte_label = "ÁUDIO DO SISTEMA (curso/vídeo)" if fonte == "sistema" else "MICROFONE (aula)"
    print(f"\n🎙️  Gravando de: {fonte_label}  [{device}]")
    print(f"📦 Transcrevendo a cada {chunk_sec}s. O texto vai aparecer abaixo.")
    print("⏹️  Pressione Ctrl+C (ou Enter) quando o vídeo/aula terminar.\n")

    # ffmpeg grava em segmentos .wav (16kHz mono = ideal pro Whisper)
    ff = subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-f", "pulse", "-i", device,
         "-ac", "1", "-ar", "16000",
         "-f", "segment", "-segment_time", str(chunk_sec), "-reset_timestamps", "1",
         padrao],
        stdin=subprocess.DEVNULL,
    )

    parado = threading.Event()
    transcricao: list[str] = []

    def worker():
        """Transcreve cada chunk assim que ele é finalizado pelo ffmpeg."""
        model = get_model(cfg)
        idx = 0
        while not parado.is_set() or _chunks_pendentes(sessao, idx):
            atual = sessao / f"chunk_{idx:05d}.wav"
            proximo = sessao / f"chunk_{idx + 1:05d}.wav"
            # chunk 'idx' está pronto quando o próximo já começou OU paramos
            if atual.exists() and (proximo.exists() or parado.is_set()):
                try:
                    segs, _ = model.transcribe(
                        str(atual), language=whisper_lang(cfg), vad_filter=True)
                    txt = " ".join(s.text.strip() for s in segs).strip()
                    if txt:
                        transcricao.append(txt)
                        print(f"📝 {txt}\n")
                except Exception as e:
                    print(f"(erro no chunk {idx}: {e})")
                idx += 1
            else:
                time.sleep(0.5)

    th = threading.Thread(target=worker, daemon=True)
    th.start()

    # Espera o usuário parar (Ctrl+C ou Enter)
    try:
        input()  # qualquer Enter encerra
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        print("\n⏹️  Encerrando gravação e transcrevendo o restante…")
        ff.send_signal(signal.SIGINT)
        try:
            ff.wait(timeout=10)
        except subprocess.TimeoutExpired:
            ff.kill()
        time.sleep(1.0)  # deixa o último chunk fechar
        parado.set()
        th.join(timeout=120)

    texto = " ".join(transcricao).strip()
    if not texto:
        die("Nenhum áudio transcrito. Verifique a fonte com: python estudo.py listar")

    destino = salvar_inbox(cfg, tema, "gravacao", f"{fonte}:{device}", texto,
                           extra=_extra_curso(curso, {"chunks": len(transcricao)}))

    # limpa os .wav temporários
    for w in sessao.glob("*.wav"):
        w.unlink(missing_ok=True)
    sessao.rmdir()
    return destino


def _chunks_pendentes(sessao: Path, idx: int) -> bool:
    return (sessao / f"chunk_{idx:05d}.wav").exists()


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main():
    cfg = load_config()
    ap = argparse.ArgumentParser(
        prog="estudo.py",
        description="Transcreve vídeos/aulas e salva no _inbox do Obsidian.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    curso_help = "Nome do curso, p/ agrupar várias partes na mesma pasta (opcional)"

    p_yt = sub.add_parser("youtube", help="Transcreve um vídeo do YouTube")
    p_yt.add_argument("url")
    p_yt.add_argument("--tema", required=True)
    p_yt.add_argument("--curso", default=None, help=curso_help)

    p_lo = sub.add_parser("local", help="Transcreve um arquivo de vídeo/áudio")
    p_lo.add_argument("arquivo")
    p_lo.add_argument("--tema", required=True)
    p_lo.add_argument("--curso", default=None, help=curso_help)

    p_gr = sub.add_parser("gravar", help="Grava e transcreve ao vivo")
    p_gr.add_argument("--tema", required=True)
    p_gr.add_argument("--curso", default=None, help=curso_help)
    p_gr.add_argument("--fonte", choices=["sistema", "mic"],
                      default=cfg["gravacao"]["fonte_padrao"])

    sub.add_parser("listar", help="Lista as fontes de áudio disponíveis")

    args = ap.parse_args()

    if args.cmd == "listar":
        listar_fontes()
        return

    if args.cmd == "youtube":
        destino = from_youtube(cfg, args.url, args.tema, args.curso)
    elif args.cmd == "local":
        destino = from_local(cfg, args.arquivo, args.tema, args.curso)
    elif args.cmd == "gravar":
        destino = from_gravacao(cfg, args.tema, args.fonte, args.curso)
    else:
        ap.error("comando desconhecido")
        return

    print("\n" + "=" * 60)
    print(f"✅ Transcrição bruta salva em:\n   {destino}")
    print("\nPróximo passo: abra o Claude Code neste vault e rode:")
    print("   /nota-video")
    print("Eu transformo isso numa nota didática organizada por módulos. 🎓")
    print("=" * 60)


if __name__ == "__main__":
    main()
