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

## Passo 2 — Entender e estruturar

Leia a transcrição inteira. A transcrição é fala corrida, com erros de Whisper,
sem pontuação ideal. Seu trabalho:

1. **Corrigir** termos técnicos mal transcritos pelo contexto (ex.: "fast api",
   "pái dent" → Pydantic, "tai pinte" → type hint).
2. **Identificar a estrutura lógica**: divida o conteúdo em **Módulos** (grandes
   blocos) e, dentro deles, **Tópicos** (`##`) e subtópicos (`###`).
3. **Não copie a fala** — reescreva como material de estudo claro e didático,
   em português, na 2ª pessoa quando fizer sentido ("você define…").
4. Preserve **exemplos de código** que apareçam (formate em blocos ```` ```lang ````).
   Se o conteúdo for de programação e o autor descreveu código, reconstrua um
   exemplo mínimo coerente e marque-o como exemplo reconstruído.

## Passo 3 — Escolher onde salvar

- Decida a matéria a partir do `tema`/conteúdo e mapeie para uma pasta existente
  em `Pessoal/` (ex.: FastAPI, Machine Learning, Bancos de Dados, Engenharia de
  Software…). Se nenhuma servir, crie `Pessoal/<Matéria>/`.
- Nome do arquivo = o tema, em Title Case legível (ex.: `Async e Await no FastAPI.md`).
- **Antes de escrever, verifique se já existe nota parecida** nessa pasta. Se
  existir, prefira **complementar/atualizar** a existente a duplicar — pergunte ao
  Pablo se a fusão não for óbvia.

## Passo 4 — Escrever a nota

Use o template em `Pessoal/_Sistema-Estudos/_template-modulo.md` como base
(é o estilo dos módulos que o Pablo já mantém). A nota DEVE conter:

- **Frontmatter** com `tema`, `fonte`, `origem`, `data`, `tags`.
- **🎯 Objetivos de aprendizagem** (3–6 itens, checkbox).
- **📚 Conteúdo por módulos/tópicos** — o miolo didático, com `##`/`###`.
- **💡 Resumo / ideias-chave** — bullets curtos do essencial.
- **📖 Vocabulário** — termos técnicos com definição curta; use `[[Wikilinks]]`
  para conceitos que merecem nota própria (mesmo que ainda não existam).
- **❓ Perguntas para revisão (flashcards)** — 5–10 pares pergunta→resposta, para
  o Pablo relembrar depois.
- **🔗 Notas relacionadas** — `[[Wikilinks]]` para notas existentes no vault que
  tenham relação (verifique antes quais existem).

Tom: **didático, direto, sem encher linguiça**. Quem lê deve conseguir reaprender
o assunto só com a nota.

## Passo 5 — Fechar o ciclo

1. Salve a nota no lugar escolhido.
2. Edite o frontmatter do arquivo do `_inbox`: troque `status: bruto` por
   `status: processado` e adicione `nota: "<caminho da nota gerada>"`.
   (Assim ele não é reprocessado, mas fica o rastro. O Pablo pode apagar depois.)
3. No final, me diga em 2–3 linhas: onde salvei, quantos módulos/tópicos, e
   quais `[[links]]` novos ficaram pendentes de criar.
