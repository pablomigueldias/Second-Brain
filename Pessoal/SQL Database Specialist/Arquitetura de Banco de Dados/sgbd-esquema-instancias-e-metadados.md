---
titulo: "SGBD: Esquema, Instâncias e Metadados"
tags: [sgbd, banco-de-dados, conceitos, dados, organizacao, modelagem-de-dados]
data: 2026-09-30
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 7
conceitos: [Esquema, Construtores, Instâncias, Estado de Banco de Dados, Snapshot, Metadados, SGBD, Modelo Relacional]
---

# SGBD: Esquema, Instâncias e Metadados

> [!resumo] Do que se trata
> A aula define o esquema como uma descrição concisa da estrutura do banco de dados, sem dados persistidos, servindo como base para as instâncias. Explora como as instâncias representam o estado atual dos dados, que muda através de operações, e introduz o conceito de snapshot. Por fim, detalha os metadados como a descrição do esquema, construtores e regras, essenciais para o funcionamento do SGBD.

## Para lembrar

- **O esquema é uma descrição concisa do banco de dados, mostrando objetos, atributos e suas interações, funcionando como um "esqueleto" sem dados persistidos.**
- **Dentro do SGBD, existe um campo específico para metadados e esquema, utilizado para consultas e para entender a estrutura de um determinado banco de dados.**
- **As instâncias são os dados persistidos que devem condizer com o que está definido no esquema, e suas modificações alteram o estado do banco de dados.**
- **Um snapshot é uma figura do banco de dados em um determinado momento, representando sua estrutura e o conjunto de dados definidos naquele instante, como uma foto do banco de dados.**
- **Metadados consistem na descrição do esquema, nos construtores bem apresentados e nas regras (constraints) que o banco de dados está mantendo.**

## O que esta nota responde

- O que é o esquema de um banco de dados e qual sua função principal?
- Qual a diferença entre o esquema e o estado (ou instâncias) de um banco de dados?
- O que são metadados em um SGBD e qual sua importância para a estrutura do banco de dados?

## Conceitos

**Esquema** · **Construtores** · **Instâncias** · **Estado de Banco de Dados** · **Snapshot** · **Metadados** · **SGBD** · **Modelo Relacional**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Esquema: descrição, estrutura e construtores | ▪▪ |
| `04:20` | Snapshot, estado e metadados do SGBD | ▪▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Esquema** | É uma descrição concisa do seu banco de dados. Ele mostra os objetos e atributos relacionados, e como eles interagem entre si. Pode ser visto como uma 'história' ou um 'esqueleto' do banco de dados. |
| **Snapshot** | É uma figura do banco de dados em um determinado momento, representando a estrutura e o conjunto de dados definidos naquele instante. É, praticamente, uma foto do banco de dados. |
| **Metadados** | Consistem na descrição do esquema, nos construtores bem apresentados e nas regras (constraints). |

## Pegadinhas

- O esquema não possui instâncias nem dados persistidos, enquanto as instâncias são os dados que condizem com a estrutura do esquema.
- A modificação de dados dentro do banco de dados acarreta na mudança do estado, não na modificação do esquema.

## Teste-se

<details><summary>O que é um esquema de banco de dados?</summary>

É uma descrição concisa do banco de dados, mostrando objetos, atributos e suas interações. Pode ser visto como um esqueleto ou história da estrutura.

</details>

<details><summary>Qual a relação entre o esquema e as instâncias de um banco de dados?</summary>

O esquema define a estrutura e não possui instâncias nem dados persistidos. As instâncias são os dados que condizem com a estrutura definida pelo esquema.

</details>

<details><summary>O que é um snapshot no contexto de um banco de dados?</summary>

É uma figura do banco de dados em um determinado momento, representando sua estrutura e o conjunto de dados definidos naquele instante. É, praticamente, uma foto do banco de dados.

</details>

<details><summary>Como o SGBD utiliza o esquema?</summary>

O SGBD utiliza o esquema para fazer consultas e entender a estrutura de um determinado banco de dados dentro do sistema.

</details>

<details><summary>O que são metadados em um SGBD?</summary>

Metadados consistem na descrição do esquema, nos construtores bem apresentados e nas regras (constraints) do banco de dados.

</details>

## Conteúdo

`⏱ 00:00`

Olá! Vamos falar agora sobre esquema, instâncias e estado de banco de dados.

### Esquema

Primeiro, vamos definir o que é um esquema.

> [!definicao] Esquema
> É uma descrição concisa do seu banco de dados.
> Ele mostra os objetos e atributos relacionados, e como eles interagem entre si.
> Pode ser visto como uma "história" ou um "esqueleto" do banco de dados.

