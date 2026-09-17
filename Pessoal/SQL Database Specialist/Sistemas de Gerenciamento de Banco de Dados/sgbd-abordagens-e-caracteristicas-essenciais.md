---
titulo: "SGBD: Abordagens e Características Essenciais"
tags: [sgbd, banco-de-dados, conceitos, fundamentos, dados, sistema, organizacao]
data: 2026-09-17
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 14
conceitos: [Sistema de Gerenciamento de Banco de Dados (SGBD), Abordagem Tradicional, Redundância de Dados, Inconsistência de Dados, Autodescrição, Isolamento de Dados e Programas, Múltiplas Visões, Controle de Concorrência]
---

# SGBD: Abordagens e Características Essenciais

> [!resumo] Do que se trata
> Esta aula explora a abordagem de SGBD, detalhando suas características e vantagens em comparação com o gerenciamento de dados tradicional. Ela aborda problemas como redundância e inconsistência de dados em sistemas legados, apresentando o SGBD como uma solução dedicada. A aula também discute as principais características de um SGBD, incluindo autodescrição, isolamento, compartilhamento, múltiplas visões e controle de concorrência para transações multi-usuário.

## Para lembrar

- **Um Sistema de Gerenciamento de Banco de Dados (SGBD) é um sistema que traz características relacionadas ao gerenciamento de dados, como isolamento, autodescrição, compartilhamento e visões.**
- **A autodescrição de um banco de dados significa que ele mantém a estrutura que o define.**
- **A abordagem tradicional de gerenciamento de dados via programação pode levar à redundância de informações e inconsistência de dados entre diferentes aplicações.**
- **O SGBD possibilita o acesso concorrente às informações persistidas e evita a necessidade de modificar a aplicação ao alterar a estrutura de dados.**

## O que esta nota responde

- Por que é vantajoso utilizar um SGBD em vez de uma abordagem tradicional para gerenciar dados?
- Quais são as principais características de um Sistema de Gerenciamento de Banco de Dados (SGBD)?
- Como um SGBD resolve problemas de redundância e inconsistência de dados?

## Conceitos

**Sistema de Gerenciamento de Banco de Dados (SGBD)** · **Abordagem Tradicional** · **Redundância de Dados** · **Inconsistência de Dados** · **Autodescrição** · **Isolamento de Dados e Programas** · **Múltiplas Visões** · **Controle de Concorrência**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | SGBD: Abordagem e Características Iniciais | ▪▪ |
| `04:00` | Problemas Abordagem Tradicional e Solução | ▪▪ |
| `08:00` | Características Essenciais do SGBD | ▪▪▪ |
| `12:00` | Uso SGBD, Visões e Transações | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Sistema de Gerenciamento de Banco de Dados (SGBD)** | Um sistema que traz características relacionadas ao gerenciamento de dados, como isolamento, autodescrição, compartilhamento e visões. |
| **Abstração** | A abstração está associada ao isolamento entre programa e dados. É um pilar do pensamento computacional e permite determinar a estrutura dos dados no banco de dados e manipular essas informações. |
| **Banco de Dados Autodescritivo** | Significa que o banco de dados possui uma descrição específica e concisa de si mesmo dentro do sistema, o que permite gerenciar os dados da maneira mais otimizada. |

## Pegadinhas

- Na abordagem tradicional, a estrutura dos dados está atrelada à aplicação, exigindo *down* para modificações, o que é prejudicial em produção; com SGBD, a aplicação não gerencia a estrutura diretamente, minimizando o impacto de mudanças.
- A abordagem tradicional leva à redundância e inconsistência de dados, enquanto o SGBD garante consistência e facilita o compartilhamento e acesso concorrente.

## Teste-se

<details><summary>O que é um SGBD?</summary>

É um sistema que gerencia dados, oferecendo características como isolamento, autodescrição, compartilhamento e múltiplas visões.

</details>

<details><summary>Qual o principal problema da abordagem tradicional em relação à estrutura dos dados?</summary>

Na abordagem tradicional, a estrutura dos dados está atrelada à aplicação. Isso significa que qualquer modificação na estrutura exige o *down* da aplicação para ser implementada, o que é inviável em produção.

</details>

<details><summary>Cite duas características principais de um SGBD.</summary>

