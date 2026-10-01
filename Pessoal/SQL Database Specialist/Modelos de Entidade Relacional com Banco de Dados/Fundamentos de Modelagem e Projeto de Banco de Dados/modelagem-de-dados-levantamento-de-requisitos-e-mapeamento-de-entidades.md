---
titulo: "Modelagem de Dados: Levantamento de Requisitos e Mapeamento de Entidades"
tags: [modelagem-de-dados, banco-de-dados, fundamentos, conceitos, sql, sgbd, dados]
data: 2026-10-01
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 15
conceitos: [Levantamento de Requisitos, Entidade, Atributo, Relacionamento, Cardinalidade, Atributo Gerado, Projeto Lógico, Projeto Físico]
---

# Modelagem de Dados: Levantamento de Requisitos e Mapeamento de Entidades

> [!resumo] Do que se trata
> A aula aborda o processo de modelagem de dados para uma aplicação, começando pelo levantamento de requisitos e a identificação de entidades como empregados, projetos e departamentos. Ela detalha a definição de atributos para cada entidade e o estabelecimento de relacionamentos entre elas, como a supervisão de um departamento por um empregado. Por fim, explica o mapeamento do modelo conceitual e lógico para um modelo relacional, transformando entidades e relacionamentos em tabelas e atributos estruturados.

## Para lembrar

- **O processo inicial de modelagem de dados envolve levantar requisitos, coletar dados e analisar as entidades e seus relacionamentos.**
- **A cardinalidade é o conceito que define em números como o relacionamento entre diferentes entidades acontece.**
- **Um atributo gerado não é armazenado diretamente no banco de dados, mas sim calculado a partir de uma consulta a outros atributos existentes, como a idade a partir da data de nascimento.**
- **O projeto lógico de um banco de dados utiliza o modelo relacional para definir as tabelas e seus atributos de forma estruturada.**
- **No projeto físico, são criados os comandos SQL para persistir as informações no banco de dados, com base nos requisitos da aplicação.**

## O que esta nota responde

- Como iniciar o processo de modelagem de dados para uma nova aplicação?
- Quais são os elementos fundamentais (entidades, atributos, relacionamentos) a serem considerados na modelagem de dados?
- Qual a distinção entre as fases de projeto lógico e projeto físico na criação de um banco de dados?

## Conceitos

**Levantamento de Requisitos** · **Entidade** · **Atributo** · **Relacionamento** · **Cardinalidade** · **Atributo Gerado** · **Projeto Lógico** · **Projeto Físico**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Modelagem de dados: entidades e requisitos | ▪▪ |
| `04:20` | Atributos, relacionamentos e dependentes | ▪▪ |
| `08:20` | Modelo Entidade-Relacionamento e fluxo | ▪▪ |
| `13:00` | Álgebra relacional e consultas | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Atributo Gerado** | Um atributo que não é armazenado diretamente, mas sim calculado a partir de uma consulta a outros atributos existentes. |

## Teste-se

<details><summary>Quais são as três entidades principais usadas como exemplo para rastreamento de informações?</summary>

As três entidades principais são Empregados, Projetos e Departamentos.

</details>

<details><summary>O que a cardinalidade representa no levantamento de requisitos?</summary>

A cardinalidade representa o conceito de entender em números como o relacionamento entre entidades acontece.

</details>

<details><summary>Qual é a definição de um atributo gerado?</summary>

Um atributo gerado é aquele que não é armazenado diretamente, mas sim calculado a partir de uma consulta a outros atributos existentes.

</details>

<details><summary>Quais são as três etapas do fluxo de modelagem de dados apresentado?</summary>

As três etapas são: Modelagem Conceitual (DER), Projeto Lógico (Modelo Relacional) e Projeto Físico (SQL / Banco de Dados).

</details>

<details><summary>Por que o relacionamento `works on` (esforço) é tratado como uma entidade de relacionamento?</summary>

Ele é tratado como uma entidade de relacionamento porque possui atributos próprios, o que faz sentido no mapeamento do Entidade-Relacionamento para o Relacional.

</details>

<details><summary>Em que conceitos a álgebra relacional se baseia?</summary>

A álgebra relacional se baseia na ideia de teoria de conjuntos.

</details>

## Conteúdo

`⏱ 00:00`

Vamos finalizar este assunto introdutório sobre o projeto de bloco de dados, focando na modelagem de dados de uma aplicação.

> [!exemplo] Exemplo de rastreamento de dados
> Uma empresa precisa rastrear informações de alguns objetos relacionados ao seu contexto. Esses objetos são:
> - Empregados
> - Projetos
> - Departamentos
>
> Não estou definindo detalhadamente o processo, apenas apresentando essas três entidades sobre as quais precisamos rastrear informações.

### Levantamento de Requisitos

Primeiro, precisamos levantar os requisitos relacionados a essas entidades. Isso envolve entender:
- Quais são os atributos.
- Como elas se relacionam entre si.
- Se há algum tipo de restrição.

