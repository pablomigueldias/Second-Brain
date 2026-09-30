---
titulo: "Modelagem de Dados: Abstração e os Três Níveis de Modelos"
tags: [modelagem-de-dados, banco-de-dados, sgbd, pensamento-computacional, conceitos, sql, sistema]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 9
conceitos: [Modelagem, Abstração, Sistemas Gerenciadores de Banco de Dados (SGBDs), Modelo de Dados Conceitual, Modelo de Entidade-Relacionamento (ER), Modelo Representacional, Modelo de Dados Físico, Modelos de Dados Autodescritivos]
---

# Modelagem de Dados: Abstração e os Três Níveis de Modelos

> [!resumo] Do que se trata
> A aula explora a modelagem de dados, associando-a à capacidade de abstração para definir problemas e soluções em SGBDs. Ela detalha os três modelos de dados principais: Conceitual (alto nível), Representacional (intermediário) e Físico (baixo nível), explicando seus focos e objetivos. Por fim, aborda a autodescritividade desses modelos, que permitem compreender suas propostas.

## Para lembrar

- **Abstração é a capacidade de trazer algo do específico para o geral, representando um conceito de forma abrangente para ser aplicado em diversos cenários.**
- **A modelagem em SGBDs envolve a definição de relacionamentos, objetos, estrutura, atributos, constraints e operações, além de requisitos funcionais e não funcionais.**
- **Existem três modelos de dados principais: Conceitual (alto nível), Representacional (intermediário) e Físico (baixo nível).**
- **O Modelo de Dados Conceitual é de alto nível, foca em entidades, atributos e relacionamentos, visando definir o que o sistema deve conter, independentemente da tecnologia.**
- **O Modelo de Dados Físico é de baixo nível, atrelado à especificidade do sistema, detalhando como as informações serão persistidas, incluindo índices, estrutura de armazenamento e performance.**

## O que esta nota responde

- Qual a relação entre modelagem de dados e abstração?
- Quais são os três modelos de dados e qual o foco de cada um?
- Como os modelos de dados conceitual, representacional e físico se diferenciam em termos de nível e objetivo?

## Conceitos

**Modelagem** · **Abstração** · **Sistemas Gerenciadores de Banco de Dados (SGBDs)** · **Modelo de Dados Conceitual** · **Modelo de Entidade-Relacionamento (ER)** · **Modelo Representacional** · **Modelo de Dados Físico** · **Modelos de Dados Autodescritivos**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Modelagem, Abstração e Três Níveis de Modelos | ▪▪ |
| `04:20` | Detalhes dos Modelos e Autodescritividade | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Abstração** | Trazer algo do específico para o geral, para o generalista. Representar o conceito de forma abrangente, aplicável a diversos cenários, sem aspectos particulares. |
| **Modelo de Dados Conceitual** | Modelo de alto nível focado em entidades, atributos e relacionamentos, que define o que o sistema deve conter, independentemente da tecnologia. |
| **Modelo Representacional** | Modelo intermediário focado na estrutura do banco de dados, que define essa estrutura através da linguagem SQL. |
| **Modelo de Dados Físico** | Modelo de baixo nível focado nos requisitos de operação do sistema, que implementa o sistema detalhando como os dados serão armazenados (ex: índices, estrutura de dados, persistência). |
| **Modelo ER estendido** | Extensão do modelo de entidade-relacionamento que inclui conceitos como generalização e especialização, atrelados à programação orientada a objetos. |
| **Modelos de dados autodescritivos** | Modelos a partir dos quais conseguimos entender o que cada um propõe, descrevendo a estrutura de dados e o 'meio mundo'. |

## Teste-se

<details><summary>Qual a principal característica da abstração na modelagem de dados?</summary>

A abstração foca no essencial, retirando informações particulares para representar o conceito de forma abrangente, aplicável a diversos cenários.

</details>

<details><summary>Quais são os três modelos de dados abordados na aula?</summary>

