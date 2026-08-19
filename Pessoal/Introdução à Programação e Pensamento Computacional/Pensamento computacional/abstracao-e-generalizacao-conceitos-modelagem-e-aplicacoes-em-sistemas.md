---
titulo: "Abstração e Generalização: Conceitos, Modelagem e Aplicações em Sistemas"
tags: [pensamento-computacional, fundamentos, conceitos, dados, estudos]
data: 2026-08-19
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 9
conceitos: [Abstração, Generalização, Modelagem de dados, Tipos Abstratos de Dados (TAD), Arquitetura em camadas (OSI / TCP-IP), Reutilização de padrões]
---

# Abstração e Generalização: Conceitos, Modelagem e Aplicações em Sistemas

> [!resumo] Do que se trata
> A aula define o pilar da abstração como o processo intelectual de isolar características essenciais e descartar detalhes para generalizar problemas do mundo concreto para o abstrato. Apresenta aplicações práticas em modelagem de dados, estruturas de dados, algoritmos e arquiteturas em camadas na computação e redes. Conclui demonstrando como selecionar apenas as variáveis relevantes de um contexto para criar soluções genéricas e reutilizáveis.

## Para lembrar

- **Abstrair é o processo intelectual de isolamento de objetos da realidade, focando na essência e descartando detalhes irrelevantes para o contexto.**
- **Na lógica, a generalização consiste na operação intelectual de reunir um conjunto de seres ou fenômenos similares dentro de uma classe geral.**
- **Na computação, tipos abstratos de dados (como árvores, listas e grafos), linguagens de programação e máquinas de estados finitos são exemplos de abstrações.**
- **Arquiteturas de sistemas e redes, como os modelos em camadas OSI e TCP/IP e o modelo cliente-servidor, são construídos sobre abstrações.**
- **A generalização de um problema prático permite criar modelos reutilizáveis aplicáveis a outros cenários que apresentem o mesmo padrão estrutural.**

## O que esta nota responde

- O que é abstração e qual a sua relação direta com a generalização?
- Como a abstração é utilizada na modelagem de bases de dados?
- Quais são os principais exemplos de abstração aplicados a redes e arquitetura de computadores?

## Conceitos

**Abstração** · **Generalização** · **Modelagem de dados** · **Tipos Abstratos de Dados (TAD)** · **Arquitetura em camadas (OSI / TCP-IP)** · **Reutilização de padrões**

## Conteúdo

`⏱ 00:00`

Muito bem. Vamos falar sobre abstração.

Para entender o que é abstrair, você deve observar múltiplos elementos, avaliando suas características e propriedades separadamente. Dado um elemento, você precisa analisar suas características, ficar com a essência.

A abstração é um processo intelectual de isolamento de objetos da realidade. Abstrair é detectar características, e a abstração é extrapolar um objeto do mundo concreto para o mundo das ideias, isolado da realidade.

Generalizar é tornar algo mais amplo e extenso. Ou seja, nesse processo, precisamos pegar os elementos principais de um determinado objeto, extrapolá-lo para um mundo abstrato, de maneira que você o torne geral. Por isso, abstrair é generalizar.

### Generalização na Lógica

Generalizar, na lógica, é a operação intelectual que consiste em reunir, numa classe geral, um conjunto de seres ou fenômenos similares. Quando generalizamos, conseguimos determinar classes e objetos que compõem essas classes.

Por exemplo, eu tenho aqui algo nebuloso. Não sei o que é, mas a partir do momento em que começo a analisar suas características e tento extrapolá-lo para algo mais abstrato, mais geral, posso determinar se essas formas são triângulos, losangos ou círculos. Essa é a ideia.

Em um sentido clássico, classificar esses dados através de características que vêm de encontro à definição de abstrair: detectar os pontos essenciais e, então, generalizar em detrimento do detalhe.

### Aplicação Prática: Modelagem de Dados

Às vezes, um determinado objeto possui uma série de características, e muitas dessas características podem não interessar para o contexto que você precisa resolver.

