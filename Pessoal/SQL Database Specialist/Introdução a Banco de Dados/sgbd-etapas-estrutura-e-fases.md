---
titulo: "SGBD: Etapas, Estrutura e Fases"
tags: [banco-de-dados, sgbd, conceitos, dados, modelagem-de-dados, estrutura-de-dados, sql]
data: 2026-09-14
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 14
conceitos: [SGBD, Definição de Dados, Construção de Banco de Dados, Manipulação de Dados, Compartilhamento de Dados, Transação, Estrutura Relacional, Tabela (Banco de Dados)]
---

# SGBD: Etapas, Estrutura e Fases

> [!resumo] Do que se trata
> Esta aula aprofunda no conceito de SGBD, detalhando suas etapas fundamentais: definição, construção, manipulação e compartilhamento. Explora a estrutura relacional de um SGBD, explicando tabelas, colunas e linhas. Aborda também as fases de construção e manipulação, incluindo a importância de índices para performance e o processamento de transações.

## Para lembrar

- **Um SGBD (Sistema Gerenciador de Banco de Dados) é um software de propósito geral que gerencia os dados persistidos.**
- **As etapas de um SGBD incluem Definição, Construção, Manipulação e Compartilhamento dos dados.**
- **Na fase de Definição, são estabelecidos o tipo de dado, a estrutura e as regras que representam o 'mini mundo' real dentro do SGBD.**
- **A estrutura fundamental de um SGBD relacional é a tabela, composta por colunas (atributos) e linhas (dados persistidos).**
- **Transações são conjuntos de comandos ou ações agregadas que são submetidas ao SGBD para processamento.**

## O que esta nota responde

- Quais são as etapas fundamentais de um SGBD?
- Como é a estrutura relacional de um SGBD e quais seus componentes?
- O que é uma transação no contexto de um SGBD?

## Conceitos

**SGBD** · **Definição de Dados** · **Construção de Banco de Dados** · **Manipulação de Dados** · **Compartilhamento de Dados** · **Transação** · **Estrutura Relacional** · **Tabela (Banco de Dados)**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | SGBD: Definição e Etapas Principais | ▪▪ |
| `04:20` | SGBD: Transações, Ciclo, Proteção | ▪▪ |
| `09:00` | Estrutura Relacional, Metadados e Fases | ▪▪▪ |
| `13:20` | Exemplo: Concorrência e Bloqueio | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **SGBD** | Um software de propósito geral cuja função principal, entre outras atividades, é gerenciar os dados que estão sendo persistidos dentro dele. |
| **Software Modular** | É composto por outros softwares internos que vão auxiliá-lo na execução de suas tarefas associadas. |
| **Tabela (Estrutura Relacional)** | É a estrutura fundamental da estrutura relacional, onde cada entidade é mapeada. É composta por colunas, relacionadas aos atributos, e linhas, que representam os dados persistidos. |
| **Metadados** | Estão relacionados às informações de estrutura de um banco de dados ou de um conjunto de dados. Descrevem o banco de maneira concisa e são contidas no SGMD. O SGMD consulta os metadados para processar queries, compilando-as e acessando a estrutura antes de buscar os dados persistidos. |

## Teste-se

<details><summary>Quais são as quatro etapas principais de um SGBD?</summary>

As quatro etapas principais de um SGBD são Definição, Construção, Manipulação e Compartilhamento.

</details>

<details><summary>O que é um SGBD?</summary>

Um SGBD (Sistema Gerenciador de Banco de Dados) é um software de propósito geral. Sua função principal é gerenciar os dados que estão sendo persistidos dentro dele.

</details>

<details><summary>Qual a função dos metadados em um SGBD?</summary>

Metadados são informações de estrutura de um banco de dados, descrevendo-o de forma concisa. O SGMD os consulta para processar queries, entender a estrutura e acessar os dados persistidos.

</details>

<details><summary>Como o SGBD lida com o acesso simultâneo de dados na fase de compartilhamento?</summary>

O SGBD gerencia acessos concorrentes criando regras e, por padrão, bloqueia tabelas durante updates via transações. Isso garante a integridade dos dados, como em uma reserva de assento.

</details>

<details><summary>Quais são os dois níveis de proteção que um SGBD oferece?</summary>

O SGBD oferece proteção contra mau funcionamento, usando réplicas e logs para retornar a um estado persistente. Também oferece proteção de acesso, restringindo usuários e definindo perspectivas distintas dos dados.

</details>

<details><summary>O que é uma tabela na estrutura relacional e quais seus componentes?</summary>

Uma tabela é a estrutura fundamental da estrutura relacional, onde cada entidade é mapeada. Ela é composta por colunas, que representam atributos, e linhas, que representam os dados persistidos.

</details>

## Conteúdo

`⏱ 00:00`

Já diferenciamos banco de dados de SGBDs e agora vamos aprofundar no que é um SGBD.

