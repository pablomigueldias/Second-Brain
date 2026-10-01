---
titulo: "Modelagem de Dados: Projeto Lógico, Físico e Mapeamento Entidade-Relacionamento"
tags: [modelagem-de-dados, sgbd, banco-de-dados, fundamentos, sql, conceitos, engenharia-de-software]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 18
conceitos: [Projeto Lógico, Projeto Físico, Modelo Conceitual, SGBD, Modelo Relacional, Mapeamento Entidade-Relacionamento, Entidade Fraca, Cardinalidade]
---

# Modelagem de Dados: Projeto Lógico, Físico e Mapeamento Entidade-Relacionamento

> [!resumo] Do que se trata
> Esta aula detalha as fases de projeto lógico e físico na modelagem de dados, explicando como o modelo lógico descreve o conceitual com base na estrutura do SGBD escolhido. Ela diferencia o projeto lógico, que é dependente do SGBD, do projeto conceitual, que é independente, e aborda o fluxo de mapeamento do modelo Entidade-Relacionamento para o relacional. Por fim, a aula descreve o ciclo de vida completo do desenvolvimento de banco de dados, desde a coleta de requisitos até a implementação física.

## Para lembrar

- **O modelo lógico é a descrição do modelo conceitual, organizando os dados com base na estrutura definida pelo Sistema Gerenciador de Banco de Dados (SGBD) escolhido.**
- **A estrutura do modelo lógico varia conforme o SGBD: relacional para MySQL/Postgres, Wide Column para Cassandra, e baseado em documentos para MongoDB.**
- **O Projeto Lógico depende do modelo de banco de dados e define a organização dos dados em uma estrutura específica, enquanto o Projeto Conceitual é independente do modelo e foca nos relacionamentos e entidades.**
- **O mapeamento do projeto conceitual para o projeto lógico resulta no esquema de um banco de dados.**
- **Um relacionamento M para N (muitos para muitos) entre entidades no modelo conceitual gera uma tabela intermediária no modelo relacional, com chaves estrangeiras que compõem sua chave primária.**

## O que esta nota responde

- Qual a diferença fundamental entre o projeto lógico e o projeto conceitual na modelagem de dados?
- Como a escolha de um SGBD específico afeta a estrutura do modelo lógico de um banco de dados?
- Como um relacionamento de muitos para muitos (M para N) é mapeado do modelo Entidade-Relacionamento para o modelo relacional?

## Conceitos

**Projeto Lógico** · **Projeto Físico** · **Modelo Conceitual** · **SGBD** · **Modelo Relacional** · **Mapeamento Entidade-Relacionamento** · **Entidade Fraca** · **Cardinalidade**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Projeto lógico, físico e conceitual | ▪▪ |
| `04:20` | Percurso e fluxo do projeto lógico | ▪▪ |
| `08:40` | Mapeamento ER para Relacional | ▪▪▪ |
| `13:20` | Projeto físico e ciclo de vida | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **SQLite** | Uma biblioteca em C, utilizada massivamente em aplicações mobile. |
| **Entidade Fraca** | Basicamente, ela depende de uma outra entidade para existir. |

## Pegadinhas

- Projeto Lógico depende do modelo de banco de dados, enquanto o Projeto Conceitual é independente do modelo.
- O esquema conceitual é independente de um SGBD específico, mas depende do modelo do SGBD (ex: relacional).
- O modelo Entidade-Relacionamento não possui chaves primárias ou estrangeiras, mas o modelo relacional sim.
- A implementação final do fluxo de modelagem de banco de dados resulta no esquema físico, não no esquema lógico.

## Teste-se

<details><summary>Qual a principal diferença entre Projeto Lógico e Projeto Conceitual?</summary>

A principal diferença reside na dependência do SGBD. O Projeto Lógico depende do modelo de banco de dados, enquanto o Projeto Conceitual é independente do modelo, focando apenas nos relacionamentos de objetos.

</details>

<details><summary>Quais são os três principais modelos de banco de dados mencionados e seus SGBDs correspondentes?</summary>

Os modelos são relacional (MySQL, Postgres), Wide Column (Cassandra) e baseado em documentos (MongoDB). Cada SGBD possui uma estrutura específica que o projeto lógico deve refletir.

</details>

<details><summary>Quais são os 'Pontos de Atenção' ao mapear um modelo Entidade-Relacionamento para o modelo relacional?</summary>

Deve-se verificar o tipo de entidade (ex: fraca), o tipo de relacionamento (binário ou de grau mais alto), o tipo de cardinalidade e se os atributos são multivalorados.

</details>

<details><summary>O que o projeto físico de um banco de dados define?</summary>

