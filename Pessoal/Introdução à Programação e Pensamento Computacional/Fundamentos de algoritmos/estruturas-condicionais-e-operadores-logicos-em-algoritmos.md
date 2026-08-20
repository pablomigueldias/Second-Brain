---
titulo: "Estruturas Condicionais e Operadores Lógicos em Algoritmos"
tags: [operadores, algoritmos, pensamento-computacional, raciocinio-logico, conectivos, variaveis, logica-proposicional]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 8
conceitos: [Estrutura Condicional, Condicional Simples, Condicional Composta, Condicional Encadeada, Operadores Relacionais, Operador Lógico E (AND), Operador Lógico OU (OR), Operador Lógico NÃO (NOT)]
---

# Estruturas Condicionais e Operadores Lógicos em Algoritmos

> [!resumo] Do que se trata
> A aula aborda a implementação de estruturas condicionais em algoritmos, detalhando os tipos simples, compostos e encadeados. Em seguida, são introduzidos os operadores lógicos (AND, OR, NOT), que são fundamentais para a álgebra booleana e para a construção de verificações complexas em programação.

## Para lembrar

- **Estrutura Condicional: É um conceito que expressa uma condição ou uma suposição, contendo ou implicando em uma hipótese que, se satisfeita, executa uma determinada instrução.**
- **Estrutura Composta: Possui uma verificação em relação à exceção, permitindo que, se a condição não for satisfeita, seja executada uma série de instruções alternativa (o 'SENÃO' ou 'ELSE').**
- **Estrutura Encadeada: É uma sucessão de condicionais, seguindo o padrão 'SE... SENÃO SE...' para verificar múltiplas condições em ordem.**
- **Operador Lógico E (AND): Retorna 'Verdadeiro' somente quando todas as entradas conectadas são satisfeitas; caso contrário, retorna 'Falso'.**
- **Operador Lógico OU (OR): Retorna 'Verdadeiro' se pelo menos uma das condições conectadas for verdadeira; só retorna 'Falso' se todas forem falsas.**

## O que esta nota responde

- Como eu verifico se um aluno foi reprovado ou aprovado em um algoritmo?
- Qual a diferença entre uma estrutura condicional simples, composta e encadeada?
- Quando devo usar os operadores lógicos AND, OR e NOT em um algoritmo?

## Conceitos

**Estrutura Condicional** · **Condicional Simples** · **Condicional Composta** · **Condicional Encadeada** · **Operadores Relacionais** · **Operador Lógico E (AND)** · **Operador Lógico OU (OR)** · **Operador Lógico NÃO (NOT)**

## Conteúdo

`⏱ 00:00`

Muito bem. Voltando ao nosso exemplo anterior, se quisermos colocar algum tipo de verificação para saber se o aluno foi reprovado ou não, precisamos introduzir um novo conceito: a estrutura condicional.

Dado o estado de uma pessoa ou de uma coisa, existe uma condição para que algo aconteça. O condicional expressa uma condição ou uma suposição; ele contém ou implica em uma suposição ou em uma hipótese. Há uma condição que, se satisfeita, executa uma determinada instrução.

Qual é a ideia de uma estrutura condicional? Dado uma condição que foi satisfeita, eu executo uma determinada operação. Se essa operação for satisfeita, ela é executada. Ou seja, a condição sendo satisfeita, a operação é executada. Caso isso seja uma inverdade e a condição não seja satisfeita, acarreta em uma exceção.

Podemos perceber que existem diferentes estruturas condicionais:

- **Estrutura Simples:** Apenas verifica se a condição foi satisfeita.
- **Estrutura Composta:** Possui uma verificação em relação à exceção. Se a condição não for satisfeita, é jogada uma exceção.
- **Estrutura Encadeada:** É um `se... senão` dentro de outro. É uma sucessão de estruturas condicionais.

### Operadores Relacionais

Quais são os operadores relacionais que nos ajudam a definir estruturas de condição dentro de um algoritmo?

Temos:

- Igual (`=`)
- Diferente (`!=`)
- Maior que (`>`)
- Menor que (`<`)
- Maior ou igual (`>=`)
- Menor ou igual (`<=`)

Todos esses operadores são utilizados em diferentes estruturas condicionais, para que elas possam verificar uma determinada afirmação. Se ela for satisfeita, ou seja, se aquela condição for verdadeira, ele executa a ação.

