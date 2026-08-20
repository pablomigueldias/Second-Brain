---
titulo: "Fundamentos de Algoritmos: Variáveis, Tipos de Dados e Estruturas de Controle"
tags: [fundamentos, pensamento-computacional, raciocinio-logico, conceitos, dados, variaveis, algoritmos]
data: 2026-08-19
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 11
conceitos: [Algoritmo, Variável, Constante, Tipos de Dados Primitivos, Numérico, Caractere (String), Booleano (Lógico), Processamento de Dados]
---

# Fundamentos de Algoritmos: Variáveis, Tipos de Dados e Estruturas de Controle

> [!resumo] Do que se trata
> Esta aula aborda os fundamentos de algoritmos, começando pela tipologia de dados (numérico, caractere, booleano) e a função das variáveis como estruturas mutáveis. São explorados os conceitos de constantes, o papel das variáveis em ação e controle, e o processamento de dados através de instruções e operações.

## Para lembrar

- **Os dados são o objeto de manipulação e processamento do computador, enquanto as instruções são as normativas ou diretivos utilizados para processar esses dados.**
- **Os tipos primitivos de dados são: numérico (inteiros e reais), caractere (string) e booleano (lógico), sendo o booleano atrelado à lógica booleana com apenas dois resultados possíveis: verdadeiro ou falso.**
- **Uma variável é uma estrutura mutável que pode receber e modificar seu valor, mas está restrita ao seu tipo de dado. Uma constante, por outro lado, é um valor fixo e inalterável.**
- **O nome de uma variável deve seguir boas práticas, sendo ideal que ele tenha sentido (ex: `nome_de_usuário`) e não deve utilizar palavras reservadas de uma linguagem de programação.**
- **Dentro do algoritmo, uma variável pode ter papel de Ação (modifica o estado do algoritmo/programa) ou de Controle (utilizada para controlar uma estrutura ou equação).**

## O que esta nota responde

- Qual é a função básica do computador em relação aos dados e às instruções?
- Qual a diferença entre variáveis e constantes em um algoritmo?
- Quais são os tipos de dados primitivos que um algoritmo deve conhecer?

## Conceitos

**Algoritmo** · **Variável** · **Constante** · **Tipos de Dados Primitivos** · **Numérico** · **Caractere (String)** · **Booleano (Lógico)** · **Processamento de Dados**

## Conteúdo

`⏱ 00:00`

É muito bem. Nossa terceira aula é focada nos fundamentos de algoritmos.

O foco desta aula é passar conceitos básicos, como variáveis, tipos de dados, instruções, condições e toda a gama de conceitos que vão auxiliar na construção de um algoritmo.

A estrutura do conteúdo será a seguinte:

- A primeira etapa é sobre tipologia e variáveis.
- Na segunda, estaremos falando de instruções primitivas.
- Na terceira etapa, estruturas condicionais e operadores.
- Quarta, estrutura de repetição.
- Quinta, vetores e matrizes.
- Sexta, o que são funções.
- E na sétima, instruções de entrada e saída.

Vamos começar pela tipologia e variáveis.

Qual é a função do computador? É processar as informações que nós passamos para ele. Essas informações são compostas por dois tipos de conteúdos:

1. Os dados. São dados puros, o objeto de manipulação e de processamento do computador.
2. As instruções. São as normativas, os diretivos utilizados pelo computador para executar determinadas ações que irão processar aqueles dados.

Essa é a função do computador. Os dados são tratados e processados, mas quais são os tipos existentes? Temos o numérico, os caracteres e os lógicos. Esses são os tipos primitivos, os tipos básicos de dados.

O tipo mais comum é o numérico, onde temos os inteiros e os reais. Podemos usar tipos como `int`, `long` ou `float` para representar números reais. Cada um tem sua peculiaridade, mas vamos focar em inteiros e reais.

Os inteiros são todos os números positivos ou negativos que não possuem casas decimais.

Os reais são todos os números que compõem o nosso espectro de tipo numérico, sendo positivos e negativos com casas decimais.

O caractere é tudo aquilo que não representa um número. Até o próprio número pode ser um caractere. As letras têm uma representação específica por aspas duplas. Para designar, por exemplo, "programação", isso seria uma *string*, e não apenas um caractere.

Um caractere tem um limite de tamanho. Quando utilizamos esse tipo de dado na programação, o computador acaba convertendo para um valor numérico, visto que ele entende como zero e um em qualquer instrução. Qualquer instrução que passamos via linguagem de programação, quando compilada e levada para um código de mais baixo nível, será interpretada pelo computador como zero e um.

