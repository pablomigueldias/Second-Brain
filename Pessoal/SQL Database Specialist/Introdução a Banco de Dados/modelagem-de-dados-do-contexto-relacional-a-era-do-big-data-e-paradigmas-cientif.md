---
titulo: "Modelagem de Dados: Do Contexto Relacional à Era do Big Data e Paradigmas Científicos"
tags: [dados, banco-de-dados, sgbd, modelagem-de-dados, ia, machine-learning, conceitos]
data: 2026-09-16
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 17
conceitos: [Modelos de dados relacionais, NoSQL, HPC (High Processing Computing), Big Data, SGBD (Sistema Gerenciador de Banco de Dados), Paradigma científico, Data Driven Science, Granularidade de dados]
---

# Modelagem de Dados: Do Contexto Relacional à Era do Big Data e Paradigmas Científicos

> [!resumo] Do que se trata
> Esta aula explora a evolução da modelagem de dados, abordando a transição dos modelos relacionais para novas estruturas como NoSQL e os desafios impostos pelo Big Data e HPC. Ela contrasta o uso majoritário de SGBDs relacionais em ambientes corporativos com a complexidade dos dados em cenários de pesquisa, que exigem abordagens específicas. A aula também introduz os paradigmas científicos, focando no quarto paradigma (Data Driven Science) e sua relação com os 3 V's do Big Data, IA, Machine Learning e Data Science.

## Para lembrar

- **Em pelo menos 90% das situações, SGBDs de modelo relacional são utilizados, principalmente em sistemas corporativos para manutenção de dados de negócio.**
- **Ambientes de pesquisa lidam com cenários de dados de alta complexidade, como mapeamento de DNA e simulação de fármacos, que não são comumente encontrados em empresas.**
- **A granularidade da resolução de dados impacta diretamente o volume: uma resolução de 3 km pode gerar 8 petabytes de dados, enquanto 100 km geram 8 terabytes.**
- **O paradigma do Big Data é caracterizado pelos seus três Vs: Velocidade (rapidez de geração, processamento e análise), Variedade (diferentes formatos e tipos de dados) e Volume (quantidade massiva de dados).**
- **O quarto paradigma científico, Data Driven Science, é atrelado aos 3 V's do Big Data e utiliza ferramentas como IA, Machine Learning e Data Science para extrair informações significativas.**

## O que esta nota responde

- Quais são os principais desafios da modelagem de dados na era do Big Data e como eles se diferenciam dos modelos relacionais?
- Como os ambientes de pesquisa se distinguem dos cenários corporativos em termos de complexidade e volume de dados?
- Quais são os quatro paradigmas científicos e como o quarto paradigma (Data Driven Science) se relaciona com os 3 V's do Big Data?

## Conceitos

**Modelos de dados relacionais** · **NoSQL** · **HPC (High Processing Computing)** · **Big Data** · **SGBD (Sistema Gerenciador de Banco de Dados)** · **Paradigma científico** · **Data Driven Science** · **Granularidade de dados**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Era dos Dados e Futuro Modelagem | ▪ |
| `04:20` | Pesquisa: Volume, Heterogeneidade, Exemplos | ▪▪ |
| `08:40` | Desafios Dados e Paradigmas Científicos | ▪▪ |
| `13:00` | Quarto Paradigma e Requisitos | ▪▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **SGBD (Sistema Gerenciador de Banco de Dados)** | O papel principal de um SGBD relacional está associado aos sistemas corporativos. Grandes empresas, startups, ou qualquer que seja o nível e tamanho da empresa, utilizam um modelo relacional. |
| **Data Driven Science** | É uma ciência baseada em dados, orientada a dados. É o profissional de dados que se preocupa em pegar dados e transformá-los em informação útil para tomadas de decisão, seja para um negócio ou para ações relacionadas à saúde. |
| **Os 3 V's do Big Data** | O paradigma Data Driven Science está atrelado a três características principais: Velocidade (A rapidez com que os dados são gerados, processados e analisados), Variedade (Os diversos formatos e tipos de dados (estruturados, semiestruturados, não estruturados)), Volume (A vasta quantidade de dados que é produzida e armazenada). |
| **Reprodutividade** | Dentro do quarto paradigma, é essencial que todo estudo possa ser reproduzido por outra pessoa. Para isso, o estudo deve ser abstrato e generalista, permitindo sua aplicação em outros cenários dentro do mesmo contexto. |

## Pegadinhas

- Computação paralela e distribuída são diferentes.
- Modelagem relacional tradicional é impossível para cenários de Big Data como o Dark Energy Survey, devido ao volume, velocidade e complexidade dos dados.

