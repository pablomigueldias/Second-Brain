---
titulo: "Modelagem de Dados: Desenvolvimento, Implementação e Integração"
tags: [modelagem-de-dados, banco-de-dados, sgbd, fundamentos, sql, engenharia-de-software, dados]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 12
conceitos: [Levantamento de Requisitos, Projeto Conceitual, Especificação de Acesso, CRUD, Regra 20/80 para Acessos ao Banco de Dados, Online Transaction Processing (OLTP), Online Analytical Processing (OLAP), Data Model Mapping]
---

# Modelagem de Dados: Desenvolvimento, Implementação e Integração

> [!resumo] Do que se trata
> Esta aula detalha as fases interligadas de desenvolvimento de aplicações e banco de dados, desde o levantamento de requisitos até a implementação e testes. Ela explora a relação crucial entre a especificação de acesso da aplicação e o projeto físico do SGBD, enfatizando a necessidade de desenvolvimento concorrente. A aula também aborda a regra 20/80 para acessos ao banco de dados, a classificação de aplicações por uso de dados (OLTP e OLAP), e o processo de mapeamento do modelo de dados para o design físico.

## Para lembrar

- **A especificação de acesso é um ponto crucial de conexão entre a aplicação e o projeto físico do SGBD, definindo o CRUD (Create, Read, Update, Delete) e as restrições de acesso.**
- **A regra 20/80 para acessos ao banco de dados indica que 80% dos acessos são para operações CRUD simples e 20% para consultas mais complexas.**
- **Aplicações são classificadas como Online Transaction Processing (OLTP) para alta performance em transações online ou Online Analytical Processing (OLAP) para análise e tomada de decisão.**
- **Data Model Mapping é o processo de mapear o modelo de dados de alto nível (conceitual) para o modelo específico (relacional), preparando-o para a implementação do SGBD.**

## O que esta nota responde

- Quais são as fases de desenvolvimento de aplicações e banco de dados e como elas se interligam?
- Como a especificação de acesso e o CRUD são definidos e qual a sua relação com o projeto físico do SGBD?
- O que são OLTP e OLAP, e como o Data Model Mapping se encaixa no desenvolvimento do banco de dados?

## Conceitos

**Levantamento de Requisitos** · **Projeto Conceitual** · **Especificação de Acesso** · **CRUD** · **Regra 20/80 para Acessos ao Banco de Dados** · **Online Transaction Processing (OLTP)** · **Online Analytical Processing (OLAP)** · **Data Model Mapping**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Fases e integração de desenvolvimento | ▪▪ |
| `04:20` | Premissas, CRUD, tipos de processamento | ▪▪ |
| `09:00` | Mapeamento e design de dados | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Levantamento de Requisitos** | É a fase de comunicação com o cliente, onde se levantam e se analisam os dados necessários. |
| **Projeto Conceitual** | O banco de dados passa por esta fase, que é o modelo de alto nível. |
| **Análise Funcional do Sistema** | No mundo do desenvolvimento de software, esta análise define o que a aplicação vai precisar fornecer e o que ela deve fazer. |
| **Especificação de Acesso** | Define quem pode acessar, o que pode ser acessado e qual é o caminho para que a aplicação acesse ou seja acessada por informações. |
| **Online Transaction Processing (OLTP)** | Alta performance para transações online. |
| **Online Analytical Processing (OLAP)** | Utiliza data warehouses para análise e tomada de decisão para negócios. |
| **Hybrid Transaction Analytical Processing (HTAP)** | Modelo híbrido que combina a performance de OLTP com a capacidade analítica de OLAP. |
| **Minimundo** | O texto de Minimundo é o que se quer modelar. |
| **Data Model Mapping** | É o mapeamento do modelo de dados do alto nível para o específico, que é o relacional. |

## Pegadinhas

- O modelo conceitual de dados é independente do banco de dados, enquanto o modelo posterior (físico) é específico ao SGBD.

## Teste-se

<details><summary>Quais são as quatro fases principais do desenvolvimento de um projeto, conforme descrito na aula?</summary>

As fases são: Levantamento de Requisitos, Projeto Conceitual, Análise Funcional do Sistema e Especificação de Acesso. Elas ocorrem em paralelo e são cruciais para o desenvolvimento de aplicações e bancos de dados.

</details>

<details><summary>Qual a importância da especificação de acesso na relação entre aplicação e banco de dados?</summary>

A especificação de acesso é um ponto crucial de conexão, definindo quem pode acessar, o quê e como. Ela deve ser verificada em relação ao projeto físico do SGBD e suas restrições precisam refletir na aplicação para que esta seja desenvolvida corretamente.

</details>

<details><summary>Explique a Regra 20/80 para acessos ao banco de dados.</summary>

