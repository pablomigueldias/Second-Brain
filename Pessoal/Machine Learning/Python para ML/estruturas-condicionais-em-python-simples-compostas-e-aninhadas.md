---
titulo: "Estruturas Condicionais em Python: Simples, Compostas e Aninhadas"
tags: [estudo, conceitos, fundamentos, pensamento-computacional, linguagens-de-programacao, variaveis, operadores]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 17
conceitos: [Estrutura Condicional Simples, Estrutura Condicional Composta, Estrutura Condicional Aninhada, if, else, elif, Comparação de Valores]
---

# Estruturas Condicionais em Python: Simples, Compostas e Aninhadas

> [!resumo] Do que se trata
> A aula aborda o uso de estruturas condicionais em Python, começando pela estrutura simples, que utiliza `if` e `else` para tomar decisões baseadas em condições. Em seguida, são exploradas as estruturas compostas e aninhadas, que permitem a criação de lógica de programação mais complexa, como a utilização de `elif` para múltiplas verificações. Por fim, é mostrado como essas estruturas são fundamentais para a automação de processos, inclusive em sistemas de Inteligência Artificial.

## Para lembrar

- **Para verificar se dois valores são iguais, deve-se usar dois sinais de igual (`==`) na comparação.**
- **O símbolo de diferente em Python é representado por exclamação com sinal de igual (`!=`).**
- **São possíveis usar os símbolos de comparação: maior (>), menor (<), maior ou igual (>=) e menor ou igual (<=).**
- **Estruturas condicionais aninhadas são usadas quando uma condição é colocada dentro do bloco de outra condição, permitindo comparações mais complexas.**
- ⚠ **A estrutura condicional composta permite adicionar um `elif` (else if) para verificar múltiplas condições sequencialmente.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Como implementar uma lógica de decisão em Python?
- Qual a diferença entre usar `if` e `elif` em estruturas condicionais?
- Como aninhar ou encadear múltiplas condições em um programa?

## Conceitos

**Estrutura Condicional Simples** · **Estrutura Condicional Composta** · **Estrutura Condicional Aninhada** · **if** · **else** · **elif** · **Comparação de Valores**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e hoje vamos ver um conteúdo relacionado à parte básica do Python para programação, envolvendo estruturas condicionais.

As estruturas condicionais do Python são bem parecidas com as de outras linguagens, não há tanto segredo. O objetivo é fazer uma relação com o que já sabemos e ver alguns exemplos de estruturas condicionais.

A ideia é que a gente veja:

- Estrutura condicional composta;
- Estruturas condicionais simples;
- Estruturas condicionais aninhadas.

Vamos começar pela estrutura condicional simples.

### Estrutura Condicional Simples

Vou mostrar um exemplo. Vamos fazer um exemplo aqui. Vou colocar um `if`, que é a nossa condição. Vou dizer que se a minha soma for maior do que zero, eu vou `print` dizendo que essa soma é maior do que zero. Vou colocar um `else` e vou `print` caso seja o contrário, dizendo que é menor do que zero.

Aqui eu vou entrar com o meu valor para `soma`. Vou dizer que a minha `soma` é igual a 3. Vou executar. Tem um erro aqui na linha 5: faltaram os dois pontos e faltaram também no `else`. Vou executar de novo. Está me mostrando que a minha `soma` é maior do que zero. Por quê? Porque o valor que eu tenho aqui para a minha variável `soma` é igual a 3.

Agora, se a gente colocar o valor menos 1, o valor da minha `soma` é menor do que zero. A gente poderia colocar outra condição para caso o valor de entrada seja zero, por exemplo.

Este é o nosso primeiro exemplo de estrutura condicional simples.

Vou colocar uma outra condicional para que a gente consiga comparar um valor se ele é diferente do outro.

Vou colocar aqui `número1` é igual a `número2`. Eu criei duas variáveis e coloquei dois números diferentes para cada uma delas. Agora, vou comparar se esses números são iguais.

Eu vou comparar se o `número1` é igual ao `número2`. Note que faltou um sinal de igual; tem que colocar dois sinais de igual juntos (`==`) para que eu faça uma comparação desse tipo.

Com este `if`: `if número1 == número2:`, se sim, eu vou `print` dizendo que os valores são iguais. E vou dizer, caso contrário, com o `else`, eu vou dizer que os valores são diferentes.

Vou `print` aqui: "Os valores são diferentes". Faltaram os dois pontos aqui. Vou executar. Como o meu `número1` vale 2 e a minha variável `número2` vale 3, os valores são diferentes.

Agora, se eu colocar o `número2` valendo também 2, eu vou para o caso do `if`, e eu vou `print`: "Os valores são iguais". Eu não vou cair no `else`. Igual a essa vez aqui. Então, os valores são iguais.

Quais os comandos que a gente pode usar?

A gente pode usar também o símbolo de diferente. A gente pode usar este aqui: exclamação com sinal de igual (`!=`). Minha comparação é a seguinte: `número1` é diferente do `número2`?

Eu estou fazendo uma nova comparação. Vou colocar aqui: "Os valores são...".

`⏱ 06:40`

... os valores são iguais. Inverteu. Vou executar. Se o número 1 é diferente do número 2, vai cair no meu `else`. Os valores são iguais, bom? Esse é o nosso símbolo de diferente para essa condicional.

