---
titulo: "Visualização de Dados e Regressão com Matplotlib e Scikit-Learn"
tags: [estudos, conceitos, machine-learning, dados, linguagens-de-programacao, variaveis, matplotlib]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 11
conceitos: [Matplotlib, Gráfico 2D, Gráfico 3D, Mapa de calor, Regressão, Scikit-Learn, Amostras de treinamento]
---

# Visualização de Dados e Regressão com Matplotlib e Scikit-Learn

> [!resumo] Do que se trata
> A aula apresenta a biblioteca Matplotlib, essencial para gerar gráficos profissionais em projetos de Machine Learning e Deep Learning. É demonstrado como usar essa biblioteca para visualizar dados, como gráficos 2D, 3D e mapas de calor. Além disso, é ensinado o uso do Scikit-Learn para gerar amostras de regressão, simulando dados para o treinamento de modelos.

## Para lembrar

- **A biblioteca Matplotlib é uma das mais utilizadas para Machine Learning envolvendo Python e confere um aspecto profissional aos projetos.**
- **Matplotlib permite plotar diversos tipos de gráficos, incluindo gráficos 2D, 3D e mapas de calor.**
- **É possível usar o Scikit-Learn para gerar um método de regressão, definindo valores em X e Y, e simulando amostras para o treinamento.**
- **Ao plotar os dados gerados, é possível visualizar a região de busca e a distribuição das amostras iniciais, como em um algoritmo genético.**

## O que esta nota responde

- Qual biblioteca é utilizada para gerar gráficos e visualizar resultados em projetos de Machine Learning?
- Como o Matplotlib pode ser usado para representar diferentes tipos de dados, como em um algoritmo genético?
- Como gerar e plotar dados de regressão simulados usando Scikit-Learn para fins de treinamento?

## Conceitos

**Matplotlib** · **Gráfico 2D** · **Gráfico 3D** · **Mapa de calor** · **Regressão** · **Scikit-Learn** · **Amostras de treinamento**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e hoje vamos ver um pouco sobre uma biblioteca que nos permite gerar gráficos, representando nossos resultados ou uma amostra de entrada para o nosso treinamento.

A biblioteca que vamos usar hoje é a `Matplotlib`. É uma biblioteca muito interessante para utilizar em nossos projetos e que confere um aspecto mais profissional, especialmente na área de Machine Learning. Ela é muito utilizada em projetos, principalmente de Deep Learning. Vou mostrar aqui um projetinho bem simples para vocês, começando por falar sobre a biblioteca `matplotlib` para termos uma noção do que ela é.

### Visão Geral da Matplotlib

Temos a página oficial deles, que mostra basicamente todo o conteúdo que eles fornecem. É uma das bibliotecas mais utilizadas para Machine Learning envolvendo Python.

É possível instalar essa biblioteca nativa em nossa máquina. No entanto, como vou mostrar o funcionamento da biblioteca, vou acabar usando o Colab para apresentar a ferramenta.

No próprio site deles há vários exemplos. Vocês podem ver exemplos de como plotar:

- Um gráfico 2D.
- Um gráfico 3D.
- Um gráfico onde é possível gerar, por exemplo, um mapa de calor, para representar uma região de busca.

Existem várias funções aqui dentro. Basicamente, tudo que eu preciso para gerar um gráfico nos meus projetos eu uso essa biblioteca. Existem outras, porém, eu considero esta biblioteca completa para tudo que precisamos envolvendo a parte gráfica.

Em todos os projetos que trabalhei, acabei usando esta biblioteca; eu particularmente gosto muito dela e acabo usando sempre. Ela tem várias funções: é possível representar um gráfico de forma seno ou cosseno, ou representar uma população gerada de busca.

O exemplo que vamos fazer é gerar uma população inicial para o nosso projeto e, em seguida, plotar essa população em um gráfico. Para quem viu a parte de algoritmo genético, vamos pensar naquele exemplo onde vamos gerar uma população inicial e imprimir essa população em um gráfico.

