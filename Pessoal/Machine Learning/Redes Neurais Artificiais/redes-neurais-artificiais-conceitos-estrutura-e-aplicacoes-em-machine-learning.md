---
titulo: "Redes Neurais Artificiais: Conceitos, Estrutura e Aplicações em Machine Learning"
tags: [machine-learning, redes-neurais-artificiais, bioinspirados, ia, conceitos, algoritmos]
data: 2026-08-21
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 14
conceitos: [Redes Neurais Artificiais (RNA), Algoritmos Bio-inspirados, Inteligência Artificial Geral vs. Restrita, Sinapses, Dendritos, Pesos Sinápticos, Função de Ativação, Combinador Linear]
---

# Redes Neurais Artificiais: Conceitos, Estrutura e Aplicações em Machine Learning

> [!resumo] Do que se trata
> A aula aborda o conceito de redes neurais artificiais, explicando sua inspiração biológica e seu papel no campo do machine learning. São detalhados os componentes estruturais de uma RNA, como dendritos, pesos sinápticos e a função de ativação, e como o processamento de dados ocorre em sistemas de automação.

## Para lembrar

- **Redes neurais artificiais são algoritmos bio-inspirados, inspirados nas interligações dos neurônios biológicos do cérebro.**
- **As aplicações atuais de inteligência artificial são restritas a problemas pré-definidos, diferentemente da inteligência artificial geral.**
- **A estrutura de uma RNA é constituída por neurônios, um conjunto de neurônios pré-definido e os pesos que são gerados para que esse neurônio seja treinado.**
- **Os componentes de uma rede neural artificial incluem: sinais de entrada, pesos sinápticos, o combinador linear, a função de ativação e o sinal de saída.**
- **Em sistemas de automação, o processamento é realizado por meio de uma função de ativação, que recebe os dados e, se for um valor esperado, ativa a saída; caso contrário, há um bloqueio da rede.**

## O que esta nota responde

- O que são redes neurais artificiais e como elas se inspiram na biologia?
- Quais são os componentes estruturais de uma rede neural artificial?
- Como o processamento de dados ocorre em uma rede neural e qual o papel da função de ativação?

## Conceitos

**Redes Neurais Artificiais (RNA)** · **Algoritmos Bio-inspirados** · **Inteligência Artificial Geral vs. Restrita** · **Sinapses** · **Dendritos** · **Pesos Sinápticos** · **Função de Ativação** · **Combinador Linear**

## Conteúdo

`⏱ 00:00`

O conteúdo de hoje é sobre redes neurais artificiais. Vamos abordar tanto a parte teórica quanto a prática, um tema muito importante para a área de *machine learning*.

### O que são Redes Neurais?

Primeiramente, a ideia é mostrar como as redes neurais foram criadas. Elas foram desenvolvidas por cientistas da computação que interpretaram esse modelo se inspirando na natureza. Por isso, esse tipo de algoritmo de redes neurais é um algoritmo bio-inspirado.

O que são redes neurais? Biologicamente falando, as redes neurais são as interligações dos neurônios que temos em nosso cérebro, seja um cérebro humano ou de qualquer outro animal.

Com isso, os cientistas da computação tiveram a ideia de criar esse modelo de forma computacional. O objetivo é que seja possível classificar problemas e lidar com outras situações que veremos nesta aula. A ideia das redes neurais é trazer algoritmos inteligentes para o cenário de *machine learning*.

### Funcionamento e Aplicações

Basicamente, o estudo das redes neurais é voltado para as sinapses que conectam os neurônios. Um neurônio envia um sinal de ativação para outro. Dentro desse contexto, temos as ativações cerebrais que processam algo, como um pensamento, um cálculo matemático ou a nossa visão.

É importante notar que essas funções são restritas. Ou seja, quando implementamos uma rede neural, ela não é feita para fazer tudo o que o nosso cérebro faz de forma computacional. Ela é projetada para realizar uma atividade específica:

- Reconhecer uma imagem;
- Fazer um cálculo;
- Descobrir algum parâmetro importante para um sistema.

Tudo isso é feito de forma restrita.

Se pegarmos o cenário de inteligência artificial dos filmes, um robô parece conseguir fazer tudo: dirigir um carro, cozinhar, roubar. Embora algumas pessoas tenham essa capacidade e se coloque que os robôs também podem, precisamos saber que isso se baseia na inteligência artificial geral — uma IA que consegue realizar várias tarefas humanas. No entanto, nossas aplicações atuais de inteligência artificial são restritas a problemas pré-definidos.

### Estrutura e Biologia

Qual é a estrutura de uma rede neural artificial? A estrutura, que usamos a sigla RNA, é constituída pela conexão entre:

- Neurônios;
- Um conjunto de neurônios pré-definido;
- Os pesos que são gerados para que esse neurônio seja treinado.

Falando biologicamente, ainda não sabemos muito bem como funciona o cérebro. Por exemplo, como a memória é armazenada em nosso cérebro? Como lembramos de um conteúdo que aprendemos na faculdade ou na escola? Onde isso fica armazenado?

Em um computador, sabemos que há um HD ou outro tipo de memória que armazena tudo isso. No entanto, em um cérebro, não temos noção de onde tudo isso é armazenado. Sabemos que é um conjunto de interligações neurais que armazenam isso de forma eletrônica.