> [!definicao] SGBD
> Um **SGBD** (Sistema Gerenciador de Banco de Dados) é um software de propósito geral cuja função principal, entre outras atividades, é gerenciar os dados que estão sendo persistidos dentro dele.

Atreladas ao SGBD, existem algumas etapas:
- Definição
- Construção
- Manipulação
- Compartilhamento

### Etapas de um SGBD

#### Definição

Esta fase geralmente está atrelada à parte mais conceitual. Nela, precisamos definir o tipo de dado, a estrutura e as regras ou diretrizes associadas ao contexto. Pensamos em um "mini mundo", ou seja, qual é a representação do mundo real que queremos colocar e representar dentro do SGBD.

#### Construção

Em uma fase posterior, temos a construção do SGBD, que implica na própria inserção e persistência desses dados, garantindo sua existência através de uma determinada estrutura. Aqui, ocorre o mapeamento: as informações são retiradas de requisitos, compreendidas, e a estrutura designada para o SGBD (no nosso caso, relacional) é criada. A partir dessa estrutura, é possível criar uma série de comandos para persistir e inserir as informações no SGBD.

#### Manipulação

Nesta etapa, o SGBD já está em funcionamento, fornecendo e fomentando dados para diversas aplicações. A fase de manipulação está relacionada à recuperação de informações e à geração de relatórios. Ela será acessada por algumas aplicações, dependendo do ambiente computacional e do contexto do negócio.

Existe uma linguagem específica que fornece acesso aos dados. Essa linguagem atua como intermediária, pois o computador não entende linguagens de alto nível, ele entende bits.

> [!exemplo] Acesso e Compilação de Comandos
> Quando você interage com o SGBD usando uma linguagem de alto nível, como SQL, o computador não entende diretamente esses comandos. As informações e comandos que você envia são compilados, ou seja, traduzidos para a linguagem de máquina (bits). Somente depois dessa compilação o SGBD pode processar e transferir as informações solicitadas. Da mesma forma, relatórios podem ser gerados, puxando diversas informações do SGBD.

#### Compartilhamento

Na fase de compartilhamento, assim como na manipulação, diversas aplicações acessam os dados em momentos distintos. Provavelmente, haverá diferentes grupos de usuários interessados no mesmo dado (não no tipo de dado, que remete a `int`, `float` etc., mas na mesma entidade ou tabela).

Nesse cenário, é preciso determinar o acesso simultâneo e como ele ocorrerá dentro do SGBD. Regras são criadas para gerenciar esses acessos concorrentes. O SGBD é capaz de fornecer acessos simultâneos, mas é crucial gerenciar esses acessos, pois ele possui um comportamento específico por padrão.

Percebemos que é possível executar uma série de ações. Essas ações, ou conjuntos de comandos, são agregadas dentro de uma **transação**.

`⏱ 04:20`

E você submete essa transação ao SGBD. A partir daí, o SGBD te retorna os dados relacionados àquelas solicitações que você enviou. As *queries* que você vai realizar, as consultas, são, na verdade, solicitações. Você solicita uma determinada informação ao banco de dados e ele te passa os dados relacionados àquela informação.

Além disso, o SGBD tem outras características interessantes. Ele possui um ciclo de vida longo, com um longo prazo de utilização, de forma que se consiga utilizá-lo bastante sem haver comprometimento da base.

Outro fator interessante é a questão da proteção. Existem dois níveis diferentes de proteção:

| Nível de Proteção | Descrição |
|---|---|
| Mau Funcionamento | Utilização de réplicas e ações para contornar falhas no sistema. Uso de log para retornar ao estado anterior do banco de dados, onde aquele estado era persistente. |
| Acesso | Restrição de acesso a um grupo de pessoas e determinação de perspectivas distintas de um mesmo dado. |

O SGBD traz essas diversas vantagens e *features* associadas a ele.

### Estrutura do SGBD

Para descrever essas etapas, um contexto de universidade foi trazido. A estrutura de como seria o SGBD é a seguinte:

> [!definicao] Software Modular
> O SGBD é um **software modular**, ou seja, ele é composto por outros softwares internos que vão auxiliá-lo na execução de suas tarefas associadas.

Por exemplo, a compilação das *queries*, armazenar informações especificamente, armazenar a informação de estrutura, acesso ao banco de dados, enfim. Diversos softwares modulares estarão compondo um SGBD.

Se pensarmos em um cenário de universidade, onde o SGBD está persistindo informações sobre alunos, o aluno tem uma série de características específicas. Mas estamos interessados em um conjunto dessas características. Esse conjunto vai nos fornecer uma ideia que vai modelar e representar o contexto.

Nesse sentido, temos alguns exemplos de informações sobre alunos de universidade. Vamos entender como é esse processo.

