---
titulo: "Jornada da Formação SQL Database Specialist"
tags: [banco-de-dados, sql, conceitos, fundamentos, estudo, dados, sistema]
data: 2026-09-13
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 11
conceitos: [SQL Database Specialist, SGBD, MySQL, Modelagem de Banco de Dados, SQL, Triggers, Indexação, Normalização]
---

# Jornada da Formação SQL Database Specialist

> [!resumo] Do que se trata
> Esta formação visa capacitar analistas de banco de dados com foco em MySQL, abordando fundamentos de SGBDs aplicáveis a diversos sistemas. O curso cobre desde a modelagem e construção de bancos de dados até a interpretação, extração e manutenção de dados usando SQL. Ele também explora técnicas avançadas como triggers, indexação, normalização, transações, concorrência, backup e recuperação de dados.

## Para lembrar

- **A teoria e os fundamentos dos SGBDs abordados na formação são agnósticos, permitindo que algoritmos e práticas sejam aplicados em diferentes SGBDs.**
- **Apesar de o SQL ter uma normativa, cada SGBD pode definir uma sintaxe específica, como a diferença entre MySQL e Postgres.**
- **SQL é uma linguagem de consulta utilizada para interagir e recuperar informações persistidas no banco de dados.**
- **Triggers (gatilhos) são mecanismos que possibilitam a automação de processos e ações dentro do banco de dados.**

## O que esta nota responde

- Qual é o objetivo principal da formação SQL Database Specialist?
- Quais são as principais habilidades que um aluno desenvolverá ao concluir a formação SQL Database Specialist?
- Como a formação aborda a manutenção e a segurança de bancos de dados?

## Conceitos

**SQL Database Specialist** · **SGBD** · **MySQL** · **Modelagem de Banco de Dados** · **SQL** · **Triggers** · **Indexação** · **Normalização**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Introdução, objetivos e capacidades da formação | ▪ |
| `03:40` | Papel DBA e estrutura dos módulos | ▪▪ |
| `07:20` | SQL dinâmico, otimização, segurança e logística | ▪▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **SQL** | Linguagem de consulta voltada para o banco de dados. |
| **Views** | Visões que exportamos para o usuário, representando de forma específica os dados persistidos, o que permite maior controle sobre o que é mostrado e oferece diversas vantagens. |
| **DDL (Data Definition Language)** | A linguagem de definição de dados, que permite definir o esquema em banco de dados e entender seu funcionamento. |
| **Triggers (Gatilhos)** | Possibilitam uma automação de processos e ações dentro do banco de dados. |
| **Queries Ad Hoc** | Queries isoladas que são executadas no banco de dados. Em um ambiente transacional real, raramente se lida com elas. |

## Pegadinhas

- A sintaxe SQL varia entre SGBDs, como MySQL e Postgres, apesar da normativa.
- Em ambiente transacional real, raramente se usa queries ad hoc; transações garantem segurança e reversão.

## Teste-se

<details><summary>Qual o foco principal da formação SQL Database Specialist?</summary>

A formação foca em capacitar o aluno a traçar o caminho de analista de banco de dados com foco no MySQL, mas com teoria agnóstica aplicável a outros SGBDs.

</details>

<details><summary>Quais são as três principais capacidades que o aluno desenvolverá após a formação?</summary>

O aluno será capaz de realizar modelagem e construção de banco de dados, interpretação e extração de dados usando SQL, e manutenção de bancos de dados existentes.

</details>

<details><summary>O que é a modelagem de dados e qual sua importância?</summary>

A modelagem de dados é o primeiro contato com um modelo conceitual, essencialmente teórica, que será aplicado em um script SQL. Ela é fundamental para construir um banco de dados enxuto, interessante e performático.

</details>

<details><summary>Por que a normalização é importante em banco de dados?</summary>

A normalização é crucial para ter um banco de dados performático. Ela implica em menor redundância dos dados e maior performance do SGBD.

</details>

<details><summary>O que são transações e por que são preferíveis a queries ad hoc em ambientes reais?</summary>

Transações são operações que garantem maior segurança e confiabilidade das ações no banco de dados. Elas permitem reverter situações de erro ou falha de forma mais fácil do que queries ad hoc (isoladas).

</details>

<details><summary>Onde os materiais e desafios de projeto da formação são disponibilizados e como devem ser entregues?</summary>

Todos os scripts e códigos SQL estão no GitHub. Os desafios de projeto, presentes em quase todos os módulos, devem ser entregues submetendo um link de repositório do GitHub para avaliação.

</details>

## Conteúdo

`⏱ 00:00`

Olá! Sejam muito bem-vindos à formação `SQL Database Specialist`. Meu nome é Juliana Mascarenhas e estarei com vocês durante todo o processo.

