link conteúdo: [Conceito Banco de dados](https://www.youtube.com/watch?v=Q_KTYFgvu1s&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD)

## Dados x Informação

`Dados`: São fatos em uma forma primária, que podem ser armazenados em algum meio.
- Ex.: CPF, Nome, Data

`Informação`: São os fatos organizados de maneira a produzir um significado -> Dados colocados em contexto.
- Ex.: Lista de clientes com números de CPF, ordenados.

---
## Metadados

- Definimos Metadados como sendo "Dados sobre os dados".
- Permitem efetuar a representação e identificação dos dados, garantindo sua consistência e persistência.
- Os Metadados são mantidos no Dicionário de Dados (ou em um Catálogo de Dados).

---
## Banco de Dados

Um Banco de Dados (BD) é uma coleção organizada de dados. Esses dados são organizados de modo a modelar aspectos do mundo real, para que seja possível efetuar processamento que gere informações relevantes para os usuários a partir desses dados.

Um BD é composto por diversos objetos, tais como: tabelas, esquemas visões, consultas, relatórios, procedimentos, triggers, entre outros.

---
## Aplicações dos Bancos de Dados

Bancos de dados encontram aplicações em inúmeras áreas, como:

- Sistema bancários
- Reservas em hotéis
- Controle de estoque em supermercados
- Catálogo de livros em bibliotecas
- E-commerce
- Receita Federal
- Youtube

---
## SGBD

Sistema de Gerenciamento de Banco de Dados

- Um SGBD é uma coleção de software que permite aos usuários criarem e manterem um ou mais banco de dados.
- São usados nas tarefas de definição, construção, manipulação e compartilhamento dos bancos de dados entre aplicações e usuários.
- Permitem proteger o banco de dados e mantê-lo ao longo do tempo.

---
## Exemplos de SGBDs

- Oracle Database
- Microsoft SQL Server
- MySQL
- IBM DB2
- SAP Sybase
- MongoDB
- Teradata
- PostgreSQL
- SQLite

---
## Sistema de Banco de Dados

A figura a seguir ilustra a relação entre usuário, banco de dados, SGBDs e as aplicações que acessam os dados:

![](../IMG/Pasted%20image%2020260107145259.png)

---
## Usuários de Banco de Dados

- Administrador (DBA)
- Projetista / Desenvolvedor
- Usuário Final

---
## Características e Funcionalidades

- Controle de Redundância
- Múltiplas Visões dos Dados
- Controle de Concorrência
- Backup e Restauração
- Autenticação e Autorização de acesso
- Restrições de Integridade

---
## Modelos de Banco de Dados

### Antigo

`Modelo Hierárquico`:
- Neste modelo os dados são organizados de forma hierárquica, com conjuntos de tipos de registros interconectados por meio de ligações.
- Uma ligação representa uma relação entre dois tipos de registros: pai e filho.
- Um esquema no modelo hierárquico é um diagrama de estrutura em árvore.
- O acesso aos dados é sempre unidirecional a partir do pai ao filho

![](../IMG/Pasted%20image%2020260107150444.png)

`Modelo em Rede`:
- No modelo em Redes os dados são organizados em tipos e ligações entre dois registros.
- Não há restrições hierárquica.
- Tanto o esquema quanto ocorrência de dados são visualizados como um grafo direcionado.

![](../IMG/Pasted%20image%2020260107150706.png)
### Atual

`Modelo Relacional`:
- Neste modelo os dados são separados em entidades, conforme cada assunto, e registrados como atributos dessas entidades.
- As entidades se relacionam entre si e permitem que os dados sejam armazenados e recuperados de forma rápida e segura.

![](../IMG/Pasted%20image%2020260107150933.png)