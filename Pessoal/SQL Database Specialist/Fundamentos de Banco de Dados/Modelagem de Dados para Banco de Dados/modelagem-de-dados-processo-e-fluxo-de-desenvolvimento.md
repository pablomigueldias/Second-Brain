---
titulo: "Modelagem de Dados: Processo e Fluxo de Desenvolvimento"
tags: [modelagem-de-dados, banco-de-dados, fundamentos, sgbd, sql, engenharia-de-software, conceitos]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 6
conceitos: [Diagrama de Identidade de Relacionamento (Diagrama ER), Cardinalidade, Processo de Modelagem de Banco de Dados, Projeto Conceitual, Projeto Lógico, Projeto Físico, Esquema Conceitual, Esquema Lógico]
---

# Modelagem de Dados: Processo e Fluxo de Desenvolvimento

> [!resumo] Do que se trata
> A aula explora um cenário de modelagem de dados, utilizando um diagrama de entidade e relacionamento para ilustrar as conexões entre entidades como empregados, departamentos e projetos. Ela detalha o processo de desenvolvimento de banco de dados, que segue etapas sequenciais: conceitual, lógica, física e validação. Por fim, descreve o fluxo de modelagem, desde os requisitos iniciais até a criação do esquema físico com comandos SQL.

## Para lembrar

- **O Projeto Conceitual de um banco de dados define os requisitos de alto nível e o que o banco de dados deve conter.**
- **O Projeto Lógico estrutura as informações utilizando o modelo relacional, que consiste em entidades e relacionamentos (tabelas e suas conexões).**
- **O Projeto Físico é a implementação efetiva do modelo de banco de dados, culminando na criação de tabelas e índices.**
- **O fluxo de modelagem de dados inicia com requisitos que fomentam o projeto conceitual, resultando em um esquema conceitual (diagrama ER).**
- **O esquema conceitual é mapeado para um esquema lógico (modelo relacional), que por sua vez gera o esquema físico com comandos SQL.**

## O que esta nota responde

- Quais são as etapas do processo de desenvolvimento de um banco de dados?
- Como um diagrama de entidade e relacionamento (ER) é utilizado no cenário de modelagem?
- Qual é o fluxo completo da modelagem de dados, desde os requisitos até a implementação física?

## Conceitos

**Diagrama de Identidade de Relacionamento (Diagrama ER)** · **Cardinalidade** · **Processo de Modelagem de Banco de Dados** · **Projeto Conceitual** · **Projeto Lógico** · **Projeto Físico** · **Esquema Conceitual** · **Esquema Lógico**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Cenário e etapas de modelagem | ▪▪ |
| `04:20` | Fluxo de modelagem de dados | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Processo de Modelagem de Banco de Dados** | O desenvolvimento passa por etapas sequenciais, partindo de um projeto conceitual de alto nível, passando pela estruturação lógica e culminando na implementação física. |
| **Projeto Conceitual** | É o ponto de partida, onde se define o que o banco de dados deve conter, abrangendo todos os requisitos já levantados. |
| **Projeto Lógico** | Nesta fase, é preciso estruturar toda a informação recebida. Utiliza-se o modelo relacional, que consiste na estrutura de entidades, relacionamentos (ou seja, tabelas e suas conexões). |
| **Modelo Relacional** | estrutura de entidades, relacionamentos (ou seja, tabelas e suas conexões). |
| **Projeto Físico** | É a implementação efetiva de tudo aquilo que foi modelado anteriormente. |
| **Validação** | A etapa final, onde o sistema é validado. |
| **Esquema Conceitual** | o diagrama de entidade e relacionamento. |
| **Esquema Físico** | consiste nas sequências de comandos em SQL necessárias para criar efetivamente o banco de dados. |

## Teste-se

<details><summary>Qual o ponto de partida do processo de desenvolvimento de banco de dados?</summary>

O ponto de partida é o Projeto Conceitual, onde se definem os requisitos de alto nível e o que o banco de dados deve conter.

</details>

<details><summary>Qual modelo é utilizado na fase de Projeto Lógico?</summary>

Na fase de Projeto Lógico, utiliza-se o modelo relacional, que estrutura as informações em entidades e relacionamentos, ou seja, tabelas e suas conexões.

</details>

<details><summary>O que é o Projeto Físico no processo de modelagem de dados?</summary>

O Projeto Físico é a etapa de implementação efetiva de tudo que foi modelado, criando a estrutura do banco de dados com tabelas e índices.

</details>

<details><summary>Qual é o objetivo do esquema conceitual no fluxo de modelagem de dados?</summary>

O esquema conceitual, que é o diagrama de entidade e relacionamento, fomenta o projeto conceitual e subsidia o esquema lógico.

</details>

<details><summary>O que o esquema físico consiste em?</summary>

O esquema físico consiste nas sequências de comandos em SQL necessárias para criar efetivamente o banco de dados.