Este vídeo tem como objetivo explicar a jornada que nos aguarda, como a formação está estruturada e o que vocês verão. Meu foco aqui é nos resultados que vocês terão.

### Sobre a Formação

A partir desta formação, vocês serão capazes de traçar o caminho de **analista de banco de dados** com foco no `MySQL`.

Toda a teoria, fundamento e base dos **SGBDs** (Sistemas Gerenciadores de Banco de Dados) são voltados para um modelo agnóstico. Isso significa que algoritmos, práticas e outros temas que veremos podem ser aplicados em outros `SGBDs`.

> [!atenção] Diferenças de Sintaxe
> Apesar do `SQL` ter uma normativa que define seu comportamento e sintaxe, cada `SGBD` tem a liberdade de definir uma sintaxe específica. Assim, a sintaxe utilizada pelo `MySQL` no `SQL` será diferente da do `Postgres`.

### O que você será capaz de fazer

Após esta formação, vocês serão capazes de executar diversas tarefas:

-   **Modelagem e Construção de Banco de Dados**
    Vocês atuarão no perfil de designer de projetos de banco de dados, lidando com o cliente e realizando todo o desenvolvimento de um projeto conceitual. Isso inclui o levantamento de **requisitos funcionais e não funcionais**, que serão utilizados para fomentar a criação de um banco de dados.

    Para isso, é fundamental ter em mente como é feita a **modelagem conceitual** e a **modelagem de modelo relacional**, para que consigam construir o banco de dados de maneira mais assertiva. Vocês realizarão toda a parte de modelagem do projeto e a construção do banco de dados a partir dessa modelagem, resultando em um banco mais enxuto, interessante e performático.

-   **Interpretação e Extração de Dados**
    Vocês poderão lidar com ferramentas de interpretação e extração de dados, como o próprio `SQL`.

> [!definicao] SQL
> Linguagem de consulta voltada para o banco de dados.

    Toda a parte teórica e prática fundamentará o conhecimento para que possam alçar um voo autônomo, utilizando o `SQL` para recuperar informações persistidas no banco de dados. Vocês também se preocuparão em verificar o desempenho de métricas e outras informações relacionadas à saúde da empresa, se esse for o seu foco, através de técnicas de extração utilizando o `SQL`.

-   **Manutenção de Banco de Dados**
    Mais para frente, vocês lidarão com a manutenção de métodos e `procedures`. Provavelmente terão contato com bancos de dados já instituídos e implementados dentro de empresas. Será necessário entender o que foi feito, quais são as estruturas implementadas e dar manutenção a elas, através de `procedures`, `functions` e outros objetos armazenados no banco de dados.

`⏱ 03:40`

E muitas vezes, se você não for partir para um ambiente de análise de dados voltados para uma nova área, a de cientista de dados, você provavelmente fará parte da equipe do **DBA**, que é o administrador de banco de dados.

### Módulo Introdutório

A formação começa com o módulo introdutório, onde vocês terão o primeiro contato com o mundo de `SGBDs` e de banco de dados. Se você já possui toda a base de conhecimento, não precisará assistir tudo de novo. Você poderá realizar os questionários e, sendo bem-sucedido, concluir as aulas e partir para o próximo módulo.

O módulo introdutório apresentará uma breve contextualização histórica de `SGBDs` no mercado, como foi feita a transição, por que deixamos de utilizar o gerenciamento de dados dentro das aplicações e quais são as perspectivas futuras. Em seguida, mergulharão no mundo de `SGBDs` e entenderão seu funcionamento, suas vantagens e quando não utilizá-los.

### Modelagem de Dados

A **modelagem de dados** é o primeiro contato com um modelo conceitual, que será aplicado posteriormente em um script `SQL`. Em seguida, será abordada a arquitetura de banco de dados, destrinchando o funcionamento de um `SGBD`.

Vocês terão todo o fundamento teórico, pois a modelagem de dados é essencialmente teórica. Serão utilizadas ferramentas de modelagem de dados, com diversas opções apresentadas. Vocês entenderão o modelo de entidade e relacionamento, suas entidades, atributos e relacionamentos, e os conceitos por trás desse contexto.

Posteriormente, será abordado o aprimoramento desse modelo, impulsionado pela evolução das técnicas de programação e pela orientação a objetos.

> [!exemplo] Desafio de Modelagem Conceitual
> Em um momento posterior, vocês realizarão um desafio, criando uma modelagem conceitual a partir de cenários específicos, como contextos de universidade e e-commerce.

### Modelo Relacional e SQL

No próximo módulo, vocês serão capazes de explorar o modelo relacional, fazer o mapeamento do modelo conceitual para o relacional e aprofundar-se em `SQL`. Serão abordados os primeiros passos, a exploração de *queries* e todas as suas possibilidades, incluindo a criação de *queries* com funções e cláusulas de agrupamento.

