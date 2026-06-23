---
tags:
  - machine-learning
  - ia-generativa
  - whisper
  - audio
  - transcrição
---

# 2. Whisper e Transcrição de Áudio

> [!info] O que esta nota cobre
> O **Whisper**, modelo da OpenAI que **transforma fala em texto** (speech-to-text). Seus tamanhos de modelo e o trade-off entre **precisão, memória e velocidade**.

---

## 2.1. O que é o Whisper

> [!note] Definição
> **Whisper** é um modelo **baseado em Transformers** que faz **reconhecimento de fala**: recebe **áudio** e devolve **texto transcrito**. Funciona em vários idiomas.

> [!tip] Curiosidade
> É exatamente o tipo de modelo por trás de sistemas de transcrição de aulas e legendas automáticas — incluindo pipelines de estudo que convertem vídeos em texto.

---

## 2.2. Os tamanhos de modelo

> [!important] Escolher o tamanho é um trade-off
> O Whisper vem em vários tamanhos. Maior = **mais preciso**, mas **mais lento** e exigindo **mais memória (VRAM)**.

| Tamanho | Parâmetros | VRAM necessária | Velocidade relativa |
|---|---|---|---|
| **tiny** | 39 M | ~1 GB | ~32x (mais rápido) |
| **base** | 74 M | ~1 GB | ~16x |
| **small** | 244 M | ~2 GB | ~6x |
| **medium** | 769 M | ~5 GB | ~2x |
| **large** | 1550 M | ~10 GB | 1x (mais lento, mais preciso) |

> [!note] Modelos só-inglês vs. multilíngues
> Os tamanhos menores (até `medium`) têm uma versão **English-only** (`.en`), que é mais precisa **para inglês**. Para outros idiomas (como português), use a versão **multilingual**. O `large` é sempre multilíngue.

> [!example] Como escolher
> - Precisa rápido e o hardware é fraco? → **tiny/base**.
> - Precisa de máxima qualidade e tem GPU boa? → **large**.
> - Meio-termo equilibrado → **small/medium**.

---

## 2.3. Esqueleto em Python

```python
import whisper

modelo = whisper.load_model("small")        # escolha do tamanho
resultado = modelo.transcribe("teste.mp3")  # áudio → texto
print(resultado["text"])
```

> [!example] No curso
> Foi usado um arquivo `teste.mp3` para demonstrar a transcrição na prática.

---

## 2.4. Resumo

> [!summary] O essencial
> - **Whisper** = modelo Transformer que faz **áudio → texto** (speech-to-text), multilíngue.
> - Tamanhos: **tiny → large**. Maior = mais preciso, mas mais lento e com mais VRAM.
> - Versões `.en` (só inglês) são mais precisas para inglês; multilingual para os demais idiomas.

---

## 🔗 Próximos passos
- [[03 - Ferramentas e APIs de IA Generativa]] — os modelos de chat/texto (GPT, Gemini, DeepSeek) e como chamá-los.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
