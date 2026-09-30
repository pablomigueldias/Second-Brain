---
titulo: "SGBD: Interfaces, Tipos e Usuários"
tags: [sgbd, banco-de-dados, interfaces, usuarios, ferramentas, conceitos, sql]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 15
conceitos: [Interfaces, WebClient, Mobile, Forms, GUI (Graphical User Interface), NLE (Natural Language Interface), Usuário Ingênuo (Naive User), DBA (Database Administrator)]
---

# SGBD: Interfaces, Tipos e Usuários

> [!resumo] Do que se trata
> Esta aula define interfaces como mecanismos de consulta e manipulação de dados em SGBDs, explorando diversos tipos como WebClient, Mobile, Forms, GUI e NLE. Ela detalha como cada interface permite a interação com o banco de dados, desde menus e formulários até comandos de voz. A aula também diferencia as operações realizadas por usuários ingênuos (naive) e o papel dos profissionais de banco de dados.

## Para lembrar

- **Interfaces são mecanismos de consulta, consumo, inserção e manipulação de dados em um SGBD, utilizadas por VAs, designers e end-users.**
- **O WebClient é uma interface autodescritiva acessada via web browser, que utiliza menus e listas para navegação e requisições ao SGBD, como o phpMyAdmin.**
- **Formulários (Forms) são interfaces para entrada de novos dados, frequentemente usados por usuários ingênuos, onde a submissão de informações pode ser validada pela aplicação ou pelo banco de dados.**
- **A GUI (Graphical User Interface) é uma interface gráfica que permite ao usuário navegar por diagramas com requisitos embarcados de queries, enquanto a NLE (Natural Language Interface) possibilita interação por comandos de voz ou texto natural.**
- **Usuários ingênuos (naive users) realizam operações repetitivas e dentro de um mesmo contexto, como verificar extrato ou saldo, com queries pré-programadas para minimizar erros.**

## O que esta nota responde

- O que são interfaces em um SGBD e quais são seus principais objetivos?
- Quais são os diferentes tipos de interfaces para SGBDs e suas características de uso?
- Como as interfaces de linguagem natural (NLE) e as interfaces gráficas (GUI) facilitam a interação com bancos de dados?

## Conceitos

**Interfaces** · **WebClient** · **Mobile** · **Forms** · **GUI (Graphical User Interface)** · **NLE (Natural Language Interface)** · **Usuário Ingênuo (Naive User)** · **DBA (Database Administrator)**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Interfaces: WebClient, Mobile, Forms | ▪▪ |
| `04:20` | Usuários, GUI e NLE | ▪▪ |
| `08:40` | NLE, Keyword e Speech I/O | ▪▪ |
| `13:00` | Usuários Naive e DBA | ▪▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Interfaces** | Mecanismos de consulta, consumo, inserção e qualquer tipo de manipulação ou articulação relacionada aos dados de um SGBD. |
| **Naive users** | Aqueles que interagem com o sistema de forma mais simples, sem conhecimento técnico aprofundado. |
| **Parametric users** | Usuários que geralmente estão consultando ou acessando a organização do banco de dados através de transações pré-definidas. |
| **GUI (Graphical User Interface)** | Uma interface gráfica de usuário disposta em forma de diagramas. O usuário navega através de um diagrama que possui requisitos embarcados de queries que manipulam o banco de dados. A interação pode ser feita por meio de menus ou formulários, que se configuram como parte desse diagrama, permitindo o acesso às informações. Nesse contexto, a API é esse diagrama. |
| **NLE (Natural Language Interface)** | Uma abordagem que utiliza um intérprete, um agente com inteligência artificial, para acessar informações e retorná-las ao usuário, permitindo a interação por meio da linguagem natural. |
| **Papel do DBA (Database Administrator)** | O DBA e sua equipe estão relacionados a comandos de nível de privilégio, que envolvem: definir a estrutura do banco de dados; definir e modificar esquemas, se necessário; definir índices e cache; realizar otimizações de segurança; executar diversos comandos relacionados ao desempenho do sistema, visando entregar a melhor experiência possível ao usuário. |

## Teste-se

<details><summary>O que são Interfaces em um SGBD e quem as utiliza?</summary>

Interfaces são mecanismos para consulta, consumo, inserção e manipulação de dados em um SGBD. Elas são utilizadas por VAs, designers e end-users.

