---
titulo: "SGBD: Natureza Autodescritiva, Esquema e Catálogo"
tags: [sgbd, banco-de-dados, dados, conceitos, fundamentos, estruturas-de-dados, modelagem-de-dados]
data: 2026-09-17
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 6
conceitos: [Autodescritivo, SGBD, Esquema de Dados, Metadados, Catálogo, Abordagem Tradicional, DBA]
---

# SGBD: Natureza Autodescritiva, Esquema e Catálogo

> [!resumo] Do que se trata
> Esta aula explora a natureza autodescritiva dos SGBDs, explicando como eles mantêm a descrição de sua estrutura e regras através de componentes como esquema, metadados e catálogo. Ela contrasta a abordagem do SGBD com a tradicional, onde a estrutura dos dados é definida na aplicação, e destaca as vantagens do SGBD no gerenciamento de informações. A nota detalha como o SGBD utiliza essas informações internas para realizar consultas e operações de forma eficiente.

## Para lembrar

- **A natureza autodescritiva de um SGBD significa que ele possui uma descrição de si mesmo, incluindo sua estrutura e regras.**
- **O esquema de dados é a estrutura bem definida dos dados, sem a utilização das instâncias e sem a inserção dos dados.**
- **Metadados e esquema são os componentes utilizados para gerar a natureza autodescritiva do SGBD, permitindo consultas e operações.**
- **O catálogo é o componente que permite ao SGBD refletir os relacionamentos e as estruturas internas do banco de dados.**
- **Diferentemente da abordagem tradicional, onde a estrutura é definida na aplicação, o SGBD armazena a descrição da estrutura e regras de forma independente.**

## O que esta nota responde

- O que significa a natureza autodescritiva de um SGBD?
- Qual a diferença entre a abordagem de SGBD e a abordagem tradicional de gerenciamento de dados?
- Qual o papel do esquema, metadados e catálogo na autodescrição de um SGBD?

## Conceitos

**Autodescritivo** · **SGBD** · **Esquema de Dados** · **Metadados** · **Catálogo** · **Abordagem Tradicional** · **DBA**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Natureza autodescritiva, esquema, metadados e vantagens | ▪▪ |
| `04:00` | Catálogo, consulta e problemas tradicionais | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Autodescritivo** | Possuir uma descrição de si mesmo. |
| **Schema de Dados** | A estrutura bem definida dos dados, sem a utilização das instâncias e sem a inserção dos dados. |
| **Catálogo** | É o componente que permite ao SGBD refletir como estão os relacionamentos e as estruturas internas do banco de dados. |

## Pegadinhas

- Na abordagem tradicional, a estrutura dos dados é definida dentro do arquivo de programação da aplicação, enquanto no SGBD ela é definida por esquema e metadados, gerenciados pelo DBA.

## Teste-se

<details><summary>O que significa a natureza autodescritiva de um SGBD?</summary>

Significa que o SGBD possui uma descrição de si mesmo, incluindo sua estrutura e regras que regem os dados.

</details>

<details><summary>Quais são os dois componentes principais que o SGBD utiliza para sua natureza autodescritiva?</summary>

O SGBD utiliza o esquema e os metadados para realizar consultas e entender a estrutura do banco de dados.

</details>

<details><summary>Qual a principal diferença na autodescrição entre um SGBD tradicional e um banco NoSQL?</summary>

Em SGBDs tradicionais, esquema e metadados descrevem a estrutura. Em NoSQL, a autodescrição geralmente está dentro do próprio arquivo ou documento.

</details>

<details><summary>Qual o papel do DBA na estruturação de um banco de dados em um SGBD?</summary>

O DBA é responsável por criar o esquema e definir os metadados, estruturando todo o banco de dados.

</details>

<details><summary>O que é o catálogo em um SGBD e qual sua função?</summary>

O catálogo é o componente que permite ao SGBD refletir os relacionamentos e as estruturas internas do banco de dados, informando detalhes como número de colunas e tipos de dados.

</details>

<details><summary>Como o SGBD utiliza os metadados ao processar uma consulta?</summary>

Ao receber uma consulta, o SGBD consulta os metadados (estrutura/esquema) para identificar como o que está sendo procurado está disposto e, então, recuperar as informações.

</details>

## Conteúdo

`⏱ 00:00`

Muito bem, eu comentei com vocês que a gente já ia falar de isolamento. Mas, primeiramente, a gente vai falar da natureza **autodescritiva** que um SGBD possui. Depois, a gente vai falar de isolamento entre programa e dados.

### Natureza Autodescritiva do SGBD

Vamos pensar um pouquinho sobre essa natureza **autodescritiva**. O que significa ser **autodescritivo**?

> [!definicao] Autodescritivo
> Possuir uma descrição de si mesmo.

O SGBD traz consigo a descrição da sua estrutura e suas regras bem definidas que regem o contexto representado pelos dados. Para isso, ele tem algo que a literatura de banco de dados denomina como **esquema**.

> [!definicao] Schema de Dados
> A estrutura bem definida dos dados, sem a utilização das instâncias e sem a inserção dos dados.

Com isso, também nós temos os **metadados** e o **esquema** que estão sendo utilizados para gerar essa natureza **autodescritiva** do SGBD.

