---
titulo: "Modelagem de Dados: Requisitos, Modelos Conceitual e Lógico"
tags: [sgbd, dados, banco-de-dados, modelagem-de-dados, fundamentos, conceitos, engenharia-de-software]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 11
conceitos: [Banco de Dados, SGBD, Requisitos do Sistema, Dado, Informação, Modelagem de Alto Nível, Modelo Conceitual, Modelo Lógico]
---

# Modelagem de Dados: Requisitos, Modelos Conceitual e Lógico

> [!resumo] Do que se trata
> Esta aula detalha o processo de criação de um banco de dados, começando pela compreensão dos requisitos do sistema e a elaboração de uma narrativa de alto nível. Ela explora o processo evolutivo da modelagem, a importância dos dados para insights de negócio e a transição entre os modelos conceitual e lógico. O objetivo é guiar desde a ideia inicial até a definição da estrutura exata do banco de dados.

## Para lembrar

- **Dado é o dado cru, sem significado aparente; informação é o dado refinado que alimenta decisões de negócio.**
- **A modelagem de alto nível começa com a criação de uma narrativa do sistema, definindo o contexto e os requisitos a serem representados.**
- **O processo de criação e configuração de um banco de dados é evolutivo e gradual, culminando na implementação após a fase de modelagem.**
- **O Modelo Conceitual de alto nível, com objetos e suas interações, serve como base para a definição do Modelo Lógico, que especifica a estrutura exata do banco de dados.**

## O que esta nota responde

- Como um banco de dados é concebido e quais são as etapas iniciais de sua criação?
- Qual a distinção fundamental entre dado e informação no contexto de um sistema de gerenciamento de dados?
- Quais são as características e o propósito dos modelos conceitual e lógico na modelagem de um banco de dados?

## Conceitos

**Banco de Dados** · **SGBD** · **Requisitos do Sistema** · **Dado** · **Informação** · **Modelagem de Alto Nível** · **Modelo Conceitual** · **Modelo Lógico**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Nascimento e persistência de dados | ▪ |
| `04:00` | Cenários e importância dos dados | ▪ |
| `08:20` | Modelo lógico e arquitetura | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Dado** | O dado cru, ele não tem significado aparente. |
| **Informação** | É o resultado do refinamento de dados, que adquire significado e alimenta decisões de negócio. |
| **Modelo Lógico** | Nesta fase, define-se a estrutura exata do banco de dados, escolhendo um modelo de arquitetura de banco de dados específico, como o relacional. O objetivo é delimitar o tipo de modelo (relacional, baseado em documento, baseado em grafo, etc.), e não um Sistema Gerenciador de Banco de Dados (SGBD) específico. |

## Pegadinhas

- Informação é diferente de dado: dado é cru, informação é refinada e com significado.
- O Modelo de Entidade-Relacionamento (MER) da versão de 1970 não contempla a visão de orientação a objetos.
- O modelo lógico define o tipo de arquitetura do banco de dados (relacional, documento, grafo), mas a escolha do SGBD específico ocorre apenas na fase do projeto físico.

## Teste-se

<details><summary>Qual a diferença fundamental entre dado e informação?</summary>

Dado é a informação crua, sem significado aparente. Informação é o dado refinado, que adquire significado e alimenta decisões de negócio.

</details>

<details><summary>Quais são as duas primeiras fases do processo evolutivo de criação de um banco de dados, antes da implementação?</summary>

As duas primeiras fases são a definição do que se quer representar (requisitos e contexto) e a criação de um modelo ou esquema conceitual.

</details>

<details><summary>O que é definido no modelo conceitual de alto nível?</summary>

No modelo conceitual de alto nível, definem-se os requisitos, questões de visualização, quem usará, os atributos dos objetos e suas interações (relacionamentos).

</details>

<details><summary>Qual o objetivo principal do modelo lógico?</summary>

O objetivo principal do modelo lógico é definir a estrutura exata do banco de dados, escolhendo um modelo de arquitetura específico (como relacional, baseado em documento ou grafo), sem especificar o SGBD.

</details>

<details><summary>Em que fase do projeto de banco de dados é escolhido o SGBD específico?</summary>

O SGBD específico é escolhido na fase posterior, dentro do projeto físico.

</details>

## Conteúdo

`⏱ 00:00`

