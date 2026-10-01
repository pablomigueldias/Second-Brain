---
titulo: "Modelagem de Dados: Projeto Conceitual, Flexibilidade e Transição"
tags: [sgbd, dados, banco-de-dados, modelagem-de-dados, engenharia-de-software, fundamentos, conceitos]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 11
conceitos: [Aplicação de banco de dados, SGBD, Queries, GUI, Usuários Naive, SQLite, Modelo Entidade-Relacionamento, Projeto Conceitual]
---

# Modelagem de Dados: Projeto Conceitual, Flexibilidade e Transição

> [!resumo] Do que se trata
> Esta aula explora a relação entre aplicações de banco de dados e SGBDs, detalhando o processo de design e a importância da comunicação com o cliente. Aborda a flexibilidade necessária no projeto conceitual e a transição para a modelagem relacional. Também discute o papel de ferramentas como o SQLite em cenários de desenvolvimento mobile.

## Para lembrar

- **Usuários Naive interagem com o banco de dados de forma indireta, geralmente através de uma interface gráfica de usuário (GUI) ou API, sem conhecimento direto das queries ou da estrutura interna do banco.**
- **O SQLite é uma biblioteca da linguagem C que atua como um SGBD, sendo muito utilizado em ambientes mobile para persistência de dados.**
- **O design de bancos de dados se relaciona com o design de engenharia de software, especialmente no desenvolvimento de aplicações que acessam dados.**

## O que esta nota responde

- Como as aplicações de usuário interagem com um SGBD?
- Qual a importância da comunicação e flexibilidade no projeto conceitual de banco de dados?
- O que é SQLite e qual seu papel em ambientes mobile?

## Conceitos

**Aplicação de banco de dados** · **SGBD** · **Queries** · **GUI** · **Usuários Naive** · **SQLite** · **Modelo Entidade-Relacionamento** · **Projeto Conceitual**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Fundamentos de Aplicações e BD | ▪▪ |
| `04:20` | Etapas do Projeto de Banco de Dados | ▪▪▪ |
| `08:20` | Comunicação e Refinamento Conceitual | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Usuários Naive** | Usuários que interagem com o banco de dados de forma indireta, geralmente através de uma interface gráfica de usuário (GUI) ou API, sem conhecimento direto das queries ou da estrutura interna do banco. |
| **SQLite** | O SQLite é uma biblioteca da linguagem C que é um banco de dados. Ela gera toda uma interface e todo um sistema voltado para a persistência de dados, como um SGBD. É específico e muito utilizado em ambientes mobile, em cenários onde se desenvolve aplicativos para celular. |
| **Cliente** | A pessoa que está demandando um projeto. |

## Teste-se

<details><summary>O que são usuários naive em um contexto de banco de dados?</summary>

São usuários que interagem com o banco de dados de forma indireta, geralmente através de uma interface gráfica de usuário (GUI) ou API. Eles não possuem conhecimento direto das queries ou da estrutura interna do banco.

</details>

<details><summary>Quais são as três etapas principais de um projeto de banco de dados?</summary>

As etapas são: criar um projeto conceitual (modelo de alto nível), criar um projeto lógico baseado no modelo relacional e criar um projeto físico.

</details>

<details><summary>Por que a comunicação com o cliente é crucial na fase do projeto conceitual?</summary>

A comunicação é crucial para entender o que o cliente precisa e garantir que o projeto contemple os cenários esperados. Isso permite refinar o projeto conceitual antes de avançar para as próximas etapas.

</details>

<details><summary>O que é SQLite e onde ele é frequentemente utilizado?</summary>

SQLite é uma biblioteca da linguagem C que funciona como um banco de dados, gerando um sistema para persistência de dados. É muito utilizado em ambientes mobile, especialmente no desenvolvimento de aplicativos para celular.

</details>

<details><summary>Qual a principal diferença na flexibilidade entre o desenvolvimento de software e o projeto de banco de dados?</summary>

O projeto de banco de dados, embora dinâmico, não é tão flexível quanto o desenvolvimento de software devido à dependência entre suas etapas. Mudar o projeto em fases avançadas pode ser custoso.

</details>

## Conteúdo

`⏱ 00:00`

