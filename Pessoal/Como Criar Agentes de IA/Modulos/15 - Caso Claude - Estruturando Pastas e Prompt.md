---
tema: "Estruturando as pastas e o prompt do Claude Cowork"
curso: "Como Criar Agentes de IA"
fonte: "gravacao"
origem: "LinkedIn Learning — instrutor Ricardo Vargas"
data: 2026-06-17
tags: [estudo, ia, agentes-de-ia, claude, prompt, caso-pratico]
---

# Caso Claude — Estruturando as Pastas e o Prompt

> Em uma frase: você vai preparar o Claude Cowork para organizar o caos — com um prompt que pede análise antes da ação.

## 👋 Vamos começar
Vamos colocar o **Claude Cowork** para resolver a bagunça do Phoenix. O segredo
está num **prompt bem pensado**: primeiro analisar e confirmar, só depois agir.

## 🛠️ Passo a passo
1. **Contextualize.** Os dois primeiros parágrafos do prompt resumem a história:
   recém-designado gerente, herdou informação caótica de muita gente.
2. **Peça um diagnóstico primeiro.** Instrua: "examine a pasta e me mostre um
   resumo (total de arquivos, intervalo de datas, tipos de conteúdo)".
3. **Peça que o agente faça perguntas antes de analisar.** O que você espera
   descobrir? Algum arquivo deve ser priorizado? Qual o formato mais útil da
   análise final?
4. **Defina regras de escopo.** "Se houver mais de 20 arquivos (e há), comece
   pelos **10 mais recentes**. Mostre os **3 a 5 principais padrões** que
   encontrar (problemas, conflitos) com 2–3 exemplos de cada."
5. **Crie um checkpoint humano.** "**Depois que eu confirmar** que você está no
   caminho certo, faça o restante." → você aprova antes da ação em massa.
6. **Defina o resultado.** Organize a pasta criando duas subpastas: **"versão
   oficial"** (o que vale) e **"delete"** (o que descartar).
7. **Aponte a pasta de trabalho e autorize o acesso.** No Cowork, abra a aba
   "Co-work", cole o prompt, escolha a pasta (Project Phoenix) e **autorize** o
   Claude a acessá-la ("sempre permitir").

> 💡 **Guarde isto:** o padrão **"analise → me pergunte → mostre os achados →
> espere eu confirmar → então execute"** mantém você no controle de uma ação
> arriscada (mexer em 100+ arquivos). É o uso prático dos **guardrails**.

---

## 🧠 Por que isso importa pra você
Quando a ação é destrutiva (organizar/apagar arquivos), o prompt precisa de
**checkpoints de aprovação**. Esse desenho de prompt vale para qualquer tarefa em
que o erro custa caro.

## 📌 Resumo pra fixar
- Prompt em fases: contexto → diagnóstico → perguntas → regras de escopo →
  checkpoint humano → resultado (pastas "oficial" e "delete").
- Aponte a pasta e autorize o acesso do agente.

## 🗝️ Palavras novas (do jeito simples)
- **[[Claude Cowork]]** — modo do Claude para trabalhar sobre seus arquivos/pastas.
- **[[Checkpoint humano]]** — ponto onde o agente para e espera sua aprovação.
- **[[Permissão de acesso]]** — autorização para o agente ler/alterar suas pastas.

## ✅ Teste-se (pra enraizar)
1. **P:** Por que pedir diagnóstico e perguntas antes da ação? → **R:** Para confirmar a direção e manter controle antes de mexer em 100+ arquivos.
2. **P:** Quais as duas subpastas de saída? → **R:** "Versão oficial" e "delete".
3. **P:** O que é o checkpoint humano no prompt? → **R:** A instrução de só executar a ação em massa depois da sua confirmação.

## 🔗 Para continuar
- [[14 - Caso Claude - Dados Caóticos]]
- [[16 - Caso Claude - Fonte Única de Verdade]]
- [[_Índice Como Criar Agentes de IA]]
