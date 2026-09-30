---
titulo: "SGBD: Vantagens, Otimização e Integridade dos Dados"
tags: [sgbd, banco-de-dados, dados, sistema, otimizacao, modelagem-de-dados, conceitos]
data: 2026-09-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 26
conceitos: [SGBD (Sistema Gerenciador de Banco de Dados), Controle de redundância, Desnormalização, Restrição de acesso, Persistência de dados, Backup recovery, SGBD NoSQL, Otimização de desempenho (SGBD)]
---

# SGBD: Vantagens, Otimização e Integridade dos Dados

> [!resumo] Do que se trata
> Esta aula detalha as vantagens de um SGBD, como controle de redundância, restrição de acesso e persistência de dados, contrastando com abordagens tradicionais. Ela aborda problemas de *mismatch* entre linguagens de programação e SGBDs, introduzindo os SGBDs NoSQL como solução. A aula também explora técnicas de otimização de desempenho, como *caching* e indexação, e enfatiza a importância da integridade dos dados e das *constraints* para manter o estado válido do sistema.

## Para lembrar

- **As vantagens de um SGBD incluem controle de redundância, restrição de acesso, persistência de dados transparente ao usuário e backup recovery.**
- **A desnormalização é uma técnica que, em cenários específicos, insere redundância para otimizar o desempenho de leitura, encobrindo ineficiências inerentes ao banco de dados relacional.**
- **SGBDs NoSQL surgiram para solucionar problemas de *mismatch* entre paradigmas de orientação a objeto e modelos relacionais, especialmente em relação a tipos de dados.**
- **Técnicas como *caching*, *buffering* e indexação são utilizadas para otimizar o desempenho de um SGBD, tornando consultas mais rápidas para dados de alta demanda.**
- **Um SGBD deve manter o estado válido do sistema, impedindo que o banco de dados seja migrado para um estado inválido, utilizando *log* para recuperar o estado anterior em caso de falha.**

## O que esta nota responde

- Quais são as principais vantagens de utilizar um SGBD?
- Como o SGBD lida com a redundância de dados e o que é desnormalização?
- Que técnicas são empregadas para otimizar o desempenho de um SGBD e garantir a integridade dos dados?

## Conceitos

**SGBD (Sistema Gerenciador de Banco de Dados)** · **Controle de redundância** · **Desnormalização** · **Restrição de acesso** · **Persistência de dados** · **Backup recovery** · **SGBD NoSQL** · **Otimização de desempenho (SGBD)**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Vantagens SGBD e Controle Redundância | ▪▪ |
| `04:20` | Acesso, Persistência, Mismatch e SQL | ▪▪ |
| `12:00` | SQL: Execução, Lógica e Otimização | ▪▪ |
| `16:00` | Otimização, Integridade e Interfaces | ▪▪▪ |
| `24:20` | Regras, Triggers e Vantagens | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **API (Application Programming Interface)** | Interface que faz a conexão e a consulta aos dados de um STBD. Pode ser criada em linguagens como Python e Java, com uma estrutura voltada para armazenar as informações persistidas no banco de dados e depois passá-las para outra ponta. |
| **SQL (Structured Query Language)** | Linguagem de programação projetada para facilitar o entendimento do desenvolvedor, sendo intuitiva. Não possui soluções de lógica ou definição de negócios como uma linguagem de programação tradicional, focando na recuperação de dados. Utiliza a teoria de conjuntos para ser versátil e simples, mesmo em queries complexas utilizando subqueries e joins dentro de cada subquery. |
| **DBA (Database Administrator)** | Profissional responsável por técnicas relacionadas a caching, buffering e indexação, entre outras, para gerenciar bancos de dados. |
| **Manutenção da Integridade pelo SGBD** | Um SGBD tem que manter o estado válido do sistema. O banco de dados não pode ser migrado para um estado inválido, seja por Query SQL, por uma falha do sistema, ou pelo que for. |
| **Trigger (Gatilho)** | É um mecanismo acionado no momento em que uma modificação é realizada, acarretando em uma outra ação posterior à ação tomada. |

