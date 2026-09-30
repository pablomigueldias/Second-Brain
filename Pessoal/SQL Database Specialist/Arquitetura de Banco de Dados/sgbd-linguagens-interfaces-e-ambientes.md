---
titulo: "SGBD: Linguagens, Interfaces e Ambientes"
tags: [sgbd, banco-de-dados, sql, conceitos, fundamentos, linguagens-de-programacao, sistema]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 7
conceitos: [SGBD, Linguagem SQL, Data Definition Language (DDL), Storage Definition Language (SDL), Data Manipulation Language (DML), DML de Baixo Nível Procedural, DML de Alto Nível Não Procedural, Esquema de Banco de Dados]
---

# SGBD: Linguagens, Interfaces e Ambientes

> [!resumo] Do que se trata
> Esta aula explora as linguagens, interfaces e ambientes essenciais para SGBDs, detalhando a função da Data Definition Language (DDL) na criação da estrutura do banco de dados. Aborda a Storage Definition Language (SDL) para definição de armazenamento e a Data Manipulation Language (DML) para manipulação de dados. A aula diferencia ainda os dois tipos de DML: a procedural de baixo nível e a não procedural de alto nível, explicando suas características e aplicações.

## Para lembrar

- **A Data Definition Language (DDL) é utilizada para definir o esquema do banco de dados, criando toda a sua estrutura e gerando os modelos relacional e físico.**
- **A Storage Definition Language (SDL) está relacionada à definição e ao armazenamento de dados, permitindo a criação de views, índices de cache e a disposição otimizada das informações.**
- **A Data Manipulation Language (DML) tem como propósito persistir e permitir o consumo de dados, possibilitando inserir, recuperar e atualizar informações no banco de dados.**
- **A DML de baixo nível procedural requer uma aplicação separada e foca no 'como' as operações são executadas, geralmente inserindo dados via loop, um por vez.**
- **A DML de alto nível não procedural se preocupa apenas em especificar 'o que' recuperar, permitindo a inserção de conjuntos de dados de uma só vez, com o SGBD decidindo o 'como'.**

## O que esta nota responde

- Quais são as principais linguagens e interfaces utilizadas em Sistemas Gerenciadores de Banco de Dados (SGBDs)?
- Qual a função da DDL, SDL e DML na arquitetura de um banco de dados?
- Quais as diferenças operacionais entre a DML de baixo nível procedural e a DML de alto nível não procedural?

## Conceitos

**SGBD** · **Linguagem SQL** · **Data Definition Language (DDL)** · **Storage Definition Language (SDL)** · **Data Manipulation Language (DML)** · **DML de Baixo Nível Procedural** · **DML de Alto Nível Não Procedural** · **Esquema de Banco de Dados**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | SGBD: Linguagens, Interfaces e Ambientes | ▪▪ |
| `05:00` | DML: Procedural vs Não Procedural | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Data Definition Language (DDL)** | Linguagem de definição de dados, utilizada para definir o esquema do banco de dados e criar toda a estrutura, gerando o modelo relacional e físico. O papel do DBA e do designer se misturam. |
| **Storage Definition Language (SDL)** | Linguagem relacionada à definição e ao armazenamento de dados. Permite a definição de índices de cache, disposição de informações e está relacionada às views para representar contextos limitados. |
| **Data Manipulation Language (DML)** | Linguagem para persistir e consumir dados. Permite inserir, recuperar e atualizar informações, proporcionando liberdade para consumir os dados do banco. |

## Pegadinhas

- A maioria dos SGBDs não utiliza os três tipos de linguagem SQL (DDL, SDL, DML) de forma explícita; apenas uma minoria os emprega.
- Na DML, a linguagem de baixo nível procedural foca no 'como' recuperar informações, enquanto a de alto nível não procedural foca apenas no 'o que' recuperar.

## Teste-se

<details><summary>Qual a principal função da Data Definition Language (DDL)?</summary>

A DDL é utilizada para definir o esquema do banco de dados, criando toda a estrutura e gerando o modelo relacional e físico.

</details>

<details><summary>O que a Storage Definition Language (SDL) permite definir?</summary>

A SDL permite a definição e o armazenamento de dados, incluindo índices de cache, disposição de informações e views para representar contextos limitados.

</details>

<details><summary>Quais são as operações básicas que a Data Manipulation Language (DML) possibilita?</summary>

A DML possibilita inserir, recuperar e atualizar informações, proporcionando liberdade para consumir os dados do banco.

</details>

<details><summary>Qual a diferença fundamental entre a DML de baixo nível procedural e a de alto nível não procedural em relação ao foco da operação?</summary>

A DML de baixo nível procedural se preocupa em especificar 'como' recuperar as informações, enquanto a de alto nível não procedural se preocupa apenas em especificar 'o que' recuperar.

</details>

## Conteúdo

`⏱ 00:00`

