---
titulo: "Estatística Básica em R: Média, Mediana e Moda"
tags: [estudos, conceitos, dados, variaveis, operadores, linguagens-de-programacao, machine-learning]
data: 2026-08-25
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [Estatística Básica, Média (Mean), Mediana (Median), Moda (Mode), Vetor, Linguagem R]
---

# Estatística Básica em R: Média, Mediana e Moda

> [!resumo] Do que se trata
> A aula aborda os conceitos estatísticos básicos de média, mediana e moda, reforçando que o R é uma linguagem ideal para quem vem de áreas de estatística e matemática. São revisadas operações matemáticas e vetoriais em R, e são ensinadas as funções específicas para calcular esses três indicadores estatísticos.

## Para lembrar

- **O R é uma linguagem desenvolvida primariamente para quem trabalha com estatística e matemática, facilitando o uso computacional para não-programadores.**
- **O cálculo de média em R é feito pela função `mean()`, que soma todos os valores de um vetor e divide pela quantidade de elementos.**
- **O valor retornado pela função `median(x)` representa um ponto central no conjunto de valores.**
- **A moda é o valor mais predominante em um vetor, calculado pela função `mode()`.**
- **O R é uma linguagem funcional, o que facilita o desenvolvimento de projetos em Data Science e Big Data sem exigir um conhecimento profundo de programação de baixo nível.**

## O que esta nota responde

- Qual a função do R em relação a estatística e matemática?
- Como calcular média, mediana e moda usando a linguagem R?
- Por que o R é considerado ideal para quem vem de áreas estatísticas e matemáticas?

## Conceitos

**Estatística Básica** · **Média (Mean)** · **Mediana (Median)** · **Moda (Mode)** · **Vetor** · **Linguagem R**

## Conteúdo

`⏱ 00:00`

Meu nome é Diego Bruno e hoje vamos ver um conteúdo relacionado à parte básica de estatística.

Ao longo das nossas aulas, já vimos como realizar operações aritméticas e operações lógicas. Também vimos como manipular vetores, como manipular matrizes, como ler um vetor, atribuir um vetor a um objeto, concatenar dois vetores e aprenderam também como concatenar duas matrizes e multiplicar matrizes. Vimos também como realizar operações básicas de forma geral dentro da linguagem R.

Acredito que todo mundo conseguiu interpretar tranquilamente, porque é uma linguagem que tem um apelo muito matemático. Por conta desse apelo matemático, não estamos tão presos na parte de código. É uma linguagem mais voltada para quem trabalha com estatística ou matemática.

Essa linguagem não foi desenvolvida para programadores; foi desenvolvida para quem é da área de matemática ou estatística. O que acontece é que é uma linguagem que tem um apelo computacional mais raso em conteúdo. Não que seja uma linguagem ruim por isso, mas ela facilita a vida de muita gente que não é formada na área de computação.

Por exemplo, eu já ministrei curso de IR para a área de estatística e matemática lá em São Carlos, na USP. Isso facilita que eles tenham uma ferramenta computacional de código para os projetos que desenvolvem, sem ter que aprender uma linguagem com uma complexidade tão grande, como programar em C ou programar em Python.

Para nós é fácil, mas para quem não é do mundo da computação, do mundo da programação, se torna algo mais complicado.

Em linguagens orientadas a objetos, por exemplo, temos que definir objetos, definir estruturas, definir construtores e classes. E ensinar isso para quem nunca programou é um desafio. No R, não temos tanta preocupação com esse tipo de aspecto. É uma linguagem que facilita muito a vida de quem está programando para Data Science ou para quem programa na área de Big Data e não tem uma formação computacional, mas sim uma formação mais matemática ou estatística.

### Estatística Básica: Média, Mediana e Moda

Hoje vamos ver um conteúdo relacionado à parte básica de estatística. Vamos aprender a calcular:

- Média
- Mediana
- Moda

Só para relembrar alguns exemplos que vimos lá na época do colegial.

Professor, mas vamos ver exemplos aqui nesse cenário, um cenário já ultrapassado no nosso conhecimento?

Não, porque vamos aprender esses fatores, principalmente porque é uma linguagem de base matemática.

Quando pegamos, por exemplo, o cálculo, vamos colocar aqui um exemplo só para recordar o que já vimos. Se eu pegar, por exemplo, `2 + 2 * 4`, se não nos atentarmos a esse problema, vamos acabar fazendo `2 + 2`, que dá 4, e aí vai multiplicar por 4, e vai errar a conta.

Porque eu teria que fazer antes `2 * 4`, que é 8, mais 2, que dá 10. Temos que lembrar também de jogar esse cálculo aqui. Então deu 10.

Agora, se eu pegar e colocar parênteses aqui e executar, meu valor vai mudar, vai dar 16.