## Pegadinhas

- Embora o SGBD controle a redundância, em cenários específicos como a desnormalização, a redundância pode ser intencionalmente introduzida para otimização de desempenho de leitura.
- A estrutura de dados na programação (paradigma de orientação a objeto) difere da estrutura de persistência de dados em SGBDs (modelo relacional), gerando o Impendency Mismatch Problem.
- A verificação de estado pode ser feita por inferência (a partir dos dados e informações do usuário) ou por regras declarativas (programação procedural); regras declarativas exigem modificação manual se as regras de negócio mudarem, enquanto a inferência se adapta.

## Teste-se

<details><summary>Quais são as quatro vantagens adicionais do SGBD mencionadas na aula, além das características já comentadas?</summary>

As vantagens adicionais são: Controle de redundância, Restrição de acesso, Persistência de dados (transparente ao usuário) e Backup recovery.

</details>

<details><summary>O que é o Impendency Mismatch Problem e qual sua causa principal?</summary>

É a falta de combinação entre a estrutura de dados usada no desenvolvimento de software (orientação a objeto) e a estrutura usada para persistir dados em SGBDs (modelo relacional).

</details>

<details><summary>Quais são as três técnicas de otimização de desempenho do SGBD mencionadas na aula?</summary>

As técnicas de otimização são caching, buffering e indexação. Elas são usadas para dados de alta demanda e para tornar consultas mais rápidas.

</details>

<details><summary>Qual o papel do SGBD na manutenção da integridade dos dados?</summary>

O SGBD deve manter o estado válido do sistema, impedindo que o banco de dados migre para um estado inválido. Em caso de falha, ele pode usar o log para recuperar um estado anterior.

</details>

<details><summary>O que é um Trigger (Gatilho) em um SGBD?</summary>

Um Trigger é um mecanismo acionado no momento em que uma modificação é realizada, acarretando em uma outra ação posterior à ação tomada.

</details>

<details><summary>Quais são os seis passos do fluxo de execução de uma consulta SQL?</summary>

Os passos são: criação da query, submissão ao SGBD, busca no disco, carregamento para memória, envio e processamento, e retorno do resultado.

</details>

## Conteúdo

`⏱ 00:00`

Falamos bastante sobre diversas características de um SGBD e dos atores que estão direta e indiretamente ligados a ele. O SGBD provê toda uma infraestrutura para que possamos utilizar esse sistema que nos facilita tanto a vida.

### Vantagens do SGBD

Já mencionei diversas vantagens atreladas ao SGBD, mas quero pontuar cada uma delas.

Além das quatro características que já comentamos — abstração (associada a isolamento), múltiplas visões, autodescrição e compartilhamento (atrelado à transação multiusuário) — temos outras vantagens associadas.

As vantagens são:
- **Controle de redundância**
- **Restrição de acesso**
- **Persistência de dados**, que ocorre de maneira transparente ao usuário (seja ele sofisticado ou *naive*)
- **Backup recovery**

O SGBD provê e fornece a estrutura relacionada a como os dados devem ser persistidos.

### Controle de Redundância

Para exemplificar o **controle de redundância**, pense na abordagem tradicional. Nela, teríamos dois arquivos distintos, muitas vezes trabalhando no mesmo contexto. Cada um trabalhando na sua ferramenta, na sua IDE, utilizando a aplicação e modelando o mesmo cenário. Isso gera redundância.

> [!exemplo] Redundância na Abordagem Tradicional
> No `Storage C`, temos uma relação associada com o desenvolvedor A.
> No `Storage D`, temos praticamente o mesmo arquivo, os mesmos dados, refletidos pelo usuário B.
> >
> Isso leva a:
> - Desperdício de recursos (poder computacional, tempo, dinheiro).
> - Redundância de informações.
> - Inconsistência das informações, já que não estão em um único local e são gerenciadas por diferentes pessoas e arquivos. Isso aumenta a probabilidade de inconsistência.
> - Updates desnecessários: Seria preciso fazer o dobro de updates, pois ambos os arquivos precisariam ser atualizados.

