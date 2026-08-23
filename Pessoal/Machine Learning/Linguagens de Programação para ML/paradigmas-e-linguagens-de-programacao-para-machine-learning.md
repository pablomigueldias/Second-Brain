---
titulo: "Paradigmas e Linguagens de Programação para Machine Learning"
tags: [machine-learning, linguagens-de-programacao, paradigmas-de-programacao, pensamento-computacional, fundamentos-de-algoritmos, conceitos]
data: 2026-08-23
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 28
conceitos: [Python, R, Scilab, Paradigmas de Programação, Programação Imperativa, Arquitetura de Von Neumann, Programação Lógica, Programação Funcional]
---

# Paradigmas e Linguagens de Programação para Machine Learning

> [!resumo] Do que se trata
> A aula aborda as linguagens de programação mais utilizadas em Machine Learning, focando em Python, R e Scilab, e explica a importância de entender os paradigmas de programação. São detalhados os conceitos de programação imperativa, lógica, funcional e orientada a objetos, mostrando como cada paradigma determina a visão de estruturação e execução de um programa.

## Para lembrar

- **Python é a linguagem mais utilizada em Machine Learning, pois possui as maiores bibliotecas e a maioria dos grandes grupos de pesquisa utiliza essa linguagem.**
- **O paradigma imperativo é relacionado à linguagem humana, pois descreve a computação como ações ou comandos que mudam estados das variáveis de um programa.**
- **A arquitetura de Von Neumann, que ainda é utilizada, possui uma Unidade Central de Processamento (CPU), uma memória primária e uma memória auxiliar.**
- **A programação lógica funciona com base em uma base de dados de conhecimento, e se uma pergunta não tiver resposta, significa apenas que não se sabe a informação, e não que ela seja falsa.**
- **O objetivo da Programação Orientada a Objetos é transformar um problema do mundo real em partes, permitindo que o computador compreenda esses problemas em módulos e possibilitando um programa com melhor nível de abstração.**

## O que esta nota responde

- Quais são as linguagens de programação mais usadas em Machine Learning?
- O que são os paradigmas de programação e por que eles são importantes?
- Como a Programação Orientada a Objetos ajuda a modelar problemas do mundo real em software?

## Conceitos

**Python** · **R** · **Scilab** · **Paradigmas de Programação** · **Programação Imperativa** · **Arquitetura de Von Neumann** · **Programação Lógica** · **Programação Funcional**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e, na aula de hoje, vamos começar a ver a parte de linguagens de programação para Machine Learning.

A ideia é que, neste curso, vejamos as principais linguagens e suas aplicações. Vou comentar um pouco sobre cada uma, onde aplicamos principalmente cada linguagem, se ela é mais voltada para a academia, ou se é uma linguagem mais voltada para o desenvolvimento de software.

A princípio, vamos aprender um pouco sobre:
- `Python`
- `R`
- `Scilab`

Para quem nunca ouviu falar sobre `Scilab`, certamente já deve ter ouvido falar sobre a ferramenta `MATLAB`. A ferramenta `Scilab` é uma versão gratuita do `MATLAB`.

Vamos usar essas ferramentas e ver um pouco sobre elas na aula de hoje.

### Programação em Machine Learning

Agora, vamos começar a programar efetivamente os nossos projetos. Principalmente, utilizaremos `Python`.

Embora possamos acabar utilizando `Scilab` e `R` para alguns exemplos — para não ficarmos muito fechados em um único tipo de linguagem, é legal vermos outras linguagens — o foco principal será o `Python`.

Usaremos `Python` porque é onde temos as maiores bibliotecas para Machine Learning. Os maiores grupos de pesquisa em Machine Learning estão utilizando `Python`.

Para dar um exemplo: Quando entrei no meu doutorado, eu não programava em `Python`. Eu estava firme e forte com a linguagem `C`, programando tudo em `C`. Chegou um momento em que eu estava tendo que programar tanta coisa que já estava pronta em `C`, que pensei: "Pera lá, vamos testar um pouco dessa linguagem em `Python` para ver como é."

