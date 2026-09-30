---
titulo: "SGBD: Arquitetura de Três Esquemas e Isolamento"
tags: [sgbd, banco-de-dados, conceitos, estudo, otimizacao, modelagem-de-dados, sistema]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [Arquitetura de Três Esquemas, Isolamento, Esquema Interno (internal level), Modelo Conceitual, Esquema Externo (external level), Views, Modelo Lógico, Modelo Físico]
---

# SGBD: Arquitetura de Três Esquemas e Isolamento

> [!resumo] Do que se trata
> A arquitetura de três esquemas define as funções de cada nível (interno, conceitual e externo) dentro de um SGBD, promovendo o isolamento entre dados e programas. Este isolamento garante que modificações em um esquema não afetem os demais, facilitando a manutenção e otimização do sistema. Embora não seja explicitamente suportada pelos SGBDs atuais, essa arquitetura é fundamental para entender a separação entre as camadas física e lógica e as visões personalizadas dos usuários.

## Para lembrar

- **A Arquitetura de Três Esquemas define a função de cada esquema (interno, conceitual e externo) dentro de um SGBD, suportada por isolamento entre dados e programa, catálogo e visões.**
- **O objetivo do isolamento é garantir que uma modificação em um esquema não influencie o esquema subsequente, otimizando a manutenção do SGBD.**
- **O Esquema Interno (`internal level`) é o nível mais baixo, atrelado ao modelo de dados físico, definindo a disposição de arquivos, distribuição e criação de índices.**
- **O Modelo Conceitual define entidades, operações de usuários, `constraints` e relacionamentos, servindo como base para as visões dos dados.**
- **`Views` são representações restritas dos dados, definidas em projetos de alto nível, que personalizam o acesso às informações para diferentes grupos de usuários.**

## O que esta nota responde

- O que é a Arquitetura de Três Esquemas e quais características a suportam?
- Qual o principal objetivo do isolamento em um SGBD e como ele é alcançado entre os esquemas?
- Como as `Views` contribuem para a personalização e restrição do acesso aos dados para diferentes usuários?

## Conceitos

**Arquitetura de Três Esquemas** · **Isolamento** · **Esquema Interno (internal level)** · **Modelo Conceitual** · **Esquema Externo (external level)** · **Views** · **Modelo Lógico** · **Modelo Físico**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Arquitetura Três Esquemas e Isolamento | ▪▪ |
| `04:40` | Isolamento, Visões e Suporte SGBD | ▪▪ |
| `09:00` | Modelos Lógico, Físico e Otimização | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Arquitetura de Três Esquemas** | Possui o papel de conseguir definir qual é a função de cada esquema dentro de um SGBD. |
| **Isolamento** | O objetivo é promover o isolamento de tal forma que uma modificação que ocorra em um determinado esquema não influencie o seu esquema subsequente. Isso permite que a manutenção do SGBD continue tranquila e mais otimizada. |
| **Esquema Interno (`internal level`)** | É o nível mais interno de modelos relacionados a dados físicos. Seu objetivo é definir a disposição dos arquivos dentro do sistema, a distribuição deles, a criação de índices, operações de `split` ou `merge` entre arquivos. Engloba toda a parte que dá as diretrizes relacionadas a como os arquivos serão persistidos, estando atrelado ao modelo de dados físico. |
| **Views** | Dentro do modelo conceitual, as **views** são definidas em projetos de alto nível. Elas permitem criar uma representação dos dados mais restrita, de acordo com cada grupo de usuário, baseando-se nas informações que cada grupo precisa ter acesso. |
| **Modelo Lógico** | Associado à visão do usuário e ao modelo conceitual. É uma abstração, uma ideia do que se quer representar dos dados. |
| **Modelo Físico** | Representação dos dados criada a partir de uma série de requisitos. Relacionado à definição em `SQL` e ao ambiente de criação do banco de dados. Em nível mais baixo, envolve índices e cache para performance. |

## Pegadinhas

- A Arquitetura de Três Esquemas não é explicitamente suportada pelos SGBDs atuais; extensões são usadas para simular o isolamento.
- O isolamento físico é mais fácil de ser alcançado que o isolamento lógico, embora o lógico não seja impossível, apenas mais difícil.

## Teste-se

<details><summary>Quais são as três características que dão suporte à Arquitetura de Três Esquemas?</summary>

As características são: isolamento entre dados e programa, catálogo e vírus.

</details>

<details><summary>Qual o principal objetivo do isolamento na Arquitetura de Três Esquemas?</summary>

O objetivo é que uma modificação em um esquema não influencie o esquema subsequente, permitindo manutenção tranquila e otimizada do SGBD.

</details>

<details><summary>Qual a função do Esquema Interno (`internal level`)?</summary>

Ele define a disposição e distribuição dos arquivos, criação de índices e operações de `split` ou `merge`, atrelado ao modelo de dados físico.

</details>

