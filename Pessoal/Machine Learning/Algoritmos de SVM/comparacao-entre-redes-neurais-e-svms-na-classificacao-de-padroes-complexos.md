---
titulo: "Comparação entre Redes Neurais e SVMs na Classificação de Padrões Complexos"
tags: [machine-learning, redes-neurais-artificiais, algoritmos, conceitos, dados]
data: 2026-08-22
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [TensorFlow Playground, Problema da espiral, Hiperplano de separação, Support Vector Machines (SVM), Redes neurais rasas (shallow), Deep learning, Margem de segurança]
---

# Comparação entre Redes Neurais e SVMs na Classificação de Padrões Complexos

> [!resumo] Do que se trata
> A aula demonstra o funcionamento prático de redes neurais no TensorFlow Playground em cenários de classificação simples e complexos, como o problema da espiral. Em seguida, analisa a aplicação de Support Vector Machines (SVM) via código, destacando como o algoritmo define hiperplanos e margens de separação entre classes. Por fim, compara a robustez e as limitações de ambos os métodos, evidenciando quando redes neurais profundas superam o SVM em dados sobrepostos ou não linearmente separáveis.

## Para lembrar

- **O problema da espiral não pode ser resolvido com uma quantidade baixa de neurônios nem por um hiperplano simples gerado por SVM, exigindo múltiplas camadas e neurônios especialistas.**
- **Em problemas bidimensionais linearmente separáveis, redes neurais com apenas dois neurônios de entrada conseguem convergir com erro próximo de zero em poucas épocas.**
- **O objetivo do SVM é encontrar um hiperplano ideal e estabelecer uma margem de segurança entre vetores de classes distintas para definir o universo de respostas.**
- **Redes neurais artificiais são mais robustas do que SVMs em tarefas complexas em que as classes estão muito misturadas ou exigem maior capacidade de aprendizado e generalização.**

## O que esta nota responde

- Por que o SVM tem dificuldades para resolver o problema clássico da espiral?
- Como a adição de camadas e neurônios especializados no TensorFlow Playground altera a capacidade de classificação de dados complexos?
- Qual é a diferença de robustez entre Redes Neurais e SVMs ao lidar com classes com amostras sobrepostas?

## Conceitos

**TensorFlow Playground** · **Problema da espiral** · **Hiperplano de separação** · **Support Vector Machines (SVM)** · **Redes neurais rasas (shallow)** · **Deep learning** · **Margem de segurança**

## Conteúdo

`⏱ 00:00`

### Classificação com Redes Neurais no TensorFlow Playground

Aqui temos uma representação de como funciona a classificação de uma rede neural artificial. Estamos trabalhando dentro do `Playground` do `TensorFlow`, uma ferramenta que veremos logo mais na nossa trilha.

Essa ferramenta dá suporte para simularmos os nossos neurônios, as comunicações entre eles e classificar tipos de problemas clássicos na computação:

- Um primeiro problema onde temos as amostras da classe 1 na periferia e de uma segunda classe mais ao centro, que é um problema relativamente tranquilo por estar bem dividido;
- Um problema que já tem amostras um pouco mais próximas umas das outras, com o universo de respostas não tão bem dividido assim;
- Um exemplo muito fácil, com tudo bem dividido;
- O problema da espiral, que é um clássico da computação para situações bem difíceis, pois está tudo muito junto e, apenas trabalhando com uma quantidade baixa de neurônios, não conseguimos gerar essa solução.

### Redes Neurais versus SVMs

Por que estamos vendo um problema dentro de redes neurais para a aula de SVMs? O sentido desse conteúdo é mostrar que as redes neurais são mais robustas para algumas aplicações onde se exige uma maior capacidade de aprendizado, nas quais a redução do erro na classificação é mais importante dentro de aplicações complexas como essas.

### Simulação de Cenários no Playground

Vamos colocar um exemplo bem simples, trabalhando apenas com dois neurônios de entrada bidimensionais: um atuando com um hiperplano vertical e o outro com um hiperplano horizontal. 

Ao dar play, o modelo já classifica e cria o hiperplano de classificação entre as duas amostras. O erro fica praticamente zerado, necessitando de pouquíssimas épocas para atingir essa classificação.

Em outra aplicação, já mais complexa, ao dar play o sistema inicia a classificação e a conclui. Por mais que sejam amostras mais parecidas umas com as outras dentro do universo de possibilidades, a rede se comporta bem para classificar o problema usando apenas os neurônios bidimensionais.