### Exemplos de Estruturas Condicionais

#### Condicional Simples

Um condicional simples seria algo mais similar a isto:

`A` e `B` (que será o somatório) e `X` recebe. Se `X` for maior que 10, então coloco aqui sim, imprimo `X` e saio.

Neste caso, conseguiríamos ver isso em uma estrutura mais próxima do pseudocódigo:

```
SE condição_verdadeira, ENTÃO instrução_para_condição_verdadeira
FIM SE
```

E aqui seria o algoritmo relacionado ao fluxograma que acabamos de explicar.

#### Condicional Composta

Como seria, no caso, uma condicional composta?

Dado uma condição, se ela não for satisfeita, temos um `SENÃO` (ou `ELSE`), onde jogamos uma exceção.

Por exemplo: `A` mais `B` é recebido por `X`.

`X` é maior ou igual a 10?
*   **Sim:** Então eu faço `X` mais...
*   **Caso contrário:** `X` menos 7.

Vemos aqui a ideia composta, que acaba sendo uma exceção dentro da outra. O que estamos olhando é:

`SE` condição acontece, `ENTÃO` eu executo uma série de instruções. `SENÃO` eu executo outra série de instruções para uma condição falsa. E aí sim, termino o meu estrutura condicional.

#### Condicional Encadeada

Vamos lembrar da média escolar. Ela está próxima da estrutura de condição `SE... SENÃO`. Portanto, ela é uma condicional composta.

Já o condicional encadeado é um `SE... SENÃO SE...` sucessivo.

Ele continua essa sucessão de condicionais. Se `condição 1`, então instruções para a condição. Se não, ele verifica a `condição 2`, e aí se for verdadeira, executa. Caso contrário, executa as instruções para `condição 1` e `condição 2`, que são falsas.

Exemplo: A gente lê `A` e `B`, faz o somatório, e:

Se `X` for menor ou igual a 10, eu faço `X` é igual a `X` menos 7.
Caso contrário, eu faço `X` igual a `X` mais 5.

E aí nós temos os operadores lógicos.

`⏱ 05:40`

A álgebra booleana envolve os operadores `AND`, `OR` e `NOT`. Eles são bem intuitivos e fáceis de entender.

Quando utilizar esses operadores? Você precisa de uma resposta simplificada, como verdadeiro ou falso. Por meio dessa estrutura condicional, acabamos substituindo por um encadeamento de condições.

### Operador Lógico E (`AND`)

O operador lógico `E` verifica as entradas que devem ser satisfeitas. Ele retorna:

*   `Falso` se for um ou outro.
*   `Verdadeiro` quando os dois são satisfeitos.

*(Nota: A parte de inserção é se gramática e conversação, então escreva provado se não se provar.)*

### Operador Lógico OU (`OR`)

Qual é o sentido aqui? Se uma condição é verdadeira ou a outra condição é verdadeira, o resultado é verdadeiro.

Ou seja, eu preciso apenas que uma condição seja verdadeira. Se ambas forem falsas, o resultado é falso.

É interessante notar que o `OR` está associado à união. Na verdade, o `OR` é da união. O `AND` é interseção.

**Exemplo:**
Se choveu ou a grama está molhada, então escreva "plantas regadas". Caso contrário, regar...

A partir da união desses dois conjuntos, eu já tenho um cenário que posso estar analisando.

### Operador Lógico NÃO (`NOT`)

O `NOT` é um operador lógico, um operador de negação, onde a inversão do resultado lógico é o resultado dessa operação.

*   Se eu tenho uma condição que é verdadeira, ela se torna falsa.
*   Se ela é falsa, torna-se verdadeira.

Esse operador de negação também pode ser utilizado da seguinte forma: `A - B`.

Tudo que não está em `B`, ou seja, tudo que está em `A` e não pertence a `B`. É essa a ideia do operador lógico de negação.

## Relacionado

- [[operadores-variaveis-e-estruturas-de-controle-em-algoritmos]]
- [[logica-proposicional-3-conectivos-parte-2]]
- [[10 - AutoML e Tuning de Modelos]]
- [[tecnicas-de-logica-de-programacao-linear-estruturada-e-modular]]
