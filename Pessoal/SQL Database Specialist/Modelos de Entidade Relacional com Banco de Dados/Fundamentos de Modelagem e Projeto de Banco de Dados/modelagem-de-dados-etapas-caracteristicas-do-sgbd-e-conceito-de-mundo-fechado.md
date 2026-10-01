---
titulo: "Modelagem de Dados: Etapas, Características do SGBD e Conceito de Mundo Fechado"
tags: [modelagem-de-dados, sgbd, banco-de-dados, conceitos, fundamentos, sql, sistema]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 10
conceitos: [Modelagem de Dados, SGBD (Sistema Gerenciador de Banco de Dados), Projeto Conceitual, Projeto Lógico, Projeto Físico, Integridade e Consistência de Dados, Controle de Concorrência, Mundo Fechado]
---

# Modelagem de Dados: Etapas, Características do SGBD e Conceito de Mundo Fechado

> [!resumo] Do que se trata
> Esta aula introdutória aborda a modelagem de dados para SGBDs, detalhando suas etapas de design (conceitual, lógico e físico) e a relação com o desenvolvimento de aplicações. Ela explora as características essenciais de um SGBD, como controle de acesso, persistência, integridade, segurança, recuperação e concorrência, destacando suas vantagens sobre métodos tradicionais. Por fim, a aula define o conceito de Mundo Fechado, fundamental para a lógica formal de sistemas de banco de dados relacionais, e o contrasta brevemente com a Open World Assumption.

## Para lembrar

- **As etapas que compõem o processo de modelagem de dados para um SGBD são: projeto conceitual, projeto lógico e projeto físico.**
- **Um SGBD retira da aplicação a obrigatoriedade do gerenciamento de dados, controlando acesso, persistência, estado do sistema e concorrência, o que garante maior isolamento programa-dados e consistência.**
- **A integridade e consistência dos dados em um SGBD garantem que o sistema não passe de um estado válido para um estado com erro, revertendo transações em caso de falha.**
- **O controle de concorrência em um SGBD gerencia o acesso simultâneo a dados, bloqueando tabelas ou entidades em edição para outros usuários.**
- **O conceito de Mundo Fechado, aplicado ao modelo relacional, afirma que o que estiver fora do escopo ou contexto definido (mini-mundo) é considerado falso.**

## O que esta nota responde

- Quais são as etapas do processo de modelagem de dados para um SGBD?
- Quais as principais características e vantagens de um SGBD em comparação com a abordagem tradicional de gerenciamento de dados?
- O que significa o conceito de Mundo Fechado no contexto de um SGBD e modelo relacional?

## Conceitos

**Modelagem de Dados** · **SGBD (Sistema Gerenciador de Banco de Dados)** · **Projeto Conceitual** · **Projeto Lógico** · **Projeto Físico** · **Integridade e Consistência de Dados** · **Controle de Concorrência** · **Mundo Fechado**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Introdução e Etapas da Modelagem | ▪▪ |
| `04:20` | Características e Vantagens do SGBD | ▪▪ |
| `09:00` | Mundo Fechado e Modelos de BD | ▪▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Integridade dos Dados** | O SGBD mantém um estado válido dos dados. Se houver algum tipo de operação dentro de uma transação em que um erro é ocasionado, aquela transação é revertida, ou seja, o estado anterior volta a ser o válido. Ele não permite que o sistema passe de um estado válido para um estado com erro. |
| **Mundo Fechado** | Este conceito é uma proposição que determina uma afirmação: dentro do contexto a ser modelado, toda informação contida no SGBD pode ser utilizada para responder perguntas. O que está fora do escopo ou domínio não pode ser respondido e, consequentemente, é considerado negativo ou falso. |

## Pegadinhas

- O conceito de Mundo Fechado assume que o que não está no escopo é falso, enquanto o Open World Assumption atribui uma probabilidade ao que não consta no domínio.

## Teste-se

<details><summary>Quais são as três etapas que compõem o processo de modelagem de dados para um SGBD?</summary>

As etapas são projeto conceitual, projeto lógico e projeto físico.

</details>

<details><summary>Cite duas vantagens de se utilizar um SGBD em comparação com a abordagem tradicional de gerenciamento de dados.</summary>

O SGBD oferece controle de acesso, controle de persistência dos dados, manutenção do estado do sistema, controle de concorrência e isolamento programa-dados.

