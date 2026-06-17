---
tags: [sistema, guia]
---

# 📋 Como usar o Sistema de Estudos

Guia rápido do dia a dia. (Documentação completa: [[README]])

> **Regra de ouro:** sempre abra o terminal nesta pasta e ative o ambiente antes:
> ```bash
> cd "/mnt/dados/Second-Brain/Pessoal/_Sistema-Estudos"
> source .venv/bin/activate
> ```

---

## 🔁 O fluxo é sempre o mesmo (2 passos)

```
1) TERMINAL:  python estudo.py <fonte> ... --tema "..."   →  salva no _inbox/
2) CLAUDE:    /nota-video                                  →  vira nota didática
```

---

## 1️⃣ Transcrever (escolha a fonte do conteúdo)

### 📺 Vídeo do YouTube  (mais rápido — pega a legenda)
```bash
python estudo.py youtube "COLE_A_URL_AQUI" --tema "Async no FastAPI"
```

### 💻 Curso online (Udemy, Santander) ou qualquer vídeo na tela
Transcreve **ao vivo** enquanto você assiste. Rode o comando, **depois dê play**:
```bash
python estudo.py gravar --tema "Padrões de Projeto" --fonte sistema
```
➡️ A cada ~20s o texto aparece com `📝`. **Aperte Enter** para encerrar.

### 🎤 Aula presencial / ao vivo (microfone)
```bash
python estudo.py gravar --tema "Aula de Eng. de Software" --fonte mic
```
➡️ **Aperte Enter** quando a aula acabar.

### 📁 Arquivo de vídeo/áudio salvo no PC
```bash
python estudo.py local "/home/pablo/Vídeos/aula03.mp4" --tema "Normalização de BD"
```

> 💡 `--tema` é obrigatório: escreva sobre o que é o vídeo. Isso vira o título e
> ajuda a organizar a nota na matéria certa.

---

## 2️⃣ Gerar a nota didática (aqui no Claude Code)

Abra o Claude Code neste vault e digite:

```
/nota-video
```

- Sem nada depois → usa a transcrição **mais recente** do `_inbox`.
- Para uma específica → `/nota-video nome-do-arquivo.md`

Eu corrijo os termos técnicos, organizo em **módulos → tópicos**, e crio
vocabulário + **flashcards de revisão**, salvando na pasta da matéria. 🎓

---

## 🧹 Organizar o que você já tem

```
/organizar-estudos              ← diagnóstico do vault todo
/organizar-estudos FastAPI      ← foca numa matéria
```

---

## 🆘 Se algo der errado

| Problema | O que fazer |
|---|---|
| "ffmpeg não instalado" | `sudo apt-get install -y ffmpeg` |
| Gravação não pega o som | `python estudo.py listar` e veja o "Sink padrão". Se usa fone HDMI/Bluetooth, defina ele como saída padrão antes de gravar |
| Transcrição lenta | edite `config.json` → `"model": "base"` (mais rápido) |
| YouTube sem legenda | ele baixa o áudio e transcreve sozinho (mais lento) |

---

## ⚡ Cola rápida (copiar e colar)

```bash
# entrar no ambiente (sempre primeiro)
cd "/mnt/dados/Second-Brain/Pessoal/_Sistema-Estudos" && source .venv/bin/activate

# YouTube
python estudo.py youtube "URL" --tema "TEMA"

# curso na tela (ao vivo)
python estudo.py gravar --tema "TEMA" --fonte sistema

# aula presencial (microfone)
python estudo.py gravar --tema "TEMA" --fonte mic

# arquivo local
python estudo.py local "/caminho/video.mp4" --tema "TEMA"

# ver fontes de áudio
python estudo.py listar
```

Depois, no Claude Code: **`/nota-video`** ✅
