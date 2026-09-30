---
titulo: "Modelagem de Dados: Implementação de Entidades e Relacionamentos com SQL"
tags: [modelagem-de-dados, sql, banco-de-dados, sgbd, engenharia-de-software, fundamentos, conceitos]
data: 2026-09-27
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 8
conceitos: [UML, Modelo Entidade-Relacionamento (ER), SQL, Primary Key, Foreign Key, Cardinalidade e Multiplicidade, Linguagem Declarativa, STBD]
---

# Modelagem de Dados: Implementação de Entidades e Relacionamentos com SQL

> [!resumo] Do que se trata
> A aula aborda a implementação de modelos de dados, contrastando brevemente a abordagem orientada a objetos da UML com o Modelo Entidade-Relacionamento (ER). Ela detalha o uso da linguagem SQL para inserir e acessar informações em um Sistema de Gerenciamento de Banco de Dados (STBD), apresentando comandos essenciais de manipulação de dados. Por fim, são fornecidos exemplos práticos de criação de tabelas, definição de chaves primárias e estabelecimento de relacionamentos com chaves estrangeiras em SQL.

## Para lembrar

- **SQL é uma linguagem declarativa voltada para a consulta e manipulação de dados em um STBD, baseada na teoria de conjuntos.**
- **Comandos SQL como CREATE, ALTER, DROP, SELECT, INSERT e UPDATE são essenciais para manipular informações dentro de um banco de dados.**
- **Uma Primary Key é um identificador único que garante a não repetição de informação em uma tabela, definida no SQL como `id integer primary key`.**
- **A Foreign Key é utilizada para definir relacionamentos entre entidades, referenciando a primary key de outra tabela, e deve ser definida na tabela antes de ser referenciada.**
- **Na UML, é possível definir o nome da classe, atributos e métodos/operações, enquanto no Modelo Entidade-Relacionamento (ER) o foco é na identificação e definição de identificadores.**

## O que esta nota responde

- Como a UML se diferencia do Modelo Entidade-Relacionamento na representação de dados?
- Quais comandos SQL são utilizados para manipular informações em um Sistema de Gerenciamento de Banco de Dados (STBD)?
- Qual a função de uma Primary Key e de uma Foreign Key na criação de tabelas SQL?

## Conceitos

**UML** · **Modelo Entidade-Relacionamento (ER)** · **SQL** · **Primary Key** · **Foreign Key** · **Cardinalidade e Multiplicidade** · **Linguagem Declarativa** · **STBD**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | UML, SQL e criação de tabelas | ▪▪ |
| `04:20` | Chaves primária e estrangeira SQL | ▪▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **SQL** | Linguagem declarativa voltada para a consulta de dados dentro do STBD, baseada na teoria de conjuntos. |
| **Primary Key** | Um identificador único que garante que não haja repetição de informação em uma tabela, mesmo que não esteja explicitamente no modelo ER. É definida no SQL como `id integer primary key`. |

## Pegadinhas

- Não use o mesmo nome de variável (`id`) para a `primary key` e para a `foreign key` que referencia outra tabela, pois isso causará um erro.

## Teste-se

<details><summary>Qual o foco principal da aula em relação à modelagem de dados?</summary>

O foco principal da aula é a entidade de relacionamento (ER). A UML é abordada apenas superficialmente.

</details>

<details><summary>O que é SQL e qual sua base teórica?</summary>

SQL é uma linguagem declarativa voltada para a consulta de dados dentro do STBD. Ela é baseada na teoria de conjuntos.

</details>

<details><summary>Cite três comandos de manipulação de dados em SQL.</summary>

Três comandos de manipulação de dados em SQL são `CREATE`, `ALTER` e `DROP`.

</details>

<details><summary>Qual a função de uma `primary key` em uma tabela?</summary>

Uma `primary key` é um identificador único que garante que não haja repetição de informação em uma tabela. Ela é definida no SQL para esse fim.

</details>

<details><summary>Qual erro comum deve ser evitado ao definir uma `foreign key`?</summary>

Deve-se evitar usar o mesmo nome de variável para a `primary key` de uma tabela e para a `foreign key` que referencia outra tabela. Isso causará um erro.

</details>

<details><summary>Como a cardinalidade 'zero ou muitos' pode ser interpretada em um contexto de artigos e periódicos?</summary>

Significa que um artigo pode não ter sido aceito ou publicado por ninguém ainda. A modelagem exata depende da subjetividade do contexto.

</details>

## Conteúdo

`⏱ 00:00`

A UML tem um outro viés. Como ela foi desenvolvida fora da área de STBDs, ela traz consigo o paradigma de orientação a objeto.

Nessa modelagem, "periódicos" tem uma cara de objeto, da ideia de Programação Orientada a Objetos (POO), porque isso, na verdade, é um diagrama de classe. Então, "periódicos" é uma classe.

Se você for pensar nas entidades, elas representam um objeto que representa uma classe, que forma a generalista. Periódicos possuem uma `primary key`. Essa ideia de `primary key` está na UML, mas ela não existe na entidade de relacionamento (ER). Você só consegue identificar e definir os identificadores dentro do ER.

Na UML, conseguimos definir o nome da classe, os atributos e se existe algum método ou operação associada àquele objeto. A cardinalidade e a multiplicidade, e como eles se relacionam, são criadas de uma forma diferente.

Vou deixar a parte de destrinchar esses modelos. Na verdade, a UML será só uma pincelada, porque o foco nesta informação é a entidade de relacionamento.

