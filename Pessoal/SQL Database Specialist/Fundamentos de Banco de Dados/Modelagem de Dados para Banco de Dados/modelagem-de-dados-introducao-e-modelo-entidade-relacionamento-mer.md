---
titulo: "Modelagem de Dados: Introdução e Modelo Entidade-Relacionamento (MER)"
tags: [modelagem-de-dados, banco-de-dados, sgbd, conceitos, fundamentos, engenharia-de-software, mer]
data: 2026-09-27
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 12
conceitos: [Modelagem de Dados, SGBD, Modelo Conceitual, Modelo Físico, Processo de Modelagem, Diagramas UML, Modelo Entidade-Relacionamento (MER), Entidade]
---

# Modelagem de Dados: Introdução e Modelo Entidade-Relacionamento (MER)

> [!resumo] Do que se trata
> Esta aula introduz a modelagem de dados para bancos de dados, explicando sua importância e os benefícios de otimização de tempo e compreensão do sistema. Ela detalha os níveis de modelagem, do conceitual ao físico, e o processo de criação de um esquema. A aula também apresenta o Modelo Entidade-Relacionamento (MER) e suas vantagens para a comunicação com públicos não técnicos.

## Para lembrar

- **A modelagem proporciona uma maior compreensão do sistema e otimiza o tempo de implementação, servindo como representação ou referência para outros cenários.**
- **Os níveis de modelagem para banco de dados incluem o Modelo Conceitual, uma representação gráfica para leigos, e o Modelo Físico, mais relacionado à implementação do sistema.**
- **O processo de modelagem segue o fluxo de definir o contexto, realizar uma representação de alto nível e, posteriormente, definir o esquema.**
- **O Modelo Entidade-Relacionamento (MER) é um modelo de relacionamento que facilita a compreensão para leigos, permitindo definir o conhecimento de forma abstrata e didática.**
- **No MER, uma entidade representa um objeto do mundo real (ex: 'Periódico'), possuindo atributos (características como 'Nome', 'ISSN') e se relacionando com outras entidades (ex: 'Editora').**

## O que esta nota responde

- Por que a modelagem de dados é importante para o desenvolvimento de sistemas?
- Quais são os níveis de modelagem de dados e suas características?
- O que é o Modelo Entidade-Relacionamento (MER) e quais suas vantagens?

## Conceitos

**Modelagem de Dados** · **SGBD** · **Modelo Conceitual** · **Modelo Físico** · **Processo de Modelagem** · **Diagramas UML** · **Modelo Entidade-Relacionamento (MER)** · **Entidade**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Introdução, por que e o que é modelagem | ▪▪ |
| `04:00` | Modelagem SGVDs, níveis, processo e esquemas | ▪▪ |
| `08:00` | UML, MER, exemplo e vantagens | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Modelagem** | A modelagem proporciona uma maior compreensão do sistema e otimiza o tempo de implementação. O intuito é compreender o fenômeno e o contexto em que o sistema está inserido. É a representação, uma referência ou um modelo que servirá de base para outros cenários. |
| **Modelagem para SGVDs** | A modelagem possui foco na descrição e relacionamento dos elementos que compõem a representação do contexto do mundo, do mini mundo. |
| **Periódico** | Para fins de modelagem, um periódico é entendido como uma revista. |

## Pegadinhas

- A UML acabou caindo em desuso por ter um efeito meio cascata, não condizendo com o desenvolvimento de software dinâmico e flexível, sendo substituída por metodologias ágeis.

## Teste-se

<details><summary>Qual o principal objetivo da modelagem de dados?</summary>

A modelagem proporciona maior compreensão do sistema e otimiza o tempo de implementação. Seu intuito é compreender o fenômeno e o contexto em que o sistema está inserido.

</details>

<details><summary>Quais são os dois níveis de abstração da modelagem para banco de dados?</summary>

Os dois níveis são o Modelo Conceitual, uma representação gráfica para leigos, e o Modelo Físico, mais relacionado à implementação do sistema.

</details>

<details><summary>Quais são as duas formas de representar o esquema de um banco de dados mencionadas na aula?</summary>

As duas formas são Entidade-Relacionamento (ER), que é o foco da aula, e Linguagem Unificada para Modelagem (UML).

</details>

<details><summary>Por que a UML perdeu espaço para outras metodologias no desenvolvimento de software?</summary>

A UML acabou caindo em desuso por ter um efeito meio cascata, o que não condiz com o desenvolvimento de software, que é algo mais dinâmico e flexível. As metodologias ágeis tomaram seu lugar.

</details>

<details><summary>Qual a principal vantagem do Modelo Entidade-Relacionamento (MER) para leigos?</summary>

O MER é mais fácil para leigos entenderem, permitindo definir o conhecimento do modelo de forma abstrata e didática. Isso facilita a visualização da interação entre as entidades.

</details>

## Conteúdo