</details>

<details><summary>O que o SGBD garante em relação à integridade dos dados?</summary>

O SGBD garante que os dados mantenham um estado válido. Se uma transação causar um erro, ela é revertida para o estado anterior, impedindo que o sistema passe para um estado inválido.

</details>

<details><summary>Qual é a principal afirmação do conceito de Mundo Fechado?</summary>

O conceito de Mundo Fechado afirma que toda informação contida no SGBD pode ser usada para responder perguntas. O que está fora do escopo ou domínio é considerado negativo ou falso.

</details>

<details><summary>Qual conceito se contrapõe ao Mundo Fechado e qual sua característica principal?</summary>

O conceito que se contrapõe é o Open World Assumption. Nele, se a informação não consta no domínio, é fornecida uma probabilidade de ser verdadeira ou falsa.

</details>

## Conteúdo

`⏱ 00:00`

Olá! Vamos ingressar agora em uma parte introdutória relacionada à modelagem de banco de dados. Neste tema específico, falaremos de modelagem de dados para representar todos os dados que queremos persistir no banco de dados. Para isso, precisamos da modelagem, e existe uma metodologia que você utiliza para modelar um determinado contexto que se deseja representar dentro de um SGBD.

O objetivo desta parte é revisar alguns conceitos relacionados a **SGBD**, como "mundo fechado" e "mini mundo", definindo cada termo antes de entrarmos efetivamente na parte de modelagem. Esses conceitos são importantes porque precisamos definir e delimitar como será a modelagem lógica do sistema. Para isso, é preciso entender as premissas associadas, e daí poder partir para a representatividade, ou seja, representar os objetos relacionados ao contexto em que o problema a ser modelado está inserido.

### Etapas da Modelagem de Dados

Esta é a parte de design. Abordaremos a implementação do modelo e os requisitos do sistema. Falarei brevemente sobre:
- Projeto conceitual
- Projeto lógico
- Projeto físico

Essas são as etapas que compõem o processo de modelagem de dados para um SGBD. Também discutiremos como o desenvolvimento de aplicações e de SGBDs estão entrelaçados, pois um está relacionado ao outro. Ambos visam prover um tipo de serviço, e geralmente uma aplicação é associada a um SGBD. Apresentarei alguns exemplos para ilustrar esta aula teórica.

### Características de um SGBD

Vamos agora conversar sobre as características de um banco de dados. Antes de falar sobre termos específicos, quero relembrar algumas características de um **SGBD** quando comparado a uma abordagem tradicional de gerenciamento e manutenção de dados. Na abordagem tradicional, que já comentamos, utilizávamos a própria aplicação para criar e lançar os dados.

Nesse modelo, observamos uma série de questões, como inconsistência e a dificuldade de ter um bom isolamento do programa de dados. Há uma série de problemas associados a isso, e uma série de vantagens quando se utiliza um SGBD.

Com o SGBD, você retira da aplicação a obrigatoriedade do gerenciamento de dados, passando esse papel para um sistema específico. Ele controla o acesso, a persistência dos dados, mantém o estado do sistema e controla a concorrência. Há uma série de questões inerentes a um SGBD que trazem uma vantagem enorme quando passamos essa função de lidar com os dados da aplicação para um SGBD. O próprio isolamento programa-dados é uma consequência disso.

| Abordagem Tradicional (Problemas) | SGBD (Vantagens/Características) |
|---|---|
| Inconsistência | Controle de acesso |
| Dificuldade de isolamento programa-dados | Controle de persistência dos dados |
| | Manutenção do estado do sistema |
| | Controle de concorrência |
| | Isolamento programa-dados |

Antigamente, se houvesse alguma modificação no arquivo onde os dados estavam contidos, teríamos um problema em que boa parte da aplicação teria que ser [inaudível].

`⏱ 04:20`

boa parte da aplicação teria que ser refeita, ou pelo menos a parte que era baseada, a parte da aplicação construída com base em toda a estrutura que estava dentro daquele arquivo. Quando nós passamos essa função de lidar com os dados para o SGBD, conseguimos maior isolamento. Consequentemente, há uma maior consistência dentro do programa e menor mutabilidade, ou seja, uma menor mutação. Mexemos muito menos no código quando há alguma modificação dos dados.

### Integridade e Consistência

