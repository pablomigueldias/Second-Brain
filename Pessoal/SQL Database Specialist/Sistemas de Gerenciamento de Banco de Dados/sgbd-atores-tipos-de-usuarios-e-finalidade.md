---
titulo: "SGBD: Atores, Tipos de Usuários e Finalidade"
tags: [sgbd, banco-de-dados, conceitos, fundamentos, engenharia-de-software, modelagem-de-dados]
data: 2026-09-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 14
conceitos: [Atores em SGBD, Designer de Banco de Dados, Projeto Conceitual, Usuários Finais, Kennedy Transactions, Usuários Ingênuos (Naive), Usuários Standalone, Engenheiro de Software]
---

# SGBD: Atores, Tipos de Usuários e Finalidade

> [!resumo] Do que se trata
> A aula explora os diversos atores envolvidos em um SGBD, como designers, DBAs e usuários finais, e suas respectivas responsabilidades. Detalha as categorias de usuários, incluindo ingênuos, sofisticados e standalone, e as formas como interagem com o sistema, seja via queries ou APIs. Aborda a finalidade do SGBD em facilitar o acesso e a manipulação de dados, além de discutir cenários em que SGBDs relacionais podem não ser a solução ideal.

## Para lembrar

- **Em grandes organizações, há perfis bem definidos de atores em um SGBD: o administrador (DBA), o designer e os usuários finais.**
- **O designer de banco de dados levanta os requisitos, identifica os dados, representa-os graficamente e mapeia a estrutura para o modelo relacional.**
- **Projeto Conceitual é a fase onde se identificam tanto requisitos funcionais como não funcionais para a modelagem do banco de dados.**
- **Usuários ingênuos (naive) acessam os dados por uma API gráfica (GUI), como em um caixa eletrônico, com raras ocorrências de erros.**
- **A finalidade do SGBD é implementar diversos recursos para facilitar a vida dos usuários, proporcionando uma experiência mais amigável que a abordagem tradicional.**

## O que esta nota responde

- Quais são os principais atores envolvidos na operação de um SGBD?
- Qual o papel do designer de banco de dados e do engenheiro de software em um SGBD?
- Quais são os diferentes tipos de usuários finais e como eles interagem com o SGBD?

## Conceitos

**Atores em SGBD** · **Designer de Banco de Dados** · **Projeto Conceitual** · **Usuários Finais** · **Kennedy Transactions** · **Usuários Ingênuos (Naive)** · **Usuários Standalone** · **Engenheiro de Software**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | SGBD: Atores, vantagens e cenários | ▪▪ |
| `04:20` | Modelagem, DBA e usuários finais | ▪▪ |
| `08:20` | Tipos de usuários e programadores | ▪▪ |
| `12:40` | Fluxo de interação e tarefas | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Projeto Conceitual** | É a fase onde se identificam tanto requisitos funcionais como não funcionais. É o primeiro projeto, a fase preliminar da elaboração de um banco de dados. |
| **DBA (Database Administrator)** | É o administrador do banco de dados. |
| **Kennedy Transactions** | As transações são encapsuladas através de uma linguagem de programação. |

## Teste-se

<details><summary>Quais são os três principais atores do dia a dia em um SGBD?</summary>

Os atores do dia a dia em um SGBD são o administrador (DBA), o designer e os usuários finais.

</details>

<details><summary>Qual é o papel principal do designer de banco de dados?</summary>

O designer de banco de dados levanta os requisitos, identifica os dados do contexto e os representa graficamente para mapear a estrutura para o modelo relacional.

</details>

<details><summary>Como os usuários ingênuos (naive) geralmente acessam os dados?</summary>

Os usuários ingênuos acessam os dados por uma API gráfica (GUI) e utilizam as chamadas Kennedy Transactions, onde as transações são encapsuladas por uma linguagem de programação.

</details>

<details><summary>Quem são os responsáveis por programar as Kennedy Transactions?</summary>

Os engenheiros de software são os responsáveis por programar as Kennedy Transactions, desenvolvendo APIs, programas e aplicações que acessam o banco de dados.

</details>

<details><summary>Qual a finalidade geral de um SGBD?</summary>

A finalidade do SGBD é implementar diversos recursos para facilitar a vida dos usuários, proporcionando uma experiência mais amigável no acesso e consulta aos dados.

</details>

<details><summary>Em que cenário um SGBD relacional pode não ser suficiente?</summary>

Um SGBD relacional pode não ser suficiente em cenários com milhões ou bilhões de acessos e instâncias de um banco de dados, onde se parte para bancos NoSQL.

</details>

## Conteúdo

`⏱ 00:00`

Entraremos agora em uma nova área, onde falaremos de outras características relacionadas aos SDPDs, continuando a exploração das abordagens de sistemas de gerenciamento de banco de dados. Nosso foco está nos atores: quem trabalha nos bastidores para fazer o sistema acontecer, quais as vantagens de utilizar um SGBD e quando não utilizá-lo – sim, há cenários em que isso acontece.