</details>

<details><summary>Cite uma das relações importantes que podem ser representadas em um cenário de modelagem de dados envolvendo empregados.</summary>

Uma relação importante é que um empregado pode ter um dependente, como um filho, que é persistido no banco de dados.

</details>

## Conteúdo

`⏱ 00:00`

Continuando, eu quis trazer logo de cara um diagrama de identidade de relacionamento. Vou falar de uma maneira bem geral, bem superficial, sobre o que estou querendo dizer aqui. Não vou entrar em detalhes de porquê de linhas, porquê de ter uma linha dupla, ou porquê de um determinado nome estar sublinhado. Vou falar o que está escrito aqui, representado aqui, de maneira de alto nível.

#### Cenário de Modelagem

Tenho um cenário de uma companhia onde existem empregados, e esses empregados trabalham para diferentes departamentos. Há também os projetos, que são o foco da empresa.

O que consigo tirar com esse modelo? Não modelei, estou apenas tendo acesso a ele. Vamos pensar que sou um cliente olhando esse modelo.

*   O empregado vai trabalhar em um projeto.
*   É possível notar a noção de cardinalidade:
    *   Um empregado pode trabalhar em mais de um projeto.
    *   Um projeto pode ter mais de um empregado.
    *   Geralmente, as equipes são grandes.
    *   O empregado está relacionado a um determinado departamento.

Além disso, há outras relações importantes:

*   Um empregado trabalha para um departamento.
*   Há um gerente: consigo representar que um determinado empregado vai gerenciar o departamento.
*   O empregado pode ter um dependente. Se um empregado tem um filho, por exemplo, o filho dele estará persistido no banco de dados como dependente. O nome é bem intuitivo: essa entidade depende do empregado.
*   Um empregado supervisiona outros empregados.

#### O Processo de Desenvolvimento do Banco de Dados

Continuando, criamos o nosso esquema, definindo nosso diagrama. Temos os conceitos de modelos relacionados, e as análises das queries. Os dados requisitos, que são relacionados à parte de coleta e análise, vão fomentar as análises das queries posteriormente.

O meu esquema será a base da estrutura do banco de dados, e essas informações são base para queries.

Para definir o que temos a cada etapa dentro de um desenvolvimento de banco de dados, o processo segue uma sequência lógica:

> [!definicao] Processo de Modelagem de Banco de Dados
> O desenvolvimento passa por etapas sequenciais, partindo de um projeto conceitual de alto nível, passando pela estruturação lógica e culminando na implementação física.

**As etapas são:**

1.  **Projeto Conceitual:** É o ponto de partida, onde se define o que o banco de dados deve conter, abrangendo todos os requisitos já levantados.
2.  **Projeto Lógico:** Nesta fase, é preciso estruturar toda a informação recebida. Utiliza-se o **modelo relacional**, que consiste na estrutura de entidades, relacionamentos (ou seja, tabelas e suas conexões).
3.  **Projeto Físico:** É a implementação efetiva de tudo aquilo que foi modelado anteriormente.
4.  **Validação:** A etapa final, onde o sistema é validado.

| Etapa | Objetivo | Estrutura Utilizada |
| :--- | :--- | :--- |
| **Conceitual** | Definir o que o banco de dados deve conter (requisitos de alto nível). | Requisitos de Negócio |
| **Lógico** | Estruturar a informação recebida. | Modelo Relacional (Entidades e Relacionamentos) |
| **Físico** | Implementação efetiva do modelo. | Estrutura de Banco de Dados (Tabelas, Índices, etc.) |

`⏱ 04:20`

validação, ação, teste e manutenção.

### Definição dos Projetos de Banco de Dados

Para definir os projetos de banco de dados, temos:

| Projeto      | Objetivo                                     |
| :----------- | :------------------------------------------- |
| Conceitual   | Define o que será contido no banco de dados. |
| Lógico       | Define a estrutura do banco de dados.        |
| Físico       | Implementa o banco de dados.                 |

### Fluxo de Modelagem de Dados

Os requisitos iniciais fomentam o **projeto conceitual**. Este projeto entrega um **esquema conceitual**, que é o diagrama de entidade e relacionamento.

O esquema conceitual, por sua vez, subsidia o **esquema lógico**. Há um mapeamento de todas as informações representadas no esquema conceitual para o esquema lógico, que, neste caso, utiliza o modelo relacional.

A partir do **esquema lógico**, cria-se o **esquema físico**. Este consiste nas sequências de comandos em `SQL` necessárias para criar efetivamente o banco de dados.

## Relacionado

- [[modelagem-de-dados-introducao-e-modelo-entidade-relacionamento-mer]]
- [[modelagem-de-dados-implementacao-de-entidades-e-relacionamentos-com-sql]]
- [[sgbds-historico-e-modelos-de-dados]]
- [[Casos de Uso]]