Isso facilitou muito a minha vida. Meu doutorado acabou sendo todo programado em `Python`, porque eu precisava de uma biblioteca. A biblioteca fazia uma função que, como eu estava programando em `C`, eu acabava refazendo as coisas. Isso não é legal. As ferramentas existem aí para ajudar no nosso dia a dia.

Portanto, `Python` é o que vamos usar mais aqui no curso.

Como mencionei, vamos começar trabalhando primeiramente com essas linguagens: `Python`, `R` e `Scilab`. Vou tentar sempre mostrar exemplos que são simultâneos nas três linguagens, para que vocês vejam qual é a dificuldade de se trabalhar com uma ou com outra, e para que possamos comparar.

No entanto, chegará um determinado ponto em que vamos ficar trabalhando só com `Python`, que é o nosso foco aqui do curso.

### Paradigmas de Programação

Falando sobre linguagens, não podemos esquecer de falar sobre os paradigmas de programação.

Os paradigmas de programação são importantes para que tenhamos noção do porquê estar utilizando aquela linguagem, do porquê investir nela, e do porquê aquela linguagem tem aquele comportamento.

Nesse contexto, vou comentar um pouco sobre o que são paradigmas de programação.

Eu costumo dizer que um paradigma de programação determina a visão que o programador, o desenvolvedor, possui sobre a estruturação e a execução do programa que ele está codificando.

Essa noção determina a visão dele sobre o programa: como ele será executado, como ele deve ser estruturado, até mesmo a sintaxe do programa, o formato de abordar uma função — se vai ser uma função encapsulada, ou se eu vou ter a chamada...

`⏱ 05:40`

...de uma função de forma recursiva, ou se eu vou utilizar uma programação que é mais lógica, se ela é funcional. Tudo isso envolve os paradigmas de programação, e isso ajuda muito o programador a decidir qual é a melhor linguagem e qual é o melhor paradigma para utilizar na programação.

Às vezes, a gente fica sofrendo com uma linguagem. Por exemplo, no meu doutorado, eu estava usando `C` e pensando: "Não vou usar `Python`, não vou querer aprender uma linguagem nova agora, porque eu já tenho um monte de coisa para fazer." Mas aí eu fui vendo `Python` e pensei: "Caramba, estou perdendo tempo aqui com `C`."

A ideia é essa: saber utilizar a melhor linguagem que envolva o melhor paradigma de programação para o problema que estamos passando.

### Paradigma de Programação Orientada a Objetos (POO)

Em programação orientada a objeto, o programador pode abstrair um programa como uma coleção de objetos que interagem entre si. A Programação Orientada a Objetos é, portanto, um tipo de paradigma de programação.

Qual é a vantagem?

Na POO, conseguimos estruturar melhor nosso programa, de forma que quem for usar o meu código consiga entender o comportamento dele de forma clara. Isso é crucial quando eu vou reutilizar o código de alguém ou quando aquele projeto vai ser evoluído por outra pessoa.

Até mesmo por nós mesmos. Quando fazemos um programa e deixamos ele mal comentado ou nem comentamos, depois, quando pegamos o nosso programa, a gente não lembra, e aí pensamos: "Nossa, é melhor refazer esse código."

A Programação Orientada a Objetos tem esse destaque: criar vários objetos, uma coleção de objetos que cada objeto representa parte de um problema em um todo.

Se analisarmos nosso dia a dia, é praticamente isso que fazemos. Não acordamos e pensamos: "Vou resolver todos os meus problemas agora, de uma vez só." Não. Temos que ir lá: "Bom, agora eu vou trabalhar, agora eu vou participar de uma reunião, agora eu vou ir no mercado comprar minhas coisas para fazer meu almoço." Tudo é feito meio que por partes, não é mesmo?