<details><summary>Como as `VIEW`s contribuem para a visão do usuário na camada lógica externa?</summary>

As `VIEW`s permitem restringir e personalizar informações, otimizando a busca e exibição dos dados de acordo com o que cada grupo de usuário precisa acessar.

</details>

<details><summary>Por que a Arquitetura de Três Esquemas é utilizada para fins de estudo, mesmo não sendo totalmente suportada pelos SGBDs atuais?</summary>

Ela é usada para que se consiga entender o papel do isolamento entre cada camada, mesmo que os SGBDs atuais usem extensões para simular esse isolamento.

</details>

<details><summary>Qual a diferença de dificuldade entre alcançar o isolamento físico e o isolamento lógico?</summary>

O isolamento físico é mais fácil de ser alcançado do que o isolamento lógico, embora o isolamento lógico não seja impossível, apenas mais difícil.

</details>

## Conteúdo

`⏱ 00:00`

### Arquitetura de Três Esquemas

Agora, a gente vai falar da **Arquitetura de Três Esquemas**. O que é isso?

Primeiramente, existem três características que dão suporte a essa arquitetura. As características que o STB possui são:
- isolamento entre dados e programa;
- catálogo;
- vírus.

Elas vão determinar os esquemas relacionados a essa arquitetura de três esquemas.

> [!definicao] Arquitetura de Três Esquemas
> Possui o papel de conseguir definir qual é a função de cada esquema dentro de um SGBD.

Esse tipo de arquitetura não é explicitamente suportado pelo STBD, havendo a necessidade de uma extensão. Mas o intuito aqui é conversar justamente sobre o **isolamento** que ela proporciona e dissertar sobre essas questões, o que acaba influenciando em quê.

> [!definicao] Isolamento
> O objetivo é promover o isolamento de tal forma que uma modificação que ocorra em um determinado esquema não influencie o seu esquema subsequente. Isso permite que a manutenção do SGBD continue tranquila e mais otimizada.

A gente consegue já definir uma separação, pelo menos, entre a aplicação do usuário (a parte mais externa) e a parte física já relacionada ao SGBD. Então, a parte física e outras partes estão relacionadas ao SGBD, enquanto a aplicação do usuário está relacionada à parte mais externa.

A gente já consegue entender que o SGBD acaba fornecendo vias de consumo para os dados que são persistidos através das aplicações.

Comentando um pouco sobre a figura: o `internal level`, que é o nível mais interno dessa arquitetura, está associado à parte de armazenamento, à parte física do próprio SGBD. A parte conceitual carrega o esquema conceitual e o mapeamento entre o interno e o conceitual. Da mesma forma, existe o mapeamento entre o conceitual e o externo, onde nós temos a camada da arquitetura mais associada, diretamente ligada, à aplicação do usuário.

A gente começa pelo esquema de baixo nível, o nível mais interno de modelos relacionados a dados físicos.

> [!definicao] Esquema Interno (`internal level`)
> É o nível mais interno de modelos relacionados a dados físicos. Seu objetivo é definir a disposição dos arquivos dentro do sistema, a distribuição deles, a criação de índices, operações de `split` ou `merge` entre arquivos. Engloba toda a parte que dá as diretrizes relacionadas a como os arquivos serão persistidos, estando atrelado ao modelo de dados físico.

O **modelo conceitual** já está relacionado ao modelo de implementação, onde define as entidades, as operações de usuários, `constraints` e relacionamentos. O intuito aqui é que um esteja separado do outro, de maneira que essa parte não interfira no entendimento de construção do esquema conceitual.

Você consegue visualizar perfeitamente como esse isolamento seria alcançado. Por quê? A maneira com que o arquivo está sendo persistido não vai influenciar realmente no modelo de implementação, onde são definidas as operações de usuários, relacionamentos, as regras e as entidades. Isso ocorre porque essas são operações em cima do conjunto de dados, e não especificamente sobre como aqueles dados serão acessados.

`⏱ 04:40`

e não especificamente como que eu vou acessar aqueles dados. A questão é como eu persisto e como eu acesso, pois as operações são em cima.

Se eu tenho uma determinada entidade e algumas *constraints* relacionadas a ela, sei que aquelas regras estão gerenciando a entidade. Independentemente de como a entidade está organizada em termos físicos, ela pode estar dispersa na memória, onde consigo procurar informações a partir de uma árvore de busca, por exemplo.

Já o **esquema conceitual**, que está entre o modelo interno e uma camada externa diretamente ligada à experiência do usuário, precisa de um mapeamento. É preciso mapear do modelo físico para o conceitual e manter uma estrutura que sirva de base no modelo físico. Ao mesmo tempo, essa estrutura será base também para os acessos dos usuários.

Podemos fazer um paralelo com o modelo relacional. Já que estou definindo entidade, relacionamento e *constraints*, sei que é o modelo relacional que está ali. Esse modelo relacional definirá como a aplicação consumirá esses dados, especificamente utilizando `SQL`.

