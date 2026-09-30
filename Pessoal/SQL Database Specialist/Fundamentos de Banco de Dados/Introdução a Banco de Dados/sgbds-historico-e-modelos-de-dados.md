---
titulo: "SGBDs: Histórico e Modelos de Dados"
tags: [sgbd, banco-de-dados, modelagem-de-dados, historia-da-computacao, conceitos, fundamentos, dados]
data: 2026-09-16
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 16
conceitos: [SGBD (Sistema de Gerenciamento de Banco de Dados), Modelo Relacional, Álgebra Relacional, Teoria de Conjuntos, Modelo Hierárquico, Modelo em Rede (Network Model), Inconsistência de Dados, Democratização da Tecnologia]
---

# SGBDs: Histórico e Modelos de Dados

> [!resumo] Do que se trata
> Esta aula explora o histórico dos Sistemas de Gerenciamento de Banco de Dados (SGBDs), detalhando a necessidade de sua criação em 1960 para reduzir custos e inconsistências de dados. Aborda a evolução dos modelos de dados, incluindo o hierárquico, em rede e o modelo relacional proposto por Edgar Codd em 1970. A aula também traça a linha do tempo dos bancos de dados e discute o impacto da democratização da tecnologia na demanda por SGBDs.

## Para lembrar

- **A ideia de um Sistema de Gerenciamento de Banco de Dados (SGBD) surgiu em 1960, enquanto o modelo relacional original foi concebido em 1970.**
- **A principal motivação para a criação dos SGBDs pela IBM em 1960 foi diminuir custos e resolver problemas de inconsistência de dados gerados por aplicações de usuário.**
- **Antes do modelo relacional, existiram o modelo hierárquico e o modelo em rede, que foram abordados brevemente.**
- **O modelo relacional, ainda utilizado hoje, foi criado por Edgar Codd em 1970, baseado na Álgebra Relacional e na Teoria de Conjuntos.**
- **A democratização da tecnologia nos anos 1980, com a redução dos custos de acesso a notebooks e PCs, aumentou significativamente a necessidade e a demanda por SGBDs.**

## O que esta nota responde

- Qual foi a motivação inicial para a criação dos SGBDs?
- Quais modelos de dados precederam o modelo relacional?
- Quem propôs o modelo relacional e em que ano?

## Conceitos

**SGBD (Sistema de Gerenciamento de Banco de Dados)** · **Modelo Relacional** · **Álgebra Relacional** · **Teoria de Conjuntos** · **Modelo Hierárquico** · **Modelo em Rede (Network Model)** · **Inconsistência de Dados** · **Democratização da Tecnologia**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Histórico SGBDs, necessidade e modelos de dados | ▪▪ |
| `04:00` | Modelo Relacional, linha do tempo e evolução | ▪▪ |
| `08:20` | NoSQL, evolução SGBDs e Modelo Hierárquico | ▪▪ |
| `12:40` | Modelos Hierárquico, Rede e evolução SGBDs | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Modelo Relacional** | Estrutura de tabelas e operações baseadas na teoria de conjuntos, que oferece uma abordagem generalista e um alto nível de transparência para o usuário sobre a manutenção e o gerenciamento dos dados no sistema. |
| **Paradigma de Orientação a Objeto** | Abordagem de programação que traz a ideia de objetos, características e operações relacionadas. |
| **Modelo Hierárquico** | É um sistema gerenciado voltado para a informação, onde se busca registros. Diferentemente do modelo relacional, que possui uma estrutura (entidade) e não uma instância, o modelo hierárquico possui uma instância (registro). |

## Pegadinhas

- A ideia de um sistema de gerenciamento de banco de dados surgiu em 1960, mas a do modelo relacional original surgiu em 1970.
- A IBM não foi a primeira empresa a fazer o primeiro SGBD; este foi lançado pela Honeywell Information System em 1976.
- O modelo hierárquico busca registros (instâncias), enquanto o modelo relacional possui uma estrutura (entidade).
- O modelo em rede faz relacionamento N para N, mas não é tão rico quanto o relacional, que permite atributos específicos para o relacionamento.

