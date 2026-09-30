---
titulo: "Bancos de Dados: Definição, Acesso e Escala"
tags: [conceitos, dados, banco-de-dados, sistema, organizacao, fundamentos, sql]
data: 2026-09-14
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [Dados, Banco de Dados (Database), SGBD (Sistema de Gerenciamento de Banco de Dados), API (Application Programming Interface), Consistência de Dados, Escala de Dados, Complexidade de Dados, Persistência de Dados]
---

# Bancos de Dados: Definição, Acesso e Escala

> [!resumo] Do que se trata
> Esta aula define dados como fatos brutos e bancos de dados como conjuntos estruturados que transmitem informação. Ela explora como o acesso a esses dados é frequentemente mediado por APIs e discute a crescente escala e complexidade dos bancos de dados em diversos cenários. A importância da consistência de dados é enfatizada para garantir a confiabilidade das mudanças de estado em um sistema.

## Para lembrar

- **Dados são efetivamente um fato, como um diamante bruto, relacionados a determinado acontecimento, conhecimento ou fenômeno.**
- **Um banco de dados é um conjunto de dados que transmitem informação, evoluindo para um sistema próprio para essa finalidade.**
- **Para que os dados possam fazer sentido e constituir um banco de dados, deve existir um relacionamento entre eles.**
- **O acesso a um banco de dados é realizado via uma API, que atua como intermediário entre o usuário e o sistema.**
- **Para que uma mudança de estado seja confiável, o sistema deve ser acurado o suficiente para passar de um estado válido para outro válido, mantendo a consistência de dados.**

## O que esta nota responde

- Qual a diferença entre dados e banco de dados?
- Como os dados são acessados em um sistema?
- O que é consistência de dados e por que ela é importante?

## Conceitos

**Dados** · **Banco de Dados (Database)** · **SGBD (Sistema de Gerenciamento de Banco de Dados)** · **API (Application Programming Interface)** · **Consistência de Dados** · **Escala de Dados** · **Complexidade de Dados** · **Persistência de Dados**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Bancos de Dados: Definição e Contexto | ▪▪ |
| `04:00` | SGBD, API e Acesso a Dados | ▪▪ |
| `08:00` | Consistência, Escala e Complexidade | ▪▪ |
| `12:00` | Necessidade e Definição de SGBD | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Dados** | Dados são efetivamente um fato. Eles são como um diamante bruto, relacionados a determinado acontecimento, conhecimento ou fenômeno, representando um fato. |
| **Banco de Dados** | É um conjunto, uma coleção de palavras, onde, dentre elas, há um relacionamento. Entre esses dados existe um relacionamento para que eles possam fazer sentido. Essa é uma definição generalista e bem ampla. |
| **SGBD (Sistema Gerenciador de Banco de Dados)** | Um SGBD (Sistema Gerenciador de Banco de Dados), também conhecido como DBMS (Database Management System), é um ambiente específico, voltado para o papel de gerenciamento de dados, onde esses dados representam uma determinada informação. Um SGBD é composto por diversos bancos de dados, cada um com sua estrutura e significado atrelado. |
| **Consistência de Dados** | Para que uma mudança de estado seja confiável, o sistema deve ser acurado o suficiente para passar de um estado válido para outro estado válido. Se houver erro, o sistema precisa ser capaz de retroceder (Ctrl Z) para o estado anterior válido. É fundamental manter o modelo e o estado do banco de dados sempre coerentes e consistentes para que o serviço não pare. |

## Pegadinhas

- Banco de dados não é sinônimo de SGBD. A definição de banco de dados é mais generalista, enquanto SGBD é um ambiente específico para gerenciamento de dados.

## Teste-se

<details><summary>Qual a diferença fundamental entre um Banco de Dados e um SGBD?</summary>

Um Banco de Dados é um conjunto generalista de dados relacionados que transmitem informação. Um SGBD é um ambiente específico para o gerenciamento desses dados, composto por diversos bancos de dados.

</details>

<details><summary>O que são dados, de acordo com a aula?</summary>

