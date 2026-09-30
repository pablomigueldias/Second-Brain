---
titulo: "SQL Database Specialist: Comandos Essenciais para Gerenciamento de Bancos de Dados"
tags: [banco-de-dados, sql, sgbd, modelagem-de-dados, conceitos, ferramentas, dados]
data: 2026-09-27
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 34
conceitos: [Banco de Dados, SQL, MySQL, SGBD, Modelagem de Dados, Redundância, PRIMARY KEY, FOREIGN KEY]
---

# SQL Database Specialist: Comandos Essenciais para Gerenciamento de Bancos de Dados

> [!resumo] Do que se trata
> Esta aula oferece uma introdução prática aos comandos SQL para MySQL, abordando o acesso ao sistema, a criação e o gerenciamento de bancos de dados e tabelas. Ela demonstra a inserção de dados, a correção de erros e a aplicação de conceitos como chaves primárias e estrangeiras para garantir a integridade e otimização dos dados. O conteúdo enfatiza a importância do SGBD na prevenção de redundância e na otimização de buscas, consolidando a teoria com a prática.

## Para lembrar

- **Para listar os bancos de dados existentes no MySQL, usa-se o comando `SHOW DATABASES;`.**
- **Para criar um banco de dados, usa-se `CREATE DATABASE [nome_do_banco];` e para acessá-lo, `USE [nome_do_banco];`.**
- **Um SGBD pode ter vários bancos de dados diferentes, cada um com um esquema distinto, permitindo contextos e estruturas variadas.**
- **O comando `UNIQUE` é utilizado para garantir que não haja duplicação de valores em um campo específico de uma tabela, evitando redundância.**
- **Uma Foreign Key (Chave Estrangeira) oferece segurança, garantindo que um registro só possa ser inserido se o registro relacionado já existir e estiver devidamente cadastrado.**

## O que esta nota responde

- Como acessar e manipular o MySQL usando comandos básicos?
- Quais comandos SQL são usados para criar, gerenciar e deletar bancos de dados e tabelas?
- Como garantir a integridade e evitar redundância de dados em um banco de dados usando `UNIQUE` e `FOREIGN KEY`?

## Conceitos

**Banco de Dados** · **SQL** · **MySQL** · **SGBD** · **Modelagem de Dados** · **Redundância** · **PRIMARY KEY** · **FOREIGN KEY**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Introdução ao SQL e SGBD | ▪▪ |
| `04:00` | Criação de tabelas e atributos | ▪▪ |
| `09:40` | Schema, Constraints e Chave Primária | ▪▪ |
| `14:40` | Chave Estrangeira e Inserção de Dados | ▪▪▪ |
| `20:00` | Redundância, Otimização e ISSN | ▪▪ |
| `25:20` | Validação, Chave Estrangeira e Autoincremento | ▪▪▪ |
| `30:40` | Importância do SGBD e Próximos Passos | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Sistema Gerenciador de Banco de Dados (SGBD)** | Um SGBD pode ter vários bancos de dados diferentes, e cada um com um esquema distinto. Isso permite que um único sistema tenha contextos diferentes e estruturas com relação às entidades e relacionamentos. |
| **Primary Key** | É o identificador da instância relacionada à minha tabela. |
| **Estado Inicial do Banco de Dados e Schema** | Neste momento, o estado do banco de dados corresponde ao schema de dados, a estrutura em si. Isso ocorre porque não há instância alguma, nenhum tipo de dado inserido. O estado inicial do banco de dados é, portanto, equivalente ao esquema. |
| **Constraints** | Todo tipo de restrição e vantagem que o SGBD traz, relacionado aos dados, é definido através de constraints. |
| **Foreign Key (Chave Estrangeira)** | Uma Foreign Key é um atributo ou variável de uma tabela (entidade) que estabelece um link ou relacionamento com outra tabela, referenciando a chave primária dessa outra tabela. Ela serve para ligar duas entidades de um banco de dados. |
| **Constraint (Restrição)** | Uma constraint é uma regra ou condição que se insere em uma tabela para determinar que um atributo ou variável específica é uma Foreign Key, e a qual tabela e variável (geralmente a chave primária) ela está associada. |
| **ISSN** | O ISSN (International Standard Serial Number) é um número de oito dígitos que referencia uma determinada publicação. |

