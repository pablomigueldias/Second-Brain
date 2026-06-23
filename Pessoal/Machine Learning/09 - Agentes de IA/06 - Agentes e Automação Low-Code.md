---
tags:
  - machine-learning
  - agentes-ia
  - low-code
  - no-code
  - n8n
  - automação
---

# 6. Agentes e Automação Low-Code

> [!info] O que esta nota cobre
> Como construir **agentes e automações** sem escrever todo o código na mão, usando ferramentas **low-code / no-code** como **n8n**, **Zapier** e **Bubble**.

---

## 6.1. Low-Code / No-Code

> [!note] Definição
> - **No-Code:** construir aplicações/automações **sem escrever código** — arrastando e conectando blocos visuais.
> - **Low-Code:** **pouco** código — a maior parte é visual, com encaixes de script onde necessário.

> [!important] Por que isso importa para agentes
> Montar um agente "na unha" (LangChain + vector store + APIs) dá controle total, mas dá trabalho. Ferramentas low-code permitem **prototipar e operar agentes rapidamente**, conectando LLMs a centenas de serviços com blocos prontos.

---

## 6.2. As ferramentas

| Ferramenta | Foco |
|---|---|
| **Bubble** | Construir **aplicações web** completas sem código. |
| **n8n** | **Automação de fluxos** (open source); ótimo para orquestrar agentes e integrações. |
| **Zapier** | **Automação** conectando milhares de apps (SaaS). |

> [!tip] Conexão com o resto do seu vault
> Essas mesmas ferramentas aparecem no curso [[../../Criar valor com IA, automação e bots/Modulos/02 - Automatize o Seu Caminho Através do Caos|Criar valor com IA, automação e bots]] (Zapier) e no curso [[../../Como Criar Agentes de IA/_Índice Como Criar Agentes de IA|Como Criar Agentes de IA]] (n8n). É o ponto onde **agentes** e **automação no-code** se encontram.

---

## 6.3. O caminho típico de um agente low-code

> [!example] Como costuma ser montado
> 1. Um **gatilho** inicia o fluxo (mensagem recebida, novo registro, horário).
> 2. Um nó chama o **LLM** (via API) para interpretar/decidir.
> 3. Conforme a decisão, o fluxo chama **ferramentas** (buscar no banco, enviar e-mail, atualizar planilha) — possivelmente via **[[05 - MCP (Model Context Protocol)|MCP]]**.
> 4. O agente responde e, se necessário, **mantém o contexto** para a próxima interação.

> [!note] No próximo conteúdo do curso
> O curso indica como evolução: construir um **agente autônomo com IA e LLMs** usando **n8n** + **MCP** — unindo tudo o que foi visto neste módulo (LLM, RAG, ferramentas, protocolo) num fluxo low-code.

---

## 6.4. Quando programar vs. usar low-code

> [!summary] O trade-off
> | Use low-code quando... | Programe quando... |
> |---|---|
> | Quer **prototipar rápido** | Precisa de **controle fino**/customização |
> | Integrações **já existem** prontas | A integração necessária **não existe** |
> | Volume **baixo/médio** | Volume **altíssimo** (custo por uso pesa) |

---

## 6.5. Resumo

> [!summary] O essencial
> - **No-code/low-code** = montar agentes e automações com **blocos visuais**, com pouco ou nenhum código.
> - Ferramentas: **Bubble** (apps), **n8n** (fluxos, open source), **Zapier** (integrações).
> - Caminho do agente: **gatilho → LLM decide → ferramentas (MCP/APIs) → resposta + contexto**.
> - Low-code para velocidade; código para controle/escala.

---

## 🔗 Próximos passos
- Fim do módulo de Agentes! Volte ao [[00 - Índice]] ou siga para [[../10 - Detecção de Anomalias/00 - Índice|Detecção de Anomalias]].

---
[[00 - Índice|⬅️ Voltar ao Índice]]
