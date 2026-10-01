---
titulo: "SGBD: Mundo Fechado, Mini Mundo e CWA"
tags: [sgbd, banco-de-dados, fundamentos, conceitos, modelagem-de-dados, sql, sistema]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 5
conceitos: [Mundo Fechado, Mini Mundo, Universo de Discurso, Close World Assumption (CWA), Modelo de Dados, Álgebra Relacional, Queries, Sistemas Gerenciadores de Banco de Dados (SGPD)]
---

# SGBD: Mundo Fechado, Mini Mundo e CWA

> [!resumo] Do que se trata
> A aula explora os conceitos de Mundo Fechado e Mini Mundo no contexto de bancos de dados, definindo o primeiro como a premissa de que informações não presentes no modelo são consideradas falsas. Ela explica que o Mini Mundo é a porção do mundo real a ser modelada, e o banco de dados representa e armazena seus dados. Por fim, introduz a Close World Assumption (CWA) como o princípio lógico que governa as operações de consulta em Sistemas Gerenciadores de Banco de Dados (SGBDs).

## Para lembrar

- **Mundo Fechado é a ideia de que, se algo não está contemplado no modelo de dados, a resposta para uma consulta sobre essa informação será falso.**
- **Um mini mundo (ou universo de discurso) é um pedaço do mundo real que se deseja modelar, e o banco de dados representa e armazena os dados relacionados a ele.**
- **O conceito de mundo fechado está diretamente atrelado ao mini mundo, pois delimita um espaço do contexto real, respondendo 'falso' para o que está fora dessa delimitação.**
- **A Close World Assumption (CWA) é uma proposição ligada à lógica de predicados e à álgebra relacional, que rege as diretrizes das queries e operações em um SGPD.**
- **Em bancos de dados probabilísticos, o comportamento seria diferente da CWA, fornecendo uma probabilidade de que algo fosse verdadeiro ou falso, em vez de simplesmente assumir falso.**

## O que esta nota responde

- O que significa o conceito de Mundo Fechado em bancos de dados?
- Qual a definição de Mini Mundo e como ele se relaciona com a modelagem de dados?
- Como a Close World Assumption (CWA) influencia as consultas e operações em um SGPD?

## Conceitos

**Mundo Fechado** · **Mini Mundo** · **Universo de Discurso** · **Close World Assumption (CWA)** · **Modelo de Dados** · **Álgebra Relacional** · **Queries** · **Sistemas Gerenciadores de Banco de Dados (SGPD)**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Mundo Fechado e Mini Mundo: Conceitos | ▪▪ |
| `04:20` | Close World Assumption (CWA) | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Mundo Fechado** | A ideia de que, se algo não está contemplado no modelo de dados, a resposta para uma consulta sobre essa informação será `falso`. |
| **Mini Mundo (ou Universo de Discurso)** | Um **mini mundo** (ou **universo de discurso**) é um pedaço do mundo real que se deseja modelar. O que se consegue representar no banco de dados é esse pedaço. O modelo lógico do banco de dados representa e armazena os dados relacionados a esse mini mundo. O termo 'universo de discurso' é muito utilizado em Inteligência Artificial (IA). |
| **Close World Assumption (CWA)** | Uma proposição ou afirmação relacionada à lógica de predicados. Ela está ligada a todo o funcionamento da álgebra relacional que rege as diretrizes das *queries*, das consultas e das operações que realizamos em cima do `SGPD`. |

## Pegadinhas

- A CWA assume que algo é falso se não está no modelo, enquanto bancos de dados probabilísticos fornecem uma probabilidade de que algo seja verdadeiro ou falso.

## Teste-se

<details><summary>Qual a conclusão sobre a resposta de uma consulta no Mundo Fechado se a informação não está contemplada no modelo?</summary>

Se você procura algo que não está contemplado no seu modelo, a resposta será `falso`. Essa é a ideia de Mundo Fechado.

</details>

<details><summary>O que é um Mini Mundo?</summary>

Um mini mundo (ou universo de discurso) é um pedaço do mundo real que se deseja modelar. O modelo lógico do banco de dados representa e armazena os dados relacionados a esse mini mundo.

</details>

<details><summary>Como o conceito de Mundo Fechado se atrela ao Mini Mundo?</summary>

O conceito de mundo fechado está diretamente atrelado ao mini mundo porque se está delimitando um espaço dentro do contexto, e a partir dessa delimitação, responde-se 'não' (falso) para o que está fora dela.

</details>

<details><summary>Qual a principal característica da Close World Assumption (CWA) em relação a uma verificação?</summary>

A CWA faz com que, a partir de uma determinada linha, não se responda a uma verificação. Em vez disso, simplesmente se assume que é falso.

</details>

<details><summary>A que a Close World Assumption (CWA) está ligada em termos de lógica e operações de banco de dados?</summary>

A CWA está ligada à lógica de predicados e a todo o funcionamento da álgebra relacional que rege as diretrizes das *queries*, consultas e operações realizadas em cima do SGPD.

</details>