O SGBD vai manter um estado válido dos dados. Sempre que houver algum tipo de modificação na base, no banco de dados, o SGBD é responsável por manter a **integridade** desses dados.

> [!definicao] Integridade dos Dados
> O SGBD mantém um estado válido dos dados. Se houver algum tipo de operação dentro de uma transação em que um erro é ocasionado, aquela transação é revertida, ou seja, o estado anterior volta a ser o válido. Ele não permite que o sistema passe de um estado válido para um estado com erro.
> >
> Se existe algum tipo de equívoco na hora de realizar uma `query` que está dentro de uma determinada organização, o SGBD vai tratar aquele erro voltando para o estado anterior.

### Segurança

Com relação à segurança, além de uma maior restrição no acesso dos dados, os dados estão seguros em um sistema à parte e não na própria aplicação. Ganhamos, assim, uma camada a mais de segurança.

Com relação à restrição dos dados, temos alguns mecanismos. Um deles, por exemplo, são as `views`. A partir de uma base já consolidada no SGBD, conseguimos criar diferentes perspectivas para grupos específicos de usuários do SGBD.

### Recuperação

A recuperação, através da álgebra relacional que o modelo relacional traz, é muito mais facilitada. Utilizando a teoria de conjuntos, perceberemos no decorrer do tempo que podemos realizar `queries` simples que retornam uma quantidade de dados significativa. A recuperação dos dados é facilitada nesse sentido, quando utilizamos o SGBD.

### Controle de Concorrência

O controle de concorrência, seja para concorrência de transações, ou quando uma pessoa acessa uma tabela ou entidade e realiza uma modificação, é gerenciado. Essa tabela será bloqueada para qualquer outro usuário enquanto estiver sendo editada.

Existem diretrizes que você definirá dentro do seu projeto, determinando como será o controle de concorrência. Tudo isso ocorre de uma maneira muito mais fácil dentro de um SGBD do que se você desenvolver a sua aplicação para prever todas essas situações.

### O Conceito de Mundo Fechado

Feita essa revisão, vamos conversar sobre o conceito que delimita e traz uma lógica formal para o sistema de um SGBD, e para o sistema como um todo, que extrapola um banco de dados específico que está persistindo no sistema, aplicando-se a todo o modelo relacional: o conceito de **Mundo Fechado**.

> [!definicao] Mundo Fechado
> Este conceito é uma proposição que determina uma afirmação: dentro do contexto a ser modelado, toda informação contida no SGBD pode ser utilizada para responder perguntas. O que está fora do escopo ou domínio não pode ser respondido e, consequentemente, é considerado negativo ou falso.
> >
> É uma afirmação em cima de um predicado, ou seja, de uma ação sobre o sujeito.

[inaudível]

`⏱ 09:00`

Consequentemente, é negativo, é falso. É isso o que o **conceito de mundo fechado** traz. Ele é uma afirmação em cima de um predicado, ou seja, de uma ação sobre o sujeito. Esse conceito de mundo fechado é uma proposição utilizada para o **modelo relacional**.

Ele está relacionado ao contexto, e esse contexto é o que determina se é verdade ou não.

> [!definicao] Conceito de Mundo Fechado
> O que estiver fora do meu escopo, o que não está contemplado no meu contexto, no meu mini-mundo, é falso.

Essa ideia de mundo fechado se contrapõe a um outro conceito, chamado de **Open World Assumption**. Nesse outro conceito, se a informação não consta no meu domínio e não está persistida nos meus dados, eu vou fornecer uma probabilidade daquilo ser verdadeiro ou falso.

### Modelos de Banco de Dados

Ao abordar a Open World Assumption, entramos na seara dos **bancos probabilísticos**.

O nosso modelo aqui é relacional, e é o que trata a maioria dos problemas. Ainda hoje é dessa forma.

Nós temos a vertente do `NoSQL`, que é sim aplicada para cenários específicos e traz várias vantagens. Mas o **modelo relacional** ainda é o que garante a maior parte dos problemas e que compõe a maior parte das soluções voltadas para dados.

## Relacionado

- [[jornada-da-formacao-sql-database-specialist]]
- [[modelagem-de-dados-abstracao-e-os-tres-niveis-de-modelos]]
- [[contextualizacao-da-formacao-sql-database-specialist-apresentacao-da-instrutora-]]
- [[modelagem-de-dados-introducao-e-modelo-entidade-relacionamento-mer]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `preposição → proposição`