## Pegadinhas

- O campo `ISSN` é *case sensitive*; se você o definir com letras maiúsculas, deve sempre usá-lo dessa forma ao inserir informações.
- Ao usar `SELECT`, os dados são ordenados por inserção, não de forma alfanumérica ou alfabética, a menos que uma *query* específica seja usada para ordenar.
- Tentativas de inserção mal-sucedidas, mesmo que retornem erro, podem ocasionar um incremento no ID da tabela, fazendo com que o SGBD já trate de fazer esse autoincremento, mesmo que a instância não seja efetivamente criada.
- É uma convenção usar comandos SQL em letra maiúscula (ex: `CREATE TABLE`), mas o sistema entenderá se você usar em minúsculo.

## Teste-se

<details><summary>Qual o comando SQL para listar os bancos de dados existentes?</summary>

O comando SQL para listar os bancos de dados existentes é `SHOW DATABASES;`.

</details>

<details><summary>Qual a finalidade de uma `PRIMARY KEY`?</summary>

A `PRIMARY KEY` é o identificador da instância relacionada à tabela, garantindo a unicidade de cada registro.

</details>

<details><summary>Como o SGBD previne a redundância de informações?</summary>

O SGBD previne a redundância através de `constraints`, como o comando `UNIQUE`, que impede a duplicação de valores em um campo específico.

</details>

<details><summary>O que acontece com o `AUTO_INCREMENT` em tentativas de inserção mal-sucedidas?</summary>

Mesmo em tentativas de inserção mal-sucedidas que retornam erro, o SGBD já trata de fazer o autoincremento do ID da tabela, mesmo que a instância não seja efetivamente criada.

</details>

<details><summary>Qual a principal vantagem de usar um SGBD em relação à abordagem tradicional de guardar dados em arquivos?</summary>

A principal vantagem é o maior controle e otimização na manipulação dos dados, com algoritmos de busca mais eficientes e prevenção de redundância, o que não ocorre na abordagem tradicional sem programação adicional.

</details>

<details><summary>Qual a função de uma `FOREIGN KEY`?</summary>

Uma `FOREIGN KEY` estabelece um link ou relacionamento entre duas tabelas, referenciando a chave primária de outra tabela. Ela oferece segurança, garantindo que um registro só possa ser inserido se o registro relacionado já existir e estiver devidamente cadastrado.

</details>

## Conteúdo

`⏱ 00:00`

Com essa parte em que estamos estudando muita teoria, falamos sobre o que é um banco de dados, suas características, a arquitetura do banco de dados, a abordagem e também quando utilizá-lo e quando não.

Trouxe para vocês um exemplo. Como estamos falando da estrutura que o banco de dados traz para os dados, a formatação para os dados de uma maneira mais generalista, quis dar um exemplo bem básico e simples, pois é um modo introdutório.

Vamos falar sobre projetos, maturidades, desenvolver toda a parte relacionada ao design em diante e à inserção das informações do banco em uma próxima etapa, em um próximo momento. Agora, vamos dar o primeiro contato com o **SQL**.

### Acessando o MySQL

Para acessar, vou entrar com `sudo mysql`. Se você não for usuário `sudo`, você vai usar `mysql -u [seu_usuario] -p`.

Coloquei a senha. Já entrei no MySQL. A instalação foi feita em uma etapa anterior, tanto no Windows quanto no Linux. Agora, vamos manipular um pouco.

Já modelamos nosso cenário. Usei a ferramenta de design com vocês, com o mesmo exemplo dos slides. Vou mostrar um pouco do processo de criação do modelo, que é o modelo conceitual de alto nível.

Vou puxar de vez em quando algumas informações teóricas, só para podermos ver e assimilar mais um pouco. É mais fácil assimilar praticando do que simplesmente ouvindo e lendo.

> [!exemplo] A analogia da memória para o aprendizado
> Gosto muito de anotar. Brinco que, quando ouvimos ou lemos, estamos usando a memória RAM. Quando escrevemos, passamos pela memória RAM, fazemos um processo de I/O e mandamos para o hardware, para o HD.

### Comandos Básicos de SQL

Vou colocar os comandos em letra maiúscula para diferenciar o que é SQL e o que é informação do banco de dados.