Além dos tipos numérico e caractere, temos o booleano, o lógico. Ele está atrelado à lógica booleana, e dentro dela, temos apenas dois tipos de resultados possíveis: verdadeiro ou falso.

Verdadeiro seria 1, e falso seria 0. Dentro do português estruturado, seria ponto `V` ou ponto `S` para verdadeiro, e ponto `F` ou ponto `N` para falso.

Assim, definimos os tipos de dados existentes.

Quando queremos utilizar esses dados dentro de um programa, como fazemos isso? Através de variáveis.

O que é uma variável? É um tipo de estrutura mutável. Ela pode variar em seu valor, ela é inconstante. Ela pode receber, pode ser sobrescrita, pode receber mais de um valor e modificar seu conteúdo.

Ela é instável, incerta. Ela irá receber um valor que não se sabe qual, mas sabe o tipo.

`⏱ 05:40`

Uma variável é uma estrutura que irá receber um tipo de dado, mas que não tem certeza do seu valor. Por exemplo, a variável pode assumir qualquer um dos valores de um determinado conjunto de valores, contudo ela está restrita ao seu tipo.

Se uma variável é do tipo numérico, ela vai receber numérico. Se é do tipo `string`, ela vai receber `string`, e assim por diante.

Vamos supor: `a + b = c` e `a - b = d`. Neste caso, `c` vai receber o somatório de `a` e `b`, e `d` vai receber a subtração de `a` e `b`. Eu sei que o tipo é, mas eu não tenho certeza do valor que irei receber. Isto é uma variável.

Pensa numa variável como uma caixinha dentro de uma sucessão de armários, em que ela vai identificar um determinado conteúdo, um determinado dado e o tipo daquele dado. Essa daí seria uma analogia interessante para você identificar o que é uma variável.

### Nomenclatura e Tipos de Variáveis

O nome da variável segue regras, ou, melhor dizendo, boas práticas. O ideal é que você atribua um ou mais caracteres, ou seja, que você dê sentido para aquela variável. Não simplesmente atribua `x` ou `x.igual a x`.

Pode colocar matrícula, CPF ou então e-mail. Esses nomes de variáveis devem dizer algo, que significa uma coisa, sem espaços em branco. É vedada a utilização de palavras reservadas de uma determinada linguagem de programação.

Uma variável pode receber caracteres, números, inclusive também tipo booleano.

Alguns exemplos de nomes possíveis para uma variável são: `x2`, `nome_de_usuário`, `underline_telefone`, `user12`, `z4`. Não quer dizer que seriam bons nomes. Acho que o único aqui é `nome_usuário` e `telefone` que quer dizer alguma coisa.

### Papel da Variável: Ação e Controle

Dentro desse contexto, a variável possui um papel. Ela pode ser de ação ou pode ser de controle.

*   **Ação:** É quando ela modifica o estado do algoritmo, o estado do programa.
*   **Controle:** É quando ela é utilizada para controle de alguma estrutura, de alguma estrutura dentro do algoritmo, do programa, ou então dentro de alguma equação.

### Constantes vs. Variáveis

Temos associado à variável o fato de ela ser inalterável, ou seja, o que não muda, a variável. Na verdade, tudo aquilo que é fixo ou estável, isso daqui já é uma constante e não uma variável.

Existem alguns tipos de constantes que podemos estar definindo, e podemos utilizar uma variável para definir uma constante. Por exemplo, eu posso dar o nome da minha variável de `pi` e `pi` recebe um valor que não será modificado: `3.14`. Outra variável recebe o nome de `Phi` e ela vai receber `1.618`.

E aí eu vou ter uma variável que vai receber uma variável chamada `recebido`. E aí uma constante `0.10`. Essa daqui vai ser sempre se manter desse jeito, a não ser que eu modifique.

A ideia da constante é ser inalterável, diferente da variável que pode sim variar.

### Processamento de Dados

Qual o objetivo que os dados são tratados e processados? As instruções, o que são? São exatamente as operações que vão processar esses dados. Para falar disso, nós vamos para a próxima etapa.

## Relacionado

- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
- [[visao-geral-da-carreira-em-ti-da-rede-a-ciencia-de-dados-e-programacao]]
- [[fundamentos-e-pilares-do-pensamento-computacional]]
- [[tecnicas-de-logica-de-programacao-linear-estruturada-e-modular]]
