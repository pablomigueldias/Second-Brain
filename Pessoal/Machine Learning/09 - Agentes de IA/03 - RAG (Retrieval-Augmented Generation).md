---
tags:
  - machine-learning
  - agentes-ia
  - rag
  - llm
  - vector-store
---

# 3. RAG (Retrieval-Augmented Generation)

> [!info] O que esta nota cobre
> A técnica **RAG**: como dar ao LLM acesso a **documentos específicos** (contratos, manuais, políticas) **antes** de gerar a resposta — resolvendo o problema de o modelo "não conhecer" os dados da sua empresa.

---

## 3.1. O problema que o RAG resolve

> [!warning] LLMs não conhecem os SEUS dados
> Um LLM foi treinado com texto geral da internet. Ele **não conhece** o seu contrato específico, o manual do seu produto, as normas internas da sua empresa — e, se perguntado, pode **alucinar** uma resposta. O RAG resolve isso.

---

## 3.2. O que é RAG

> [!note] Definição
> **RAG (Retrieval-Augmented Generation)** = uma técnica que melhora a geração de texto **adicionando uma fase de recuperação de informações antes de gerar a resposta**.

> [!important] As duas partes do nome
> - **Retrieval (Recuperação):** busca os **documentos relevantes** numa base de conhecimento.
> - **Generation (Geração):** usa um **LLM** para responder **com base nos documentos recuperados**.

```
   Pergunta → [Retrieval] busca docs relevantes → [Generation] LLM responde
                    ▲                                  usando os docs
              base de conhecimento
              (vector store)
```

> [!example] Analogia
> É a diferença entre um aluno respondendo **de cabeça** (pode chutar) e um aluno fazendo uma prova **com consulta**: ele primeiro **procura** a informação no material e **depois** responde com base nela. Muito mais confiável.

---

## 3.3. Onde RAG é útil (exemplos do curso)

> [!summary] Casos de uso
> - Clientes perguntam sobre **contratos, faturas, planos, produtos**.
> - Profissionais precisam interpretar **contratos, leis ou políticas internas**.
> - **Normas tributárias** que mudam constantemente e variam por região/setor.
> - **Novos colaboradores** com dúvidas sobre processos internos.
> - **Suporte técnico** para problemas recorrentes.
> - Executivos/analistas que querem **dados específicos** que mudam com frequência.

> [!tip] O fio comum
> RAG brilha quando a resposta depende de **informação específica, que muda** e que o LLM **não tem como saber sozinho**. Em vez de re-treinar o modelo (caro), você só **atualiza os documentos** da base.

---

## 3.4. Como funciona por dentro (visão geral)

> [!note] O fluxo típico
> 1. Os documentos são quebrados em pedaços e convertidos em **embeddings** ([[../07 - Processamento de Linguagem Natural (NLP)/03 - Word Embeddings e Transformers|vetores]]).
> 2. Esses vetores ficam guardados num **[[04 - Vector Stores e Orquestração de LLMs|Vector Store]]**.
> 3. Quando chega uma pergunta, ela também vira vetor e busca-se os **trechos mais similares**.
> 4. Esses trechos são enviados ao **LLM** junto com a pergunta → o LLM responde **fundamentado** neles.

> [!example] O exemplo do curso
> O curso construiu um **Agente RAG especializado** (`AgenteRAGEspecializado.ipynb`) usando o **manual técnico de um nobreak (FXP-2000)** como base de conhecimento. O agente respondia perguntas como "qual a autonomia?" ou "como trocar a bateria?" buscando no manual — em vez de inventar.

---

## 3.5. Resumo

> [!summary] O essencial do RAG
> - Resolve a limitação de o LLM **não conhecer seus documentos** (e evitar alucinação).
> - **Retrieval** (busca docs relevantes) + **Generation** (LLM responde com base neles).
> - Ideal para informação **específica e que muda** (contratos, leis, manuais, FAQs).
> - Atualizar o conhecimento = atualizar os **documentos**, sem re-treinar o modelo.

---

## 🔗 Próximos passos
- [[04 - Vector Stores e Orquestração de LLMs]] — a infraestrutura que faz o RAG funcionar.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
