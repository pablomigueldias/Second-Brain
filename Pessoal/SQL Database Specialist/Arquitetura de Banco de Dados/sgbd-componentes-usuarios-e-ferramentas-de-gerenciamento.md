---
titulo: "SGBD: Componentes, Usuários e Ferramentas de Gerenciamento"
tags: [sgbd, banco-de-dados, conceitos, organizacao, otimizacao, ferramentas, sistema]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 14
conceitos: [SGBD (Sistema Gerenciador de Banco de Dados), Software modularizado, Runtime Database Processor, Data Dictionary System, DBA Staff, Otimização de Query, DML (Data Manipulation Language), Parametric Users]
---

# SGBD: Componentes, Usuários e Ferramentas de Gerenciamento

> [!resumo] Do que se trata
> Esta aula detalha a composição interna de um SGBD, abordando seus componentes robustos como bancos de dados armazenados e o processador de tempo real. Ela explora os diferentes tipos de usuários, incluindo DBA staff, usuários casuais, desenvolvedores e usuários paramétricos, descrevendo seus fluxos de interação com o sistema. Além disso, a aula apresenta diversas utilidades e ferramentas essenciais para o gerenciamento de dados, como otimização de query, backup, loading e o sistema de dicionário de dados.

## Para lembrar

- **O SGBD (Sistema Gerenciador de Banco de Dados) é um software modularizado, composto por outros programas que o auxiliam a entregar seu objetivo final: o gerenciamento de dados.**
- **Os `parametric users` são os usuários mais simples e utilizam `Complete Transactions` diretamente, que chegam ao `Runtime Database Processor` para processar comandos.**
- **A otimização de query envolve a reordenação de operações para tornar a requisição mais eficiente, permitindo eliminar redundâncias e gerando um arquivo `.exe` com o objetivo de ganhar performance.**
- **A DML (Data Manipulation Language) é extraída pelo pré-compilador da linguagem de programação para ser compilada separadamente e, então, processada pelo `runtime database processor`.**
- **O Data Dictionary System é um componente que armazena informações de decisão de design, padrão de utilização e descrição das aplicações, relacionadas ao projeto de banco de dados.**

## O que esta nota responde

- Quais são os principais componentes internos de um SGBD e suas funções?
- Como os diferentes tipos de usuários, como desenvolvedores e usuários paramétricos, interagem com o SGBD?
- Quais são as principais utilidades e ferramentas de gerenciamento de dados oferecidas por um SGBD?

## Conceitos

**SGBD (Sistema Gerenciador de Banco de Dados)** · **Software modularizado** · **Runtime Database Processor** · **Data Dictionary System** · **DBA Staff** · **Otimização de Query** · **DML (Data Manipulation Language)** · **Parametric Users**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | SGBD: componentes e tipos de usuários | ▪▪ |
| `04:20` | Usuários, DDL, DML e gerenciamento de dados | ▪▪ |
| `09:00` | Ferramentas e utilidades de gerenciamento SGBD | ▪▪ |
| `13:40` | Ferramentas de design de SGBD | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **SGBD (Sistema Gerenciador de Banco de Dados)** | É um software modularizado, composto por outros programas que o auxiliam a entregar seu objetivo final: o gerenciamento de dados. |
| **DDL (Data Definition Language)** | Linguagem utilizada para definir a estrutura de um banco de dados, como esquemas, catálogos e metadados. |
| **Storage Data Manager** | Componente responsável por armazenar informações sobre disco e memória, mesmo com o sistema operacional realizando cache e bufferização. Suas características estão diretamente ligadas à performance. |
| **Data Dictionary System** | É um componente que armazena informações de decisão de design, padrão de utilização e descrição das aplicações. São informações extras, mas que estão relacionadas ao projeto de banco de dados e que podem fazer a diferença em uma futura modelagem ou modificação do seu banco. |

## Teste-se

<details><summary>Qual o objetivo final de um SGBD?</summary>

O objetivo final de um SGBD é o gerenciamento de dados, sendo um software modularizado composto por outros programas que o auxiliam nessa tarefa.

</details>

<details><summary>Quais são os quatro tipos de usuários de um SGBD mencionados na aula?</summary>

Os quatro tipos de usuários são: a equipe do DBA, usuários casuais, desenvolvedores (programadores de aplicação) e parametric users (ou naive).

</details>

<details><summary>Qual a função do Runtime Database Processor?</summary>

O Runtime Database Processor é responsável por processar todos os comandos e requisições que chegam ao SGBD, incluindo transações compiladas, queries e comandos privilegiados.

</details>

<details><summary>O que é a DDL e para que ela é utilizada?</summary>

DDL (Data Definition Language) é a linguagem utilizada para definir a estrutura de um banco de dados, como esquemas, catálogos e metadados, sendo usada pelo DBA para criar a estrutura do banco.

</details>

<details><summary>Como a otimização de query contribui para a performance?</summary>