## Teste-se

<details><summary>Qual foi a principal motivação para o surgimento da ideia de um SGBD em 1960?</summary>

A principal motivação foi a necessidade de diminuir custos e otimizar recursos, evitando que o gerenciamento de dados fosse feito diretamente pelas aplicações de usuário. Isso também visava reduzir problemas como a necessidade de mudar a aplicação a cada alteração na estrutura dos dados e a inconsistência de dados por fadiga humana.

</details>

<details><summary>Quem criou o Modelo Relacional e em que ano? Em que bases ele foi desenvolvido?</summary>

O Modelo Relacional foi criado por Edgar Codd em 1970. Ele foi desenvolvido com base na Álgebra Relacional e na teoria de conjuntos.

</details>

<details><summary>Cite dois problemas do Modelo Hierárquico.</summary>

O Modelo Hierárquico não utiliza uma estrutura geral, mas sim registros (instâncias), o que agrega complexidade. Além disso, as buscas em árvore são mais complexas e menos otimizadas, tornando-as mais lentas.

</details>

<details><summary>Qual a principal diferença na abordagem de busca entre o Modelo Hierárquico e o Modelo Relacional?</summary>

No Modelo Hierárquico, busca-se um registro por vez, 'descendo' na árvore para acessar detalhes específicos de uma instância. No Modelo Relacional, busca-se uma estrutura de uma entidade, permitindo consultas mais gerais e otimizadas baseadas na teoria de conjuntos.

</details>

<details><summary>Quais são alguns exemplos de SGBDs NoSQL mencionados na aula?</summary>

Alguns exemplos de SGBDs NoSQL mencionados são Neo4j, Cassandra, MongoDB e Red.

</details>

<details><summary>Qual a principal desvantagem do Modelo em Rede em relação ao Modelo Relacional?</summary>

A principal desvantagem é que a pessoa que lida com o SGBD precisa conhecer a estrutura física do banco de dados, pois a busca em um grafo não é trivial. O modelo relacional, por sua vez, oferece maior transparência e consultas mais facilitadas.

</details>

## Conteúdo

`⏱ 00:00`

### Histórico dos SGBDs

Olá! Vamos falar um pouco do histórico dos **SGBDs** (Sistemas de Gerenciamento de Banco de Dados). O intuito não é ser maçante, é apenas passar de maneira breve sobre como surgiu a ideia de um sistema voltado para gerenciamento de dados. Abordaremos quando e por que surgiu o **Modelo Relacional**, e com base em quê.

Em seguida, teremos uma visão geral sobre as características e propriedades deste modelo, que é utilizado até hoje. Numa última etapa, falaremos dos sistemas de gerenciamento de banco de dados mais utilizados no mercado. Esse é o nosso roteiro para este assunto.

A ideia de um sistema de gerenciamento de banco de dados, não do modelo relacional, surgiu em 1960. A ideia do modelo relacional original surgiu em 1970. Há um período entre um e outro, e nesse intervalo surgiram outros dois modelos que serão abordados brevemente.

### A Necessidade de um SGBD

Por que surgiu essa vontade de criar um sistema de gerenciamento de banco de dados? Essa ideia, que surgiu em 1960 através da IBM, tinha o intuito de diminuir custos. Pense no seguinte: se você não tem um sistema voltado para isso, como o gerenciamento de dados é feito? Através das aplicações de usuário.

Nesse cenário, você mantém a estrutura e define o gerenciamento dentro da própria aplicação. Isso traz uma série de problemas. Um deles, bastante óbvio, é que se houver alguma mudança na estrutura dos seus dados, você terá que mudar a aplicação. Imagine o quão problemático isso é para uma aplicação em produção! Além disso, o custo era alto. Ao tirar essa função dos desenvolvedores e da aplicação, você otimiza recursos.

