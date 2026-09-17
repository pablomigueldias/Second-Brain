---
titulo: "SGBDs: Os Mais Utilizados no Mercado"
tags: [banco-de-dados, sgbd, sql, conceitos, dados, fundamentos]
data: 2026-09-16
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 23
conceitos: [SGBD, Oracle DB, MySQL, PostgreSQL, MariaDB, Elasticsearch, Banco de Dados Relacional, Banco de Dados NoSQL]
---

# SGBDs: Os Mais Utilizados no Mercado

> [!resumo] Do que se trata
> Esta aula apresenta uma lista dos SGBDs mais utilizados no mercado, destacando suas características e cenários de uso. Ela aborda tanto bancos de dados relacionais como Oracle DB, MySQL, SQL Server e PostgreSQL, quanto opções NoSQL como MongoDB, Redis e Elasticsearch. A escolha do SGBD é contextualizada pela empresa e cenário, com foco na versatilidade e performance de cada sistema.

## Para lembrar

- **A escolha de SGBDs como Oracle, MySQL, SQL Server ou Postgres é considerada uma boa opção, sendo guiada pelo cenário e empresa.**
- **O Oracle DB, pioneiro no mercado, foi projetado para alta performance e é amplamente utilizado por grandes corporações e governos.**
- **MySQL é o SGBD de código aberto mais popular, mantido pela Oracle, e é frequentemente a primeira escolha para aplicações web devido à sua leveza e versatilidade.**
- **PostgreSQL é uma alternativa robusta e de código aberto ao Oracle, preferida por programadores Python, e oferece suporte nativo para armazenamento de documentos.**
- **MariaDB é um derivado do MySQL, mantendo a licença de código aberto e sendo praticamente intercambiável com o MySQL em termos de estrutura e base.**

## O que esta nota responde

- Quais são os SGBDs mais utilizados no mercado e suas principais características?
- Quais são as diferenças e semelhanças entre MySQL, PostgreSQL e MariaDB?
- Em que cenários o Oracle DB e o Elasticsearch são mais indicados?

## Conceitos

**SGBD** · **Oracle DB** · **MySQL** · **PostgreSQL** · **MariaDB** · **Elasticsearch** · **Banco de Dados Relacional** · **Banco de Dados NoSQL**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Introdução e escolha de SGBDs | ▪ |
| `04:00` | MySQL: popularidade e origem | ▪▪ |
| `08:20` | PostgreSQL: vantagens e recursos | ▪▪ |
| `12:40` | Redis: NoSQL, cache e performance | ▪▪ |
| `17:00` | Access: escolha e cenário de uso | ▪ |
| `21:00` | Fatores de escolha de SGBD | ▪▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **BI (Business Intelligence)** | Ferramentas voltadas para a integração com Business Intelligence. |
| **MongoDB** | Um SGBD NoSQL orientado a documentos. |
| **Redis** | Um SGBD NoSQL orientado a chave-valor, equivalente a um dicionário. É performático, escalável e muito popular. |
| **NoSQL** | Um tipo de banco de dados que não utiliza o modelo relacional tradicional, sendo mais flexível e escalável para lidar com grandes volumes de dados não estruturados ou semiestruturados. |

## Pegadinhas

- A classificação do Elasticsearch como SGBD NoSQL orientado a documentos é debatida, com alguns considerando-a uma forçação de barra.
- Não há necessidade de converter um banco de dados para migrar de MySQL para MariaDB, pois eles têm praticamente a mesma estrutura e base.
- O Access não é um SGBD robusto como Oracle, MySQL ou Postgres, mas tem seu nicho para projetos simples.

## Teste-se

<details><summary>Qual SGBD é considerado o pioneiro e o melhor para gerenciamento de grandes volumes de dados?</summary>

O Oracle DB é o pioneiro e é considerado o melhor sistema para gerenciamento de grandes volumes de dados, sendo utilizado por grandes corporações e governos.

</details>

<details><summary>Quais SGBDs a Oracle mantém, demonstrando sua hegemonia no mercado?</summary>

A Oracle mantém o Oracle DB, que foi o pioneiro, e também o MySQL, que é uma solução de código aberto e um dos mais utilizados no mundo.

</details>

<details><summary>Qual a estratégia da Microsoft para tornar o SQL Server atrativo para o mercado?</summary>

A Microsoft investiu massivamente no SQL Server, oferecendo bons descontos para instituições educacionais e tornando-o gratuito ou mais barato, visando garantir usuários futuros.

</details>

<details><summary>Quais são as principais características do Redis?</summary>