### Os Paradigmas de Programação

A linguagem com paradigma orientado a objeto tem essa faculdade especialidade. Quais são os paradigmas que temos em programação?

*   O paradigma lógico.
*   O paradigma funcional.
*   O paradigma imperativo.
*   O paradigma orientado a objetos.

É muito importante que a gente entenda esses paradigmas para pensar como resolver os nossos problemas de computação, principalmente no nosso caso, dando resoluções para problemas de *machine learning*.

### Paradigma de Programação Imperativa

O paradigma de programação imperativa está relacionado muito com a forma como fazemos comunicações com o mundo real.

A gente vai lá, coloca uma condição: "Se aquela condição é satisfeita, a gente realiza a nossa saída." A programação imperativa tem essa cara.

Por exemplo, alguém me chama para ir almoçar no shopping. Eu digo: "Bom, se eu tiver dinheiro e eu tiver carro para ir para o shopping, eu vou almoçar."

Essa é a cara da programação imperativa, relacionada com a nossa linguagem, que é a linguagem de comunicação humana, que também é imperativa. Esse paradigma...

`⏱ 10:20`

Escreve-se a computação como ações, enunciados ou comandos que mudam estados das variáveis de um programa. Esse paradigma foi inicialmente projetado para a arquitetura de computadores prevalecente.

A arquitetura que usamos até hoje é a de Von Neumann. Essa arquitetura foi modelada a partir de seu hardware e ainda utilizamos até hoje. Ela possui:

- Uma unidade central de processamento (CPU).
- Uma memória primária, que armazena nosso programa e nossos dados.
- Uma memória auxiliar, que guarda toda a nossa informação de forma massiva.

Essa linguagem é muito aplicada nesse tipo de arquitetura, pois ela se dá muito bem tanto pela proximidade do processamento com a memória, quanto pelo fácil acesso do programa aos dados da memória. Tudo acontece muito rápido.

### Linguagens Imperativas

Um exemplo de linguagem imperativa é a linguagem `C` e a linguagem `assembly`. São linguagens muito utilizadas nesse formato de programação imperativa e acredito que são as mais conhecidas dentro desse paradigma.

### Programação Lógica

Falando sobre o paradigma de programação lógica, ela está muito próxima de como um computador funciona. Como um processador processa informação, certo?

Porém, sabemos que os processadores trabalham também com uma linguagem próxima à lógica. Na verdade, o processador trabalha de forma lógica; é um processador lógico. Temos ali na estrutura de processamento portas lógicas que manipulam os nossos dados.

Atualmente, a programação lógica é mais utilizada para:

- Inteligência Artificial (IA), principalmente para criar bases de dados. Por exemplo, em um sistema inteligente, quando eu tenho uma combinação de valores na entrada, qual é a resposta que ele deve dar na saída? É mais ou menos dentro desse cenário que a programação lógica é utilizada.
- Processamento de Linguagem Natural (PLN). Isso ocorre porque precisamos ter bases de dados bem definidas para que reconheçamos o significado de uma fala ou de uma frase que uma pessoa disse.

Quando damos um "Ok Google" no nosso celular e pedimos para pesquisar "a farmácia é mais próxima", como o sistema consegue processar essa linguagem? Ele consegue processar porque possui bases de dados bem definidas de forma lógica.

### Fundamentos da Programação Lógica

A lógica tem o objetivo de trazer o estilo da lógica matemática para a programação de computadores. Quando falamos de programação lógica, basicamente estamos tentando trazer a matemática e a lógica matemática para os computadores.

Aqui eu até coloquei um exemplo: o de um circuito combinacional, que é mais ou menos como um processador funciona, utilizando portas lógicas para processar uma função.

Falando de programação lógica, faremos mais ou menos a mesma forma, porém utilizando algum tipo de linguagem. Uma das linguagens mais conhecidas é a linguagem `Prolog`.

A linguagem `Prolog` é uma linguagem muito famosa para a parte de programação lógica.