Dados são efetivamente um fato, como um diamante bruto, relacionados a determinado acontecimento, conhecimento ou fenômeno. Eles representam um fato que precisa ser lapidado para se transformar em informação.

</details>

<details><summary>Qual a função de uma API no acesso a dados?</summary>

A API atua como uma interface para acessar dados, permitindo que um sistema (cliente) solicite informações ou execute ações em outro sistema (backend/banco de dados) sem precisar conhecer os detalhes internos de como a operação é realizada.

</details>

<details><summary>O que significa a consistência de dados em um SGBD?</summary>

Consistência de dados significa que o sistema deve garantir que, ao passar de um estado para outro, ambos os estados sejam válidos. Se uma mudança levar a um erro, o sistema deve ser capaz de retroceder para o estado anterior válido, mantendo a coerência.

</details>

<details><summary>Cite um exemplo de como a complexidade dos dados se manifesta em redes sociais.</summary>

Em redes sociais como o Facebook, a complexidade se manifesta na variedade de tipos de dados persistidos, como posts, mensagens de chat, conexões de amigos, likes e análises para sistemas de recomendação.

</details>

## Conteúdo

`⏱ 00:00`

Fizemos nossa contextualização sobre esse mundo de dados e agora precisamos entender o que são bancos de dados. Diferentemente do que nos acostumamos a falar, **banco de dados** não é sinônimo de SGVDs. Muitas vezes falamos de um BD como se fosse um SGVD. Sim, realmente. Mais à frente, podemos até mesclar essas duas palavras e não há problema em utilizá-las como sinônimos. No entanto, precisamos entender qual é a diferença entre elas.

Nosso objetivo é prover serviços para as pessoas, na maioria dos casos. Temos diversos cenários distintos onde serviços diferentes podem estar sendo prestados, e há dados associados a eles. Temos cenários como engenharia, negócios, e-commerce, medicina, redes sociais, uma série de cenários onde precisamos desses dados.

Esses dados geralmente vêm em conjunto. Não é um dado específico de uma pessoa, uma única unidade. Eles vêm em conjunto, e esses conjuntos possuem uma determinada estrutura.

### O que são Dados?

Já que o dado vem dentro de uma estrutura, o que é dado de fato?

> [!definicao] Dados
> Dados são efetivamente um fato. Eles são como um diamante bruto, relacionados a determinado acontecimento, conhecimento ou fenômeno, representando um fato.

Esse fato precisa ser lapidado. Precisamos pegar aquele fato, entender o que ele está querendo dizer e transformá-lo em informação. Antes dessa parte de análise acontecer, esses dados são persistidos, são armazenados em algum lugar. Daí que vem a ideia de *databases*.

### Bancos de Dados (Databases)

> [!definicao] Banco de Dados
> Um banco de dados é um conjunto de dados que transmitem informação. Inicialmente, a ideia de *databases* era mais geral, não apenas para armazenar. Posteriormente, a ideia do *database* evoluiu para um sistema próprio para essa finalidade.

Até então, tínhamos uma abordagem chamada tradicional, onde a aplicação determinava o comportamento, a estrutura e o gerenciamento dos dados. Temos uma infinidade de informações, desde uma escala menor até uma maior. Esses dados (não informações) transmitem algum tipo de significado, e precisamos entendê-los. Assim, conseguimos montar a estrutura de um sistema, de uma aplicação.

### Exemplo: Agenda de Contatos no Celular

> [!exemplo] Agenda de Contatos no Celular
> Pense no seu celular, que é mais potente que um computador de 20 anos atrás. Ele possui um cadastro onde o software gerencia informações.
> >
> Existe uma biblioteca de C, chamada `SQLite`, que pode ser usada para fazer todo esse gerenciamento das informações.
> >
> No seu celular, você já tem esse tipo de coisa: nome, telefone, e-mail, WhatsApp. Isso representa um campo bem simplificado, uma maneira bem simplificada de representar o cadastro, a agenda dos seus contatos no celular.
> >
> Você tem dados que informam, que fornecem um significado relacionado a "isso aqui é um contato". É o contato de uma pessoa, e aqui estão as maneiras que posso me comunicar com ela. É isso que temos quando olhamos para um cadastro, para uma agenda de contato dentro do celular. E é isso que podemos considerar como banco de dados: um conjunto, uma coleção de palavras.