## Teste-se

<details><summary>Qual a porcentagem de situações em que um SGBD relacional é utilizado, segundo a aula?</summary>

Em pelo menos 90% das situações, um SGBD de modelo relacional é utilizado.

</details>

<details><summary>Cite duas características que diferenciam os dados de pesquisa dos dados corporativos.</summary>

Dados de pesquisa frequentemente envolvem mapeamento de DNA, simulação de fármacos e análise de grande volume de dados com alta complexidade. Dados corporativos focam na manutenção de informações de negócio como vendas e funcionários, com baixa complexidade.

</details>

<details><summary>Quais são os três primeiros paradigmas científicos na ordem cronológica?</summary>

Os três primeiros paradigmas científicos são: Primeiro (Empírico/Experimental), Segundo (Teórico/Matemático) e Terceiro (Simulações Computacionais).

</details>

<details><summary>Quais são os '3 V's' do Big Data?</summary>

Os '3 V's' do Big Data são Velocidade (rapidez na geração e processamento), Variedade (diversos formatos e tipos de dados) e Volume (vasta quantidade de dados produzida e armazenada).

</details>

<details><summary>O que é 'Data Driven Science'?</summary>

Data Driven Science é uma ciência baseada e orientada a dados, onde profissionais transformam dados em informação útil para tomadas de decisão em negócios ou pesquisas científicas.

</details>

## Conteúdo

`⏱ 00:00`

### A Era dos Dados e o Futuro da Modelagem

Vamos conversar sobre uma nova perspectiva e um novo contexto que definem diretrizes para a maneira como olhamos para os dados. Isso inclui outras estruturas que não são modelos de dados relacionais. A partir dos anos 2000, surgiram os NoSQL.

Também há a questão do paradigma científico da HPC, que é o High Processing Computing, e o Big Data. Quero pontuar alguns passos e pensamentos futuros dentro de uma área que está sempre evoluindo.

### O Contexto Majoritário: Modelos Relacionais

Começaremos com o contexto majoritário, ou seja, o que comumente acontece no cenário de dados que a maioria das empresas necessita. O modelo relacional está inserido nesse contexto.

Posso afirmar com certeza que, em pelo menos 90% das situações, vocês utilizarão um **SGBD** de modelo relacional.

> [!definicao] SGBD (Sistema Gerenciador de Banco de Dados)
> O papel principal de um SGBD relacional está associado aos sistemas corporativos. Grandes empresas, startups, ou qualquer que seja o nível e tamanho da empresa, utilizam um modelo relacional.

Você terá pessoas interessadas em consumir esse conteúdo e esses dados, independentemente do seu perfil:
- Analistas
- Usuários de outros grupos

Na maioria dos cenários, temos requisições mais comuns. Se pensarmos na regra 80/20, em 80% do tempo, você terá uma consulta simples sendo executada sobre o grupo de dados. Além disso, algumas operações mais simples, como `mínimo`, `máximo`, `count`, `média` e `somar`, são frequentemente realizadas.

Em 80% das situações, é assim que acontecerá. Ao programar ou desenvolver um projeto de dados, você deve pensar nesse cenário mais comum e deixar as questões específicas para os 20% mais complexos. Via de regra, a maioria das situações ocorre dessa forma.

### Ambientes de Pesquisa e a Complexidade dos Dados

Temos um novo ambiente de pesquisa, geralmente acadêmico, onde nosso interesse vai além de apenas manter os dados de uma corporação. Uma empresa, seja um e-commerce ou de qualquer outro viés, precisa manter, no mínimo, os dados dos funcionários e os dados das vendas. A maioria das empresas lida com vendas, direta ou indiretamente.

Há diversas informações relacionadas ao negócio que, às vezes, não contêm uma complexidade muito elevada, como em ambientes de pesquisa, e precisam ser mantidas pelo SGBD. Esse é o cenário mais comum.

No entanto, dentro do ambiente de pesquisa, encontramos cenários que não são comumente utilizados nas empresas:

| Dados Corporativos | Dados de Pesquisa |
| :----------------- | :---------------- |
| Manutenção de dados de corporação | Mapeamento de DNA |
| E-commerce | Simulação de fármaco |
| Dados de funcionários | Detecção de padrões |
| Dados de vendas | Reconhecimento de fala |
| Informações relacionadas ao negócio | Detecção de dados de astronomia |
| Baixa complexidade | Análise de grande volume de dados |
| Cenários comumente utilizados nas empresas | Cenários não correntes nas empresas |

`⏱ 04:20`

