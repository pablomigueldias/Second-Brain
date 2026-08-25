---
titulo: "Operadores Lógicos e Comparação de Dados em R"
tags: [operadores, linguagens-de-programacao, machine-learning, fundamentos, variaveis, estudo]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 8
conceitos: [Operadores de comparação, Operadores lógicos, Valores booleanos, Comparação de strings, Estrutura de dados em R, Atribuição de variáveis]
---

# Operadores Lógicos e Comparação de Dados em R

> [!resumo] Do que se trata
> Apresenta o funcionamento dos operadores de comparação e relacionais na linguagem R, como igualdade, diferença e desigualdades. Demonstra a execução prática de testes lógicos com variáveis numéricas que retornam valores booleanos. Explica como realizar comparações entre caracteres e strings para verificação e busca de registros.

## Para lembrar

- **Os operadores relacionais em R incluem menor que (<), maior que (>), igual (== ), diferente (!=), maior ou igual (>=) e menor ou igual (<=) .**
- **As comparações lógicas em R avaliam expressões e retornam valores booleanos (TRUE ou FALSE) de forma automática.**
- ⚠ **A comparação de igualdade funciona tanto com números quanto com caracteres únicos ou strings completas.**
- ⚠ **A comparação de strings permite verificar a correspondência de valores em operações de busca e iteração sobre conjuntos de dados.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Quais são os operadores de comparação utilizados na linguagem R?
- Como funciona a comparação de caracteres e strings em R?
- Que tipo de resposta a linguagem R retorna ao avaliar expressões relacionais?

## Conceitos

**Operadores de comparação** · **Operadores lógicos** · **Valores booleanos** · **Comparação de strings** · **Estrutura de dados em R** · **Atribuição de variáveis**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e agora vamos ver um conteúdo relacionado aos operadores lógicos para R.

Quem já trabalhou com linguagens como C, Python, SciLab ou MATLAB, já vai ficar bem tranquilo com essa questão, porque é bem parecido o que temos aqui. No entanto, vocês vão ver que as respostas são mais intuitivas.

### Operadores Lógicos

Os operadores lógicos que temos aqui serão deixados comentados para não serem interpretados pela linguagem.

Os operadores de comparação que temos são:

*   `x` é menor do que `y`
*   `x` é maior que `y`
*   `x` é igual a `y`
*   `x` é diferente de `y`
*   Maior ou igual a (`>=`)
*   Menor ou igual a (`<=`)

Não é obrigatório dar um espaço entre o operador lógico, mas fazemos isso para deixar o código mais legível.

### Demonstração de Comparação Numérica

Vou colocar aqui a atribuição. Vocês estão vendo que eu coloquei os meus exemplos aqui, tudo em maiúsculo. Vou continuar assim.

Vou definir que `x` vale 10 e `y` vale 20. Agora vou perguntar se `x` é menor do que `y` e vou rodar no meu programa. Ele me retornou a resposta `true`. Ou seja, é verdadeiro que `x` é menor do que `y`.

Se eu mudar, colocando `x` é maior do que `y`, a gente também terá a resposta de forma automática. Nesse caso, o resultado é `false`.

Eu posso também fazer comparações de se é diferente, se é igual, maior ou menor ou igual. Isso é tranquilo.

### Comparando Strings

Vou mostrar para vocês como comparar uma string. A gente também consegue fazer isso.

Vamos imaginar que vamos criar dois objetos em R que armazenam a primeira letra do seu primeiro nome e as primeiras letras dos seus dois nomes.

No meu caso, meu nome é Diego Renan Bruno. Vou armazenar a letra D, que é de Diego, e a letra R, que é de Renan. E aí vou comparar esses valores.

Como seria isso aqui? Vou colocar uma variável, um objeto resumido, que será a primeira letra do primeiro nome. E a outra que vou criar será a primeira letra do segundo nome.

Vou atribuir: a minha primeira letra do primeiro nome é `D`, e a do segundo nome é `R`.

Agora vou fazer uma comparação: vou comparar se a primeira letra é igual à segunda.

Vou comparar esse objeto e vou ver se é igual ao meu segundo objeto.

Vou reproduzir isso aqui. O resultado retornou `false`. Por quê? A primeira letra do meu nome é Diego, então é `D`, e a segunda, o segundo nome, a primeira letra é `R`.

`⏱ 06:00`

### Comparação de Caracteres e Strings

É `R`, não é igual. Se eu colocar `D` aqui também, supondo que meu segundo nome também começa com a letra `D`, vai retornar verdadeiro, porque tenho a mesma letra. 

A gente consegue também comparar uma string. Vamos supor que eu coloco aqui `Diego` e aqui eu coloco `Renan`: eu consigo fazer essa comparação.

Se a gente imaginar que estamos percorrendo um conjunto de valores e eu preciso encontrar a minha resposta, eu consigo percorrer uma lista, encontrar a variável que estou buscando, compará-la e dizer se encontrei ou não, se a variável que encontrei tem o mesmo registro ou não. Seria mais dentro desse cenário.

### Operadores Lógicos

Os operadores lógicos são bem tranquilos, como a gente viu aqui. Espero que tenha sido tranquilo para vocês. A gente vai usar um pouco mais disso nas outras aulas de `R`.

## Relacionado

- [[estruturas-de-controle-e-operadores-em-scilab]]
- [[estruturas-condicionais-e-operadores-logicos-em-algoritmos]]
- [[linguagem-r-ambiente-replit-operadores-aritmeticos-e-escopo-em-machine-learning]]
- [[instalacao-operacoes-basicas-e-estruturas-de-programacao-no-scilab]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Então é isso, Até a próxima e muito obrigado!

</details>
