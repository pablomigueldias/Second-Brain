---
tags:
  - machine-learning
  - nlp
  - llm
  - gpt
  - fine-tuning
---

# 4. LLMs (Large Language Models)

> [!info] O que esta nota cobre
> Os **Large Language Models (LLMs)**: o que são, exemplos (GPT, BERT, T5), as tarefas que executam, a diferença entre **open source** e **proprietário**, o conceito de **fine-tuning** e as plataformas **HuggingFace** e **OpenAI**.

---

## 4.1. O que é um LLM

> [!note] Definição
> **LLMs (Large Language Models)** são modelos de linguagem **baseados em Transformers**, treinados em quantidades gigantescas de texto. Exemplos:
> - **GPT-2 / GPT-3 / GPT-4**
> - **BERT**
> - **T5**
> - **RoBERTa**

---

## 4.2. Open Source vs. Proprietário

> [!important] Duas categorias
> | Open Source (abertos) | Proprietário (fechados) |
> |---|---|
> | GPT-2 | GPT-3 |
> | BERT | GPT-4 |
> | T5 | |
> | XLNet | |

> [!tip] O que considerar além do nome
> Ao escolher um LLM, observe também:
> - **Idioma** (foi treinado/funciona bem em português?)
> - **Licença** (pode usar comercialmente? é gratuito?)

---

## 4.3. Tarefas que um LLM executa

> [!summary] O repertório
> - **Classificação de texto** (ex.: spam, sentimento)
> - **Perguntas e respostas** (Q&A)
> - **Tradução**
> - **Resumos**
> - **Geração de texto**
> - **Preencher a lacuna** (*fill mask* — completar palavras faltantes)

---

## 4.4. Fine-Tuning (Ajuste Fino)

> [!important] LLMs já vêm "pré-treinados"
> Diferente de um modelo clássico de ML (que você treina do zero com seus dados), os **LLMs são pré-treinados** — já aprenderam linguagem geral consumindo enormes recursos computacionais.

> [!note] O que é Fine-Tuning
> **Fine-Tuning** = o processo de **ajustar o modelo pré-treinado às especificidades do seu negócio/tarefa**. Em vez de treinar tudo de novo, você "afina" o modelo com um conjunto menor de dados específicos.

> [!example] Analogia
> O LLM pré-treinado é como um profissional formado e experiente em **generalidades**. O fine-tuning é o **treinamento de onboarding** que o ensina as particularidades da **sua** empresa. Muito mais barato que formar alguém do zero.

---

## 4.5. Plataformas

> [!note] HuggingFace
> Repositório/hub com milhares de **modelos LLM** prontos (GPT-2, BERT, T5…) para baixar e usar. É o "GitHub dos modelos".

> [!note] OpenAI
> - Modelos **GPT-3 e GPT-4** acessados por uma **API**, via **chave de autenticação**.
> - O uso dos modelos é **pago** (cobrado por uso/tokens), mas há opções de **trial**.

> [!tip] Conexão com o resto do curso
> A diferença prática: **HuggingFace** você costuma **rodar localmente** (modelos abertos); **OpenAI** você **chama via API** (modelos fechados, pagos). A escolha envolve custo, privacidade dos dados e qualidade — temas que reaparecem em [[../09 - Agentes de IA/00 - Índice|Agentes de IA]] e na [[../08 - LLMs e IA Generativa/00 - Índice|IA Generativa]].

---

## 4.6. Esqueleto em Python (HuggingFace)

```python
from transformers import pipeline

# fill-mask: o LLM completa a lacuna
preencher = pipeline("fill-mask", model="neuralmind/bert-base-portuguese-cased")
print(preencher("A capital do Brasil é [MASK]."))

# geração de texto
gerador = pipeline("text-generation", model="gpt2")
print(gerador("Era uma vez", max_length=30))
```

---

## 4.7. Resumo

> [!summary] O essencial dos LLMs
> - LLMs = modelos de linguagem **baseados em Transformers**, treinados em texto gigante.
> - **Open source** (GPT-2, BERT, T5) vs. **proprietário** (GPT-3, GPT-4).
> - Fazem classificação, Q&A, tradução, resumo, geração, fill-mask.
> - São **pré-treinados**; você os adapta com **fine-tuning** (mais barato que treinar do zero).
> - **HuggingFace** (modelos abertos) e **OpenAI** (API paga) são as plataformas-chave.

---

## 🔗 Próximos passos
- Fim do módulo de NLP! Siga para [[../08 - LLMs e IA Generativa/00 - Índice|LLMs e IA Generativa]], onde os LLMs viram ferramentas práticas (imagens, áudio, chat).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