<details><summary>Qual a diferença de comportamento entre a CWA e bancos de dados probabilísticos?</summary>

Enquanto a CWA assume que algo é falso se não está no modelo, bancos de dados probabilísticos fornecem uma probabilidade de que algo seja verdadeiro ou falso.

</details>

## Conteúdo

`⏱ 00:00`

### Mundo Fechado e Mini Mundo

#### O conceito de Mundo Fechado

> [!exemplo] Consultas e o "não" no Mundo Fechado
> Para exemplificar, imagine uma tabela com alunos (`alumni`) e seus graus obtidos.
> >
> **Cenário 1: Informação presente e verdadeira**
> > > **Pergunta:** Qual é o menor grau que eu tenho na minha entidade, menor que um PHD?
> > > **Processo:** O banco de dados procura nas instâncias relacionadas à entidade qual aluno possui um grau menor que PHD.
> > > **Resultado:** Retorna que Peter tem mestrado. Sim, ele tem um grau menor.
> >
> **Cenário 2: Informação ausente no modelo**
> > > **Pergunta:** Existe algum aluno que não tem um grau superior, como mestrado, tendo ido apenas até bacharel?
> > > **Processo:** Essa informação não existe no banco de dados.
> > > **Resultado:** Se a pergunta for feita de forma aleatória, ou buscando um aluno com grau menor que mestrando, mas maior que mestrado, o sistema retornará `falso`, porque não possui essa informação.
> >
> **Cenário 3: Informação presente, mas falsa**
> > > **Pergunta:** Pedro possui o grau (`degree obtained`) igual a PHD?
> > > **Processo:** O sistema conhece essa informação.
> > > **Resultado:** Retorna `falso`, não porque não conhece a informação, mas porque a informação existe e realmente não é verdadeira.
> >
> **Conclusão:** Se você procura algo que não está contemplado no seu modelo, a resposta será `falso`. Essa é a ideia de **Mundo Fechado**.

> [!definicao] Mundo Fechado
> A ideia de que, se algo não está contemplado no modelo de dados, a resposta para uma consulta sobre essa informação será `falso`.

A partir desse cenário de mundo fechado, um contexto fechado do mundo real que se quer modelar, é praticamente impossível modelar todo o mundo relacionado ao problema. Por exemplo, ao modelar algo relacionado a vendas, é preciso verificar o que realmente é necessário dentro do modelo, dentro da modelagem, para que represente o contexto. Não é preciso colocar informações desnecessárias; será o mínimo necessário para representar e operacionalizar a situação.

#### O conceito de Mini Mundo

> [!definicao] Mini Mundo (ou Universo de Discurso)
> Um **mini mundo** (ou **universo de discurso**) é um pedaço do mundo real que se deseja modelar.
> O que se consegue representar no banco de dados é justamente esse pedaço, esse mini mundo.
> O modelo lógico, o banco de dados, será o modelo lógico que representa e armazena os dados relacionados a esse mini mundo.
> O termo "universo de discurso" é muito utilizado também em Inteligência Artificial (IA).

A ordem é a seguinte: pega-se um pedaço do mundo real, que se chama minimundo, e é preciso representá-lo a partir de um modelo lógico. O banco de dados, que possui esse modelo lógico, vai persistir e armazenar os dados relacionados ao minimundo.

Esse minimundo, por exemplo, pode ser a parte de universidades, onde há departamentos, cursos, professores e alunos. Dependendo do que se quer responder, ou seja, quais são as perguntas que se quer fazer, a modelagem será feita de uma forma diferente. Veremos um pouco mais para frente que, dependendo do tipo de relacionamento que se cria ou das entidades que estão conectadas, é possível representar algumas informações em detrimento de outras.

O conceito de mundo fechado está diretamente atrelado ao mini mundo, porque se está delimitando um espaço dentro do contexto, dentro do mundo real, e a partir dessa delimitação, responde-se "não" (falso) para o que está fora dela.

`⏱ 04:20`

a partir dessa delimitação, eu respondo não. Dentro do Minimundo, verificamos se algo é verdadeiro ou falso.

### Close World Assumption (CWA)

>[!definicao] Close World Assumption (CWA)
> Uma proposição ou afirmação relacionada à lógica de predicados. Ela está ligada a todo o funcionamento da álgebra relacional que rege as diretrizes das *queries*, das consultas e das operações que realizamos em cima do `SGPD`.

A **Close World Assumption (CWA)**, ou `CWA`, faz com que, a partir de uma determinada linha, não se responda a uma verificação. Em vez disso, simplesmente se assume que é falso.

>[!exemplo] Bancos de dados probabilísticos
> Em um contexto de bancos de dados probabilísticos, o comportamento seria diferente. A partir de uma determinada linha, seria fornecida uma probabilidade de que algo fosse verdadeiro ou falso.

## Relacionado

- [[logica-proposicional-negacao-e-equivalencia]]
- [[sgbds-historico-e-modelos-de-dados]]
- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[aplicacao-do-pensamento-computacional-jogo-de-adivinhacao-e-algoritmo-de-busca-b]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `preposição → proposição`