O projeto físico descreve o modelo lógico do banco de dados e define como ele será implementado. Ele é diretamente ligado ao SGBD e define parâmetros como estrutura, utilização de índice, organização de arquivos e caching.

</details>

<details><summary>Qual é a primeira fase do fluxo de modelagem de banco de dados e o que ela envolve?</summary>

A primeira fase é o Projeto Conceitual, que começa com a coleta e análise dos requisitos funcionais e não funcionais. A narrativa definida a partir desses requisitos subsidia o esquema conceitual.

</details>

<details><summary>Quem é o responsável pela etapa de 'Validação' no ciclo de vida do desenvolvimento de banco de dados?</summary>

A equipe de DBA (Database Administrator) é responsável pela validação. Eles verificam todos os requisitos do SGBD, garantindo que ele está se comportando da maneira que deveria.

</details>

## Conteúdo

`⏱ 00:00`

### Projeto Lógico e Projeto Físico

Continuando, vamos falar sobre o projeto lógico e o projeto físico.

O intuito dessa parte é justamente a modelagem. A modelagem é conceitual e a modelagem lógica é a parte do projeto físico, que ficará para outra ocasião, quando falarmos de SQL.

Eu vou introduzir toda a parte de SQL para que possamos pegar um determinado modelo e, a partir dele, criar um mapeamento e definir o esquema dentro do banco de dados. É necessário fazer toda a manipulação do banco para poder representar o modelo lá dentro.

### O que é o Modelo Lógico?

O modelo lógico é a descrição do modelo conceitual, onde há a organização dos dados baseada em determinada estrutura. Essa estrutura será definida pelo Sistema Gerenciador de Banco de Dados (SGBD) escolhido.

A estrutura varia conforme o SGBD:

*   **MySQL ou Postgres:** O modelo será relacional.
*   **Cassandra:** O modelo é *Wide Column*.
*   **MongoDB:** O modelo é baseado em documentos.

Cada SGBD possui uma estrutura específica, e o projeto lógico refletirá justamente essa estrutura.

Como nosso foco é banco de dados relacional, é aqui que pararemos. A parte de como faríamos um projeto lógico para um modelo NoSQL fica para outro cenário.

### Diferença entre Projeto Lógico e Projeto Conceitual

A grande diferença está na dependência do SGBD.

*   **Projeto Lógico:** Depende do modelo de banco de dados. Ele define a organização dos dados que está baseada em uma estrutura específica.
*   **Projeto Conceitual:** É independente do modelo. Ele foca apenas em definir o relacionamento dos objetos, estruturando efetivamente esses relacionamentos e entidades.

No caso de um modelo conceitual para um modelo relacional, temos as entidades e as tabelas. É esse tipo de estrutura e informação que fornece a organização dos dados.

### O Fluxo de Mapeamento

O processo de modelagem envolve várias etapas:

1.  **Projeto de Alto Nível:** É a fase em que você consegue falar com o cliente, definir todos os requisitos e verificar se as consultas serão solucionadas a partir do modelo. Nesta fase, definimos todos os requisitos funcionais e não funcionais.
2.  **Mapeamento:** A partir do esquema gerado nesta fase, é necessário realizar o mapeamento.
3.  **Projeto Físico:** Este é o mapeamento para o projeto físico, que será feito depois.

O mapeamento do projeto conceitual para o projeto lógico resulta no esquema de um banco de dados.

### Escolhendo a Estrutura do Projeto Lógico

Ao definir o projeto lógico, é preciso considerar vários fatores. Por exemplo:

*   Se o modelo relacional não se adequar bem ao projeto, deve-se considerar outras opções.
*   Se for necessário um ambiente distribuído.
*   Se o sistema for mobile.
*   Se for necessária alta performance.

`⏱ 04:20`

A escolha da estrutura a ser utilizada depende de algumas questões relacionadas ao ciclo de vida do projeto. Os **requisitos**, definidos no seu **projeto conceitual**, são os que vão te ajudar a definir o tipo de estrutura.

> [!definicao] SQLite
> Uma biblioteca em C, utilizada massivamente em aplicações mobile.

Nosso foco aqui é em relacional.

### O Percurso do Projeto Lógico

Qual é o percurso durante esse projeto lógico?
1.  Criamos o **esquema lógico**.
2.  A partir desse esquema lógico, que é definido nesta segunda fase do projeto de banco de dados (o projeto lógico, modelagem estrutural do nosso contexto), vamos instalar e configurar o **SGBD**.
3.  A escolha do SGBD já é parte do **projeto físico**. Uma vez instalado e configurado corretamente o SGBD, você parte para a criação do esquema dentro do banco de dados, dentro do SGBD relacionado ao seu banco de dados.