> [!exemplo] Cardinalidade e Multiplicidade
> Para acabar com a curiosidade, o que a notação "de zero para muitos" e "de zero a um" quer dizer?
>
> Eu sei que zero ou muitos artigos são publicados em um periódico.
>
> Enquanto zero ou um periódico publicam um artigo.
>
> Esse zero significa que eu tenho um artigo que não foi aceito ou publicado por ninguém ainda. Essa é uma maneira de representar. Dependendo do seu contexto, pode ser obrigatório ter pelo menos um. A modelagem fica a cargo da subjetividade do seu contexto.

### Inserindo Informações no STBD com SQL

Como conseguimos inserir informações dentro do nosso STBD, já baseado no nosso modelo de entidade de relacionamento que definimos?

Nós vamos utilizar a linguagem **SQL**.

> [!definicao] SQL
> Linguagem declarativa voltada para a consulta de dados dentro do STBD, baseada na teoria de conjuntos.
>
> Quando você usa `SELECT FROM`, você está se baseando na teoria de conjuntos para puxar a informação de determinado conjunto, independentemente da quantidade de elementos, características ou atributos que ele possui.

Nós temos comandos de manipulação utilizando SQL, como:
- `CREATE`
- `ALTER`
- `DROP`
- `SELECT`
- `INSERT`
- `UPDATE`
- entre outros, para manipular com sucesso as informações dentro do banco de dados.

### Acessando Informações

Como acessamos essas informações?
Podemos acessar via `phpmyadmin` ou `pgadmin`. Também conseguimos acessar via terminal.

Eu gosto muito de acessar via terminal, entrando na linha de comando e puxando essas informações por ali. Mas você tem essas duas opções: acessar por uma interface gráfica ou via terminal.

Outra maneira é acessar através de programação, utilizando bibliotecas e APIs para criar conexão com o banco de dados e extrair as informações.

### Exemplo: Criando Tabela Periódicos com SQL

Este é o nosso primeiro exemplo, utilizando o modelo ER para "periódico".

> [!exemplo] Criação de Tabela "Periódicos"
> O exemplo é justamente de periódico utilizando o modelo ER.
>
> Vou criar uma tabela com o nome `periódico` e o `ESSN`.
>
> Primeiro, crio o banco de dados:
> ```sql
> CREATE DATABASE first_example;
> ```
>
> Depois, crio a tabela `periódicos` e defino suas colunas:
> ```sql
> CREATE TABLE periódicos (
>     id INTEGER,
>     nome VARCHAR(120),
>     essn INTEGER
> );
> ```
> O `id` será do tipo `INTEGER` (ou `INT`), o `nome` será `VARCHAR` de 120 caracteres, e o `essn` também será `INTEGER` (número).

`⏱ 04:20`

e o `ssn integer`. Como garantir que não haja uma repetição de informação na tabela de periódicos? Isso pode ser garantido através do `ID`. Ele será a **primary key**.

Este é um passo adicional. Embora eu vá definir o projeto de banco de dados mais detalhadamente em outro momento, a ideia é que, após modelar o contexto com o `ER`, você precise persistir isso no banco de dados.

Eu vou definir o `ID` como uma `primary key`. Mesmo que não haja `ID` no modelo, ele é usado para esse fim.

> [!definicao] Primary Key
> Um identificador único que garante que não haja repetição de informação em uma tabela, mesmo que não esteja explicitamente no modelo `ER`. É definida no `SQL` como `id integer primary key`.

Podemos adicionar essa informação ou, ao criar a tabela, especificar `id integer primary key`. Essa é a forma de apresentar, utilizando `SQL`, qual é a chave identificadora da tabela.

### Entidade Editora e Chave Estrangeira

O próximo passo é criar a entidade `editora`, que é uma entidade relacionada a `periódicos`. Ela terá um `ID`, o nome do editor, o país e o `editor ID`.

Como definir esse relacionamento? Utilizando uma **foreign key**. A `foreign key ID` fará referência ao `editor ID`.

> [!exemplo] Definindo a Foreign Key
> Ao definir a `foreign key`, é comum cometer um erro.
> >
> **O Problema:**
> Você definiu `id integer` como `primary key` para a tabela de periódicos. Agora, precisa de outra identificação para a editora. Se você tentar usar `foreign key id` referenciando `id editora`, isso causará um erro.
> >
> [!atenção]
> Não use o mesmo nome de variável (`id`) para a `primary key` e para a `foreign key` que referencia outra tabela. Isso causará um erro.
> >
> **A Solução:**
> Primeiro, defina a variável que será usada como `foreign key` explicitamente. Ela precisa estar definida na tabela antes de ser referenciada.
> >
> É como em linguagens procedurais, como C, onde você precisa definir estaticamente o tipo de dado.
> >
> **Exemplo de Código Correto:**
> ```sql
> id_editora integer,
> foreign key (id_editora) references editora (id)
> ```
> >
> Essa é a lógica e o raciocínio correto.

### Desafio de Modelagem

Como um exercício para treinar o raciocínio, eu defini as entidades `editoras` e `periódicos`. Não haverá nenhuma outra informação além dessas.

A partir disso, vocês devem criar as seguintes entidades:
-   `artigo`
-   `pesquisador` ou `autor`

Se vocês quiserem agregar conhecimento, criem essas entidades e relacionem-nas. Por exemplo:
Um periódico é uma revista. O que ela faz? Ela está associada a um artigo. De que forma?
Vocês devem começar a pensar e criar esse modelo para fundamentar o conhecimento.

## Relacionado

- [[modelagem-de-dados-introducao-e-modelo-entidade-relacionamento-mer]]
- [[../../../Engenharia de Software/UML/Introdução UML]]
- [[../../../Machine Learning/Linguagens de Programação para ML/paradigmas-e-linguagens-de-programacao-para-machine-learning]]
- [[../../../Engenharia de Software/UML/Diagrama de Componentes vs. Modelagem de Dados]]
