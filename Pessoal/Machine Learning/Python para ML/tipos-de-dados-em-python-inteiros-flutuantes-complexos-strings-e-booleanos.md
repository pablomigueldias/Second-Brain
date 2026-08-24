---
titulo: "Tipos de Dados em Python: Inteiros, Flutuantes, Complexos, Strings e Booleanos"
tags: [estudo, conceitos, fundamentos, linguagens-de-programacao, variaveis, dados, python-para-ml]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 15
conceitos: [Tipo Inteiro (`int`), Tipo Float (Ponto Flutuante/Decimal), Tipo Complexo, Variável `string`, Variável `boolean`, Números Racionais, Programação em Python]
---

# Tipos de Dados em Python: Inteiros, Flutuantes, Complexos, Strings e Booleanos

> [!resumo] Do que se trata
> A aula aborda os tipos de variáveis fundamentais em Python, começando pelos tipos numéricos (inteiro, float e complexo). Em seguida, detalha o uso de variáveis para representar texto (string) e valores lógicos (boolean), mostrando como esses conceitos são a base para a programação e o Machine Learning.

## Para lembrar

- **O tipo inteiro (`int`) é composto por caracteres numéricos e é usado para valores sem componente decimal, como 21, 4 ou -2048.**
- **O tipo `float` (ponto flutuante/decimal) é usado para números racionais, ou seja, números que podem ser representados por frações, como 1.80 ou 1.91.**
- **O tipo `complex` é utilizado em áreas como engenharia para calcular circuitos eletrônicos em corrente alternada.**
- **Variáveis do tipo `string` são usadas para representar palavras, frases ou textos, como o nome de um aluno.**
- **Variáveis do tipo `boolean` são usadas para valores lógicos, como True ou False, sendo essenciais em áreas como IoT e robótica.**

## O que esta nota responde

- Quais são os tipos de variáveis mais básicos que devo saber usar em Python?
- Qual a diferença prática entre usar um `int`, um `float` e um `complex`?
- Como os tipos de dados básicos (como booleanos e strings) se aplicam na programação e no Machine Learning?

## Conceitos

**Tipo Inteiro (`int`)** · **Tipo Float (Ponto Flutuante/Decimal)** · **Tipo Complexo** · **Variável `string`** · **Variável `boolean`** · **Números Racionais** · **Programação em Python**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e agora vamos ver um pouco sobre os tipos de variáveis.

Já vimos um ambiente interessante para programar nativo na máquina, instalando um software na nossa máquina. Vimos também quando precisamos rodar algo online sem instalar um software na nossa máquina. Isso é interessante tanto para a questão de não ficar preso a uma máquina, quanto para deixar tudo salvo em uma nuvem, e na parte de compartilhar o projeto e editar esse mesmo projeto com outras pessoas.

Agora que sabemos duas ferramentas muito legais para a programação em Python, vamos ver um pouco da parte base que envolve as variáveis. Para quem está começando a programar em Python, ou até mesmo para quem está entrando no mundo da programação, a questão de variáveis gera um pouco de confusão, então vou abordar esse conteúdo com vocês.

### Tipo Inteiro (`int`)

Um tipo de variável que é o mais simples é o tipo inteiro. O tipo inteiro é composto por caracteres numéricos. Vamos trabalhar com algarismos inteiros. É um tipo sempre usado com um número que pode ser escrito sem um componente decimal. Vamos trabalhar com números inteiros, sem quebras.

Por exemplo, podemos trabalhar com o número `21`, o número `4`, o número `0`, o número `-2048`. Esses números são valores inteiros.

Quando pegamos, por exemplo, `9.75` ou `1.5`, esses valores não são valores inteiros. Precisamos atribuir outro tipo de variável a eles.

Aqui temos um exemplo onde estou entrando com o valor de `idade` igual a `18` e o valor de `ano` igual a `2002`. Se eu pegar esse código e printar essas variáveis, ou printar o tipo delas, ele vai retornar que essas variáveis são do tipo inteiro. O tipo desses dados são referentes a valores inteiros.

### Tipo Float (Ponto Flutuante/Decimal)

Aqui temos as variáveis do tipo `float`, que é o inverso do que estávamos vendo para inteiro. O nome pode ser tanto "ponto flutuante" quanto "decimal"; é reconhecido dessas duas formas.

O tipo `float` é composto por caracteres numéricos, algarismo também, de forma decimal. O famoso ponto flutuante é um tipo usado para números racionais.

Para lembrar o que é um número racional, são números que podem ser representados por meio de frações. Informalmente, é também conhecido como número quebrado. Quando vamos usar um número quebrado, acabaremos utilizando uma variável do tipo `float`. Em vários casos, vamos precisar desse tipo de variável.

Por exemplo, a altura de uma pessoa. É muito difícil termos uma variável do tipo inteiro. A pessoa tem um metro ou dois metros. Sempre vai ser um metro e meio, `1.80`, `1.90`, `1.91`. São valores que chamamos de valores quebrados.

O peso também. Você vai pesar e terá um valor em quilos e um valor em gramas. Você vai trabalhar com valores do tipo `float` também.

Se der um `print` nesse valor, por exemplo, `printType(peso)` e `printType(altura)`, vamos retornar na nossa saída que a classe é do tipo `float`. A própria linguagem consegue detectar o tipo de valor que está sendo dado como entrada para ela.

### Tipo Complexo

Variável do tipo complexo. Principalmente quem é da área de engenharia e da área de ciência já deve ter utilizado um número complexo.

`⏱ 05:20`

