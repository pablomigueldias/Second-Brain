---
titulo: "Manipulação de Vetores e Matrizes em R para Machine Learning"
tags: [estudos, conceitos, machine-learning, algoritmos, matematica, dados, estruturas-de-dados]
data: 2026-08-25
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [Vetor, Matriz, Concatenar, Machine Learning, Data Science, Deep Learning, Redes Neurais]
---

# Manipulação de Vetores e Matrizes em R para Machine Learning

> [!resumo] Do que se trata
> A aula aborda a definição e manipulação de vetores e matrizes, estruturas fundamentais para o trabalho em Machine Learning e Data Science. São ensinadas funções como `c()` para concatenar valores e `length()` para determinar o tamanho de um vetor. Além disso, são detalhados os processos de criação, visualização e multiplicação de matrizes, destacando a importância dessa operação em Redes Neurais e Deep Learning.

## Para lembrar

- **Para definir um vetor, utiliza-se a função `c()` (concatenar), que recebe um conjunto de valores separados por vírgula.**
- **A função `length()` é usada para determinar o tamanho (número de elementos) de um vetor.**
- **Vetores e matrizes são estruturas cruciais em Machine Learning e Data Science, pois são usadas para representar dados como imagens e vetores de treinamento.**
- **A multiplicação de matrizes é um conceito fundamental em Deep Learning, pois os algoritmos precisam percorrer imagens e dados usando matrizes convolucionais.**

## O que esta nota responde

- Como devo definir e manipular vetores e matrizes em R?
- Por que o conhecimento sobre vetores e matrizes é importante para Machine Learning?
- Qual a importância da multiplicação de matrizes no contexto de Deep Learning?

## Conceitos

**Vetor** · **Matriz** · **Concatenar** · **Machine Learning** · **Data Science** · **Deep Learning** · **Redes Neurais**

## Conteúdo

`⏱ 00:00`

Meu nome é Diego Bruno e a ideia da aula de hoje é trabalhar com vetores e matrizes. Esse conteúdo é muito importante, principalmente para quando formos trabalhar com nossos modelos de *machine learning* e *data science*. Isso ocorre porque trabalhamos muito com leitura de imagens, e imagens são matrizes. O vetor de treinamento é representado por um vetor numérico. Portanto, é muito importante que saibamos manipular essas estruturas, como defini-las.

### Definindo e Manipulando Vetores

A primeira coisa que quero mostrar é como definir um vetor. Para definir um vetor, vamos usar a função `c()`. Essa função recebe esse nome porque o `c` vem de "concatenar".

Vou definir, por exemplo, um vetor que vou chamar de `primeiro_vetor`. Ele receberá um conjunto de valores. Usarei a função `c()` para definir meus valores: `1, 3, 5, 9, 10`, separados por vírgula.

```
primeiro_vetor <- c(1, 3, 5, 9, 10)
```

Ao rodar o algoritmo, ele imprime os valores: `1, 3, 5, 9, 10`.

É possível definir valores de certeza, como por exemplo, `verdadeiro` ou `falso`.

Além disso, podemos perguntar o tamanho desse vetor. Se eu quiser saber o tamanho dele, eu uso a função `length()` e coloco o nome do meu vetor, que neste caso é `primeiro_vetor`.

```
length(primeiro_vetor)
```

Ao executar, ele mostra o valor que está no vetor e também retorna o tamanho. Temos 5 valores, e o valor de retorno é 5.

*(Observação: Houve um pequeno erro na execução inicial, mas ao rodar novamente, o sistema mostra os valores e a quantidade de valores dentro do vetor.)*

#### Concatenando Vetores

Também podemos concatenar dois vetores.

Vou copiar o `primeiro_vetor` para a linha de baixo e vou deixá-lo como `vetor1`. E aqui, vou criar um `vetor2`, mudando um pouco os valores.

```
vetor1 <- c(1, 3, 5, 9, 10)
vetor2 <- c(1, 4, 5, 8, 22)
```