### Modelagem de Dados e Aplicações

Vamos falar um pouco sobre modelagem. Antes de começarmos, vou apenas pincelar um determinado assunto.

Uma aplicação de banco de dados possui um `BD` particular. Na verdade, ela possui uma série de bancos de dados dentro do sistema, e cada `BD` tem seu esquema relacionado.

Esse `BD` particular tem uma série de softwares que dão suporte a ele, permitindo diversas vantagens que o próprio `SGBD` possui: gerenciamento de dados, concorrência de transações, segurança, integridade, corretude, entre outras. Todas essas vantagens são contempladas a partir dos softwares que compõem o `SGBD`.

Além disso, existem softwares que precisam acessar esse banco, acessar esses dados, através de uma `API` ou de um acesso direto ao banco de dados. Esses softwares acabam utilizando, de maneira direta ou indireta, as `queries`. Essas `queries` podem gerar `updates`.

Quando tratamos de aplicações de usuário, esses softwares utilizarão uma `GUI` para que os usuários possam acessar os dados. As `queries` estarão encapsuladas na interface gráfica de usuário, de maneira que a operação se torna transparente para quem está acessando o banco.

A maioria dos usuários de banco de dados utiliza o banco de dados dessa forma, sendo categorizados como **usuários naive** ou ingênuos. Seriam os leigos que utilizam os `SGBDs`.

> [!definicao] Usuários Naive
> Usuários que interagem com o banco de dados de forma indireta, geralmente através de uma interface gráfica de usuário (`GUI`) ou `API`, sem conhecimento direto das `queries` ou da estrutura interna do banco.

> [!exemplo] Acesso ao Banco via Caixa Eletrônico
> Toda vez que você vai ao banco e coloca seu cartão no caixa eletrônico, você está utilizando uma `API`. Você está utilizando um intermediário que está acessando o banco de dados do banco, verificando seu saldo, seu extrato e puxando todas as informações relacionadas à sua conta.

Quando pensamos na parte de interface de usuário, podemos criar um software para mobile ou para outro fim. Trago o mobile neste cenário porque existe um software específico que é interessante, e você precisa avaliar o `trade-off` ao utilizá-lo ou não.

Até chegar ao desenvolvimento dessa aplicação, que acessa o banco de dados e retorna as informações (por exemplo, o próprio aplicativo do banco), passamos por algumas etapas:
-   **Design:** todo o design desse projeto, como será estruturado, o que terá, o que o usuário terá acesso, como ele responderá.
-   **Implementação.**
-   **Testes.**
-   **Produção:** após os testes, se tudo correu perfeitamente, podemos prosseguir para a produção do aplicativo.

Quando tratamos de aplicativo, essa parte está mais relacionada ao engenheiro de software. O design de bancos se relaciona ao de engenharia de software, ao design de uma aplicação.

Quando tratamos de design para uma interface mobile, podemos estar usando...

`⏱ 04:20`

a gente pode estar usando um `SQLite`.

> [!definicao] SQLite
> O `SQLite` é uma biblioteca da linguagem C que é um banco de dados, não simula [inaudível]. Ela gera toda uma interface e todo um sistema voltado para a persistência de dados, como um **SGBD** (Sistema Gerenciador de Banco de Dados). É específico e muito utilizado em ambientes mobile, em cenários onde se desenvolve aplicativos para celular.

Voltando, percebemos que esses dois processos (desenvolvimento de aplicação e de banco de dados) são entrelaçados. Isso é bem intuitivo e óbvio, porque toda aplicação provê um tipo de serviço, e esses serviços buscam dados. Esses dados precisam estar armazenados em algum lugar, geralmente em um SGBD, seja no ciclo ou relacional. O importante é que essas informações estão persistidas em algum lugar.

Para que haja sintonia entre a aplicação e o SGBD, eles acabam sendo definidos, às vezes, em conjunto.

