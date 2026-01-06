
Link do conteúdo : [SGBD](https://www.youtube.com/watch?v=2oFepn1KXQM)

### Sistema Gerenciador de Banco de Dados

- Programas utilizados para gerencias a estrutura e as informações dos Bancos de Dados.
- As funções de um SGBD incluem: transformar e apresentar dados, controlar o acesso de multiusuário e prover interfaces de comunicação do banco de dados.
- Os programas usados em um SGBD permitem criação de estruturas, manutenção de dados gerenciamento de transações e extração de informações.

`SGBD`: Gerencia uma coleção de dados inter-relacionados e uma coleção de programas para acesso a esse banco de dados.

![[Pasted image 20251231135524.png]]

`Visão`: é o conceito que permite que os diferentes usuários compartilhe dados e recursos de processamento.

## `SGBDR` 

### Banco de Dados Relacional

Uma maneira intuitiva e direta de representar dados em tabelas. Cada linha na tabela é um registro. As colunas da tabela contêm atributos dos dados e cada registro geralmente tem um valor para cada atributo.

![[Pasted image 20251231140411.png]]

## SQL (Structured Query Language)
Linguagem de Consulta Estruturada

Conjunto de comando de manipulação de banco de dados. Através da Linguagem SQL podemos criar, incluir, excluir, modificar e pesquisar informações nas tabelas de banco de dados relacional. 


|        SGBDR         |
| :------------------: |
| Microsoft SQL Server |
|        MySQL         |
|     PostgreeSQL      |
|   Oracle DATABASE    |
|       Firebird       |
|   Microsoft ACCESS   |
|   LibreOffice BASE   |
|        dBase         |

## Propriedades Básicas da Transação

`ACID`
- Atomicidade
- Consistência
- Isolamento
- Durabilidade

`Atomicidade`: Transação deve ter todas suas operações executadas em caso de sucesso. Apresentando falhas nenhum resultado das operações deve refletir sobre o banco de dados.

`Concistência`: Respeitar as regras de integridade dos dados. A execução de uma transação leva o banco de dados  de um estado consistente para outro estado consistente.

`Isolamento`: Evitar que transações paralelas interfiram umas nas outras.

`Durabilidade`: Persistência dos efeitos de uma transação no banco de dados em caso de sucesso, mesmo com quedas de energia, erros ou travamentos.

## `SGBD NoSQL`

Movimento que propõe novas estruturas de banco de dados "não relacionais"

| SGBD NoSQL     |
| -------------- |
| MongoDB        |
| Redis          |
| Cassandra      |
| Neo4j          |
| AmazonDynamoDB |
| Apache HBase   |

Classificação dos modelos existentes em NoSQL de acordo com a estrutura que os dados são armazenados

Atualmente, existem 4 modelos principais:
- orientado a chave-valor
- orientado a documentos
- orientados a colunas
- orientados a grafos

![[Pasted image 20251231141649.png]]

- **orientado a chave-valor**
	- DynamoDB
	- Redis
	- Riak
	- Memcached
	- Berkeley DB
	- LevelDB

- **orientado a documentos**
	- MongoDB
	- Couchbase
	- CouchDB
	- MarkLogic
	- RavenDB

- **orientado a colunas**
	- Cassandra
	- HBase
	- Hypertable

- **orientado a grafos**
	- AllegroGraph
	- ArangoDB
	- InfoGrid
	- Neo4j
	- Titan
	- FlockDB
	- HyperGraphDB

## Teorema CAP

**Consiste em um conjunto de requisitos para sistemas distribuídos:**

- Consistência (Consistency)
- Disponibilidade (Availability)
- Tolerância à partição (Partition tolerance)

![[Pasted image 20251231153039.png]]


`Consistência(Consistency)`: A consistência refere-se ao aspecto que todos os nós do sistema devem conter os mesmo dados, garantindo que diferentes usuários terão a mesma visão do estado dos dados. Ou seja, é preciso garantir que todos os servidores de um cluster terão cópias consistentes dos dados.
A consistência aqui descrita não tem o mesmo significado que a existente no termo ACID, em que consistência se refere ao fato de que operações que violam alguma regra do banco de dados não serão aceitas.

`Diponibilidade(Availability)`: Para o requisito de disponibilidade, os sistema deverá sempre responder a uma requisição, mesmo que não esteja consistente.

`Tolerância à partição(Partition tolerance)`: Por fim, a tolerância à partição deve garantir que o sistema continuará em operação mesmo que algum servidor do cluster venha a falhas.

### Teorema CAP

Ainda segundo Brewer, é teoricamente impossível obter um sistema que atenda os 3 requisitos.
Segundo o Teorema CAP, se você precisar garantir consistência e disponibilidade para uma aplicação, você precisará abrir mão da tolerância à partição, pois ele não oferece garantias em relação à alta consistência dos dados se precisar manter a aplicação sempre disponível. 