`⏱ 04:00`

é um conjunto, uma coleção de palavras, e, dentre elas, há um relacionamento. Entre esses dados existe um relacionamento para que eles possam fazer sentido, e isso constitui um banco de dados.

> [!definicao] Banco de Dados
> É um conjunto, uma coleção de palavras, onde, dentre elas, há um relacionamento. Entre esses dados existe um relacionamento para que eles possam fazer sentido. Essa é uma definição generalista e bem ampla.
> >
> Um **SGBD** (Sistema Gerenciador de Banco de Dados) é um ambiente específico, voltado para o papel de gerenciamento de dados, onde esses dados representam uma determinada informação. Um SGBD é composto por diversos bancos de dados, cada um com sua estrutura e significado atrelado.

Se pensarmos agora em um cenário mais restrito, podemos fazer um paralelo com esse conjunto de dados e entender que, dentro de um SGBD, nesse cenário mais restrito, existe um contexto. Estaremos representando um determinado contexto do mundo real, onde os dados ali precisam ter coerência e um propósito associado.

O uso mais restrito e relacional de um SGBD acaba sendo utilizado como sinônimo de banco de dados, mas a definição de banco de dados é mais generalista. Em termos de conjunto, um banco de dados pode ser um emaranhado de informações relacionadas a determinada situação, não tão coerente como seria uma representação dentro de um SGBD.

### Acesso a Dados e APIs

Como você acessa esse tipo de informação? Você tem diversas fontes distintas produzindo dados. Esses dados acabam sendo persistidos em algum lugar e gerenciados por algum tipo de software. Você precisará acessar esses dados através de uma **API**. Geralmente, na maioria das situações, o acesso a um banco de dados é realizado via uma API.

Por exemplo, a situação de quando você vai ao banco, dentro do caixa, e consegue as informações da sua conta, aquilo é uma API.

Para entender melhor a ideia de `API`, vamos usar uma analogia muito comum:

> [!exemplo] A analogia do restaurante e do garçom para `API`
> Você chega no restaurante e não precisa saber como o chefe de cozinha vai executar seu prato. Você pega o menu, escolhe o prato número 2 e chama o garçom.
> >
> O garçom pega seu pedido e leva até o chefe. O chefe de cozinha executa o pedido sem precisar saber quem o solicitou. Ele simplesmente pega uma requisição e devolve a resposta.
> >
> Por sua vez, a pessoa que solicitou (você) só recebe a informação. Você não precisa saber como o chefe de cozinha fez o prato ou qual processo o garçom utilizou para trazê-lo.
> >
> Nesse cenário:
> - O **garçom** é a `API`. Ele é a interface entre você (o cliente) e a cozinha (o sistema que processa os dados).
> - O **menu** é a documentação da `API`, mostrando o que está disponível.
> - O **chefe de cozinha** é o sistema de *backend* (o banco de dados e a lógica de negócios).
> - O **prato** é a informação ou o resultado da operação.

Quando você acessa dados de alguma forma, você está executando ações, seja para consulta, modificação ou atualização. Essas ações implicam em uma mudança de estado.

Em SGBDs, quando você executa uma determinada ação via uma linguagem específica utilizada pelo SGBD, você está trazendo o banco de dados de um estado original para um estado subsequente. Assim, você caracteriza uma mudança de estado através de uma atualização da base.

`⏱ 08:00`

E aí, a gente precisa fazer o seguinte: esse sistema, para que ele permita que essa mudança seja confiável, ou seja, que eu precise passar de um estado válido para outro estado válido. Não adianta pegar meu estado original, que está tudo certinho, fazer uma modificação e levar a erro. Isso não pode acontecer.