Os três modelos são: Modelo de Dados Conceitual de Alto Nível, Modelo Representacional e Modelo de Dados Físico.

</details>

<details><summary>Qual o foco principal do Modelo de Dados Conceitual?</summary>

O Modelo de Dados Conceitual foca em entidades, atributos e relacionamentos, visando definir o que o sistema deve conter, independentemente da tecnologia.

</details>

<details><summary>O que o Modelo de Dados Físico detalha?</summary>

O Modelo de Dados Físico detalha como as informações serão persistidas, incluindo a criação de índices, a estrutura de armazenamento (ex: árvore hash) e o tipo de estrutura de dados utilizado, focado na performance.

</details>

<details><summary>O que significa dizer que os modelos de dados são autodescritivos?</summary>

Significa que, a partir deles, conseguimos entender o que cada um propõe, descrevendo a estrutura de dados e o contexto em que estão inseridos.

</details>

<details><summary>Qual a linguagem utilizada para definir a estrutura no Modelo Representacional?</summary>

No Modelo Representacional, a estrutura é definida através da linguagem SQL.

</details>

## Conteúdo

`⏱ 00:00`

Vamos entrar no nosso assunto sobre arquiteturas, modelos, esquemas e instâncias. Este curso abordará a parte de arquitetura, focando especificamente em três aspectos: modelos, esquemas e instâncias.

### Modelagem e Abstração

O tema da modelagem está muito associado à capacidade de abstração.

> [!definicao] Abstração
> Trazer algo do específico para o geral, para o generalista. Não se deve trazer aspectos particulares de um determinado contexto, mas sim representar o conceito da maneira mais abrangente possível, para que ele possa ser aplicado a uma maior quantidade de cenários.

Ao pensar em modelagem, é necessário focar no que é essencial, retirando aquelas informações que acabam particularizando o contexto. Esse tipo de explicação está muito atrelado à abstração do pensamento computacional, o que nos ajuda na definição de problemas e soluções desses problemas.

### Modelagem em SGBDs

Quando pensamos em algo voltado para Sistemas Gerenciadores de Banco de Dados (SGBDs), precisamos definir:

*   Os relacionamentos e os objetos que compõem esses relacionamentos.
*   A estrutura, as características, os atributos e também as *constraints*.
*   As operações que estão relacionadas.

Por exemplo, existe um determinado grupo de usuários que necessitam de restrição de acesso, ou então eles apenas acessam uma determinada *view* do nosso banco de dados. Um conjunto de operações pode ser executado por um usuário com mais privilégios.

Assim, conseguimos definir e enriquecer o nosso modelo dessa forma, definindo requisitos funcionais e não funcionais dentro do contexto. A partir daí, conseguimos tirar essa visão de focar no que é realmente específico e levar para o geral.

> [!exemplo] Processo de Modelagem
> 1. Definir um modelo generalista para o contexto (ex: universidade, e-commerce).
> 2. Pensar nas especificidades, como quem precisa de restrição de acesso e quem não pode acessar determinado conteúdo.
> 3. Definir as operações associadas ao modelo de dados.

A classificação das informações está muito atrelada à estrutura que o dado possui, e essa estrutura será definida pelo modelo.

### Os Três Modelos de Dados

No nosso contexto, existem três modelos:

1.  **Modelo de Dados Conceitual de Alto Nível:** Este modelo está atrelado ao modelo de Entidade-Relacionamento.
2.  **Modelo Representacional:** Este modelo fica no meio.
3.  **Modelo de Dados Físico:** Este modelo está relacionado à implementação do sistema.

Para entender a diferença entre eles, podemos compará-los:

| Modelo | Nível | Foco Principal | Objetivo |
| :--- | :--- | :--- | :--- |
| **Conceitual** | Alto Nível | Entidades, atributos e relacionamentos. | Definir o que o sistema deve conter, independentemente da tecnologia. |
| **Representacional** | Intermediário | Estrutura do banco de dados. | Definir a estrutura através da linguagem `SQL`. |
| **Físico** | Baixo Nível | Requisitos de operação do sistema. | Implementar o sistema, detalhando como os dados serão armazenados. |