Essas regrinhas básicas da parte de matemática, lá do ensino fundamental, ensino médio, acabamos esquecendo. Acabamos revendo aqui nessa linguagem, mas temos como base dessa linguagem esse conteúdo mesmo. Por ser uma linguagem funcional, não nos desviamos muito dessas questões.

`⏱ 05:40`

É uma linguagem muito voltada principalmente para quem está trabalhando nas áreas de Machine Learning, Data Science e Big Data e não tem tanta facilidade com programação. Por isso, o R se dá muito bem, pois é como se fosse uma calculadora de funções, uma linguagem bem tranquila de se trabalhar.

Vamos colocar aqui como exemplo um vetor. Eu joguei um vetor do jeito que aprendemos, atribuindo ao meu objeto `x` um vetor concatenado com os valores: 12, 7, 3, 4.2, 18, 2, 54, -21, 8 e -5.

### Cálculo da Média (Mean)

O que vou fazer é pegar esse vetor e calcular a média dos valores dele.

Para isso, vou criar um objeto chamado `result.man` e atribuir a ele o cálculo da média. Eu vou calcular a média usando esta função e, especificamente, quero calcular a média de `x`.

O que ele vai fazer? Ele vai pegar o meu vetor, percorrer ele, ler os valores e calcular a média usando esta função.

Agora, o que tenho que fazer é imprimir o `result.man`. Vamos executar e ver o que ele retorna. Ele retornou o valor 8.22.

O que seria esse 8.22? Ele está somando todos os valores e dividindo pela quantidade de elementos concatenados dentro do vetor. É isso que está fazendo a função `mean()`, que calcula a nossa média.

### Cálculo da Mediana (Median)

Vamos reaproveitar esse vetor e aplicar agora para o cálculo da mediana.

Para quem não lembra o que é mediana, ela seria um cálculo que define um elemento central que representa o eixo de valores do meu vetor. Seria um valor central, um pivô em um vetor de valores. De forma bem resumida, é isso.

O que vou fazer aqui é calcular `median.result` e definir para esse valor a função `median(x)`. Em seguida, vou imprimir o `median.result` e vou executar.

O valor que ele vai me retornar é um valor que representa o centro de valores. Assim, 5.6 seria um número que representa um ponto central nesse meu concreto de valores.

### Cálculo da Moda (Mode)

O que mais podemos calcular é a moda. É só chamar a função `mode()`, que calcula esse valor para a gente.

O que seria a moda? Eu vou pegar um vetor e vou procurar quais os valores que são predominantes, os valores que acontecem mais dentro do meu vetor.

Se eu pegar esse vetor aqui, não tem nenhum valor que acontece mais. Mas se eu colocar, por exemplo, 2 aqui e 2 aqui, já tenho dois valores do tipo 2. Se eu colocar outro 2, então tenho três valores 2. Esse valor é a minha moda porque ele acontece mais dentro aqui do meu vetor concatenado.

Esses exemplos simples, envolvendo estatística, mostram que o conteúdo de R é bem tranquilo. Quando precisamos de uma função, por exemplo, calcular uma integral ou algo do tipo, também temos o `help` da linguagem R, que é a documentação.

`⏱ 11:20`

A documentação mostra como gerar funções prontas para calcular integral, derivada, seno e cosseno. Não é preciso implementar numericamente o cálculo de uma integral.

Esse conteúdo foi feito para trazer a base da linguagem, para que possamos desenvolver nossos projetos tanto em `python`, quanto em `essai lab`, quanto em `r`, definindo qual linguagem seria a melhor para determinada situação.

### Escolha de Linguagem para Machine Learning

**Aluno:** Professor, eu vou implementar uma rede de `deep learning`. Eu vou implementar em `R`, dá para fazer?

**Professor:** Dá para implementar. Porém, seria muito mais tranquilo fazer em `python`.

Uma preocupação que temos atualmente é saber qual linguagem usar para trabalhar em determinada empresa, qual linguagem precisamos aprender para entrar no mercado de trabalho de `machine learning`, de `big data` ou de `data science`.

As linguagens que estão em alta no momento são:

*   `R`
*   `Python`
*   `Java`
*   `JavaScript`

Essas linguagens abordam muito conteúdo envolvendo `machine learning`.

Nosso conteúdo por hoje é esse.

## Relacionado

- [[linguagem-r-ambiente-replit-operadores-aritmeticos-e-escopo-em-machine-learning]]
- [[r-para-machine-learning-paradigma-funcional-recursos-base-e-pacotes]]
- [[manipulacao-de-vetores-e-matrizes-em-r-para-machine-learning]]
- [[linguagem-r-objetos-atribuicao-case-sensitivity-e-constantes-internas]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Um abraço para vocês e até a próxima.

</details>