### O Nascimento de um Banco de Dados

Vamos finalmente, brincadeiras à parte, para o nosso projeto. Como nasce um banco de dados? Como surge a ideia de tirar todo aquele papel, toda a função de gerenciamento de dados da aplicação e passar para um sistema à parte? Como fazemos para ter um SGBD gerenciando o nosso banco de dados?

Qual é a ideia? Como vou implementar um banco de dados? Tenho as informações, sou uma empresa, tenho meus clientes, tenho uma série de informações. Elas estão lá na planilha, e preciso colocá-las em um sistema de gerenciamento de dados. Preciso persistir isso no BD de uma maneira mais inteligente e automatizada.

### Entendendo os Requisitos do Sistema

Preciso, então, entender os requisitos do meu sistema. Qual é o meu contexto? O que estou modelando? O que preciso responder? Quais são os perfis? O que preciso estar representando no meu modelo para estar coerente com as informações que estou querendo persistir e também estar coerente com o que estou querendo responder?

> [!definicao] Dado vs. Informação
> Porque é o seguinte: a partir de diversas informações, diversos **dados** que estão persistidos no banco de dados, quero te dar a **informação**.
> >
> Informação é diferente de dado. O **dado** é o dado cru, ele não tem significado aparente. Preciso refinar aqueles dados para conseguir informações, e as informações alimentam decisões de negócio.

Nessa fase, preciso entender qual é o meu contexto. Ou seja, se é um contexto de vendas, preciso entender que tenho um cliente, um produto e uma venda. A partir daí, já consigo entender quais são os meus objetos.

### Modelagem de Alto Nível: Criando a Narrativa

Vou descrever parte a parte o que contempla essa minha primeira fase, que é a parte de alto nível, modelagem de alto nível.

> [!exemplo] Criando a narrativa do sistema
> Entendi meu contexto. O que você vai fazer? Você vai criar uma narrativa. Você vai falar: "Ah, o meu sistema precisa gerar vendas, e essas vendas são oriundas de pedidos, e os pedidos são criados por clientes." E aí você começa.
> >
> Você cria toda uma narrativa, uma história, para poder estar definindo aquele seu contexto a ser modelado.
> >
> E dentro dessa história, você pode colocar requisitos:
> - "Ah, o meu cliente só pode comprar com o CPF. Ele não pode utilizar mais de um CPF."
> - Ou, por exemplo: "O meu cliente só pode comprar o produto utilizando o cartão que está com o CPF dele."
> >
> Isso eu só estou chutando, não estou dizendo que isso acontece, é só para exemplificar.

Então, vai ser nessa fase que você vai definir qual o tipo de requisito do seu sistema, o que ele precisa fornecer para o seu cliente.

Quais são os perfis de acesso? Vou ter diferentes grupos acessando o meu banco de dados? Preciso entender nessa fase o que realmente quero representar.

### Processo Evolutivo de Criação e Configuração

E aí, nós temos um processo evolutivo gradual de criação e configuração de um banco de dados. Preciso entender o que quero representar. Vou definir o modelo. Esse modelo vai ter as funcionalidades, a estrutura. E já pego o modelo um pouco mais geral quando falo de relacionamento e de relacional. Você vai ter um pouquinho mais para frente quando eu definir...

`⏱ 04:00`

quando eu definir muito bem esses cenários. E aí, depois dessa fase toda de modelagem, eu vou ter efetivamente a implementação.

Eu defino muito bem o que eu quero e coloco isso no modelo ou um **esquema conceitual**. A partir desse modelo, eu já sei: "Opa, essas informações são facilmente gerenciadas por um sistema relacional." Então, eu já sei que meu modelo lógico vai ser relacional. Definindo tudo certinho, eu parto para a implementação. Parece simples, mas é um pouquinho mais complexo do que isso.

### Cenários de Modelagem e a Importância dos Dados