Para exemplificar, dentro desse diagrama, temos os programas de usuário que farão acesso ao SGBD. Aqui, temos a aplicação que vai rodar as *queries*, ou seja, os programas de acesso direto. Por exemplo, quando se entra no `MySQL` e se executa uma *query* como `SHOW DATABASES` para verificar quais bancos de dados estão persistidos dentro do SGBD.

Aqui, começamos a entender os softwares, onde nós temos o processamento das *queries*. Essas *queries* vão ser compiladas. A partir daí, uma vez que foram compiladas, esses dados precisam ser acessados e, eventualmente, o banco de dados precisa acessar informações relacionadas à estrutura desses dados que estão armazenados.

Na fase de definição, estamos explorando novas entidades. Queremos persistir e rastrear informações sobre estudante, curso, sessão, alguns pré-requisitos relacionados aos cursos e o relatório da grade. Essas entidades compõem um BD específico dentro do SGBD.

A estrutura que está representando essa base de dados, e que está persistida nesse local, é denominada **metadados**. O SGBD faz uso dessas informações para criar e ter um modelo para essa base que será persistida e para eventuais consultas.

`⏱ 09:00`

e para eventuais consultas.

E aqui, para mostrar como seria a **estrutura relacional**, se estou falando de SGBD, não tem como não mostrar um pouco da estrutura que ele possui.

> [!definicao] Tabela (Estrutura Relacional)
> Cada **entidade** é mapeada para uma **tabela**, que é a estrutura fundamental da **estrutura relacional**.
> >
> Uma tabela é composta por:
> - **Colunas**: Relacionadas aos **atributos**, que são as propriedades de uma determinada entidade ou objeto.
> - **Linhas**: Representam os dados persistidos.
> >
> Essa estrutura permite fazer o link entre as informações.

> [!exemplo] Navegando a estrutura relacional
> Por exemplo, ao verificar um estudante, temos o número do estudante no `Grad Report`. Isso indica que o relatório de notas está relacionado ao estudante.
> >
> Podemos ver a sessão em que o estudante está matriculado, como a "grade B", que está relacionada a um determinado estudante em uma sessão `112`.
> >
> Ao verificar a sessão `112`, descobrimos que é de matemática e ministrada pelo professor Scheng.
> >
> Assim, conseguimos fazer o link e navegar entre essas entidades (tabelas), identificando informações e situações relacionadas ao nosso contexto.

Cada atributo determinará um **tipo de dado** específico para a propriedade. Por exemplo, o número do estudante pode ser representado com `int`, e o nome pode ser um `varchar`.

> [!definicao] Metadados
> Os **metadados** estão relacionados às informações de estrutura de um banco de dados ou de um conjunto de dados.
> >
> Essas informações descrevem o banco de maneira concisa e são contidas no SGMD (Sistema Gerenciador de Metadados).
> >
> O SGMD consulta os metadados quando precisa processar as *queries* realizadas. Ao compilar as *queries* e antes de acessar os dados persistidos, ele consulta a estrutura, o esquema e os metadados do banco.
> >
> Após conhecer a estrutura, o sistema então busca as informações.

### Fase de Construção

Nesta fase, determinamos como será feito o acesso aos dados persistidos em diversos arquivos. É preciso pensar em como acessar esses dados de forma performática. Qual estrutura de dados utilizar para realizar uma busca eficiente?

Existem estruturas de dados específicas que melhoram a performance de busca de informações. Nesta fase, tratamos especificamente esses casos, como, por exemplo, determinando **índices** para um acesso mais rápido a um determinado dado dentro do banco de dados.

### Fase de Manipulação (Manutenção)

Nesta fase, que seria a manutenção do banco, temos os *updates* que acabam acontecendo. Uma solicitação, seja via acesso de usuário ou de algum programa, é processada pelo próprio SGBD. O sistema a transforma em *query* e a passa para compilação.

Da compilação, ele determina o acesso àqueles dados, consulta os metadados para então pegar as informações que estão ali dentro, entender a estrutura e retornar esses dados, voltando todo o caminho até o usuário.

### Compartilhamento e Concorrência

Quando precisamos realizar um compartilhamento, o SGBD determina, por padrão, que haja um bloqueio das tabelas quando for executado um *update* dessas informações relacionadas à tabela. Esse tipo de coisa ocorre via **transação**.

Por exemplo, quando estou num cenário de modificação de assento...

`⏱ 13:20`

quando estou num cenário de modificação de assento em um avião.

> [!exemplo] Cenário de modificação de assento em um avião
> Nesse cenário, se eu estiver reservando uma cadeira, preciso que ela realmente esteja reservada para mim.
> Para isso, é necessário bloquear o acesso de outros indivíduos ou usuários àquela tabela de maneira momentânea, enquanto a reserva ainda não foi realizada e efetivada.

## Relacionado

- [[SGBD]]
- [[01 - Conceitos Banco de Dados]]
- [[bancos-de-dados-definicao-acesso-e-escala]]
- [[00 - Índice]]
