---
titulo: "SGBD: Classificação, Performance e Modelo Relacional"
tags: [sgbd, banco-de-dados, conceitos, fundamentos, dados, otimizacao, sql]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 6
conceitos: [SGBD, Modelo de dados, Modelo relacional, NoSQL, OLTP, Tabela, View, Custo de SGBD]
---

# SGBD: Classificação, Performance e Modelo Relacional

> [!resumo] Do que se trata
> Esta aula detalha os parâmetros para classificar SGBDs, incluindo modelo de dados, número de usuários, sites, custo, tipo de acesso e performance. Ela explora o trade-off entre modelos relacionais e NoSQL, e a importância do OLTP para sistemas de alta performance. Por fim, a nota define os conceitos de tabelas e views dentro do modelo relacional.

## Para lembrar

- **SGBDs podem ser classificados por modelo de dados (relacional ou NoSQL), número de usuários, número de sites (centralizado ou distribuído), custo (open source ou comercial), tipo do caminho de acesso e performance.**
- **O modelo relacional possui um limite de escalabilidade, após o qual SGBDs NoSQL se tornam mais interessantes para manter a performance em grandes volumes de dados e usuários.**
- **SGBDs podem ser gratuitos e open source (como MySQL e Postgres) ou soluções comerciais pagas (como Oracle), além de opções baseadas em nuvem (AWS, Azure).**
- **OLTP (Online Transaction Processing) é um sistema voltado para performance, ideal para cenários com alta demanda de transações, como reservas de avião.**
- **No modelo relacional, uma tabela é um arquivo, enquanto uma view é uma representação de alto nível associada a um usuário, abstraindo a implementação subjacente.**

## O que esta nota responde

- Quais são os principais parâmetros para classificar um SGBD?
- Quando um SGBD NoSQL é mais indicado que um relacional?
- O que é OLTP e qual sua finalidade?

## Conceitos

**SGBD** · **Modelo de dados** · **Modelo relacional** · **NoSQL** · **OLTP** · **Tabela** · **View** · **Custo de SGBD**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Classificação e parâmetros de SGBDs | ▪▪ |
| `04:20` | Performance, OLTP e modelo relacional | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Tabela** | Uma tabela é um arquivo. |
| **View** | Uma view é associada a um determinado usuário. |
| **OLTP** | online transaction processing |

## Teste-se

<details><summary>Quais são os principais parâmetros para classificar SGBDs?</summary>

Os parâmetros são: modelo de dados, número de usuários, número de sites, custo, tipo do caminho de acesso e performance.

</details>

<details><summary>Qual a relação entre o modelo relacional e o NoSQL em termos de performance e escalabilidade?</summary>

Existe um limite para o modelo relacional, e a partir dele, o NoSQL é interessante para ganhar performance. Conforme o modelo relacional fica muito grande, ele começa a ficar lento.

</details>

<details><summary>O que é OLTP e qual seu propósito?</summary>

OLTP significa Online Transaction Processing. É um sistema voltado para performance, desde sua concepção, em cenários de transações online.

</details>

<details><summary>Como o modelo relacional define tabelas e views?</summary>

No modelo relacional, uma tabela é um arquivo. Uma view é associada a um determinado usuário, representando uma visão de alto nível.

</details>

<details><summary>Cite dois exemplos de SGBDs open source e um comercial mencionados na aula.</summary>

MySQL e Postgres são exemplos de SGBDs open source. Oracle é um exemplo de solução comercial.

</details>

## Conteúdo

`⏱ 00:00`

### Classificação de SGBDs

Como podemos classificar os SGBDs e quando utilizá-los? Existem alguns parâmetros para essa classificação.

#### Parâmetros de Classificação

Os critérios de classificação são:

-   **Modelo de dados:** Se é relacional ou NoSQL.
-   **Número de usuários:** O limite para o modelo relacional e a necessidade de NoSQL para performance.
-   **Número de sites:** Se é centralizado ou distribuído.
-   **Custo:** Se é gratuito (*open source*) ou pago (assinatura).
-   **Tipo do caminho de acesso:** Como o SGBD lida com a estrutura de arquivos.
-   **Performance:** A capacidade do SGBD de ser performático.

Dependendo do tipo de informação que você quer armazenar, o modelo de dados será um ou outro. A maioria dos casos está relacionada ao NoSQL ou ao modelo relacional.