Existem também os símbolos de maior, menor, maior ou igual, e menor ou igual. Podemos usar, por exemplo, `número 1 é menor do que o número 2` ou `número 1 é maior ou igual ao número 2`. Também podemos usar o símbolo `número 1 é menor ou igual ao número 2`, bom?

Essas são as nossas condicionais para o caso de uma situação simples.

### Estruturas Condicionais

Também temos as estruturas condicionais compostas, onde vamos entrar com duas situações.

1.  **Estrutura Condicional Simples:** Tenho apenas um `if` e basicamente só tenho a resposta para esse `if`. Exemplo: `número 1 é menor ou igual que o número 2`, aí eu `printo` "sim". Isso seria uma estrutura condicional simples.
2.  **Estrutura Condicional Composta:** Se fizermos o que fizemos aqui, onde eu tenho um `else` para uma outra condição, já temos uma estrutura condicional composta.
3.  **Estruturas Condicionais Aninhadas:** Podemos colocar uma outra condição aninhada dentro do meu caso.

A gente pode fazer mais ou menos assim: estrutura condicional aninhada.

### Condicionais e Inteligência Artificial

Vai ter condições que vão acontecer dessa forma. A gente brinca muito na área de inteligência artificial. Quando alguém desenvolve uma IA, e não tem nada de IA, a gente fala: "Sua IA é um conjunto de `if`", porque é uma estrutura aninhada que compara várias situações e vai entrando dentro de vários `if`s.

Isso acontece de uma forma que conseguimos realizar uma automação de um processo, porém, não tem nada de IA. A gente até brinca muito com aquele robô Sofia, dizendo: "Ah, não tem uma IA ali, igual eles estão querendo vender. É simplesmente um monte de `if` para que ela funcione daquela forma."

É basicamente isso: a inteligência artificial que temos atualmente. As IAs que temos de forma restrita são algoritmos que trabalham com várias condições de forma aninhada. Não temos nada de outro mundo ainda para o cenário de inteligência artificial.

Para dar um exemplo de uma situação onde temos uma estrutura condicional aninhada com vários tipos de `if`s, a inteligência artificial trabalha muito com esse cenário.

Vamos fazer aqui agora uma comparação, por exemplo:

```python
if soma > 0:
    # Código para soma maior que zero
    pass
elif soma == 0:
    # Código para soma igual a zero
    print("Minha soma é igual a...")
else:
    # Código para soma menor que zero
    print("Minha soma é menor do que zero")
```

Vou executar aqui. Tem alguns errinhos. Vou executar. Está faltando a chamada também da minha variável. Então, vou colocar aqui que `soma` é igual a 1. Vou executar. Está dando erro na linha 7. Deixa eu ver aqui. Bom, linha 7: `soma` igual a 0. Tem algum erro aqui que eu não estou enxergando? Um minutinho.

`⏱ 13:00`

Se `soma` é igual a zero, se é maior que zero, printa essa função. (A linha 7 está faltando um sinal de igual). Aqui eu tenho que `soma` é igual a 1. Eu atribuí o valor 1 à minha variável `soma`. Em qual condição eu vou cair? Que a minha `soma` é maior do que zero? Se eu colocar o valor zero aqui para a variável `soma`, eu tenho que `soma` é igual a zero. E se eu colocar um valor negativo, a minha `soma` é menor do que zero. Aqui a gente tem uma estrutura alinhada.

### Aplicação da Estrutura Condicional

Usamos muito essa estrutura condicional alinhada para modelos de inteligência artificial, onde temos várias situações que devem ser interpretadas para que reconheçamos um determinado comportamento.

Por exemplo, na interpretação de linguagem natural, quando damos um comando de voz, temos um `case` para cada tipo de fala. Quando você diz "ok", quando você diz "sim", "não", o sistema cai dentro de uma condição. Ele executa alguma saída de acordo com o que foi lido na entrada, no caso, no `if`.

Por exemplo:
*   `if` não, a gente vai realizar uma função.
*   `if` sim, a gente vai realizar outra função.

E usamos também o `else` para fazer a condição oposta em alguns casos.

### Tipos de Estruturas Condicionais

Neste conteúdo, vimos:

- Estrutura condicional simples, onde basicamente vou ter um `if` com uma resposta para essa condição.
- Estrutura condicional composta, onde temos mais de uma condição.
- Estrutura condicional alinhada, onde começamos a pendurar várias condicionais dentro de um mesmo problema.

É muito importante ter essa ideia de condicional ao modelar nossos algoritmos, pois vamos usar bastante, principalmente nas estruturas de treinamento. Por exemplo, para ter uma condição que termina depois de uma quantidade de épocas, ou porque termina depois de um valor de acurácia pré-definido.

Essas estruturas ajudarão no desenvolvimento de projetos. No nosso próximo conteúdo, veremos a parte de algoritmos com estruturas de repetição.

Por agora, é isso.

## Relacionado

- [[estruturas-condicionais-e-operadores-logicos-em-algoritmos]]
- [[estruturas-de-repeticao-em-algoritmos-tipos-funcionamento-e-aplicacoes]]
- [[tipos-de-dados-em-python-inteiros-flutuantes-complexos-strings-e-booleanos]]
- [[pratica-de-algoritmos-em-portugol-soma-de-intervalo-media-e-reutilizacao-de-func]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Um abraço e até a próxima.

</details>
