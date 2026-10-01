---
titulo: "Modelagem de Dados: Projeto e Esquema Conceitual"
tags: [modelagem-de-dados, banco-de-dados, conceitos, fundamentos, sgbd, engenharia-de-software, dados]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 15
conceitos: [Visões, Abstração, Esquema Conceitual, Entidade, Atributo, Redundância, Modelo Entidade-Relacionamento (MER), Projeto Conceitual]
---

# Modelagem de Dados: Projeto e Esquema Conceitual

> [!resumo] Do que se trata
> Esta aula explora a criação de visões e a aplicação da abstração na modelagem de dados, culminando na definição de um esquema conceitual como representação gráfica da narrativa. Através de um exemplo prático de periódicos e editoras, são detalhadas a identificação de entidades e atributos, e a importância de evitar redundância. A aula também aborda a validação do modelo com perguntas, a utilização de UML e MER no projeto conceitual, e a natureza de alto nível e iterativa do projeto conceitual, focando nos requisitos do sistema.

## Para lembrar

- **Abstração é a necessidade de generalizar, deixando de lado detalhes desnecessários para o contexto, focando no que é realmente preciso.**
- **O esquema conceitual fornece a visão gráfica da narrativa do modelo de dados, a partir da modelagem e do projeto conceitual.**
- **Uma entidade é preferível a um atributo quando a repetição de informações da entidade principal geraria redundância significativa.**
- **O Modelo Entidade-Relacionamento (MER) é um modelo de alto nível, mais comum e interessante para leigos visualizarem, focado no que realmente se quer saber.**
- **O projeto conceitual é um modelo de alto nível que define o 'quê' (processos, informações, funções, requisitos de performance) sem especificar 'como' os dados serão armazenados ou implementados.**

## O que esta nota responde

- O que é abstração e como ela se aplica na modelagem de dados?
- Como um esquema conceitual é definido e qual sua importância na representação de dados?
- Quais são os princípios do projeto conceitual e como ele se relaciona com os requisitos do sistema?

## Conceitos

**Visões** · **Abstração** · **Esquema Conceitual** · **Entidade** · **Atributo** · **Redundância** · **Modelo Entidade-Relacionamento (MER)** · **Projeto Conceitual**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Visões, abstração e esquema conceitual | ▪▪ |
| `04:20` | Entidades, atributos e validação do modelo | ▪▪ |
| `08:40` | UML, MER e requisitos do sistema | ▪▪ |
| `13:00` | Esquema conceitual e fluxo iterativo | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Abstração** | É a necessidade de generalizar, mas para isso é preciso deixar de lado detalhes que são desnecessários para o contexto. O foco é no que realmente é preciso, ignorando os detalhes. |
| **Esquema Conceitual** | Esse modelo de alto nível, relacionado ao projeto conceitual e o modelo representado pelo esquema conceitual, é independente do modelo de banco de dados. |
| **Requisitos Funcionais** | São o que a aplicação precisa executar. Incluem os processos que serão rodados e os tipos de funções que serão contemplados na aplicação, que acessarão o banco de dados e retornarão informações. A ideia de função e de execução está atrelada a esse tipo de requisito. |
| **Requisitos Não Funcionais** | Estão atrelados ao próprio sistema. Envolvem aspectos como segurança e desempenho. Nesta etapa do projeto, verifica-se se o projeto será, por exemplo, voltado para um sistema de banco de dados para OLTP (Online Transaction Processing), que é um tipo de sistema que exige alta performance. |

## Pegadinhas

- Um periódico não deve ser modelado como atributo de uma editora se houver redundância de informação, mas sim como uma entidade própria.

## Teste-se

<details><summary>Qual o propósito da abstração na modelagem de dados?</summary>

A abstração foca em generalizar informações, ignorando detalhes desnecessários e concentrando-se apenas no que é relevante para o contexto.

</details>

<details><summary>Por que um 'Periódico' pode ser modelado como entidade e não atributo de 'Editora'?</summary>

