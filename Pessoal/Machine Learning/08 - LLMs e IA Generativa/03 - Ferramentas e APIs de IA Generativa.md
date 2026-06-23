---
tags:
  - machine-learning
  - ia-generativa
  - gpt
  - gemini
  - deepseek
  - api
---

# 3. Ferramentas e APIs de IA Generativa

> [!info] O que esta nota cobre
> As ferramentas de **texto/chat** exploradas na prática do curso — **GPT (OpenAI)**, **Gemini (Google)** e **DeepSeek** — além de tarefas como **geração de texto**, **resumo** e **fill-mask**, e como acessá-las por **API**.

---

## 3.1. Acessando modelos: a ideia de API e chave

> [!important] O padrão dos modelos proprietários
> Modelos como GPT, Gemini e DeepSeek são acessados por **API**, com uma **chave de autenticação**. Você envia um **prompt** e recebe a resposta. O uso costuma ser **pago por tokens** (ver [[../07 - Processamento de Linguagem Natural (NLP)/04 - LLMs (Large Language Models)|LLMs]]).

> [!tip] Lembrete de segurança
> A **chave de API** é secreta — nunca a coloque direto no código que vai pro Git. Use variáveis de ambiente. (Vazar a chave = alguém gasta na sua conta.)

---

## 3.2. As ferramentas do curso

| Ferramenta | Empresa | Acesso | Observação |
|---|---|---|---|
| **GPT (ChatGPT)** | OpenAI | API paga + chave | O mais conhecido; texto, chat, código. |
| **Gemini** | Google | API + chave | Concorrente do GPT; multimodal. |
| **DeepSeek** | DeepSeek | API / open weights | Forte em raciocínio e código; opção mais econômica. |

> [!example] Notebooks do curso
> O curso trouxe exemplos práticos em notebooks: `OpenAIGPT.ipynb`, `Gemini.ipynb`, `DeepSeek.ipynb`, além de `TextGenerator.ipynb` (geração), `Resumo.ipynb` (resumos) e `Fillmask.ipynb` (preencher lacunas).

---

## 3.3. Tarefas práticas

> [!summary] O que dá para fazer
> - **Geração de texto** — criar conteúdo a partir de um prompt.
> - **Resumo** — condensar um texto longo.
> - **Fill-mask** — completar lacunas em frases (típico de modelos como BERT).
> - **Q&A, tradução, classificação** — todo o repertório de LLM.

---

## 3.4. Esqueleto em Python

```python
# OpenAI GPT
from openai import OpenAI
client = OpenAI(api_key="SUA_CHAVE")

resposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Resuma em 1 frase: ..."}],
)
print(resposta.choices[0].message.content)

# Google Gemini
import google.generativeai as genai
genai.configure(api_key="SUA_CHAVE")
modelo = genai.GenerativeModel("gemini-1.5-flash")
print(modelo.generate_content("Explique embeddings em 2 linhas").text)
```

> [!note] Escolher o modelo é escolher um trade-off
> Modelos maiores/melhores custam mais por token; modelos menores são baratos e rápidos. Para tarefas simples (resumo, classificação), um modelo pequeno resolve. Avalie **qualidade × custo** conforme o volume de uso.

---

## 3.5. Resumo

> [!summary] O essencial
> - Modelos de texto generativos (**GPT, Gemini, DeepSeek**) são acessados por **API + chave**.
> - Tarefas: **geração, resumo, fill-mask, Q&A, tradução**.
> - Custo por **token**: escolha o modelo conforme **qualidade × preço × volume**.
> - Proteja sua **chave de API**.

---

## 🔗 Próximos passos
- Fim do módulo de IA Generativa! Esses modelos viram o "cérebro" dos [[../09 - Agentes de IA/00 - Índice|Agentes de IA]] (próximo módulo).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