O Redis é um SGBD NoSQL orientado a chave-valor, performático, escalável e popular. Ele armazena informações em memória, resultando em leituras absurdamente rápidas e diminuindo atrasos de busca.

</details>

<details><summary>O que o texto menciona sobre a origem do MariaDB em relação ao MySQL?</summary>

O MariaDB é um projeto que se originou do MySQL, criado por profissionais que trabalharam no projeto original. Eles são muito similares, e não há necessidade de converter um banco de dados para migrar entre eles.

</details>

<details><summary>Cite três características importantes na escolha de um SGBD, além da popularidade e tempo de mercado.</summary>

Além da popularidade e tempo de mercado, outras características importantes na escolha de um SGBD são a robustez do servidor, a confiabilidade, a segurança e a capacidade multiplataforma.

</details>

## Conteúdo

`⏱ 00:00`

### Introdução aos SGBDs Mais Utilizados

Aqui está uma lista dos **SGBDs** (Sistemas de Gerenciamento de Banco de Dados) mais utilizados no mercado. Não entraremos em detalhes de arquitetura, diferenças de *features* ou forma. A ideia é citar algumas características para contextualizar e mostrar quais são os mais utilizados, com os quais você provavelmente lidará.

Se você escolher `Oracle`, `MySQL`, `SQL Server` ou `Postgres`, estará fazendo uma boa escolha. Sua decisão provavelmente será guiada pela empresa onde você vai estudar, pela faculdade ou pelo curso que você está fazendo.

Nesta formação, utilizarei o `MySQL`. No entanto, na parte de instalação, instalaremos o `Postgres` e o `MySQL` com vocês, tanto na plataforma Windows quanto na Linux. Algumas questões associadas a consultas utilizando `SQL` mudarão, mas isso será abordado em uma parte mais avançada, quando falarmos de `SQL` especificamente. Por enquanto, focaremos na parte conceitual, entendendo as diferenças de forma superficial. Em breve, instalaremos esses dois SGBDs juntos.

A escolha do SGBD dependerá do seu cenário e da sua empresa. Usaremos o `MySQL` como principal, mas com as diferenças que serão pontuadas entre `Postgres` e `MySQL`, você conseguirá acompanhar mesmo que esteja utilizando um SGBD diferente.

### 1. Oracle DB

O primeiro da lista é o `Oracle DB`. Um dos motivos para ele ser o primeiro é que foi o pioneiro. Ele foi projetado para fornecer maior performance e, consequentemente, acabou sendo utilizado por grandes corporações e governos.

> [!exemplo] Design e Impacto de Mercado do Oracle DB
> O `Oracle DB` possui uma espécie de "reserva de mercado" por ter sido adotado por grandes corporações desde o início.
> Sua arquitetura é voltada para cenários de alta performance, sendo projetado para trabalhar em *grid*, o que permite atender de forma mais assertiva às demandas de grandes corporações.
> Ele é considerado o melhor sistema para gerenciamento de grandes volumes de dados, mantendo uma posição inabalável no mercado ao oferecer soluções para essas corporações.

Suas características incluem:
- Alta disponibilidade
- Segurança
- Autoescalabilidade
- Manutenção
- Resiliência a falhas nos servidores

Ele possui características realmente interessantes para grandes corporações.

### 2. MySQL

O segundo SGBD nesta lista é o `MySQL`. Ele também é mantido pela Oracle, mas é uma solução de código aberto (*open source*).

É o mais popular entre os SGBDs de código aberto e um dos mais utilizados no mundo. Geralmente, quando você está aprendendo...

`⏱ 04:00`

Geralmente, quando você está aprendendo no banco de dados, você começa por ele. O `MySQL` é muito utilizado, por exemplo, na maioria das aplicações web, por ser bem leve. Isso permite uma performance mais interessante em aplicações web. Contudo, ele não se limita a esse cenário.

Ele possui características e *automatic features* mais robustas, tornando-o um SGBD versátil. Tem uma boa integração com `PHP`, o que permite construir soluções utilizando tanto o *front-end* quanto o *back-end* do `PHP`, integrando com o `MySQL`.

A empresa que criou o `MySQL` lá atrás foi a `Sun Microsystem`, mas ela acabou sendo vendida e comprada pela `Oracle`. Hoje, a `Oracle` é quem mantém esse SGBD. É interessante pontuar que o primeiro e o segundo colocados desse ranking são mantidos pela `Oracle`, o que demonstra a hegemonia da `Oracle` no mercado.

### SQL Server