Para listar os bancos de dados existentes, usamos o comando:
`SHOW DATABASES;`

Ele já vem com alguns bancos de dados criados no momento da instalação.

### Criando e Gerenciando Bancos de Dados

Precisamos criar nosso cenário. Vou simular a criação e a correção de um erro, para quem está começando já saber como deletar e refazer.

Para criar um banco de dados, use:
`CREATE DATABASE [nome_do_banco];`
Por exemplo: `CREATE DATABASE registro_publicacoes;`

Para verificar se foi criado, podemos listar novamente:
`SHOW DATABASES;`
O banco deve aparecer na lista.

Para entrar em um banco de dados específico, use:
`USE [nome_do_banco];`
Por exemplo: `USE registro_publicacoes;`

Após o comando, a mensagem `Database changed` indica que você entrou no banco de dados que acabou de criar.

> [!definicao] Sistema Gerenciador de Banco de Dados (SGBD)
> Um **SGBD** pode ter vários bancos de dados diferentes, e cada um com um esquema distinto. Isso permite que um único sistema tenha contextos diferentes e estruturas com...

`⏱ 04:00`

estruturas com relação às entidades e relacionamentos. A estrutura tabular que o SGBD traz é a mesma, só que o contexto, as entidades e relacionamentos podem ser diferentes.

> [!exemplo] Gerenciando bancos de dados
> Eu consigo ter vários bancos de dados no mesmo SGBD.
> >
> Quando dou o comando `use nome_do_banco`, estou dentro dele. Se eu der um `show`, tenho um conjunto que está zerado.
> >
> Ah, não é esse nome que eu quero. Usei `drop database`. Estava na dúvida se era só o nome ou eu tinha que colocar `database`. Deletei.
> >
> Se eu vier e verificar, não com `show tables`, mas com `show databases`, foi deletado com sucesso.
> >
> Agora vou dar um `create database first_example`. Este é um que vou estar criando e utilizando por vocês.
> >
> Vou dar um `use`. Ele não consulta o tab... Ah, funciona! `use first_example`. Essa é uma boa informação, ele usa o tab.

### Criando a Tabela 'periodicos'

Uma vez que já entramos no banco de dados, vamos criar agora a nossa tabela. O comando é `create table`. É o nome da tabela e as informações, ou seja, os atributos que quero que ela tenha.

Vamos criar a tabela `periodicos` com os seguintes atributos:

- `id`: `int` (ou `integer`), `auto_increment`.
> [!definicao] Primary Key
> É o identificador da instância relacionada à minha tabela.
> Ele também é uma **primary key**, que é o identificador da instância relacionada à minha tabela.
> - `nome_periodico`: `varchar`. Não pensei em tamanho, vou simplesmente colocar o valor. Vamos supor 20 caracteres, o tamanho da revista.
> - `ISSN`: `int`.
> [!atenção] Case Sensitivity
> O `ISSN` é *case sensitive*. Se você colocar dessa forma, tem que sempre lembrar de manter dessa forma quando for inserir as informações.

Aqui tem uma questão, vou deixar assim por enquanto e vou explicar para vocês a questão que está aqui. Lembro que temos uma questão aqui: periódicos vai estar relacionado a editoras. Portanto, em periódico, preciso ter a editora relacionada.

Para que eu possa criar a minha **foreign key**, preciso que na minha tabela `periodicos` exista uma variável que vou estar... Então, vai ser `id_editora int`. Não vou determinar ela como `foreign key` porque não tenho uma outra entidade criada ainda. Isso aqui estou até adiantando.

### Correção de Erro

Vamos ver se está tudo certo. Teve o `periodo` que já existe? Ah, já sei o que foi. Acho que foi no teste que fiz antes. Deixa eu dar um `drop`. Um exemplo, ele deve ter retornado isso e eu não percebi e acho que errei o nome do banco. `show databases`. Esqueci. Não, `database first_example`. Muito bem. Agora sim. Vou só copiar para o padrão, meu `database select`. É até bom.

`⏱ 09:40`

É até bom que eu acabei deletando e não criei o database de novo. Tenho que criar, dar um `USE` nele, para depois poder criar a tabela. Fiz essa besteira. `paste`. Feito.

### Criando a Entidade Editoras

