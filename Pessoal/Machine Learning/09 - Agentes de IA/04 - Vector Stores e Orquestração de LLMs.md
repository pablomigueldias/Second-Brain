---
tags:
  - machine-learning
  - agentes-ia
  - vector-store
  - langchain
  - embeddings
---

# 4. Vector Stores e Orquestração de LLMs

> [!info] O que esta nota cobre
> A infraestrutura por trás de agentes e RAG: **Vector Stores** (bancos de dados vetoriais que guardam embeddings) e **frameworks de orquestração** de LLMs (LangChain, CrewAI e cia.).

---

## 4.1. Vector Store (Banco de Dados Vetorial)

> [!note] Definição
> Um **Vector Store** é um **banco de dados para vetores numéricos**. Ele **armazena embeddings** e, principalmente, **facilita buscas de vetores semelhantes**.

> [!important] Por que não um banco comum?
> Um banco SQL tradicional busca por **igualdade** ("WHERE nome = 'João'"). Um vector store busca por **similaridade** ("quais textos têm significado parecido com esta pergunta?"). É exatamente o que o [[03 - RAG (Retrieval-Augmented Generation)|RAG]] precisa na fase de *retrieval*.

> [!example] Como funciona
> Você guarda os embeddings dos seus documentos. Quando chega uma pergunta (também virada vetor), o vector store retorna **os vetores mais próximos** (por similaridade de cosseno). Esses são os trechos mais relevantes.

### Opções de banco vetorial

| Ferramenta | Característica |
|---|---|
| **Pinecone** | Serviço gerenciado (na nuvem). |
| **Chroma** | Open source, simples de usar localmente. |
| **FAISS** | Biblioteca do Facebook, muito rápida; roda local. |

> [!tip] No curso
> O **Agente RAG especializado** usou o **FAISS** como vector store — leve e rápido para rodar localmente.

---

## 4.2. Orquestração de LLMs

> [!note] O que é orquestrar
> Construir um agente envolve **coordenar várias peças**: o LLM, o vector store, as ferramentas externas, a memória da conversa. Os **frameworks de orquestração** existem para colar tudo isso de forma organizada.

### Frameworks

| Framework | Para que serve |
|---|---|
| **LangChain** | O mais popular; encadeia LLMs, memória, ferramentas e RAG. |
| **Haystack** | Focado em busca/Q&A sobre documentos. |
| **Semantic Kernel** | Orquestração da Microsoft. |
| **CrewAI** | Coordena **múltiplos agentes** trabalhando juntos (equipes de agentes). |

> [!example] No curso
> O agente RAG foi montado com **LangChain** + **FAISS** + **OpenAI** — um trio clássico: LangChain orquestra, FAISS guarda os vetores, OpenAI fornece o LLM.

---

## 4.3. Como as peças se encaixam

```
   ┌─────────────────────────────────────────┐
   │           LangChain (orquestra)          │
   │   ┌──────────┐  ┌──────────┐  ┌────────┐ │
   │   │   LLM     │  │  FAISS    │  │ Memória│ │
   │   │ (OpenAI)  │  │ (vetores) │  │ sessão │ │
   │   └──────────┘  └──────────┘  └────────┘ │
   └─────────────────────────────────────────┘
```

> [!summary] A divisão de trabalho
> - **LLM** = o cérebro que raciocina e gera texto.
> - **Vector Store (FAISS)** = a memória de documentos (RAG).
> - **Framework (LangChain)** = o maestro que coordena tudo.
> - **Memória de sessão** = mantém o contexto da conversa.

---

## 4.4. Resumo

> [!summary] O essencial
> - **Vector Store** = banco que guarda **embeddings** e busca por **similaridade** (base do RAG).
> - Opções: **Pinecone** (serviço), **Chroma**, **FAISS** (locais).
> - **Orquestração** = colar LLM + vetores + ferramentas + memória.
> - Frameworks: **LangChain** (popular), Haystack, Semantic Kernel, **CrewAI** (multiagente).

---

## 🔗 Próximos passos
- [[05 - MCP (Model Context Protocol)]] — um protocolo padrão para conectar agentes a ferramentas externas.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
