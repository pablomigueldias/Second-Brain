---
titulo: "Bancos de Dados: Da Evolução ao Big Data"
tags: [banco-de-dados, conceitos, dados, fundamentos, sistema, organizacao]
data: 2026-09-13
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 17
conceitos: [Banco de Dados, SGBD, Dados, Informação, Cookies, HTTP, Big Data, Bancos NoSQL]
---

# Bancos de Dados: Da Evolução ao Big Data

> [!resumo] Do que se trata
> Esta aula introduz os bancos de dados, diferenciando dados de informação e explorando a evolução do armazenamento de dados, desde métodos analógicos até a era digital. Ela detalha o poder dos dados na personalização de serviços e publicidade, as vantagens dos bancos de dados e SGBDs, e o novo cenário impulsionado pelo Big Data. Por fim, aborda as tecnologias emergentes para lidar com os desafios do grande volume e heterogeneidade de dados.

## Para lembrar

- **Dados são a matéria-prima bruta que precisa ser explorada, limpa, ter sua estrutura compreendida e ter equívocos ou redundâncias tratadas.**
- **Informação são os fatos organizados de maneira a produzir um significado, ou seja, dados colocados em contexto.**
- **Cookies são um tipo específico de dado relacionado ao protocolo HTTP, utilizados por empresas para personalizar serviços e enviar publicidade direcionada.**
- **O SGBD (Sistema Gerenciador de Banco de Dados) gerencia o acesso e as permissões aos dados, garantindo segurança e persistência confiável.**
- **A estrutura do banco de dados relacional ainda atende a cerca de 90% dos casos de modelagem de dados, mas cenários de Big Data exigem novas formas de modelar.**

## O que esta nota responde

- Qual a diferença fundamental entre dados e informação?
- Quais são as principais vantagens de utilizar um banco de dados e um SGBD?
- Como a evolução da computação e o surgimento do Big Data impactaram a necessidade de novas tecnologias de armazenamento e processamento de dados?

## Conceitos

**Banco de Dados** · **SGBD** · **Dados** · **Informação** · **Cookies** · **HTTP** · **Big Data** · **Bancos NoSQL**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Introdução e evolução do armazenamento de dados | ▪ |
| `04:00` | Poder, persistência e vantagens dos dados | ▪▪ |
| `08:00` | Evolução computacional e novo cenário de dados | ▪ |
| `12:20` | Big Data e tecnologias de suporte | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Dados** | a matéria-prima bruta que precisa ser explorada, limpa, ter sua estrutura compreendida, e ter equívocos ou redundâncias identificados e tratados. |
| **Cientista de dados** | pega os dados brutos e os transforma em algo útil e em insights para fomentar tomadas de decisão relacionadas ao negócio e impactar positivamente a saúde da empresa. |
| **Big Data** | caracterizado pelos seus três Vs: Velocidade (a rapidez com que os dados são gerados, processados e analisados), Variedade (os diferentes formatos e tipos de dados) e Volume (a quantidade massiva de dados gerados). |
| **Bancos NoSQL (Not Only SQL)** | sistemas de gerenciamento de banco de dados (SGBDs) que surgiram como uma nova forma de modelar dados para cenários onde a estrutura do banco de dados relacional não é mais adequada, como em contextos de Big Data, onde há grande heterogeneidade e dados não estruturados. |

## Pegadinhas

- Dados e informações são coisas diferentes: dados são a matéria-prima bruta, enquanto informações são o resultado útil do tratamento dos dados.
- Bancos de dados relacionais atendem a 90% dos casos, mas para Big Data e dados não estruturados, a estrutura relacional não é mais adequada, exigindo bancos NoSQL.
- NoSQL significa 'Not Only SQL', indicando que esses bancos não são apenas uma alternativa ao SQL, mas uma forma diferente de modelar dados.

## Teste-se

<details><summary>Qual é o principal objetivo dos bancos de dados, conforme a introdução da aula?</summary>

O objetivo é diferenciar e estruturar dados, entender a diferença entre dados e informação, e tratar e persistir dados de forma confiável.

</details>

<details><summary>Como a aula descreve a diferença entre dados e informações?</summary>

Dados são a matéria-prima bruta que precisa ser explorada e tratada. Informações são o resultado útil e os insights gerados após o tratamento dos dados, que fomentam tomadas de decisão.

</details>

<details><summary>Quais são as três características (os '3 Vs') que definem o paradigma do Big Data?</summary>

O Big Data é caracterizado por Volume (quantidade massiva de dados), Variedade (diferentes formatos e tipos de dados) e Velocidade (rapidez na geração, processamento e análise dos dados).

