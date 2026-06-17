---
tema: "O caso do agente de fluxo de trabalho para análise de riscos (n8n)"
curso: "Como Criar Agentes de IA"
fonte: "gravacao"
origem: "LinkedIn Learning — instrutor Ricardo Vargas"
data: 2026-06-17
tags: [estudo, ia, agentes-de-ia, n8n, workflow, caso-pratico]
---

# Caso n8n — O Agente de Riscos (Visão Geral)

> Em uma frase: o segundo projeto — um **agente de fluxo de trabalho** que lê e-mails, avalia riscos sozinho e atualiza o registro de riscos.

## 👋 Vamos começar
Agora entramos nos **agentes de fluxo de trabalho** (workflow agents): fluxos que
executam uma série de tarefas usando IA. A plataforma será o **n8n**. Antes de
construir, vamos desenhar a lógica no papel — entender o "o quê" antes do "como".

## 🛠️ O fluxo que vamos construir (a lógica)
Imagine que você atribuiu a um agente a missão de analisar os riscos do projeto.
O fluxo:
1. **Monitora um e-mail** (ex.: `linkedin@ricardovargas.com`).
2. **Filtro:** o assunto contém a palavra **"risk"/"risco"**? Se **não**, ignora o
   e-mail. Se **sim**, dispara o fluxo.
3. **Aciona um agente de IA** (baseado no plugin da OpenAI) que:
   - consulta um **banco de dados histórico de riscos**;
   - usa uma estrutura para **categorizar** o risco;
   - cria uma **descrição** a partir do corpo da mensagem;
   - monta uma **avaliação** estruturada (evento + impacto);
   - dá nota de **probabilidade e impacto de 1 a 5** (1 = muito baixo, 5 = muito alto).
4. **Atualiza o registro de riscos** automaticamente.
5. **Responde** a quem enviou, informando o risco registrado, probabilidade,
   impacto e o plano de resposta proposto.

> 💡 **Guarde isto:** desenhar o fluxo em linguagem clara **antes** de abrir a
> ferramenta é o que torna a construção simples depois.

---

## 🧠 Por que isso importa pra você
Este é o **agente como executor de processo**: enquanto o Manus produziu um
documento, aqui o agente roda um **processo contínuo e automático** — exatamente
o tipo de "gestão proativa de riscos" da aula 05.

## 📌 Resumo pra fixar
- Workflow agent = fluxo de tarefas encadeadas com IA, no n8n.
- Lógica: monitora e-mail → filtra "risco" → IA avalia (prob./impacto 1–5) →
  registra → responde.

## 🗝️ Palavras novas (do jeito simples)
- **[[Agente de fluxo de trabalho]]** — fluxo automatizado que executa tarefas em
  sequência usando IA.
- **[[Gatilho (trigger)]]** — o evento que inicia o fluxo (aqui, um e-mail com "risco").
- **[[Registro de riscos]]** — a planilha/documento com todos os riscos do projeto.

## ✅ Teste-se (pra enraizar)
1. **P:** O que dispara o fluxo? → **R:** Um e-mail cujo assunto contém a palavra "risco".
2. **P:** O que a IA faz com o e-mail? → **R:** Categoriza, descreve, avalia (prob./impacto 1–5) e propõe resposta.
3. **P:** Quais os 2 últimos passos? → **R:** Atualizar o registro de riscos e responder a quem enviou.

## 🔗 Para continuar
- [[09 - Caso Manus - Avaliando os Resultados]]
- [[11 - Caso n8n - Estruturando o Fluxo]]
- [[_Índice Como Criar Agentes de IA]]