O tema é bem descritivo: atores, workers, vantagens e quando não utilizar. Começaremos pelos atores de um banco de dados.

Em organizações mais simples, ou mesmo para um freelancer, temos bancos de dados mais simplificados, de acesso geralmente único. Acesso único não significa que o sistema esteja limitado a um único acesso, mas que poucas pessoas estão interessadas em acessar as informações.

Já no contexto de grandes organizações, como big organizations, big techs e big companies, há uma grande equipe, um setor com muitas pessoas interessadas em manipular e interagir com o sistema. Nesse cenário, falamos de 10 mil persistências, um número muito grande de acessos.

Quando pensamos em milhões ou bilhões de acessos e instâncias de um banco de dados, o SGBD relacional não é suficiente. Essa é uma ordem gigantesca, e nesse ponto, partimos para o cenário dos bancos `NoSQL`. Com esse cenário mais complexo em mente, percebemos que há perfis bem definidos de atores em um SGBD.

### Atores em SGBD

O primeiro aspecto é o **design**. Há a necessidade de modelar. Embora isso possa ser usado em abordagens simplificadas, é muito requisitado em grandes organizações. A modelagem precisa ser, se não perfeita, pelo menos otimizada, devido ao número gigantesco de acessos.

Temos também a **usabilidade**: quem determinará como o sistema funciona para satisfazer os requisitos?

E a **manutenção**: haverá uma equipe responsável por realizá-la.

Dentro desse cenário, os atores do dia a dia são:
- O administrador (DBA)
- O designer
- Os usuários finais

Vamos agora detalhar o significado e os papéis de cada um.

### O Designer de Banco de Dados

O primeiro perfil a ser explorado é o **designer de banco de dados**. Seu papel é:
- Levantar os requisitos.
- Identificar os dados que comporão o contexto.

Ele entra em contato com o cliente – a pessoa interessada na modelagem e no consumo das informações.

Após identificar requisitos e dados, o designer deve representá-los graficamente. Isso permite, junto com a equipe de banco de dados, mapear a estrutura para o modelo, no nosso caso, relacional.

Esta é a fase preliminar, constituída pela modelagem. O designer tem grande preocupação em entender o contexto dos dados, o que será retornado de informação e quais perguntas precisam ser respondidas.

`⏱ 04:20`

A maneira com que você quer enxergar os dados vai interferir na modelagem. E a modelagem vai interferir na estrutura que será definida para compor esses dados. Consequentemente, uma estrutura equivocada não refletirá no banco de dados uma eventual consulta com uma determinada pergunta que a pessoa quer.

Entenderemos bem melhor o que vai interferir na modelagem, como dispor as entidades e os relacionamentos, e como isso vai interferir quando tratarmos, mais adiante, de modelagem utilizando o modelo de entidade e relacionamento, que está associado ao projeto conceitual.

> [!definicao] Projeto Conceitual
> É a fase onde se identificam tanto requisitos funcionais como não funcionais. É o primeiro projeto, a fase preliminar da elaboração de um banco de dados.

### Papel do DBA

Na sequência, temos o **DBA**, que é o administrador do banco de dados. Ele geralmente tem uma staff o acompanhando. O designer geralmente compõe a staff do DBA.

> [!definicao] DBA (Database Administrator)
> É o administrador do banco de dados.

O DBA gerencia os recursos do banco de dados, orquestra o sistema e maneja a autorização de acesso. Ele define as `constraints`, a estrutura, a base de dados, tudo que está relacionado, e softwares adicionais relacionados à execução, configuração e gerenciamento do banco de dados. Conforme necessário, ele passa essas responsabilidades para sua staff.

### Usuários Finais e Acesso ao Banco de Dados

Os **usuários finais** são aqueles interessados em consumir as informações. Eles são categorizados por alguns critérios. A maioria deles não acessa via `query`.

Conforme a informação for progredindo, quando estivermos tratando de SQL e modelagem de entidade e relacionamento para modelo relacional, entenderemos como realizar `queries`. Estaremos criando um banco de dados, persistindo dados, extraindo informações e fazendo consultas mais simples e mais complexas.

Mais adiante, trabalharemos com a parte de programação voltada para a integração com o banco de dados. Construiremos `APIs` que realizarão a consulta ao banco, e essas `APIs` serão utilizadas pelos atores, os usuários finais. Utilizaremos `APIs` em `Java` e em `Python` para realizar esse tipo de consulta.

As maneiras de acesso são via `query` e via `APIs`. O propósito do **SGBD** (Sistema Gerenciador de Banco de Dados) é justamente fomentar o acesso dessas pessoas, desses usuários.

Os usuários finais são classificados por alguns critérios:

-   **Casual**: Tem acesso ocasional e geralmente busca diferentes informações persistidas. O acesso é frequentemente acompanhado do uso de `APIs`, como, por exemplo, via um `phpMyAdmin` ou uma `API` de mais alto nível, onde a parte de `query` seria mais transparente para ele.
-   **Ingênuo**: Constitui a maior parte dos usuários finais.

`⏱ 08:20`

Os usuários ingênuos, que representam a maior parte dos usuários finais, utilizam algo chamado `Kennedy Transactions`.

### Kennedy Transactions

> [!definicao] Kennedy Transactions
> As transações são encapsuladas através de uma linguagem de programação.

É justamente o que faremos mais adiante, programando com Java e Python para integrar com o sistema de novidades, retornando o valor das consultas.

### Usuários Ingênuos (Naive)

A maioria dos usuários, chamados de **ingênuos** ou *naive*, acessa os dados por uma `API` gráfica, ou `GUI`. Nesse sentido, raramente ocorrem erros. Se houver erro a partir de uma `Kennedy Transaction`, ele estará associado ao desenvolvimento da aplicação.

Aqui estão alguns exemplos de cenários em que o usuário ingênuo atua como ator de coleta e consulta desses dados.

> [!exemplo] Cenário de Usuário Ingênuo
> Um caixa eletrônico, onde a pessoa está sacando dinheiro, é um exemplo de cenário em que o usuário ingênuo atua na coleta e consulta de dados. Ele permite o acesso e a passagem de informações.

Há uma infinidade de exemplos onde acessamos diversos bancos de dados, sistemas e `SGBDs` para consumir dados a partir de `APIs`.

### Usuários Sofisticados

Os **usuários sofisticados** já possuem conhecimento prévio do sistema. São cientistas, engenheiros, analistas e outras pessoas que já têm noção da tecnologia, conhecem o `SGBD` e entendem como ele funciona, utilizando `queries`.

Quando se fala em "noção", eles não precisam ter conhecimento total do sistema para consumir os dados. Basta que entendam como funciona uma `query SQL` para extrair as informações. Eles não precisam compreender o funcionamento detalhado de um `SGBD`, suas abordagens ou vantagens.

O intuito desta formação é capacitar profissionais especialistas em banco de dados, por isso detalhamos esses conceitos. Vocês não são simplesmente usuários, mas sim especialistas neste assunto.

### Usuários Standalone

Temos também o usuário **Standalone**, que possui um `DB` e realiza seus acessos e consultas. A diferença é que ele está *standalone*, ou seja, apenas ele acessa essa base de dados.

### Finalidade do SGBD

A finalidade do `SGBD` é implementar diversos recursos para facilitar a vida dos usuários. Nesse sentido, todos os usuários acessam e realizam consultas aos dados, e o sistema proporciona uma experiência mais amigável do que a abordagem tradicional, que utiliza aplicações.

### Programadores de Kennedy Transactions

Quem programa as `Kennedy Transactions`? Os responsáveis por essas transações, que são encapsuladas e enviadas ao `SGBD` para tratamento, são os **engenheiros de software**.

Temos, portanto, mais um ator associado que não está diretamente ligado ao ambiente do `SGBD`. No entanto, ele é importante porque programa e desenvolve `APIs`, programas e aplicações que acessam o banco de dados, seja diretamente ou via `APIs`.

`⏱ 12:40`

ou via `APIs`.

### Fluxo de Interação com a API

O **programador**, ou **`dev`**, desenvolve uma **`API`**. Essa `API` é consultada por um usuário. Por sua vez, a `API` consulta o banco de dados. O banco retorna a informação, e a `API` a retorna para o usuário que a solicitou.

| Etapa | Ator | Ação |
| :---- | :--- | :--- |
| 1     | Usuário | Consulta a `API` |
| 2     | `API` | Consulta o banco de dados |
| 3     | Banco de dados | Retorna a informação |
| 4     | `API` | Retorna a informação para o usuário |

### Tarefas do Engenheiro de Software

As tarefas e atividades relacionadas ao engenheiro de software incluem:

-   análise de sistema;
-   desenvolvimento da aplicação;
-   teste e documentação da aplicação.

## Relacionado

- [[sgbd-natureza-autodescritiva-esquema-e-catalogo]]
- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[bancos-de-dados-da-evolucao-ao-big-data]]
- [[sgbd-perspectivas-distintas-com-views]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- dinheiro eu depositando dentro de uma rede social quando você se conecta uma pessoa dá um like no post a parte de transportes também quando eu tô passando por exemplo pelo que eu esqueci o nome que dá hoje em vez de você passar pelo pedágio pagar diretamente a pessoa Há um RFIDzinho, vou reformular isso, há um RFID, que é o identificador par de frequência, onde ele se conecta ali com o sensor que está dentro do pedágio, e a partir de uma base que ele tem ali, ele está refletindo se ele tem ou não saldo.

</details>
