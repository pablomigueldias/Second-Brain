---
description: Transforma uma transcrição bruta do _inbox numa nota de estudo didática, organizada por módulos e tópicos.
argument-hint: "[nome-do-arquivo no _inbox | vazio = mais recente]"
---

# /nota-video — Gerar nota de estudo a partir de uma transcrição

Você vai transformar uma **transcrição bruta** (gerada pelo `estudo.py`) numa
**nota de estudo completa, didática e organizada por módulos/tópicos**, no estilo
que o Pablo já usa no vault.

## Passo 1 — Achar a transcrição

O argumento passado foi: `$ARGUMENTS`

- Se houver um nome de arquivo, use `Pessoal/_Sistema-Estudos/_inbox/<arquivo>`.
- Se estiver vazio, liste `Pessoal/_Sistema-Estudos/_inbox/*.md`, pegue o de
  `status: bruto` **mais recente** (pelo timestamp no nome) e use esse.
- Leia o frontmatter (`tema`, `fonte`, `origem`, `data`) e o corpo (texto bruto).

## Passo 2 — Entender e ENSINAR (estilo "professor")

Leia a transcrição inteira. Ela é fala corrida, com erros de transcrição e sem
pontuação ideal. **Corrija os termos silenciosamente** — nunca mencione que houve
erro de transcrição, nem cite "Whisper", "o áudio saiu como…", etc. A nota deve
parecer escrita por um professor, não por um corretor.

Seu papel é **dar uma aula escrita** ao Pablo, não resumir o vídeo:

1. **Voz de professor, 2ª pessoa, calorosa e didática.** Explique como se estivesse
   ensinando pessoalmente: "vamos entender…", "pense nisso como…", "na prática…".
2. **Ensine de verdade.** Quando aparecer um termo ou conceito (ex.: agente de IA,
   pipeline, orquestração), **pare e explique** com palavras simples, analogia e
   exemplo — mesmo que o vídeo tenha passado rápido. O objetivo é o Pablo
   **aprender coisas novas** e **enraizar** o aprendizado, não só registrar.
3. **Não copie a fala.** Reescreva como material de aprendizado claro, do simples
   ao detalhado, conectando os conceitos entre si.
4. **Seja fiel aos fatos do vídeo.** Pode enriquecer com explicação geral de
   conceitos (isso é ensinar), mas não invente fatos específicos do curso.
5. Preserve **exemplos de código** (em blocos ```` ```lang ````). Se o autor
   descreveu código, reconstrua um exemplo mínimo coerente.

## Passo 3 — Escolher onde salvar

**Caso A — a transcrição TEM o campo `curso` no frontmatter** (várias partes do
mesmo curso, gravadas aos poucos):

- A pasta-base é `Pessoal/<Curso>/`. Crie se não existir, com a subpasta
  `Pessoal/<Curso>/Modulos/`.
- Cada parte vira um arquivo de módulo numerado em ordem de chegada:
  `Modulos/NN - <tema>.md` (ex.: `01 - Introdução.md`, `02 - Variáveis.md`).
  Descubra o próximo `NN` olhando os arquivos já existentes em `Modulos/`.
- Crie/atualize o índice do curso `Pessoal/<Curso>/_Índice <Curso>.md`: uma lista
  ordenada com `[[link]]` para cada módulo e uma linha de descrição. Atualize-o
  toda vez que um novo módulo entrar.
- Assim, conforme você manda intro, módulo 1, 2… tudo fica agrupado e em ordem.

**Caso B — sem `curso`** (vídeo avulso):

- Decida a matéria a partir do `tema`/conteúdo e mapeie para uma pasta existente
  em `Pessoal/` (ex.: FastAPI, Machine Learning, Bancos de Dados, Engenharia de
  Software…). Se nenhuma servir, crie `Pessoal/<Matéria>/`.
- Nome do arquivo = o tema, em Title Case legível (ex.: `Async e Await no FastAPI.md`).

**Em ambos os casos:** antes de escrever, **verifique se já existe nota parecida**
na pasta. Se existir, prefira **complementar/atualizar** a existente a duplicar —
pergunte ao Pablo se a fusão não for óbvia.

## Passo 4 — Escrever a nota

Use o template em `Pessoal/_Sistema-Estudos/_template-modulo.md` como base — é
uma **aula escrita**, em voz de professor. A nota DEVE conter:

- **Frontmatter** com `tema`, `curso` (se houver), `fonte`, `origem`, `data`, `tags`.
- **👋 Abertura** curta e acolhedora, dizendo o que o Pablo vai aprender.
- **📖 Explicação passo a passo** (`##`/`###`) — o coração: ensine cada conceito
  com analogia + exemplo, parando para explicar termos novos. Use callouts
  `> 💡 **Guarde isto:**` e `> [!TIP] Na prática` para destacar o que fixar.
- **🧠 Por que isso importa pra você** — conecta com o objetivo/uso real.
- **📌 Resumo pra fixar** — bullets curtos do essencial.
- **🗝️ Palavras novas** — termos explicados de forma simples; use `[[Wikilinks]]`
  para conceitos que merecem nota própria (mesmo que ainda não existam).
- **✅ Teste-se** — 5–10 pares pergunta→resposta para enraizar o aprendizado.
- **🔗 Para continuar** — `[[Wikilinks]]` para aulas/notas relacionadas (verifique
  antes quais existem).

Tom: **um bom professor explicando com calma e clareza** — caloroso, em 2ª pessoa,
do simples ao detalhado. Quem lê deve conseguir aprender o assunto só com a nota.

## Passo 5 — Fechar o ciclo

1. Salve a nota no lugar escolhido.
2. Edite o frontmatter do arquivo do `_inbox`: troque `status: bruto` por
   `status: processado` e adicione `nota: "<caminho da nota gerada>"`.
   (Assim ele não é reprocessado, mas fica o rastro. O Pablo pode apagar depois.)
3. No final, me diga em 2–3 linhas: onde salvei, quantos módulos/tópicos, e
   quais `[[links]]` novos ficaram pendentes de criar.