Essa descrição pode ser representada através de um diagrama. Isso é diferente do que está sendo persistido no banco de dados. Não que a estrutura seja distinta, mas a ideia de um diagrama voltado para um esquema é diferente da inserção de dados em si. Nossa preocupação aqui é definir a estrutura que será a base para a persistência dos dados.

Dentro do próprio `SGBD`, existe um campo específico para metadados e esquema. O `SGBD` utiliza esse campo para fazer consultas e entender a estrutura de um determinado banco de dados dentro do sistema.

O diagrama depende do tipo de modelo de banco de dados. No nosso caso, o diagrama está relacionado ao modelo relacional.

> [!exemplo] Estrutura do banco de dados (Canavate)
> Usando o exemplo do livro de referência Canavate, temos as entidades: estudante, curso, pré-requisitos de sessão e relatório da grade.
> >
> O que percebemos aqui é que se trata apenas da estrutura. Por exemplo, para o objeto estudante, definimos as características essenciais, utilizando a abstração. Informações como cor preferida, filme preferido ou o caminho que faz entre casa e universidade são desnecessárias para o nosso contexto. Focamos no essencial.
> >
> Da mesma forma, isso se aplica a curso, pré-requisito, sessão e relatório da grade.

Dentro do esquema, nossas entidades, ou objetos, são denominados **construtores**.

O nosso **esquema**, ou esqueleto, não possui instâncias. Ele não possui nenhum tipo de dado persistido. Também não contém o tipo de dado nem os itens, sendo que os itens seriam os dados persistidos.

O que buscamos nesse esquema, nessa descrição, é apenas como são e o que compõe nossos construtores, nossas entidades.

Os dados mudam. Definimos uma estrutura, um esquema, porque nossos dados mudam. Inserimos, retiramos, operamos e atualizamos. Existe uma série de operações que ocorrem sobre os dados que causariam inconsistência se utilizássemos as **instâncias** como base.

Primeiro, criamos a estrutura, que é o esquema. Ele é uma base geral para qualquer instância que venha a ser persistida dentro dessa estrutura. A instância, ou seja, os dados que serão persistidos, deve condizer claramente com o que está definido no esquema.

`⏱ 04:20`

Como os dados mudam, existe um **snapshot** desses dados. Quando consultamos uma tabela, puxamos uma figura do que ela representa, do que ela nos mostra de dados. Temos uma foto, um snapshot.

A cada modificação, a cada atualização de informações dentro do nosso sistema, e através de um `insert`, um `delete`, um `update`, existe uma modificação de estado. Agora não estou falando de esquema, e sim de modificação de dados dentro do meu banco de dados, o que acarreta na mudança do estado. Falei modificação do esquema, mas na verdade é a modificação do estado do banco de dados.

> [!definicao] Snapshot
> É uma figura do banco de dados em um determinado momento, representando a estrutura e o conjunto de dados definidos naquele instante. É, praticamente, uma foto do banco de dados.

Temos um estado inicial. Esse estado inicial é condizente com o nosso esquema. Nosso snapshot, nosso estado inicial, é vazio. Por que ele é vazio? Porque não tem nada persistido. Ele está bem alinhado com o que é o nosso esquema. Conseguimos fazer um paralelo entre os dois, e um representa o outro. O esquema é equivalente ao estado inicial do banco de dados, que é um estado vazio.

A partir do momento que realizamos uma série de ações e levamos o banco de dados de um estado antigo válido para um novo estado válido, criamos uma atualização de informação, e esse estado passa a se modificar. Temos agora uma quantidade X de dados persistentes, e eles são diferentes. Nosso esquema e nosso estado inicial são diferentes.

Lembrando que o banco de dados utiliza o esquema para eventuais consultas e para entender melhor como estão posicionadas e descritas as identidades dentro do banco de dados de um SGBT. Toda mudança acaba acarretando a evolução do esquema.

> [!atenção] Modificação de Esquema
> Não é trivial fazer uma modificação de esquema. Embora seja mais facilitado se comparado à abordagem tradicional, ainda assim não é trivial.

### Metadados

O que são meus **metadados**?

> [!definicao] Metadados
> Consistem na descrição do esquema, nos construtores bem apresentados e nas regras (constraints).

Temos, na verdade, um snapshot com relação a toda a estrutura que o nosso banco de dados está mantendo.

## Relacionado

- [[bancos-de-dados-definicao-acesso-e-escala]]
- [[sgbd-ganhos-e-otimizacao-operacional]]
- [[sgbd-natureza-autodescritiva-esquema-e-catalogo]]
- [[sgbd-etapas-estrutura-e-fases]]
