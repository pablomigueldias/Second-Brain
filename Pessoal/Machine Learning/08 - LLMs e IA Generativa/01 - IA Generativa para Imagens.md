---
tags:
  - machine-learning
  - ia-generativa
  - dall-e
  - stable-diffusion
  - imagens
---

# 1. IA Generativa para Imagens (DALL-E e Stable Diffusion)

> [!info] O que esta nota cobre
> Como a IA **gera imagens a partir de texto**: o modelo **DALL-E** (OpenAI) e o **Stable Diffusion** (open source). O que são, como funcionam em alto nível e como usar.

---

## 1.1. DALL-E

> [!note] O que é
> **DALL-E** é um modelo de **Deep Learning baseado em Transformers** capaz de **gerar imagens a partir de uma descrição em texto** (um *prompt*).

> [!summary] Características
> - **DALL-E 2** é uma versão aprimorada do original.
> - Possui **12 bilhões de parâmetros**.
> - É **treinado em pares de texto-imagem** — aprende a associação entre descrições e o que elas representam visualmente.

> [!important] Produto da OpenAI
> - Acessível por **site e API**.
> - Usa a **mesma biblioteca e chave** do modelo de NLP (GPT) da OpenAI — então quem já integrou o GPT integra o DALL-E facilmente.
> - O uso é **pago**.

---

## 1.2. Controlando o estilo via prompt

> [!example] O prompt define o resultado
> A imagem gerada depende muito da descrição. Você pode pedir estilos como:
> - **3D**
> - **Preto e branco**
> - **Antigo / vintage**
> - **Zoom / close**
> - etc.

> [!tip] Conexão
> Vale a mesma lição da [[../../Criar valor com IA, automação e bots/Modulos/03 - Desbloquear Soluções com IA Generativa|IA Generativa]]: *garbage in, garbage out*. Quanto mais **específico** o prompt (objeto + estilo + cenário + iluminação), melhor a imagem.

---

## 1.3. Stable Diffusion

> [!note] A alternativa open source
> O curso também usou o **Stable Diffusion**, um modelo de geração de imagens **open source**. Diferente do DALL-E (fechado e pago via API), o Stable Diffusion pode ser **baixado e rodado localmente** (ou via HuggingFace), o que dá mais controle e privacidade — ao custo de exigir mais hardware (GPU).

> [!example] Diferença prática
> | | DALL-E | Stable Diffusion |
> |---|---|---|
> | Acesso | API paga (OpenAI) | Open source (local/HuggingFace) |
> | Hardware | Não precisa (roda na nuvem) | Precisa de GPU para rodar bem |
> | Controle | Menor | Maior (ajusta, faz fine-tuning) |

---

## 1.4. Esqueleto em Python

```python
# DALL-E via API da OpenAI
from openai import OpenAI
client = OpenAI(api_key="SUA_CHAVE")

resposta = client.images.generate(
    model="dall-e-3",
    prompt="um gato caramelo em estilo 3D, numa rua de cidade inglesa",
    size="1024x1024",
)
print(resposta.data[0].url)

# Stable Diffusion via HuggingFace (roda localmente, precisa de GPU)
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda")
imagem = pipe("um gato caramelo em estilo 3D").images[0]
imagem.save("gato.png")
```

---

## 1.5. Resumo

> [!summary] O essencial
> - **IA generativa de imagens** = texto (prompt) → imagem.
> - **DALL-E** (OpenAI): baseado em Transformers, 12 bi de parâmetros, treinado em pares texto-imagem, **API paga**.
> - **Stable Diffusion**: alternativa **open source**, roda localmente (precisa de GPU).
> - O **prompt** controla estilo e qualidade (seja específico).

---

## 🔗 Próximos passos
- [[02 - Whisper e Transcrição de Áudio]] — saindo das imagens para o áudio.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