Seja `MySQL` ou `Cassandra`, o SGBD determinará as características que o seu modelo terá. As características do modelo do SGBD vão influenciar o seu modelo. Se estou usando o **modelo relacional**, ele vai influenciar o meu projeto lógico.

Mesmo o **esquema conceitual** sendo independente de um SGBD específico (ele pode ser de qualquer tipo), ele está sendo modelado para ser utilizado em qualquer banco de dados relacional, seja `Postgres`, `MySQL`, `Oracle`, enfim. Apesar de ser independente, o tipo de banco de dados e suas características vão influenciar na sua construção. Apesar de não depender do SGBD, ele depende do modelo do SGBD.

### Fluxo do Projeto de Banco de Dados

Qual é o fluxo aqui agora?
1.  **Coleta e Análise:** É a primeira fase, onde temos o projeto conceitual.
2.  **Esquema Conceitual:** Partimos para o esquema conceitual, onde temos os conceitos de alto nível e definimos o design do nosso banco de dados.
3.  **Mapeamento para o Modelo Relacional:** A partir daqui, faremos um mapeamento, especificando nosso projeto. Estou trazendo algo mais generalista, de alto nível, para algo específico relacionado ao modelo relacional. Vou mapear o projeto conceitual para o modelo relacional, definindo o esquema lógico.

### Exemplo de Mapeamento

Vamos entender o que isso quer dizer, não de maneira detalhista, mas de maneira geral.

> [!exemplo] Mapeamento de Entidade-Relacionamento para o Modelo Relacional
> O projeto conceitual da minha companhia, da minha empresa, que tem empregado, dependente, departamento de projeto como **entidades**, será mapeado e modelado para um modelo relacional, onde temos as tabelas, as entidades relacionadas, as tabelas mesmo relacionadas às entidades.
> >
> Por exemplo: "Departamento de localização, trabalha em". "Trabalha em" não é uma entidade, é um **relacionamento**. Isso é uma característica de mapeamento do modelo Entidade-Relacionamento para o relacional.
> >
> Considere "Empregado trabalha em Projeto".
> Um ou mais empregados podem trabalhar em um ou mais projetos. E um ou mais projetos podem ter um ou mais empregados. Então, o relacionamento é M para N (muitos para muitos). Isso gera uma entidade, tanto que ela tem até um próprio atributo.

`⏱ 08:40`

A gente vai comentar um pouquinho melhor sobre isso lá na frente.

Aqui, eu tenho mapeado por um modelo relacional a entidade `Empregado` com todos os seus atributos. Eu tenho a entidade `Departamento` com os seus atributos relacionados.

Também, eu tenho a entidade `Departamento de Localização`. Provavelmente, foi uma modificação dentro do meu esquema onde eu percebi que precisava de uma entidade definida para `Localizações`. Ah, sim, aqui, `Localizações`. Isso é um tipo complexo de atributo que acabou gerando uma entidade. Vou entrar em detalhes sobre isso depois.

Muito bem. E aí eu tenho o `Projeto` também, que é essa entidade com seus atributos, `TrabalhaEm`, que eu já comentei, e `Dependente`. Eu tenho essa quantidade de entidades do meu modelo relacional. Eu acabei deixando aqui maior para que vocês pudessem ver. Já falei sobre as entidades e o mapeamento que aconteceu, e vou entrar em maiores detalhes mais para frente.

Aqui é só um mapeamento para que vocês possam ver o que está referenciando. Porque, apesar do modelo Entidade-Relacionamento não possuir `primary key` (chave primária) ou `foreign key` (chave estrangeira), o modelo relacional possui.

> [!exemplo] Chaves Estrangeiras no Modelo Relacional
> No modelo relacional, `Dependente` tem um determinado número que está associado a um número específico de `Empregado`.
>
> A entidade `TrabalhaEm` está relacionada ao `SSN` de `Empregado` e ao `PNO` do `Projeto`. `TrabalhaEm` tem duas chaves estrangeiras que, na verdade, compõem sua chave primária. O atributo `Horas` está relacionado a esses dois outros atributos.

### Mapeamento Entidade-Relacionamento para Relacional

Como funciona esse mapeamento da entidade de relacionamento para o relacional? Eu tenho alguns pontos de atenção para falar com vocês.

Se a gente for pensar nas entidades, temos que pensar no seguinte: qual o tipo de entidade?

> [!definicao] Entidade Fraca
> Basicamente, ela depende de uma outra entidade para existir.

Então, eu preciso entender qual o tipo de entidade que está no meu modelo conceitual. Eu preciso entender os meus relacionamentos: eles são binários ou são de um grau mais alto? Qual o tipo de cardinalidade? Meus atributos são multivalorados?

