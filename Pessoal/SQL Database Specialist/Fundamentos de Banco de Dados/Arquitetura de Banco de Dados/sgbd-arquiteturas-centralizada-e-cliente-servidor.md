---
titulo: "SGBD: Arquiteturas Centralizada e Cliente-Servidor"
tags: [sgbd, banco-de-dados, arquitetura, sistema, conceitos, ferramentas]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 8
conceitos: [Arquitetura Física Centralizada, Mainframe, Arquitetura Cliente-Servidor, Stateless, ODBC driver, API (Application Programming Interface), Arquitetura Two-Tier, Arquitetura Three-Tier]
---

# SGBD: Arquiteturas Centralizada e Cliente-Servidor

> [!resumo] Do que se trata
> Esta aula explora as diferentes arquiteturas de Sistemas de Gerenciamento de Banco de Dados (SGBD), começando pelo modelo físico centralizado e evoluindo para a arquitetura cliente-servidor. Ela detalha o conceito de comunicação stateless e o acesso ao SGBD via ODBC e API. Por fim, a aula diferencia as arquiteturas cliente-servidor two-tier e three-tier, explicando como cada uma organiza o acesso às informações.

## Para lembrar

- **A Arquitetura Física Centralizada é um modelo antigo onde todos os recursos (hardware, sistema operacional, SGBD e aplicações) estão em uma única máquina, acessada via terminal.**
- **A arquitetura cliente-servidor é caracterizada pelo modo stateless, onde cada lado da comunicação não guarda o estado do outro lado, solicitando informações se necessário.**
- **Uma API (Application Programming Interface) é um componente intermediário que permite a solicitação e o retorno de informações entre uma linguagem de programação e o banco de dados.**
- **Na arquitetura two-tier (duas camadas), os componentes estão distribuídos em seus servidores específicos, com comunicação direta entre cliente e servidor via rede.**
- **A arquitetura three-tier (três camadas) é uma evolução que organiza o acesso às informações em três níveis: servidor do banco de dados, aplicação do servidor e cliente.**

## O que esta nota responde

- Quais são as características da arquitetura física centralizada e como ela difere da arquitetura cliente-servidor?
- O que significa o modo "stateless" em uma arquitetura cliente-servidor?
- Como as arquiteturas cliente-servidor two-tier e three-tier organizam o acesso aos dados?

## Conceitos

**Arquitetura Física Centralizada** · **Mainframe** · **Arquitetura Cliente-Servidor** · **Stateless** · **ODBC driver** · **API (Application Programming Interface)** · **Arquitetura Two-Tier** · **Arquitetura Three-Tier**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Arquiteturas Centralizada e Cliente-Servidor | ▪▪ |
| `04:40` | Acesso SGBD e Arquiteturas Multi-Tier | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Arquitetura Física Centralizada** | É o modelo antigo, onde existiam grandes mainframes e a tecnologia era muito cara. Nela, todos os recursos (hardware, sistema operacional, SGBD, compiladores, editores de texto, terminal e aplicações de programa) estão centralizados em uma única máquina. |
| **Stateless** | É uma característica da arquitetura cliente-servidor onde cada lado da comunicação não guarda o estado do outro lado, do seu par. O cliente não guarda o estado do servidor, e o servidor não guarda o estado do cliente. Se for necessário, informações são solicitadas ou processadas (por exemplo, dentro de `Cookies`) para identificar o cliente. |
| **API (Application Programming Interface)** | É um componente intermediário que permite a solicitação e o retorno de informações. Através de uma linguagem de programação, uma API pode ser criada para acessar um banco de dados, solicitando as informações necessárias e retornando os dados relacionados à requisição. |

## Teste-se

<details><summary>Qual a principal característica da arquitetura física centralizada?</summary>

Na arquitetura física centralizada, todos os recursos (hardware, sistema operacional, SGBD, compiladores, editores, terminal e aplicações) estão em uma única máquina, remetendo à época dos grandes mainframes.

</details>

<details><summary>O que significa a característica 'stateless' na arquitetura cliente-servidor?</summary>

'Stateless' significa que cada lado da comunicação (cliente e servidor) não guarda o estado do seu par. Se necessário, informações são solicitadas ou processadas (ex: em Cookies) para identificar o cliente.

</details>

<details><summary>Qual o papel de uma API no acesso a um SGBD?</summary>