O SGBD oferece a super vantagem do controle de redundância. Ao invés de cada um acessar seus arquivos individualmente, cada um consulta o SGBD. Assim, garantimos o controle da redundância e o acesso concorrente às informações.

Cada um consegue acessar esses dados, e eles são refletidos para os usuários.

Mas, haverá redundância dentro de um SGBD? Não se pode dizer que nunca. Há cenários em que é interessante inserir algum nível de redundância para otimizar o desempenho de leitura. Em alguns casos, isso é chamado de **desnormalização** e ajuda a encobrir algumas ineficiências inerentes ao banco de dados relacional.

> [!atenção] Desnormalização
> Em alguns cenários bem específicos, é interessante criar redundância através da desnormalização. Isso será tratado mais adiante e não é uma preocupação para agora.

`⏱ 04:20`

desnormalização então continuando outro fator é a restrição de acesso que a gente até já comentou também nós temos diversas pessoas interessadas em acessar esses dados e alguns cenários com relação à restrição de acesso um deles é essa pessoa não você não tem permissão de acessar as informações e aí isso vai ser tratado via a algum gerencia algum sistema de gerenciamento se eu vou acessar o sgbd eu preciso ter um login e senha eu preciso ter um usuário cadastrado Ok se você sabe uma API eu preciso saber se aquela PM ao que aquela MP API vai dar acesso, ? Às vezes é um acesso limitado, somente de leitura. Se eu for persistir informação no banco de dados, por exemplo, via o método post, através de requisição HTTP, eu vou preencher o formulário, e só por ali ele vai ser enviado para o servidor, e o servidor vai processar aquela informação, enviando... informações ali pelo meu back para o meu sistema de banco de dados, ok? Então, nós temos essa parte mais segura com relação ao acesso dos dados, ? Então, muitas vezes eu preciso apenas, essa mulher, ela vai ter um acesso de update. Então, essa pessoa específica, ela pode ter um acesso, uma autorização para a atualização. Esse daqui é um read only, então ele só tem acesso aos dados, todos os dados, de maneira restrita e não para edição. Enquanto o lado de cá tem o restricted view, ou seja... Eu só tenho uma view. Quando eu acesso o banco de dados, eu não tenho noção geral daqueles dados, e sim uma view que me fornece o sistema baseado no grupo que eu estou identificado. E quem que faz essa restrição de acesso? É justamente o DBA, que é o administrador do banco de dados. E acaba... acontecendo que esse, o SGBD, ele trata através de um subsistema secundário toda essa questão de restrição de acesso, de autorização de acesso, ? Via aí assinatura digital e certificação, ? Então, existe sim esse nível de segurança dentro do SGBD que a gente pode estar configurando e, na verdade, é o papel do DBA que faz essa configuração, e a gente pode estar explorando isso lá na frente. Prover persistência. Quando a gente pensa no termo de persistir um dado, a gente tem um programa-fonte, o que acontece? Esse programa-fonte vai ser executado por um copilador. Esse compilador, por sua vez, vai transformar esse programa-fonte em um programa-objeto, em um programa de linguagem de máquina, onde geralmente está associado à linguagem assembly. Mas o que acontece com os dados de um programa-objeto? Aí é que vem uma questão. Esses dados acabam sofrendo uma convers... Eles são salvos em arquivo, ok? Em contrapartida, quando o meu programa se torna um programa objeto, ele simplesmente continua consultando o banco de dados. Ele não tem que lidar com a estrutura e com os dados que eu estou ali manipulando dentro do meu programa objeto, ? Então, nós temos essa outra vantagem com relação à persistência da... informações. Então, nós temos que sair de novo aquela questão do isolamento programa e dados. Então, seguindo nessa linha, vamos entender o que significa, dentro desse sentido de persistência de dados, estruturas utilizadas para estar armazenando os dados, o que seria um problema denominado Impendency Mismatch Problem. Esse tipo de problema está relacionado justamente ao nome que ele está associado, mismatch. Ou seja, a falta de um match, a falta de uma combinação entre a estrutura utilizada dentro de desenvolvimento de software e desenvolvimento de STBDs. A gente vai ver mais para frente uma outra etapa, um outro módulo.