Na vida, eu sou da área de eletrônica, então usava muito na época da minha graduação o número `complex` para calcular circuitos eletrônicos em corrente alternada. Trabalhávamos com os números que chamamos de números imaginários.

A gente tem os números reais, que é a parte real, que é a parte que conhecemos no nosso dia a dia, e a gente tem uma parte que é a parte imaginária. Para quem já trabalhou com alguma dessas áreas, principalmente na elétrica e eletrônica, já deve ter usado números imaginários.

Aqui, a gente consegue representar também um número imaginário. Quando definimos, por exemplo, `A = 5 + 2J`, o `J` representa o lado imaginário. Se eu colocar um `print` para esses valores, um `print` para o tipo deles, eu vou ter como retorno uma variável do tipo `complex`.

### Variáveis `string`

Uma variável também muito conhecida é a variável `string`. O que seria uma `string`? É quando a gente tem um conjunto de caracteres dispostos de uma forma que determina uma ordem. Geralmente é utilizada para representar palavras, frases ou textos.

Não é sempre que a gente vai trabalhar com números apenas. Às vezes o retorno que a gente tem para o usuário é uma `string`. Por exemplo, eu preciso retornar uma variável que encontrei na minha busca, e essa variável é uma palavra. Estou retornando o nome de um aluno em uma lista que estou buscando pelo número do RA, pelo número do registro acadêmico. A variável de retorno vai ser o nome do aluno, então é uma variável do tipo `string`.

Aqui temos um exemplo: estou definindo o nome igual a `Guilherme` e a profissão dele, engenheiro de software. Colocar o `print` para o tipo da minha variável vai retornar uma variável do tipo `string`.

### Variáveis `boolean`

Outra variável muito conhecida para a parte de computação, e principalmente para quem trabalha com situações onde estamos usando apenas a lógica, é a variável do tipo `boolean`.

A variável do tipo `boolean` trabalha de forma lógica e pode assumir apenas dois valores: verdadeiro ou falso. Se a gente representar isso na lógica computacional, sabemos que trabalhamos com os valores zero e um. Para quem conhece um pouco da área eletrônica, o valor que um computador recebe para zero é zero volts, e quando a gente recebe o valor 1, estamos trabalhando com 5 volts. São os valores que temos para representar a variável.

Existem situações em que vamos precisar trabalhar apenas com esses dois valores. Por exemplo, quando estamos trabalhando com IoT ou com robótica. Quando um sensor é excitado, ele manda um sinal 1 para o controlador. Quando ele não recebe valor nenhum, está recebendo na verdade o valor zero, porque não está sendo excitado.

Com esse valor 1, que está representando o verdadeiro, eu posso montar a minha lógica. Por exemplo, o robô detectou um obstáculo, então ele recebeu o valor 1. O que o robô faz? Ele para ou ele desvia, depende qual é a lógica que eu montei para ele.

Quando trabalhamos com valores lógicos, acabamos usando a variável do tipo `boolean`.

Aqui, por exemplo, temos dois exemplos: `Fim_de_semana = True`. Estamos no final de semana.

`⏱ 10:00`

[Continuação do conteúdo]

A variável `fim de semana` recebe o valor booleano, e o tipo da variável `feriado` também recebe um valor booleano. Esses tipos de variáveis são importantes para que a gente saiba modelar bem o nosso problema. Se a gente não começar pela modelagem dos nossos valores possíveis, acabamos nos perdendo no que estamos esperando do retorno do nosso programa, do nosso sistema.

### Objetivo e Algoritmos de Machine Learning

O nosso objetivo agora vai ser trabalhar com algoritmos que são próximos aos algoritmos de machine learning.

Claro que não vamos começar implementando uma rede neural do zero, porque é um algoritmo mais complexo. No entanto, vamos começar a ver a parte de:

- Multiplicar matriz.
- Multiplicação de vetores.
- Ler uma entrada em formato de imagem e manipular essa imagem.

Vamos começar com esses exemplos para que vocês comecem a se habituar com essa parte de machine learning. Depois, quando for implementar mesmo uma rede neural ou uma rede de deep learning, é basicamente essa estrutura que vamos ter: multiplicação de matrizes, leitura de uma imagem, interpretação dessa imagem no formato de uma matriz, e aplicação de um filtro.

### Programação e Machine Learning

Quando falamos de programação e machine learning, é tudo o que sabemos de básico unindo para se tornar um todo, que é algo mais complexo, que seria um modelo de machine learning. Mas tudo que temos na parte de base é o que vamos usar na parte de machine learning.

Não existe diferença entre "eu sei programar em Python" e "não sei programar para machine learning". É uma única coisa.

É claro que vamos usar métodos que existem dentro de bibliotecas, como, por exemplo, `NumPy`, `SciPy`, `Scikit Learning` e `Matplotlib`. São bibliotecas que vamos chamar para nos ajudar, para que não precisemos implementar uma função, por exemplo, de analisar valores com `pandas`, do zero, ou plotar valores, ou simplesmente rodar um modelo. Não precisamos implementar tudo do zero, porque acabaremos usando bibliotecas que vão auxiliar o nosso trabalho.

As bibliotecas são as grandes aliadas para Python na área de Machine Learning. Se pegarmos quem está trabalhando com Machine Learning e por que está trabalhando com Python, é justamente para reaproveitar bibliotecas e códigos de outros desenvolvedores.

## Relacionado

- [[fundamentos-de-algoritmos-variaveis-tipos-de-dados-e-estruturas-de-controle]]
- [[python-para-machine-learning-paradigmas-ecossistema-e-ambientes-de-execucao]]
- [[instalando-sublime]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Muito obrigado aí e até a próxima.

</details>
