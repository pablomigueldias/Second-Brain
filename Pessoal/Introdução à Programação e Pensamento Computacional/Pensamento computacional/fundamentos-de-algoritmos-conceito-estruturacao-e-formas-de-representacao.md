---
titulo: "Fundamentos de Algoritmos: Conceito, Estruturação e Formas de Representação"
tags: [pensamento-computacional, fundamentos, conceitos, estudos]
data: 2026-08-19
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 9
conceitos: [Algoritmo, Entrada e Saída de Dados, Processamento de Dados, Descrição Narrativa, Fluxograma, Pseudocódigo, Estruturas de Decisão]
---

# Fundamentos de Algoritmos: Conceito, Estruturação e Formas de Representação

> [!resumo] Do que se trata
> Apresenta o conceito de algoritmo como uma sequência finita e ordenada de passos para instruir computadores ou guiar tarefas cotidianas. Explica o ciclo de desenvolvimento de programas baseado na análise do problema, definição de entradas, processamento e saídas. Detalha as três principais formas de representação algorítmica: descrição narrativa, fluxograma e pseudocódigo, ilustradas com exemplos práticos.

## Para lembrar

- **Um algoritmo é uma sequência finita de passos e instruções com objetivo definido que precisa ser compreensível tanto por humanos quanto por máquinas.**
- **O desenvolvimento de um programa exige a compreensão do problema, o mapeamento dos dados de entrada, a definição do processamento lógico e a entrega dos dados de saída.**
- **A representação narrativa utiliza linguagem natural, mas apresenta o risco de gerar ambiguidades e múltiplas interpretações.**
- **O fluxograma utiliza símbolos gráficos pré-definidos para indicar operações, desvios condicionais e fluxos de dados de forma visual.**
- **O pseudocódigo funciona como uma etapa intermediária entre a linguagem natural e as linguagens de programação formais, utilizando regras estruturadas sem a rigidez sintática de um código final.**

## O que esta nota responde

- Quais são os passos fundamentais para estruturar e desenvolver um algoritmo?
- Quais são as diferenças, vantagens e desvantagens entre descrição narrativa, fluxograma e pseudocódigo?
- Como funcionam os fluxos de entrada, processamento, decisão e saída na resolução de problemas computacionais?

## Conceitos

**Algoritmo** · **Entrada e Saída de Dados** · **Processamento de Dados** · **Descrição Narrativa** · **Fluxograma** · **Pseudocódigo** · **Estruturas de Decisão**

## Conteúdo

`⏱ 00:00`

Muito bem. Vamos falar de algoritmos.

O computador é uma maravilha. Ele é um trabalhador que tem energia para caramba; não tem problema, ele pode trabalhar 24 horas. Ele é eficiente, é rápido. Ele tem uma série de vantagens, só tem um probleminha: ele não opera sozinho.

Você precisa determinar instruções para que ele possa executar. Ele não vai resolver seu problema sem você dizer o que você quer. Para isso, ele precisa de instruções detalhadas. Essas instruções detalhadas são o processamento dos dados dentro do computador, utilizando os programas.

O objetivo de um computador é exatamente receber, manipular, armazenar e processar esses dados. Os programas, por sua vez, são constituídos pelas instruções, e essas instruções possuem o passo a passo do que o computador precisa realizar.

### O Conceito de Algoritmo

O processo de resolução de problemas através de algoritmos é algo que podemos chamar de *step by step*, ou seja, passo a passo, utilizando as instruções que você determinou.

Para determinar as instruções, precisamos saber duas coisas:
1. O que precisa ser feito.
2. Qual a ordem de execução dessas instruções.

É importante que esse algoritmo seja entendido tanto por um humano quanto por uma máquina. Eu já comentei no início, na visão geral, que o algoritmo geralmente pode ser feito na mão. Se você precisa codificar, você precisa programar um computador. Ele tem que fazer sentido tanto no papel quanto no código. Ele tem que ser entendido por você e pela máquina.

### Desenvolvimento de Programas

Vamos para a parte do exemplo e desenvolvimento de programa.

O que precisamos fazer primeiro?
1. Analisar e entender: Estudar e definir quais são os dados de entrada e saída.
2. Identificar: O que eu preciso estar inserindo no programa? Quais são os dados inerentes ao meu contexto e o que eu espero algum tipo de desigualdade?

O algoritmo descreve o problema por meio de ferramentas, como narrativas, fluxogramas ou pseudocódigo. Existem técnicas distintas em que você pode estar determinando o seu algoritmo.

A parte de codificação é onde você utiliza alguma linguagem de programação para poder estar codificando aquele algoritmo. Nós temos aí uma sequência de passos com objetivo definido, execução de tarefas específicas e um conjunto de operações que resultam em uma sucessão de finitas ações.

### Exemplos de Algoritmos no Dia a Dia