A Regra 20/80 estabelece que 80% dos acessos ao banco de dados são de CRUD simples, enquanto os 20% restantes correspondem a consultas mais complexas. Essa regra ajuda a entender o perfil de uso dos dados.

</details>

<details><summary>Quais são os três tipos de classificação de aplicações por uso de dados e suas características principais?</summary>

As aplicações são classificadas como OLTP (alta performance para transações online), OLAP (usa data warehouses para análise e tomada de decisão) e HTAP (modelo híbrido que combina performance OLTP com capacidade analítica OLAP).

</details>

<details><summary>O que é o Data Model Mapping no contexto do desenvolvimento de banco de dados?</summary>

Data Model Mapping é o mapeamento do modelo de dados de alto nível para o modelo específico, que geralmente é o relacional. É a transição do modelo conceitual para o modelo que será implementado no SGBD.

</details>

<details><summary>Por que o desenvolvimento do banco de dados e da aplicação devem ser feitos de maneira concomitante?</summary>

O desenvolvimento concomitante garante que o banco de dados represente o contexto que a aplicação vai consumir e que a aplicação conheça as restrições de acesso. Isso evita problemas de integração e garante que a aplicação acesse os dados corretamente.

</details>

## Conteúdo

`⏱ 00:00`

A parte de desenvolvimento de aplicações e de banco de dados estão interligadas. Se conseguirmos ver os dois mundos juntos, podemos perceber que a fase de levantamento de requisitos é comum tanto ao desenvolvimento de banco de dados quanto ao desenvolvimento de aplicações.

### Fases de Desenvolvimento

O projeto segue uma série de etapas que ocorrem em paralelo:

1.  **Levantamento de Requisitos:** É a fase de comunicação com o cliente, onde se levantam e se analisam os dados necessários.
2.  **Projeto Conceitual:** O banco de dados passa por esta fase, que é o modelo de alto nível.
3.  **Análise Funcional do Sistema:** No mundo do desenvolvimento de software, esta análise define o que a aplicação vai precisar fornecer e o que ela deve fazer.
4.  **Especificação de Acesso:** Define quem pode acessar, o que pode ser acessado e qual é o caminho para que a aplicação acesse ou seja acessada por informações.

### A Relação entre Aplicação e Banco de Dados

A especificação de acesso é um ponto crucial de conexão.

> [!exemplo] A Especificação de Acesso
> A especificação de acesso deve ser verificada em relação ao projeto físico do SGBD. Ao restringir o acesso ou definir `views` para um determinado grupo de usuário que utilizará o SGBD, qualquer restrição imposta deve refletir na aplicação. A aplicação precisa conhecer essas restrições de acesso para ser desenvolvida de maneira correta.

É fundamental que as fases de desenvolvimento da aplicação e do banco de dados andem de maneira concorrente. Se essa fase não estiver andando de maneira concorrente, é preciso verificar no projeto físico e definir quais são as restrições.

A especificação de acesso está relacionada ao projeto físico porque a aplicação estará acessando os dados do SGBD. É necessário verificar as instruções e refletir isso na aplicação.

### Implementação e Testes

Após a definição dos requisitos e do projeto, o processo avança para a implementação.

#### Implementação do Banco de Dados (SGBD)

Nesta etapa, implementa-se o SGBD, o que significa definir o projeto físico e criar a parte de comandos `SQL`.

#### Implementação da Aplicação

Paralelamente, cria-se toda a estrutura para dar suporte à implementação da aplicação.

Uma vez que o banco de dados e a aplicação estiverem implementados, o processo avança para a validação e testes.

#### Validação e Testes

Nesta fase, verifica-se a aplicação e, simultaneamente, verifica-se o acesso dela ao banco de dados. É necessário testar todos os cenários possíveis, garantindo que a aplicação está realmente conseguindo acessar o SGBD.

Para contextualizar, o desenvolvimento de banco de dados e de aplicação é regido por uma premissa que envolve todas essas etapas.

`⏱ 04:20`

A premissa do nosso desenvolvimento de banco de dados e de aplicação é regida por uma diretriz relacionada ao minimundo e ao contexto de um mundo fechado. A análise funcional é fomentada pelas premissas do levantamento de requisitos.

A especificação de acesso define o **CRUD**. Esse CRUD deve ser consonante com as `queries` e `views` definidas no projeto.

### Regra 20/80 para Acessos ao Banco de Dados

Existe uma regra chamada 20/80 para acessos ao banco de dados:

| Porcentagem | Tipo de Ação/Acesso |
|---|---|
| 80% | Simples CRUD |
| 20% | Consultas mais complexas |

Também é nessa fase que se define a privacidade do usuário e dos dados.

Na parte de desenvolvimento de aplicações, define-se o CRUD para acesso aos dados e também os parâmetros de privacidade dos usuários.