Uma API (Application Programming Interface) atua como um componente intermediário. Ela permite que uma linguagem de programação solicite informações ao banco de dados e retorne os dados relacionados à requisição.

</details>

<details><summary>Quais são as três camadas da arquitetura `3-tier`?</summary>

As três camadas da arquitetura `3-tier` são: o servidor do banco de dados (SGBD), a aplicação do servidor (backend ou web server) e o frontend.

</details>

<details><summary>Cite dois tipos de clientes que podem existir em um cenário de arquitetura `two-tier`.</summary>

Em um cenário `two-tier`, podem existir clientes *diskless* (não armazenam dados localmente) e clientes com disco (possuem armazenamento associado).

</details>

<details><summary>Como era o acesso ao banco de dados na arquitetura física centralizada?</summary>

O acesso era feito via terminal, onde se abria um monitor ou display e se conectava ao controle do display via rede para puxar informações do SGBD.

</details>

## Conteúdo

`⏱ 00:00`

Provavelmente você já ouviu falar do modelo cliente-servidor, da arquitetura cliente-servidor. Eu vou falar um pouquinho sobre ela e depois sobre as classificações de um SGPD. Uma arquitetura de um STBD pode ser centralizada ou distribuída.

### Arquitetura Física Centralizada

Eu vou começar pelo modelo de uma **arquitetura física centralizada**, que era o modelo antigo, onde existiam aqueles grandes mainframes, onde a tecnologia era uma coisa muito cara ainda. Aqui nessa figura nós temos a parte do hardware: o sistema operacional. Hardware, firmware, memória, CPU, o controller, o I/O, devices, o disco. Enfim, isso aqui é o sistema operacional que acaba sendo base para poder estar instalando o seu software, o seu SGBD. Por exemplo, você vai ter uma série de instruções diferentes para estar instalando o `MySQL` no `Windows` ou para estar instalando ele no `Linux`, como a gente vai fazer aqui.

Aqui então é o SO. E ali no software, no nosso SGBD, não é apenas o SGBD. O SGBD é um componentezinho aqui. Então nós temos os compiladores, os editores de texto, o terminal e as aplicações de programa. Isso aqui tudo numa mesma máquina.

A gente começa a perceber: como é que era o acesso antes? Via terminal. Ou seja, eu abria o monitor, um display qualquer, acessava o banco, terminal display control, acessava essa parte de controle do display via rede. Eu estava me conectando aqui. Se fosse via, teria que ser via `SSH` para manter a confiabilidade, a segurança dos pacotes, a criptografia. Vamos abstrair essa parte. Então eu estou me conectando aqui para conseguir puxar informações do meu sistema de gerenciamento de banco de dados. E aí eu tenho uma série aqui de outros softwares que estão associados ao meu contexto.

> [!definicao] Arquitetura Física Centralizada
> É o modelo antigo, onde existiam grandes mainframes e a tecnologia era muito cara. Nela, todos os recursos (hardware, sistema operacional, SGBD, compiladores, editores de texto, terminal e aplicações de programa) estão centralizados em uma única máquina.

Essa é uma arquitetura física onde nossos recursos estão todos centralizados em uma única máquina. Então, no mesmo SO, está rodando um STBD, o compilador e outros programas. Isso remete àquela época dos grandes mainframes, onde nós acessávamos via terminal.

### Arquitetura Cliente-Servidor

Com a evolução, com a democratização da tecnologia, surgiram os PCs, os personal computers. E aí começamos a ter uma **arquitetura cliente-servidor**, uma arquitetura onde cada lado se preocupa com apenas a sua função, com apenas o seu papel.

Vamos pensar o seguinte: o cliente se preocupa apenas em realizar a sua requisição. Não importa o que o servidor vai fazer para atendê-la. Por sua vez, o servidor recebe a requisição, olha aquela requisição e envia a resposta. Não importa se é a primeira vez, se é a nona vez que o cliente está enviando aquela informação.

Uma característica desse tipo de arquitetura é o modo **stateless**.

> [!definicao] Stateless
> É uma característica da arquitetura cliente-servidor onde cada lado da comunicação não guarda o estado do outro lado, do seu par. O cliente não guarda o estado do servidor, e o servidor não guarda o estado do cliente. Se for necessário, informações são solicitadas ou processadas (por exemplo, dentro de `Cookies`) para identificar o cliente.

