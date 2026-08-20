---
titulo: "Aplicação do Pensamento Computacional: Jogo de Adivinhação e Algoritmo de Busca Binária"
tags: [pensamento-computacional, caso-pratico, fundamentos, otimizacao, estudo]
data: 2026-08-19
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 5
conceitos: [Busca binária, Busca por varredura, Vetor ordenado, Espaço de busca, Pensamento computacional, Otimização de algoritmos]
---

# Aplicação do Pensamento Computacional: Jogo de Adivinhação e Algoritmo de Busca Binária

> [!resumo] Do que se trata
> Apresenta o estudo de caso do jogo de adivinhar um número para demonstrar a eficiência da estratégia de divisão do espaço de busca. Detalha o passo a passo do algoritmo de busca binária, destacando a obrigatoriedade de trabalhar com dados previamente ordenados. Explora como aprimorar e internalizar o pensamento computacional por meio da explicação do próprio raciocínio e do debate sobre otimizações.

## Para lembrar

- **A delimitação sucessiva do espaço de busca reduz o número de tentativas e é muito mais eficiente do que a busca linear por varredura.**
- **O passo a passo da busca binária calcula o elemento central dividindo o tamanho do vetor por dois, compara com o valor alvo e repete o processo até encontrar o resultado.**
- **O pensamento computacional é aprimorado quando o indivíduo explica seu processo de tomada de decisão e reflete sobre melhorias e otimizações para a solução.**
- **A busca binária exige obrigatoriamente que a lista, vetor ou sequência esteja previamente ordenada para funcionar.**


## O que esta nota responde

- Qual é o pré-requisito indispensável para a execução de uma busca binária em um vetor?
- Quais são os passos fundamentais do algoritmo de busca binária?
- Como a prática de explicar o próprio raciocínio ajuda a exercitar o pensamento computacional?

## Conceitos

**Busca binária** · **Busca por varredura** · **Vetor ordenado** · **Espaço de busca** · **Pensamento computacional** · **Otimização de algoritmos**

## Conteúdo

`⏱ 00:00`

Vamos fazer um último estudo de caso: adivinhar o número.

Vamos supor que eu tenho um valor que escolhi e preciso adivinhar o número dessa pessoa. A pessoa me responderá com perguntas de sim ou não, e eu preciso encontrar o número escolhido da melhor maneira.

Por exemplo, considerar o número 1, 2, 3 é uma possível solução, mas é uma maneira muito ineficiente de abordar o problema e há um desperdício de tempo absurdo.

Vamos pensar um pouco mais. Lembre que falamos de busca binária. A ideia vai nesse sentido.

A pessoa vai responder sim ou não, correto? Não há um limite para o número de perguntas que eu possa fazer. Mesmo que seja até o infinito, em uma hora eu vou encontrar o número com o menor número de tentativas se comparado com o primeiro caso.

Vamos supor que eu pergunte: "O número é maior do que 50?" A resposta é "Não". Então, o número está abaixo de 50. Já consegui delimitar. Em seguida, eu pergunto: "O número é menor que 20?" A resposta é "Sim". Opa, o número é menor que 20, então ele está entre 1 e 20.

Eu continuo nesse mesmo sentido, nesse mesmo raciocínio, até encontrar o número. Isso vai de encontro ao raciocínio da busca binária, que é a maneira mais eficiente de fazer uma busca do que uma busca por varredura.

### Algoritmo da Busca Binária

A busca binária é exatamente essa questão de adivinhar o número.

Qual seria o algoritmo? Qual seria o passo a passo?

1.  **Ordenar o Vetor:** Eu ordeno meu vetor se ele não estiver ordenado. Não é possível fazer a busca binária sem um vetor ordenado, sem uma lista ordenada ou uma sequência ordenada.
2.  **Identificar o Módulo:** Eu identifico o módulo de `L`, onde `L` é o tamanho do meu vetor, dividido por 2. Se o meu vetor for ímpar, eu vou encontrar um resultado quebrado, então eu tiro o módulo.
3.  **Acessar a Posição:** Eu acesso a estrutura naquela posição em que encontrei pela operação de `L dividido por 2` ou o módulo de `L/2`.
4.  **Comparar Valores:** Eu comparo os valores daquela posição com o meu valor alvo. É o que eu quero? Não.
5.  **Repetir:** Eu repito o processo até encontrar o número alvo, o número que eu quero encontrar dentro daquela estrutura.
6.  **Resultado:** Quando eu encontrar, eu imprimo: "Bem-sucedido".

Acho que é isso.

### Aprimorando o Pensamento Computacional

Só um adendo, para conversarmos um pouco. Como a gente aprimora essa habilidade? Como podemos exercitar cada vez mais e tornar esse tipo de pensamento algo mais internalizado?

O pensamento computacional exige que você se permita — ou que o professor permita — que os alunos expliquem as suas decisões e o seu processo de desenvolvimento. O que ele pensou? Qual foi o raciocínio dele até ele chegar naquela resolução?

Você começa a pensar sobre o problema: "Olha, mas de repente eu não poderia fazer assim? O que eu poderia melhorar?". Eles começam a debater sobre aquele assunto, e isso vai criando, vai fundamentando, vai criando fundações dentro do seu cérebro em que você consegue entender e otimizar as suas decisões.

Essa é uma maneira ótima de você estar treinando o seu pensamento computacional.

E terminamos a etapa de pensamento computacional. Vamos agora para a introdução.

`⏱ 04:40`

à lógica de programação.

## Relacionado

- [[fundamentos-e-pilares-do-pensamento-computacional]]
- [[aplicacao-do-pensamento-computacional-soma-de-intervalos-e-construcao-de-algori]]
- [[logica-proposicional-2-conectivos-parte-1]]
- [[01 - Introdução à Busca e Otimização]]