Outro ponto a considerar é a inconsistência dos dados. Se uma pessoa é responsável por manter o gerenciamento e a estrutura dos dados, é completamente factível que haja alguma inconsistência.

> [!exemplo] A inconsistência dos dados por fadiga humana
> O cansaço acontece. Nosso cérebro se estafa, diferentemente de um computador. Embora alguns computadores possam se estafar e desligar, eles conseguem operar 24 horas por dia. Nós, humanos, precisamos de um período de descanso.
>
> Quando nosso cérebro está funcionando há muito tempo, ou estamos na mesma função por muitas horas (como um desenvolvedor programando por várias horas e não conseguindo encontrar um erro no programa), a fadiga mental ocorre.
>
> Muitas vezes, ao sair daquele contexto, respirar, fazer outra coisa e depois voltar, o erro se torna óbvio. Isso acontece porque nosso cérebro se estafa, e inconsistências podem surgir nesse meio tempo.
>
> Ao tirar essa função e preocupação do desenvolvedor, além de tornar a vida dele mais fácil, otimizamos recursos e reduzimos a chance de inconsistências.

### Modelos de Dados

Para conseguir gerenciar dados, precisamos primeiro definir uma estrutura. Essa estrutura, ou as diretrizes que regem a estrutura de um dado em um **Modelo de Dados**, é definida justamente no modelo. Isso pode ser um modelo em rede, hierárquico ou relacional.

Antes do modelo relacional surgir em 1970, existiram o modelo hierárquico e o modelo em rede. Falaremos um pouco sobre cada um.

O modelo relacional, que é utilizado até hoje, foi criado por Edgar Codd e desenvolvido com base na **Álgebra Relacional**.

`⏱ 04:00`

O modelo relacional foi criado com base na álgebra relacional e na teoria de conjuntos, de forma que ele consegue trazer uma estrutura mais generalista. Veremos mais adiante, por exemplo, quando fazemos uma consulta em `SQL`, que conseguimos abstrair a estrutura de uma tabela, a estrutura de uma entidade.

### O Modelo Relacional de Edgar Codd

Quando Edgar Codd definiu a estrutura de tabelas e as operações baseadas na teoria de conjuntos, ele trouxe um modelo mais generalista e conseguiu um nível relativamente alto de transparência para o usuário, com relação a como ocorre toda a manutenção e o gerenciamento dos dados dentro do sistema.

> [!definicao] Modelo Relacional
> Estrutura de tabelas e operações baseadas na teoria de conjuntos, que oferece uma abordagem generalista e um alto nível de transparência para o usuário sobre a manutenção e o gerenciamento dos dados no sistema.

Edgar Codd apresentou sua ideia através de um artigo, como geralmente acontecia naquela época, e muitas inovações são propostas dessa forma, principalmente na academia. Isso aconteceu em 1970, justamente pela `IBM`.

Parece estranho e contraditório, mas a `IBM` não foi a primeira empresa a fazer o primeiro `SGBD`. Na verdade, ela criou primeiramente o `System R`, que não era baseado no modelo relacional, e que acabou servindo de base para o `DB2`. O `SQL` definiu a `ISO` que o rege.

Quando Ted Codd definiu a estrutura de um **modelo relacional**, ele também definiu posteriormente a **linguagem de consulta** para recuperar informações de dados baseados nesse modelo.

### Linha do Tempo dos Bancos de Dados

Para ter uma noção da sequência de eventos e da linha do tempo:

| Ano | Evento / Tecnologia | Detalhes |
| :--- | :--- | :--- |
| 1960 | Conceito de Banco de Dados | Surgiu a ideia. |
| 1970 | Modelo Relacional | Surgiu (Edgar Codd, `IBM`, baseado em álgebra relacional e teoria de conjuntos). |
| 1976 | Primeiro `SGBD` (não relacional) | Lançado pela `Honeywell Information System`. |
| 1980 | `Oracle SGBD` (relacional) | `Oracle 2` (ou `Oracle DB2`) lançado. |
| 1983 | `IBM SGBD` (relacional) | `IBM SQA SQL DS` (ou `SQL DS`) lançado. |
| 1983 | `Oracle 3` | Lançado. |
| 2022 | `Oracle DB` | Top 3 utilizado, considerado pioneiro. |