A **cardinalidade**, que veremos mais para frente, levaria ao conceito de entender em números como esse relacionamento acontece.

O processo inicial é: levantar requisitos, levantar os dados e analisar.

### Entidade: Departamento

A primeira entidade que vamos analisar é o Departamento. A descrição do mini-mundo relacionada ao departamento inclui:
- Nome
- Número
- Gerente (que é um empregado)

Também precisamos rastrear informações interessantes, como a data de início do gerente e o local relacionado ao departamento.

Dentro de Departamento, temos o nome, o número, o gerente e a data de início desse gerente. Além disso, precisamos guardar a informação de qual local o departamento está situado.

> [!exemplo] Localização de Departamentos
> Considere uma empresa como a Petrobras, que possuía vários prédios no centro do Rio de Janeiro. Dependendo do tipo de departamento e de um Sistema de Banco de Dados (SBD) integrado e distribuído, é necessário refletir as informações de localização.
>
> Por exemplo, um departamento pode estar no prédio principal, enquanto outro está no edifício Castelo. O local define exatamente onde o departamento está.

### Entidade: Projetos

Outra questão a ser levantada são os Projetos. Um projeto pode ter um ou mais empregados. Posso ter vários projetos em andamento.

As características desses projetos são:
- Nome
- Número
- Localização

Este projeto estará relacionado ao departamento. A função do departamento é gerenciar ou controlar esses projetos e seus andamentos.

De maneira bem simplificada, os projetos têm nome, número e localização. Eles poderiam ter outros atributos, mas estou simplificando para facilitar a visualização e o entendimento.

### Entidade: Empregados e Relacionamentos

Agora podemos organizar as relações:
- Empregados participam de projetos.
- Projetos são relacionados ao departamento.
- Empregado está relacionado ao departamento (pois pertence a um departamento).

Isso fecha um ciclo de relacionamentos.

Os atributos do Empregado são:
- Nome
- Seguro Social
- Endereço
- Salário

`⏱ 04:20`

Um empregado tem nome, seguro social, endereço, salário, dados de nascimento, entre outras informações que podem constar aqui. Novamente, é apenas para exemplificação.

No meu contexto, o empregado tem dependentes. Faz sentido mapear essa informação, pois ela é relevante para a empresa.

> [!exemplo] A relevância dos dependentes
> Em empresas que seguem o modelo CLT, por exemplo, o empregado terá um plano de saúde e poderá incluir seus dependentes. Pode haver alguma taxa ou desconto, mas o importante é que, se houver dependentes, eles poderão ser incluídos no plano de saúde. Essa informação é relevante para a empresa.

Até agora, discutimos de forma superficial. Por exemplo, não expliquei o que significa um atributo com uma elipse pontilhada, nem uma hierarquia de atributos. Isso ficará no ar por enquanto, mas é um pouco intuitivo. Por exemplo, um nome é composto por outras partes. Vamos construir essa ideia e conceito aos poucos.

O que conseguimos definir é que o empregado tem dependentes, participa de projetos, e projetos estão relacionados ao departamento. Os empregados estão relacionados a departamentos porque pertencem a eles. Ou seja, um empregado trabalha para um departamento. Isso já vimos.

### Supervisão

A parte de supervisão não foi abordada em nosso brainstorming ou narrativa anterior. Supondo que o brainstorming fosse o primeiro contato com o contexto a ser modelado, ao apresentar o modelo ao cliente, ele poderia questionar: "Os empregados são supervisionados por alguém?". E, ao descobrir que "é outro empregado", já podemos modelar que um empregado é supervisionado por outro empregado. Mas, deixemos isso de lado por enquanto.

### Gerenciamento de Departamento

Um empregado trabalha para um departamento e também gerencia. Essa ideia já foi vista antes, pois percebemos em nosso brainstorming que um departamento tem um gerente. Portanto, podemos definir, por meio de um **relacionamento**, que um empregado pode gerenciar um departamento.

Definiremos em detalhes o que é o relacionamento e como criá-lo mais adiante. A ideia é construir o conhecimento aos poucos, para que, ao ver como um relacionamento é criado, você entenda o motivo de certas escolhas feitas anteriormente.

### Projeto e Departamento

Entendemos essa parte. O próximo é o projeto. O projeto está relacionado ao departamento. Na verdade, um departamento controlará o projeto, que é o que queríamos representar. Um ou mais projetos são controlados por um departamento.

Há outra relação: empregados estão relacionados a projetos. Qual o papel do empregado nesse contexto? Ele trabalhará em um projeto.

`⏱ 08:20`

trabalham em projetos, e um projeto pode ter diversos empregados.

Qual é o outro relacionamento que existe? É o dependente. O empregado possui dependente, e o dependente, por sua vez, depende de um empregado.

Essa ideia que queremos passar é que temos os seguintes relacionamentos:

*   Empregado $\leftrightarrow$ Projeto
*   Departamento $\leftrightarrow$ Projeto
*   Empregado $\leftrightarrow$ Departamento

