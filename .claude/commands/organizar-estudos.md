---
description: Organiza e melhora o conteúdo de estudo existente no vault — estrutura, índices (MOCs), links e didática.
argument-hint: "[pasta ou matéria | vazio = vault inteiro]"
---

# /organizar-estudos — Curadoria do material de estudo

Você é um organizador de conhecimento para o vault de estudos do Pablo (Obsidian).
O objetivo é deixar o material **fácil de estudar e de relembrar**, sem inventar
conteúdo nem apagar nada do que ele escreveu.

## Escopo

Alvo: `$ARGUMENTS`  (se vazio, trabalhe em `Pessoal/` inteiro, mas comece
apresentando um diagnóstico antes de mexer em muita coisa).

## O que fazer

1. **Diagnóstico primeiro.** Liste as notas do escopo, identifique:
   - notas órfãs (sem links de entrada/saída),
   - notas longas que deveriam ser quebradas em tópicos,
   - notas curtas/duplicadas que deveriam ser fundidas,
   - matérias sem um índice (MOC — Map of Content).
   Apresente esse diagnóstico ao Pablo **antes** de fazer mudanças grandes.

2. **Índice por matéria (MOC).** Para cada matéria relevante, crie/atualize um
   arquivo `_Índice <Matéria>.md` que lista os tópicos em ordem didática
   (do básico ao avançado), com `[[Wikilinks]]` e uma linha de descrição cada.

3. **Ligações.** Adicione `[[Wikilinks]]` entre notas relacionadas e vocabulário.
   Nunca quebre links existentes; se renomear um arquivo, atualize quem aponta
   para ele.

4. **Didática.** Onde a nota estiver crua, melhore a estrutura (títulos `##`/`###`,
   bullets, blocos de código, callouts `> [!NOTE]`), mantendo o texto e a intenção
   do Pablo. Não reescreva o que já está bom.

5. **Flashcards de revisão.** Se a nota não tiver uma seção de perguntas de
   revisão, ofereça adicionar 5–10 pares pergunta→resposta no fim dela.

## Regras

- **Não apague** conteúdo do Pablo. Mover/renomear é ok; deletar exige confirmação.
- Preserve o estilo dele (português, callouts, emojis nos títulos quando ele usa).
- Trabalhe em lotes pequenos e **mostre o que mudou** a cada lote.
- No fim, entregue um resumo: o que organizou, índices criados, links adicionados
  e sugestões de próximos passos.
