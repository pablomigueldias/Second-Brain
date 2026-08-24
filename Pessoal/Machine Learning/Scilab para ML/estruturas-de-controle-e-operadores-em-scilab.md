---
titulo: "Estruturas de Controle e Operadores em Scilab"
tags: [conceitos, estudo, scilab-para-ml, linguagens-de-programacao, operadores, algoritmos, variaveis]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 27
conceitos: [Estrutura Condicional, Operadores Relacionais, Operadores Lógicos, Atribuição vs. Comparação, Scilab, Subplot, Vetores e Matrizes]
---

# Estruturas de Controle e Operadores em Scilab

> [!resumo] Do que se trata
> A aula demonstra o uso de estruturas condicionais (`if`, `then`, `else`) em Scilab, aplicando-as em exemplos práticos como cálculo de área e comparação de variáveis. Em seguida, são abordados os operadores lógicos (E, OU, Negação) e o uso de `subplot` para a construção de múltiplos gráficos em uma única janela.

## Para lembrar

- **Em uma estrutura condicional, uma condição deve ser satisfeita para que um conjunto de comandos seja executado; caso contrário, são executados comandos correspondentes no bloco `else`.**
- **Para verificar se dois números são iguais, deve-se usar o operador de comparação `==`, e não o operador de atribuição `=`.**
- **Os operadores lógicos incluem o E lógico (`&`), o OU lógico (verificação de alguma das variáveis A ou B) e a Negação (`~`).**
- **Para gerar múltiplos gráficos na mesma janela em Scilab, deve-se utilizar o comando `subplot`.**

## O que esta nota responde

- Como implementar uma lógica de decisão em um programa Scilab?
- Qual a diferença entre atribuir um valor e comparar valores em Scilab?
- Como realizar operações lógicas complexas (E, OU, Negação) e gerar múltiplos gráficos em Scilab?

## Conceitos

**Estrutura Condicional** · **Operadores Relacionais** · **Operadores Lógicos** · **Atribuição vs. Comparação** · **Scilab** · **Subplot** · **Vetores e Matrizes**

## Conteúdo

`⏱ 00:00`

### Estruturas Condicionais no Scilab

A ideia agora é ver um pouco sobre estrutura condicional, trabalhando com `if`, `then` e `else`. Quem programa em linguagens como C ou Python já sabe muito bem como usar essas estruturas. Faremos um exemplo para ter uma noção de como aplicá-las dentro do Scilab.

Em uma estrutura condicional, temos uma condição: se ela é satisfeita, é executado um conjunto de comandos; se não, executam-se outros comandos correspondentes.

### Exemplo: Cálculo da Área de uma Sala

O exemplo a ser desenvolvido é o cálculo da área de um quadrado. O programa vai avaliar se o valor informado pelo usuário é maior do que zero para realizar o cálculo, pois não existe uma sala de aula com lado negativo ou nulo.

A construção do código segue os seguintes passos:

- Definir a variável de entrada `lado`, utilizando a função `input`.
- Colocar a pergunta entre aspas para o usuário: `"Informe a medida do lado da sala"`.
- Finalizar a linha com ponto e vírgula e ir para a linha de baixo.
- Inserir a estrutura `if`, que já se autocompleta com `then` e `end`.
- Estabelecer a condição de comparação: `lado > 0`.
- Dentro do bloco condicional, calcular a área: `area = lado * lado`.
- Imprimir o resultado com a função `printf`, passando o texto `"A área da sala"`, o especificador `%f`, seguido de vírgula e da variável `area`.
- Fechar com ponto e vírgula e adicionar o bloco `else`.
- No `else`, utilizar outro `printf` para exibir a mensagem informando que o valor digitado é inválido.

### Salvando e Executando o Programa

O programa é salvo na pasta `Scilab Exemplos` com o nome `exemplo 2`.

Ao executar o programa no terminal:

- O sistema solicita a medida do lado da sala. Informando o valor `2`, o resultado exibido para a área da sala é `4`.
- Ao executar o código novamente e inserir o valor `-1`, o programa indica que o valor informado é inválido, por se tratar de um número menor do que zero.

### Verificação de Igualdade entre Dois Números

Outro exemplo possível de estrutura condicional é verificar se dois números são iguais. 

Para a primeira entrada do programa:
- Definir a variável `n1` recebendo uma entrada via `input`.
- Solicitar a informação ao usuário: `"Informe o primeiro número"`.

`⏱ 05:20`

Vou colocar dois pontos aqui e vou fechar meu programa. Agora eu vou colocar `N2`. `N2` é igual a uma entrada também. Vou definir para o usuário informar: "Informe o segundo número". Vou fechar aqui.

### Comparação de Variáveis

Agora eu vou comparar com um `if` e vou colocar: `N1 == N2`.

A gente lembra que, lá em C, quando a gente coloca um igual (`=`), a gente está dizendo que uma variável é igual a outra (atribuição). Agora, quando a gente coloca dois sinais de igual (`==`), a gente está fazendo uma comparação.

Se `N1` é igual a `N2`, eu estou comparando se `N1` é igual a `N2`.

Agora eu vou printar aqui, vou dar um `printf`. Então eu vou dizer que "Os números fornecidos são iguais". E eu vou colocar agora um `else` para dizer que, se eles não forem iguais, eu vou dizer que são diferentes.

`printf("Os números fornecidos são diferentes")`.

Vou fechar aqui com dois pontos, vou salvar o meu programa e vou executar.

Executei, vou lá na minha área de trabalho do SciLab.

Informe o primeiro número. Coloco o primeiro número: 4.
Informe o segundo número. Vai dizer que ele é 4 também.
Resultado: "Os números fornecidos são iguais".

Se eu rodar de novo o meu programa aqui, vou executar novamente. Ele vai pedir que eu informe o número. Vou colocar 4 e vou colocar agora 5.
Resultado: "Os números fornecidos são diferentes".

Nosso programa de comparação está feito. É uma estrutura condicional.

### Operadores Relacionais

Agora, a gente vai ver um pouco sobre operadores relacionais. Os operadores relacionais trazem para a gente relações entre variáveis, basicamente.

A gente tem aqui os operadores:

- `==`: Significa igual a.
- `!=`: Operador de diferente (til e sinal de igual).
- `>`: Operador de maior.
- `>=`: Operador de maior ou igual.
- `<`: Operador de menor.
- `<=`: Operador de menor ou igual.

Esses operadores servem para a gente fazer essas comparações.

Por exemplo, eu estou comparando se os meus valores são iguais. Eu poderia colocar aqui o `!=` e o valor de igual.

Eu estou comparando se o valor digitado inicialmente e o segundo valor são diferentes. Eu posso comparar também se `N1` é maior do que `N2`.

Eu posso também comparar se `N1` é maior ou igual a `N2`.

Eu posso comparar se `N1` é menor ou igual a `N2`.

Eu coloquei todas as comparações possíveis. Os operadores relacionais vão trazer para a gente essa resposta.

Se eu colocar, por exemplo, o caso `N1` é maior do que `N2`, eu vou comparar se `N1` é maior do que `N2`. Se `N1` é maior que `N2`, eu vou dizer que sim, é maior. Se não for, eu vou colocar não, é menor.

Vou salvar o meu programa aqui e vou dar play.

Vou ir lá na minha área de trabalho.
Informe o primeiro número: 5.
Informe o segundo número: 2.
Resultado: "Sim, N1 é maior do que N2".

Se eu colocar o inverso, vou dar um play aqui de novo. Colocar o inverso: 2 e...

`⏱ 11:00`

Ele vai indicar: não, é menor; `N1` é menor do que `N2`.

### Operadores Lógicos