A otimização de query contribui para a performance reordenando operações para tornar a requisição mais eficiente e eliminando redundâncias, gerando um arquivo executável para ganho de performance.

</details>

<details><summary>Por que o SGBD possui seus próprios mecanismos de bufferização e caching?</summary>

O SGBD possui seus próprios mecanismos de bufferização e caching porque essas características influenciam diretamente no tempo de resposta ao usuário e na performance geral, mesmo que o sistema operacional já realize cache e bufferização.

</details>

## Conteúdo

`⏱ 00:00`

Nosso tópico agora é sobre ambientes de SGBD. Vamos procurar entender um pouco melhor como um SGBD é composto.

Se olharmos um pouco mais de perto, percebemos que o **SGBD** (Sistema Gerenciador de Banco de Dados) é um software modularizado.

> [!definicao] SGBD (Sistema Gerenciador de Banco de Dados)
> É um software modularizado, composto por outros programas que o auxiliam a entregar seu objetivo final: o gerenciamento de dados.

Essa figura foi retirada do Navathe, como já comentado. Estou com a versão PDF em inglês e estou pegando essas informações. Nosso livro-texto, nosso livro-guia, é realmente o livro do Navathe, que está nas referências.

Vamos analisar essa parte, que é relacionada aos usuários e ao próprio SGBD.

### Componentes Internos do SGBD

Vamos olhar o SGBD primeiro. Nesta parte maior, neste componente mais robusto, temos:

-   **Bancos de dados armazenados**: É o banco de dados propriamente dito, as instâncias. A persistência dos dados ocorre nesse componente.
-   `Runtime Database Processor`: Um processador de tempo real do banco de dados que processa todos os comandos que chegam a ele.
-   Catálogo do sistema (`Data Dictionary`): Um componente separado que será abordado posteriormente, e é interessante entender por que ele existe.
-   Subsistema de controle: Inclui controle de concorrência, backup e recuperação.
-   Gerenciador de armazenamento de dados.

Temos, então, alguns componentes que acabam compondo um SGBD, cada um com sua função. Restringindo a função de cada um, conseguimos ter maior controle.

### Tipos de Usuários e Seus Fluxos

Vamos analisar um pouco melhor como está disposta a parte do usuário. Temos:

-   A equipe do DBA
-   Usuários casuais
-   Desenvolvedores (que são os programadores de aplicação)
-   `Parametric users` (que são os `naive`)

> [!exemplo] Fluxo dos `Parametric Users`
> Os `parametric users` são os usuários mais simples. Eles utilizam `Complete Transactions` diretamente.
> O fluxo de dados para eles, a partir dessas transações compiladas, chega até o `Runtime Database Processor` para processar e acessar os comandos associados àquela transação.

> [!exemplo] Fluxo dos Desenvolvedores (Programadores de Aplicação)
> Os desenvolvedores pegam um programa específico escrito em alguma linguagem (`Java`, `C`, `Python`).
> O processo envolve:
> 1.  Pré-compilação desse programa, pois o `SQL` está embutido dentro de uma linguagem de programação.
> 2.  Compilação da aplicação.
> 3.  Passagem para um `DML compiler`, onde ocorre a compilação da `DML` (a *query* relacionada à aplicação).
> 4.  Compilação das transações.
> 5.  Direcionamento para o processador de banco de dados em tempo real.

`⏱ 04:20`

eu sou direcionada para o processador de banco de dados em tempo real.

Agora, em relação aos **usuários casuais**, nós temos a parte de interação via query. Já falamos um pouco sobre esses usuários: eles são pontuais e com contextos distintos.

Essas queries serão compiladas e, se necessário, otimizadas. O compilador verificará se existe alguma maneira de reordenar aquela ação para otimizá-la. Uma vez compilada, a query é direcionada para [inaudível] esse processo.

### DBA Staff

A **DBA Staff** tem acesso a comandos privilegiados e a `DDL Statements`. O comando SQL relacionado às `DDL Statements` possui um compilador separado.

Esse compilador de `DDL` gera informações do programa objeto para definir esquemas, o catálogo e outras informações de metadados. Os comandos privilegiados são diretamente executados pelo `runtime database processor`.

A ideia dessa estrutura é definir bem o papel de cada componente. O ambiente do banco de dados, na parte inferior, é composto pelo SGBD e seus módulos internos, onde cada um possui sua função.

> [!definicao] DDL (Data Definition Language)
> Linguagem utilizada para definir a estrutura de um banco de dados, como esquemas, catálogos e metadados.

A `DDL` é usada para definir um esquema. Quando o DBA cria um banco de dados, ele define a estrutura desse banco de dados através do esquema. Para criar esse esquema, é preciso utilizar a **DDL** (Data Definition Language). A partir daí, é possível inserir informações sobre os módulos e esquemas dentro desse componente, onde o banco de dados está armazenado.

### Otimização de Query

O `case reuses` (acesso ocasional) está relacionado à otimização de query.