Duas características principais são a abstração, que isola programa e dados, e o banco de dados autodescritivo, que contém sua própria descrição para gerenciamento otimizado.

</details>

<details><summary>Como o SGBD lida com o controle de concorrência?</summary>

O SGBD garante que, ao modificar um dado, como o status de um assento, aquele campo seja bloqueado (para leitura ou totalmente) para evitar que múltiplos usuários tentem alterar o mesmo dado simultaneamente, prevenindo inconsistências.

</details>

<details><summary>Qual a vantagem das 'múltiplas visões' em um SGBD?</summary>

As múltiplas visões permitem que diferentes grupos de usuários, como o financeiro ou professores, acessem os mesmos dados de formas personalizadas, de acordo com suas necessidades específicas, sem impactar a estrutura original.

</details>

## Conteúdo

`⏱ 00:00`

Agora, vamos explorar a abordagem de SGBD. Este tema traz algumas características relacionadas ao **Sistema de Gerenciamento de Banco de Dados (SGBD)**.

> [!definicao] Sistema de Gerenciamento de Banco de Dados (SGBD)
> Um sistema que traz características relacionadas ao gerenciamento de dados, como isolamento, autodescrição, compartilhamento e visões.

As características que vamos conversar agora são: isolamento, autodescrição, compartilhamento e visões.

Como já comentei, o tema da aula é autodescritivo, assim como o banco de dados. Vamos falar sobre as abordagens e depois sobre as características:

-   **Autodescrição**: o banco de dados mantém a estrutura que o define.
-   **Isolamento de dados e programas**: vamos comparar o nível de isolamento de uma abordagem tradicional e de uma abordagem utilizando o SGBD.
-   **Múltiplas visões**: algo que vem para nos auxiliar a identificar e apresentar diferentes visões em cima de um mesmo conjunto de dados.
-   **Compartilhamento e processamento das transações**.

É nesse sentido que vamos começar a falar agora.

### Por que utilizar um SGBD?

Já comentei o que é e a questão da estrutura relacionada a alguns processos. Agora, precisamos entender por que usar um SGBD é tão mais interessante do que utilizar uma abordagem tradicional, que seria gerenciar esses dados via programação.

Vamos pensar sobre o assunto. Podemos, sim, além de definir a estrutura do conjunto de dados, fazer o gerenciamento deles dentro da sua aplicação. A questão é que você precisará fazer todo o gerenciamento.

Desde a alocação de memória (que pode depender do tipo da linguagem, por exemplo, Java faz isso de maneira transparente para o desenvolvedor), até definir a estrutura, armazenar em arquivo, puxar esses arquivos, manter a consistência dos dados e, além disso, manter a concorrência. Diferentes pessoas utilizando o mesmo arquivo não é muito viável. Geralmente, cada programa acaba utilizando seu próprio arquivo, e vemos algumas questões relacionadas a esse tipo de abordagem.

### Exemplo: Abordagem Tradicional e Redundância

> [!exemplo] Abordagem Tradicional e Redundância
> Vamos supor que temos duas aplicações simplificadas em um contexto universitário:
> -   `Cadastro`: função específica de cadastro de alunos.
> -   `Verificação de Pagamento`: função específica de identificar se o aluno pagou a mensalidade.
>
> Cada aplicação terá seu próprio conjunto de dados associados. A aplicação de `Cadastro` manterá os dados dos alunos, e a aplicação de `Verificação de Pagamento` também precisará de informações relacionadas ao aluno para verificar pagamentos, mantendo um conjunto de dados apenas para ela.
>
> **Problema:** Haverá redundância de informações (ex: identificação do aluno, dados do pagador) porque ambas as aplicações, dentro do mesmo contexto, estão relacionadas ao mesmo objeto (o aluno) e mantêm seus próprios conjuntos de dados.

Você pensa: "Ok, então eu tenho esses dados aqui, que estão sendo acessados por `Cadastro`." Nesse caso, só essa aplicação terá acesso e ela que terá que manter. Em contrapartida, a `Verificação de Pagamento` também precisa de informações relacionadas ao aluno, então ela precisa manter um conjunto de dados apenas para ela. E percebemos que haverá essa redundância.

`⏱ 04:00`