Em contrapartida, os NoSQL não possuem uma estrutura dedicada para esse tipo de situação, para a descrição do banco. Os bancos NoSQL geralmente possuem uma autodescrição já dentro do próprio arquivo. Por exemplo, em bancos de dados orientados a documento, o documento vai possuir dentro dele mesmo como que ele está estruturado. E aí sim, você vai tratar de uma outra forma essa questão.

Aqui, o banco de dados precisa, o SGBD do modelo [inaudível], que é o modelo mais tradicional, ele possui essas duas características, na verdade, esses dois componentes, chamados de **metadados** e **esquema**, para que ele possa estar realizando eventuais consultas e entendendo como que é estruturado o seu banco de dados.

O SGBD pode, na verdade, ele armazena mais de um banco de dados, mais de um contexto representado. Basta que ele tenha o mesmo esquema. Nesse sentido, nós temos o DBA criando o esquema, definindo os metadados. Toda a estruturação do banco de dados é definida pelo DBA. O sistema de banco de dados, por sua vez, ele vai acessar essas informações para que ele possa estar realizando as consultas, para que ele possa estar seguindo, executando essas operações.

### Vantagens e Uso do SGBD

> [!atenção] Uso Generalizado do SGBD
> Dificilmente você vai encontrar uma empresa que não utilize um SGBD, justamente por diversas vantagens que ele possui, como a facilidade de gerenciar as informações.

Como eu comentei, o SGBD pode possuir vários bancos de dados dentro do sistema, basta que cada um tenha o seu esquema relacionado. Se eu tenho, por exemplo, a Amazon pode ter diversos bancos de dados com [inaudível] distintos, a Nubank, a GIO. Todas as empresas utilizam, vamos colocar assim, que dificilmente você vai ver um cenário que a pessoa não utiliza o SGBD. Utilizam o SGBD de uma maneira que facilita o gerenciamento de seus dados.

### SGBD vs. Abordagem Tradicional

Diferentemente de uma abordagem utilizada [inaudível], a abordagem **autodescritiva**, numa abordagem tradicional, ela já é meio que complicada. Por quê? Essa abordagem **autodescritiva** está dentro da aplicação. De maneira que a estrutura, ela está sendo definida dentro do arquivo de programação. E aí nós temos essa questão que, por exemplo, se você tem uma determinada classe representada, você não vai ter isso associado a um SGBD. Na abordagem tradicional, quem vai definir a estrutura dessa classe?

A seguir, uma comparação entre a abordagem do SGBD e a abordagem tradicional para a autodescrição:

| Característica        | SGBD (Modelo [inaudível])                               | Abordagem Tradicional                                  |
| :-------------------- | :------------------------------------------------------ | :----------------------------------------------------- |
| **Autodescrição**     | Possui natureza **autodescritiva**.                     | A abordagem **autodescritiva** é mais complicada.      |
| **Estrutura e Regras** | Traz consigo a descrição da sua estrutura e regras.     | A estrutura é definida dentro do arquivo de programação. |
| **Componentes**       | Utiliza **esquema** e **metadados**.                    | Não associa a estrutura a um SGBD.                     |
| **Definição**         | O DBA cria o **esquema** e define os **metadados**.     | A estrutura da classe é definida na aplicação.         |

`⏱ 04:00`

da sua classe é justamente o programa. Não importa se é Python, se Java, não importa qual é. Se você estiver utilizando esse tipo de abordagem, você vai definir as estruturas do seu conjunto de dados em um determinado arquivo do seu programa.

Isso, no entanto, apresenta problemas. Temos os problemas de processamento e de ter a estrutura atrelada ao programa, à aplicação. Essa natureza autodescritiva, onde temos um espaço específico para poder definir bem a estrutura e, consequentemente, outras informações relacionadas ao banco de dados, acaba se perdendo.

### O Catálogo e a Autodescrição do SGBD

Nesse contexto, o que é chamado de **catálogo** é fundamental. O catálogo está justamente atrelado à questão da autodescrição do SGBD.

> [!definicao] Catálogo
> É o componente que permite ao SGBD refletir como estão os relacionamentos e as estruturas internas do banco de dados.

É através dele que conseguimos ver os relacionamentos. Por exemplo, existe uma tabela específica para os relacionamentos daquele banco de dados. Podemos ter, por exemplo, `Estudante`, `curso`, `sessão`, `report da grade` e os pré-requisitos. O catálogo informa o número de colunas, dando uma noção do tamanho do banco de dados.

Em outra tabela, ele apresenta os atributos, que são as propriedades das entidades. Por exemplo, podemos ter o nome e o `student number`. O catálogo também registra o tipo de dado e a qual entidade, na verdade, ele pertence (`belongs to relation`).

### Consulta e Metadados

O interessante é que, quando o banco de dados precisa retornar informações sobre os dados — por exemplo, ao dar um `SELECT` ou fazer uma consulta, como no cadastro dos alunos —, ele não depende apenas do código da aplicação.

Ele consulta os **metadados**, ou seja, a estrutura do banco, o **esquema**. O sistema identifica como está disposto o que ele está procurando. O software modulado, que está dentro do SGBD, vai então solicitar e recuperar essas informações relacionadas.

## Relacionado

- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[bancos-de-dados-da-evolucao-ao-big-data]]
- [[bancos-de-dados-definicao-acesso-e-escala]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `esquema do banco → schema`