### Projeto Físico e Implementação Concomitante

No projeto físico, já se conhece a aplicação e como ela se comporta. A implementação do banco de dados é baseada no que a aplicação espera.

Se o desenvolvimento do banco de dados e da aplicação são feitos de maneira concomitante, o banco de dados precisa representar o contexto que a aplicação vai consumir.

Nesse ponto, já se conhece a aplicação, todos os seus requisitos funcionais, as especificações de acesso e privacidade. Já se entende como a aplicação se comporta. Então, parte-se para a implementação do banco e da aplicação.

### Integração na Fase de Implementação

Na fase de implementação, um ponto importante é a integração. No teste, verifica-se se a aplicação está acessando com sucesso o banco de dados, e para isso é preciso uma integração bem feita.

### Classificação de Aplicações por Uso de Dados

As aplicações são classificadas de acordo com o uso dos seus dados. Elas têm abordagens distintas:

| Tipo de Processamento | Características |
|---|---|
| **Online Transaction Processing (OLTP)** | Alta performance para transações online. |
| **Online Analytical Processing (OLAP)** | Utiliza data warehouses para análise e tomada de decisão para negócios. |
| **Hybrid Transaction Analytical Processing (HTAP)** | Modelo híbrido que combina a performance de OLTP com a capacidade analítica de OLAP. |

### O Projeto de Desenvolvimento de Banco de Dados (Visão Geral)

Todo o projeto de desenvolvimento de banco de dados está refletido nesta figura. As figuras são tiradas do livro do Navate, que é o livro de referência.

> [!definicao] Minimundo
> O texto de Minimundo é o que se quer modelar.

A partir do Minimundo, tem-se a coleta de requisitos e análises. Dentro disso, há a parte de projeto conceitual, onde se define o modelo de entidade-relacionamento.

`⏱ 09:00`

e onde a gente vai definir o modelo de entidade relacionamento através do diagrama de entidade de relacionamento.

Em uma fase posterior, podemos observar uma distinção importante:

| Fase | Característica |
| :--- | :------------- |
| Conceitual | Independente do banco de dados (o modelo) |
| Posterior | Específico ao banco de dados (os dados em si) |

### Mapeamento do Modelo de Dados

Passada essa fase conceitual, entramos no **Data Model Mapping**.

> [!definicao] Data Model Mapping
> É o mapeamento do modelo de dados do alto nível para o específico, que é o relacional.

Aqui temos um esquema que reflete o que conversamos sobre o desenvolvimento da aplicação. Definidos os requisitos e a coleta das informações, seguimos as seguintes etapas:

-   Definimos os requisitos funcionais.
-   Realizamos a análise funcional da aplicação.
-   Temos a especificação de alto nível das transações que serão realizadas para acessar o banco de dados.

Tudo isso é de alto nível, sem necessidade de especificar o SGBD. A partir daqui, a especificação do SGBD já acontece.

### Desenvolvimento do Banco de Dados e Aplicação

Voltando para o nosso desenvolvimento de banco de dados, nessa parte, vamos especificar o modelo relacional como o modelo que será utilizado para a implementação do SGBD.

Relacionado a ele, está o design do programa de aplicação. Vamos definir a estrutura e todo o design que a nossa aplicação precisa ter.

> [!exemplo] Relação entre Entidade da Aplicação e Banco de Dados
> Se você acessa dados do seu SGBD, a `entity` da sua aplicação (por exemplo, dentro de um projeto Spring Boot com arquitetura MVC) precisa estar condizente com a estrutura que você vai encontrar dentro do banco de dados.
> Na hora de buscar as informações, elas precisam bater: os atributos e os nomes dos atributos têm que estar relacionados às entidades do banco de dados, dessa forma na aplicação.

### Design Físico do Banco de Dados

Em seguida, partimos para o design físico do banco de dados, onde vamos referir o esquema do SGBD. Isso está relacionado ao próprio SGBD em si, como se vamos utilizar o `MySQL` ou o `Postgres`. Aqui estão as particularidades relacionadas a cada SGBD.

Isso estará diretamente relacionado à parte de implementação das transações. Ao definir o SGBD, vamos criar o `driver` que será utilizado dentro da aplicação, ou a maneira de interagir com o banco de dados será influenciada pelo modelo físico.

Finalmente, finalizamos a aplicação do programa e todo o desenvolvimento do banco de dados.

## Relacionado

- [[modelagem-de-dados-projeto-conceitual-flexibilidade-e-transicao]]
- [[modelagem-de-dados-processo-e-fluxo-de-desenvolvimento]]
- [[modelagem-de-dados-requisitos-modelos-conceitual-e-logico]]
- [[modelagem-de-dados-projeto-conceitual-representacao-e-proposito]]