E a gente percebe que vai ter essa redundância. Além disso, cada uma dessas aplicações vai ter atributos específicos. Esses atributos poderiam ser utilizados em outra visão ou por outra aplicação.

De novo, fica com o problema de compartilhamento de informações. Gerenciar esse tipo de questão é bem mais complicado em uma abordagem tradicional.

### Problemas da Abordagem Tradicional

Além da questão da **redundância** e de uma necessidade de acesso concomitante ou concorrente, a estrutura desses dados está atrelada à aplicação. Não só o gerenciamento desses dados, mas toda a estrutura que define como os dados estão sendo armazenados.

> [!exemplo] Modificação de dados em abordagem tradicional
> Imagine se é preciso modificar um conjunto de dados, colocando um novo atributo ou uma informação a mais. Será necessário modificar na aplicação.
> >
> Em termos de produção, com uma aplicação (uma `API` rodando) acessando aqueles dados, você terá que:
> - Dar um *down* na aplicação.
> - Fazer a modificação.
> - Subir a aplicação de novo para que ela possa refletir a modificação que foi feita.

> [!atenção] Impacto da modificação de dados
> Em termos de produção, essa necessidade de *down* na aplicação para modificações é prejudicial.

Nós temos também um esforço repetitivo, no sentido de que é preciso manter dois arquivos diferentes que possuem informação relacionada, gerando redundância. Além de gastar recursos e poder computacional, podemos acarretar em outro problema: a **inconsistência**.

> [!exemplo] Inconsistência de dados: o aluno que trancou a matrícula
> Imagine que um aluno foi removido do conjunto de alunos da universidade porque trancou a matrícula.
> >
> Se essa informação for refletida no cadastro, mas não nos dados de pagamento, quando a aplicação for verificar se o aluno fez o pagamento da mensalidade, haverá uma inconsistência.
> >
> Isso pode ocasionar uma ação equivocada, como acionar o financeiro para que o aluno efetue o pagamento da mensalidade, quando na verdade ele já foi removido.

### A Solução: Um Sistema Dedicado para Dados

Nesse sentido, o que seria ideal? Utilizar um **sistema próprio** para isso. Quais seriam as vantagens? O que ele traz de novo?

Ao invés de termos duas aplicações distintas gerenciando arquivos e conjuntos de dados distintos, elas agora fazem uma consulta a um sistema, e não o gerenciamento direto das informações. A aplicação não mantém mais a estrutura relacionada àquele conjunto de dados.

Então, já não há o problema de ter que mudar toda a aplicação se a estrutura de dados mudar. O que acontece se houver alguma modificação dentro do sistema de banco de dados (o banco de dados armazenado no `SGBD`)? Provavelmente, teremos que representar alguma coisa na aplicação, talvez, se algum atributo ou objeto foi removido. No entanto, se não impactar na consulta da aplicação, você simplesmente continua.

Mais para frente, falarei sobre a parte de `SQL`, *queries* e modelagem. Quando fazemos um `SELECT` em uma tabela, não importa a quantidade de atributos relacionados a ela, o sistema simplesmente retorna os dados.

> [!exemplo] Consulta a dados com sistema dedicado
> Se você faz um acesso, por exemplo, a `aluno` (cadastro de aluno `V1 Select`), utilizando uma `API` em Java, ela retornará aquele conjunto de dados.
> >
> Se houver uma modificação e o aluno precisar de um novo dado associado a ele para representação...

`⏱ 08:00`

houve uma modificação e o aluno precisa de um novo dado associado a ele para estar representando melhor o meu contexto. Eu vou continuar fazendo `SELECT` do mesmo jeito. Eu não preciso modificar nada. Essa é uma das coisas interessantes de utilizar um **SGBD**. Você não precisa mais, nesse sentido, puxar ou consultar os alunos e suas propriedades. Eu não preciso mais modificar minha aplicação.

Em contrapartida, se eu tivesse isso dentro de um arquivo e minha aplicação estivesse gerenciando essa estrutura, eu teria que fazer a modificação com certeza.

O SGBD possibilita o acesso concorrente às informações persistidas. É toda uma regra que você acaba definindo. Falaremos sobre isso mais para frente, em outro módulo, onde conseguimos representar informações. Definirei para vocês as `views` logo em seguida, onde representamos perspectivas diferentes para grupos distintos.