Com relação ao NoSQL, temos exemplos como `Cassandra` e `NovoDB`, que vêm ganhando bastante força no mercado.

#### Detalhamento dos Parâmetros

##### Modelo de Dados e Número de Usuários

Existe um limite para o modelo relacional. A partir desse limite, é interessante começar a pensar na utilização de um NoSQL para que ele ganhe mais performance. Conforme o modelo relacional fica muito grande, ele começa a ficar lento.

> [!exemplo] Trade-off de Performance e Escalabilidade
> É necessário um *trade-off* entre modelos de SGBD. Muitas vezes, é preciso utilizar mais de um SGBD.
> >
> Se uma página acessa a base de dados e há uma crescente utilização, com uma grande quantidade de informações e pessoas acessadas, pode-se partir para um SGBD mais robusto, como um NoSQL, para lidar com o aumento da demanda e manter a performance.

##### Número de Sites

Este parâmetro se refere a como o SGBD está espalhado: ele é distribuído ou centralizado?

Se for distribuído, como ele faz a integração entre os *clusters* e entre os nós desse *cluster*? Como ocorre o processamento? Há um *core* mais sobrecarregado do que outro? Essas são algumas questões relacionadas.

Dentro desse contexto, podemos considerar o Big Data, a replicação, a heterogeneidade e o DB federado. As fontes heterogêneas representam um desafio. Associando o número de sites à questão da heterogeneidade (que pode ser de fontes diferentes), temos a replicação e a questão do Big Data associado.

##### Custo

Qual é o custo desse SGBD?

> [!exemplo] Custo de SGBDs: Open Source vs. Comercial
> Um SGBD pode ser gratuito e *open source*, como o `MySQL` ou `Postgres`, que você pode instalar na sua máquina.
> >
> Ou pode ser uma solução comercial, como o `Oracle`, que exige a compra de uma assinatura.
> >
> Outras soluções podem ser baseadas em nuvem, como as da `AWS` ou `Azure`.
> >
> É preciso criar um *trade-off* e verificar qual é o melhor custo-benefício para a sua necessidade.

##### Tipo do Caminho de Acesso

Especificamente, este parâmetro se refere a como o SGBD lida com a estrutura de arquivos. Seja uma estrutura de arquivos invertidos ou armazenamento de arquivos, este campo é relacionado aos arquivos que servem de base para a construção de um SGBD.

##### Performance

Como um SGBD é um *software* de propósito geral, ele também precisa ser performático. Às vezes, ao tentar ser muito abrangente, ele perde em alguns recursos e na utilização desses recursos.

`⏱ 04:20`

quando a gente fica um pouquinho mais específico, a gente consegue a performance e sai um pouco desse cenário amplo demais.

### Performance e OLTP

Com relação à performance, nós temos o **OLTP**, que é um `online transaction processing`.

> [!exemplo] OLTP (Online Transaction Processing)
> Um cenário de reserva de avião é um exemplo onde o `OLTP` seria muito interessante de se utilizar. Se você quiser relembrar, vá na aula de `OLTP`, onde ficará bem explicadinho e você conseguirá fixar melhor vendo pela segunda vez.

O designer vai definir alguns requisitos, entender qual o momento e criar os requisitos para o contexto do banco de dados. Se for esse o caso, desde o início de sua concepção, será um sistema voltado para performance, ou seja, um sistema de `online transacting processes`.

### Modelo Relacional: Tabelas e Views

Nós temos a classificação e a correlação relacional. Temos a coleção de **tabelas**.

> [!definicao] Tabela
> Uma tabela é um arquivo.

E, com relação ao alto nível, temos a **view**.

> [!definicao] View
> Uma view é associada a um determinado usuário.

Através do modelo relacional, a gente consegue definir algumas requisições e alguns parâmetros associados ao contexto. Por exemplo, a tabela é armazenada em um arquivo, mas, via de alto nível, a view está associada a um usuário. Eu não preciso saber como isso funciona, como que está sendo implementado.

## Relacionado

- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-cenarios-de-nao-utilizacao-e-alternativas]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-ganhos-e-otimizacao-operacional]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-atores-tipos-de-usuarios-e-finalidade]]
- [[../Introdução a Banco de Dados/sgbds-os-mais-utilizados-no-mercado]]