Tudo isso que estou comentando aqui, a gente vai ver em detalhes mais para frente.

> [!atenção] Pontos de Atenção no Mapeamento
> Para mapear corretamente para o modelo relacional, verifique no seu projeto conceitual:
> - Qual o tipo de entidade (ex: **entidade fraca**).
> - O tipo de relacionamento (binário ou de grau mais alto).
> - O tipo de cardinalidade.
> - Se os atributos são multivalorados.

### Restrições e Integridade

Nós também temos uma outra questão, que são as restrições e integridade.

No nosso modelo de alto nível, a gente não consegue representar muito bem as restrições. Mas, a partir do *merge* da narrativa com o esquema, a gente consegue definir as restrições e também restrições de integridade no sistema.

O projeto físico, na verdade, vai descrever o modelo lógico do meu banco de dados. Ele vai definir como ele vai ser implementado. Na terceira etapa do nosso projeto, estamos utilizando a modelagem física, que resultará em um esquema físico do banco de dados. Este esquema descreve o modelo lógico e define sua implementação.

`⏱ 13:20`

modelo lógico. Na terceira etapa do nosso projeto, estamos utilizando a parte de modelagem física. Vamos resultar em um esquema físico do banco de dados, e ele, na verdade, descreve o modelo lógico do meu banco de dados e define como ele será implementado.

Ele vai depender do meu modelo e do meu banco de dados, ou seja, do meu **SGBD** que eu estiver utilizando. Ele é diretamente ligado ao SGBD e vai definir diversos parâmetros físicos, como:

*   Estrutura;
*   Utilização de índice;
*   Organização e caminhamento de arquivos para conseguir acessar a informação de maneira mais rápida;
*   Definindo o *caching*, por exemplo.

Também envolve a segurança do sistema e os requisitos de performance.

> [!exemplo] Parâmetros e Situações do Projeto Físico
> Alguns exemplos de parâmetros que englobamos no projeto físico do banco de dados são:
> *   Alocação de memória;
> *   Particionamento de tabelas.

Apesar de a alocação em memória ser realizada pelo sistema operacional, como é uma parte diretamente ligada à performance do banco de dados, o SGBD também consegue gerenciar essa parte.

### Fluxo de Modelagem de Banco de Dados

Dado tudo o que conversamos, desde o projeto conceitual, o projeto lógico e agora o projeto físico, o fluxo é o seguinte:

1.  **Projeto Conceitual:** Começa com a coleta e a análise dos requisitos funcionais e não funcionais.
2.  **Esquema Conceitual:** A narrativa definida a partir dos requisitos subsidia o esquema conceitual, que é o diagrama que modela o contexto.
3.  **Modelo Lógico:** O esquema conceitual, por sua vez, é a base do modelo lógico. Criamos um mapeamento entre os dois modelos. O modelo lógico está diretamente ligado à estrutura de um determinado modelo de banco de dados, e essa estrutura define o comportamento do sistema.
4.  **Projeto Físico/Implementação:** A partir daqui, temos a implementação. Embora o que está aqui seja o esquema lógico, na verdade, seria o esquema físico. Essa parte é descrita em `SQL`. Eu descrevo meu esquema lógico a partir de uma série de comandos em `SQL` que vão implementar meu esquema físico.

### Ciclo de Vida do Desenvolvimento de Banco de Dados

O esquema físico é o que cabe a nós, na parte de projeto de banco de dados e desenvolvimento de banco de dados, e vai até o esquema lógico implementado.

O ciclo completo inclui etapas adicionais que podem ser feitas pela equipe do DBA (Database Administrator) ou não:

| Etapa | Responsável | Descrição |
| :--- | :--- | :--- |
| **Desenvolvimento** | Equipe de Banco de Dados | Vai desde o projeto até a implementação do esquema lógico. |
| **Validação** | Equipe DBA | Verifica todos os requisitos do SGBD, garantindo que ele está se comportando da maneira que deveria. |
| **Produção** | Equipe de TI | O sistema passa em todos os testes e é colocado em produção. |
| **Uso** | Usuários/Aplicações | O sistema é utilizado pelas APIs, pelas aplicações e pelas interfaces de gráfica de usuário. |
| **Manutenção** | Equipe de Banco de Dados | A partir daqui, ocorre a manutenção do banco de dados. |

## Relacionado

- [[sgbd-arquitetura-de-tres-esquemas-e-isolamento]]
- [[modelagem-de-dados-requisitos-modelos-conceitual-e-logico]]
- [[modelagem-de-dados-processo-e-fluxo-de-desenvolvimento]]
- [[modelagem-de-dados-etapas-caracteristicas-do-sgbd-e-conceito-de-mundo-fechado]]
