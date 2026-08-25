---
titulo: "Machine Learning: Bibliotecas Essenciais (NumPy, SciPy, Theano, Scikit-learn)"
tags: [machine-learning, ferramentas, algoritmos, python, conceitos, fundamentos]
data: 2026-08-25
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 12
conceitos: [Bibliotecas de Machine Learning, NumPy, SciPy, Theano, Scikit-learn, Cálculos científicos, Otimização, Algoritmos de aprendizado]
---

# Machine Learning: Bibliotecas Essenciais (NumPy, SciPy, Theano, Scikit-learn)

> [!resumo] Do que se trata
> Esta aula explora as bibliotecas fundamentais para projetos de Machine Learning, destacando como elas otimizam o desenvolvimento ao fornecer funções prontas e validadas. São apresentadas as funcionalidades de NumPy para manipulação de matrizes e cálculos científicos, SciPy para otimização e álgebra linear, e Theano para matemática e estatística. Por fim, detalha-se o Scikit-learn, uma biblioteca popular que oferece modelos prontos para algoritmos de aprendizado supervisionado e não supervisionado, mineração e análise de dados.

## Para lembrar

- **Bibliotecas de Machine Learning fornecem funções prontas e validadas, como multiplicação de matrizes e análise de acurácia, economizando tempo de desenvolvimento.**
- **NumPy é uma coleção de funções matemáticas de alto nível para trabalhar com matrizes multidimensionais e cálculos científicos, fundamental para Machine Learning.**
- **SciPy oferece módulos para otimização, álgebra linear e integração estatística, sendo crucial para validação e definição da acurácia de modelos de Deep Learning.**
- **Theano é uma biblioteca para matemática e estatística, que pode ser usada para funções específicas, embora NumPy e SciPy frequentemente cubram a maioria das necessidades.**
- **Scikit-learn é uma biblioteca popular que oferece suporte para a maioria dos algoritmos de aprendizado de máquina supervisionado e não supervisionado, mineração e análise de dados, incluindo SVM, K-Means e regressão.**

## O que esta nota responde

- Quais são as principais bibliotecas utilizadas em projetos de Machine Learning?
- Como NumPy, SciPy, Theano e Scikit-learn auxiliam no desenvolvimento de modelos de Machine Learning?
- Quais tipos de algoritmos e funcionalidades o Scikit-learn oferece para Machine Learning?

## Conceitos

**Bibliotecas de Machine Learning** · **NumPy** · **SciPy** · **Theano** · **Scikit-learn** · **Cálculos científicos** · **Otimização** · **Algoritmos de aprendizado**

## Conteúdo

`⏱ 00:00`

Olá, tudo bem? Meu nome é Diego Bruno e hoje a gente vai ver um conteúdo relacionado com as bibliotecas utilizadas para Machine Learning.

A gente já viu um pouco sobre os frameworks que utilizamos, que realizam suporte para o trabalho com redes de Deep Learning e modelos em geral de Machine Learning. No entanto, também temos as bibliotecas que geram suporte para os nossos projetos, para que a gente não tenha que implementar algumas funções do zero.

Por exemplo, a multiplicação de matrizes, as convoluções de uma rede de Deep Learning, a parte de geração e análise de dados, a representação dos dados em gráficos e a análise da acurácia de um sistema que treinamos. É muito importante que a gente utilize essas bibliotecas que dão suporte.

"Mas eu consigo fazer sem o auxílio das bibliotecas?" Obviamente sim. Só que o problema que você vai ter é que vai perder tempo fazendo coisas que já estão prontas e que já são validadas por outros projetistas, por outros desenvolvedores.

Quando utilizamos uma biblioteca dessas, por exemplo, `NumPy`, `Scikit Learning`, `Matiplotlib`, `Teano`, `Pandas`, já temos uma validação sobre isso. Às vezes, desenvolvemos um método de validação ou um método de visualização de dados e ficamos nos perguntando: "Será que está certo? Alguém já validou o que eu fiz?" Obviamente não, porque você está desenvolvendo inicialmente. Agora, com essas bibliotecas, já temos esse suporte. Já temos o aval de que funciona e que podemos aplicar no nosso projeto tranquilamente.

### NumPy

A primeira biblioteca é a `NumPy`. Ela nos retorna um conjunto de funções que consegue trabalhar com matrizes multidimensionais e também com o processamento dessas matrizes.

O que é essa biblioteca? No final das contas, é uma coleção de funções matemáticas de alto nível. Ela é muito utilizada para cálculos científicos que são fundamentais para o aprendizado de máquina, no caso, no termo em inglês que estamos acostumados: Machine Learning. Essa biblioteca é muito utilizada na área de Machine Learning.

Para instalar, é muito simples. Depois eu vou mostrar para vocês como fazer isso. Para usar, eu faço:

```python
import numpy as np
```

E já tenho minha biblioteca pronta para usar. Aqui, estou manipulando uma matriz com o auxílio da função que vem da biblioteca `NumPy`.

### SciPy

A gente tem também a `SciPy`. O que seria essa `SciPy`? Também é uma biblioteca para Machine Learning que contém diversos módulos para otimização.