O que verificamos até agora é isso. O restante será entendido conforme avançamos e nos aprofundamos no modelo Entidade-Relacionamento. Esse é o foco da nossa próxima etapa.

### Modelo de Dados e Relacionamentos

Antes de entrar a fundo no modelo de Entidade-Relacionamento, é importante notar que aquela outra anotação que comentei, que é o ML, também é interessante. Ela pode ser utilizada, mas não é obrigatória.

O modelo de relacionamento é realmente mais utilizado do que o ML.

Quando falamos de uma entidade, como a entidade Empregado, estamos dizendo que temos:

1.  O nome.
2.  Os atributos (as características daquela entidade).
3.  As operações.

Por exemplo, temos o nome, o SSN, a data de aniversário (`birthday`), o endereço (`address`) e o salário.

> [!definicao] Atributo Gerado
> Um atributo que não é armazenado diretamente, mas sim calculado a partir de uma consulta a outros atributos existentes.

Não guardamos um atributo chamado `age` (idade). Este deve ser um atributo gerado a partir de uma consulta, pois faz mais sentido.

O Dependente também possui atributos relacionados. Percebemos que existe uma relação de dependência, um relacionamento de dependência entre a entidade Empregado e Dependente. Basicamente, ele visa representar o mesmo contexto, mas com outras informações. Esse conceito é puxado da ideia de conceito na orientação a objetos.

### Mapeamento do Modelo

Dado que falamos do início ao fim de um projeto, este é o projeto lógico, que utiliza o modelo relacional.

Temos um diagrama Entidade-Relacionamento (DER). Esse diagrama contém informações que subsidiarão o mapeamento para o diagrama relacional e, consequentemente, para o modelo relacional.

O relacionamento `works on` (esforço) é uma entidade de relacionamento.

> [!exemplo] Entidade de Relacionamento
> O relacionamento `works on` (esforço) é tratado como uma entidade porque ele possui atributos próprios. Isso faz sentido no mapeamento do Entidade-Relacionamento para o Relacional, onde ele se torna uma entidade.

As entidades que temos relacionadas são:

*   Empregado
*   Departamento
*   Dependente
*   Projeto

Quando passamos do projeto lógico para o projeto físico, criamos todos os comandos em SQL e começamos a persistir informações no banco de dados.

### Fluxo de Modelagem

O processo de modelagem segue uma progressão lógica:

| Etapa | Tipo de Diagrama/Modelo | Objetivo |
| :--- | :--- | :--- |
| **1. Modelagem Conceitual** | Diagrama Entidade-Relacionamento (DER) | Identificar entidades e os relacionamentos entre elas. |
| **2. Projeto Lógico** | Modelo Relacional | Definir as tabelas e os atributos de forma estruturada. |
| **3. Projeto Físico** | SQL / Banco de Dados | Criar os comandos e persistir as informações no banco de dados. |

Isso que apresentamos é apenas um pedacinho do que estávamos modelando até agora. Por exemplo, a entidade refletida em uma estrutura de tabela teria essa...

`⏱ 13:00`

a entidade refletida em uma estrutura de tabela ela teria essa

### Modelagem e Atributos das Entidades

Descrevendo as entidades, temos o nome do departamento, que pode ser o departamento de pesquisa, de administração, ou o *headquarters*. Também temos o número desse departamento, o número do gerente e a data em que o gerente começou.

Na entidade `EMPLOY` (empregado), temos o número do gerente.

Um exemplo prático: Se pegarmos o SSN 33, por exemplo, esse indivíduo, John, gerenciou o departamento de pesquisa a partir de uma determinada data.

A partir disso, conseguimos perceber que, independentemente da estrutura física, a álgebra relacional está funcionando.

### Conceito de Álgebra Relacional

Quando falamos de estrutura, estamos falando especificamente de atributos, do número de atributos e do tipo de cada atributo.

Para realizar um `SELECT`, é necessário encontrar um atributo comum entre as entidades. Esse processo é feito pela interseção.

> [!exemplo] Como funciona a Interseção
> A interseção permite encontrar, por exemplo, o indivíduo que gerenciou um departamento. Basta fazer uma consulta que encontre, em `EMPLOY`, o indivíduo que dá um *match* na combinação do número do SSN do empregado.

Ao fazer isso, a informação é retornada.

### Conclusão Teórica

Este processo é baseado na álgebra relacional e na ideia de teoria de conjuntos. É importante notar que o resultado não depende mais da estrutura daquela tabela ou daquela entidade.

Portanto, o exemplo foi dado apenas para conseguir exemplificar e mostrar como o conceito funcionaria na realidade.

## Relacionado

- [[sgbd-ganhos-e-otimizacao-operacional]]
- [[modelagem-de-dados-processo-e-fluxo-de-desenvolvimento]]
- [[modelagem-de-dados-desenvolvimento-implementacao-e-integracao]]
- [[modelagem-de-dados-projeto-logico-fisico-e-mapeamento-entidade-relacionamento]]