`⏱ 08:20`

desenvolvimento de STBDs. A gente vai ver mais para frente uma outra etapa, um outro módulo: como é feita a **modelagem de dados** para que a gente consiga persistir as informações dentro de um STBD.

E só para adiantar um pedacinho para que vocês possam entender o porquê que esse tipo de problema existe, dentro da **modelagem conceitual** e da **modelagem de dados** para banco de dados, nós temos três atributos mínimos:
- **atributos** e seus **tipos de dados**
- **tabelas**
- **tuplas**

A gente vai entender lá na frente o que significa cada uma dessas coisas, mas importa dizer que a estrutura que utilizamos para persistir os dados dentro de **STBDs** é diferente da utilizada na programação, na codificação de aplicação.

Quando você está codificando, geralmente está utilizando um **paradigma de orientação a objeto**. Não que seja uma regra, mas geralmente é isso que acontece. E quando você está persistindo os dados? Você está utilizando o **modelo relacional**. A estrutura não é a mesma, a estrutura difere. E entramos nessa questão de impedância, um problema de combinação, de impedância entre sistemas.

| Programação (Orientação a Objeto) | Persistência de Dados (Modelo Relacional) |
| :-------------------------------- | :--------------------------------------- |
| Utiliza paradigma de orientação a objeto | Utiliza modelo relacional                |
| Estrutura de dados diferente      | Estrutura de dados diferente             |

Para tentar solucionar essa questão, surgiram os **SGBDs NoSQL**. Na verdade, SGBDs com um outro escopo, com outro viés de orientação a objetos. Existem SGBDs relacionais com essa possibilidade de orientação a objeto, mas o `DB for object` e o `ZOOP` são SGBDs voltados para essa questão de orientação a objeto. Portanto, são bancos NoSQL.

### Problemas no Cenário de Mismatch

Quais os problemas que podemos ter dentro desse cenário?
- Questões de definição de dados e **tipos de dados**.
- Podemos ter **tipos de dados** presentes em linguagens como `Java` ou `C` que não existem no mundo de **STBDs**, por exemplo, dentro do `MySQL` ou do `Postgres`.
- Recuperação de informações:
  - Geralmente, quando recuperamos informações de um **STBD**, os dados vêm estruturados em forma de conjunto ou de multiconjuntos, e no mínimo uma **tupla**, ou seja, uma linha de uma tabela.
  - Em orientação a objeto, para buscar isso, precisamos varrer. Precisamos utilizar técnicas relacionadas à estrutura de dados de conjuntos para puxar as informações uma a uma, printando ou processando-as. Isso gera um gargalo.

Para isso, existem **APIs** que farão a conexão e a consulta aos dados do **STBD**.

> [!definicao] API (Application Programming Interface)
> Interface que faz a conexão e a consulta aos dados de um STBD. Pode ser criada em linguagens como `Python` e `Java`, com uma estrutura voltada para armazenar as informações persistidas no banco de dados e depois passá-las para outra ponta.

### Estrutura de Armazenamento e SQL

Seguindo nessa linha, podemos falar então de **estrutura de armazenamento**. A **estrutura de armazenamento** utilizada pelos **STBDs** geralmente é em árvores, estruturada de maneira que há uma conexão entre elas. Isso torna a busca mais eficiente.

As *queries* são a linguagem de programação. A `SQL` foi projetada de maneira a facilitar o entendimento do desenvolvedor. De qual forma? Ela seria intuitiva. Não temos soluções de lógica ou definição de negócios como uma linguagem de programação tradicional. Queremos recuperar dados.