Também é uma biblioteca [inaudível], voltada para a álgebra linear, e também para a integração estatística do nosso modelo de Deep Learning, por exemplo, com a validação, com o algoritmo que vai definir a sua acurácia. Precisamos utilizar essa biblioteca para auxiliar nessa situação.

Só um adendo a esse conteúdo: às vezes, a gente fica imaginando "eu vou chamar essa biblioteca para avaliar os dados da minha rede, como que é?". Às vezes, isso acontece frequentemente. Quando implementamos a rede, já estamos colocando as dependências dessa biblioteca. Para mostrar a nossa acurácia, para definir qual foi o erro de treinamento, qual é o erro na validação, já usamos essa biblioteca durante o corpo.

`⏱ 05:20`

...do desenvolvimento do algoritmo. Depois, a gente só instala a biblioteca porque ela vai precisar dessas funções que tem dentro da biblioteca que você utilizou no seu projeto.

É muito comum que, quando a gente sobe uma rede, por exemplo, lá no `GitHub`, a gente tem que colocar um arquivo para a pessoa ler e saber quais as dependências que ela precisa para rodar a sua rede. É muito comum a gente ter que instalar `NumPy` e `SciPy` nas redes de Deep Learning.

### Theano

A gente tem também o `Theano`. O que seria esse `Theano`? Também é uma biblioteca que trabalha basicamente com matemática e estatística.

Mas já tem `NumPy` e `SciPy`. Por que `Theano` também? Basicamente, o `Theano` vai ter outras funções de diferentes formatos. Porém, às vezes a gente não precisa usar todas. Se você usar `NumPy` e `SciPy`, já dá conta do seu problema, a gente não precisa usar `Theano`. É muito particular do seu problema.

Às vezes, quando a gente está desenvolvendo, a gente já programa alguma função que a gente nem sabe que tem dentro do `Theano`. É muito comum isso também: a gente não conhecer muito bem a documentação das bibliotecas, a gente não sabe o potencial delas. Você está programando e vê: "Ah, eu preciso aplicar aqui uma multiplicação de matrizes convolucionais. Isso eu não sei onde tem, então eu vou fazer na mão". E, às vezes, tem lá dentro da biblioteca do `NumPy`. É comum acontecer isso, a gente programar uma coisa que já tem pronta. Mas é uma questão de ler a documentação dessas bibliotecas para a gente saber como funciona.

### Scikit-learn

A biblioteca `Scikit-learn` é uma das mais famosas atualmente na área de `Machine Learning`. Por quê? A gente trabalha aqui com modelos que auxiliam em nossos projetos. A gente tem muita coisa pronta aqui dentro dessa biblioteca quando a gente precisa de algum modelo.

Por exemplo, utilizar suporte para a maioria dos algoritmos de aprendizado de máquina supervisionado e não supervisionado é uma das funções de se utilizar o `Scikit-learn`.

O `Scikit-learn` também é utilizado, além da parte tradicional de `Machine Learning`, para mineração de dados e análise de dados. São funções que a gente consegue habilitar dentro dessa biblioteca, auxiliando a nossa atividade de programação para `Machine Learning`.

Um exemplo: você precisa de uma `SVM` para rodar sobre um conjunto de dados para comparar com uma rede de `deep learning`. Você não precisa implementar uma `SVM` do zero, você utiliza uma `SVM` que tem pronta dentro dessa biblioteca.

Tem muita coisa aqui: parte de classificação e regressão. Se eu preciso fazer uma classificação, eu tenho uma `SVM` pronta. Se eu preciso trabalhar com um modelo de regressão, tem vários algoritmos prontos aqui também. Se eu preciso trabalhar com algoritmo não supervisionado, com cluster, eu tenho algoritmos como:
- `K-Means`
- `Mean Shift`

A gente tem muita coisa já implementada. A parte básica de `Machine Learning`, digamos assim, a gente tem pronta aqui. A gente não precisa ir lá implementar do zero algoritmos que são clássicos de `Machine Learning` atualmente. Se a gente for implementar, vai ter trabalho.

Vou dar um exemplo: tem muita situação que a gente tem que comparar algoritmos.

`⏱ 10:20`

Para ver qual é o melhor para o nosso problema. Já pensou você ter que implementar tudo do zero? É um problema muito grande quando a gente faz isso.

Porque, às vezes, você vai implementar para ver como se comporta e não vai ser bom o resultado. Você acaba perdendo tempo à toa.

Agora, se você tem um algoritmo pronto, você não tem essa perda de tempo. Essas bibliotecas facilitam muito a nossa vida de desenvolvimento.

## Relacionado

- [[../Introdução ao Machine Learning/redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[../Python para ML/tipos-de-dados-em-python-inteiros-flutuantes-complexos-strings-e-booleanos]]
- [[machine-learning-frameworks-e-ambientes-de-desenvolvimento-tensorflow-pytorch-ke]]
- [[../Python para ML/visualizacao-de-dados-e-regressao-com-matplotlib-e-scikit-learn]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `num Pai → NumPy`

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- conteúdo de bibliotecas para machine learning de manipulação de dados matemáticos estatísticos e também para parte de validação para utilização de modelos é isso aqui E aí a gente pode utilizar modelos com grande facilidade e a gente vai ver alguns exemplos bom por hoje o conteúdo é esse então até a nossa próxima aula um abraço para vocês e até lá

</details>