Embora esses cenários não sejam correntes comumente utilizados nas empresas, há cenários em grandes empresas como o Facebook e o Google, onde eles lidam com um grande volume de dados e precisam de uma abordagem específica. Realmente, isso acontece. Contudo, eu diria que isso é mais comum dentro da academia, principalmente em mestrado e doutorado, computados para a área de ciência de dados, por exemplo.

Temos todo esse contexto atrelado à área de pesquisa. Quando falamos de pesquisa, o que podemos pensar em relação ao poder computacional? Pesquisas estão muito ligadas ao poder de processamento, porque lidam com grande volume de dados.

Nós temos características que relacionam o número de tarefas computacionais e a quantidade de dados com que se está lidando, geralmente um grande volume. Principalmente aqui na GNCC, as bases de dados disponibilizadas para um trabalho ou projeto de ciência de dados são enormes. Por exemplo, minha base de dados do Ethereum era de mais de 500 milhões de transações. Realmente, lidamos com um grande volume de dados.

Outra característica é a **heterogeneidade**. Lidamos com diversas fontes diferentes que geram dados relacionados ao mesmo contexto, mas que possuem estruturas diferentes, padrões de escrita diferentes e também maneiras de determinar aquele contexto de formas distintas.

Além disso, a **computação paralela e distribuída**, que são diferentes, sim, estão relacionadas a esse contexto, agregando maior complexidade às pesquisas.

### Exemplos de Cenários de Pesquisa

> [!exemplo] Análise de Histórico Climático
> Um exemplo que relaciona várias dessas características é a verificação e análise do histórico do clima em uma determinada região durante 100 anos.
>
> Se pegarmos uma região com resolução de 3 km², a granularidade desse mapeamento significa que verificamos o clima a cada 3 km. Por exemplo, a cada 3 km, fazemos uma média: "neste ponto, dentro de 3 km, está meio nublado e chuvoso; a partir deste ponto, já começa a ter mais sol".
>
> Em contraste, se tivermos uma resolução de 100 km para verificar a média do clima, essa resolução torna a percepção da realidade mais difícil. Você cria uma média geral de clima, mas às vezes há uma variação muito grande naqueles 100 km.
>
> Por exemplo, a distância entre Petrópolis e Rio de Janeiro é de 60 km, mas são quilômetros totalmente diferentes em termos climáticos. Assim, você perde um pouco a percepção da realidade.
>
> Em termos de processamento, uma resolução de 100 km lida com 8 terabytes de dados. É bastante coisa. Mas quando passamos para uma granularidade de 3 km, o volume de dados vai para 8 petabytes. É muito mais coisa, muito mais dados. É uma quantidade que nos faz pensar: "não consigo nem mensurar a quantidade de linhas que essa quantidade de dados vai gerar". E tudo isso para um cenário de 100 anos.
>
> Este exemplo ilustra o grande volume de dados e também a heterogeneidade, pois, dependendo do sistema que coleta as informações, ele as destrincha e distribui de maneira diferente. Este é um cenário voltado para a área de pesquisa.

> [!exemplo] Dark Energy Survey
> Outro cenário é o `Dark Energy Survey`, um projeto específico para mapear galáxias e supernovas e detectar padrões dentro do universo. Ele gera em torno de 6.6 terabytes por dia.

`⏱ 08:40`

É gerado em torno de 6.6 terabytes dia, o que representa uma criação de dados em tempo real e contínua. Ou seja, não há uma quantidade estática de dados; é preciso analisar uma quantidade recorrente de dados todos os dias, com novas informações surgindo constantemente.

> [!exemplo] O Dark Energy Survey e o desafio dos dados
> Vinte e cinco instituições e mais de 400 cientistas compõem e estão associados a esse projeto. É um projeto muito complexo, como se pode ver pela própria câmera que mapeia o universo para encontrar galáxias e supernovas. Todos esses dados precisam ser analisados.
>
> Pense nisso dentro de um contexto tradicional de modelagem de mobilidade relacional. É impossível, não atende. Primeiro, os dados são em tempo real, uma quantidade absurda de informações.
>
> Alguém poderia argumentar que, em um cenário de e-commerce, também há compras todos os dias. Realmente há, mas não é algo tão gigantesco quanto o Dark Energy Survey, onde se analisa algo totalmente diferente. Não se está analisando venda, produto, cliente, fornecedor, mas sim uma galáxia.
>
> Como representar uma galáxia dentro de um contexto de modelagem do que se está analisando? É possível conseguir isso, mas será que há a performance necessária para lidar com esse tipo de situação?
>
> Por isso, é provável que uma outra abordagem esteja sendo utilizada para esse cenário.

