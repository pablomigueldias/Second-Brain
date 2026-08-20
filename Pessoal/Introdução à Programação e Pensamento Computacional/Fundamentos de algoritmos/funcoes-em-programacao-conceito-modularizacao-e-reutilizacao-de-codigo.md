---
titulo: "Funções em Programação: Conceito, Modularização e Reutilização de Código"
tags: [algoritmos, variaveis, conceitos, fundamentos, pensamento-computacional, estruturas-de-dados]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 7
conceitos: [Função, Modularização, Subprograma, Subalgoritmo, Subrotina, Assinatura da Função, Parâmetros]
---

# Funções em Programação: Conceito, Modularização e Reutilização de Código

> [!resumo] Do que se trata
> A aula aborda o conceito de funções, explicando que elas são blocos de instruções que realizam tarefas específicas e são sinônimas de subprograma, subalgoritmo ou subrotina. É detalhada a importância da modularização, que torna o código mais legível, conciso e permite a reutilização de código. Por fim, o fluxo de execução e a assinatura da função são explicados, mostrando como o código é modularizado para ganho de manutenção.

## Para lembrar

- **Funções são blocos de instruções que realizam tarefas específicas e são identificadas por nome e parâmetros.**
- **A modularização do código torna-o mais claro, conciso e permite a reutilização de código, evitando a necessidade de copiar e colar trechos de código.**
- **A assinatura de uma função é determinada pelo nome da função e pelos parâmetros que ela possui.**
- **As variáveis utilizadas dentro de uma função são desalocadas da memória no momento em que a função retorna o resultado para o programa principal.**
- **O fluxo de execução de uma função envolve: 1) envio de dados, 2) processamento, e 3) retorno do resultado esperado.**

## O que esta nota responde

- O que são funções em programação e por que usá-las?
- Qual é o ganho prático de modularizar um algoritmo usando funções?
- Como funciona o fluxo de execução e a assinatura de uma função?

## Conceitos

**Função** · **Modularização** · **Subprograma** · **Subalgoritmo** · **Subrotina** · **Assinatura da Função** · **Parâmetros**

## Conteúdo

`⏱ 00:00`

Muito bem. Vamos falar sobre o que são funções.

As funções vêm da ideia da matemática. A computação, na verdade, é muito baseada na matemática. Os matemáticos tiveram uma grande contribuição. O pai da computação, Alan Turing, era matemático. Temos aí muitas analogias, mas vamos seguir o conceito.

#### Conceitos e Sinônimos

As funções também têm outros nomes. Elas são conhecidas como:

- Subprograma
- Subalgoritmo
- Subrotina
- Método
- Bloco

O termo "método" está muito dentro do conceito de Programação Orientada a Objeto, mas todos são sinônimos e querem trazer a mesma ideia: a ideia de função. Quando falamos da técnica modular em lógica, associamos o conceito à função.

De forma geral, uma função implica que um elemento A seja conectado a um elemento de um conjunto B. Ou seja, a partir de um argumento que ela recebe, ela vai retornar um valor realmente associado a esse conceito.

#### Definição Formal de Funções

As funções ou subrotinas são blocos de instruções que realizam tarefas específicas. São trechos de código com objetivos específicos que podem ser chamados dentro do seu código principal.

Isso vem da ideia de decomposição de algoritmos, de você modular o seu algoritmo e torná-lo mais legível. Além disso, permite utilizar o reaproveitamento de código.

##### Por que modularizar?

Algumas pessoas pensam: "Não é mais fácil fazer tudo junto? Deixa tudo lá bonitinho, tudo no mesmo local?" Para quem está iniciando, pode ser um pouco complicado, mas com o tempo você pega o jeito.

A modularização traz vários benefícios:

- O código fica mais claro e mais conciso.
- Fica mais limpo e mais legível.
- Permite a reutilização de código.

Imagine que você tem uma mesma operação utilizada em pontos diferentes dentro do seu programa. Em vez de você copiar e colar aquele trecho de código, você utiliza uma função. O trecho vai ficar exatamente ali, e se você precisar fazer alguma alteração dentro dessa função, você só precisa alterar em um ponto, e não em N pontos distintos dentro do seu programa principal.

#### Componentes e Assinatura da Função

Voltando à definição formal, são blocos de instruções, códigos, e eles são identificados por nomes e parâmetros.

A **assinatura da função** é determinada pelo nome da função e pelos parâmetros que ela possui.

O que está atrelado a uma função é:

1.  **A definição:** O objetivo que ela possui.
2.  **O nome da função:** O identificador que será usado para invocá-la.
3.  **Os parâmetros:** As variáveis que ela vai utilizar.

É importante notar que essas variáveis são utilizadas apenas dentro da função e são destruídas no momento em que a função retorna o resultado para o programa principal. Elas são desalocadas da memória.

#### Fluxo de Execução

O fluxo é o seguinte:

1.  Os dados são enviados para a função.
2.  A função executa o processamento.
3.  A função retorna o resultado esperado pela operação proposta.

A função efetivamente altera o estado do programa.

Para finalizar, vamos determinar a sintaxe através de uma função e ver qual o ganho que temos ao fazer essa modificação.

`⏱ 05:00`

Este é um exemplo para estarmos sempre treinando. Estou utilizando a parte de média escolar para que possamos perceber o que essas modificações acarretam de ganho no nosso algoritmo, nesse caso, a reutilização de código.

Eu tenho a função `média_escolar` e eu inicializei uma variável com o resultado igual a zero. O meu resultado será nota 1 mais nota 2 dividido por 2.

O retorno... Ao invés de eu escrever exatamente isso aqui três vezes, eu chamo a função para os alunos distintos. Olha o ganho: estamos reutilizando o código. E se por acaso a minha média mudar? Ao invés de eu mudar em três locais diferentes, eu vou estar modificando apenas dentro da função. Eu tenho um ganho muito grande em termos de manutenção e de escrita de código.

### O Conceito de Função

A função é pegar um trecho de código em que você vai utilizá-lo algumas vezes e colocar em um espaço específico, modulando o seu código de maneira que você possa reutilizá-lo dentro do seu programa. É só isso.

Como vimos, existem diversos ganhos atrelados. Bora para a próxima etapa?

## Relacionado

- [[visao-geral-da-carreira-em-ti-da-rede-a-ciencia-de-dados-e-programacao]]
- [[conceitos-fundamentais-de-logica-e-logica-de-programacao]]
- [[fundamentos-de-algoritmos-variaveis-tipos-de-dados-e-estruturas-de-controle]]
- [[fundamentos-e-pilares-do-pensamento-computacional]]
