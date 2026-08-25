---
titulo: "Linguagem R: Objetos, Atribuição, Case Sensitivity e Constantes Internas"
tags: [linguagens-de-programacao, machine-learning, variaveis, conceitos, estudo]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 17
conceitos: [Linguagem interpretada, Objetos em R, Operador de atribuição (<-), Case sensitivity, Comentários de código, Constantes internas]
---

# Linguagem R: Objetos, Atribuição, Case Sensitivity e Constantes Internas

> [!resumo] Do que se trata
> Apresenta os fundamentos de execução e sintaxe da linguagem R, destacando que ela é interpretada e trata tudo como objetos. Demonstra a atribuição de valores pelo operador `<-`, manipulação de variáveis, case sensitivity e uso de comentários com `#`. Explora a resolução de um cálculo de volume físico e exemplifica o uso de constantes e variáveis internas como `pi`, `letters` e `month.name`.

## Para lembrar

- **A linguagem R é interpretada e estrutura todos os seus elementos e dados na forma de objetos.**
- **A atribuição de valores a objetos em R é realizada com o operador `<-`.**
- **R é uma linguagem sensível a maiúsculas e minúsculas (case-sensitive), tratando `casa` e `CASA` como identificadores distintos.**
- **A linguagem R possui constantes e estruturas internas pré-definidas na biblioteca base, tais como `pi`, `letters` e `month.name`.**
- ⚠ **Comentários de código em R são demarcados pelo caractere `#`, ignorando qualquer instrução subsequente na linha.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Como funciona o operador de atribuição e a manipulação de objetos na linguagem R?
- Como a diferenciação entre maiúsculas e minúsculas (case sensitivity) impacta a declaração de variáveis em R?
- Quais são algumas das constantes e coleções pré-definidas internamente disponíveis no R básico?

## Conceitos

**Linguagem interpretada** · **Objetos em R** · **Operador de atribuição (<-)** · **Case sensitivity** · **Comentários de código** · **Constantes internas**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e agora vamos começar um conteúdo relacionado a uma parte um pouco mais avançada da linguagem R.

Vamos usar o nosso ambiente online de programação, o `Wrappold`. Essa ferramenta vai ajudar nos nossos primeiros códigos. Depois, vamos começar em uma ferramenta que é instalada na nossa máquina, um ambiente Studio para desenvolvimento. Mas, por enquanto, os nossos códigos iniciais vamos rodar por aqui, para facilitar quem está começando e para quem ainda não tem uma máquina dedicada para projetos. Dá para usar tranquilamente no navegador.

### Configurando o Ambiente R

Inicialmente, vou escolher minha linguagem. Vocês viram que tem muitas linguagens de programação; essa plataforma reconhece mais de 100. No nosso caso, é a linguagem R.

Vou criar um novo projeto e vou colocar aqui o primeiro ambiente para a gente trabalhar. Ele carrega automaticamente, demora um pouquinho.

Enquanto o nosso ambiente vai carregando, alguns comentários sobre a linguagem R. Já carregou, na verdade.

### Características da Linguagem R

O que eu queria mostrar para vocês é a primeira questão sobre a linguagem R. A linguagem R é uma linguagem interpretada.

Se pegarmos a maioria das linguagens, as principais, elas são compiladas. Uma linguagem interpretada tem um funcionamento um pouco diferente do que estamos acostumados. Se compararmos com a linguagem C, ela é uma linguagem compilada. Aqui, estamos trabalhando com uma linguagem que é interpretada.

Outra coisa que precisamos saber sobre a linguagem R é que tudo que geramos dentro do ambiente R, tudo que existe no R, é um objeto.

### Atribuição de Valores e Sintaxe

Para atribuir valores a objetos, basta utilizar o operador de sinal de menor com o sinal de negativo (`<-`). É dessa forma que conseguimos atribuir um valor. Quando faço isso aqui, é o sinal que estou gerando para atribuir um valor.

Se eu colocar aqui, por exemplo, objeto e colocar aqui `3 * 3`, o que estou fazendo? Estou atribuindo o valor `3 * 3` à variável `objeto`.

Vou colocar para rodar. Teve o `hello world`, eu só tenho a atribuição da variável. Agora, quando eu chamar essa variável `objeto1` na tela, o que vai acontecer? Ele vai mostrar para mim o valor 9.

Eu chamei a variável `objeto` e atribuí o valor `3 * 3`.

O que mais posso fazer? Posso chamar uma variável `objeto2` e atribuir o valor `2 * 2`. Quando fazemos essa atribuição, é para gerar o valor 4.

Vou rodar aqui o meu programa. Ele vai imprimir para mim. Não vai imprimir nada, porque só atribuí os valores. Mas se eu colocar aqui no final, `objeto1` e `objeto2`, quando rodar o meu programa, ele vai mostrar o valor 9 da primeira multiplicação e o valor 4, que é a minha segunda multiplicação.

### Manipulação de Objetos

Aí eu posso começar a manipular esses objetos. Por exemplo, se eu colocar aqui que o objeto 3 recebe o objeto 1 mais o objeto 2. Eu vou ter esse valor gerado. Estou atribuindo.

Agora coloco aqui o `objeto3` e ele vai mostrar para mim na tela essa atribuição.

(Resultado: 3 vezes 3, 9, 2 vezes 2, 4, 9.)

`⏱ 05:40`

### Objetos e Exibição de Valores em R

Essa questão sobre objetos é muito importante para que a gente entenda como funciona um código em R, as nossas funções e tudo mais. 

