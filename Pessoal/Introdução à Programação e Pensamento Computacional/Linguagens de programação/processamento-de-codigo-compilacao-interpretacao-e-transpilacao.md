---
titulo: "Processamento de Código: Compilação, Interpretação e Transpilação"
tags: [linguagens-de-programacao, pensamento-computacional, conceitos, algoritmos, estudos]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 5
conceitos: [Código-fonte, Linguagem de alto nível, Compilador, Programa objeto, Interpretação, Transpilação, Análise léxica, Análise sintática]
---

# Processamento de Código: Compilação, Interpretação e Transpilação

> [!resumo] Do que se trata
> A nota explica como um computador processa um programa de alto nível, detalhando o processo de tradução que é essencial para a execução. São abordados os métodos de compilação, onde o código é traduzido para um programa objeto de baixo nível, e a interpretação, onde o código-fonte é executado diretamente. Por fim, é apresentada a transpilação, um processo de tradução entre linguagens de alto nível de diferentes níveis.

## Para lembrar

- **Para que o computador entenda um programa, é necessário um processo de tradução, pois ele não consegue entender instruções de alto nível com semântica e sintaxe específicas.**
- **Na compilação, a linguagem de alto nível é enviada ao compilador, que realiza análises léxica, sintática e semântica, e gera um programa objeto de baixo nível (linguagem de máquina).**
- **O processo de compilação é mais rápido e gera programas menores, pois o objeto é executado, e não o programa-fonte.**
- **Na interpretação, o programa-fonte é executado diretamente, o que confere maior flexibilidade e facilidade de programação, mas torna o processo mais lento.**
- **A transpilação é um processo de tradução de uma linguagem de alto nível para outra linguagem de alto nível de nível um pouco mais baixo, como o TypeScript sendo transpilado para JavaScript.**

## O que esta nota responde

- Como um computador consegue entender um programa escrito em uma linguagem de alto nível?
- Qual a diferença prática e de performance entre compilar e interpretar um código?
- O que é transpilação e em que cenário ela é utilizada?

## Conceitos

**Código-fonte** · **Linguagem de alto nível** · **Compilador** · **Programa objeto** · **Interpretação** · **Transpilação** · **Análise léxica** · **Análise sintática**

## Conteúdo

`⏱ 00:00`

Muito bem. Como um computador entende o programa?

Se voltarmos ao slide da etapa anterior, percebemos que um `código-fonte` é o código que eu gero a partir da minha programação em alto nível. Seja pelo meu programa em `Java`, `C`, `C Sharp`, enfim, algum programinha aí de uma linguagem que eu escolhi.

Esse `código-fonte` será traduzido ou interpretado. Vamos entender o que significa isso.

### O Processo de Compreensão do Programa

Um programa é um amontoado de palavras, e não é possível que o computador entenda, a menos que haja um processo de tradução.

Se o computador não conseguir pegar aquelas instruções de alto nível com uma semântica específica e uma sintaxe específica, e entender o que eu quero com aquilo, não adianta nada; o propósito dele é nulo. Para isso, existe o processo de tradução, que está relacionado à compilação.

#### Compilação

Dado a minha linguagem de alto nível, ela é enviada para o compilador. O compilador vai executar a análise do programa e traduzir o meu programa de alto nível em um `código` de baixo nível, de linguagem de máquina.

Eu tenho a nomenclatura para o meu `código` de baixo nível, que é o programa objeto, que será executado pelo computador. É aí que o computador entende o que está ali dentro.

No processo de compilação, o programa que é enviado ao compilador é o que será traduzido para que o computador possa entendê-lo. Este é o processo de tradução ou compilação.

Na compilação, temos:

1.  **Geração de um programa objeto:** O compilador realiza várias análises:
    *   Análise léxica
    *   Análise sintática
    *   Análise semântica
2.  Por fim, ele gera um `código` que seria o meu programa objeto.

#### Interpretação

Na interpretação, o programa-fonte é executado diretamente. Isso torna o processo mais lento.

O interpretador executa o meu programa. Ele não vai gerar um programa objeto de uma linguagem de baixo nível que o computador entenda. Por isso, ele é mais lento, porque existe todo um trabalho para que o computador entenda aquela linguagem de alto nível e para que ele possa executá-lo.

**Comparativo:**

*   **Compilação:** Eu compilo e executo o objeto, e não o meu programa-fonte. A tradução, ou compilação, é uma execução mais rápida e gera programas menores.
*   **Interpretação:** O programa-fonte é executado diretamente. A interpretação dá uma maior flexibilidade e a linguagem é geralmente mais fácil de se programar, mas é mais lenta.

### Transpilação

Existe outro conceito que também se chama transpilação. O que seria?

É similar ao conceito de compilação, só que ao invés de eu jogar de uma linguagem de alto nível para uma linguagem de baixo nível, de uma linguagem de máquina, eu jogo de uma linguagem de outro nível para uma linguagem também de outro nível, só que um pouquinho mais baixa.

Como, por exemplo, o `TypeScript` é transpilado para `JavaScript`. Algumas dessas linguagens...

`⏱ 04:40`

São, por exemplo:

*   Linguagens que são traduzidas e compiladas (como `Java` e `C++`).
*   Linguagens interpretadas (como `Ruby`, `Python` e `JavaScript`).

## Relacionado

- [[historia-da-computacao-paradigmas-e-problemas-computacionais]]
- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
- [[Compreensão de Texto]]
- [[fundamentos-e-pilares-do-pensamento-computacional]]