A próxima etapa será criar a entidade `editoras`. Ela vai compor um atributo específico da entidade `periódica`.

Não há nada dentro da tabela, pois não foi inserido nenhuma instância.

> [!definicao] Estado Inicial do Banco de Dados e Schema
> Neste momento, o estado do banco de dados corresponde ao **schema de dados**, a estrutura em si. Isso ocorre porque não há instância alguma, nenhum tipo de dado inserido. O estado inicial do banco de dados é, portanto, equivalente ao esquema.

Vou usar `CREATE` em letra maiúscula.

> [!atenção] Convenção de Comandos SQL
> É uma convenção usar comandos SQL em letra maiúscula (ex: `CREATE TABLE`). Contudo, o sistema entenderá se você usar em minúsculo.

Vamos criar a tabela `editora`:

```sql
CREATE TABLE editora (
    id INT AUTO_INCREMENT,
    nome_editora VARCHAR(120),
    pais VARCHAR(5)
);
```

Agora, vamos adicionar os atributos relacionados a essa entidade. O `id` será `INT AUTO_INCREMENT`.

O `nome_editora` será um `VARCHAR` de 120 caracteres. Há dois campos, um em `editoras` e outro em `periódicos`, que não gostaríamos que se repetissem.

> [!definicao] Constraints
> Uma das vantagens de usar um SGBD é prevenir a redundância de informações. Todo tipo de restrição e vantagem que o SGBD traz, relacionado aos dados, é definido através de **constraints**.

Nesse caso, por exemplo, ao inserir uma instância (uma linha) na tabela `editora`, que contém ID, nome e país, não queremos que haja duas instâncias diferentes com o mesmo nome de editora. Não queremos redundância ou duplicação na tabela. Para isso, utilizaremos o comando `UNIQUE` para o campo `nome_editora`.

O campo `pais` será um `VARCHAR` de cinco caracteres, assumindo uma abreviação. Estamos adicionando várias restrições para aumentar a padronização do nosso banco de dados, mas isso será aprofundado mais adiante. Aqui é apenas uma amostra do que podemos fazer.

A `PRIMARY KEY` é o `id`. Uma outra maneira de definir a `PRIMARY KEY` é desta forma:

Lá na outra entidade, o que nós fizemos foi `id INT` (ou `INTEGER`) `AUTO_INCREMENT`. Se você esqueceu de colocar a `PRIMARY KEY` no momento da criação, não precisa refazer tudo. Você pode determiná-la separadamente, especificando o parâmetro para essa informação:

```sql
PRIMARY KEY (id)
```

Isso significa que o `id` será a chave primária, sem nenhuma informação adicional.

Se agora eu executar `SHOW TABLES`, terei a tabela criada.

`⏱ 14:40`

se agora, dessa vez, eu executo o comando `show tables`, eu obtenho um resultado em que aparecem duas linhas. Nessa minha tabelinha aqui, essas duas linhas estão representando as tabelas, as entidades que eu acabei de criar para representar o contexto dos meus dados, o mini mundo em que meus dados estão inseridos.

Eu não consigo ver ainda o que tem aqui dentro. Mas eu sei que determinei a minha tabela `periodicos`, e nela coloquei uma variável específica, que é a `id_editora`.

Como que eu faço o link, voltando para o nosso slide, entre a editora, que está relacionada ao periódico, e a minha entidade, a tabela `periodicos`? É justamente através da **Foreign Key** (chave estrangeira).

> [!definicao] Foreign Key (Chave Estrangeira)
> Uma **Foreign Key** é um atributo ou variável de uma tabela (entidade) que estabelece um link ou relacionamento com outra tabela, referenciando a chave primária dessa outra tabela. Ela serve para ligar duas entidades de um banco de dados.

### Adicionando uma Foreign Key

"Ah, mas eu já criei a tabela e já coloquei todos os atributos nela, e agora?"

O que você vai fazer é uma alteração. Você vai inserir uma **constraint** para determinar que um atributo, uma determinada variável daquela tabela, daquela entidade, é uma foreign key e a qual tabela e a qual variável desta tabela ela está associada.

> [!definicao] Constraint (Restrição)
> Uma **constraint** é uma regra ou condição que se insere em uma tabela para determinar que um atributo ou variável específica é uma Foreign Key, e a qual tabela e variável (geralmente a chave primária) ela está associada.