### Isolamento e Visões

Percebemos que cada camada, cada nível, tem sua especificidade e seu papel. A questão aqui é diferenciar bem e explicitar o isolamento desejável dentro de um SGBD.

O modelo conceitual, como já comentado, será a base. Essa base não deve interferir, mas sim fomentar e mostrar as visões que determinados grupos possuem do meio à base de dados.

> [!definicao] Views
> Dentro do modelo conceitual, as **views** são definidas em projetos de alto nível.
> Elas permitem criar uma representação dos dados mais restrita, de acordo com cada grupo de usuário, baseando-se nas informações que cada grupo precisa ter acesso.

Novamente, surge a questão do isolamento. Preciso que a aplicação funcione independentemente de como está o modelo conceitual. Em certo nível, até dá para fazer, é um pouco difícil, mas dá.

> [!exemplo] Impacto da remoção de entidade na aplicação
> Se uma aplicação realiza uma operação como `SELECT`, por exemplo, `SELECT * FROM entidade`, ela retorna todas as informações daquela entidade. Isso não depende da quantidade de atributos que ela possui ou dos tipos de dados.
> >
> **Cenário:** A entidade é removida do modelo conceitual e, consequentemente, do banco de dados.
> **Problema:** A aplicação, ao tentar chamar o recurso ou método associado àquela entidade, encontrará um erro.
> **Solução:** Será necessário modificar a aplicação para corrigir o erro.
> >
> Este cenário demonstra que, embora o isolamento seja desejável, a remoção de uma entidade no modelo conceitual pode exigir alterações na aplicação.

Podemos alcançar um nível de isolamento razoável, mas é um pouco mais difícil.

> [!atenção] Suporte dos SGBDs ao isolamento
> A arquitetura de separação e isolamento entre os níveis interno, conceitual e externo não é explícita nem completamente suportada pelos SGBDs mais atuais. Embora seja possível usar extensões, elas são frequentemente usadas para simular esse isolamento.

Como já comentado, pode-se utilizar uma extensão, mas ela acaba sendo utilizada mais para fingir...

`⏱ 09:00`

Essa arquitetura é utilizada para fins de estudo, para que se consiga entender o papel do isolamento entre cada camada.

### Camadas Física e Lógica

Conseguimos separar essas camadas, classificando-as em física e **lógica**.

> [!definicao] Modelo Lógico
> Associado à visão do usuário e ao modelo conceitual.
> É uma abstração, uma ideia do que se quer representar dos dados.

Quando se fala de **modelo físico**, significa que é preciso criar uma representação dos dados a partir de uma série de requisitos.

> [!definicao] Modelo Físico
> Representação dos dados criada a partir de uma série de requisitos.
> Relacionado à definição em `SQL` e ao ambiente de criação do banco de dados.
> Em nível mais baixo, envolve índices e cache para performance.

Se for a um nível ainda mais baixo, estará relacionado a índices, cache, entre outras informações que poderiam ser gerenciadas e mapeadas para entregar uma melhor performance do banco de dados.
Entretanto, o esquema interno ficará um pouco longe desse esquema conceitual, porque ali se definirá com maior abstração, utilizando outro nível, e se dirá: "essa entidade possui esses atributos". Assim, é possível criar essas entidades do banco.
Mas surge a questão: é preciso de um cache para essas entidades? É preciso de um índice? Como armazenar? Como distribuir as instâncias dessa entidade em memória? Isso está relacionado àquela entidade.
Os atributos e as informações da entidade vão subsidiar as operações relacionadas à orquestração dos arquivos.
Isso, na verdade, independe das operações que serão realizadas via `SQL` nos dados, porque por trás dos panos haverá uma série de algoritmos de busca rodando para encontrar a melhor maneira possível de obter os dados solicitados.

### A Visão do Usuário (Camada Lógica Externa)

Com relação à parte lógica, temos a experiência mais externa, que é a do usuário. É possível determinar uma **`VIEW`** e, com isso, restringir informações, personalizar e ter uma maior otimização dos recursos e do tempo.

> [!exemplo] Otimização com `VIEW`s
> Se há uma quantidade enorme de informações, mas apenas uma parte é necessária, a busca pelo que realmente se precisa pode levar um tempo considerável.
> As `VIEW`s permitem otimizar esse processo, restringindo e personalizando as informações exibidas.

O problema é que as `VIEW`s estão relacionadas às entidades. Se uma junção de duas entidades distintas é usada para criar uma visão e um atributo é removido de uma dessas entidades, ocorrerá um erro. Por isso, percebe-se que o isolamento físico é mais fácil de ser alcançado do que o isolamento lógico, embora este último não seja impossível, apenas mais difícil.

## Relacionado

- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-vantagens-otimizacao-e-integridade-dos-dados]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-isolamento-abstracao-e-transparencia]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-abordagens-e-caracteristicas-essenciais]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-ganhos-e-otimizacao-operacional]]