> [!definicao] SQL (Structured Query Language)
> Linguagem de programação projetada para facilitar o entendimento do desenvolvedor, sendo intuitiva. Não possui soluções de lógica ou definição de negócios como uma linguagem de programação tradicional, focando na recuperação de dados. Utiliza a **teoria de conjuntos** para ser versátil e simples, mesmo em *queries* complexas utilizando `subqueries` e `joins` dentro de cada `subquery`.

`⏱ 12:00`

Mesmo que a gente tenha uma query complexa utilizando subqueries e joins dentro de cada subquery, coordenação, ação e agrupamento, você, conhecendo previamente as estruturas, cláusulas e a ordem de execução de cada cláusula em uma consulta **SQL**, consegue entender, mesmo que a consulta pareça muito complexa, como o **SGBD** vai interpretá-la e o que ele fará, na verdade, quando uma consulta é realizada a ele.

### Fluxo de Execução de uma Consulta SQL

> [!exemplo] Processamento de uma Consulta
> 1. Criação da `query`: Contém os statements e o que se deseja recuperar do banco de dados.
> 2. Submissão ao SGBD: A `query` é enviada ao Sistema Gerenciador de Banco de Dados.
> 3. Busca no disco: O SGBD procura a informação na sua base, ou seja, nos dados armazenados em disco.
> 4. Carregamento para memória: Uma vez encontrados, os dados são carregados para a memória.
> 5. Envio e processamento: O SGBD envia os dados, que podem então ser processados.
> 6. Retorno do resultado: O resultado é retornado e pode ser salvo em arquivo, usado para alimentar um dashboard (como com Power BI) ou para outras ações.

### A Lógica do SQL

Com relação à técnica de busca e às queries mais facilitadas e de fácil entendimento, mesmo que você não tenha tido contato nenhum com o SQL, você vai conseguir entender o que está aqui, porque é lógica. E é aplicada à teoria de conjuntos, que é uma lógica bem tranquila de se entender.

### Exemplo de Consulta SQL

> [!exemplo] Consulta de Nome de Curso
> Vamos pensar na seguinte consulta:
> `SELECT curse name FROM curses WHERE credit hours = max credit hours`
> >
> Isso significa que estamos selecionando o nome do curso, da tabela `curses`, onde as horas em crédito são iguais ao máximo de horas que conseguimos encontrar dentro da tabela. Percebe como isso é legível e inteligível? Você consegue entender facilmente o que está retornando.
> >
> É isso que temos com SQL: essa facilidade de utilização e do gerenciamento das informações dentro de um SGBD.

O SGBD retorna para a gente em forma de tabela, essa estruturazinha bonitinha que eu solicitei. No caso, na verdade, não era só o `curse name`. Aqui, na verdade, tem que ser um asterisco (`*`), não somente `curse name`. Ou então, `curse name`, `curse number`, `credit hours`, `department`. Eu teria que estar com esses quatro atributos definidos aqui, ou se existem somente eles dentro da minha tabela, eu mantenho com um asterisco. Mas isso a gente vai abordar quando estiver falando de SQL.

### Técnicas de Otimização de Desempenho do SGBD

Há outras técnicas para que a gente possa performar e deixar o nosso SGBD com mais desempenho. Entre elas, nós temos:
- `caching`
- `buffering`
- `indexação` (ou `indexes`, `index`)

Nesse sentido, a gente pode utilizar essas técnicas para dados que estão sendo recuperados com maior recorrência. Então, a gente tem alta demanda. Eu tenho ali o que ele está em cache, e eu torno minha consulta mais rápida. Consequentemente, eu libero o SGBD mais rapidamente. A gente vai ver em [inaudível] quando tiver tipo de situação sobre transações, locking de tabelas. Essa questão de você liberar a tabela rapidamente pode ser uma palavra-chave para você, e você pode estar utilizando de `caching`, por exemplo.

Com `buffering`, a gente pode utilizar um buffer para estar inserindo informações ali dentro.

`⏱ 16:00`

inserindo informações ali dentro e recuperando conforme demanda. Outra técnica é a **indexação**, que torna o acesso mais rápido através de algumas estruturas, como árvores. Por exemplo, a árvore hash, uma variação dessa estrutura, é utilizada na blockchain para estruturar as transações dentro da plataforma.

