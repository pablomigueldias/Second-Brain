---
titulo: "Álgebra Relacional, SGBD e Ciclo de Vida do Projeto de Banco de Dados"
tags: [sql, sgbd, banco-de-dados, modelagem-de-dados, fundamentos, otimizacao, conceitos]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 10
conceitos: [Álgebra Relacional, SGBD (Sistema de Gerenciamento de Banco de Dados), Independência da Aplicação em Dados, Teoria de Conjuntos, Dilema de Performance (em BD), Metodologia de Criação de Banco de Dados, Ciclo de Vida do Banco de Dados, Projeto Conceitual, Lógico e Físico]
---

# Álgebra Relacional, SGBD e Ciclo de Vida do Projeto de Banco de Dados

> [!resumo] Do que se trata
> A aula explora como a álgebra relacional permite a interação com SGBDs e garante a independência da aplicação em relação aos dados, utilizando a teoria de conjuntos. Ela discute o dilema de performance no projeto de banco de dados, destacando o impacto das transações na velocidade do sistema. Por fim, detalha a metodologia de criação e as fases do ciclo de vida de um banco de dados, desde o projeto conceitual até a manutenção.

## Para lembrar

- **A álgebra relacional permite criar ações e operações direcionadas ao SGBD, que as compila e retorna o resultado, como tabelas ou visões.**
- **A independência da aplicação em relação aos dados é proporcionada pela álgebra relacional, que manipula dados com base na teoria de conjuntos, não na estrutura de cada entidade.**
- **No projeto de banco de dados, há um trade-off de performance, pois a persistência de dados gera atraso ou sobreposição para cada transação, demandando tempo considerável do banco.**
- **A metodologia de criação de banco de dados segue as fases de Projeto Conceitual (requisitos), Projeto Lógico (modelagem) e Projeto Físico (escolha do modelo no SGBD).**

## O que esta nota responde

- Como a álgebra relacional interage com o SGBD para processar comandos?
- De que forma a álgebra relacional garante a independência da aplicação em relação aos dados?
- Quais são as fases da metodologia de criação e do ciclo de vida de um banco de dados?

## Conceitos

**Álgebra Relacional** · **SGBD (Sistema de Gerenciamento de Banco de Dados)** · **Independência da Aplicação em Dados** · **Teoria de Conjuntos** · **Dilema de Performance (em BD)** · **Metodologia de Criação de Banco de Dados** · **Ciclo de Vida do Banco de Dados** · **Projeto Conceitual, Lógico e Físico**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Álgebra relacional, SGBD e performance | ▪▪ |
| `04:20` | Ciclo de vida e metodologia BD | ▪▪ |
| `08:40` | Manutenção do banco de dados | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Independência da Aplicação em Dados** | A álgebra relacional retira a dependência da aplicação em relação aos dados porque, ao utilizar a teoria de conjuntos, não há uma estrutura que interfira na aplicação. |
| **Projeto Conceitual** | Projeto de alto nível, onde se definem os requisitos do sistema. |
| **Projeto Lógico** | Fase onde se modela e cria um diagrama para representar o contexto. |
| **Projeto Físico** | Fase onde se escolhe o tipo de modelo que será utilizado no SGBD. |
| **OLTP** | Usado para transações online. |
| **OLAP** | Usado para análises. |
| **Verificação de Expectativas** | O SGBD deve corresponder às expectativas, respondendo a todas as perguntas necessárias e se comportando da maneira esperada. |
| **Produção** | Momento de colocar o SGBD em produção, onde será utilizado pelas aplicações para consumo dos dados. |
| **Manutenção** | Fase onde eventuais problemas e ajustes no esquema podem ocorrer. |

## Teste-se

<details><summary>Qual o principal benefício da álgebra relacional em relação à aplicação e aos dados?</summary>

A álgebra relacional proporciona a independência da aplicação em relação aos dados. Ela retira essa dependência porque, ao utilizar a teoria de conjuntos, não há uma estrutura que interfira na aplicação.

</details>

<details><summary>Quais são as três fases da metodologia de criação de um banco de dados?</summary>