### Resolução do Problema da Espiral

Se colocarmos o problema da espiral apenas com os dois neurônios de entrada, a rede não vai conseguir classificar. Ela tenta gerar um hiperplano dividindo as classes, porém apenas esse hiperplano não é o suficiente. Ela tentará classificar durante finitas épocas, mas não conseguirá. 

Para que a rede consiga classificar esse problema, temos que inserir novas camadas. Na rede neural, conseguimos inserir mais neurônios de entrada e colocar neurônios especialistas no problema. 

Ao dar play, a classificação ocorre de forma bem diferente, conseguindo envolver a classe dentro da espiral corretamente e concluindo a tarefa. Isso demonstra a importância de se trabalhar com uma quantidade maior de neurônios e com neurônios específicos para o problema, algo que uma SVM não conseguiria tratar aqui.

`⏱ 06:20`

Para esse tipo de situação, uma rede neural se comporta muito melhor. Eu mostrei essas situações para termos uma noção do poder de uma rede neural artificial comparado a uma máquina de vetores.

Vimos o poder de uma rede neural artificial para algumas situações clássicas da computação. Este é um ponto interessante para entendermos e conseguirmos relacionar com:

- As redes de `deep learning`;
- As redes neurais normais, que chamamos de *shallow* (redes rasas);
- E também relacionar com as `SVMs` (Support Vector Machines), para entender quando aplicar um ou outro.

Vou parar aqui o algoritmo e vou mostrar um algoritmo dentro do `Collab` que é um algoritmo de `SVM`. Ele vai trabalhar com o suporte de vetores para classificar cada amostra.

#### Objetivo do SVM

O objetivo é criar um hiperplano entre as duas classes para que seja possível classificar, por exemplo, bolinhas verdes de quadrados azuis. Conseguimos criar o hiperplano e definir a margem de segurança que já discutimos, garantindo uma classificação robusta.

No entanto, vocês viram o quão complexos são alguns problemas da computação, como o problema de espiral que mostrei. Há situações em que não é possível dividir o problema ou classificar o problema apenas com o hiperplano. Nesses casos, as situações são melhor resolvidas por meio de redes neurais artificiais.

#### Funcionamento do Algoritmo e Limitações

O objetivo do algoritmo é gerar um conjunto de vetores entre cada par de amostras de diferentes classes. Isso permite a definição do hiperplano e suas margens. Além disso, trabalhamos com essas amostras de forma eficiente para conseguir um hiperplano que define muito bem o conjunto de amostras que temos como entrada.

Ao rodar o algoritmo, em ambiente de execução, conseguimos ter uma classificação dessas amostras. Depois de geradas as amostras de entrada, que são as nossas duas classes, o algoritmo define muito bem o nosso espaço de busca, dividindo o nosso universo com um hiperplano bem definido.

O objetivo do algoritmo é definir o nosso universo de respostas por meio de um limiar para cada classe. Temos os parâmetros para que cada indivíduo tenha sua classificação correta. Temos as características e aqui temos o resultado da nossa classificação.

Ao dar um zoom, conseguimos ver que a classificação não foi tão boa assim, porque temos amostras muito parecidas entre as duas classes. Vocês estão vendo que as cruzinhas verdes estão misturadas com as bolinhas da cor azul. Isso ocorre porque as classes se parecem muito.

Neste caso, seria interessante testar também uma rede neural artificial para ver o comportamento das duas. Talvez tenhamos uma melhora. Eu considero as redes neurais algoritmos mais robustos para classificação de problemas.

#### Conclusão

Tentei mostrar uma visão geral comparando redes neurais e comparando a parte de `SVM` para termos uma noção sobre esses dois tipos de algoritmos.

Esta aula termina por aqui. É um conteúdo mais teórico sobre esse tipo de algoritmo. Mais à frente, no nosso curso, veremos a parte de algoritmos focada em implementações.

`⏱ 12:20`

No uso de bibliotecas, a visão agora é apenas conseguir visualizar esses algoritmos, o comportamento deles e entender a parte teórica também por trás de tudo isso.

## Relacionado

- [[classificacao-de-dados-e-transferencia-de-conhecimento-em-redes-neurais]]
- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[logica-difusa-redes-neurais-generalizacao-e-algoritmos-bioinspirados]]
- [[fundamentos-de-svm-hiperplanos-e-comparacao-com-redes-neurais]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- por hoje é isso nossa aula termina aqui obrigado e até a próxima.

</details>