Se uma editora publica múltiplos periódicos, modelar 'Periódico' como atributo geraria redundância significativa, repetindo informações da editora para cada periódico.

</details>

<details><summary>Quais são os três critérios para identificar uma entidade?</summary>

Uma entidade é um objeto com atributos próprios, possui maior importância na narrativa do sistema e se relaciona com outras entidades.

</details>

<details><summary>Qual a principal diferença entre UML e MER para um público leigo?</summary>

Enquanto UML traz noções de orientação a objetos, o MER é um modelo de alto nível mais fácil para um leigo visualizar, pois foca no que realmente se quer saber.

</details>

<details><summary>Qual a distinção entre requisitos funcionais e não funcionais?</summary>

Requisitos funcionais definem o que a aplicação deve executar (processos, funções), enquanto requisitos não funcionais se referem a aspectos do sistema como segurança e desempenho.

</details>

<details><summary>Qual a natureza do modelo de projeto conceitual em relação ao armazenamento de dados?</summary>

O projeto conceitual é um modelo de alto nível que define 'o quê' é necessário (processos, informações, funções, performance), mas não especifica 'como' os dados serão armazenados.

</details>

## Conteúdo

`⏱ 00:00`

### Criando Visões e Abstração

Para utilizar informações base que representem perspectivas diferentes para grupos distintos, você consegue criar visões. Nesta fase, você vai definir tudo isso: se haverá alguma visão, quais são as perguntas, o que precisa ser entendido, o que precisa ser extraído do sistema, quais são as informações, ou melhor, quais são os dados que serão persistidos.

Um conceito importante, vindo do pensamento computacional, é a **abstração**.

> [!definicao] Abstração
> É a necessidade de generalizar, mas para isso é preciso deixar de lado detalhes que são desnecessários para o contexto. O foco é no que realmente é preciso, ignorando os detalhes.

> [!exemplo] Abstração no Contexto de Banco de Dados
> Dentro de uma entidade, existem vários atributos. Alguns atributos têm significado e relevância para o contexto, enquanto outros, apesar de fazerem parte da entidade, não têm relevância alguma. Nesse caso, os atributos irrelevantes não devem ser modelados; eles devem ser deixados de lado, pois não são informações necessárias. É aqui que se verifica essa necessidade.

### Esquema Conceitual

A partir da modelagem e do projeto conceitual, com todas as definições que você terá, você vai definir um **esquema conceitual**. Esse esquema fornecerá a visão gráfica da sua narrativa.

### Exemplo: Periódicos e Editoras

> [!exemplo] Modelagem de Periódicos e Editoras
> Vamos usar o exemplo de periódicos e editoras, que já foi abordado em temas anteriores.
>
> O contexto é um ambiente onde existem revistas. Um periódico geralmente é uma revista, publicado por uma editora. Esse periódico, por sua vez, contém uma série de artigos, e esses artigos são escritos por autores.
>
> Focando nos periódicos e editores, temos um modelo de entidade-relacionamento. Vamos destrinchar esse modelo para entender o que cada linha quer dizer.
>
> `Periódicos` é uma entidade. Dentro da narrativa, identificou-se que o periódico tem importância e não é simplesmente um atributo de uma editora. Com isso em mente, criou-se uma entidade para `Periódicos`.
>
> **Por que `Periódicos` é uma entidade e não um atributo?**
>
> Imagine se `Periódico` fosse um atributo da entidade `Editora`. No primeiro momento, poderia-se até modelar o periódico como atributo. No entanto, ao pensar mais a fundo, você verificaria o seguinte:
>
> Uma editora pode publicar um ou mais periódicos. Se você tiver mais de um periódico sendo publicado pela mesma editora, começará a ter redundância de informação dentro da sua entidade.
>
> **Cenário de Redundância:**
>
> Considere uma tabela ou planilha. Você insere o nome da editora, o país da editora, o código da editora. Em seguida, adiciona a informação do periódico.
>
> Se a editora publica outro periódico, você teria que criar outra linha na tabela, repetindo o nome, país e código da editora, e adicionando o novo periódico. Isso gera uma redundância significativa.
>
> Este exemplo, embora possa parecer simples, é útil para pensar sobre o assunto, pois às vezes a redundância não é imediatamente óbvia.