</details>

<details><summary>Qual a principal diferença de escopo entre interfaces WebClient e Mobile?</summary>

Interfaces WebClient geralmente possuem um escopo mais amplo. Já as interfaces Mobile são geralmente mais reduzidas, limitadas pelo aplicativo.

</details>

<details><summary>Qual o propósito principal das interfaces Forms e a que tipo de usuário elas são muito relacionadas?</summary>

Forms são interfaces para entrada de novos dados. Elas são muito relacionadas a usuários 'naive' (ingênuos) ou 'parametric users'.

</details>

<details><summary>Como a NLE (Natural Language Interface) processa um comando como 'Alexa, toque Piano Guys'?</summary>

A NLE utiliza um intérprete ou agente de IA para analisar a frase, identificar palavras reservadas (como 'Alexa', 'toque') e o conteúdo ('Piano Guys'), e então realizar a busca e ação solicitada.

</details>

<details><summary>Cite três responsabilidades do DBA e sua equipe.</summary>

O DBA e sua equipe definem a estrutura do banco de dados, modificam esquemas, definem índices e cache, e realizam otimizações de segurança e desempenho.

</details>

## Conteúdo

`⏱ 00:00`

> [!definicao] Interfaces
> **Interfaces** são mecanismos de consulta, consumo, inserção e qualquer tipo de manipulação ou articulação relacionada aos dados de um SGBD. Elas são utilizadas por VAs, designers e end-users.

### WebClient

O `WebClient` é um tipo de interface autodescritiva. Toda vez que você acessa um `web browser`, você provavelmente estará acessando um SGBD através de uma API web, a menos que os dados estejam "mocados" e estaticamente alocados no *front-end*.

> [!exemplo] Características do WebClient
> A disposição da consulta, das requisições e da estrutura utiliza menus. Conseguimos extrapolar e abrir em formato de listas, navegando como em uma estrutura de "caixinhas" ou módulos. A cada "caixinha" clicada, abre-se um subconjunto de informações, uma lista ou sublista, onde cada item está associado a um comando. Assim, é possível navegar pela lista e fazer requisições ao SGBD através do menu.

Um adendo: ao pensar em `WebClient`, podemos estar falando também de ferramentas como o `phpMyAdmin`. Essa é uma interface web, uma API web, para acessar o banco de dados por um profissional ou especialista em banco de dados, não necessariamente através de uma interface gráfica amigável a partir do `web browser`.

### Mobile

Outro cenário é o `mobile`, ou seja, aplicativos de celular. Através deles, conseguimos acessar diversos dados por meio de um menu limitado pelo aplicativo.

| Característica | WebClient                               | Mobile                                  |
| :------------- | :-------------------------------------- | :-------------------------------------- |
| Limitação      | Limitado pelo produto fornecido pela API web | Limitado pelo aplicativo                |
| Escopo         | Geralmente mais amplo                   | Geralmente reduzido                     |
| Exemplos       | `phpMyAdmin`                            | Aplicativos de banco, reserva de hotel (`Booking`) |

A partir desses aplicativos, que atuam como interfaces, é possível acessar o banco de dados ou puxar diversas informações através de botões e listas.

### Forms

`Forms` (formulários) são interfaces para entrada de novos dados, muito relacionados a usuários "naive" (embora `WebClient` e `Mobile` também possam ser).

Dentro desses formulários, há vários campos associados a espaços específicos, onde você submete suas informações. Como provavelmente se trata de uma API `HTTP` ou `REST`, são utilizados métodos `HTTP` para submeter essas informações ao servidor. Consequentemente, essas informações não estão sendo persistidas no banco de dados neste momento.

> [!exemplo] Submissão e Validação de Formulários
> Uma vez que as informações são preenchidas em cada campo específico e obrigatório, você pode submeter o formulário.
> >
> Se houver algum erro, o formulário informará. Por exemplo:
> - "Está faltando tal campo para preencher."
> - "Preencha todos os campos obrigatórios."
> >
> Um asterisco em vermelho geralmente indica os campos obrigatórios. Se um campo estiver configurado no banco de dados como "não nulo", ou seja, não aceita informações...

`⏱ 04:20`