`⏱ 00:00`

Já estamos avançando em nosso tema e agora vou falar um pouco sobre a introdução à **modelagem** de banco de dados e SQL. Primeiro, vamos definir o que é modelagem. Teremos nosso primeiro contato com a modelagem de dados voltada para o cenário de STPDs. Depois, falaremos o que é SQL e alguns comandos básicos. Esta é uma introdução, pois como este módulo é teórico e bem introdutório, quero deixar uma prévia do que vocês verão mais para frente.

### Por que Modelar?

Vamos entender o porquê modelar. Para quem está iniciando, pode parecer que modelar é um passo desnecessário, uma perda de tempo. Mas vamos pensar juntos: por que modelar em um determinado contexto? Tente extrapolar isso para fora da computação, fora da programação. Conseguimos visualizar isso de uma maneira até um pouco mais próxima do nosso dia a dia.

> [!exemplo] A importância da modelagem na prática
> **1. Construção:**
> Ao definir uma planta baixa, o arquiteto ou engenheiro vai ao terreno, analisa a qualidade do solo e uma série de requisitos e *issues*. O terreno define os requisitos mínimos para criar a planta baixa. A partir dessas informações, ele modela o que seria mais interessante para aquele terreno. Esse modelo servirá de base: se for o arquiteto, para o engenheiro que vai aplicar a planta e construir a casa; se for o próprio arquiteto, servirá de consulta e base para gerenciar a construção da casa.
> >
> **2. Desenvolvimento de Produtos:**
> No desenvolvimento de produtos, podemos falar sobre protótipos. Ao inserir um produto novo no mercado, primeiro queremos criar um protótipo para identificar como ele se comporta, se houve algum problema na construção, se a modelagem foi feita corretamente.
> >
> **3. Eletrônicos:**
> Em eletrônicos, temos o esquema de circuitos. Em vez de criar logo milhares de plaquinhas de circuitos para notebooks, tablets, celulares, joguinhos eletrônicos ou carrinhos de controle remoto, criamos um esquema. Entendemos o que é preciso para cada cenário, pois um circuito eletrônico para um carrinho de controle remoto será totalmente diferente de um para um celular. É preciso entender o contexto de cada um e se a modelagem está correta. Imagine não modelar corretamente, não passar por essa fase, e haver um erro no que foi pensado, mas que já está em execução. Errou. Você perdeu dinheiro, perdeu recurso.

A modelagem, na verdade, proporciona uma maior compreensão do sistema e otimiza o tempo de implementação. Quando falamos em implementação do sistema, podemos pensar na construção da casa como implementação, na criação do modelo real a partir do protótipo como implementação, e na criação do circuito integrado como implementação do projeto. O intuito é justamente compreender o fenômeno, o contexto em que seu sistema está inserido.

> [!definicao] Modelagem
> A modelagem proporciona uma maior compreensão do sistema e otimiza o tempo de implementação.
> O intuito é compreender o fenômeno e o contexto em que o sistema está inserido.
> É a representação, uma referência ou um modelo que servirá de base para outros cenários.

A modelagem pode se subdividir em determinados contextos e se classificar de diversas formas. Mas, ao pensar em modelagem, você pensa na representação, em uma referência, em um modelo que servirá de base para outros cenários. E podemos extrapolar isso para...

`⏱ 04:00`

E aí a gente pode extrapolar isso para o software, dados, modelagem computacional, conceitual, projetos de negócio, matemática.

A modelagem matemática usa exclusivamente recursos matemáticos para modelar o fenômeno. No entanto, é possível utilizar essa base matemática para simular computacionalmente.

A modelagem de dados é voltada para o nosso contexto. A modelagem de software está relacionada ao desenvolvimento de um software. Cada tipo de modelagem possui sua especificidade.

### O que é Modelagem?

Para definir de maneira mais formal o que é a modelagem, no contexto de assistência para SGVDs, a modelagem possui foco na descrição e relacionamento dos elementos que compõem a representação do contexto do mundo, do mini mundo.

> [!definicao] Modelagem para SGVDs
> A modelagem possui foco na descrição e relacionamento dos elementos que compõem a representação do contexto do mundo, do mini mundo.

### Níveis de Modelagem

A partir da modelagem para SGVDs, para banco de dados, temos:

*   Uma descrição concisa dos relacionamentos de entidades, como elas estão linkadas e como representam o mini mundo que se deseja refletir através dos dados.

Isso permite abstrair o modelo para níveis mais altos:

1.  **Modelo Conceitual:** É uma representação gráfica mais próxima de algo que leigos podem entender.
2.  **Modelo Físico:** É mais relacionado à parte de implementação do sistema.

### Processo de Modelagem

Pensando nos processos de modelagem, o fluxo é o seguinte:

1.  **Definir o Contexto:** Delimitar o contexto que está inserindo os dados, entendendo o nosso mini-mundo e quais são os requisitos.
2.  **Representação de Alto Nível:** Realizar uma representação de alto nível, onde se cria o modelo.
3.  **Definir o Esquema:** Posteriormente, se define o esquema, que é a estrutura do que os dados terão quando forem persistidos no SGVD (no nosso caso relacional).
4.  **Implementação:** Por último, implementa-se e cria-se o banco de dados dentro do SGVD.

O esquema é crucial. Ele entra para definir e criar uma estrutura de nível mais alto. Ele depende do modelo relacional, mas fornece a estrutura que os dados terão quando forem persistidos e facilita a compreensão do contexto.

### Representação do Esquema

Existem duas formas de representar o esquema:

1.  **Entidade-Relacionamento (ER):** Este é o nosso foco.
2.  **Linguagem Unificada para Modelagem (UML):** Foi muito utilizada durante anos no processo de desenvolvimento de software.

A UML acabou caindo em desuso por ter um efeito meio cascata. As metodologias ágeis tomaram conta do seu lugar. Embora os diagramas não sejam inúteis, a abordagem da UML, por ser mais cascata, não condiz muito com o desenvolvimento de software, que é algo mais dinâmico e flexível.

A modelagem é um passo importante para que seja possível entender os requisitos e definir de maneira apropriada, conseguindo representar, apresentar e responder às perguntas associadas no contexto da melhor maneira possível.

`⏱ 08:00`

a exemplificação para cada uma dessas representativas que nós iremos utilizar para criar o nosso esquema.

### Introdução aos Diagramas UML

O UML (Unified Modeling Language) tem uma série de diagramas associados. Como já comentei, não é que eles sejam inúteis, mas o efeito cascata atrapalha.

Nós temos diversas visões, e essas visões representam uma perspectiva específica dentro do sistema. Cada visão terá um ou mais diagramas associados.

### Modelo Entidade-Relacionamento (MER)

Pensando agora de uma maneira bem geral e superficial no Modelo Entidade-Relacionamento. Eu não vou definir aqui com vocês a estrutura toda de como criar o Modelo Entidade-Relacionamento, pois isso é objeto de um outro módulo.

Mas o que precisamos entender aqui é a maneira gráfica de representar minimamente as informações.

### Exemplo Prático: Periódicos

Vamos começar por periódicos.

> [!definicao] Periódico
> Para fins de modelagem, um **periódico** é entendido como uma revista.

Isso está associado ao ambiente acadêmico, onde os docentes e discentes geralmente publicam. Muitos visam publicar em periódicos porque têm uma nota mais elevada, pois o critério para aprovação geralmente é mais pesado para ter seu artigo publicado na revista.

> [!exemplo] Modelagem de Periódicos
> Começamos com a **entidade** "Periódico".
> >
> Essa entidade possui **atributos** associados, que representam suas características:
> - Nome
> - Identificação (`ISSN`)
> >
> O objeto "Periódico" (uma revista) é publicado, geralmente por uma editora. Isso nos leva a um **relacionamento**:
> - Um periódico é publicado por uma editora.
> - Uma editora pode publicar um ou mais periódicos.
> >
> A construção envolve criar a entidade com seus atributos e, em seguida, identificar uma nova entidade (Editora) e como ela se relaciona com a anterior.

### Vantagens do MER para Leigos

Este é um modelo de relacionamento que geralmente é mais fácil para que leigos possam entender. Se você está lidando com um cliente que não é da área de computação, por exemplo, ou o gerente, ou seu cliente está dentro da sua própria equipe, você vai conseguir definir o conhecimento desse modelo de uma maneira mais abstrata e didática, como serão os requisitos do seu sistema.

O leigo consegue facilmente, depois que ele entende a estrutura, ler aquela informação. Ou ele nem precisa entender a estrutura, mas com você explicando para ele, ele consegue visualizar facilmente como é a interação entre as entidades.

### Próximos Passos na Modelagem

Se a gente explorar a modelagem e tentar puxar outras informações, isso será abordado em um momento posterior. Nós vamos começar a ver a ideia de:
- Instância
- Multiplicidade
- Chaves e regras (`constraints`)
- Integridade de dados
- Requisitos funcionais e não funcionais do sistema

Essas são uma série de informações que estão relacionadas e inseridas dentro desse aspecto da modelagem de dados, onde vamos definir os requisitos funcionais e não funcionais do sistema. Isso a gente vai ver em um momento posterior.

## Relacionado

- [[../Introdução a Banco de Dados/jornada-da-formacao-sql-database-specialist]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-ganhos-e-otimizacao-operacional]]
- [[../Introdução a Banco de Dados/contextualizacao-da-formacao-sql-database-specialist-apresentacao-da-instrutora-]]
- [[../Sistemas de Gerenciamento de Banco de Dados/sgbd-vantagens-otimizacao-e-integridade-dos-dados]]