> [!exemplo] Adicionando uma Foreign Key com `ALTER TABLE`
> Para adicionar uma Foreign Key, utiliza-se o comando `ALTER TABLE`.
> >
> Primeiro, especifica-se a tabela que será modificada: `periodicos`.
> >
> A ação é adicionar uma constraint.
> >
> Em seguida, define-se um nome para a constraint (ex: `FK_editora_periodico`). Isso permite consultar, adicionar ou remover regras posteriormente, de acordo com as atualizações dentro do esquema de dados.
> >
> O tipo da constraint é `FOREIGN KEY`, e o atributo que será a chave estrangeira é `id_editora`.
> >
> Finalmente, indica-se a tabela e o atributo que essa Foreign Key referencia: `REFERENCES editora (id)`.
> >
> O comando completo é:
> ```sql
> ALTER TABLE periodicos
> ADD CONSTRAINT FK_editora_periodico
> FOREIGN KEY (id_editora)
> REFERENCES editora (id);
> ```
> Este comando cria uma ligação entre a variável `id` da tabela `editora` (entidade `editora`) e a variável `id_editora` da tabela `periodicos`.

Tudo certo. Nenhuma linha afetada, nenhum tipo de gravação realizado. Isso é um retorno da sua ação, do que a sua ação acabou de fazer.

Nós já temos todas as informações. Vou mostrar melhor.

### Inserindo Dados

Vamos inserir dados na tabela `editora`.

Aqui, eu vou definindo quais são as variáveis. Como eu coloquei `AUTO_INCREMENT` para o ID, eu não preciso inseri-lo. Isso já vai sempre gerar um valor válido para o ID. Toda vez que uma nova instância for inserida, ele vai auto-incrementar o ID.

Então, os campos são `nome_editora` e `pais`. E quais são os valores?
- `I3E`, dos Estados Unidos.
- `Data Science Academy`, dos Estados Unidos.

O comando `INSERT INTO` seria:
```sql
INSERT INTO editora (nome_editora, pais) VALUES
('I3E', 'Estados Unidos'),
('Data Science Academy', 'Estados Unidos');
```

Duas inserções sendo realizadas, duas linhas afetadas nessa tabela.

Então, se a gente vier aqui e executar `SELECT * FROM editora`, veremos os dados.

`⏱ 20:00`

`SELECT FROM editora`.

### Redundância e Otimização de Busca

Vou fazer aqui na mão, para vocês poderem ver, um `INSERT INTO editora` onde vou colocar `nome_editora` e `pais`.

Quais são os valores que vou inserir agora? Lembra que falamos de **redundância** e da teoria?

Quando temos a **abordagem tradicional** de guardar dados em um arquivo, não temos esse controle. A não ser que, no momento em que você está inserindo esses dados, faça algum tipo de controle para não haver redundância. Mas, mesmo assim, você teria que percorrer todo o arquivo, utilizando uma programação, para checar se há alguma informação duplicada durante a sua inserção.

Aqui, o **SGBD** faz isso para nós de uma maneira otimizada. Todos os algoritmos do SGBD são otimizados.

> [!exemplo] Otimização de busca no SGBD
> Os algoritmos de busca para retornar o resultado das *queries* são os mais utilizados. Não será um *array* nem uma lista encadeada; será, por exemplo, uma árvore ou uma árvore *hash*, que é ainda mais rápido.
> Assim, você tem implementações mais otimizadas para busca ao usar um SGBD, que é específico para isso, do que se estivesse utilizando uma abordagem tradicional. A abordagem tradicional pode ser usada, mas tem toda aquela questão que conversamos até aqui.

Vou inserir `I3E` novamente, com `Estados Unidos`. Se eu tentar inserir assim, ele vai reclamar, mesmo que não seja exatamente a mesma instância. Eu poderia ter uma `I3E` realmente nos Estados Unidos. Isso podemos tratar de outra forma depois.

O que tenho que mostrar aqui é um tratamento simples de redundância: ele reclama que está duplicado e que já existe um nome para essa editora.

Mas, se colocarmos `I3E versão da União Europeia`, ele aceita normalmente.

