
Link do conteúdo:  [Modelo Relacional - Introdução](https://www.youtube.com/watch?v=hGstS10kCPM&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=2) 

## Modelos

- Um modelo é uma estrutura que ajuda a comunicar os conceitos que estão na mente do projetista. Podemos usá-los para tarefas como descrever, analisar, especificar e comunicar ideias.
- O modelo deve possuir detalhar suficientes para que um desenvolvedor consiga construir o banco de dados de acordo com a necessidade do projeto.

---
## Modelagem de Dados

- Modelagem de Dados é o processo de criação de um Modelo de dados para um sistema de informação, com a aplicação de técnicas específicas de modelagem.
- Trata-se de processos para definir e analisar requisitos de dados necessários para suportar processos de negócios com sistemas informatizados em organizações.
- Um modelo de dados fornece um estrutura para os dados usados em si, com definições e formatos específicos

- Hierárquico
- Rede
- Relacional
- Orientado a Objetos
- Não-Relacional

---
## Modelo Relacional

- Os princípios do modelo relacional foram esboçados por E.F Codd (IBM) em um artigo publicado em junho de 1970, intitulado "A Relational Model of Data for Large Shared Data Banks", no qual o Dr. Codd propôs o modelo relacional para sistemas de banco de dados.
- Antes disso eram usados modelos como o modelo de rede e o modelo hierárquico.
- No modelo relacional os dados são organizados em coleções de tabelas bidimensionais
- Essas tabelas são também chamadas de "Relações".
- Relações é uma forma de se organizar os dados em linhas e colunas
- Baseado em lógica e teoria de conjuntos

---
## Componentes do Modelo Relacional

O modelo relacional é composto, basicamente, por:

- Coleções de objetos ou relações que armazena dados
- Um conjunto de operadores que agem nas relações, produzindo outras relações
- Integridade de dado, para precisão e consistência.

---
## Banco de Dados Relacional

- Um Banco de dados relacional é uma coleção de relações, que são tabelas bidimensionais, onde os dados são armazenados.
- Como exemplo, podemos querer armazenar dados sobre os clientes de uma loja. Para isso, criamos tabelas para guardar diferentes conjuntos de dados relacionados a esses clientes, como dados pessoais, dados de compras, crédito, e outras.

## Componentes de um Banco de Dados Relacional

- `Tabela`: estrutura básica de armazenamento no SGBDR. Armazena todos os dados necessários sobre algo do mundo real, como clientes, pedidos ou produtos. Também chamada de Relação. Um banco de dados relacional pode conter uma ou mais Tabelas
- `Tupla`: ou linha/ registro, representa todos os dados requeridos por uma determinada ocorrência de entidade em particular. Por exemplo, os dados de um cliente específico. Cada linha em uma tabela deve ser identificada por uma chave primária de modo a não haver duplicações de registro.  
- `Colunas`: Unidade que armazena um tipo específico de dado(valor) - ou não armazena nada, com valor nulo. Esta é uma coluna não-chave, significado que seu valor pode se repetir em outras linhas da tabela.
- `Relacionamento`: Associação entre as entidades(tabelas), conectadas por chaves primárias e chaves estrangeiras.
- `Outros`: Índices, SP, Triggers, etc.

- `Chave Primária`: coluna(atributo) que identifica um registro de forma exclusiva na tabela. Por exemplo, o CPF de um cliente, contendo um valor que não se repete na relação.
- `Chave Estrangeira`: coluna que define como as tabelas se relacionam umas com as outras. Uma FK se refere a um PK ou uma chave única em outra tabela(ou na mesma tabela). Por exemplo, na tabela pedidos podemos ter uma chave estrangeira efetuando o relacionamento com a chave primária na tabela de clientes.

---
## Análise de Requisitos

- Nesta fase, são realizadas reuniões para coleta de informações, que analisam o que é exigido para o banco de dados a ser criado.
- Os processos de negócio são definidos, e as entidades, atributos e relacionamentos de BD são documentadas.
- A Análise é extremamente importante para o sucesso do projeto de BD.

---
## Modelo Entidade-Relacionamento

- MER, cria uma diagrama entidade-relacionamento a partir das especificações do negócio ou narrativas do usuário. Permite ilustrar as entidades em um negócio e também relacionamentos entre elas. Construídos o MER durante a fase de análise no ciclo de vida do desenvolvimento do sistema.
- Um MER separa as informações necessária a negócio das atividades que são realizadas no negócio.

## Componentes do MER

- `Entidade`: Algo significativo, sobre o qual devemos possuir informações. como exemplos, temos clientes, funcionários, pedidos e produtos.
- `Atributos`: Algo que descreve ou qualifica uma entidade. P. ex., A entidade cliente possui atributos que descrevem seu nome, endereço, telefone, número de identificação, entre outros, Atributos podem ser obrigatórios ou opcionais.
- `Relacionamento`: Trata-se de uma associação nomeada entre entidades, como um grau de associação. Por exemplo, clientes podem estar associados a pedidos.

## Convenções para modelagem de entidades relacionamentos e atributos

- **Entidades**: Nome único, singular; em caixa alta;
- **Atributos**: nome no singular; caixa baixa; atributos obrigatórios marcados com ' * '.
- **Relacionamentos**: nome identificador(verbo); opcionalidade ("deve ser" ou "pode ser"); grau ou cardinalidade("ume a apenas um", ou "um ou mais")

**Cardinalidade** significa que cada entidade pode ser ou deve em de forma uma e apena uma ou uma ou mais com outra entidade