> [!exemplo] Integração entre Desenvolvimento de Aplicação e SGBD
> Existem dois cenários comuns:
> - **Desenvolvimento Conjunto:** Se você está desenvolvendo um sistema e um banco de dados específico para uma aplicação que ainda está sendo desenvolvida, é possível integrar os dois times. Eles se comunicam para definir a melhor forma de integração entre os sistemas.
> - **Desenvolvimento para SGBD Existente:** Se o SGBD já existe e você precisa desenvolver uma aplicação para consumir suas informações, o grupo que está desenvolvendo o aplicativo consultará o DBA ou sua equipe sobre pontos específicos do SGBD, como estruturas e outras questões.

Isso mostra que esses dois mundos conversam e estão interligados.

### Modelagem de Dados e Flexibilidade

Aqui, estou definindo o **Modelo Entidade-Relacionamento** que será utilizado. No desenvolvimento do aplicativo, já sei que usarei uma estrutura voltada para um banco de dados relacional.

Essa metodologia e passo a passo não precisam ser engessados. Uma vez que você define seu projeto conceitual, você voltará e refinará esse projeto muitas vezes. Não será tão ágil ou super flexível como o desenvolvimento de um software, porque existe uma dependência entre as etapas de um projeto de banco de dados.

As etapas são:
- Criar um projeto conceitual (modelo de alto nível).
- Criar um projeto lógico, baseado no modelo relacional.
- Criar um projeto físico.

Nada impede de voltar à prancheta. É preciso considerar o *trade-off* disso, pois mudar, dependendo do tipo de alteração, pode custar caro. Voltar e dizer: "Isso não foi legal, não foi bem desenhado, vamos arrumar" pode acontecer.

> [!atenção] Flexibilidade no Projeto de Banco de Dados
> Não pense de maneira rígida. As coisas mudam, e às vezes você não contemplou um determinado cenário da maneira que seu cliente esperava.

`⏱ 08:20`

As coisas mudam, às vezes você não contemplou um determinado cenário da maneira que seu cliente esperava. Por isso, a comunicação é muito importante na fase do projeto conceitual.

### A Importância da Comunicação e a Definição de Cliente

Você precisa entender o que o seu cliente precisa. Quando falo cliente, não me refiro apenas a termos de venda.

> [!definicao] Cliente
> A pessoa que está demandando um projeto.

### O Processo do Projeto Conceitual

Se estou com um projeto de, por exemplo, ordem de serviço, preciso entender a dinâmica daquele contexto e qual é o fluxo da informação.

Vou fazer uma reunião com o cliente. Ele começa a listar o que precisa, você anota e faz perguntas. Mas um único *brainstorm* às vezes é pouco.

Você faz o seu projeto conceitual e depois volta para discutir. "É isso que a gente tem."

Geralmente, o projeto conceitual, como não contempla informações de implementação, é muito mais fácil de ser lido e entendido por um leigo ou uma pessoa fora do ambiente de desenvolvimento de projetos de dados.

### Refinamento do Projeto Conceitual

> [!exemplo] Interação com o cliente para refinamento
> Você apresenta o modelo conceitual ao cliente, dizendo: "Modelei dessa forma, baseado no que conversamos, e com isso você consegue isso, isso, isso."
> >
> O cliente pode responder: "Ah, isso aqui eu consigo responder." Ou: "Ah, mas isso aqui?"
> >
> Você então explica: "Não, isso a gente precisa de uma outra informação que é assim, assim, assim."
> >
> Esse diálogo permite refinar o projeto conceitual.

E você começa a refinar o seu projeto conceitual.

### Transição para a Modelagem Relacional

A partir daí, alinhadas as expectativas, você já pode passar para a outra parte da modelagem, que é mapear da entidade de relacionamento para o relacional.

### Dinamismo e Refinamento Contínuo

Apesar de ser um processo dinâmico, ele não é tão dinâmico quanto o desenvolvimento de um software propriamente dito.

> [!atenção] Refinamento contínuo
> É preciso estar refinando o modelo; não basta apenas uma versão do modelo conceitual ou relacional. Dependendo do tipo de relacionamento criado, você terá uma visão distinta das instâncias.

Fica um ponto de atenção para os próximos passos.

## Relacionado

- [[modelagem-de-dados-etapas-caracteristicas-do-sgbd-e-conceito-de-mundo-fechado]]
- [[modelagem-de-dados-abstracao-e-os-tres-niveis-de-modelos]]
- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[sgbd-etapas-estrutura-e-fases]]
