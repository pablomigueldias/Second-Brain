---
titulo: "Modelagem de Dados: Projeto Conceitual, Representação e Propósito"
tags: [modelagem-de-dados, banco-de-dados, conceitos, fundamentos, dados, sgbd, sql]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 6
conceitos: [Design de Banco de Dados, Projeto Conceitual, Linguagem Textual (Modelagem), Linguagem Gráfica (Modelagem), Modelo Entidade-Relacionamento, Modelagem de Dados, Coleta de Dados, Análise de Dados]
---

# Modelagem de Dados: Projeto Conceitual, Representação e Propósito

> [!resumo] Do que se trata
> A aula detalha o design de banco de dados, focando no projeto conceitual como um modelo de alto nível para persistência de dados. Ela explora as linguagens textual e gráfica para representação de modelos, destacando o Modelo Entidade-Relacionamento para visualização. Além disso, aborda o propósito da modelagem como representação de fenômenos e os primeiros passos de coleta e análise de dados, considerando requisitos, perguntas e visões distintas.

## Para lembrar

- **O projeto conceitual é um modelo de alto nível no design de banco de dados, que define o que o projeto físico precisará ter.**
- **A representação de modelos pode ser textual para definir requisitos iniciais e gráfica, utilizando o Modelo Entidade-Relacionamento, para auxiliar na visualização.**
- **Modelar significa representar ou criar uma referência de um fenômeno, seja computacional ou matemático, para permitir sua análise.**
- **O primeiro passo em um projeto conceitual envolve a coleta de dados e a análise para refinar as informações.**
- **A fase de análise de dados verifica se as informações coletadas são suficientes para atender aos desejos do cliente, definindo a importância de atributos e os tipos de relacionamento entre objetos.**

## O que esta nota responde

- O que é o projeto conceitual no design de banco de dados?
- Quais são as formas de representar modelos de dados e quando cada uma é utilizada?
- Qual o propósito da modelagem de dados e quais são os primeiros passos em um projeto conceitual?

## Conceitos

**Design de Banco de Dados** · **Projeto Conceitual** · **Linguagem Textual (Modelagem)** · **Linguagem Gráfica (Modelagem)** · **Modelo Entidade-Relacionamento** · **Modelagem de Dados** · **Coleta de Dados** · **Análise de Dados**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Projeto conceitual: representação e propósito | ▪▪ |
| `04:20` | Projeto conceitual: coleta e análise | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Projeto Conceitual** | Aquele modelo de alto nível que foi mencionado anteriormente. |
| **Modelar** | Representar; criar uma referência. |
| **Análise** | Verificar se todas as informações coletadas têm a base necessária para criar o que o cliente deseja. |

## Teste-se

<details><summary>Qual é o foco principal da parte de design de banco de dados abordada?</summary>

O foco principal é o projeto conceitual, um modelo de alto nível.

</details>

<details><summary>Quais são as duas maneiras mais comuns de representar ou apresentar um modelo?</summary>

As duas maneiras mais comuns são a linguagem textual e a linguagem gráfica.

</details>

<details><summary>Qual é o objetivo principal da linguagem de modelagem de dados?</summary>

O objetivo principal é representar os dados, criando uma referência para análise.

</details>

<details><summary>Quais são os dois primeiros passos dentro de um projeto conceitual?</summary>

Os dois primeiros passos são a coleta de dados e a análise.

</details>

<details><summary>O que a fase de análise busca verificar?</summary>

A análise verifica se as informações coletadas têm a base necessária para criar o que o cliente deseja, definindo a importância de atributos e o tipo de relacionamento.

</details>

<details><summary>Além de requisitos, o que mais deve ser considerado na etapa de análise de um projeto conceitual?</summary>

Também devem ser consideradas perguntas a serem respondidas e visões a serem representadas.

</details>

## Conteúdo

`⏱ 00:00`

Já entendemos qual é o processo, desde a ideia de utilizar um banco de dados para persistir seus dados, como determinar os requisitos e o contexto. Tudo isso será modelado até efetivamente implementarmos um banco de dados. Já compreendemos o passo a passo, o caminho das pedras até conseguirmos efetivar o que estamos querendo fazer.

### Design de Banco de Dados