> [!atenção] Ordenação de dados
> Ao usar `SELECT`, os dados são ordenados por inserção, não de forma alfanumérica ou alfabética. Se precisar de ordenação no *front-end*, você pode fazer isso através de uma *query* específica para puxar, tratar e ordenar as informações para o cliente. Mas isso é outro assunto, não para agora, que estamos dando os primeiros passos em SQL e banco de dados.

### Inserindo Dados em Periódicos

Agora, a próxima coisa que quero fazer é um `SELECT` na tabela `periodicos`.

Como não há nada, farei um `INSERT INTO periodicos` com as seguintes informações: `nome_periodico`, `issn` e `id_editora`.

Para os valores, vou colocar o nome `Special Issue`. Existe realmente esse `Special Issue` do I3E, mas são frases específicas, por exemplo, para *blockchain* ou para *data science*. Há algumas variações. Vou colocar algo semelhante, mais geral, pois sei que existe.

> [!definicao] ISSN
> O **ISSN** (International Standard Serial Number) é um número de oito dígitos que referencia uma determinada publicação.
> Dependendo do nível do congresso, da revista ou do periódico (geralmente uma revista, que na área acadêmica é mais chamada por esse nome), ele terá um número associado.
> Além do ISSN, também existe o **DOI** (Digital Object Identifier), que é uma categoria mais elevada, mas enfim, são esses números.

`⏱ 25:20`

Aquele número de oito dígitos que referencia uma determinada publicação, para fins de exemplificação, seria 1, 2, 3, 4, 5, 6, 7, 8. A editora, neste caso, seria a I3N, que vou colocar como número 1. Vamos utilizar essa inserção.

### Inserção de Dados e Chave Única

Perfeito, tudo bem. E se eu tentar colocar algo que não existe, o sistema vai reclamar. Coloquei como **UNIQUE**? Sim, coloquei. Achei que eu tivesse tirado.

O que aconteceria se eu não tivesse colocado `UNIQUE`, que era a minha intenção, mas pelo jeito eu coloquei? Ele iria permitir uma duplicação dessa revista. Isso daria uma duplicação dentro dessa tabela, algo que a gente trata com `UNIQUE`. Mas pelo jeito eu já fiz isso.

Vamos só mudar aqui o valor do `as best in shoe` para `Jardim blockchain`, porque minha dissertação foi blockchain.

Ó, aqui tem uma coisa. Eu estou inserindo uma informação que não existe na minha entidade editora, que é o `ID 5`. `Later too long`? Ah, como eu botei `VARCHAR` pequeno, eu não posso usar um negócio tão grande. Quanto que eu coloquei? 20. Então, vou botar `Pest Fichu 2`.

### Erros de Inserção e Chaves Estrangeiras

Ah, sim, deu um erro aqui. Espera aí, deixa eu só arrumar isso aqui. Eu sei que ele comeu aquilo ali. Muito bem, foi. O que eu fiz aqui? Eu botei o `Specsfix 2`, mudei o... só que eu estava adicionando o `ID 5` de uma editora que não existe. Aqui eu estou colocando na mão o ID.

> [!exemplo] Validação de Dados no Frontend
> Se estivéssemos consumindo essas informações a partir de um frontend (em Python, Angular ou outra linguagem), você selecionaria qual é a editora. Para evitar erros, você pode determinar no frontend que o usuário selecione um dos botões, uma das editoras que estão ali. Assim, você escolhe o ID e submete. Se deixarmos a lista aberta para o usuário e ele, por uma edição, colocar uma informação errada, a inserção dessas informações falhará.

A **Foreign Key** me dá também essa segurança. Se eu só posso ter um periódico se existir uma editora, então eu não vou conseguir inserir no meu banco de dados um periódico sem a editora estar primeiramente e devidamente cadastrada.

> [!definicao] Foreign Key (Chave Estrangeira)
> Uma Foreign Key oferece segurança, garantindo que um registro (como um periódico) só possa ser inserido se o registro relacionado (como uma editora) já existir e estiver devidamente cadastrado no banco de dados.

Então, deixa eu só ver quais são aqui. Vou botar 4, 4. Por que 4? Ah, acho que não sei o que é. Bom, vou botar 4. Ok, funcionou.

Então, se nós dermos um `SELECT`... Ah, vai ficar sem isso. `FROM PERIODICUS`. Importante isso aqui. Muito bem.