</details>

<details><summary>Por que os bancos NoSQL surgiram e em quais cenários são mais adequados?</summary>

Os bancos NoSQL surgiram para cenários onde a estrutura do banco de dados relacional não é mais adequada, como em contextos de Big Data com grande heterogeneidade e dados não estruturados.

</details>

<details><summary>Cite duas vantagens de um SGBD (Sistema Gerenciador de Banco de Dados) mencionadas na aula.</summary>

Duas vantagens são a segurança e a persistência confiável dos dados, e a restrição de acesso, que gerencia permissões para evitar acessos indevidos.

</details>

<details><summary>Quais são os tipos de dados que o novo cenário de dados, impulsionado pela evolução da computação, passou a incluir além de texto e número?</summary>

O novo cenário inclui estruturas mais complexas como posts, informações de 'likes', imagens, vídeos e redes sociais.

</details>

## Conteúdo

`⏱ 00:00`

### Introdução aos Bancos de Dados

Vamos definir o que são bancos de dados. Para isso, descreveremos o cenário em que eles estão situados. Nosso objetivo é diferenciar e estruturar **dados**, entender a diferença entre dados e informação (porque há uma diferença), e por que tratamos e persistimos dados. Em seguida, definiremos exatamente o que são bancos de dados em geral, como funciona sua estrutura e todo o sistema voltado para esse tratamento, e o que são SGBDs. Este é o intuito e o objetivo desta etapa.

Tudo hoje são dados. A finalidade da internet é prover serviços a diversas pessoas, de maneira descentralizada, online e praticamente imediata. Temos uma grande rede interconectando países e pessoas, oferecendo serviços em diferentes línguas, com uma infinidade de informações e fontes heterogêneas.

### A Evolução do Armazenamento de Dados

> [!exemplo] Da Agenda ao Celular
> Antigamente, usávamos cadernos e agendas para registrar informações como números de telefone, aniversários e endereços. Eu, particularmente, ainda gosto de usar papel para estudar. Costumo brincar que, se eu apenas leio, a informação fica na memória RAM. Mas quando eu escrevo, é como se eu passasse da memória RAM para um HD, reforçando o aprendizado.
>
> A tecnologia, no entanto, evoluiu exponencialmente e se democratizou, tornando-se de baixo custo ao longo do tempo. Hoje, nossa agenda é o celular, que contém tudo. Nele, conseguimos acessar diversos dados, desde contatos até informações da nossa navegação na internet.
>
> Em qualquer dispositivo eletrônico com um navegador de internet, existem vários `cookies`. As empresas ou mantenedores de serviços utilizam esses `cookies` para personalizar o serviço para você e, muitas vezes, para enviar publicidade direcionada. A lógica é: se uma pessoa gosta de um determinado item, a publicidade desse item será enviada, aumentando a probabilidade de compra.

Se quiserem aprofundar nesse assunto, há um curso na DIO sobre os principais protocolos de comunicação. Um `cookie` é um tipo específico de dado relacionado ao protocolo `HTTP`. Tudo são dados: aplicativos, buscadores como o Google e redes sociais.

> [!exemplo] Publicidade Direcionada
> Você já notou que, ao pesquisar um produto como uma `airfryer` no Google ou YouTube, e depois retornar ao Instagram, anúncios desse mesmo produto aparecem no seu feed? Isso acontece devido à coleta e análise de dados.
>
> Às vezes, a sensação é ainda mais forte: parece que os dispositivos "ouvem" o que você está falando. Você comenta sobre algo, não pesquisa, e um pop-up ou anúncio relacionado surge. Tudo isso é resultado do tratamento de dados.

`⏱ 04:00`

mas simplesmente um pop-up de publicidade aparece relacionado àquele assunto.

### O Poder dos Dados

Qual é o poder dos dados? É justamente conseguir atingir o público de uma maneira mais assertiva. Este não é o único ponto, mas é o mais gritante, devido ao sistema de vendas, de conversão de vídeos, enfim. Conseguimos utilizar os dados para otimizar nossos negócios.

### Dados e Informações

Temos um buscador, e às vezes queremos utilizar dados para analisar informações, explorar e tratar esses dados, porque **dados** e **informações** são coisas diferentes.

>[!definicao] Dados e Informações
> **Dados** são a matéria-prima bruta que precisa ser explorada, limpa, ter sua estrutura compreendida, e ter equívocos ou redundâncias identificados e tratados.
>
> O processo de tratamento dos dados transforma-os em algo útil e em *insights* que fomentam tomadas de decisão relacionadas ao negócio e impactam positivamente a saúde da empresa.

