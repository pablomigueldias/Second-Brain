---
titulo: "Estruturas de Repetição em Algoritmos: Loops For e While"
tags: [algoritmos, estruturas-de-dados, linguagens-de-programacao, pensamento-computacional]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 5
conceitos: [Estruturas de repetição, Loop for, Loop while, Treinamento de redes neurais, Vetor, Algoritmo em Python]
---

# Estruturas de Repetição em Algoritmos: Loops For e While

> [!resumo] Do que se trata
> A aula aborda a importância das estruturas de repetição em algoritmos, especialmente em cenários como o treinamento de redes neurais. São apresentados exemplos práticos de como utilizar o loop `for` para iterar sobre elementos de uma lista e o loop `while` para repetições mais refinadas.

## Para lembrar

- **Estruturas de repetição são essenciais em algoritmos que dependem de valores serem incrementados ao longo do tempo, como o treinamento de redes neurais.**
- **O loop `for` é ideal para percorrer itens de uma lista, lendo um valor por vez, como em um vetor de instruções de um modelo de machine learning.**
- **O loop `while` é utilizado para estruturas de repetição mais refinadas, permitindo um controle mais detalhado sobre o fluxo do algoritmo.**

## O que esta nota responde

- Por que é importante entender as estruturas de repetição em algoritmos?
- Quando devo usar o loop `for` em Python?
- Qual a diferença de uso entre os loops `for` e `while`?

## Conceitos

**Estruturas de repetição** · **Loop for** · **Loop while** · **Treinamento de redes neurais** · **Vetor** · **Algoritmo em Python**

## Conteúdo

Olá. Meu nome é Diego Bruno, e a nossa aula de hoje é sobre estruturas de repetição.

É muito importante que a gente tenha noção de como fazer uma estrutura de repetição, principalmente pelo fato de aplicarmos em situações onde dependemos dos nossos valores serem incrementados ao longo do tempo.

Falando de um exemplo, o treinamento de redes neurais é incrementado a cada época. Nesse caso, ficamos em um treinamento sempre em uma estrutura de repetição. Essa estrutura vai acontecendo a todo momento, agregando conhecimento ao peso da rede, falando de forma geral.

Portanto, é importante que a gente entenda como funciona uma estrutura de repetição para um algoritmo em Python.

### Loop `for`

Vamos fazer um exemplo bem simples. Vamos começar com um loop utilizando o `for`.

O que será esse exemplo? Vamos colocar uma lista e eu vou ler essa lista. Essa lista terá os valores 1, 2, 3, 4 e 5. Agora, vou fazer uma leitura desses valores com um `for`.

Eu vou pegar o item da lista, um item de cada vez, e vou `print`ar cada um desses itens.

O que vai acontecer? Eu tenho um `for` que vai ler item por item dessa lista e ele vai mostrar na minha tela esses valores.

Assim, eu tive um loop que está lendo valor por valor dessa lista, um de cada vez. Eu leio o valor 1, depois leio o valor 2, depois leio o valor 3, depois leio o valor 4 e leio o valor 5.

#### Aplicação do `for`

Onde seria importante fazer uma leitura de uma lista dessa forma?

Às vezes, recebemos um conjunto de instruções de um modelo de machine learning que está gravado, cada instrução, em um vetor. Precisamos ler esse vetor para comparar o que está acontecendo com as respostas que esperamos.

Eu tenho um determinado comportamento que gera uma resposta. Eu comparo com o meu vetor e vejo se o meu treinamento está batendo com a resposta que estou obtendo.

Um exemplo que eu lembrei para mostrar o quanto é importante, às vezes, a gente percorrer uma lista para encontrar uma resposta equivalente para o nosso problema dentro de uma base de dados, de um banco de dados do nosso sistema inteligente. Esse seria um loop utilizando `for`.

### Loop `while`

Agora vamos ver um exemplo com `while`, um laço de repetição. Podemos usar um exemplo desse para auxiliar no caso de uma estrutura de repetição um pouco mais refinada.

## Relacionado

- [[estruturas-de-repeticao-em-algoritmos-tipos-funcionamento-e-aplicacoes]]
- [[estruturas-condicionais-em-python-simples-compostas-e-aninhadas]]
- [[tipos-de-dados-em-python-inteiros-flutuantes-complexos-strings-e-booleanos]]
- [[python-para-machine-learning-paradigmas-ecossistema-e-ambientes-de-execucao]]