O nosso cérebro se comunica com o corpo por pulsos elétricos. Quando quero movimentar o meu dedo, o cérebro manda um sinal elétrico para o sistema nervoso para realizar esse movimento. E partindo desse princípio, e partindo também do princípio...

`⏱ 05:40`

O princípio é que os nossos neurônios, de forma unida, conseguem aprender e gerar resultados por meio do aprendizado.

A gente parte para os modelos matemáticos de inteligência artificial. Basicamente, um neurônio computacional é um algoritmo de computador modelado matematicamente com base no neurônio biológico.

Ele tem as entradas (neurônios de entrada) e os neurônios de saída. Ele possui uma função que avalia todas essas variáveis de entrada para gerar um valor de saída. Ou seja, eu recebo valores na entrada para gerar um valor de resposta na saída.

Com isso, temos a conexão de um neurônio com vários outros, o que aumenta a capacidade de processamento, principalmente quando precisamos de várias entradas.

### Redes Biológicas vs. Artificiais

Fazendo uma comparação entre redes biológicas e artificiais, o comportamento de um neurônio biológico é o seguinte:

*   Ele tem a ideia de receber pulsos na entrada, estímulos.
*   Quando você sente uma temperatura muito alta no dedo, você tira a mão de lá, porque senão você vai se queimar.
*   Quando você recebe um choque elétrico, o seu corpo toma uma decisão para tirar a mão de lá.
*   As soluções também são geradas de forma autônoma.

Um exemplo disso é o nosso coração, que bate automaticamente, de forma involuntária. O nosso pulmão, por exemplo. Quando corremos e precisamos de um batimento cardíaco maior ou de uma respiração maior para oxigenar melhor o corpo, os neurônios têm a capacidade de decidir isso de forma autônoma. Eles já sabem como o nosso corpo funciona e já têm ali uma base de conhecimento para isso.

Quando falamos de sistemas automáticos, como o batimento cardíaco ou a respiração, também partimos para os modelos artificiais. Nesses modelos, por meio de um reconhecimento de um problema, conseguimos gerar uma solução pré-determinada para aquele problema.

### Automação de Processos e Tipos de Sistemas

Vou dar um exemplo: quando vamos a um caixa eletrônico para reconhecer a nossa impressão digital, há uma rede neural que detecta a impressão. Acima de uma taxa de certeza, a rede neural vai desbloquear o caixa eletrônico para você fazer a operação. Caso a taxa seja menor do esperado, vai dar um erro na leitura.

Isso ocorre porque é muito melhor não liberar o caixa para você fazer um saque do que ficar em dúvida e liberar para que você faça um saque na conta de uma pessoa que não é.

O sistema só vai liberar se ele tiver uma taxa de certeza muito grande. Isso é uma automação de processos.

É muito importante quando falamos de automação de processos envolvendo inteligência artificial, porque essa solução é não determinística. Isso significa que, quando você coloca sua impressão digital e não dá 100% de certeza, é muito difícil dar 100% de certeza.

Isso é diferente de quando você digita sua senha numérica. Minha senha é `123456`. É uma senha determinística. Se eu errar um valor, se eu errar um número apenas, um dígito, o caixa eletrônico não vai liberar para que eu faça uma operação.

Portanto, é 100% de certeza quando eu digito uma senha. Já a impressão digital não. Por isso, é melhor que eu utilize uma senha.

`⏱ 10:40`

O reconhecimento facial não é transferível. É preciso ter a pessoa naquele momento para realizar a operação. Por isso, muitos caixas eletrônicos utilizam recursos de reconhecimento biométrico ou reconhecimento facial.

Essa é a inspiração que temos entre um neurônio biológico e um neurônio artificial.

### Estrutura do Neurônio Artificial

Dentro de um neurônio artificial, temos uma caixa que chamamos de `núcleo`. Este núcleo recebe todos os valores que chegam para a rede e que serão processados. É neste núcleo que o processamento é realizado por meio de uma função de ativação.

A função de ativação recebe os dados, verifica a realidade deles e, caso seja um valor esperado, a função na saída ativa. Caso contrário, não há o resultado esperado e há um bloqueio da rede.

Em termos de componentes, temos:

- **Dendritos:** São as entradas da rede, as conexões entre os neurônios que geram um ponto em comum de leitura desses dados para que sejam processados.

Falando de uma forma mais completa, numa rede neural artificial, os componentes são:

- Os sinais de entrada.
- Os pesos sinápticos.
- O `combinador linear`, que pega esses valores de entrada e faz uma combinação.
- A função de ativação, que é uma função que interpreta a combinação dos valores de entrada depois da combinação linear.
- O sinal de saída, que é o sinal que gera a nossa resposta.

O processo envolve uma soma dos valores de entrada, que são multiplicados pela função de ativação para gerar o sinal de saída por meio do algoritmo de treinamento realizado.

Dependendo do tipo de algoritmo que está sendo utilizado, haverá um tipo de função. Isso será visto ainda.

Basicamente, o neurônio tem esse funcionamento de forma computacional porque é uma abstração do que existe na área biológica. Pode ser que falte alguma coisa aqui, pode ser que sim. Porém, esta é a nossa abstração matemática para que um neurônio artificial funcione.

## Relacionado

- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[logica-difusa-redes-neurais-generalizacao-e-algoritmos-bioinspirados]]
- [[metodos-bioinspirados-redes-neurais-e-logica-fuzzy-em-machine-learning]]
- [[tomada-de-decisao-sistemas-adas-e-deep-learning-em-veiculos-autonomos]]