### Demonstração Prática e Configuração do Código

Vou mostrar aqui para vocês. A primeira coisa que fiz foi abrir um Colab em branco.

Eu vou colocar o meu código aqui dentro dessa página. O interessante é que, se você estiver conectado com uma conta no Drive do Google, você consegue armazenar seu código lá na nuvem e depois consegue compartilhar com outras pessoas. Essa parte é muito interessante.

Vamos criar o nosso código.

Primeira coisa: vou dar um `import` para o `matplotlib`. Assim, consigo dar esse `import`. Tudo que vou importar, vou deixar aqui nesse primeiro módulo.

Agora, vou inserir uma nova célula de código. Dei o `import` aqui. Se der um *play*, já vamos ver se deu certo carregar a nossa biblioteca. O *check* aqui verde, tudo OK.

Agora, vou chamar também a biblioteca do `Scikit-Learn`. Vou jogar aqui `Scikit-Learn` para `datasets` e vou importar uma função que se chama `makeRegression` para a gente criar a nossa regressão nos valores que vou apresentar aqui para vocês.

Vou criar essa função e vou procurar valores...

`⏱ 05:40`

### Configurando a Regressão e Gerando Dados

Para a minha regressão, eu vou definir os valores em X e Y. Vou colocar um `make` que já aparece aqui para mim, para gerar a regressão. Em seguida, eu vou colocar para girar entre `n_samples` e quero girar 200 amostras. Depois, eu vou girar `n` com valor 1 para cada amostra e vou gerar um ruído de 30, só para ser um exemplo. Também vou importar aqui a função do `matplotlib` para conseguir gerar a minha regressão.

Agora, eu vou apresentar o gráfico. Vou rodar isso aqui para ver se está tudo ok, se está tudo certo. Vou inserir uma nova célula, uma célula de código. Agora, vou plotar aqui o que eu tenho para X e Y, tudo que eu gereci lá na minha regressão. Vou plotar aqui e vou dar um `plt.show()` aqui para gerar o meu gráfico. Vou dar um `play` aqui também.

### Análise e Recapitulação do Projeto

O gráfico foi gerado aqui com as minhas amostras.

Para recapitular o que fizemos:

- Importamos a biblioteca do `matplotlib`.
- Geramos um método de regressão pelo `Scikit-Learning` para gerar as nossas amostras iniciais.
- Definimos o que seria a minha regressão gerada.
- Criei 200 exemplos com características envolvendo uma unidade e coloquei um erro para representar em 30 unidades. Coloquei uma taxa de erro de 30 e plotei esse gráfico, que é o que temos aqui.

Dessa forma, dentro da nossa região de busca, girando uma população inicial, o que temos para representação é esse gráfico.

### Aplicações e Exemplos de Uso

Um exemplo bem simples seria, por exemplo, a gente imprimindo na tela a nossa população inicial de um algoritmo genético, ou plotando classes diferentes para o treinamento de uma rede neural.

Se a gente pegar, por exemplo, o TensorFlow Playground aqui no Google, ele tem problemas que trabalham com essas amostras. Se a gente pensar, por exemplo, como ele está girando esse espaço de busca com duas classes, certamente a biblioteca que eles estão utilizando é a biblioteca do `matplotlib`. Não tenho certeza, porque existe uma programação por trás aí da tela deles, mas certamente eles utilizaram uma biblioteca, se não for essa, uma biblioteca bem parecida para representar as duas classes que estão sendo relacionadas.

O conteúdo de hoje era mais ou menos esse: para a gente mostrar como criar um projeto do zero dentro do Colab e também para que vocês vejam o uso de uma biblioteca em Python exclusiva para quem trabalha com uma [inaudível]. Por hoje é isso.

## Relacionado

- [[tipos-de-dados-em-python-inteiros-flutuantes-complexos-strings-e-booleanos]]
- [[python-para-machine-learning-paradigmas-ecossistema-e-ambientes-de-execucao]]
- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[paradigmas-e-linguagens-de-programacao-para-machine-learning]]
