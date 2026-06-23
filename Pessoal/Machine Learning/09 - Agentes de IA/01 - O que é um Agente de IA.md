---
tags:
  - machine-learning
  - agentes-ia
  - fundamentos
---

# 1. O que é um Agente de IA

> [!info] O que esta nota cobre
> A definição de **agente de IA** e suas quatro capacidades fundamentais: **percepção, raciocínio, ação e aprendizado/adaptação**. E as formas pelas quais um agente "aparece" no mundo.

---

## 1.1. Definição

> [!note] O que é um agente
> Um **Agente de IA** é um sistema que **percebe o ambiente, processa informações, toma decisões e age de forma autônoma**.

> [!important] A diferença para um chatbot/LLM comum
> Um LLM "puro" só **responde** ao que você pergunta. Um **agente** vai além: ele **decide o que fazer** e **executa ações** no mundo para alcançar um objetivo — com mínima ou nenhuma intervenção humana.

---

## 1.2. As quatro capacidades

```
   AMBIENTE
      │  (1) percebe
      ▼
   [ PERCEPÇÃO ] → [ RACIOCÍNIO ] → [ AÇÃO ] → afeta o ambiente
                         ▲                │
                         └─ [ APRENDIZADO ] ◄┘
                            (mantém contexto, aprende com o passado)
```

> [!summary] O ciclo do agente
> 1. **Percepção** — tem um **entendimento do ambiente** (lê dados, mensagens, estado).
> 2. **Raciocínio** — **toma decisões** com base no que percebeu.
> 3. **Ação** — é **capaz de executar tarefas** (não só falar).
> 4. **Aprendizado e Adaptação** — **mantém contexto e aprende com o passado** (integração contínua).

> [!example] Exemplo intuitivo
> Um agente de atendimento não só responde "seu pedido está a caminho" — ele **consulta o sistema** (percepção), **decide** se cabe reembolso (raciocínio), **emite o reembolso** via API (ação) e **lembra** do histórico do cliente nas próximas interações (aprendizado).

---

## 1.3. Como um agente "se materializa"

> [!note] Formas de interface
> Um agente pode operar/ser acessado através de:
> - **API**
> - **Linha de comando**
> - **Aplicação desktop**
> - **Chatbot**
> - **RPA** (*Robotic Process Automation* — automação que imita cliques/ações de usuário)

---

## 1.4. Resumo

> [!summary] O essencial
> - Agente = sistema que **percebe, raciocina, age e aprende** de forma autônoma.
> - Diferença-chave: ele **executa ações**, não apenas responde.
> - Quatro capacidades: **percepção → raciocínio → ação → aprendizado**.
> - Materializa-se via API, CLI, desktop, chatbot ou RPA.

---

## 🔗 Próximos passos
- [[02 - Tipos de Agentes]] — dos mais simples (reativos) aos mais sofisticados (com aprendizado e multiagente).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