Voltando à apresentação, também aplicamos os operadores lógicos. Eles trazem um cenário de funções lógicas no qual conseguimos realizar operações matemáticas, como o E lógico, o OU lógico e a lógica negada.

Temos basicamente estes operadores:
- **E lógico:** representado pelo e comercial (`&`).
- **OU lógico:** verifica se alguma das variáveis `A` ou `B` tem um valor correspondente.
- **Negação:** representada por meio de um til (`~`).

No primeiro exemplo com o E lógico, verificamos se `A` é maior que zero e também se `A` é menor do que 10.

No caso do OU, podemos comparar se `A` é igual a zero ou se `B` é igual a zero. Estamos comparando o valor de duas variáveis com o valor zero utilizando o operador lógico OU.

Também podemos negar uma variável. A operação verifica se o valor da variável `A` não é menor que zero, o que é equivalente à condição de `A` ser maior ou igual a zero. A negação de `A` menor que zero resulta no mesmo que afirmar que `A` é maior ou igual a zero, realizando uma comparação lógica.

### Comportamento Matemático dos Operadores

Os operadores lógicos trabalham de forma matemática. Considerando as variáveis `A` e `B`:

Na lógica E (equivalente a uma multiplicação, onde Verdadeiro é 1 e Falso é 0):
- Verdadeiro e Verdadeiro (`1 * 1`): Verdadeiro (1)
- Verdadeiro e Falso (`1 * 0`): Falso (0)
- Falso e Verdadeiro (`0 * 1`): Falso (0)
- Falso e Falso (`0 * 0`): Falso (0)

Na lógica OU (equivalente a uma soma):
- 1 mais 1: em lógica binária, resulta em 1
- 1 mais 0: resulta em 1
- 0 mais 1: resulta em 1
- 0 mais 0: resulta em 0

Na operação de negação:
- O valor Verdadeiro vira Falso.
- O valor Falso vira Verdadeiro.

### Exemplo Prático com Condicionais

Neste exemplo, entramos com valores para `A`, `B` e `C` e fazemos uma verificação com `if`: `A` é maior do que `B`?

- A variável `A` vale 2.
- A variável `B` vale 3.

Como `A` não é maior do que `B` (é menor), o fluxo entra no caso do `else`. Em seguida, compara-se se `B` é maior do que `C`. Sendo `B` maior do que `C`, o programa imprime esse valor de `B`.

Os operadores lógicos realizam essas comparações entre valores para estruturar a tomada de decisão.

`⏱ 16:00`

Também conseguimos fazer comparações de valores entre matrizes, entre vetores e comparar uma imagem com a outra por meio de operações lógicas.

### Construção de Gráficos

Falando um pouco da construção de gráficos, temos alguns exemplos. Vamos fazer um gráfico que realiza uma interpolação entre dois valores, `x` e `y`, fazendo uma comparação par a par entre os valores, ou seja, entre pares ordenados de valores de dois vetores, para vermos como ele se comporta.

O valor de `x` vai ser igual a -3, -2, -1, 0, 1, 2 e 3. 

Agora, o meu `y` vai ser 9, 4, 1, 0, 1, 4, 9. 

Esses são os meus dois vetores de entrada. Faltou o ponto e vírgula aqui. 

Agora vou plotar `x` e `y`, dando um comando `plot(x, y)`. Para visualizar, vou salvar e dar um play. O gráfico de exemplo foi gerado. Vou aumentar um pouquinho o tamanho dele. Estou comparando par a par valores de dois vetores e gerando o gráfico.

Caso queira gerar o gráfico de treinamento de uma rede, posso comparar o valor de acerto da rede com o valor de erro e gerar o gráfico da função de validação (*validation*). É possível plotar e ver como o erro está se comportando ao longo do tempo. Quando tenho dois valores, como a acurácia e o erro, consigo traçar e plotar esse gráfico.

### Gráfico de Funções Trigonométricas

Vamos para outro exemplo. Também podemos gerar um gráfico para representar senos e cossenos. É um programa um pouco maior, mas podemos desenvolvê-lo aqui.

