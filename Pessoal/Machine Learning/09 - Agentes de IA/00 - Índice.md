---
tags:
  - machine-learning
  - moc
  - índice
  - agentes-ia
  - rag
  - mcp
aliases:
  - Agentes de IA
---

# Agentes de IA

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do módulo **9 — Agentes de IA**. Um agente vai além de responder: ele **percebe, raciocina, age e aprende**. Aqui vemos os tipos de agente, a técnica **RAG** (dar memória de documentos ao LLM), **vector stores**, o protocolo **MCP** e automação **low-code**.

---

## Roteiro de Estudo

- [[01 - O que é um Agente de IA]] — Percepção, raciocínio, ação e adaptação.
- [[02 - Tipos de Agentes]] — Reativos, autônomos, baseados em modelo/objetivo/utilidade, com aprendizado e multiagente.
- [[03 - RAG (Retrieval-Augmented Generation)]] — Como dar ao LLM acesso a documentos específicos antes de responder.
- [[04 - Vector Stores e Orquestração de LLMs]] — Bancos vetoriais (FAISS, Pinecone, Chroma) e frameworks (LangChain, CrewAI).
- [[05 - MCP (Model Context Protocol)]] — O "protocolo universal" para conectar agentes a ferramentas.
- [[06 - Agentes e Automação Low-Code]] — Construir agentes sem código pesado (n8n, Zapier, Bubble).

---

## Visão Geral em uma Imagem Mental

```
                    AGENTE DE IA
         (percebe → raciocina → age → aprende)
                         │
          ┌──────────────┼───────────────┐
        LLM            RAG              Ferramentas
      (cérebro)   (memória de docs)    (via MCP / APIs)
                         │
                   Vector Store
                  (FAISS, Pinecone)
```

---

## 🏷️ Tags Relacionadas
#machine-learning #agentes-ia #rag #mcp #llm #estudos

---
[[_Índice Machine Learning|⬅️ Voltar ao Índice do Curso]]