> [!exemplo] Otimização de Query
> A otimização de query envolve a reordenação de operações para tornar a requisição mais eficiente.
> Além da reordenação, ela permite eliminar redundâncias.
> O processo gera um arquivo `.exe` com o objetivo de ganhar performance.

Esse tipo de análise é realizado.

### DML e Processamento de Transações

No pré-compilador, a linguagem de programação extrai a **DML** (Data Manipulation Language) para que ela seja compilada separadamente e, então, processada pelo `runtime database processor`.

As **Candidate Transactions** são utilizadas pelos **Parametric Users** (ou Naive Users) e são diretamente processadas pelo `Runtime Database Processor`. Comandos privilegiados, queries e Candidate Transactions — todas as requisições são processadas pelo `Runtime Database Processor`. Este componente processa todas as requisições direcionadas ao banco de dados.

### Gerenciamento de Dados

> [!definicao] Storage Data Manager
> Componente responsável por armazenar informações sobre disco e memória, mesmo com o sistema operacional realizando cache e bufferização. Suas características estão diretamente ligadas à performance.

O **Storage Data Manager** (gerente de armazenamento de dados) possui informações tanto sobre disco quanto sobre memória. Essas informações são armazenadas dentro desse componente. Apesar de o sistema operacional já realizar cache e bufferização, essas duas características estão diretamente ligadas à performance.

`⏱ 09:00`

essas duas características estão diretamente ligadas à performance do SGBD. Consequentemente, o SGBD acaba tendo seus próprios mecanismos de bufferização e de caching, já que isso influencia diretamente no tempo de resposta do SGBD ao usuário.

Agora, posso falar um pouco sobre algumas utilidades e ferramentas relacionadas ao gerenciamento do banco de dados.

### Loading
Quando falamos de **loading**, pensamos no seguinte: vou reformatar esses dados, então preciso carregar. O objetivo aqui é que consigamos puxar as informações do HD, tendo em mente que os dados vão ser reordenados para posteriormente serem carregados.

### Backup
Quando realizamos **backup**, conseguimos ter maior resiliência com relação às falhas. Falhas podem acontecer por N motivos, e os backups são formas seguras de mantermos a rastreabilidade das informações, sem perder dados significativos ou sensíveis, o que poderia ocasionar problemas para a companhia ou organização.

O backup de um SGBD para uma determinada memória ou nível de armazenamento, como um SSD (pode ser outro tipo), pode ocorrer de maneira incremental, onde essa movimentação dos dados é realizada aos poucos.

### Reorganização do Storage
Conseguimos reorganizar o armazenamento do banco de dados para torná-lo mais performático e organizado. Assim, podemos definir, por exemplo, sistemas distribuídos onde as informações ficarão armazenadas. Pode ser uma imagem local, que seria um backup, mas também poderíamos ter um USB distribuído nesse cenário.

### Monitoramento
Conseguimos monitorar os SGBDs através de alguns sistemas de monitoramento e tirar estatísticas de banco de dados e decisões. Além disso, podemos puxar e realizar queries que possam retornar o estado do banco de dados. Entendemos esse estado não como um snapshot ou um estado válido, mas sim como as informações ali contidas que conseguem representar o contexto.

Se tenho uma série de informações e quero analisá-las, vou criar queries, puxar essas informações e começar a analisar. Esse monitoramento está associado.

### Data Dictionary System
Já tínhamos visto o **Data Dictionary System** no início, no nosso diagrama de ambiente de SGBD.

> [!definicao] Data Dictionary System
> É um componente que armazena informações de decisão de design, padrão de utilização e descrição das aplicações. São informações extras, mas que estão relacionadas ao projeto de banco de dados e que podem fazer a diferença em uma futura modelagem ou modificação do seu banco.

### Software de Comunicação
Também temos o **software de comunicação**. Podemos utilizar um terminal, um workstation ou os PCs.

Lá atrás, quando tínhamos os grandes mainframes, computadores gigantescos e com até menor capacidade do que se tem hoje, utilizávamos muito o terminal. Acessávamos muito o banco de dados via terminal.

Conforme a história e os anos foram passando, a tecnologia teve seu custo reduzido. O acesso a dados começou a ser utilizado nas workstations dentro das companhias e, consequentemente, nos computadores pessoais. Assim, conseguimos uma maior facilidade no acesso às informações.

E, além disso, também nós temos...

`⏱ 13:40`

E, além disso, também nós temos ferramentas de design que facilitam a nossa vida, como, por exemplo, o `DB for designer`.
Com essas ferramentas, conseguimos criar os projetos conceituais e os modelos conceituais de alto nível.
Aqui estão algumas das ferramentas e mecanismos que acabam facilitando a nossa vida.

## Relacionado

- [[sgbd-etapas-estrutura-e-fases]]
- [[sgbd-cenarios-de-nao-utilizacao-e-alternativas]]
- [[sgbd-atores-indiretos-e-requisitos-operacionais]]
- [[sgbd-abordagens-e-caracteristicas-essenciais]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Olá, !

</details>