Aqui eu estou gerando o valor direto, mas eu poderia colocar um `print` e mandar printar o objeto 2, por exemplo. Quando eu faço isso, ele vai gerar na tela o print desse valor, que é 4. A questão de atribuição é bem tranquila.

### Diferenciação entre Maiúsculas e Minúsculas (Case Sensitivity)

Outra coisa muito importante é que, assim como na maioria das linguagens de programação, o R é sensível a letras minúsculas e maiúsculas. Quando a gente criar um objeto com letras minúsculas e com letras maiúsculas, a gente vai ter diferença.

Vamos dar um exemplo apagando essa parte do código:

Se eu colocar o valor `casa` e atribuir a essa variável uma string dizendo "todas as letras são minúsculas", colocar isso dentro do programa, dentro do objeto `casa`, é diferente de fazer algo desse tipo: seja só o "C" maiúsculo e o resto minúsculo, seja tudo maiúsculo. Eu vou ter uma outra forma de representar o meu objeto, ele vai acabar se tornando um outro objeto com "todas as letras são maiúsculas".

Ao rodar isso, tenho a atribuição desse conjunto de strings para a minha variável ou objeto, no caso `casa` minúsculo e `CASA` maiúsculo. É um exemplo só para diferenciar essa questão de maiúsculo e minúsculo dentro do nosso programa, que é uma coisa bem básica.

### Comentários no Código

Outra coisa muito importante é o comentário. A gente usa sempre o conhecido `#`. Tudo que ficar depois de um `#` não vai ser lido como programa. 

Se eu colocar `2 * 3 * 4 * 5` depois do `#` e executar, ele não vai ler nada. É apenas um comentário para que eu entenda alguma parte do programa. Geralmente usamos para lembrar uma parte do código, o que estamos fazendo naquela linha, naquela classe ou naquele objeto. Isso é muito importante.

### Resolução de Problema Físico

Agora eu vou mostrar um problema para a gente resolver com o seguinte formato. A gente vai calcular isso com um problema que tem uma característica física, porque a base do R são esses problemas envolvendo engenharia, data science e machine learning. Vamos começar com um exemplo que a gente consegue visualizar melhor:

- Seja um tubo com raio de 10 centímetros;
- Com 1,5 metros de comprimento;
- Com uma espessura de 1 centímetro;
- Qual o volume deste tubo?

A nossa fórmula seria: volume é igual a π vezes raio ao quadrado vezes a altura ($V = \pi \cdot r^2 \cdot h$), utilizando $\pi = 3.14$.

Como ficaria o nosso projeto em código?

- A primeira coisa que eu tenho que definir é o valor do meu raio: o meu `raio` vai receber o valor `10`;
- A `espessura` tem o valor `1` (pegando lá do problema);
- O meu `comprimento` tem o tamanho `70`, visualizando os dados que a gente...

`⏱ 11:40`

[Início do cálculo do volume]

Vou fazer o cálculo desse volume. O volume será igual a $\pi$ vezes o raio menos a espessura. Por que menos a espessura? Porque eu tenho que descontar ela para calcular o volume. A fórmula é:

$$V = \pi \times (raio - espessura)^2 \times comprimento$$

Eu vou elevar o raio menos a espessura ao quadrado e multiplicar pelo comprimento.

Para colocar na prática, vou inserir também um comentário. Vamos calcular a área, calcular o volume, e depois calcular o volume do cubo.

Vou executar o código para printar o valor do volume. O valor do meu volume deu 17,812,83.

***

### A origem do valor $\pi$ na linguagem R

Vocês devem estar se perguntando: o valor do raio, da espessura e do comprimento foi definido, mas na equação eu usei $\pi$ sem atribuir um valor. Eu não fiz `pi <- 3.14`.

De onde veio esse valor?

É importante notar que o objeto $\pi$ foi declarado nesse problema. Precisamos deixar claro que, na linguagem R, nós armazenamos algumas quantidades e valores que são importantes.

***

### Valores internos e bibliotecas na linguagem R

Vou apagar meu programa e colocar o valor $\pi$. Quando eu coloco o valor `pi`, ele já é armazenado internamente na linguagem R. Existe uma biblioteca que guarda esses valores. Se eu digitar `pi` e executar, ele vai mostrar que $\pi$ é igual a 3.14.

Existem outros exemplos. Se eu colocar a variável `letters` e executar, ele vai me jogar na tela o alfabeto.

Eu poderia também colocar os meses. Deixa eu ver se eu lembro aqui, seria dessa forma: `month.name`.

Se eu executar, ele vai printar na tela os meses do ano: janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro e dezembro.

Eu posso também gerar essa variável que está guardando esses valores de forma abreviada.

*(Pausa para reconexão)*

Vocês vão ver que ele apenas joga as palavras que representam os meses de forma abreviada.

Existem várias bibliotecas, mas há uma que representa esses valores que são mais conhecidos.

***

### Conclusão

No conteúdo de hoje, eu quis trazer alguns pontos que ainda não tínhamos visto e também mostrar um probleminha envolvendo a linguagem R e a questão de valores que são importantes internamente dentro do R.

Por hoje é isso. Até a nossa próxima aula.

## Relacionado

- [[linguagem-r-ambiente-replit-operadores-aritmeticos-e-escopo-em-machine-learning]]
- [[r-para-machine-learning-paradigma-funcional-recursos-base-e-pacotes]]
- [[ambientes-de-programacao-online-variaveis-e-fluxo-de-trabalho-em-nuvem]]
- [[paradigmas-e-linguagens-de-programacao-para-machine-learning]]