Essas técnicas estão geralmente relacionadas ao **DBA**, ou Database Administrator (administrador de banco de dados).

> [!definicao] DBA (Database Administrator)
> Profissional responsável por técnicas relacionadas a caching, buffering e indexação, entre outras, para gerenciar bancos de dados.

Outras técnicas interessantes que existem dentro de um sistema de gerenciamento de bancos de dados são **backup** e **recovery**. Elas são muito interessantes quando se trata de recuperar recursos que foram perdidos por algum motivo.

Com um backup, tenho uma réplica da minha base de dados, do meu SGBD, em um local diferente. Isso me possibilita ter maior disponibilidade do meu sistema. No sentido de que, se eu perder o meu SGBD principal, posso direcionar todo o tráfego de dados para a minha réplica. Dessa forma, não perco as informações que armazenei. Erros, falhas em hardware e até em softwares podem acontecer.

Assim como a tela azul que aconteceu no meu computador por causa de uma atualização do Windows, falhas podem ocorrer. O **recovery** é interessante quando temos, por exemplo, falhas por desastres. Há um processo de recovery associado a um DBA, que pode ser realizado para recuperar informações perdidas por algum estado inválido que tenha acontecido no SGBD, ou melhor, no banco de dados. Um SGBD pode ter diversos bancos de dados armazenados.

### Interface Multi-usuário

Temos também a questão de prover uma interface multi-usuário. O SGBD é multi-usuário, dado que ele permite acesso concorrente de informações, estabelecendo seus limites.

Dentro desse assunto, um usuário pode ter habilidades, contextos e interesses diferentes, e as interfaces variam. Podemos denominar algumas interfaces como:
- `bobo apps`
- Interfaces naturais, como Alexa (quando você pede para tocar uma música no Spotify)
- `Query Language` (para profissionais de banco de dados que recuperam informações por `Queries`, `Forms` e `Command Codes`)
- `Forms` (via uma API Web)
- `Menu Driven` (para aqueles usuários mais "naíveis", onde se navega por submenus, buscando o que se precisa).

Isso se aplica a qualquer tipo de site hoje que puxa informações do banco de dados para te informar (a não ser aquelas que são estáticas e explícitas do site). Informações de negócios, produtos, estoque, por exemplo, envolvem um acesso de leitura ao SGBD. Assim, conseguimos navegar via menu através desse tipo de interface.

### Programação e APIs

Além disso, temos a programação, com `Libs` e `APIs` para criar a conexão entre o banco de dados e a aplicação. Com elas, pegamos representações complexas que poderiam ser tratadas de maneira mais difícil e as retratamos de forma fluida. Conseguimos criar relacionamentos entre duas entidades do mundo real de maneira tranquila e definir o tipo de relacionamento e a ordem em que ele acontece. Podemos ver aqui, grades...

`⏱ 20:20`

grades, e como um `report` e um `estudante` se relacionam: um `estudante` está relacionado a um `report` de uma `grade`. Através da modelagem conceitual, e criando toda essa estrutura definida, definimos todo relacionamento. A partir do tipo de relacionamento que você cria, você vai estar respondendo uma pergunta diferente.

### Integridade dos Dados

A **integridade dos dados** é uma coisa muito importante. Não adianta nada ter um sistema que gerencia seus dados se você não tem corretude dos mesmos.

> [!definicao] Manutenção da Integridade pelo SGBD
> Um SGBD tem que manter o estado válido do sistema. O banco de dados não pode ser migrado para um estado inválido, seja por `Query SQL`, por uma falha do sistema, ou pelo que for.

Se porventura isso acontecer, nós temos métodos utilizando o `log` para recuperar o estado anterior do banco de dados. Informações irão se perder, mas é melhor do que ter um estado inválido de um SGBD, ou de um banco de dados.

### Tipos de Integridade e Restrições

Nós temos algumas integridades. Essa daqui é uma **integridade de referência**. Essas são **constraints**, são regras que a gente pode estar definindo dentro do nosso esquema de banco de dados.