Em resumo, estamos indo de um alto nível para um baixo nível. Enquanto no modelo de dados conceitual estamos falando de entidades, atributos e relacionamentos, no modelo de dados físico, é que realmente definimos os requisitos de operação do sistema.

`⏱ 04:20`

O **modelo de dados conceitual** é de alto nível e visa apenas representar a situação, o contexto em que os dados estão inseridos, tentando montar um cenário autoexplicativo, principalmente para quem é leigo. A entidade-relacionamento é muito interessante nesse sentido, pois traz figuras e formas simples do nosso dia a dia para exemplificar um modelo de dados.

O modelo de entidade-relacionamento tem diversos recursos. Com o desenvolvimento da tecnologia e o amadurecimento do software, outros conceitos e paradigmas surgiram, e a modelagem de dados também evoluiu. Em um momento diferente, criou-se uma extensão do modelo de entidade-relacionamento, o **modelo ER estendido**. Ele carrega consigo informações como generalização e especialização, atreladas à ideia da programação orientada a objetos.

### Modelo de Dados Representacional

O **modelo representacional** está entre o físico e o de alto nível (o conceitual). Nele, conseguimos definir as `constraints` através das linguagens utilizadas, no nosso caso, `SQL`, e também definir as operações.

A partir do modelo de dados de alto nível, geramos um modelo de dados relacional para criar a nossa estrutura. Poderíamos ter também um modelo hierárquico, relacionado a sistemas legados. O modelo representacional classifica o nosso modelo como algo mais específico de um banco de dados, como um modelo hierárquico do legado ou um modelo relacional mais atual.

### Modelo de Dados Físico

O **modelo de dados físico** é atrelado à especificidade do sistema e geralmente precisa de um especialista.

> [!exemplo] Detalhes do Modelo Físico
> O modelo físico detalha como as informações serão persistidas, se serão criados índices e para quais informações, qual será a estrutura que armazenará esses dados (por exemplo, uma árvore *hash*), e qual tipo de estrutura de dados será utilizado. Enfim, são informações relacionadas ao modelo físico: arquivos, índices, persistência, e realmente voltado para a performance.

### Modelos Autodescritivos

Algo interessante de verificar é que esses modelos são **modelos de dados autodescritivos**. Conseguimos entender, a partir deles, o que cada um propõe.

> [!exemplo] Autodescritividade dos Modelos
> - Se falamos de um modelo de dados físico, entendemos que ele está especificando o sistema.
> - Se falamos do modelo de dados representacional, entendemos que ele está falando de um esquema relacional.
> - Se voltamos para o modelo de dados conceitual, sabemos que estamos falando de um modelo de mais alto nível, que define os requisitos do sistema.

Conseguimos, então, definir a descrição do nosso "meio mundo" e a descrição dessa estrutura de dados. Podemos utilizar arquivos `XML` ou uma abordagem com informações usando `Qvela`, que seria mais próximo do `NoSQL`. A partir dessas informações, temos um modelo de dados autodescritivo, tanto em alto nível quanto no modelo de implementação e no modelo físico.

## Relacionado

- [[../../../Introdução à Programação e Pensamento Computacional/Pensamento computacional/fundamentos-e-pilares-do-pensamento-computacional]]
- [[../../../Introdução à Programação e Pensamento Computacional/Pensamento computacional/abstracao-e-generalizacao-conceitos-modelagem-e-aplicacoes-em-sistemas]]
- [[../Modelagem de Dados para Banco de Dados/modelagem-de-dados-introducao-e-modelo-entidade-relacionamento-mer]]
- [[../Introdução a Banco de Dados/modelagem-de-dados-do-contexto-relacional-a-era-do-big-data-e-paradigmas-cientif]]