### Os Paradigmas Científicos

Começo a introduzir o **quarto paradigma**, que é chamado de **paradigma científico**. Pensando na ordem cronológica dos paradigmas, temos:

| Paradigma | Característica Principal | Descrição | Exemplos |
| :-------- | :----------------------- | :-------- | :------- |
| Primeiro  | Empírico / Experimental  | Baseado em tentativa e erro para provar algo. Descobertas muitas vezes surgiam por acidente. | Benjamin Franklin (eletricidade), Thomas Edison (lâmpada), Leonardo da Vinci (autodidata, aprendia por tentativa e erro). |
| Segundo   | Teórico / Matemático     | Associado à parte teórica da ciência, matemática e analítica. Escreve-se um teorema ou axioma e prova-se matematicamente/teoricamente, de forma direta. | Prova de teoremas e axiomas. |
| Terceiro  | Simulações Computacionais | Ciência computacional, onde sistemas podem ser mapeados ou simulados. | Simulação de dinâmica molecular, interação de dinâmica de fluidos. |

Só que aí vem o quarto paradigma, que é o paradigma do **Data Driven Science**.

> [!definicao] Data Driven Science
> É uma ciência baseada em dados, orientada a dados. É o profissional de dados que se preocupa em pegar dados e transformá-los em informação útil para tomadas de decisão, seja para um negócio ou para ações relacionadas à saúde.

`⏱ 13:00`

Se for um negócio, para ser tomada de ação relacionada à saúde da empresa. Se for em uma pesquisa científica, eu vou pegar aqueles dados, analisar para tentar entender meu contexto e tirar insights para suportar minha teoria.

Dentro desse paradigma, utiliza-se a inteligência artificial, a estatística atrelada à análise de dados, a computação, o `Data Mining`, a verificação de padrões e anomalias, e a detecção de padrões e anomalias em uma rede. É uma nova maneira de enxergar e abordar a modelagem de dados, partindo do princípio de que há uma base a ser explorada para extrair informações significativas. Para isso, são usadas ferramentas que possibilitam atingir esse objetivo, como análise utilizando IA, Machine Learning e Data Science, com diversos vieses.

Com essa perspectiva de Data Driven Science, existe uma quantidade absurda de dados sendo gerada.

> [!definicao] Os 3 V's do Big Data
> O paradigma Data Driven Science está atrelado a três características principais, conhecidas como os "3 V's":
> - **Velocidade**: A rapidez com que os dados são gerados, processados e analisados.
> - **Variedade**: Os diversos formatos e tipos de dados (estruturados, semiestruturados, não estruturados).
> - **Volume**: A vasta quantidade de dados que é produzida e armazenada.
> >
> Estes "3 V's" são fundamentais não só para a ciência, mas também para a abordagem de negócios.

### Requisitos do Quarto Paradigma

Dentro desse quarto paradigma, os requisitos ou assuntos relacionados incluem:

-   Composição do problema.
-   Execução de uma determinada teoria ou aplicação voltada para uma análise.
-   Processo de abstração: associado para criar um modelo e, a partir dele, analisar a quantidade de dados. A abstração também pode ser suficiente para encontrar o modelo a ser utilizado, e não necessariamente criá-lo.

> [!definicao] Reprodutividade
> Dentro do quarto paradigma, é essencial que todo estudo possa ser reproduzido por outra pessoa.
> >
> Para isso, o estudo deve ser **abstrato** e **generalista**, permitindo sua aplicação em outros cenários dentro do mesmo contexto.
> >
> Por exemplo, se uma metodologia é desenvolvida para analisar a rede de transações do Ethereum, ela deve ser geral o suficiente para ser aplicada de forma igual ou similar ao Bitcoin.

-   Reutilização: Ser capaz de utilizar e reutilizar o projeto de outra pessoa dentro do seu cenário.
-   Escalabilidade: Dado o modelo, a abordagem e a metodologia, ela deve ser escalável, permitindo reproduzir o estudo e a análise para um volume maior de dados.

Essas são algumas características e requisitos relacionados ao quarto paradigma, que é o paradigma científico.

## Relacionado

- [[contextualizacao-da-formacao-sql-database-specialist-apresentacao-da-instrutora-]]
- [[visao-geral-da-carreira-em-ti-da-rede-a-ciencia-de-dados-e-programacao]]
- [[bancos-de-dados-da-evolucao-ao-big-data]]
- [[historia-da-computacao-paradigmas-e-problemas-computacionais]]