>[!exemplo] A analogia do diamante bruto
> Os seus dados são como um diamante bruto. É preciso explorá-lo, limpá-lo, entender sua estrutura, identificar possíveis equívocos e redundâncias. Esse processo é o tratamento dos dados.

>[!definicao] Papel do Cientista de Dados
> O **cientista de dados** pega os dados brutos e os transforma em algo útil e em *insights* para fomentar tomadas de decisão relacionadas ao negócio e impactar positivamente a saúde da empresa.

### A Necessidade de Persistência Confiável

Nós temos diversos cenários onde tudo são dados: games, diretórios (que são arquivos dentro do seu computador), GPS, análise gráfica, aplicativos, buscadores. Tudo isso são dados.

No entanto, se tudo são dados (tudo entre aspas), precisamos persistir isso de uma maneira confiável. De uma forma que, quando você for procurar aquela informação, ela continue lá, esteja lá e não tenha sido corrompida por algum motivo.

Antigamente, um arquivo era facilmente corrompido dentro de um `HD`, que tem aquela agulhinha que fica procurando a posição correta relacionada ao arquivo persistido. Havia uma probabilidade de ter um problema e seu arquivo ser corrompido. Esse tipo de coisa não pode acontecer. Imagine você lidando com dados de uma empresa e simplesmente os perdendo.

### Vantagens do Banco de Dados e SGBD

Quando pensamos em **banco de dados** e um sistema específico voltado para isso, temos uma série de vantagens. Uma delas é a segurança e a persistência confiável desses dados.

Existe uma escala de conjuntos de dados, do menor ao maior, diferenciada pela complexidade e pelo cenário de aplicação.

Quando você acessa sua conta via caixa eletrônico ou diretamente no caixa, você está fazendo um acesso a um banco de dados. Se for pelo caixa eletrônico, você está acessando uma `API` que, por sua vez, acessa o banco de dados do banco, puxando informações como extrato e detalhes da sua conta específica.

Você não pode acessar a conta de outra pessoa. Imagine se não houvesse um sistema gerenciando esse tipo de acesso e determinando as permissões. Você poderia acessar a conta de outra pessoa, fazer um saque. Veja o problema que isso causaria.

O **SGBD** (Sistema Gerenciador de Banco de Dados), além de várias vantagens, traz a restrição de acesso. Essa é uma característica que comentaremos.

Além disso, podemos ter sistemas menos complexos, como a consulta de um título de livro na biblioteca. A biblioteca precisa manter dados relacionados a um acervo de diversos livros de áreas diferentes. Este é, obviamente, um sistema bem menos complexo do que um sistema voltado para um ambiente transacional.

`⏱ 08:00`

Esse sistema é internacional em termos de banco de dados, mas de transações financeiras.

Até relativamente pouco tempo, os dados eram massivamente numéricos e textuais. Eu lembro do disquete. Eu nasci na época em que a Microsoft foi criada, lá em 1990. Pensando em como a computação evoluiu de lá para cá, e comparando com outras áreas mais tradicionais, como engenharia mecânica e engenharia civil, a evolução da computação é algo incrível. Naquela época, há uns 9 ou 10 anos, eu lembro que meu avô tinha um computadorzinho com tela verde, aquele CRT gigante, e ele utilizava disquetes para armazenar as informações. Era coisa de Kbytes, ínfimo perto da potência de um celular básico hoje em dia. Hoje, temos a capacidade de um computador nas mãos, comparado a 20 anos atrás, aproximadamente.

### A Evolução da Computação

Isso, porém, veio mudando. Com o decorrer do tempo e a evolução que comentei, o poder de processamento aumentou. Não foi apenas a complexidade que aumentou; na verdade, a complexidade cresceu porque conseguimos maior capacidade e poder computacional. Os HDs ficaram maiores, e passamos de Kbytes para petabytes.

Podemos ver o Santos Dumont, um supercomputador mantido no LNCC, cuja capacidade é surreal. A Petrobras também tem um supercomputador. Diversos supercomputadores surgiram com capacidade de processamento e armazenamento gigantescas. O foco e a tecnologia disruptiva de hoje são totalmente diferentes de 20 anos atrás.

### O Novo Cenário de Dados

> [!exemplo] O consumo da blockchain
> A capacidade de processamento e a energia necessárias para minerar a rede do Bitcoin são equivalentes às de um pequeno país da Europa em um ano.

O paradigma e as necessidades mudaram. A computação evoluiu em termos de processamento, democratizando o acesso a ferramentas e tecnologias, aumentando a capacidade de armazenamento e permitindo a oferta de mais serviços.

