---
titulo: "Operadores, Variáveis e Estruturas de Controle em Algoritmos"
tags: [algoritmos, variaveis, operadores, fundamentos, pensamento-computacional, engenharia-de-software]
data: 2026-08-19
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 7
conceitos: [Operadores, Variáveis, Constantes, Instruções, Ordem de Prioridade dos Operadores, Entrada de Dados, Processamento de Dados, Saída de Dados]
---

# Operadores, Variáveis e Estruturas de Controle em Algoritmos

> [!resumo] Do que se trata
> A aula aborda as instruções primitivas, detalhando como os operadores (unários e binários) são usados para realizar cálculos matemáticos e definindo a ordem de prioridade desses operadores. Em seguida, explica o ciclo completo de um algoritmo, cobrindo a entrada, o processamento e a saída de dados, e finaliza com a estruturação de variáveis e o uso de estruturas condicionais.

## Para lembrar

- **As instruções determinam as ações que iremos executar em cima dos nossos dados, geralmente cálculos matemáticos, utilizando operadores.**
- **Os operadores podem ser tanto binários quanto unários.**
- **Um algoritmo possui variáveis, constantes, instruções e dados de entrada e de saída, formando uma estrutura sequencial.**
- **As estruturas condicionais permitem verificar se um evento ocorreu ou não, alterando o fluxo de execução do algoritmo.**

## O que esta nota responde

- O que são instruções e como elas são usadas para manipular dados em um algoritmo?
- Como funciona a ordem de prioridade dos operadores em um cálculo matemático?
- Quais são os componentes essenciais que formam a estrutura completa de um algoritmo?

## Conceitos

**Operadores** · **Variáveis** · **Constantes** · **Instruções** · **Ordem de Prioridade dos Operadores** · **Entrada de Dados** · **Processamento de Dados** · **Saída de Dados**

## Conteúdo

`⏱ 00:00`

Muito bom. Vamos falar agora sobre instruções primitivas.

As instruções determinam as ações que iremos executar em cima dos nossos dados, geralmente cálculos matemáticos. Para isso, nós utilizamos os operadores. Dentro desse cálculo matemático, o que vamos utilizar como informação, como `input`, são as variáveis e as constantes.

Os operadores podem ser tanto binários quanto unários. Nesta tabela, temos uma série de operadores que estão classificados como unário ou binário.

#### Operadores

*   **Operador de manutenção de sinais:** Este operador é usado para manter o sinal que está sendo carregado junto com o número. Ou seja, se ele é negativo, ele continua sendo negativo. Se ele é positivo, continua sendo positivo. Ele é um operador unário.
*   **Inversão de sinal:** Também é um operador unário. Quando colocamos um sinal de menos na frente do nosso número, seja ele positivo ou negativo, realizamos a inversão do sinal.
*   **Exponenciação:** É uma operação binária, pois precisamos de dois números.

#### Ordem de Prioridade dos Operadores

A ordem de prioridade é crucial:

1.  A exponenciação tem prioridade 2, ou seja, vem em segundo lugar na ordem de prioridade.
2.  Em seguida, temos a divisão.
3.  A multiplicação e a divisão de um real vêm em terceiro.
4.  A divisão de um inteiro vem em quarto.
5.  A multiplicação de um inteiro ou real vem em terceiro.
6.  Portanto, a divisão e a multiplicação têm o mesmo nível de prioridade.
7.  Adição, subtração e divisão por inteiro possuem também o mesmo nível de prioridade, nível 4.

**Exemplo:**
Vamos supor um exemplo para ilustrar o conceito de operadores: a área de um parque, que é igual a $\pi \times raio^2$.

Neste caso, temos:
*   A constante $\pi$.
*   A variável `raio` elevada ao quadrado.
*   E a variável `área`.

#### Definição de Instrução

Qual seria a definição formal de uma instrução?

A instrução vai executar um determinado tipo de ação para manipular o dado. As instruções são um vocabulário, uma linguagem de palavra-chave de uma determinada programação que tem por finalidade comandar um computador que irá tratar os dados. As instruções determinam as ações que irão processar e tratar esses dados.

#### Sintaxe e Linguagens

Por exemplo, vamos supor que eu tenho, dentro da minha linguagem de programação, o objeto "janela". Eu tenho diferentes formas, diferentes notações e linguagens distintas para um mesmo objeto.

*   Em português, eu falo "janela".
*   Em inglês, eu falo `window`.
*   Em espanhol, falo `ventana`.

O mesmo objeto, o mesmo conceito, possui sintaxes distintas quando levamos para o negócio de programação. Assim, as funções primitivas dentro de cada linguagem de programação possuem uma sintaxe particular. Essa notação também está relacionada aos operadores.

#### Entrada, Processamento e Saída de Dados

Outros conceitos que podemos elevar dentro dessa parte de instruções primitivas são a entrada, o processamento e a saída de dados dentro de um algoritmo.

Esses dados são importados de algum lugar — seja de um arquivo, ou de um diretório, enfim — e levados a um ambiente computacional para serem processados e depois imprimidos de alguma forma, seja em tela ou em algum outro dispositivo de saída.

**Exemplo:**
Vamos supor o exemplo de média escolar. Eu tenho o início do meu programa. Aqui, estou usando apenas uma estruturação para que vocês possam estar olhando.

`⏱ 05:00`

Entendendo que a estruturação do algoritmo independe de sintaxe e independe de técnica de representação de algoritmos.

### Exemplo de Execução e Inicialização de Variáveis

Temos aqui: `nota1` é igual a 5, `nota2` é igual a 8, e o resultado está zero. Por que o resultado está zero?

Nesse caso, o valor zero significa que estamos inicializando a variável. É como se estivéssemos dizendo: "Olha, naquele espacinho de memória que você vai alocar no computador para essa variável específica, você vai atribuir o valor zero."

O resultado será calculado como: `(nota1 + nota2) / 2`. O `nota2` seria aquele valor que está lá em cima.

A próxima instrução é: `escreva o resultado`. Fim do programa.

Nesse exemplo, nossa saída seria 6.5.

### Componentes da Estrutura Algorítmica

Nós temos as variáveis, as constantes, as instruções e os dados de entrada e de saída. Essa seria uma estrutura sequencial.

Repare que há uma ordenação, e as ações são realizadas, cada uma no seu tempo.

### Estruturas Condicionais

Se quisermos verificar se o aluno foi aprovado ou não, como fazemos isso?

Nesse caso, entramos na parte de estruturas condicionais e operadores.

## Relacionado

- [[fundamentos-de-algoritmos-variaveis-tipos-de-dados-e-estruturas-de-controle]]
- [[fundamentos-e-pilares-do-pensamento-computacional]]
- [[Diagrama de Atividade]]
- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