### Democratização e Novas Perspectivas

Em 1980, houve uma democratização de acesso à tecnologia. A tecnologia foi evoluindo, o custo foi barateando, e o acesso a notebooks e `PCs` (personal computers) se tornou mais facilitado porque os custos diminuíram com o tempo. Com mais dados sendo gerados, mais pessoas utilizando computadores e navegando, aumentou a necessidade de `SGBDs`.

Em 1990, surgiu o **paradigma de orientação a objeto**, a programação voltada com a orientação a objeto, que está bem mais próxima da nossa realidade do que a programação procedural.

> [!definicao] Paradigma de Orientação a Objeto
> Abordagem de programação que traz a ideia de objetos, características e operações relacionadas.

Se pensarmos no modelo relacional, que ainda será definido, temos uma entidade, uma tabela, e essa entidade possui características. Podemos chamá-la de objeto. Assim, conseguimos fazer um paralelo entre o mundo de orientação a objeto e o modelo relacional.

A partir dos anos 2000, surgiu uma nova perspectiva relacionada aos dados, uma nova demanda, uma nova visão e necessidade sobre os dados. Surgiram os **`NoSQL`**. Exemplos incluem `Neo4j`, `Cassandra`, `MongoDB` e `Red`.

`⏱ 08:20`

Os NoSQL, como Neo4j, Cassandra, MongoDB e Red, são vários modelos diferentes que surgiram para suprir uma lacuna que o modelo relacional acabou deixando.

Desde o primeiro SGBD disponibilizado no mercado, houve uma evolução em termos de utilização e processamento. Saímos de cerca de 8 MB de processamento para terabytes.

O feedback relacionado a esses sistemas foi muito bom, e eles foram se aprimorando ao longo do tempo. O desenvolvimento de sistemas, com um feedback ótimo, superou as expectativas, gerando a necessidade de aperfeiçoar os sistemas existentes.

Consequentemente, utilizando, por exemplo, a programação orientada a objetos, a ideia de orientação a objeto foi inserida no modelo de entidade e relacionamento estendido, que é um aprimoramento do modelo original de entidade e relacionamento. (Vamos falar sobre modelagem de dados e banco de dados em outro módulo.)

Percebemos que houve evolução, e o contexto dos SGBDs acompanhou essa evolução. Continuou-se utilizando SGBDs.

Com o advento e a utilização de sistemas distribuídos, que fornecem maior performance (dado que você tem diversos nós dentro de um cluster processando diversas informações, réplicas e redundância de informação, o que reduz o ponto de falha e oferece uma série de vantagens), aumentou ainda mais a demanda por SGBDs, por um sistema único voltado exclusivamente para este fim.

Há uma série de vantagens, e vamos destrinchar tudo sobre eles durante este módulo. Tudo isso a partir de 1980.

### Modelo Hierárquico

O que vem a ser o **modelo hierárquico**? O próprio nome já é intuitivo e autodescritivo.

> [!definicao] Modelo Hierárquico
> É um sistema gerenciado voltado para a informação, onde se busca registros.
> Diferentemente do modelo relacional, que possui uma estrutura (entidade) e não uma instância, o modelo hierárquico possui uma instância (registro).

Se observarmos a estrutura de uma árvore, onde temos os dados, os registros e seus links, eles estão conectados em cima de um tipo de extrato de dados que é uma árvore. Nela, temos o nó pai (ou nó mãe, raiz, como preferir), os nós filho e os nós folha. Esta é uma representação clássica de modelo hierárquico.

Aqui, conseguimos ver alguns problemas. Primeiro, não utilizamos uma estrutura geral, mas sim um registro, uma instância.

