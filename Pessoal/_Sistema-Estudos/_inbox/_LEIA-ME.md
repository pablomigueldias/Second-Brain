---
tema: "Como funciona o _inbox"
tags: [sistema, organizacao]
---

# Como funciona este _inbox

Este é o ponto de entrada das transcrições geradas pelo `estudo.py`.

## Convenção de organização

- **Topo do `_inbox/` (arquivos soltos)** → transcrições **pendentes** (`status: bruto`).
  É o que ainda falta virar nota de estudo. Se há arquivo aqui, há trabalho a fazer.
  É exatamente onde o `estudo.py` grava cada nova transcrição e onde o `/nota-video`
  procura o que processar.

- **`_processado/<Curso>/`** → transcrições **já processadas** (`status: processado`),
  arquivadas por curso/tópico. Não são reprocessadas (o `/nota-video` só olha o topo
  do `_inbox`). Cada arquivo tem no frontmatter o campo `nota:` apontando para a aula
  gerada. Pode apagar quando quiser — é só rastro.

## Fluxo

1. `estudo.py` grava a transcrição **bruta** no topo do `_inbox/`.
2. Você roda `/nota-video` → ele gera a nota de estudo na pasta do curso.
3. A transcrição é marcada `processado` e movida para `_processado/<Curso>/`.

> Em resumo: **topo limpo = nada pendente.** O que estiver solto aqui é o que
> falta estudar; o resto está arquivado e organizado por curso.

## Cursos arquivados
- `_processado/Como Criar Agentes de IA/`
- `_processado/Criar valor com IA, automação e bots/`