Vou colocar um exemplo que vai facilitar esse entendimento. Para que possamos ter uma representação, vamos imaginar que preciso representar uma base de estudantes. Os estudantes têm uma série de características: nome, matrícula, endereço, campus, trabalho, se têm filho ou não, um programa preferido. Há uma série de informações associadas a eles.

No entanto, nem todas essas informações são relevantes para o meu problema, não são relevantes para o meu contexto. Eu preciso identificar os pontos essenciais e descartar os detalhes.

Para resolver minha base de dados e criar um modelo que possa representar os alunos de uma faculdade, eu só preciso levar em consideração essas características. Esses detalhes são fechados de lado.

### Abstração em Computação

A abstração é utilizada em diversas áreas do conhecimento, mas dentro da computação, podemos enumerar algumas questões:

*   **Algoritmos de pesquisa e ordenação:** Como `merge sort` ou uma busca binária.
*   **Algoritmo de clusterização:** Para tornar o processo mais rápido, onde você define *clusters* e cada *cluster* executa uma determinada tarefa. Se algum *cluster* cair, outros assumem. Esse é um exemplo.
*   **Estruturas de dados:** Como tipos abstratos de dados (TAD), como árvore, lista ou grafo. São estruturas que criamos, mas que abstraímos de tal maneira que não são palpáveis. Conseguimos programá-las e criá-las via codificação, mas elas são abstrações de algo mais específico.
*   **Máquinas de estado finito:** É também uma abstração.
*   **Linguagem de programação:** A própria linguagem de programação é uma abstração de algo concreto para o mundo abstrato.

`⏱ 05:20`

O conceito de abstração, em termos de comunicação, pode ser visto no `Broadcast`. A ideia é enviar uma mensagem para todos.

Um modelo que abstrai essa característica deve ser capaz de determinar como funciona uma comunicação síncrona ou assíncrona. Você não tem nada concreto ali; você está criando um modelo.

Existem estruturas, por exemplo, o paralelismo, onde os dados são distribuídos entre os *cores* ou *clusters* e depois reconstituídos em outro ponto.

### Abstrações em Redes e Sistemas

Conceitos baseados em abstrações são muito próximos da área de redes. Exemplos incluem:

- A parte de cliente e servidor, utilizada pelo protocolo `HTTP` e outros protocolos de comunicação.
- O conceito de estrutura em camadas, utilizado pelo modelo `OSI` e pelo `TCP/IP`, que são a base da internet.
- Uma arquitetura ponto a ponto.

As arquiteturas em si são abstrações. Em todos esses exemplos, podemos citar outros além disso.

### Abstração em Cenários Práticos

Para entender o que é uma abstração de forma mais palpável, vamos supor o seguinte cenário: eu preciso limpar meu terreno.

Eu preciso analisar o meu contexto, eu preciso classificar o meu terreno, eu preciso identificar quais são as plantas, se há árvore frutífera ou não. Mas, se o meu único objetivo é limpar o terreno, eu não preciso classificar. Eu preciso identificar as distâncias.

Eu identifico quais são as características do meu problema que vou utilizar. Nesse caso, não são os tipos de plantas existentes, mas sim as instâncias entre os pontos.

Se eu estivesse realizando uma poda, aí sim eu teria que levar em consideração a classificação das plantas, porque cada poda é diferente, com uma época do ano distinta, e por aí vai.

Uma vez que determino as instâncias, eu posso determinar o percurso. A partir desse percurso, eu executo a minha tarefa.

Você pode estender esse tipo de situação para outros cenários que sejam similares e que tenham o mesmo padrão.

A ideia é abstrair um conceito, generalizar algum problema e torná-lo reutilizável. É tornar ele geral de maneira que possa ser utilizado por cenários distintos, mas com similaridade entre si. Por exemplo, nesse caso, poderíamos atrelar ao problema de melhor caminho.

Na próxima aula, falaremos sobre algoritmos.

## Relacionado

- [[fundamentos-e-pilares-do-pensamento-computacional]]
- [[Diagramas de Caso de Uso]]
- [[05 - Modelos de Dados]]
- [[01 - Introdução ao Machine Learning]]
