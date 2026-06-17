---
tags: [sistema, meta]
---

# 🎓 Sistema de Estudos — Transcrição + Notas Didáticas

Dois pedaços que trabalham juntos:

1. **`estudo.py`** (app Python, roda no terminal) — captura/transcreve o vídeo
   ou aula com **Whisper local (grátis)** e salva uma transcrição BRUTA em `_inbox/`.
2. **Claude Code** (`/nota-video`) — pega essa transcrição bruta e gera uma
   **nota de estudo didática, organizada por módulos e tópicos**, salva na
   matéria certa do vault.

```
   🎬 vídeo/aula ──> estudo.py ──> _inbox/tema__data.md (bruto)
                                          │
                                          ▼
                              Claude Code  /nota-video
                                          │
                                          ▼
                    Pessoal/<Matéria>/Nota Didática.md  ✅
```

---

## 1. Instalação (só uma vez)

```bash
cd "/mnt/dados/Second-Brain/Pessoal/_Sistema-Estudos"
chmod +x setup.sh
./setup.sh
```

Isso instala o `ffmpeg` (pede sudo) e, num ambiente virtual `.venv`, os pacotes
Python (`faster-whisper`, `youtube-transcript-api`, `yt-dlp`).

> Na **primeira** transcrição por áudio, o Whisper baixa o modelo (~uma vez só).
> O modelo padrão é `small` (bom equilíbrio em português). Para mais precisão,
> edite `config.json` → `"model": "medium"` (mais lento). Para mais velocidade,
> `"base"`.

---

## 2. Como usar no dia a dia

Sempre ative o ambiente antes:

```bash
cd "/mnt/dados/Second-Brain/Pessoal/_Sistema-Estudos"
source .venv/bin/activate
```

### a) Vídeo do YouTube  (mais rápido — usa a legenda)
```bash
python estudo.py youtube "https://youtu.be/XXXX" --tema "Async no FastAPI"
```

### b) Arquivo de vídeo/áudio local
```bash
python estudo.py local "/home/pablo/Vídeos/aula03.mp4" --tema "Normalização de BD"
```

### c) Curso online (Udemy/Santander) ou qualquer vídeo na tela
Captura o **áudio do sistema** e transcreve **ao vivo** (o texto vai aparecendo).
Comece o comando, depois dê play no vídeo:
```bash
python estudo.py gravar --tema "Padrões de Projeto" --fonte sistema
```

### d) Aula presencial / ao vivo (microfone)
```bash
python estudo.py gravar --tema "Aula de Engenharia de Software" --fonte mic
```

**Para parar a gravação:** pressione **Enter** (ou Ctrl+C). A transcrição final
é montada na hora e salva no `_inbox/`.

### Ver/escolher a fonte de áudio
```bash
python estudo.py listar
```

---

## 3. Gerar a nota didática (no Claude Code)

Abra o Claude Code neste vault e rode:

```
/nota-video
```

- Sem argumento → pega a transcrição **mais recente** do `_inbox`.
- Com argumento → `/nota-video tema__2026-06-17-1530.md` para uma específica.

Eu (Claude) leio a transcrição, corrijo os termos técnicos, organizo em
**módulos → tópicos**, escrevo vocabulário e flashcards de revisão, e salvo na
pasta da matéria certa. Depois marco a transcrição como `processado`.

---

## 4. Organizar o material que você já tem

```
/organizar-estudos                     # diagnóstico do vault inteiro
/organizar-estudos FastAPI             # foca numa matéria
```

Cria índices por matéria (MOCs), liga notas relacionadas, melhora a didática e
oferece flashcards — sem apagar o que você escreveu.

---

## Estrutura de pastas

```
_Sistema-Estudos/
├── estudo.py            # app de transcrição
├── config.json          # caminhos, modelo Whisper, fonte de áudio
├── requirements.txt
├── setup.sh             # instalação
├── _template-modulo.md  # modelo das notas
├── _inbox/              # transcrições brutas (entram aqui)
└── _audio/              # temporários da gravação (limpos sozinhos)
```

## Dúvidas comuns

- **A gravação não pega o som do sistema?** Rode `python estudo.py listar` e
  confira o "Sink padrão". O sistema usa o `.monitor` dele. Se você usa fone
  Bluetooth/HDMI, troque o sink padrão nas configurações de som antes de gravar.
- **Transcrição lenta?** Use modelo `base` no `config.json`, ou transcreva
  YouTube (usa legenda, é instantâneo).
- **Idioma?** Por padrão `config.json` → `whisper.language` é `"auto"` (o Whisper
  detecta sozinho: curso em inglês vira transcrição em inglês, aula em português
  vira português). Se quiser **forçar** um idioma, troque para `"pt"` ou `"en"`.
  Atenção: forçar `"pt"` num áudio em inglês faz o Whisper *traduzir* para português.
