---
titulo: "Modelo Relacional, Usuários e Integração de SGBDs"
tags: [banco-de-dados, sql, sgbd, modelagem-de-dados, linguagens-de-programacao, dados, conceitos]
data: 2026-09-16
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 7
conceitos: [Modelo Relacional, SQL, DBA, DDL (Linguagem de Definição de Dados), LDM (Linguagem de Manipulação de Dados), Transação, Gerenciamento de Armazenamento e Buffer, Integração de SGBDs]
---

# Modelo Relacional, Usuários e Integração de SGBDs

> [!resumo] Do que se trata
> Esta aula explora o modelo relacional, sua base na teoria de conjuntos e a relação com o SQL, detalhando os tipos de usuários em um SGBD, como o DBA e o usuário convencional. Ela descreve o processamento de comandos DDL e LDM, a importância das transações e do gerenciamento de armazenamento e buffer. Por fim, aborda a necessidade e os métodos de integração de múltiplos SGBDs em ambientes complexos.

## Para lembrar

- **O modelo relacional, introduzido por Edgar F. Codd, é baseado na teoria de conjuntos e na álgebra relacional, permitindo abstrair a estrutura de cada entidade.**
- **Dentro de um ambiente de SGBD, o DBA define a estrutura e as *constraints* usando DDL, enquanto o usuário convencional manipula dados com LDM.**
- **Uma transação agrupa uma quantidade significativa de operações para execução, sendo processada pelo SGBD para garantir a durabilidade das modificações.**
- **O gerenciamento de armazenamento refere-se à movimentação de dados do HD para a memória principal (RAM), e o gerenciamento de buffer envolve a troca contínua dessas informações na memória.**
- **A integração de múltiplos SGBDs, que podem ser distribuídos, relacionais ou NoSQL, pode ser feita através de repositórios centralizados como data warehouses ou mediadores.**

## O que esta nota responde

- Qual a base teórica do modelo relacional e do SQL?
- Quais são os tipos de usuários em um SGBD e suas responsabilidades?
- Como a integração de múltiplos SGBDs é realizada em um ambiente corporativo?

## Conceitos

**Modelo Relacional** · **SQL** · **DBA** · **DDL (Linguagem de Definição de Dados)** · **LDM (Linguagem de Manipulação de Dados)** · **Transação** · **Gerenciamento de Armazenamento e Buffer** · **Integração de SGBDs**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Modelo Relacional, SQL e Álgebra | ▪▪ |
| `04:40` | Gerenciamento, Múltiplos SGBDs | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Transação** | Uma transação agrupa uma quantidade significativa de operações para execução. Essa quantidade agrupada é processada pelo SGBD. |
| **Gerenciamento de Armazenamento e Buffer** | O gerenciamento de armazenamento refere-se à movimentação de dados do HD para a memória principal (RAM). O gerenciamento de buffer envolve a troca contínua dessas informações na memória. |

## Teste-se

<details><summary>Quem introduziu a questão do SQL no modelo relacional?</summary>

Edgar F. Codd introduziu a questão do SQL. O SQL é baseado na teoria de conjuntos.

</details>

<details><summary>Quais são os dois tipos de usuários em um ambiente SGBD?</summary>

Dentro de um ambiente de SGBD, temos o usuário convencional e o administrador do banco de dados, conhecido como DBA.

</details>

<details><summary>Qual a principal diferença entre a linguagem usada pelo DBA e pelo usuário convencional?</summary>

O DBA utiliza LDD (Linguagem de Definição de Dados) para definir a estrutura e as restrições dos dados. O usuário convencional utiliza uma linguagem de manipulação dos dados para recuperar e atualizar informações.

</details>

<details><summary>Quais são os dois mecanismos que o SGBD gerencia para otimizar a performance, mesmo que o sistema operacional também os trate?</summary>

O SGBD gerencia o armazenamento e o buffer. Ele possui um mecanismo específico para tratar os dados de maneira mais performática.

</details>

<details><summary>Quais são duas formas de integrar múltiplos SGBDs?</summary>

Para realizar a integração de SGBDs, podemos utilizar repositórios centralizados, como os data warehouses, ou mediadores (sistemas intermediários).

</details>

## Conteúdo

`⏱ 00:00`

### O Modelo Relacional e SQL

Vamos entender o que é o **modelo relacional**. Ele foi criado há muito tempo, e Edgar F. Codd introduziu a questão do **SQL**. O SQL é baseado na teoria de conjuntos.

Quando você faz uma consulta, como um `select from where` ou um `join`, você realiza operações baseadas na teoria de conjuntos. Isso permite abstrair, até certo ponto, a estrutura de cada entidade. A estrutura de cada entidade significa que cada entidade possui atributos específicos a ela. A quantidade e o tipo de dado relacionado a cada atributo também variam.

