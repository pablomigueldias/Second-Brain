---
titulo: "Paradigmas de Programação: Estruturado e Orientação a Objetos"
tags: [linguagens-de-programacao, fundamentos, conceitos, pensamento-computacional, estruturas-de-dados]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 16
conceitos: [Paradigmas de programação, Paradigma estruturado, Programação orientada a objetos (POO), Classe e objeto, Atributos e métodos, Herança, Reuso de código]
---

# Paradigmas de Programação: Estruturado e Orientação a Objetos

> [!resumo] Do que se trata
> A aula explora a definição e os principais tipos de paradigmas de programação, com ênfase no paradigma estruturado e na orientação a objetos. São detalhados os conceitos de classes, objetos, atributos, métodos, estados e herança a partir de exemplos práticos como a modelagem de uma caneta. Por fim, são analisadas as vantagens e trade-offs de cada abordagem, destacando a eficiência para problemas diretos no estruturado versus o reuso de código em POO.

## Para lembrar

- **Um paradigma de programação define diretrizes, regras e limites específicos para a resolução de problemas em um contexto determinado.**
- **O paradigma estruturado baseia-se em sequência, decisão (testes lógicos) e iteração (laços), sendo altamente eficiente para aprendizado e problemas diretos.**
- **Em Programação Orientada a Objetos, um objeto é uma instância de uma classe alocada na memória, composto por atributos (características), métodos (comportamentos) e estados.**
- **A herança permite que classes filhas herdem métodos e atributos de uma classe mãe mais genérica, podendo especializar ou sobrescrever comportamentos para seu próprio contexto.**
- **A principal vantagem da Orientação a Objetos é o reuso de código e a facilidade de instanciar novas estruturas a partir de moldes pré-definidos.**

## O que esta nota responde

- Qual a diferença fundamental entre os pilares do paradigma estruturado e da orientação a objetos?
- Como se diferenciam atributos, métodos e estados na definição de uma classe e de um objeto?
- Quais são os benefícios do uso de herança e reuso de código no paradigma orientado a objetos?

## Conceitos

**Paradigmas de programação** · **Paradigma estruturado** · **Programação orientada a objetos (POO)** · **Classe e objeto** · **Atributos e métodos** · **Herança** · **Reuso de código**

## Conteúdo

`⏱ 00:00`

Muito bem. Chegamos à nossa etapa 5, onde iremos falar dos paradigmas de programação. Vou dar um sobrevoo sobre alguns existentes e vou focar em dois.

Vamos definir primeiro: Um paradigma é a forma de resolução de problemas com diretrizes e alimentação específicas de cada paradigma, utilizando linguagem de programação. Um paradigma possui regras para resolução de um problema e ele está limitado por uma diretriz, está limitado a um contexto específico.

### Tipos de Paradigmas

Dentro desse mundo de paradigmas, temos alguns, entre eles:

- Orientação a Objeto
- Procedural
- Funcional
- Estrutural
- Computação Distribuída
- Lógico

O procedural está relacionado às chamadas sucessivas e procedimentos separados, essa ideia de sequência. O funcional está fundamentado em instruções baseadas em funções. O estruturado já está atrelado a estruturas de blocos alinhados. A computação distribuída, por sua vez, possui funções executadas de forma independente.

Para que o programa possa ser distribuído dentro do cluster, ele deve ser criado de tal forma que tenha módulos independentes dentro dele.

Os mais utilizados dentro desse mundo de paradigmas são Orientação a Objeto e o Estruturado.

### Paradigma Estruturado

Exemplos que podemos tirar de linguagens de programação são o `C` e o `Java`.

O paradigma estruturado traz consigo a ideia de:

- Sequência
- Decisão
- Iteração

A ênfase dele é em instruções sendo executadas em sequência. Independentemente se ela tem uma estrutura condicional ou estrutura de repetição, todas as instruções são executadas em sequência.

O `C` foi largamente utilizado e é parte principalmente para aprendizado.

A decisão, nesse caso de um paradigma estruturado, já está relacionada a um teste lógico. Já a iteração, ela está relacionada a laços e estruturas condicionais.

Como comentei, ele dominou o mercado até o advento da programação orientada a objeto.

Qual é a utilização desse tipo de paradigma estruturado? Ele é usado até hoje. O `C` possui uma performance superior por ser mais baixo nível do que as demais linguagens. Consequentemente, é mais difícil de programar, mas ele é ótimo para você aprender com ele.

Geralmente, em faculdade ou mestrado, você vai programar um tipo de dado abstrato em `C`. Ou seja, vai programar uma pilha, vai programar uma fila, uma árvore, um grafo em `C`. Porque quando a gente leva isso para linguagens de mais alto nível, já vem pronto. Por exemplo, em Python, se você for criar uma lista, é `list`. Mas se você for olhar lá no código fonte, como que ele foi programado, está em `C`.

### Eficiência e Desafios de Paradigmas

O paradigma estrutural é muito eficiente para problemas simples e diretos e para aprendizado de programação.

No caso, o POO ainda não é compreendido por muitos. Ainda tem pessoas que têm dificuldade com o conceito de orientação a objeto.

Aqui um exemplozinho, bem simples, uma função em `C`: `function fatorial x`. Aqui ele retorna, se `x` maior que 1, retorna `x` fatorial `x` menos 1. Isso daqui é por recursão.

O que acontece? Até ele chegar no número 1, de `x` a 1, ele vai fazer a multiplicação. Aí ele começa a voltar por recursão.