Nós temos um provedor de serviços dentro do servidor. O servidor funciona dessa maneira, mas ele vai fornecer serviços.

> [!exemplo] Servidor como provedor de serviços
> Em uma arquitetura cliente-servidor, o servidor funciona como um provedor de serviços. Por exemplo, em uma rede, pode-se ter:
> - Um servidor de impressão
> - Um servidor de arquivos
> - Um servidor do SGBD
> Cada um desses servidores é separado, com sua própria função, e todos estão conectados pela rede.

Quando a gente pensa em arquitetura, a gente pensa o seguinte: nós temos o SGBD,

`⏱ 04:40`

nós temos o `SGBD` instalado, seja no meu computador (aqui coloquei o celular, mas mais para o `SQLite`), ou, pensando no servidor, no nosso computador, no PCzinho. Eu preciso de um `ODBC driver` relacionado ao meu `SGBD`.

### Acesso ao SGBD via ODBC e API

A partir daí, eu vou utilizar. Mas eu posso utilizar uma linguagem de programação que vai criar uma **API** para mim. Eu vou criar uma `API` através dessa linguagem de programação, e ela vai acessar o banco de dados.

> [!definicao] API (Application Programming Interface)
> É um componente intermediário que permite a solicitação e o retorno de informações. Através de uma linguagem de programação, uma API pode ser criada para acessar um banco de dados, solicitando as informações necessárias e retornando os dados relacionados à requisição.

Ela vai ser o componente intermediário dessa situação, onde eu vou solicitar via `API` as informações que eu preciso. Por sua vez, essa `API` vai retornar as informações relacionadas à requisição.

A gente consegue perceber que esse tipo de coisa acontece nesse modelo de rede.

### Arquitetura Cliente-Servidor: Two-Tier

Já na arquitetura lógica e física do cliente e servidor, nós temos algo chamado **`two-tier`**. Temos um cenário onde todos estão distribuídos, cada um em seu quadrado, cada um em seu servidor específico.

> [!exemplo] Cenários da Arquitetura Two-Tier
> Na arquitetura `two-tier` (duas camadas), os componentes estão distribuídos, cada um em seu servidor específico. A comunicação entre eles é realizada via rede, garantindo simplicidade e compatibilidade com sistemas do mundo real, visto que dificilmente você vai encontrar algum sistema que seja totalmente centralizado.
> >
> Podemos ter diferentes tipos de clientes neste cenário:
> >
> | Tipo de Cliente/Servidor | Características |
> | :----------------------- | :-------------- |
> | **Cliente *diskless***   | Não possui disco, não armazena dados. Apenas acessa e lê. Pode inserir, mas não pode gravar dados localmente. |
> | **Cliente com disco**    | Possui uma quantidade X de armazenamento associada a ele. |
> | **Cybertrace**           | É um servidor dedicado, com uma quantidade X de armazenamento. |
> | **Cliente e Servidor**   | Atua com ambos os papéis simultaneamente, sendo cliente e servidor ao mesmo tempo. |

Você vai conseguir encontrar desse jeito, sim, arquitetura cliente-servidor, onde a maioria das `APIs` e a maioria das ferramentas estão sendo criadas dessa forma.

### Arquitetura Cliente-Servidor: Three-Tier

Podemos entrar em uma nova seara, onde a arquitetura lógica cliente-servidor está relacionada, então, a **`3-tier`**, a uma arquitetura de três camadas.

> [!exemplo] Arquitetura Three-Tier
> A arquitetura `3-tier` (três camadas) é uma evolução da arquitetura cliente-servidor, que organiza o acesso às informações em diferentes níveis.
> >
> As três camadas são:
> - O servidor do banco de dados (`SGBD`).
> - A aplicação do servidor (ou então no `web server`), que é a aplicação do `back-end`.
> - E o `front-end`.
> >
> Essa seria a ideia para acessar informações através de níveis diferentes, seja via interface que acessa a aplicação, e aplicação que acessa o banco de dados para recuperar as informações.

## Relacionado

- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-atores-indiretos-e-requisitos-operacionais]]
- [[../Introdução a Banco de Dados/sgbds-os-mais-utilizados-no-mercado]]
- [[sgbd-componentes-usuarios-e-ferramentas-de-gerenciamento]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-cenarios-de-nao-utilizacao-e-alternativas]]
