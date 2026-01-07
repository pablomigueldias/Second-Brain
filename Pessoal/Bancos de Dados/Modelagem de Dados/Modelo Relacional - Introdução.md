
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