O próximo SGBD é o `SQL Server`, mantido pela `Microsoft`. Ele é uma plataforma mais abrangente e sofisticada, com ferramentas voltadas para a integração com `BI`.

> [!definicao] BI (Business Intelligence)
> Ferramentas voltadas para a integração com **Business Intelligence**.

A `Microsoft` inseriu investimentos significativos para agradar os usuários do `Oracle` e também do `DB2`, que é o SGBD da `IBM`. A `Microsoft` precisava tornar o `SQL Server` atrativo de alguma forma, então começou a investir massivamente para torná-lo interessante, performático e atribuir características para aplicações críticas.

Ele possui tecnologias *in-memory*, fluxos rápidos de informação e outras características, sendo integrado com o `Excel`.

> [!exemplo] Estratégia de mercado da Microsoft para o SQL Server
> Uma abordagem que a `Microsoft` trouxe, tentando atrair o público, foi fornecer bons descontos para instituições educacionais, oferecendo o `SQL Server` gratuitamente ou por um valor bem mais baixo para assinatura.
> >
> Ao incluir escolas e universidades, a `Microsoft` garante que, se alguém aprender a usar esse SGBD específico, há uma maior probabilidade de que essa pessoa o mantenha em sua carreira. A ideia era: "fazendo dessa forma, trazendo gratuidade e descontos para universidades, para quem está aprendendo, é uma maneira de garantir meu mercado lá na frente". Essa estratégia realmente funciona, e diversas outras empresas utilizam abordagens de venda semelhantes.

O `SQL Server` é uma plataforma resiliente, com construção robusta, e implanta soluções de gerenciamento tanto locais quanto em nuvem. É um SGBD bem interessante.

> [!atenção] Escolha do SGBD
> Não há escolha errada quando você pensa em qual SGBD utilizar: `Oracle`, `MySQL`, `SQL Server` ou `Postgres`. Cada um tem sua especificidade, sua aplicabilidade e empresas que se adequam melhor a cada característica.

### PostgreSQL

O `PostgreSQL`, também conhecido como `Postgres`, é um SGBD bastante robusto e consolidado, sendo um "queridinho" de muitos. Todos os SGBDs mencionados são consolidados, mas o `PostgreSQL` possui características específicas.

Ele é considerado um exemplo quando se trata de especificação. Com relação ao `ANSI SQL`, ele é extremamente aderente a essa especificação e acabou se tornando praticamente um padrão.

O projeto do `PostgreSQL` surgiu em 1995 e derivou de um outro projeto, criado em 1976. Embora as datas não sejam o mais importante, ele foi originado de um projeto específico chamado `Ingres`, que também derivou outros SGBDs, como, por exemplo,

`⏱ 08:20`

SQL Server e Cybase. Três SGBDs distintos saíram de um mesmo projeto.

### PostgreSQL

Para quem utiliza PHP, o **MySQL** é mais interessante e familiar do que o **PostgreSQL**. No entanto, o PostgreSQL possui características interessantes. Ele é a primeira escolha para programadores voltados para linguagens como Python.

É uma alternativa ao Oracle por ser bem robusto. Embora seja um pouco mais pesado que o MySQL, ele é muito robusto e, por ser *open source* (assim como o MySQL), possui uma comunidade global que contribui para seu aprimoramento.

O PostgreSQL oferece vantagens como:
-   Criação de um modelo de dados híbrido, caso você precise de recursos no ciclo parciais em seu projeto.
-   Suporte nativo para armazenamento de documentos, com orientação em chave-valor.

Ele tem características bem interessantes, como suporte nativo a armazenamento de documentos (como `JSON`, `XML`) e replicação síncrona e assíncrona.

Cada SGBD tem uma infinidade de características interessantes. No módulo de SQL, falaremos sobre as características do MySQL e do PostgreSQL, comparando os dois SGBDs e suas diferenças na manipulação de bancos de dados.

O quinto colocado neste ranking é um SGBD NoSQL: o MongoDB.

> [!definicao] MongoDB
> Um SGBD **NoSQL** orientado a documentos.

### MongoDB

O MongoDB é um banco que armazena dados em blocos, com uma orientação diferente do **modelo relacional** que estamos estudando. Os dados são agrupados dentro de um mesmo bloco.

Ao contrário da estrutura baseada em tabelas, os detalhes de cada contato do usuário e os níveis de acesso residem no mesmo objeto. Ou seja, a estrutura dos dados e as informações relacionadas a eles estão dentro do objeto, dentro do documento.