### Autoincremento em Inserções Falhas

Olha só. Isso é uma coisa que a gente pode tratar depois. As minhas tentativas de inserção na tabela ocasionaram um alto incremento do meu ID. Eu não tenho quatro instâncias dentro da minha tabela `PERIODICOS`, eu tenho duas. Mas como eu tentei realizar duas inserções mal-sucedidas, que por algum motivo retornaram um erro, o SGBD ele já tratou de fazer esse autoincremento, que foi o que aconteceu também aqui. Por isso que eu falei, ah, já sei o que aconteceu.

> [!atenção] Autoincremento em Inserções Falhas
> Tentativas de inserção mal-sucedidas, mesmo que retornem erro, podem ocasionar um incremento no ID da tabela. O SGBD já trata de fazer esse autoincremento, mesmo que a instância não seja efetivamente criada. Isso significa que você pode ter IDs como 1, 2, 4, sem ter um registro para o ID 3, se a inserção do ID 3 falhou.

Então, quando eu olho aqui e falo, poxa, ID 4, mas eu não tenho 2 ou 3. Não. Isso aqui a gente vai ver depois como tratar também.

### Primeiros Passos com SQL

O que eu queria mostrar aqui é justamente ter esse primeiro contato com o `SQL`. Nós fizemos `SHOW TABLES`, nós inserimos.

`⏱ 30:40`

Nós inserimos as duas entidades, definimos os relacionamentos entre elas. O comando `select from` permite fazer consultas bem mais complexas, mas aqui, como eu falei, é só para iniciar com a editora.

### A Importância do SGBD

Como vimos na minha tentativa de inserção com uma ID de editora que não existia, foi mal sucedida.

> [!exemplo] Restrições de dados
> A tentativa de inserir dados com uma ID de editora inexistente resultou em falha. Isso demonstra que algumas restrições já estão sendo aplicadas pelo sistema.

Esse tratamento, esse maior controle da manipulação dos dados dentro do seu banco de dados pelo **SGBD**, torna a vida muito mais simples. É lógico que existem cenários onde não há necessidade de utilizar um SGBD, e são cenários específicos. Mas, em via de regra, em 90% a 98% dos casos, você vai utilizar um SGBD, seja `SQL` ou `NoSQL`.

### Próximos Passos e Exercício

Esta foi a nossa parte prática, só para dar um gostinho do primeiro contato. Se você já sabe, provavelmente nem passou por isso. Se você já sabe e quer se aprimorar, este é o primeiro contato que vocês estão tendo com o `SQL`.

Como eu já falei em outras partes, vamos destrinchar e fazer um projetinho do início ao fim. Eu vou mostrar para vocês — não vamos desenvolver, porque não é essa a proposta aqui — mas vamos utilizar um front-end para consumir esses dados. A maior parte do consumo desses dados é via front-end, pelos usuários.

Para que vocês possam ir treinando um pouco esses primeiros passos, façam o que eu fiz para outras duas entidades:
- Artigo relacionado a periódico.
- Autor relacionado a periódico.

Vocês vão determinar quem vai ter relacionamento com quem. Vocês vão precisar de **multiplicidade** agora. Façam uma coisa mais simples.

> [!exemplo] Relacionamento N para N
> Pode acontecer de um pesquisador ter mais de um artigo, e um artigo ter mais de um pesquisador. Isso seria um relacionamento N para N.

Porém, agora vocês podem desconsiderar essa questão, pois veremos mais para frente o que seria esse tipo de relacionamento. Para este exercício, vocês podem fazer algo mais inicial, determinando uma coisa mais simples como eu criei aqui com vocês.

## Relacionado

- [[../Introdução a Banco de Dados/contextualizacao-da-formacao-sql-database-specialist-apresentacao-da-instrutora-]]
- [[../Modelagem de Dados para Banco de Dados/modelagem-de-dados-introducao-e-modelo-entidade-relacionamento-mer]]
- [[../Introdução a Banco de Dados/jornada-da-formacao-sql-database-specialist]]
- [[../Introdução a Banco de Dados/bancos-de-dados-da-evolucao-ao-big-data]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `esquema do banco → schema`

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Então, até a próxima!

</details>