Acesso concorrente, a não modificação da aplicação, gerenciamento e consistência dos dados são uma série de vantagens que temos ao utilizar um SGBD em detrimento de uma abordagem tradicional.

### Características Principais de um SGBD

Quais são as principais características que temos dentro de um SGBD?

- A primeira delas é a **abstração**.

> [!definicao] Abstração
> A abstração está associada ao isolamento entre programa e dados.
> Ela é um pilar do pensamento computacional, um processo de raciocínio utilizado na computação.
> É através da abstração que conseguimos determinar a estrutura dos dados no banco de dados e manipular essas informações.

- O banco de dados é **autodescritivo**.

> [!definicao] Banco de Dados Autodescritivo
> Significa que o banco de dados possui uma descrição específica e concisa de si mesmo dentro do sistema.
> Isso permite gerenciar os dados da maneira mais otimizada.

- Há a parte de **compartilhamento**. Consigo, de maneira facilitada, compartilhar informações e dados com diversos grupos distintos.

- Outra coisa associada ao compartilhamento que o SGBD traz é a questão do **controle de concorrência**. Isso significa que, se você está acessando um determinado dado e vai realizar algum tipo de modificação, como atualizar o estado de uma tabela, é necessário que isso seja feito de forma coerente, que haja corretude dos dados dentro do sistema.

> [!exemplo] Controle de Concorrência na Reserva de Assentos
> Imagine a reserva de assentos em uma aeronave para um determinado voo e horário.
> >
> Quando o status de um assento é atualizado de "livre" para "ocupado", é crucial que, pelo menos, aquele campo específico (o assento) seja bloqueado para acesso. Ele pode ser:
> - `read-only` (apenas de leitura);
> - bloqueado como um todo.
> >
> Isso evita a inconsistência de duas pessoas tentando reservar o mesmo assento simultaneamente. Caso contrário, haveria um problema no embarque, com duas pessoas com passagens diferentes para o mesmo assento. Por isso, precisamos de um controle de concorrência sobre esses dados.

`⏱ 12:00`

Esse controle de concorrência em cima desses dados se torna bem mais difícil de se implementar quando temos uma aplicação e recai naquele problema que mencionei anteriormente: se a estrutura de recebimento de dados está atrelada à programação da aplicação, é preciso baixar a aplicação, modificá-la e subi-la de novo. Isso é inviável em termos de produção.

### Utilização de SGBDs

Daí que temos a utilização de **SGBDs** (Sistemas Gerenciadores de Banco de Dados). Em 99% dos casos, utilizaremos SGBD. Explicarei quando não utilizá-los um pouco mais para frente.

### Múltiplas Visões dos Dados

Atrelado a isso, se diversas pessoas podem estar acessando esses dados, elas também podem precisar de visões distintas do mesmo dado, do mesmo contexto.

> [!exemplo] Visões personalizadas
> Uma pessoa do financeiro terá uma visão diferente da de um professor acadêmico, que precisa acessar os dados para inserir as notas no sistema.
> Cada setor, cada `squad`, cada local dentro da empresa terá um acesso diferenciado e personalizado, de acordo com o que é necessário.
> A partir de múltiplas visões, conseguimos essa perspectiva, essa mudança, uma divisão em cima dos cenários e do contexto em que temos os dados persistidos.

### Transações Multi-usuário

Além disso, temos as **transações multi-usuário**. Essas transações precisam ser executadas de maneira que levem o estado de um banco de um estado inicial para um estado posterior consistente. Isso significa que temos transações concorrentes, ou seja, de muitos usuários diferentes, realizando essas transações. O SGBD precisa gerenciar e controlar esse acesso da maneira mais otimizada possível.

Este foi um panorama sobre as questões de Banco de Dados e algumas características que já abordamos. Agora, vamos para o isolamento de dados e programas.

## Relacionado

- [[bancos-de-dados-da-evolucao-ao-big-data]]
- [[jornada-da-formacao-sql-database-specialist]]
- [[modelagem-de-dados-do-contexto-relacional-a-era-do-big-data-e-paradigmas-cientif]]
- [[sgbd-etapas-estrutura-e-fases]]