O MongoDB possui recursos interessantes que podem levar um DBA a não escolher o modelo relacional. Há cenários específicos onde isso é vantajoso.

> [!exemplo] Cenários de uso do MongoDB
> Um exemplo é o caso da Black Friday. O MongoDB possui um esquema flexível para casos de uso mais imprevisíveis, quando não há previsibilidade na modelagem dos dados.

Ele fragmenta e agrupa de maneira mais simples, bastando definir a configuração de um *cluster*. Não é preciso revisitar essa configuração; a adição e remoção de módulos é extremamente simples, e a otimização de gravações é muito rápida.

Outras características inerentes a um SGBD NoSQL incluem:
-   Escalabilidade
-   Performance

### Redis

O sexto colocado é outro SGBD NoSQL.

> [!definicao] Redis
> Um SGBD **NoSQL** orientado a **chave-valor**, equivalente a um dicionário. É performático, escalável e muito popular.

É ideal para um mundo onde se precisa muito da utilização de *caches*, de gerenciamento de sessões e onde se dá...

`⏱ 12:40`

e onde a gente dá [prioridade à performance e] os dados acabam sendo acessados com mais irregularidade, precisa de rapidez nesse acesso. O que acontece é que o **Redis** acaba armazenando suas informações em memória, diminuindo e evitando atrasos relacionados a tempo de busca e consumo de CPU. As instruções de I/O diminuem muito, ou quase não existem, porque ele pega os dados em memória, não diretamente no disco. Existe I/O, mas é bem reduzido.

O banco de dados Redis é simples e relativamente fácil de aprender. Ele perde alguns recursos, mas compensa em performance. Uma vez que ele roda inteiramente na RAM, as leituras são absurdamente rápidas. Alguns projetos podem se beneficiar dessa questão de cache e acesso rápido a informações. Há um cenário bem específico quando se trata de um banco NoSQL performático, utilizando modelagem por chave-valor.

### Elasticsearch

Com relação ao **Elasticsearch**, existe um dilema: alguns locais o classificam como um SGBD NoSQL orientado a documentos, enquanto outros consideram isso uma forçação de barra.

O Elasticsearch, que surge na sétima posição, é muito utilizado, principalmente na justiça com Kibana, para realizar relatórios de logs e explorar logs de sistema. Ele é um mecanismo de busca que possui APIs REST distribuídas, capaz de atender a um número grande e crescente de casos.

O coração do Elasticsearch é a maneira como ele trata e armazena os dados de forma mais centralizada, o que permite descobrir e desvendar informações inesperadas.

> [!exemplo] Empresas que utilizam Elasticsearch
> Atualmente, o Elasticsearch é muito utilizado por startups e grandes empresas relacionadas à inovação, como:
> - SoundCloud
> - Twitter
> - Google
> - GitHub

Ele possui uma interface simples, com uma estrutura via HTTP. Como ele usa APIs REST, ele se apoia no protocolo HTTP e faz suas requisições utilizando os métodos HTTP. A maioria das APIs utiliza o formato JSON.

Então, você tem um SGBD NoSQL orientado a documentos com uma API REST associada. O cenário onde ele se encaixa é a análise de logs. Ele é comumente utilizado para ingerir e analisar logs praticamente em tempo real e de maneira escalonável. A escalabilidade é uma característica dos bancos NoSQL, o que o torna interessante para cenários onde você consegue tirar insights relacionados ao ambiente operacional, que é o ambiente de logs.

### Microsoft Access

O próximo da lista, na verdade, eu nunca diria que ele é um SGBD, dado que um SGBD tem toda uma robustez por trás. Comparar um **Access** com `Postgres`, `MySQL` ou `Oracle` é meio desleal, mas o Access tem o seu nicho.

Ele acaba sendo mais simples e é muito utilizado dentro de ambientes Windows. Ele se integra com o Office e é barato e fácil de acessar. Por isso, é utilizado em laptops: se você tem Windows, terá o Access ali dentro.

Embora seja considerado principalmente para sistemas de desktop, ele acabou se tornando extremamente conhecido à medida que muitos sistemas de gerenciamento de conteúdo e e-commerce o utilizavam.

`⏱ 17:00`

Muitos sistemas operacionais de gerenciamento de conteúdo de e-commerce, por exemplo, são alimentados por ele e executados na plataforma `Observer`.

Obviamente, a escolha do SGBD dependerá do seu cenário, da complexidade do seu projeto e dos seus dados. O Access é uma opção mais simples e tranquila.

