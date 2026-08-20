---
titulo: "Características de um Programa de Software: Legibilidade, Redigibilidade, Confiabilidade e Custo"
tags: [engenharia-de-software, algoritmos, conceitos, linguagens-de-programacao, dados, estudos]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 7
conceitos: [Legibilidade, Redigibilidade, Confiabilidade, Custo, Ortogonalidade, Modularização, Verificação de tipos, Tratamento de exceções]
---

# Características de um Programa de Software: Legibilidade, Redigibilidade, Confiabilidade e Custo

> [!resumo] Do que se trata
> A aula aborda as diretrizes e características essenciais que devem ser consideradas no desenvolvimento de um programa de software. São discutidos conceitos como legibilidade, que se refere à facilidade de leitura do código, e redigibilidade, que trata da facilidade de escrita e reuso do código. Além disso, são detalhadas a confiabilidade do código, que exige verificação de tipos e tratamento de exceções, e o custo, que envolve a análise de impacto de recursos computacionais.

## Para lembrar

- **Legibilidade é a facilidade de leitura e a compreensão associada ao código, envolvendo a coerência nas instruções.**
- **Redigibilidade está relacionada à facilidade de escrita do código e envolve a ortogonalidade, a simplicidade da escrita e o suporte à abstração.**
- **O código deve ser confiável, o que inclui a verificação de tipos, o tratamento de exceções e o uso de ponteiros.**
- **O custo de um programa deve ser analisado em termos de impacto de recursos, considerando o treinamento, a compilação e a execução, especialmente em ambientes paralelizados.**
- **Ao escolher uma linguagem, deve-se considerar as atualizações (novas features/frameworks), o uso de inteligência artificial, a disponibilidade de ferramentas e a comunidade ativa.**

## O que esta nota responde

- Quais são as boas práticas e características que devem ser consideradas ao desenvolver um programa de software?
- Como a legibilidade e a redigibilidade influenciam a qualidade e a manutenção de um código?
- Quais aspectos técnicos (como tipos e exceções) garantem a confiabilidade e a eficiência de um algoritmo?

## Conceitos

**Legibilidade** · **Redigibilidade** · **Confiabilidade** · **Custo** · **Ortogonalidade** · **Modularização** · **Verificação de tipos** · **Tratamento de exceções**

## Conteúdo

`⏱ 00:00`

Muito bem, vamos para a nossa terceira etapa. O objetivo aqui é verificar as características de um programa.

Basta programar? Existe alguma boa prática relacionada à programação? Existem sim, importantes características a serem consideradas quando você cria um programa. Dentro da área de desenvolvimento de programa, temos algumas diretrizes que podemos levar em consideração na hora de codificar o nosso algoritmo.

As características são:
- Legibilidade
- Redigibilidade
- Confiabilidade
- Custo

Você deve ter um `código` que seja bem escrito, confiável, ou seja, que ele realmente execute o que ele se compromete a fazer, e que ele tenha um baixo custo.

### Legibilidade

Com relação à legibilidade, temos a facilidade de leitura e a compreensão associada. Isso envolve a ortografia, o que é a coerência nas instruções. O seu `código` deve ser coerente. A partir da legibilidade, também definimos quais são as estruturas mais adequadas para aquele contexto.

Legibilidade é o que é legível. Temos que carregar sempre essa ideia de um `código` legível.

### Redigibilidade

A redigibilidade está relacionada à facilidade de escrita do `código`. Ela pode conflitar um pouco com a legibilidade. O seu `código` tem que ser de fácil escrita, mas dependendo de como ele é escrito, ele pode estar sendo escrito facilmente, mas não ser muito legível.

A redigibilidade também envolve:
- A ortogonalidade.
- A simplicidade da escrita.
- O suporte à abstração.
- O reuso do `código`, seja através de modularização ou alguma outra técnica que você pode estar utilizando.

O seu `código` tem que ser expressivo. Ou seja, geralmente você pode estar utilizando um operador mais baixo, como incrementar o uso do `for`. É utilizar algumas técnicas, algumas instruções, estruturas que tornem seu `código` expressivo, para que você, ao bater o olho, entenda o que ele quer dizer.

### Confiabilidade

A confiabilidade já está relacionada ao que o seu `código` foi programado para fazer. Se o seu `código` se propõe a resolver uma determinada solução, por exemplo, ser uma calculadora, ele tem que operar como uma calculadora. Ele tem que ter as operações básicas de uma calculadora, pelo menos. Ele tem que ser confiável.

Para isso, dentro da confiabilidade, nós temos:
- A parte de verificação de tipos.
- O tratamento de exceções.
- A parte de uso de ponteiros.

A parte de uso de ponteiros é muito voltada para determinar ponteiro de ponteiro e existe ponteiro de ponteiro, três vezes ponteiro de ponteiro de ponteiro. Já nas linguagens mais de alto nível, isso torna-se um pouco mais transparente. Também consideramos a compatibilidade de compiladores. Há algumas questões que são consideradas dentro da confiabilidade.

### Custo

Já se trata da análise de impacto custo: como eu estou utilizando os meus recursos? Eu estou utilizando sabiamente? Eu estou deixando meu `código` eficiente para aquele cenário?

Nesse caso, você precisa verificar a parte de treinamento, para que eles possam escrever cada vez `código`s mais eficientes.

A parte de codificação tem que estar muito atenta. A compilação também é um processo de traduzir o `código` para trazer o programa fonte para um programa objetivo.

O projeto e a própria execução do programa também podem acarretar em alto custo, ou seja, alta utilização de poder computacional, e isso se refletirá no custo e na infraestrutura alimentar. Por exemplo, se eu vou criar um programa para um ambiente como o Santos Dumont, que é um supercomputador...

`⏱ 05:00`

Em um ambiente paralelizado, não é possível criar um programa como se estivesse utilizando um computador de maneira sequencial. Ele tem que ser otimizado, ele tem que ser direcionado para aquele contexto, aquele ambiente computacional, de forma que você otimize os recursos e não simplesmente gaste os recursos de maneira displicente.

### Características a Considerar na Linguagem

Outras características que devemos levar em consideração são:

- As atualizações: Surgiu uma nova *feature*, surgiu um novo *framework*, surgiu alguma coisa nova com relação à linguagem que você está utilizando.
- O uso de inteligência artificial atrelado à linguagem: `Python` tem muitas bibliotecas voltadas para esse mundo de *machine learning* e ciência de dados.
- Disponibilidade de ferramentas: É algo que você deve levar em consideração.
- Comunidade ativa: Muitas vezes você vai se deparar com erros e o `stack overflow` vai ser uma benção na sua vida.

### Mercado e Aplicabilidade

É importante verificar também como é a adoção para o mercado. Por exemplo, o `Java` sempre foi o mais utilizado e desbancou o `C` quando ele surgiu até hoje. Ano passado, se eu não me engano, o `Python` passou, ficou ali pau a pau, acho que passou um pouquinho.

O `Python` tem uma aplicabilidade muito específica para dados e ele é muito bom nisso. Exceto quando você vai para ambientes em que você precisa de performance, e via de regra ele é muito bom para isso.

Esses são outros quesitos que nós devemos levar em consideração.

Na nossa próxima etapa, iremos falar de como que o compilador analisa o nosso código.

## Relacionado

- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
- [[raciocinio-logico-inducao-deducao-e-abducao]]
- [[Processos de Software]]
- [[decomposicao-conceitos-estrategias-e-aplicacoes]]