`⏱ 04:20`

Às vezes, determinar o que será uma **entidade** e o que será um **atributo** fica um pouco subjetivo. Mas, à medida que avançamos, veremos que existem diferentes tipos de atributos, diferentes tipos de relacionamentos e diferentes tipos de entidades. Assim, vamos construindo e fundamentando o conhecimento passo a passo, o que nos permitirá, mais adiante, entender melhor em que caso se encaixa uma determinada entidade fraca, um atributo multivalorado ou uma agregação.

### Identificando Entidades e Atributos

Se há muita redundância, não faz sentido colocar `periódico` como um atributo. `Periódico` tem uma certa importância no meu contexto, então vou criar uma entidade para ele, pois tem atributos relacionados.

> [!exemplo] Periódico como Entidade
> Um `periódico` possui atributos específicos, como o nome e o código (`ISSN`). Além disso, ele é publicado por uma `editora`.
>
> **Como identificar uma entidade:**
> *   Um objeto que possui uma série de atributos próprios.
> *   Tem uma conotação de maior importância dentro da narrativa do sistema.
> *   Relaciona-se com outras entidades. Não faz sentido ter uma entidade que não se relaciona com nenhuma outra.
>
> No nosso cenário, o `periódico` se encaixa nesses critérios, assim como a `editora`.

Um periódico é publicado por uma editora, e uma editora publica um periódico. Faz todo o sentido. Dentro dessa modelagem simples, os dois objetos mais importantes da nossa narrativa são `editora` e `periódico`. A partir daí, podemos definir quais são as editoras e, com esse relacionamento, fazer consultas futuras.

### Validando o Modelo com Perguntas

Podemos perguntar: "Quantas revistas, ou quantos periódicos, existem por cada editora?" ou "Quais editoras possuem o maior número de periódicos, acima de cinco, por exemplo?".

Conseguimos, a partir daqui, representar e responder a determinadas perguntas. Às vezes, você pode se perguntar: "Será que consigo responder a isso? Meu modelo está ok?". Verifique o que você precisa responder. Se você precisa entender algo e consegue responder com esse relacionamento, por exemplo, "Quais são as editoras que mais possuem publicações?", então o modelo está bom.

Se o modelo não consegue encontrar o caminho para sua pergunta (por exemplo, se `periódico` tivesse um relacionamento com `artigo` e você quisesse saber algo sobre isso, mas não modelou), então revise sua prancheta e veja o que aconteceu.

### Modelagem com UML

Estamos tratando aqui do modo da `UML`, que é uma linguagem voltada para o desenvolvimento de software. Ela foi utilizada por muito tempo, mas acaba gerando um efeito em cascata, sendo meio que deixada de lado depois da metodologia ágil.

No entanto, seus diagramas ainda são interessantes. Você não precisa seguir à risca a modelagem voltada para a `UML` ou os movimentos de software em cascata que a `UML` faz. Mas você pode utilizar o `diagrama de classe` e o `diagrama de caso de uso`. Eu digo isso porque, como somos muito visuais, conseguimos entender muito a partir do...

`⏱ 08:40`

Como somos muito visuais, os diagramas são muito interessantes quando você quer modelar ou apresentar para alguém.

### Modelagem com UML e Modelo Entidade-Relacionamento (MER)

O que é interessante no UML? Ele traz a noção de orientação a objetos. Nele, já temos classes, relacionamentos, cardinalidade, atributos e até a ideia de `primary key`.

Isso não acontece com o **Modelo Entidade-Relacionamento (MER)**, que já é um modelo de mais alto nível. Para um leigo, o MER é mais interessante de se visualizar, pois foca no que realmente queremos saber. Ambos podem ser utilizados, mas o MER é o mais comum. O nome desse diagrama é `Diagrama Entidade-Relacionamento`.

### Projeto Conceitual e Requisitos do Sistema