não aceito **informações** que vêm no banco de dados como nulo. CPF, por exemplo, não pode ser nulo. Se a pessoa não inserir o CPF, isso pode ser tratado pela aplicação diretamente ou pelo banco de dados. Na verdade, é mais fácil tratar pela aplicação. Pense assim: se já sabemos que o banco de dados não aceita nulo, é mais fácil verificar na aplicação e já inserir de uma vez, do que esperar, tentar inserir no banco de dados, retornar um erro e ter que tratar este erro.

### Preenchimento de Formulários
O preenchimento pode ser total ou parcial, dependendo muito de como o Forms foi construído e dos requisitos que você precisa passar.

Essa situação é muito voltada para os **naive users** (usuários ingênuos) ou **parametric users**.

> [!definicao] Tipos de Usuários
> **Naive users** (usuários ingênuos) são aqueles que interagem com o sistema de forma mais simples, sem conhecimento técnico aprofundado.
> **Parametric users** são usuários que geralmente estão consultando ou acessando a organização do banco de dados através de transações pré-definidas.

Essas transações, muitas vezes chamadas de "tuneladas", são programadas para serem enviadas de uma aplicação diretamente para o SGPD (Sistema Gerenciador de Banco de Dados).

### Submissão de Dados e Transações
Nesse sentido, estou utilizando o método `POST` da HTTP para submeter as informações ao servidor. O servidor tratará essas informações e, posteriormente, as inserirá no banco de dados.

A ideia é que, dentro da questão das transações, a possibilidade de erro é mínima, visto que as `queries` (transações) foram programadas pelo profissional de desenvolvimento para que o usuário ingênuo (`naive user`) pudesse acessar o banco de dados.

Se houver algum erro, ele estará na aplicação. Se houver um erro recorrente decorrente desse tipo de situação, provavelmente foi programado errado, houve um equívoco, ou então o servidor está fora do ar. Isso pode acontecer, e existe outro cenário também.

### GUI (Graphical User Interface)
Continuando, temos a **GUI**, que é a *Graphical User Interface* (interface gráfica de usuário).

> [!definicao] GUI (Graphical User Interface)
> A **GUI** é uma interface gráfica de usuário disposta em forma de diagramas.
> Em uma GUI, o usuário navega através de um diagrama que possui requisitos embarcados de `queries` que manipulam o banco de dados.
> A interação pode ser feita por meio de menus ou formulários, que se configuram como parte desse diagrama, permitindo o acesso às informações.
> Nesse contexto, a API é esse diagrama.

### NLE (Natural Language Interface)
A **NLE**, *Natural Language Interface* (interface de linguagem natural), está crescendo em utilização. Essa abordagem utiliza um intérprete, um agente com inteligência artificial, para acessar informações e retorná-las ao usuário.

> [!definicao] NLE (Natural Language Interface)
> A **NLE** é uma abordagem que utiliza um intérprete, um agente com inteligência artificial, para acessar informações e retorná-las ao usuário, permitindo a interação por meio da linguagem natural.

> [!exemplo] Cenário da Alexa
> Suponha que você diga: "Alexa, toque Piano Guys."
> A Alexa começará a analisar sua frase e o comando solicitado.
> Ela interpretará: "Alexa está me solicitando uma requisição."
> Em seguida, ela analisará "Toque Piano Guys". "Toque" está relacionado a uma chamada para tocar música. "Piano Guys" é provavelmente um álbum, artista ou músico.
> A partir do contexto que ela possui e de sua base de dados, ela interpretará o comando e realizará a busca solicitada.

`⏱ 08:40`

ela vai interpretar o meu comando e daí realizar a busca que eu solicitei.

> [!exemplo] Interpretação de comandos da Alexa
> Se, ao buscar no Spotify, a Alexa encontra "Piano Guys" e o comando foi "tocar", ela já coloca o play.
> Se você perguntar: `Alexa, procure Fundo do Mar no YouTube`, ela vai procurar e mostrar uma lista.
> Se você disser: `Alexa, coloque Fundo do Mar no YouTube`, ela vai tocar algum vídeo que encontrar sobre Fundo do Mar.

Esse tipo de contexto e comando está crescendo muito em utilização, especialmente ao se empregar **agentes** para intermediar a comunicação entre você e a aplicação. A arquitetura envolve: você, o agente, a aplicação e o *back-end*, onde estão o servidor e o seu SGBD.