Para tornar o conceito mais palpável, vamos trazer isso para o nosso dia a dia.

**1. Preparar um sanduíche:**
Você tem um passo a passo que estipula para poder estar criando o seu sanduíche.
*   Você pega o pão.
*   Você passa manteiga ou passa requeijão.
*   Escolhe qual é o tipo de parâmetro para que, qual o tipo de ingrediente você vai colocar ali.
*   Por exemplo: Vai botar queijo ou não? Botar presunto ou não?
*   Se você fecha o pão.
*   Se você leva o pão na chapa.

Você tem uma sequência de instruções que você realiza para criar o seu sanduíche.

**2. Trocar uma lâmpada:**
Da mesma forma, para trocar uma lâmpada:
*   Primeiro, apaga a luz.
*   Sobe na escada.
*   Tira a lâmpada.
*   Se a lâmpada não estiver quente, coloca outra lâmpada no lugar.
*   Desce da escada.
*   Liga a luz.

Você tem uma sucessão de instruções e de ações sendo executadas.

**3. Outros exemplos:**
Da mesma forma para fazer uma receita de bolo.
Da mesma forma para executar o trajeto da sua casa ao trabalho.

Tudo isso que eu comentei são instruções executadas passo a passo para concluir uma tarefa, e é essa a ideia de algoritmo.

Mas, então, como construir um algoritmo?

`⏱ 04:20`

Para começar, é preciso partir da compreensão do problema. Quais são os pontos mais importantes relacionados ao seu contexto?

Em seguida, você deve definir os dados de entrada — os dados fornecidos, que são inerentes ao seu contexto, no qual você precisa estar defendendo o programa.

Você vai definir o processamento desses dados: quais são as operações que serão realizadas dentro do seu programa, dentro do seu algoritmo, para que você possa processar aqueles dados e, depois, retornar as informações de saída. Ou seja, definir os dados de saída, os resultados, que isso ocorre geralmente após o processamento.

Depois disso, você utilizará algum método de construção ou de refinamento de código, de algoritmo. Você pode realizar testes e diagnósticos para estar refinando o seu algoritmo ou verificando se ele realmente funciona da maneira que deveria funcionar.

### Tipos de Representação de Algoritmos

No desenvolvimento de algoritmos, temos diferentes formas de construção:

- **Narrativa:** É a mais simples. Ela não atribui conceitos novos a esse tipo de estruturação de instruções passo a passo. Ela utiliza a linguagem natural, ou seja, a sua língua nativa. Contudo, ela pode ser ambígua, dependendo de como você vai formular o passo a passo, e pode fornecer diversas interpretações, dependendo de como for escrita.

- **Fluxograma:** É uma estrutura gráfica onde você tem símbolos pré-definidos que definem qual é o tipo de ação que está sendo executada ali. Pode ser uma operação, um `print` na tela, ou uma variável que está sendo alocada. Ele é de simples rendimento, mas requer um conhecimento prévio da estrutura e dos símbolos que estão sendo utilizados.

- **Pseudocódigo:** É a parte de regras bem definidas, com um passo a passo a ser executado. Ele está mais próximo de uma codificação, mas não é uma linguagem de programação efetivamente. Ele é um meio termo, para que você possa se acostumando com o mundo da programação.

### Exemplos de Algoritmos

**Exemplo 1: Multiplicação de dois números**

*   **Narrativa:** Você recebe os valores, multiplica e depois imprime o resultado.
*   **Fluxograma:** Temos o início do programa. Determinamos as variáveis `n1` e `n2`, realizamos uma operação de multiplicação e um `print` na tela, retornando os dados de saída. O algoritmo se encerra.

**Exemplo 2: Média dos alunos**

*   **Narrativa:** Você recebe os valores, imprime o resultado, verifica a regra de aprovação e depois imprime o resultado.
*   **Fluxograma:** Temos o início do programa. Determinamos as variáveis `N1` e `N2`, realizamos a operação de média, imprimimos na tela e verificamos se a média é maior ou igual a 7. Isso gera um fator de decisão — uma regra de aprovação — se ele será aprovado ou reprovado. Por fim, encerramos o programa.

### Conclusão

É essa a ideia do que é um algoritmo. Na verdade, ele é uma sequência de instruções passo a passo para que você possa resolver algum tipo de tarefa e atingir um objetivo final.

`⏱ 09:00`

Falando mais um pouco sobre outros conceitos que precisamos aprender para continuar o nosso curso de Primeiros Passos para Programar.

Até!

## Relacionado

- [[fundamentos-e-pilares-do-pensamento-computacional]]
- [[visao-geral-da-carreira-em-ti-da-rede-a-ciencia-de-dados-e-programacao]]
- [[raciocinio-logico-inducao-deducao-e-abducao]]
- [[02 - Hill Climbing]]