> [!exemplo] O canhão e a formiga
> Se o seu projeto for simples, você não vai utilizar um canhão para matar uma formiga. Ou seja, você não vai utilizar um `Oracle DB` se você tem uma padaria na esquina. Para um pequeno negócio, o Access pode ser suficiente.

Ou então, um SGBD Open Source como `MySQL` ou `Postgres` já pode resolver.

Vocês devem ter percebido que estou dando uns "pulinhos" na sequência (do 7 para o 9, do 9 para o 12, do 12 para o 11). Isso é estratégico, pois queria citar esses SGBDs específicos. Se quiserem ver a lista completa, podem acessar o link que está aqui embaixo.

### MariaDB

O `MariaDB` é um projeto que se originou do `MySQL`. Foi um braço que se deslocou do `MySQL`, criado por profissionais que trabalharam no projeto original.

Como um derivou do outro, eles são muito similares. Não há necessidade de converter um banco de dados para migrar de `MySQL` para `MariaDB`; você simplesmente o utiliza, pois eles têm praticamente a mesma estrutura e base.

As diferenças entre `MySQL` e `MariaDB` são:

| Característica | MySQL                                                              | MariaDB                                                               |
| :------------- | :----------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Origem**     | Projeto original                                                   | Derivado do `MySQL`                                                   |
| **Licença**    | Código aberto, mas com opção de distribuição comercial (Oracle)    | Derivado do código-fonte do `MySQL`, mantendo a licença de código aberto |
| **Suporte**    | Servidores de suporte com diferenças em relação ao `MariaDB`       | Servidores de suporte com diferenças em relação ao `MySQL`            |
| **Performance**| Padrão                                                             | Método de busca e consulta mais otimizado, aumentando o desempenho    |

Por meio de `benchmarking`, é possível verificar a velocidade e comprovar se o `MariaDB` é melhor que o `MySQL` em termos de performance. O `MariaDB` está crescendo em utilização.

### Cassandra

O `Cassandra` é um banco de dados **NoSQL**, gratuito e open source, especificamente baseado em colunas. Ele é voltado para ambientes de gerenciamento de larga escala, utilizando dados de grande volume através de diferentes servidores, provendo alta disponibilidade com apenas um ponto de falha.

> [!definicao] NoSQL
> Um tipo de banco de dados que não utiliza o modelo relacional tradicional, sendo mais flexível e escalável para lidar com grandes volumes de dados não estruturados ou semiestruturados.

O `Cassandra` foi inicialmente desenvolvido pelo Facebook e utilizado para motores de busca e caixas de entrada de mensagens. Em 2008, tornou-se open source e, em 2009, passou a ser administrado e mantido pela `Apache Foundation`, que também está relacionada ao `Apache Server` e `Apache HTTP`.

É um SGBD que está em alta e sendo bastante utilizado no cenário NoSQL. Vale a pena citar esses sistemas.

`⏱ 21:00`

O que influencia na **escolha de um SGBD** a ser utilizado no mercado é a popularidade dele e o tempo de mercado. O Oracle DB é pioneiro.

> [!exemplo] A analogia do Bitcoin
> Quando o Bitcoin surgiu no mercado, ele foi pioneiro. Se você for compará-lo com Ethereum, ele tem algumas limitações, mas continua valendo mais. O fato de ser pioneiro também influencia na popularidade de um determinado sistema.

### Documentação
A documentação é muito importante. Para qualquer tecnologia, para programação ou qualquer assunto relacionado a TI, é sempre interessante procurar uma documentação relacionada àquele assunto. O `MySQL`, por exemplo, tem a página deles com toda a especificação e documentação para você poder utilizar o SGBD. Da mesma forma, para os demais.

### Outras Características na Escolha de um SGBD
Outras características interessantes na escolha de um SGBD são:
- **Robustez do servidor**: quanto ele aguenta de demanda.
- **Confiabilidade**: se ele vai estar "up" e dar conta.
- **Segurança**: se os dados estarão protegidos, se haverá restrição de acesso, perfis associados, e se os dados não serão corrompidos.
- **Multiplataforma** (ou *cross-platform*): essa questão também é muito interessante e influencia na tomada de decisão ao escolher um SGBD.

## Relacionado

- [[jornada-da-formacao-sql-database-specialist]]
- [[bancos-de-dados-da-evolucao-ao-big-data]]
- [[sgbd-etapas-estrutura-e-fases]]
- [[contextualizacao-da-formacao-sql-database-specialist-apresentacao-da-instrutora-]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `Jason → JSON`
- `RESTful → APIs REST`
- `restful → APIs REST`