Olá! Seguindo nosso assunto de arquitetura, falaremos sobre linguagens, interfaces e ambientes de SGBDs. Além das linguagens e interfaces, abordaremos ambientes, utilitários e ferramentas interessantes para serem utilizadas em conjunto com o SGBD.

Para começar, para consumir e inserir dados de uma determinada estrutura, precisamos de uma linguagem bem definida associada ao modelo. O modelo relacional possui a linguagem SQL associada a ele.

Temos linguagens e interfaces associadas ao usuário para que ele possa utilizar os recursos do banco de dados. Para definir e criar informações no banco de dados, os comandos são caracterizados como Data Definition Language.

> [!definicao] Data Definition Language (DDL)
> É uma linguagem de definição de dados, onde o papel do DBA e do designer se misturam. Ambos utilizam a mesma definição de linguagem.
> >
> A DDL é utilizada para definir o esquema do banco de dados, criando toda a estrutura. A partir dela, geram-se o modelo relacional e o modelo físico.

DDL e DML são ambas linguagens SQL. Contudo, conseguimos definir, de maneira abstrata, a que tipo de linguagem pertence cada comando SQL.

Em poucos SGBDs, existe uma separação explícita entre o design e o DBA. Quando se trata de persistência física, utilização de índices e outras questões, podemos falar da SDL.

> [!definicao] Storage Definition Language (SDL)
> É a linguagem relacionada à definição e ao armazenamento de dados.
> >
> A SDL também está relacionada às *views*, onde conseguimos representar um contexto limitado para um conjunto de pessoas. Ela permite a definição de índices de cache e a disposição das informações da melhor maneira possível.

Temos, então, uma separação mais explícita, onde cada um tem seu papel, apesar de todos serem SQL. Há uma linguagem específica para *views* e uma linguagem para *storage*.

Além disso, precisamos das linguagens de manipulação. Existem três linguagens, mas a maioria dos SGBDs não as utiliza dessa forma; é uma minoria que emprega os três tipos de linguagem SQL.

A DDL é realmente utilizada pela grande maioria dos SGBDs para a definição de dados, permitindo definir o esquema e as informações sobre as entidades.

Em contrapartida, temos a DML.

> [!definicao] Data Manipulation Language (DML)
> O intuito de persistir dados é que eles sejam consumidos por alguém, geralmente por uma série de pessoas envolvidas em determinado contexto.
> >
> A partir da DML, é possível inserir, recuperar e atualizar informações, proporcionando liberdade para consumir os dados do banco.

A DML possui dois tipos de linguagem. Apesar de não ser muito falado, no livro do Navathe, nossa referência bibliográfica, temos a DML não procedural, de alto nível, onde as operações do banco de dados são executadas por tempo.

`⏱ 05:00`

onde as operações do banco de dados são executadas por tempo.

### Tipos de Linguagem DML

A DML também possui um tipo de **linguagem de baixo nível procedural**. Nesse caso, é necessário criar uma aplicação separada para dar suporte a essa abordagem, o que implica em verificar a execução dessas operações.

> [!exemplo] Inserção de dados em DML
> Ao inserir dados utilizando uma linguagem de baixo nível procedural de DML, a persistência ocorre via loop, através de uma aplicação de usuário. A cada loop, a cada passo, um dado é inserido.
>
> Em contraste, com uma **linguagem de alto nível não procedural**, é possível inserir uma série de conjuntos de dados de uma só vez, pois as operações são executadas por tempo.

Uma característica importante da linguagem de alto nível não procedural é que ela se preocupa apenas em especificar "o que" recuperar, sem se importar com "como" o SGBD fará isso. Já no baixo nível, é preciso se preocupar com o "como", pois o usuário define um loop para buscar as informações, exigindo a compreensão do processo de recuperação.

Em resumo, a linguagem de baixo nível procedural especifica o "como", enquanto a de alto nível simplesmente pede o "que".

| Característica         | DML de Baixo Nível Procedural                                  | DML de Alto Nível Não Procedural                               |
| :--------------------- | :------------------------------------------------------------- | :------------------------------------------------------------- |
| **Natureza**           | Procedural                                                     | Não Procedural                                                 |
| **Aplicação**          | Requer aplicação separada para suporte.                        | Não requer aplicação separada (operações por tempo).           |
| **Execução (Inserção)**| Persistida via loop; inserção de um dado por passo/loop.       | Inserção de conjuntos de dados "em uma tacada só" (por tempo). |
| **Foco**               | Preocupa-se em *como* recuperar as informações (define o loop). | Preocupa-se apenas em *o que* recuperar ("quero recuperar isso"). |
| **SGBD**               | O usuário define o *como*.                                     | O SGBD decide o *como*.                                        |

## Relacionado

- [[sql-database-specialist-comandos-essenciais-para-gerenciamento-de-bancos-de-dado]]
- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[modelagem-de-dados-abstracao-e-os-tres-niveis-de-modelos]]
- [[sgbd-ganhos-e-otimizacao-operacional]]