Temos aqui, por exemplo, uma base de dados que diz que:

- Maria gosta de flores.
- Maria gosta de Pedro.
- Paulo gosta de Maria.

Se fizermos uma pergunta sobre a nossa base de dados, isso significa que temos uma base de dados que passamos para a máquina, e essa base de dados vai retornar para nós um conhecimento.

Se fizermos essa pergunta para a máquina...

`⏱ 15:40`

Como, por exemplo, do que é que Maria gosta? Eu tenho aqui uma pergunta: o meu `x` é a minha incógnita. Eu vou procurar na minha base de dados. Minha base de dados informa que Maria gosta de flores. Se a gente perguntar do que Maria gosta, o `prolog` vai responder que a variável `x` é igual a `flores`.

Isso é uma base de dados que contém informações sobre o cenário de modelagem do meu problema. Porém, se eu fizer uma pergunta e não houver resposta, não quer dizer que aquela resposta não seja verdadeira.

Por exemplo, se eu perguntar do que é que Diego gosta? Essa informação não está na minha base de dados. Isso não quer dizer que Diego não goste de nada. Quer dizer que eu não sei do que Diego gosta, porque eu não tenho isso na minha base de conhecimento. A programação lógica funciona dessa forma.

### Paradigma de Programação Funcional

Falando sobre o paradigma de programação funcional. A ideia é trabalhar com funções. O próprio nome já indica que o paradigma funcional é um paradigma bem matemático. Para quem tem noção de matemática, a ação funcional é bem visível.

É uma linguagem muito utilizada no meio acadêmico, mas também é muito utilizada em empresas que trabalham com análise estatística.

Vamos ver exemplos do `R` aplicado em situações onde precisamos fazer um levantamento estatístico sobre um problema, onde é mais fácil usar o paradigma funcional do que aplicar um algoritmo em `Python`, porque ele é bem focado para resolver um problema matemático.

A programação funcional é um paradigma de programação que trata a computação como avaliações de funções matemáticas. Teremos um problema que será decifrado e solucionado por meio de funções. As funções retornam um resultado sobre algum determinado comportamento do nosso sistema, como o reconhecimento de um padrão.

Se pegarmos, por exemplo, a função `2 + 2 * 3`. Muita gente fará: `2 + 2`, que é 4, vezes 3, resultando em 12. Isso está errado. Por quê? Sabemos que temos que fazer primeiro a multiplicação: `2 * 3`, que é 6, mais 2, que é igual a 8.

A programação funcional trabalha nesse sentido, com funções matemáticas. O resultado é sempre gerado de forma determinística, já que trabalhamos com funções e a entrada de dados é bem definida para o nosso problema.

É muito aplicado em problemas que temos na área estatística. Ao longo do nosso curso, estudaremos modelos probabilísticos e modelos de regressão. Às vezes, analisar um modelo desse se torna mais fácil utilizando programação funcional.

A programação funcional não é necessariamente específica para um tipo de linguagem. Se pegarmos a linguagem `Python`, ela tem suporte para a programação funcional. Se pegarmos o `JavaScript`, também temos suporte para a programação funcional.

Tanto no `Python` quanto no `JavaScript`, podemos usar trechos de código com funções matemáticas para solucionar uma determinada equação e retornar um determinado valor que estamos esperando. Por exemplo, eu posso aplicar Pitágoras para descobrir o lado de um triângulo retângulo. Eu aplico e essa função me retorna o valor que estou esperando.

`⏱ 20:40`

### Programação Funcional

Para um determinado ponto do algoritmo, temos como chamar uma função para resolver o problema. 

Na linguagem `Scheme`, que é uma das linguagens voltadas para a programação funcional, temos um cálculo de `λx`, com funções de soma aplicadas sobre as variáveis `x` do programa e uma multiplicação entre `3` e `4`:

- `3` vezes `4` é igual a `12`, portanto `x` vale `12`;
- O resultado dessa equação será `x` mais `x`, ou seja, `12` mais `12`, que resulta em `24`.

Essa estrutura lembra a forma de aplicar uma equação em calculadoras antigas — aquelas com fita de papel —, nas quais se inseriam os valores e os operadores dessa maneira.

### Paradigma de Programação Orientada a Objetos

O objetivo da programação orientada a objetos é transformar um problema do mundo real em partes, permitindo que o computador compreenda esses problemas em módulos e possibilitando um programa com melhor nível de abstração.

Comparando a programação estruturada com a orientada a objetos:
- Na **programação estruturada**, há diversas funções agrupadas gerando a resposta.
- Na **programação orientada a objetos**, temos métodos e dados definidos dentro de objetos particulares.

Essa organização garante o reaproveitamento de código e de objetos. Por exemplo, em um sistema bancário, ao criar um método de saque para diferentes tipos de conta (conta-salário, conta-corrente, conta-poupança), utiliza-se a mesma operação de saque para contas distintas.

Os principais benefícios incluem:
- **Herança**: facilita o reaproveitamento de código;
- **Abstração**: simplifica a representação do mundo real em formato de objetos, evitando a complexidade de tentar abstrair um problema inteiro de uma só vez;
- **Encapsulamento**: protege métodos e dados para que não fiquem acessíveis a qualquer parte do código.

A programação orientada a objetos auxilia bastante na área de *Machine Learning*, em que há muitos elementos compondo um problema e a divisão em objetos facilita o desenvolvimento. Uma das linguagens que trabalha com orientação a objetos e é amplamente utilizada nesse cenário é o `Python`.

### Programação Multiparadigma

A linguagem `Python` é uma linguagem multiparadigma, pois utiliza...

`⏱ 25:40`

Pouco da programação funcional, um pouco da programação orientada a objetos. Mas também temos ambientes que trabalham com programação. Além da programação orientada a objetos, podemos trabalhar com outros paradigmas de programação.

Nesse cenário, temos, por exemplo, a linguagem `Python`, que já discutimos aqui, mas também temos a ferramenta `SciLab`. Ele é, falando a grosso modo, um ambiente de computação numérica e um laboratório de matrizes. Aqui trabalhamos com multi-paradigmas.

Temos programação funcional e programação orientada a objetos. Há vários paradigmas dentro dessa ferramenta, o que facilita a vida do programador. Por exemplo, ele precisa chamar um bloco para executar uma rede neural. Há um bloco lá no programa, como se fosse uma biblioteca, que realiza o processamento da rede neural. Depois, há um módulo que vai gerar o gráfico, que vai plotar o gráfico.

É uma linguagem muito legal para trabalharmos, uma ferramenta muito potente e usada principalmente por quem trabalha na área de matemática, na área de estatística e para quem trabalha na área de machine learning, que utiliza tudo isso. É uma ferramenta muito importante.

### Aplicações Profissionais e Modelagem

Muitas pessoas dizem: "Ah, mas é uma ferramenta muito acadêmica. Isso é para o professor ensinar conteúdo." No entanto, eu tenho vários exemplos de empresas que utilizam tanto o `MATLAB` quanto o `SciLab` como ferramenta de desenvolvimento.

Toda a modelagem do problema é feita aqui. Depois, é utilizada uma linguagem para embarcar o `code` e tudo mais.

### Conclusão sobre Linguagens

Esse conteúdo de Machine Learning voltado para linguagens foi importante para discutirmos um pouco sobre o que existe de linguagem. Sobre por que usar uma e não a outra, e vice-versa. E para entendermos também que não existe a melhor linguagem. Existe a melhor linguagem para determinado problema, mas não existe uma linguagem universal.

## Relacionado

- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[historia-da-computacao-paradigmas-e-problemas-computacionais]]
- [[paradigmas-de-programacao-estruturado-e-orientacao-a-objetos]]