Hoje, não temos apenas texto e número, como em um bloco de notas ou no `gedit` do Linux. Temos redes sociais, com estruturas mais complexas como posts e informações de "likes" (que podem ser representadas como entidades), além de imagens, vídeos e redes se conectando. Queremos mapear o comportamento dessas redes, onde as pessoas se conectam facilmente, e identificar perfis para possíveis compradores, por exemplo.

### O Paradigma do Big Data

O cenário mudou completamente. Temos o paradigma do **Big Data**.

> [!definicao] Big Data
> O paradigma do Big Data é caracterizado pelos seus três Vs:
> - **Velocidade**: a rapidez com que os dados são gerados, processados e analisados.
> - **Variedade**: os diferentes formatos e tipos de dados (estruturados, semiestruturados e não estruturados).
> - **Volume**: a quantidade massiva de dados gerados.

São três características que geram um trabalho enorme. Em termos de volume, a quantidade de dados que uma rede social (que é o exemplo mais palpável para vocês) produz é gigantesca. Pense em um banco como o Itaú, que é um dos maiores, se não...

`⏱ 12:20`

O Itaú ficou maior, um dos maiores bancos do mundo. A quantidade de informações que ele possui, processa e armazena é gigantesca.

A **variedade**, que é a questão das fontes heterogêneas, e como tratamos isso, também é um desafio e uma questão explorada na academia. Minha experiência com mestrado me mostrou que eles são muito fortes na área de Ciência de Dados e Big Data. Quando pensamos em tratar fontes heterogêneas, temos um novo desafio: entender como tudo isso funciona, encaixar e depois analisar.

Além disso, a **velocidade**. A velocidade com que os dados são produzidos hoje é praticamente a segundo, milissegundo. As pessoas estão conectadas o tempo inteiro. Quase, se pudesse, estaria conectado dormindo. Há uma quantidade muito grande de dados sendo produzidos a todo momento. Isso também é um desafio: como analisar dados em tempo real?

Tudo isso que comentei até agora é um mundo de pesquisa.

### Tecnologias para Big Data

Nesse sentido, surgiram diversas tecnologias para dar suporte a todos esses desafios e a essa nova perspectiva relacionada ao mundo dos dados.

A estrutura do banco de dados relacional, que trataremos aqui, ainda atende a cerca de 90% dos casos de modelagem de dados. No entanto, há cenários específicos onde essa estrutura não cabe mais, como os relacionados a Big Data. Nesses casos, você tem heterogeneidade e dados que não são estruturados de maneira relacional, exigindo uma nova forma de modelar.

> [!definicao] Bancos NoSQL (Not Only SQL)
> São sistemas de gerenciamento de banco de dados (SGBDs) que surgiram como uma nova forma de modelar dados para cenários onde a estrutura do banco de dados relacional não é mais adequada. Isso ocorre, por exemplo, em contextos de Big Data, onde há grande heterogeneidade e dados não estruturados.

Surgiram, então, os **bancos NoSQL**, ou SGBDs `NoSQL`. Exemplos incluem `Cassandra`, `Neo4j`, `MongoDB` e `Redis`.

| Banco NoSQL | Tipo/Modelo de Dados | Características |
|---|---|---|
| `Cassandra` | Wide Column | |
| `Neo4j` | Grafo (SGBD baseado em grafo) | Muito utilizado em Ciência de Dados e `Network Data Science` para analisar e extrapolar dados para modelos de grafos. |
| `MongoDB` | Documentos | Curva de aprendizado baixa. |

Além disso, veio a computação em nuvem.

> [!exemplo] Vantagens da Computação em Nuvem
> A computação em nuvem, como os serviços da `Amazon` (`AWS`) ou `Azure` (`Microsoft`), oferece um cenário propício para uso em Big Data. Ao invés de ter um Centro de Processamento de Dados (`CPD`) local, você utiliza um `CPD` distribuído globalmente, provido por terceiros.
> >
> Isso facilita a vida do desenvolvedor, pois:
> - Você não precisa provisionar servidores, comprar hardware caro ou lidar com infraestrutura para momentos específicos.
> - A nuvem provê "computação como serviço", simplificando a gestão de recursos.
> >
> Tudo isso veio para facilitar, apesar de exigir aprendizado, e se alinha com o novo paradigma de dados.

Tudo isso veio juntamente com esse novo cenário, esse novo paradigma relacionado a dados.

## Relacionado

- [[contextualizacao-da-formacao-sql-database-specialist-apresentacao-da-instrutora-]]
- [[SGBD]]
- [[00 - Índice]]
- [[01 - Conceitos Básicos]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `DIU → DIO`