Vou entrar com o valor desse gráfico em `x`, que vai ser 0.14 multiplicando o valor de `pi`.

Agora vou entrar com o valor da variável `y1`, que vai ser o seno de `x`, sendo `x` o valor definido anteriormente.

Em seguida, vou definir o valor de `y2`, que é a segunda variável, correspondendo ao cosseno de `x`.

Agora vou plotar `x`, `y1` e esse valor de `b`. Vou colocar o ponto e vírgula e copiar e colar para plotar também para `y2`.

Em seguida, vou definir o título do gráfico, que é o nome exibido na barra superior: "funções seno e cosseno".

Depois, vou definir o `label` para o eixo x do gráfico, indicando "eixo x". O mesmo farei para o eixo y, apenas mudando a variável para y e inserindo a identificação "eixo y". 

E agora eu tenho a minha legenda.

`⏱ 22:00`

### Geração de Gráficos e Subplot

E agora eu vou dar um ponto e vírgula aqui também. Vamos executar para ver se ficou certinho.

Pronto, geramos o nosso gráfico representando seno e cosseno desse valor que definimos para `y`. Basicamente, estamos gerando um gráfico para ver o comportamento de uma função que trabalha com senos e cossenos. É um problema que colocamos aqui só para ver o gráfico, mas isso é legal para vermos o comportamento gráfico do Scilab.

Deixa eu expandir de novo a minha tela aqui. Esse é o gráfico que gerou para a gente.

Também podemos gerar gráficos na mesma janela. Quando vamos comparar vários valores, não é preciso gerar um gráfico de cada vez; é possível gerar todo mundo de uma vez só.

Para isso, ao invés de plotar um gráfico com a função `plot`, é só usar a `subplot`. Quantos gráficos forem colocados para plotar, eles vão todos plotar na mesma janela.

Aqui, por exemplo, temos:
- uma função quadrática;
- uma função cúbica;
- uma função de seno;
- uma função quadrática;
- outra função cosseno.

### Operações com Matrizes

Agora vamos ver a parte de operações com matrizes. A parte de operação com matrizes é muito importante, principalmente quando falamos de redes neurais. Redes neurais convolucionais utilizam matrizes para percorrer a nossa imagem, sendo muito importante utilizarmos essa ferramenta do Scilab para trabalhar com matrizes, principalmente se tivermos uma aplicação dessas.

Uma matriz é definida desta forma: eu consigo definir uma matriz atribuindo o valor para a variável, que é a matriz `A`. Se eu coloco `1, 2, 3`, significa que é a primeira linha da matriz. A vírgula vai separar a coluna e o ponto e vírgula vai separar a linha.

Vamos fazer um exemplo aqui para não ficar confuso. Minha matriz, que vou chamar de matriz `A`, vai ser igual a `1, 2, 3; 4, 5, 6; 7, 8, 9`. Defini a minha matriz igual ao exemplo aqui. 

Ao dar um Enter, a matriz foi lida no meu programa.

Agora, vou colocar aqui como matriz `B` a mesma matriz.

O que eu posso fazer agora é multiplicar essas matrizes: matriz `A` vezes matriz `B`. Assim, eu tenho a multiplicação das matrizes. Para quem lembra da parte matemática de multiplicar matriz, é uma coisa um pouco chata, e vemos o quanto o Scilab consegue fazer essa multiplicação de forma instantânea. 

A parte de matrizes também é bem tranquila.

### Estruturas de Repetição

Agora vamos ver um pouco de estruturas de repetição.

## Relacionado

- [[estruturas-condicionais-em-python-simples-compostas-e-aninhadas]]
- [[instalacao-operacoes-basicas-e-estruturas-de-programacao-no-scilab]]
- [[estruturas-condicionais-e-operadores-logicos-em-algoritmos]]
- [[paradigmas-de-programacao-estruturado-e-orientacao-a-objetos]]
