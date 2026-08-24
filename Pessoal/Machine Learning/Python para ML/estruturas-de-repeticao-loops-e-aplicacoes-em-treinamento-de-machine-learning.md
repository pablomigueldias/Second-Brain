---
titulo: "Estruturas de Repetição (Loops) e Aplicações em Treinamento de Machine Learning"
tags: [estudo, conceitos, algoritmos, machine-learning, linguagens-de-programacao, estruturas-de-dados]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 9
conceitos: [Estruturas de repetição, Laço while, Condição de parada, Treinamento de Machine Learning, Rede de deep learning, Iteração]
---

# Estruturas de Repetição (Loops) e Aplicações em Treinamento de Machine Learning

> [!resumo] Do que se trata
> A aula explica o conceito de estruturas de repetição, utilizando o laço `while` como exemplo prático. São mostradas aplicações desse laço em Machine Learning, como a iteração sobre imagens de um dataset ou o controle do treinamento de redes neurais até que uma condição específica seja atingida. O conteúdo enfatiza a importância de definir condições de parada e o estado inicial do contador para o funcionamento correto do algoritmo.

## Para lembrar

- **O laço `while` executa um bloco de código enquanto uma condição booleana for verdadeira (ex: `while contador < 10`).**
- **Em Machine Learning, o treinamento de redes neurais pode ser controlado por um laço até que uma condição específica seja atingida, como a acurácia da rede atingir 95%.**
- **É necessário definir uma condição para o ponto em que o algoritmo será treinado, ou seja, para a leitura das imagens da pasta durante o treinamento.**

## O que esta nota responde

- Como usar estruturas de repetição em algoritmos?
- Como controlar o treinamento de uma rede neural de deep learning?
- Qual a importância de definir uma condição de parada em um laço while?

## Conceitos

**Estruturas de repetição** · **Laço while** · **Condição de parada** · **Treinamento de Machine Learning** · **Rede de deep learning** · **Iteração**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e hoje vamos ver um pouco sobre estruturas de repetição envolvendo um laço do tipo `while`.

Uma aplicação que consigo fazer com esse tipo de laço é na leitura de imagens de uma rede neural. Por exemplo, eu lerei todas as imagens de uma pasta de imagens, com dados que não foram lidos do meu dataset. Eu vou lendo as imagens e jogando para o treinamento da rede neural. Isso é feito em cada iteração da rede.

Eu também posso aplicar isso em uma situação onde o algoritmo de treinamento da rede vai rodar até que eu chegue em um valor pré-estabelecido, como a quantidade de épocas. Por exemplo, eu vou treinar por mil épocas e vou parar o treinamento, ou vou rodar meu treinamento dentro de um laço até que a acurácia da rede atinja 95%. Nesse caso, eu terei um comparador o tempo todo até que aconteça o que estou esperando.

Uma estrutura de repetição é muito importante para diversas aplicações envolvendo inteligência artificial, principalmente na fase de treinamento de um sistema de machine learning, como uma rede de deep learning.

### Exemplo Prático de `while`

Vou iniciar um contador. Meu contador vai iniciar valendo zero, que é o estado inicial dele.

Agora, vou colocar o meu laço `while`. Vou dizer que enquanto o meu contador for menor do que 10, vou incrementar o contador e vou imprimir o valor do meu contador.

```python
while contador < 10:
    print(valor do contador é, contador)
    contador += 1
```

Aqui vem a parte que eu vou incrementar o valor. A cada iteração, eu vou incrementar ele em mais um.

Vamos executar para vermos o que aconteceu.

A primeira vez, o contador valeu zero. Por que o contador começou em zero para entrar na minha tela? A primeira vez que vou imprimir o valor, meu sistema ainda não incrementou. Portanto, a primeira vez que ele vai imprimir, quando cai dentro do laço, é o valor zero. Depois, eu vou imprimir na minha tela o valor 1, porque eu já incrementei o contador. A cada iteração, o valor vai subindo: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

Se eu colocar o computador `while contador < 10`, ele para em 9. Se eu colocar `while contador <= 10`, então vamos fazer isso até que o contador chegue no valor 10. Eu posso colocar também um valor maior, por exemplo, o valor 100. Vou executar. O sistema vai imprimir os valores até o valor 100.

Uma estrutura de repetição bem simples. A base é entender como que acontece isso. Temos uma repetição dentro de uma condição do contador, que é enquanto o contador for menor e igual a 100, e isso vai ser executado até que aconteça o valor 100.

Como dei o exemplo para vocês, na área de IA, nos nossos algoritmos de machine learning de treinamento...

`⏱ 07:40`

### Condição de Treinamento de Algoritmos

É necessário definir uma condição para o ponto em que o algoritmo será treinado, ou seja, para a leitura das imagens da pasta durante o treinamento. Precisamos de condições para definir até que ponto o aprendizado deve ocorrer.

### Analogia do Aprendizado Humano

Um exemplo disso é em analogia. Podemos pensar até que ponto ensinamos uma pessoa um determinado conteúdo. Aplicamos uma prova, verificamos se o aluno aprendeu, e aí terminamos aquele conteúdo. Caso contrário, acabaríamos ensinando aquele conteúdo a vida toda.

### Aplicação em Deep Learning

Nas redes de *deep learning*, nas redes em geral de aprendizado de máquina, precisamos definir um ponto de parada.

Sempre estaremos rodando uma estrutura de repetição para o treinamento, para a leitura das imagens. Por hora, são os exemplos que tenho para colocar para vocês, mas teremos outras situações também, utilizando redes neurais ou outras redes que possuem essa condição de repetição.

O que eu queria mostrar para vocês, basicamente, são as estruturas de repetição.

Por hoje, este é o nosso conteúdo. Até uma próxima.

## Relacionado

- [[estruturas-de-repeticao-em-algoritmos-loops-for-e-while]]
- [[estruturas-de-repeticao-em-algoritmos-tipos-funcionamento-e-aplicacoes]]