Esse é um outro tema. Isso aqui é só uma exemplificação. Recursão é um tema um pouquinho mais complicado para quem está iniciando.

### Programação Orientada a Objeto

E a programação orientada a objeto? Qual é o conceito aí que está atrelado?

`⏱ 05:40`

O conceito de objeto tenta ser análogo ao mundo real. Ele baseia a programação na utilização de objetos e suas interações.

Quem é um objeto? Um violão, um robô, uma bota, um telescópio — tudo isso são objetos. Em um sentido mais amplo, dentro do mundo da orientação a objetos, tudo isso é considerado um objeto.

Podemos extrapolar e generalizar esse conceito, puxando o pensamento computacional para abstrair uma classe. Lembre-se que a classe é uma abstração de uma entidade de software.

### O que é um Objeto?

Um objeto é descrito por três elementos principais: características específicas, comportamentos e estados.

*   **Características:** São os atributos.
*   **Comportamento:** São os métodos associados.
*   **Estado:** É o estado em que o objeto se encontra.

Isso significa que:
*   **Características** são o que eu tenho.
*   **Comportamento** é o que eu sou capaz de fazer.
*   **Estado** é como eu faço.

### Exemplo Prático: A Caneta

Vamos supor que temos uma caneta e queremos especificar um modelo dela. Para fazer isso, precisamos definir a classe da caneta.

**1. Atributos (O que eu tenho):**
*   Modelo
*   Cor
*   Carga
*   Corpo
*   Tampa
*   Ponta

Tudo isso são os atributos, são as características da caneta.

**2. Métodos (O que eu sou capaz de fazer):**
Qual é o comportamento? Eu escrevo, desenho, rabisco, pinto, destampo. Tudo isso são comportamentos, representados como métodos. Um método é uma função associada a uma classe.

**3. Estados (Como eu faço):**
*   Estampada
*   Destampada
*   Em uso

De maneira geral, um objeto possui atributo, comportamento e estado. O que eu tenho é o atributo; o que sou capaz de fazer são os métodos; e como faço são os estados. Isso reflete o conceito de orientação a objetos.

### A Classe e a Programação

Ao classificar a caneta, precisamos identificar o modelo. Esse modelo é a nossa classe, e ela deve conter todas as informações que mencionamos: os atributos, os métodos e os estados.

Os tipos de canetas podem variar, mas ela está baseada nesse modelo. A cor, o modelo e o tipo de tampa podem variar; os atributos podem variar, e isso é normal.

Do ponto de vista de programação, o objeto é uma classe, e a parte de programação do objeto aloca em memória uma instância dessa classe, que é o objeto. Essa instância possui operações associadas, que são os métodos.

Em uma forma estrutural configurada, temos:
1.  Alocação de memória.
2.  Operações associadas.

É importante notar que as operações estão desassociadas de uma variável. Temos variáveis, métodos, estados e atributos associados a um objeto, e especialmente a uma classe, e somente aquela classe.

Por exemplo, a classe pode ter atributos como `cor`, `carga` e `tampa`.

O método `escrever` é um comportamento. O método é uma função associada a uma classe.
*   Se estiver destampada, o método `escrever` é executado.
*   Se não estiver, escreve algo. Ou seja, se ela estiver destampada, eu vou escrever.

E o método `tampar` define o estado `tampada` como igual a `true`.

`⏱ 10:40`

Isso é só uma exemplificação. Nós temos os pilares da orientação a objeto. Ele realmente tem algumas informações mais rebuscadas do que um estruturado. É mais intuitivo.

Nós temos:
- Herança
- Encapsulamento
- Polimorfismo
- Abstração

Vamos ver cada um separadamente.

### Herança
Com relação à herança, temos que uma classe filha herda características de uma classe mãe. Isso inclui os atributos, os métodos e o comportamento.

No entanto, a classe filha pode ter especializações próprias, podendo ter atributos e métodos específicos dela. Ela também pode sobrescrever métodos que são herdados e atribuir operações referentes ao seu próprio contexto.

A classe mãe geralmente tem um comportamento mais geral, enquanto as classes filhas que recebem por herança, possuem comportamentos mais específicos.

### Vantagens e Paradigmas
O que é interessante na orientação a objeto é o reuso de código.

Uma vez que eu determino um objeto, por exemplo, uma caneca, e coloco os métodos e as características associados àquela classe, sempre que eu precisar instanciar um novo objeto, será muito mais fácil, porque já tenho uma quantidade enorme de código associado que me define exatamente a estrutura de uma caneca.

Já o paradigma estruturado ataca problemas específicos e diretos.

Existe aí um *trade-off*: você tem que identificar qual é o seu problema, como que ele se resolveria e qual seria o melhor paradigma a ser utilizado dentro desse contexto.

Por exemplo, quando utilizaríamos um paradigma estruturado?

A gente poderia estar fazendo análise de dados com `Python`. Ele também tem orientação a objetos, ele também tem o paradigma funcional e outros paradigmas. Contudo, ele é uma linguagem interpretada, o que o torna mais lento.

Nesse caso, a gente poderia estar utilizando o `C`, se fosse o caso de ganho de performance.

É aí que fica a cargo de cada um identificar qual que é o paradigma mais adequado para o seu contexto.

## Relacionado

- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
- [[visao-geral-da-carreira-em-ti-da-rede-a-ciencia-de-dados-e-programacao]]
- [[historia-da-computacao-paradigmas-e-problemas-computacionais]]
- [[fundamentos-e-pilares-do-pensamento-computacional]]