Por exemplo, quando você realiza uma operação de união, consegue fazê-la independentemente de as entidades terem quantidades diferentes de atributos ou tipos de dados distintos. Existe um nível de transparência em relação à estrutura de dados utilizada pelo modelo relacional para armazenar as informações e os dados. Consequentemente, o modelo relacional é baseado na álgebra relacional.

### Tipos de Usuários

Dentro de um ambiente de SGBD, temos dois tipos de usuários: o usuário convencional e o administrador do banco de dados, conhecido como **DBA**.

O DBA define as tabelas, a estrutura e as *constraints* (restrições) para os dados. Ele determina as regras que fornecem as diretivas do contexto, as tabelas, as entidades e seus atributos. Os comandos utilizados pelo DBA são traduzidos como LDD (Linguagem de Definição de Dados) ou `DDL`.

O DBA tem um nível de importância elevado por ser o administrador do banco. Junto com ele, há outros perfis, como o de *design* de banco de dados, que o auxilia na modelagem de alto nível, definindo entidades, estruturas e *constraints* específicas para cada contexto. O DBA também é responsável pela manipulação; qualquer modificação no esquema é feita por ele.

### Processamento de Comandos DDL

Como o banco de dados entende a `LDD`? Nesse processo, é realizada uma tradução. A `LDD` ou `DDL` é um tipo de `SQL`, mas são comandos específicos para a definição dos dados.

Ocorre um processo de tradução onde a `query` precisa ser compilada. Depois disso, ela passa para um mecanismo de execução, que pega as informações compiladas e as leva para um baixo nível (linguagem de máquina) para executá-las. Nesse processo, há um gerenciador que trata a demanda para direcionar corretamente a extração dos dados, acessando os metadados do esquema para conhecer a estrutura e, então, retornar as informações.

### Usuário Convencional e Manipulação de Dados

O usuário convencional utiliza uma linguagem de manipulação dos dados, não uma linguagem de definição. O objetivo principal é recuperar informações. Geralmente, a atualização de informações é feita via formulários.

As características das ações do usuário convencional incluem:
- Alterar e extrair informações.
- Recuperar e atualizar informações.

Essas características são duráveis, ou seja, as modificações realizadas através dessas transações são duráveis.

> [!definicao] Transação
> Uma transação agrupa uma quantidade significativa de operações para execução. Essa quantidade agrupada é processada pelo SGBD.

Além disso, em relação à manipulação dos dados, há uma preocupação com o *Store* e o *Buffer*. É preciso que haja um gerenciamento.

`⏱ 04:40`

É preciso que haja um gerenciamento de armazenamento e também o gerenciador de buffer. Apesar de esse tipo de situação ser tratada pelo sistema operacional, o SGBD, por ter uma importância significativa em termos de performance, precisa tratar os dados de maneira mais performática. Esse é o viés dele: muitas vezes, o SGBD possui um mecanismo específico para isso.

> [!definicao] Gerenciamento de Armazenamento e Buffer
> O **gerenciamento de armazenamento** refere-se à movimentação de dados do HD para a memória principal (RAM).
> O **gerenciamento de buffer** envolve a troca contínua dessas informações na memória.

Não é apenas um SGBD em operação. Muitas vezes, uma empresa tem mais de um SGBD, e cada um com uma função específica.

> [!exemplo] Múltiplos SGBDs em uma empresa
> Uma empresa pode ter mais de um SGBD, cada um com uma função específica. Por exemplo, algumas empresas utilizam SGBDs NoSQL para períodos de alta demanda, enquanto outras usam SGBDs relacionais para 99% dos casos.

### Integração de SGBDs
Quando há múltiplos SGBDs (distribuídos, relacionais, NoSQL), é preciso integrá-los. A **integração de SGBDs** é uma área de pesquisa muito específica.

Para realizar essa integração, podemos utilizar:
- Repositórios centralizados, como os `data warehouses`.
- Mediadores (sistemas intermediários).

> [!exemplo] Exemplo de sistema de integração: Portal de Espécies e Ocorrências
> Um sistema de integração, como o de um portal de espécies e ocorrências ao CBBR, funciona da seguinte forma:
> - Recebe uma série de fontes distintas e heterogêneas de informação.
> - Associa a esse sistema integrado os **metadados**, que definem a estrutura dos dados.
> - Processa as informações para prover um determinado serviço, como o acesso às informações do portal de espécies e ocorrências.

A área de integração é muito específica e é uma área de estudo e pesquisa relacionada ao banco de dados.

## Relacionado

- [[pre-requisitos-para-a-formacao-sql-database-specialist]]
- [[sgbds-historico-e-modelos-de-dados]]
- [[bancos-de-dados-da-evolucao-ao-big-data]]