> [!exemplo] Busca de aluno no Modelo Hierárquico
> Imagine um cenário simples com `aluno`.
> No modelo hierárquico, não há uma tabela que define todos os alunos, mas sim instâncias individuais, como "Cecília de Taubaté".
> Para procurar um aluno, não se acessa uma estrutura geral com todas as ocorrências. Em vez disso, busca-se um aluno por vez, e para obter mais informações sobre ele, é necessário "descer" na árvore para acessar os detalhes específicos daquela instância.

Percebe-se que isso agrega complexidade ao modelo, porque uma busca em árvore é mais complexa. Além disso, não se busca uma estrutura de uma entidade, mas sim um registro. Assim, você pode vir para cá e não encontrar o registro de aluno que quer, tendo que começar a buscar nas outras ramificações dessa árvore, o que torna...

`⏱ 12:40`

Os algoritmos de busca mais complicados e menos otimizados são aqueles que precisam buscar em uma árvore. Por isso, são mais lentos.

Esse modelo foi utilizado por sistemas como `Cobol`, `FoxPro` e `Clipper`. Existem exemplos de utilização desse modelo, mas ele não foi o modelo que vingou.

### Modelo em Rede (Network Model)

Para visualizar o que significa, vamos usar um grafo. Temos links, que são os ponteiros entre os nós. Esses nós possuem informações geradas hierarquicamente, como nome, cidade e telefone.

Percebo que tenho essa estrutura linkada com outra estrutura, como `cliente` e `conta`. Não sei que tipo de relacionamento é esse, mas sei que um associado está associado a outro.

Na mesma forma que esses dois estão associados, olhando este grafo, eu posso ter uma série de nós diferentes associados ao mesmo grafo, ao mesmo nó, e até a aquele grafo. Isso agrega complexidade ao meu modelo.

O modelo em rede foi sugerido lá em 1900. Qual é o principal problema dele?

A pessoa que está lidando com o SGBD precisa conhecer a estrutura física do banco de dados, porque não é trivial. Assim como não é trivial uma busca em uma árvore, não é trivial uma busca em um grafo. São aí questões de otimização.

O modelo em rede, na verdade, faz um relacionamento N para N. Ele não é tão complexo quanto o modelo relacional, mas também não é tão rico.

#### Comparação de Complexidade

| Característica | Modelo em Rede | Modelo Relacional |
| :--- | :--- | :--- |
| **Relacionamento** | N para N | N para N |
| **Complexidade** | Simples, mas não tão rico. | Mais complexo, mais rico. |
| **Atributos de Relacionamento** | Não há definição clara de atributos específicos para o relacionamento. | Permite ter atributos, características específicas desse relacionamento. |
| **Consulta** | Menos fácil de otimizar. | Baseado na teoria de conjuntos, permite criar consultas mais gerais e otimizar essas consultas, tornando-as mais simples. |

No modelo relacional, eu extrapolo esse relacionamento para uma nova identidade. Isso acontece no modelo relacional, tornando-o mais rico.

### A Evolução dos SGBDs

O intuito aqui não é aprofundar no modelo hierárquico nem no modelo em rede. É passar uma ideia do que aconteceu no mundo dos SGBDs, da história dos SGBDs, e que acabou se motivando a criação do modelo relacional.

Por quê? Porque os modelos anteriores eram mais complexos e não tratavam todos os cenários.

Estruturas em grafo ou estrutura em árvore são interessantes, mas elas não são aplicadas a todos os casos. O modelo relacional trouxe uma aplicabilidade mais vasta e também uma transparência para o sistema. Além de consultas mais facilitadas, ele foi o modelo que avançou.

A partir daqui, vamos entrar no assunto de modelo relacional.

## Relacionado

- [[bancos-de-dados-da-evolucao-ao-big-data]]
- [[bancos-de-dados-definicao-acesso-e-escala]]
- [[sgbd-etapas-estrutura-e-fases]]
- [[jornada-da-formacao-sql-database-specialist]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Tchau, tchau.

</details>