Agora, posso definir um terceiro vetor, que chamaremos de `vetor3`, e dentro da concatenação, vou colocar o `vetor1` e o `vetor2`.

```
vetor3 <- c(vetor1, vetor2)
```

Ao executar, ele retorna a união desses dois vetores: `1, 3, 5, 9, 10, 1, 4, 5, 8, 22`. Podemos fazer esse tipo de operação com qualquer vetor de entrada.

### Introdução às Matrizes

Agora vou mostrar um pouco sobre matrizes. Matriz também é uma estrutura muito útil de criar em R.

Vou definir, por exemplo, uma `MatrizA` que receberá uma matriz. O objeto `MatrizA` receberá uma matriz.

`⏱ 06:00`

A função `matriz`. Vou colocar aqui o valor de matriz para a gente ler. Vou definir um valor de matriz qualquer. No caso, vou definir `2, 4, 3, 1, 5` e `7`.

Agora, vou definir dentro desse vetor o tamanho da minha matriz. Vou definir o número de linhas e depois o número de colunas, que vai ser `3`. Aí vou definir o restante da estrutura da matriz, que é uma matriz linha por coluna, e vou fechar aqui.

Eu atribuo essa estrutura. Só que vai ter que ficar todo mundo na mesma linha. Eu dou `Enter` para ficar mais claro, mas tenho que fechar aqui.

Vou executar. Há um erro aqui ainda. Deixa só o `A` aqui para ver se é o problema do objeto que eu criei. `A` está recebendo, aqui é com `X`, matriz não é com `Z` ali no caso, é com `X`. Ainda tem um erro. Falta dizer que eu quero concatenar. Depois de definir que é uma matriz, eu tenho que definir o valor `C` para concatenar essa estrutura.

Vou executar de novo. Ainda tem erro. Vamos tirar esse erro.

Estou definindo a matriz, concatenando ela: `2, 4, 3, 1, 5` e `7`, com número de linhas `2` e número de colunas `3`.

Acho que tem que ser maiúsculo. Deve ser esse o erro. Vou colocar para executar. Pronto, não deu erro agora.

### Visualizando a Matriz

Agora vou colocar aqui para `print`ar essa matriz para a gente visualizar. Está aqui a minha matriz definida em duas linhas e três colunas.

Vocês viram que eu entro com o valor de linha, quantidade de linha e quantidade de coluna. Com isso, consigo representar o vetor na ordem que eu tenho aqui:

*   `2, 4, 3` (primeira linha).
*   `1, 5, 7` (segunda linha).

Aqui temos uma representação de como apresentar vetores e matrizes. Vamos usar isso nos nossos exemplos aplicados de Machine Learning. É bom que a gente tenha uma noção de como manipular esse tipo de estrutura.

### Multiplicação de Matrizes

Eu consigo também fazer uma multiplicação disso. Por exemplo, eu tenho aqui a matriz `A`. Vou definir agora uma matriz `B`, só copiei e colei aqui, mas vou mudar alguns valores para não ficar igual.

O que eu posso fazer é um `print` de `A` vezes `B`. Vou executar aqui. Temos o resultado da nossa multiplicação de duas matrizes.

Este é um ponto bem interessante quando estamos trabalhando com esse aspecto: a multiplicação de matrizes. Ela é muito importante quando estamos trabalhando nas redes de Deep Learning, com as convoluções. Os nossos algoritmos precisam percorrer a imagem com uma matriz e tudo mais. É muito importante para que a gente trabalhe dentro desse cenário.

Esse é o resultado da nossa multiplicação das duas matrizes. O conteúdo da aula de hoje é esse.

`⏱ 12:20`

Muito obrigado pela participação de vocês.

Até o nosso próximo conteúdo.

## Relacionado

- [[fundamentos-de-algoritmos-vetores-matrizes-e-estruturas-de-dados]]
- [[estruturas-de-controle-e-operadores-em-scilab]]
- [[estruturas-de-repeticao-em-algoritmos-tipos-funcionamento-e-aplicacoes]]
- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
