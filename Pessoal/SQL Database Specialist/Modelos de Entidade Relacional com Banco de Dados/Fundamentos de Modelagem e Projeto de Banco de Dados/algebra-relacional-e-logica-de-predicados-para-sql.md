---
titulo: "Álgebra Relacional e Lógica de Predicados para SQL"
tags: [sql, banco-de-dados, sgbd, fundamentos, conceitos, matematica, operadores]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 5
conceitos: [Lógica de Predicados, Predicado, Álgebra Relacional, Teoria de Conjuntos, Modelo Relacional, Operações da Álgebra Relacional, Funções Agregadas, SQL]
---

# Álgebra Relacional e Lógica de Predicados para SQL

> [!resumo] Do que se trata
> Esta nota explora a lógica de predicados como base para queries SQL complexas, definindo-a como o critério sobre o sujeito da oração. Em seguida, detalha a álgebra relacional como uma linguagem formal para consulta e extração de dados, fundamentada na teoria de conjuntos e no modelo relacional. Por fim, apresenta as operações e funções essenciais da álgebra relacional, como seleção, projeção, união e funções agregadas, que são a base para a manipulação de dados em SGBDs.

## Para lembrar

- **Predicado é a parte da oração que contém o verbo e traz informação sobre o sujeito, sendo a base para queries SQL complexas.**
- **Ao usar `SELECT FROM WHERE determinada condição` em SQL, aplica-se a lógica de predicados para filtrar informações.**
- **Álgebra Relacional é uma linguagem formal para consulta e extração de dados, baseada na teoria de conjuntos e no modelo relacional.**
- **O SQL é baseado na álgebra relacional, que define operações como seleção, projeção, união, interseção, produto cartesiano e lógica (AND, OR, NOT).**
- **Operações comuns em SQL incluem `COUNT`, `SUM`, Média, `MIN` e `MAX`, sendo 80% das queries simples (CRUD) e 20% complexas para insights.**

## O que esta nota responde

- O que é a lógica de predicados e como ela se aplica ao SQL?
- Qual a definição de álgebra relacional e qual sua relação com o SQL?
- Quais são as principais operações e funções da álgebra relacional utilizadas em SGBDs?

## Conceitos

**Lógica de Predicados** · **Predicado** · **Álgebra Relacional** · **Teoria de Conjuntos** · **Modelo Relacional** · **Operações da Álgebra Relacional** · **Funções Agregadas** · **SQL**

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Predicado** | A parte da oração que contém o verbo e que traz a informação sobre o sujeito. |
| **Álgebra Relacional** | Uma linguagem formal para consulta e extração de dados. |

## Teste-se

<details><summary>O que é um predicado?</summary>

É a parte da oração que contém o verbo e traz informação sobre o sujeito. Na lógica de predicados para SQL, é um critério relacionado ao sujeito para queries complexas.

</details>

<details><summary>Em que a álgebra relacional é baseada?</summary>

A álgebra relacional é baseada no modelo relacional, que por sua vez é baseado na teoria de conjuntos.

</details>

<details><summary>Qual a relação entre SQL e álgebra relacional?</summary>

O SQL que usamos é baseado na álgebra relacional. Ela define o conjunto de operações que são a base para extrair informações usando as queries do SQL.

</details>

<details><summary>Quais são os dois tipos de operações que constituem a álgebra relacional?</summary>

A álgebra relacional é constituída por operações da teoria de conjuntos e operações específicas do modelo relacional de bancos de dados.

</details>

<details><summary>Cite três operações da álgebra relacional mencionadas no texto.</summary>

Três operações são Seleção, Projeção e União.

</details>

<details><summary>Quais são alguns dos tipos de comandos SQL mais comumente utilizados para inferir informações?</summary>

Alguns dos comandos mais comumente utilizados são COUNT, SUM, Média, MIN e MAX.

</details>

## Conteúdo

### Lógica de Predicados

Eu queria falar agora com vocês um pouquinho de álgebra relacional, especificamente a **lógica de predicados**.

> [!definicao] Predicado
> A parte da oração que contém o verbo e que traz a informação sobre o sujeito.

O que nós temos aqui é uma informação, um determinado critério relacionado ao nosso sujeito, que vai ser a base para *queries* mais complexas.

> [!exemplo] Lógica de predicados em SQL
> Ao utilizar um comando como `SELECT FROM WHERE determinada condição`, você está usando a lógica de predicados. Você está dizendo: "Eu quero selecionar da minha entidade, de uma determinada entidade, onde tal condição acontece."
>
> Baseado nessa lógica, o sistema retornará a informação, a instância ou as instâncias daquela identidade que contém aquela informação.

A álgebra relacional é baseada no modelo relacional, que por sua vez é baseado na teoria de conjuntos.

### Álgebra Relacional

> [!definicao] Álgebra Relacional
> Uma linguagem formal para consulta e extração de dados.

O `SQL` que usamos é baseado na **álgebra relacional**. Ela define um conjunto de operações, que são constituídas por:
- Operações da teoria de conjuntos.
- Operações específicas do modelo relacional de bancos de dados.

Esse conjunto de funções é a base e as operações que temos disponíveis para extrair *insights* e informações utilizando as *queries* do `SQL`. Veremos mais para frente como tirar essas informações, desde as *queries* mais básicas até algo mais avançado.

Isso ficará para a próxima parte, onde pegaremos o modelo que estaremos criando nesta etapa. Criaremos o modelo Entidade-Relacionamento, depois o mapearemos para o modelo relacional e, então, usaremos as operações baseadas na teoria de conjuntos e na álgebra relacional para retirar informações e *insights* do banco de dados.

### Operações e Funções

Podemos ter as seguintes operações:
- Seleção (`selection`)
- Projeção (`projection`)
- União
- Interseção
- Produto cartesiano
- Lógica (`AND`, `OR`, `NOT`)

Essas são algumas das operações que temos à disposição para inferir informações no nosso SGBD.

Aqui estão alguns dos tipos de operações que temos ao utilizar o `SQL`:
- `COUNT`
- `SUM`
- Média
- `MIN`
- `MAX`

Esses são os tipos de comandos mais comumente utilizados. Há uma regra chamada 20/80 que diz o seguinte: 80% do tempo você estará utilizando *queries* simples, um `CRUD` mesmo, e os 20% restantes você estará retirando *insights* através de *queries* mais complexas.

Eu trouxe uma mistura delas, de algumas básicas que são mais utilizadas nesse sentido.

## Relacionado

- [[modelo-relacional-usuarios-e-integracao-de-sgbds]]
- [[pre-requisitos-para-a-formacao-sql-database-specialist]]
- [[modelagem-de-dados-implementacao-de-entidades-e-relacionamentos-com-sql]]
- [[sgbds-historico-e-modelos-de-dados]]
