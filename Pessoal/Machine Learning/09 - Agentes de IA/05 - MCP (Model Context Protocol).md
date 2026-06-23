---
tags:
  - machine-learning
  - agentes-ia
  - mcp
  - protocolo
  - ferramentas
---

# 5. MCP (Model Context Protocol)

> [!info] O que esta nota cobre
> O **MCP (Model Context Protocol)**: um formato **padronizado** para agentes de IA conversarem com ferramentas e recursos externos. O que é, a arquitetura cliente-servidor e suas vantagens.

---

## 5.1. O que é MCP

> [!note] Definição
> **MCP (Model Context Protocol)** é um **formato de dados padronizado para a interação com LLMs** — um **protocolo** que define como um agente pede coisas a ferramentas externas e recebe respostas.

> [!example] Analogia: o "USB" dos agentes
> Antes do USB, cada aparelho tinha um conector diferente. O USB padronizou tudo. O MCP faz o mesmo para agentes: em vez de cada ferramenta ter uma integração própria e diferente, todas falam o **mesmo protocolo**. Conecte e funcione.

---

## 5.2. Arquitetura: Client e Server

```
        ┌──────────────┐        ┌──────────────┐
        │ Agente de IA │        │ Agente de IA │
        │  MCP Client  │        │  MCP Client  │
        └──────┬───────┘        └──────┬───────┘
               │      protocolo MCP     │
        ┌──────┴───────┐        ┌──────┴───────┐
        │  MCP Server   │        │  MCP Server   │
        │ (ferramenta/   │        │ (ferramenta/   │
        │  recurso)      │        │  recurso)      │
        └──────────────┘        └──────────────┘
```

> [!note] As duas pontas
> - **MCP Client:** fica do lado do **agente** — faz os pedidos.
> - **MCP Server:** expõe um **recurso/ferramenta externo** (um banco, uma API, um sistema de arquivos) de forma padronizada.
>
> Um agente pode ter **vários clients** falando com **vários servers**.

> [!example] No curso
> O curso trouxe configurações de exemplo (`MCPServer.json`, `ClienteAtendimento.json`), mostrando como declarar um servidor MCP e conectá-lo a um agente.

---

## 5.3. Vantagens

> [!summary] Por que usar MCP
> - **Comunicação padronizada** entre cliente e servidores.
> - **Abstração** entre o servidor e os recursos externos (o agente não precisa saber os detalhes internos).
> - **Independência do modelo LLM** (troca o GPT pelo Gemini sem refazer integrações).
> - **Reuso de ferramentas** (um server serve vários agentes).
> - **Escalabilidade e modularidade**.
> - **Segurança e controle** (o server controla o que é exposto).
> - **Melhor depuração**.
> - **Facilidade de integração** com frameworks de agentes (LangChain, CrewAI…).

---

## 5.4. Resumo

> [!summary] O essencial
> - **MCP** = protocolo **padronizado** para agentes acessarem ferramentas/recursos externos.
> - É o "**USB** dos agentes": conecta qualquer ferramenta de forma uniforme.
> - Arquitetura **Client (agente)** ↔ **Server (recurso)**.
> - Vantagens: padronização, independência de LLM, reuso, segurança, escalabilidade.

---

## 🔗 Próximos passos
- [[06 - Agentes e Automação Low-Code]] — construir agentes e automações **sem** programar tudo na mão.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