> [!definicao] Consistência de Dados
> Para que uma mudança de estado seja confiável, o sistema deve ser acurado o suficiente para passar de um estado válido para outro estado válido. Se houver erro, o sistema precisa ser capaz de retroceder (`Ctrl Z`) para o estado anterior válido.
>
> É fundamental manter o modelo e o estado do banco de dados sempre coerentes e **consistentes** para que o serviço não pare.

Se a mudança for efetivada com sucesso, ela é prática e terá um reflexo praticamente imediato. Haverá um delay operacional em relação ao clock do sistema, ao tempo de execução da ação e à persistência dos dados (modificação da base pelo SGBD), mas o resultado é quase instantâneo.

### A Escala dos Bancos de Dados

O que vai mudar, na verdade, é o tamanho. Você terá desde centenas de instâncias e registros até bilhões de registros. Pense em uma rede social. Um exemplo é um sistema de consulta de uma biblioteca.

Você terá desde uma coisa mais simples, que um smartphone lida, até algo que precisa de um processamento bem parrudo, relacionado a redes sociais, a uma estrutura gigantesca de um banco, como o Itaú, ou então uma empresa que processa muita informação, como a Petrobras. A escala é que vai mudar.

### Complexidade e Variedade dos Dados

O que mudou realmente desde aquele tempo? Por que há uma escala tão grande? Por que bilhões de registros? E por que uma variedade tão grande?

> [!exemplo] Complexidade em Redes Sociais (Facebook)
> Uma empresa como o Facebook apresenta grande complexidade devido aos seus tipos de dados persistidos:
> - Posts
> - O próprio chat do Facebook, o `Messenger`
> - A questão dos amigos (`friends`) e as conexões entre eles
> - Análise das conexões para sugerir novos amigos (sistema de recomendação)
> - Likes
>
> Todas essas informações, dentro do contexto de rede social, agregam em termos de complexidade para o gerenciamento desses dados.

### Mensurando o Tamanho dos Bancos de Dados

Vamos pensar no que são bancos de dados em termos de tamanho, só para conseguir mensurar.

> [!exemplo] Escala de Dados na Amazon
> A Amazon, em uma pesquisa anterior, possuía:
> - 60 milhões de usuários (atualmente, certamente mais)
> - 42 terabytes de informação
>
> Para tratar essa quantidade de dados, é necessário um SGBD distribuído de alta performance. A Amazon provavelmente utiliza modelos relacionais, NoSQL e distribuídos (sendo que o distribuído geralmente é NoSQL, mas modelos relacionais também podem ser distribuídos). Isso serve para dar uma noção do tamanho da situação.

Dificilmente se encontrará o cenário antigo onde as informações eram acessadas manualmente e todo o gerenciamento era feito através da própria programação, de uma maneira mais tradicional.

`⏱ 12:00`

Dificilmente você vai ter aquele cenário antigo onde você vai acessar as informações manualmente e fazer todo o gerenciamento dele através da própria programação, de uma maneira mais abordada, mais tradicional. Em vez disso, você vai ter um sistema fazendo esse gerenciamento.

Com certeza, grandes ou pequenas empresas hoje em dia precisam de um `SGBD`. Dificilmente você vai ver um cenário onde isso não se aplica.

> [!definicao] Sistema de Gerenciamento de Banco de Dados
> Esse sistema, como já comentado, é denominado `SGBD`, ou seja, **Sistema de Gerenciamento de Banco de Dados**.
> Também é conhecido como `DBMS` (`Database Management System`).

Essa é a contextualização do porquê do banco de dados e do porquê de utilizar o sistema de banco de dados, de uma maneira bem superficial. A próxima etapa abordará o que é exatamente o sistema de macros de dados.

## Relacionado

- [[contextualizacao-da-formacao-sql-database-specialist-apresentacao-da-instrutora-]]
- [[bancos-de-dados-da-evolucao-ao-big-data]]
- [[01 - Conceitos Banco de Dados]]
- [[01 - Conceitos Básicos]]