As três fases são: Projeto Conceitual, onde se definem os requisitos; Projeto Lógico, onde se modela e cria um diagrama; e Projeto Físico, onde se escolhe o tipo de modelo do SGBD.

</details>

<details><summary>O que é o dilema de performance no projeto de banco de dados?</summary>

É o trade-off entre a disponibilidade e o tempo de gravação, especialmente quando há modificações recorrentes nos dados. Inserções e persistências geram um atraso considerável, impactando a performance.

</details>

<details><summary>Qual a diferença entre OLTP e OLAP?</summary>

OLTP (Online Transaction Processing) é usado para transações online, enquanto OLAP (Online Analytical Processing) é utilizado para análises.

</details>

<details><summary>Quais são as fases do ciclo de vida do banco de dados após o Projeto Físico?</summary>

Após o Projeto Físico, as fases são Validação, Verificação de Expectativas, Produção e Manutenção.

</details>

<details><summary>O que é necessário para ajustar o esquema de um banco de dados em manutenção?</summary>

Para ajustar o esquema, é preciso parar o banco de dados, modificar o esquema, levantar os dados e, então, colocar o banco de dados para operar novamente.

</details>

## Conteúdo

`⏱ 00:00`

### Álgebra Relacional e SGBD

Quando utilizamos comandos e a **álgebra relacional**, criamos ações e operações que são direcionadas ao SGBD. O SGBD, por sua vez, compila e interpreta essas informações, retornando o resultado da ação. Ou seja, ele retorna a tabela ou a visão que estamos gerando a partir de uma determinada operação.

Aqui, podem ser um conjunto de instâncias de uma mesma tabela, ou podemos criar um `JOIN`, uma união entre entidades distintas, para representar algum tipo de visão mais complexa, criando um *matching* entre as chaves. (Este é um tema para mais adiante.)

### Independência da Aplicação em Dados

A álgebra relacional proporciona a independência da aplicação em relação aos dados. Ela retira essa dependência porque, ao utilizarmos a teoria de conjuntos, não há uma estrutura que interfira na aplicação.

> [!exemplo] Teoria de Conjuntos na Álgebra Relacional
> Imagine um conjunto A com determinada quantidade de dados (uma entidade A), e um conjunto B com outras informações (uma entidade B).
> Não interessa qual é o tipo de atributo, qual a quantidade ou quais os atributos relacionados à entidade B.
> Através de uma operação de teoria de conjuntos, como a união (representada por um riscado que abrange ambos os conjuntos) ou a interseção (que seria apenas a parte comum), é possível manipular os dados.
> Isso é feito com base nos conjuntos, e não na estrutura de cada entidade. Essa é a essência e a grande sacada do modelo relacional.
> Conseguimos representar consultas bem mais complexas de uma maneira facilitada, utilizando a álgebra relacional.

### O Dilema de Performance no Projeto de Banco de Dados

Existe um *trade-off*, que é, na verdade, um dilema. Precisamos pensar e balancear o que é necessário.

> [!atenção] Impacto da Persistência na Performance
> Ao projetar o banco de dados, você deve ter em mente que, sempre que algo é inserido ou persistido no banco de dados, há um atraso (`delay`) ou sobreposição (`overlap`) para gerar uma transação.
> Essa transação modifica o banco e persiste, levando-o de um estado a outro.
> Esse tipo de ação demanda um tempo considerável do banco.
> Pense numa quantidade de modificações constantes: um banco que precisa de maior performance seria prejudicado se houvessem muitas modificações na base.

Este *trade-off* é um adendo e uma curiosidade. Quando vocês forem projetar um banco de dados, muitas vezes farão simplesmente a manutenção de um banco de dados já criado na empresa.

Mas, se vocês forem participar de algum projeto de *design*, e o *designer* do banco de dados está dentro da equipe do DBA (que é o administrador do banco de dados), vocês precisarão definir o seguinte: "Este meu banco precisa de performance." Esse tipo de informação é definida no projeto físico. Então, se eu tenho um banco que precisa de maior performance, eu tenho que pensar...

`⏱ 04:20`

se eu tenho um banco que precisa de maior performance eu tenho que pensar em como lidar com essa questão de modificações recorrentes do banco de dados que geram um *delay*.