> [!exemplo] Cenários de Modelagem e Impacto de Negócio
> Nós temos diversos cenários possíveis para modelagem.
>
> **Exemplo 1: Colaboradores**
> Imagine uma empresa onde você tem colaboradores e um tipo de interação entre eles, e você precisa persistir as informações. Os mil colaboradores geralmente estão associados a *squads* ou a departamentos. Esses departamentos têm subgrupos, subdepartamentos ou sub-squads? A partir daí, você consegue entender como modelar o cenário de colaborador.
>
> **Exemplo 2: E-commerce**
> O que você quer traduzir no seu banco de dados que está relacionado ao seu comércio eletrônico? O que é preciso mostrar para conseguir ver alguns *insights* de vendas? Por exemplo, o cliente que colocou no carrinho e não comprou, ou os clientes que mais consumiram nos últimos meses e por que eles têm uma taxa recorrente de consumo na minha plataforma. Várias informações podem ser tiradas do banco de dados.
>
> **A Importância da Área de Dados**
> Este é um dos motivos pelos quais a área de dados está crescendo agora. Os bancos de dados são utilizados nesse sentido. Se você for pegar cientistas de dados, a grande maioria utiliza massivamente `Python`, mas você também tem o `SBD` (Sistema de Banco de Dados) como a segunda tecnologia mais utilizada. Por que? É preciso persistir dados. Já falei anteriormente sobre o porquê utilizar o `SBD` ou quando não utilizar.
>
> Esses dois cenários são também contemplados pelo cientista de dados, que precisa analisar esses dados para tirar diversos *insights* que vão fomentar decisões de negócio.
>
> **Impacto nas Decisões de Negócio**
> Essas decisões vão interferir diretamente no negócio da empresa, seja um e-commerce, uma universidade, uma fábrica (uma produção de algum tipo de material, algum tipo de *commodities*, enfim, de algum produto de valor), seja um banco (área financeira), ou um sistema mais simples, como o gerenciamento de uma farmácia.
>
> Por que eu vou ter e-commerce e farmácia diferentes? Eles são cenários distintos, com particularidades e peculiaridades relacionadas ao seu contexto. O e-commerce também, ou em bibliotecas, enfim.
>
> Este é apenas um apanhado geral para mostrar quais cenários nós conseguimos modelar dados. E esses dados acabam fomentando *insights* relacionados a esses cenários e a tomada de decisão.

### Resolvendo a Modelagem: O Modelo Conceitual

Como que eu resolvo essa questão da modelagem? Eu primeiro começo com o **modelo de alto nível**, que é o **modelo conceitual**. Ali eu defino meus requisitos, questões de visualização, quem vai usar ou não, o que eu preciso ter de atributo para os meus objetos, porque dentro do meu contexto eu tenho objetos. Você pode sim fazer uma associação aí com o mundo de orientação a objetos. Eu vou comentar uma coisinha aqui.

`⏱ 08:20`

Eu vou comentar uma coisa que, embora eu vá falar mais à frente, vale a pena pontuar agora: o **Modelo de Entidade-Relacionamento** (MER), pelo menos a versão construída em 1970, não contempla a visão de orientação a objetos. Ele consegue representar muitas coisas.

Veremos mais para frente que existe um aprimoramento desse modelo que utiliza a parte de orientação a objetos. Por enquanto, falarei sobre o conceito de objeto, mas não usaremos todas as características e particularidades da orientação a objetos neste modelo.

Com o modelo conceitual de alto nível bem definido — com os objetos, suas interações (ou relacionamentos) e os tipos de interação — eu parto para o modelo lógico.

### Modelo Lógico

> [!definicao] Modelo Lógico
> Nesta fase, define-se a estrutura exata do banco de dados, escolhendo um **modelo de arquitetura de banco de dados** específico, como o relacional. O objetivo é delimitar o tipo de modelo (relacional, baseado em documento, baseado em grafo, etc.), e não um Sistema Gerenciador de Banco de Dados (SGBD) específico.

A definição do SGBD ocorre em uma fase posterior, dentro do **projeto físico**. É nesse momento que se define qual SGBD será utilizado, cria-se o esquema e usa-se `SQL` para inserir as instâncias, ou seja, os valores relacionados a atributos e entidades.

Este é o caminho que percorremos, desde a concepção de um banco de dados que represente o meu contexto e o meu mundo, até a implementação propriamente dita.

## Relacionado

- [[modelagem-de-dados-etapas-caracteristicas-do-sgbd-e-conceito-de-mundo-fechado]]
- [[algebra-relacional-sgbd-e-ciclo-de-vida-do-projeto-de-banco-de-dados]]
- [[sgbds-historico-e-modelos-de-dados]]
- [[sgbd-etapas-estrutura-e-fases]]
