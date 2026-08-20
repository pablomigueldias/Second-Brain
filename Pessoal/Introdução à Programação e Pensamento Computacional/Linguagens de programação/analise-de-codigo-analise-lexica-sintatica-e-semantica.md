---
titulo: "Análise de Código: Análise Léxica, Sintática e Semântica"
tags: [linguagens-de-programacao, fundamentos, depuracao, pensamento-computacional, conceitos]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 6
conceitos: [Análise léxica, Tokens, Lexemas, Análise sintática, Análise semântica, Erros de semântica, Compilação]
---

# Análise de Código: Análise Léxica, Sintática e Semântica

> [!resumo] Do que se trata
> Apresenta as três fases principais de análise realizadas pelo compilador: léxica, sintática e semântica. Explica como cada etapa processa o código-fonte, desde a formação de tokens e remoção de comentários até a verificação gramatical e de significado. Destaca a natureza dos erros semânticos e por que são mais complexos de identificar e corrigir do que os erros de sintaxe.

## Para lembrar

- **A análise léxica (scanner) lê o código caractere por caractere para produzir tokens, agrupando palavras reservadas e identificadores e eliminando espaços em branco e comentários.**
- **A análise sintática verifica a forma e a estrutura gramatical do programa de acordo com as regras da linguagem de programação utilizada.**
- **A análise semântica incide sobre o significado e a lógica das instruções, como a diferença entre atribuir um valor (=) e comparar valores (== ).**
- **Erros de semântica não violam as regras gramaticais da linguagem, tornando sua identificação mais difícil e exigindo análise minuciosa da lógica linha a linha.**

## O que esta nota responde

- Quais são as três etapas de análise pelas quais o código-fonte passa durante a compilação?
- Qual é o papel da análise léxica e o que ela remove do código-fonte?
- Por que um erro de semântica é mais difícil de identificar do que um erro de sintaxe?

## Conceitos

**Análise léxica** · **Tokens** · **Lexemas** · **Análise sintática** · **Análise semântica** · **Erros de semântica** · **Compilação**

## Conteúdo

`⏱ 00:00`

Muito bem. Agora vamos falar sobre como o computador analisa o nosso código.

Primeiramente, estou voltando uma imagem que já tinha colocado antes. Nessa fase, em que o nosso código-fonte vai para o compilador, existem três tipos de análises que ele faz:

1.  A análise léxica, ou *lexical analyzer*.
2.  A análise sintática, ou *syntax analyzer*.
3.  A análise semântica, ou *semantic analyzer*.

Vamos entender o que seria essa primeira etapa, que é a análise léxica.

### Análise Léxica (Lexical Analysis)

Ela também é conhecida como *scanner* ou leitura. É a primeira fase do processo de compilação.

A função dela é fazer a leitura do programa-fonte, caractere por caractere, letra por letra, e agrupar os caracteres em lexemas. O objetivo é produzir uma sequência de símbolos léxicos, conhecidos como *tokens*.

Nesse processo, ela vai particionar, classificar e eliminar aquilo que não é necessário. Ao particionar, ela vai identificar os elementos, os lexos, que são os *tokens*, e vai agrupá-los.

Esses elementos incluem:
- Identificadores;
- Palavras reservadas;
- Números;
- *Strings*;
- Todo o conteúdo que é relevante para a codificação do nosso programa.

Ela vai eliminar caracteres em branco e comentários. Esses são coisas que a gente acaba utilizando nos comandos para nosso melhor entendimento dentro do programa, mas o compilador não precisa daquilo. Portanto, nessa análise léxica do programa-fonte, essa parte é retirada.

### Análise Sintática (Syntax Analysis)

Entramos na análise sintática. O que "sintaxe" remete é a forma. A sintaxe é o componente do sistema linguístico que interliga os constituintes da sentença, atribuindo-lhe uma estrutura.

A sintaxe de um programa é a forma que ele define através de palavras reservadas e de indexação de símbolos especiais, qual é a estrutura relacionada para codificação dentro daquela linguagem específica. Ela define, portanto, a análise que define a corretude do programa.

Se verificarmos a parte de padrão gramática, veremos que ela depende da linguagem de programação utilizada. Como exemplifiquei, para cada linguagem de programação, haverá uma sintaxe associada.

### Análise Semântica (Semantic Analysis)

A semântica está relacionada ao significado.

Por exemplo, sintaticamente, o `=` e o `==` estão corretos, mas possuem significados chamados distintos.

A análise semântica de um programa está relacionada ao estudo do significado. Incide sobre a relação entre significantes — como palavras, frases, sinais e símbolos — e a lógica do programa.

Podemos olhar esse exemplozinho e perguntar: tem algum erro nesse pedacinho de código?

Sintaticamente, não é erro, porque o `=` é válido, não é um erro de sintaxe. Contudo, ele não faz o que é esperado. Existe, portanto, um erro de semântica, um erro de significado.

Se a gente colocar o operador correto, ou seja, `if x == 0` e não `if x = 0` (apenas um sinal de igual), significa atribuição e não comparação. A gente não tem erro nessa parte de cima, no verde.

Se fizermos `fixe = 0` (onde o valor é nulo), é só uma comparação. Já `fixe = 0` vai dar erro se o programa não retornar aquilo que é esperado dele.

Mas ele não torna um erro de sintaxe. Um erro de semântica é bem mais complicado de se encontrar do que o erro de sintaxe.

`⏱ 05:20`

### Identificando Erros de Semântica

[O trecho parece estar descrevendo um problema de programação.]

Há um erro aqui, um erro de semântica que está relacionado à lógica do seu programa.

Para resolver isso, você vai ter que destrinchar, divulgar e entender o que você fez, linha a linha, às vezes, para conseguir encontrar o erro de semântica.

## Relacionado

- [[processamento-de-codigo-compilacao-interpretacao-e-transpilacao]]
- [[caracteristicas-de-um-programa-de-software-legibilidade-redigibilidade-confiabil]]
- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
- [[Processos de Software]]