Nesse cenário, ao pensar no *clock* do sistema, no tempo que o sistema leva para responder a uma inserção, o tempo de gravação pode ser maior do que a disponibilidade que você precisa gerar. Ele vai demorar bastante tempo para poder responder uma eventual consulta durante esse período.

Você precisa pensar no equilíbrio entre:
- Disponibilidade e tempo de gravação;
- Modificações relativamente recorrentes no grupo de dados e a disponibilidade de acesso a esses dados.

### Metodologia de Criação de Banco de Dados

Para conseguir utilizar um SGBD e criar um banco de dados efetivamente, seja mais simples como `PostgreSQL`, seja `Oracle`, seja qual for o que estiver na sua empresa, você precisa de uma metodologia, uma estrutura que defina como criar o banco do início ao fim.

Embora em alguns casos você possa ficar apenas na manutenção do banco de dados, se for necessário participar de todas as etapas, o processo segue uma sequência estruturada:

1. **Projeto Conceitual:** É um projeto de alto nível, onde você define os requisitos do sistema.
2. **Projeto Lógico:** Você modela e cria um diagrama para representar o seu contexto.
3. **Projeto Físico:** Você escolhe o tipo de modelo que estará utilizando no SGBD.

> [!exemplo] Modelagem e Estrutura
> Ao definir o modelo, você deve determinar se será um modelo relacional, se será um `NoSQL`, ou se será um tipo específico de sistema:
> - **OLTP** (Online Transaction Processing): Usado para transações online.
> - **OLAP** (Online Analytical Processing): Usado para análises.
>
> É durante essa fase de projeto de banco de dados que você deve definir qual a estrutura que melhor atende o seu contexto e o seu problema modelado.

### Fases do Ciclo de Vida do Banco de Dados

O processo não se encerra após o Projeto Físico. Ele passa por várias etapas cruciais:

- **Validação:** Após concluir o projeto conceitual, lógico e físico, e já ter inserido no SGBD e criado o esquema, você precisa definir requisitos como disponibilidade, segurança e índices. A partir do projeto físico do SGBD, isso passa para a validação.
- **Verificação de Expectativas:** O SGBD deve corresponder às expectativas, respondendo a todas as perguntas necessárias e se comportando da maneira esperada. Isso inclui não apenas responder às perguntas que você quer, mas também ter a performance desejada e o acesso aos dados de maneira otimizada. Por exemplo, verificar se os índices foram definidos da melhor maneira possível. Isso é verificado durante a fase de validação.
- **Produção:** Quando está tudo certo, você passa para a parte de produção. É o momento de colocar o SGBD em produção, onde ele será utilizado pelas aplicações para consumo desses dados. Ele estará online e sendo consumido pelas APIs.
- **Manutenção:** O ciclo não termina aqui. Há sempre a parte de manutenção, onde eventuais problemas e ajustes no esquema podem ocorrer.

`⏱ 08:40`

Ainda tem parte de manutenção, que eventuais problemas ocorrem, eventuais ajustes no esquema podem ocorrer.

### Manutenção do Banco de Dados

É mais raro acontecer um ajuste no esquema, até porque isso gera um trabalho considerável.

> [!exemplo] Ajuste de Esquema
> Para ajustar o esquema, você precisa:
> - Parar o banco de dados.
> - Modificar o esquema.
> - Levantar os dados.
> - Colocar o banco de dados para operar novamente.

Mas, isso pode acontecer.

Além disso, você precisa estar checando os índices. É importante verificar se essas informações ainda são válidas e se esses índices ainda são interessantes. Toda a estrutura que você montou é aprimorada com o tempo. Isso fica a cargo da parte de **manutenção do banco de dados**.

## Relacionado

- [[modelagem-de-dados-etapas-caracteristicas-do-sgbd-e-conceito-de-mundo-fechado]]
- [[algebra-relacional-e-logica-de-predicados-para-sql]]
- [[sql-database-specialist-comandos-essenciais-para-gerenciamento-de-bancos-de-dado]]
- [[modelo-relacional-usuarios-e-integracao-de-sgbds]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `postgre → PostgreSQL`