Serão apresentadas diversas técnicas básicas de `SQL` para recuperar informações, até o ponto de lidar com agrupamento de registros e tabelas utilizando o `Joint Statement`. Assim como no módulo anterior, haverá dois desafios de projeto, voltados para um projeto lógico de banco de dados.

### Técnicas Avançadas em Banco de Dados

No módulo de Técnicas Avançadas em Banco de Dados, vocês terão contato com `Views`.

> [!definicao] Views
> Visões que exportamos para o usuário, representando de forma específica os dados persistidos, o que permite maior controle sobre o que é mostrado e oferece diversas vantagens.

Será explorada a `DDL`.

> [!definicao] DDL (Data Definition Language)
> A linguagem de definição de dados, que permite definir o esquema em banco de dados e entender seu funcionamento.

Posteriormente, será abordada a lógica de programação voltada para o `SQL` dinâmico, permitindo a inclusão de estruturas condicionais e de repetição.

`⏱ 07:20`

Depois entraremos na parte de lógica de programação voltada para o SQL dinâmico. Aqui a gente consegue colocar estruturas condicionais e de repetição dentro da linguagem SQL, trazendo uma maior versatilidade e flexibilidade para as suas operações e instruções do dia a dia.

### Triggers
Feito isso, vamos entender como acontece e como podemos criar as **triggers**, os gatilhos que possibilitam uma automação de processos e ações dentro do banco de dados.

> [!definicao] Triggers (Gatilhos)
> Possibilitam uma automação de processos e ações dentro do banco de dados.

### Indexação
E por fim, abordaremos os fundamentos de indexação em SGBDs, onde você vai entender quando deve ou não criar índices atribuídos a determinados atributos, e como isso pode impactar na sua performance de recuperação de dados.

### Normalização
E nada mais importante do que a **normalização** em banco de dados, para que você consiga ter um banco performático. É preciso que ele seja normalizado. Em que isso implica? Em uma maior redundância dos dados e em uma maior performance do SGBD. Vocês vão entender bem o que significa isso.

### Módulo Avançado: Transações e Concorrência
Da mesma forma, teremos também desafios de projetos. Agora, entramos no módulo mais avançado ainda, quando tratamos de **transações**.

Raramente, em um mundo real, em um ambiente transacional, você vai lidar com **queries ad hoc**, ou seja, você vai executar queries isoladas no seu banco de dados.

> [!definicao] Queries Ad Hoc
> Queries isoladas que são executadas no banco de dados. Em um ambiente transacional real, raramente se lida com elas.

É preciso que haja uma maior segurança e que haja também maior confiabilidade das suas ações, dado que, se houver algum erro ou falha, conseguimos reverter toda a situação de uma maneira muito mais fácil do que se fosse uma query ad hoc. Sendo assim, é intuitivo dizer que precisamos conversar sobre o **controle de concorrência** e também sobre **backup e recuperação de banco de dados**.

### Backup e Recuperação de Banco de Dados
Uma vez que podem haver falhas nesse processo ou em qualquer outro momento de operação de um SGBD, é preciso que tenhamos um primeiro contato com a realização de backup de todos os dados persistidos. Dessa maneira, se perdermos nossas informações por algum motivo, não há desespero. Temos um backup para que possamos recuperar toda a informação. Vocês terão o contato e verificarão como isso acontece na prática, utilizando o `MySQL`.

### Informações Importantes do Curso
O último recado que vale a pena deixar para vocês é o seguinte:

> [!atenção] Materiais e Desafios do Curso
> - Todo script e código `SQL` que será disponibilizado ao longo dos módulos desta formação está disponível no `GitHub`.
> - Com exceção do primeiro módulo (que é uma contextualização e o primeiro contato com o mundo de SGBD), todos os demais possuem desafios de projetos.
> - Esses desafios de projetos precisam ser entregues a partir de um link de repositório do `GitHub`.
> - Seja um esquema relacional, um modelo conceitual ou um script `SQL` que você precise entregar, você criará um repositório no `GitHub` e submeterá o link para avaliação, relacionado a cada desafio de projeto existente nos módulos desta formação.

### Conclusão
Muito bem, vocês viram, então, o overview do que aguarda vocês, todo esse processo, essa jornada que vocês vão iniciar. Espero que seja bastante proveitoso e que vocês possam tirar o máximo de todo o conteúdo passado. Até!

## Relacionado

- [[../../Introdução à Programação e Pensamento Computacional/Pensamento computacional/visao-geral-da-carreira-em-ti-da-rede-a-ciencia-de-dados-e-programacao]]
- [[../../Bancos de Dados/_Índice Bancos de Dados]]
- [[../../Bancos de Dados/Conceitos Básicos/00 - Índice]]
- [[../../Bancos de Dados/SGBD - Rodrigo Schaeffer/SGBD]]