No projeto conceitual, o foco recai um pouco no engenheiro de software, pois é preciso determinar as requisições funcionais da aplicação.

Ao pensar nas operações que precisarão ser feitas, realizadas e submetidas no banco de dados, o enfoque é maior na engenharia de software. Nesse sentido, você pode estar integrado e em conversa com outro time, se forem equipes distintas, para verificar os requisitos do sistema e os requisitos funcionais da sua aplicação, a fim de modelar melhor o projeto conceitual.

O modelo que é originado a partir do projeto conceitual é um modelo de alto nível. A partir dos requisitos definidos para o sistema, que formam a narrativa, serão retirados os **requisitos funcionais** e **não funcionais**.

> [!definicao] Requisitos Funcionais
> São o que a aplicação precisa executar.
> Incluem os processos que serão rodados e os tipos de funções que serão contemplados na aplicação, que acessarão o banco de dados e retornarão informações.
> A ideia de função e de execução está atrelada a esse tipo de requisito.

> [!definicao] Requisitos Não Funcionais
> Estão atrelados ao próprio sistema.
> Envolvem aspectos como segurança e desempenho.
> Nesta etapa do projeto, verifica-se se o projeto será, por exemplo, voltado para um sistema de banco de dados para `OLTP` (Online Transaction Processing), que é um tipo de sistema que exige alta performance.
> Se você precisa de um sistema com maior indexação e acessos mais rápidos a informações específicas, você definirá esses requisitos não funcionais nesta etapa.
> Esses requisitos serão utilizados no projeto físico para garantir a aderência com o que foi modelado no projeto conceitual.

### A Natureza de Alto Nível do Projeto Conceitual

Como mencionado, o projeto conceitual é um modelo de alto nível, o que significa que ele não contém informações sobre como os dados serão armazenados. Ele simplesmente define o *quê*: "preciso desse processo", "preciso que me retorne essas informações", "essas funções têm que ser correspondidas".

Além disso, ele estabelece requisitos como: "preciso que meu sistema seja performático" ou "preciso de acesso rápido a essas informações". Perceba que em momento algum está sendo definido *como* isso vai acontecer. Apenas se constata a necessidade de ter informações de acesso rápido e o que é preciso.

`⏱ 13:00`

informações que você precisa ter de acesso rápido. De termos, já não é preciso que você consiga realizar modificações constantes, e sim que se atualize muito bem.

Dependendo do requisito, você vai definir lá na frente qual será a sua modelagem. Você terá os requisitos funcionais e os não funcionais dentro desse ponto do projeto de banco de dados.

> [!definicao] Esquema Conceitual
> Esse modelo de alto nível, relacionado ao projeto conceitual e o modelo representado pelo **esquema conceitual**, é independente do modelo de banco de dados, como já havia sido comentado.

### Fluxo Iterativo do Projeto Conceitual

Qual seria, então, o fluxo da informação?

- Os dados e requisitos são coletados.
- São analisados.
- Somente então é possível modelar e definir o design conceitual através de um esquema ou de um `DR`.

> [!exemplo] O Processo Iterativo
> Você pode fazer o seguinte: verifiquei os dados e os requisitos funcionais e não funcionais do meu contexto, na minha narrativa. Crio um esquema, volto.
> >
> Cliente, então, vamos alinhar. Se o alinhamento não for exatamente isso, volta, analisa, vê se tem dado faltando, insere e volta. E aí vem de novo para o design.

Portanto, o processo não é engessado; é algo gradual e evolutivo. O esquema conceitual traz conceitos de alto nível e acaba se tornando mais fácil para um leigo conseguir entender o seu modelo.

## Relacionado

- [[modelagem-de-dados-abstracao-e-os-tres-niveis-de-modelos]]
- [[sgbd-atores-tipos-de-usuarios-e-finalidade]]
- [[modelagem-de-dados-requisitos-modelos-conceitual-e-logico]]
- [[modelagem-de-dados-introducao-e-modelo-entidade-relacionamento-mer]]
