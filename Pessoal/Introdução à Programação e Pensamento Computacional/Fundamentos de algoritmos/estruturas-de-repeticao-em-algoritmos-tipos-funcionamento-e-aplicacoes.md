---
titulo: "Estruturas de Repetição em Algoritmos: Tipos, Funcionamento e Aplicações"
tags: [algoritmos, fundamentos, pensamento-computacional, conceitos, estudo]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 8
conceitos: [estruturas de repetição, loop infinito, condição de parada, laço enquanto (while), laço repita até (repeat-until), laço para (for), aninhamento de estruturas]
---

# Estruturas de Repetição em Algoritmos: Tipos, Funcionamento e Aplicações

> [!resumo] Do que se trata
> Apresenta o conceito, a finalidade e as vantagens das estruturas de repetição no controle de fluxo de algoritmos. Explica as diferenças práticas entre os laços com teste no início, com teste no final e com número fixo de iterações. Demonstra a possibilidade de aninhar estruturas de repetição com estruturas condicionais.

## Para lembrar

- **Toda estrutura de repetição exige uma condição de parada (por contagem prefixada ou condição satisfeita) para evitar loops infinitos.**
- **O uso de laços reduz a quantidade de linhas de código, melhora a compreensão e diminui a ocorrência de erros e inconsistências em relação à duplicação manual de instruções.**
- **Na estrutura 'enquanto' (while), o teste lógico é realizado no início antes do bloco; na estrutura 'repita até' (repeat-until), o teste ocorre ao final, garantindo que o bloco seja executado ao menos uma vez.**
- **A estrutura 'para' (for) possui teste no início e opera com um intervalo (range) definido, sendo utilizada quando o número exato de repetições é previamente conhecido.**

## O que esta nota responde

- Qual é a diferença de funcionamento entre as estruturas enquanto, repita até e para?
- Por que é obrigatório definir uma condição de parada em uma estrutura de repetição?
- Como funciona a combinação de estruturas de repetição com estruturas condicionais em um algoritmo?

## Conceitos

**estruturas de repetição** · **loop infinito** · **condição de parada** · **laço enquanto (while)** · **laço repita até (repeat-until)** · **laço para (for)** · **aninhamento de estruturas**

## Conteúdo

`⏱ 00:00`

Vamos falar das estruturas de repetição.

Dado que eu preciso que um pedaço do meu código seja executado mais de uma vez, com diferentes parâmetros — por exemplo, diferentes valores dentro das suas variáveis —, eu preciso fazer uma repetição.

Nesse contexto, temos um laço, que é um controle de fluxo, uma malha de repetição, um `loop`. Esses são sinônimos, palavras com o mesmo sentido. Uma estrutura de repetição irá executar um determinado trecho de um programa a partir de certos parâmetros que estão estabelecidos dentro dessa estrutura.

#### Funcionamento e Vantagens das Estruturas de Repetição

Toda estrutura de repetição exige uma condição de parada. Caso contrário, nós entraríamos em um `loop` infinito.

A condição de parada pode variar:

*   Pode ser a partir de um número de repetições pré-fixado.
*   Pode ser por uma condição a ser satisfeita.

Você pode estar pensando: "Não é só repetir meu código?". Não. Existem nuances relacionadas.

Qual é a vantagem de utilizar uma estrutura de repetição, especialmente para quem está começando?

1.  **Redução de linhas:** Imagine que você precisa fazer algo várias vezes e pensa em usar `Ctrl + C`, `Ctrl + V`, `Ctrl + C`, `Ctrl + V`... E se você quiser fazer alguma modificação? Você terá que modificar tudo.
2.  **Redução de erro e inconsistência:** A sua compreensão será prejudicada porque você terá informação demais. Seu código ficará muito poluído e você não conseguirá entender facilmente.

Ao utilizar essas estruturas de repetição, você garante a redução de linhas, uma melhor compreensão e uma redução de erros.

#### Tipos de Estruturas de Repetição

De fato, existe mais de uma. Alguns exemplos são:

*   `enquanto` (While)
*   `faça/enquanto` (Do-While)
*   `repita até` (Repeat-Until)
*   `para` (For)
*   `dê até faça` (Do-While/For-Do)

#### Exemplos Práticos

Para exemplificar, vamos usar exemplos do nosso dia a dia, bem tranquilos e fáceis de entender.

**Exemplo 1: O Cortador de Grama (Estrutura `Enquanto`)**

Vamos supor um trabalhador que tem uma casa e precisa cortar o jardim. Ele vai fazer o seguinte:

Ele tem um teste lógico no início. Enquanto houver grama, ele corta a grama.

Ele terá um número de repetições, mas não sabe quantas vezes terá que passar o cortador para que toda a grama seja efetivamente cortada.

A instrução que será repetida é: "Enquanto a grama estiver alta, cortar a grama."

A condição de parada é analisando a grama: "A minha grama foi completamente cortada?"

1.  Se não, ele continua no `loop`: `enquanto grama alta, cortar grama`.
2.  Como seria isso em código? A variável `grama` começa como `false`.
3.  `enquanto grama == false` (ou seja, estamos fazendo uma comparação, não uma atribuição):
    *   Faça a instrução de cortar grama.
    *   Atualiza `grama`.
4.  Quando eu perceber nesse meu `loop` que a grama foi totalmente cortada, eu vou atualizar a variável `grama` para `true`. A partir dessa atualização, vai acionar a minha condição de parada e eu saio do meu `loop` do `enquanto`.

**Exemplo 2: Leitura de um Livro (Comparação de Teste Lógico)**

Agora vamos supor uma estrutura de repetição para leitura de um livro. Eu estou procurando determinado artigo dentro de uma revista ou de um livro e preciso estar virando as páginas.

*   **Se o teste lógico é no final:** Usamos `repita até`.
*   **Se o teste lógico é no início:** Usamos `enquanto`.

Lembre-se:

`enquanto grama == false, faça` (O teste é feito antes de entrar no bloco).

`⏱ 05:00`

O `repita` (repeat): o meu teste lógico ocorre ao final. Eu sei que vou executar essa instrução ao menos uma vez. Por exemplo: Repita até encontrar o artigo. Procura o artigo, vira a página, analisa o conteúdo. Encontrou o artigo? Não. Continua. O número de repetições para este caso também é indefinido.

Temos também o `for`. O `for` de D até. O teste é no início e o número de repetições é bem definido, ao contrário dos outros dois. Sei que vou, por exemplo, do 1 até um determinado valor, e esse `range` vai determinar o número de repetições dentro do meu loop. Vai determinar quantas vezes a minha instrução vai se repetir.

Exemplo: `somatório` é igual a zero. Para início de 1 até 10, eu tenho: `somatório` é igual a `somatório` mais `início`, e escrevo a `somatório`. Esses dois trechos de código são as instruções que vão ser repetidas a cada loop, a cada volta que o `for` der.

É possível mesclar as estruturas, utilizar uma dentro da outra? Certamente. Posso utilizar o seguinte: Um `while` (enquanto condição) pode utilizar uma estrutura condicional dentro de uma estrutura de repetição, ou vice-versa. Enquanto uma determinada condição ocorrer, vou executar o que está dentro. Nesse caso, temos uma estrutura condicional de `se` condição 2, executa as instruções, `fim C`. E uma vez que a condição principal do `while` tenha sido satisfeita, encerro o meu loop.

### Próximo Assunto: Vetores e Matrizes

Agora, o nosso próximo assunto é sobre vetores e matrizes. Já falamos sobre as estruturas de repetição que existem, as estruturas de repetição, as de condição também, e dá para já ter uma noção do que e quando utilizar cada uma. O próximo assunto é vetores e matrizes.

## Relacionado

- [[estruturas-condicionais-e-operadores-logicos-em-algoritmos]]
- [[operadores-variaveis-e-estruturas-de-controle-em-algoritmos]]
- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
- [[decomposicao-conceitos-estrategias-e-aplicacoes]]