A busca é feita a partir de uma **palavra reservada** e do conteúdo associado ao comando. Por exemplo, `Alexa` é uma palavra reservada. No comando `Alexa, toque Piano Guys`, `toque` também é uma palavra reservada. O sistema analisa o conteúdo (`Piano Guys`) e o comando (`toque`), e a partir dessa análise, retorna o que encontrou na requisição.

### Pesquisa por Palavra-Chave (Keyword)

Existe também a pesquisa por **keyword** (palavra-chave). A partir de uma palavra-chave, inicia-se uma pesquisa para verificar se há um *match* parcial ou total. Isso está relacionado a conceitos como índices e *hash functions*, indicando que essa parte se conecta mais ao modelo físico do SGBD.

### Speech Input e Output

O **Speech Input e Output** significa que a solicitação é feita por *speech* (fala) e o retorno também é por *speech*. Ou seja, você solicita algo usando linguagem natural, e a resposta é retornada a você também por linguagem natural, provavelmente com a ajuda de um agente.

Esse contexto, embora limitado, define o *speech* como *input*. A partir desse *input*, o sistema procura o assunto e os dados relacionados. Na hora de retornar a resposta ao usuário, ela é tratada e enviada novamente como *speech*.

> [!exemplo] Google e Speech Input/Output
> Ao usar a ferramenta de busca do Google com o microfone para procurar algo, como `tabela periódica`, o sistema retorna o resultado. O Google, nesse cenário, pega o primeiro resultado e começa a "ler" o que está escrito para você, utilizando *speech*. Este é um cenário similar ao de *Speech Input* e *Speech Output*.

### Interfaces: Naive e DBA

O **Naive** (usuário ingênuo) está muito associado às operações repetitivas que ele pode fazer. Por ser "ingênuo", ele geralmente acessa informações dentro do mesmo contexto.

> [!exemplo] Operações do usuário Naive no banco
> Ao usar o `OPP` do banco, as operações mais comuns que um usuário Naive realiza são:
> - Ver o extrato da conta.
> - Ver o extrato da fatura do cartão.
> - Verificar se há alguma pendência para pagar.
>
> Há, portanto, um conjunto de operações mais comuns e repetitivas.

`⏱ 13:00`

Essas operações comuns se aplicam ao contexto de um **usuário ingênuo**. Você acaba tendo uma repetição de operações. Toda vez que você entra na sua conta, verifica o seu saldo. Isso é um fato. Você sempre vai verificar o seu saldo.

### Operações Repetitivas do Usuário Ingênuo

> [!exemplo] Operações Repetitivas de Usuário Ingênuo
> Se você observar o aplicativo do seu banco, provavelmente há um atalho logo na página inicial para exibir o seu saldo e os lançamentos futuros. Isso ocorre porque é sabido que, nesse contexto, verificar o saldo e os lançamentos são operações repetitivas que o **usuário ingênuo** geralmente realiza, pois estão diretamente relacionadas à sua rotina.

### O Papel do DBA

Agora, vamos abordar o **DBA** e sua equipe.

> [!definicao] Papel do DBA (Database Administrator)
> O DBA e sua equipe estão relacionados a comandos de nível de privilégio, que envolvem:
> - Definir a estrutura do banco de dados.
> - Definir e modificar esquemas, se necessário.
> - Definir índices e cache.
> - Realizar otimizações de segurança.
> - Executar diversos comandos relacionados ao desempenho do sistema, visando entregar a melhor experiência possível ao usuário.
>
> Exemplos de comandos específicos incluem:
> - `definir índices`
> - `criar um novo BD` (para mapear outro contexto)
> - `criar views`
> - `modificar um esquema`

O DBA e sua equipe estão, portanto, relacionados a um contexto de acesso mais privilegiado ao sistema, caracterizando um perfil especialista. Isso difere dos cenários de **usuário ingênuo**, que têm acesso mais restrito.

## Relacionado

- [[sgbd-vantagens-otimizacao-e-integridade-dos-dados]]
- [[sgbd-linguagens-interfaces-e-ambientes]]
- [[sgbd-natureza-autodescritiva-esquema-e-catalogo]]
- [[sgbd-atores-tipos-de-usuarios-e-finalidade]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `RESTful → APIs REST`
