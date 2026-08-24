---
titulo: "Estruturas de Repetição com While no Scilab e Introdução ao Processamento de Imagens"
tags: [machine-learning, algoritmos, linguagens-de-programacao, caso-pratico, ferramentas]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 9
conceitos: [Laço while, Variável acumuladora, SciNotes, Condição de parada, Processamento de imagens, Visão computacional]
---

# Estruturas de Repetição com While no Scilab e Introdução ao Processamento de Imagens

> [!resumo] Do que se trata
> A aula demonstra a implementação de estruturas de repetição utilizando o laço while no ambiente SciNotes do Scilab para acumular valores até uma condição de parada. Apresenta a analogia desse fluxo de repetição com o treinamento iterativo de redes neurais baseado em critérios de acurácia. Por fim, introduz o uso de toolboxes no Scilab voltadas para processamento de imagens e visão computacional.

## Para lembrar

- **No Scilab, o laço while repete um bloco de código delimitado por end enquanto a condição lógica de teste permanecer verdadeira.**
- **A leitura de dados pelo teclado no SciNotes é realizada com o comando input e a exibição formatada de inteiros na tela utiliza o printf com o especificador %d.**
- **O treinamento de redes neurais utiliza a mesma lógica de repetição com laços iterativos até atingir um critério de parada, como uma acurácia pré-determinada.**
- **O Scilab suporta módulos adicionais via toolboxes específicas para image processing e computer vision para execução de rotinas de processamento de imagens.**

## O que esta nota responde

- Como estruturar um laço while com acumulador de soma e condição de parada no Scilab?
- De que forma o laço de repetição se relaciona com o treinamento e épocas de uma rede neural?
- Quais toolboxes são utilizadas no Scilab para trabalhar com visão computacional e processamento de imagens?

## Conceitos

**Laço while** · **Variável acumuladora** · **SciNotes** · **Condição de parada** · **Processamento de imagens** · **Visão computacional**

## Conteúdo

`⏱ 00:00`

### Estruturas de Repetição

Nas estruturas de repetição, lidamos com situações em que precisamos repetir a mesma função por determinado período ou de forma iterativa. Nesses casos, vamos somando uma variável ou utilizando um contador para registrar a quantidade de vezes que a execução passa por dentro do laço, de maneira semelhante ao que ocorre em C e em Python.

### Exemplo de Soma com o Laço `while`

Temos a estrutura de laço `while` aplicada a um programa que lê números inteiros do teclado até que o número zero seja inserido:

- O programa captura as entradas do teclado até que a variável informada seja igual a zero.
- Enquanto o valor for diferente de zero, o fluxo permanece dentro do laço para a digitação dos valores.
- Ao sair do laço — quando a entrada for igual a zero —, o programa entrega a soma de todos os valores que foram digitados.

### Construção do Código no SciNotes

A implementação do programa dentro do `SciNotes` segue os seguintes passos:

- Definir a variável inicial acumuladora: a primeira linha estabelece que `total = 0`.
- Definir a primeira entrada do teclado associada à variável `x`, solicitando a mensagem `"digite o primeiro"` (incluindo dois pontos e um espaço para formatar a entrada de dados).
- Abrir o laço `while` verificando a condição de `x` ser diferente de zero.
- Dentro do laço, realizar a soma cumulativa definindo `total = total + x`, somando a variável acumuladora com o valor de entrada atual.
- Atualizar a variável `x` com um novo comando de `input`, exibindo a mensagem `"digite mais um valor ou zero para terminar a soma"`, fechando a linha com ponto e vírgula.
- Encerrar o bloco de repetição com o comando `end`.
- Imprimir o resultado na tela utilizando o `printf`, formatando a mensagem `"a soma dos números informados é"`, utilizando `%d` para projetar o valor numérico e passando a variável `total`.

### Execução e Teste no Scilab

Ao salvar o arquivo e executá-lo na área de trabalho do `Scilab`, o programa faz a leitura sequencial dos valores informados, por exemplo: `5`, `1`, `7`, `1` novamente e `3`. Quando o valor `0` é digitado, a repetição se encerra e o programa exibe a soma total de todos os números inseridos.

Essa lógica baseada em laço de repetição é a mesma empregada em aplicações mais avançadas, como no treinamento de uma rede neural, onde ocorrem diversas iterações e épocas de processamento dentro de uma estrutura de repetição.

`⏱ 05:40`

Até chegar em uma condição. Por exemplo, meu treinamento chegou a 90%, para mim é suficiente e vou terminar o treinamento, porque ele já atingiu uma boa acurácia. Existem várias condições em que vamos usar um laço de repetição.

### Processamento de Imagens no Scilab

Falando um pouco agora da parte de processamento de imagens, o algoritmo trabalha dentro do `Scilab` com a *toolbox* instalada para processamento de imagens. 

Instalei essa *toolbox* de `image processing` e também instalei uma outra, que é um módulo específico para `computer vision`. Estou trabalhando aqui com processamento de imagem e visão computacional.

Ao entrar no `help`, temos alguns exemplos. A partir de agora, vamos rodar alguns exemplos disponíveis dentro do próprio `Scilab` para a parte de visão computacional e processamento de imagens.

O que aconteceu com você?

## Relacionado

- [[estruturas-de-repeticao-em-algoritmos-tipos-funcionamento-e-aplicacoes]]
- [[estruturas-de-repeticao-em-algoritmos-loops-for-e-while]]
- [[estruturas-de-repeticao-loops-e-aplicacoes-em-treinamento-de-machine-learning]]