O que vamos abordar agora é a parte de design de banco de dados, especificamente o **projeto conceitual**.

> [!definicao] Projeto Conceitual
> Aquele modelo de alto nível que foi mencionado anteriormente.

Nesse sentido, o que é um projeto conceitual? Como vamos criar um modelo?

Existem duas maneiras de representar ou apresentar algo, pelo menos as duas mais palpáveis e comuns: podemos utilizar a linguagem textual ou a linguagem gráfica. Conseguimos modelar toda a informação a partir de, por exemplo, uma narrativa, ou a partir de imagens, figuras, enfim.

A linguagem textual pode ser comparada à parte de algoritmos, onde temos três métodos distintos de modelar e criar algoritmos. Se quiser saber mais sobre isso, tenho um curso de introdução a pensamento computacional e programação, criado com a Gil, onde falo de algoritmos. Podemos fazer esse adendo porque a linguagem de modelagem de dados voltada para algoritmo é textual, com três formas de seguir esse caminho.

### Representação de Modelos

Quando pensamos em absorção de informação, conseguimos inferir melhor com algo que é visual. No entanto, em um primeiro momento, precisamos da escrita, do modelo textual para definir os requisitos. Geralmente, ao modelar e criar seu projeto conceitual, você vai até o cliente e escreve o que precisa ter, ou escreve no computador, ou ele chega com uma lista de requisitos que precisam ser contemplados no banco de dados.

Nesse sentido, vocês vão refinar aquilo e fazer eventuais anotações sobre o contexto. Mas, em um primeiro momento, você tem um modelo textual, uma linguagem de modelagem de dados textual para dar os primeiros passos, o suporte ao seu modelo gráfico.

Na segunda etapa, temos a parte gráfica para nos auxiliar na visualização do que vai acontecer, da ideia do projeto final. Não é exatamente o projeto final, mas o que temos de ideia do que o projeto final precisa ter, o que nosso projeto físico lá na frente vai precisar ter. Vamos utilizar o modelo chamado Entidade-Relacionamento, que exploraremos em um momento posterior.

### O Propósito da Modelagem

Essa linguagem de modelagem de dados visa justamente a representação; o objetivo dela é representar os dados.

> [!definicao] Modelar
> Representar; criar uma referência.

Sempre que vamos **modelar**, queremos representar um fenômeno, seja ele com uma modelagem computacional ou uma modelagem matemática. Queremos, através da modelagem, representar. Eu diria que são praticamente sinônimos: modelar é representar, é criar uma referência. E a partir dessa referência, podemos analisar aquilo, o nosso contexto, aquele mundo que estamos modelando.

Muito bem. Qual é o primeiro passo?

`⏱ 04:20`

O primeiro passo é dentro de um projeto conceitual. Nele, definimos a **coleta de dados** e a **análise**.

A coleta de dados é intuitiva e já conversamos bastante sobre ela.

> [!definicao] Análise
> Verificar se todas as informações coletadas têm a base necessária para criar o que o cliente deseja.

> [!exemplo] Pedido vs. Venda
> No ambiente de vendas, pode-se ter cliente, pedido e venda. A análise serve para determinar se "pedido" e "venda" são objetos distintos no modelo ou se um pedido simplesmente possui um status (como "venda realizada" ou "cancelada"). Esse é o tipo de situação que deve ser verificada no projeto.

É na fase de análise que se define a importância de cada atributo, o tipo de relacionamento que ocorre entre os objetos e com quem um objeto precisa se relacionar para fornecer uma determinada visão do contexto ou ambiente.

### Requisitos, Perguntas e Visões

Nesta etapa, temos:
- Requisitos a serem atendidos.
- Perguntas a serem respondidas.
- Visões a serem representadas.

Isso é importante porque, muitas vezes, grupos diferentes de pessoas, com necessidades distintas, podem consumir as mesmas informações, mas estas podem precisar ser dispostas de maneiras diferentes para cada grupo.

## Relacionado

- [[sgbd-atores-tipos-de-usuarios-e-finalidade]]
- [[modelagem-de-dados-projeto-conceitual-flexibilidade-e-transicao]]
- [[modelagem-de-dados-requisitos-modelos-conceitual-e-logico]]
- [[jornada-da-formacao-sql-database-specialist]]