Vocês vão entender onde cada palavra dessas se encaixa, pois conforme a gente for avançando em temas como modelagem conceitual e mapeamento do esquema conceitual para o relacional, utilizando o `SQE` (ou a gente vai utilizar o `SQE` também lá para frente, enfim), vocês vão entender onde cada coisa se encaixa.

> [!exemplo] Integridade de Referência
> Essa restrição diz que `curso` está associado à `sessão`. Se `sessão` está referenciando `curso`, há a obrigatoriedade de que, ao inserir alguma informação dentro de `sessão`, ela tem que existir obrigatoriamente em `curso`. Esse tipo de restrição é de integridade, e mantém a coerência dos dados.

Existem alguns tipos de restrições:
- regra de domínio;
- integridade referencial;
- dependências funcionais.

E a gente pode estar atribuindo essas restrições tanto por gatilhos, assertões e `constraints`.

### Regras de Negócio e Representação no Banco de Dados

A gente pensa ainda com relação à integridade de dados. Procuramos sempre estar representando as **regras de negócio**. Nosso banco de dados tem que fazer um paralelo com o mundo real de forma que eu consiga representá-lo aqui dentro.

Eu tenho uma aplicação que possui as regras de negócio associadas a ela, e ela faz o intermédio entre o meu mundo real e o meu SGBD. Então, é uma questão semântica, de sentido da coisa, do que a gente está fazendo e qual a proposta que a gente está procurando resolver.

### Verificação de Estado: Inferência vs. Regras Declarativas

A partir daí, como a gente consegue, por exemplo, verificar o estado de aprovação de um estudante? A gente pode estar criando uma **inferência**. Inferimos a partir dos dados que algo aconteceu, e os usuários me passam aquela informação, ao invés de eu criar uma regra declarativa sobre o assunto.

A outra maneira é criar uma **regra declarativa**, ou seja, eu especifico dentro de uma programação procedural que um aluno será reprovado ou não, se a nota dele for tanta.

| Inferência                                                              | Regra Declarativa                                                                                             |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| Criada a partir dos dados.                                              | Especificada em programação procedural.                                                                       |
| Usuários passam a informação.                                           | Exemplo: aluno reprovado se a nota for X.                                                                     |
|                                                                         | Problema: se a regra de negócio mudar (ex: média de 5 para 7), exige alteração manual no esquema de dados/código. |

E se o meu mundo mudar? E se, em vez da média ser 5, ela passar a ser 7? Se eu defini isso no esquema de dados, vou ter que ir lá mexer, vou ter que alterar. Isso me dá o maior trabalho. Aquele programa procedural vai ter que ser muito...

`⏱ 24:20`

Aquele programa de procedurar vai ter que ser muito modificado para poder ser reexecutado. Para evitar isso, podemos utilizar as regras de dedução e, por exemplo, atribuir esse tipo de `constrain` à aplicação.

### Vantagens do SGBD

Temos as **triggers**, ou gatilhos. O interessante é que podemos iniciá-los a partir de uma ação anterior.

> [!definicao] Trigger (Gatilho)
> É um mecanismo acionado no momento em que uma modificação é realizada, acarretando em uma outra ação posterior à ação tomada.

> [!exemplo] Funcionamento de um Trigger
> Se você realiza um `update` (uma modificação), o trigger é acionado no momento dessa modificação. Ele, então, acarreta em uma outra ação posterior.
> >
> Por exemplo: dada uma tabela, ao realizar uma ação, o trigger é acionado, envia a informação e modifica uma segunda tabela.

Essa é a ideia. Com isso, encerramos as vantagens e o assunto sobre as vantagens do SGBD.

## Relacionado

- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[../Introdução a Banco de Dados/sgbds-os-mais-utilizados-no-mercado]]
- [[../Introdução a Banco de Dados/bancos-de-dados-da-evolucao-ao-big-data]]
- [[sgbd-atores-tipos-de-usuarios-e-finalidade]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `esquema do banco → schema`
