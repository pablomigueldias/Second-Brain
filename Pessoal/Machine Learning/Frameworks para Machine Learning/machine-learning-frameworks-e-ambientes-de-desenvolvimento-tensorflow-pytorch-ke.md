---
titulo: "Machine Learning: Frameworks e Ambientes de Desenvolvimento (TensorFlow, PyTorch, Keras)"
tags: [machine-learning, ia, redes-neurais-artificiais, ferramentas, algoritmos, conceitos]
data: 2026-08-25
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [Frameworks, TensorFlow, PyTorch, Keras, Deep Learning, Transfer Learning, ImageNet, GPU]
---

# Machine Learning: Frameworks e Ambientes de Desenvolvimento (TensorFlow, PyTorch, Keras)

> [!resumo] Do que se trata
> Esta aula explora os principais frameworks e ambientes de desenvolvimento utilizados em projetos de Machine Learning e Inteligência Artificial. São apresentados o TensorFlow e o PyTorch como ferramentas essenciais que gerenciam dependências e hardware, facilitando a programação. A aula detalha o Keras como uma API de alto nível que simplifica a criação de redes neurais e permite a importação de modelos pré-treinados, como os baseados no dataset ImageNet, para aplicação de Transfer Learning.

## Para lembrar

- **Na computação nada se cria, tudo se copia é uma frase aplicável a Machine Learning, onde há muitas soluções prontas e reutilizáveis.**
- **TensorFlow e PyTorch são frameworks que desenvolvem uma camada entre o programador e o sistema de bibliotecas, gerenciando dependências e o uso de hardware como GPUs.**
- **Keras é uma API de alto nível que auxilia o desenvolvimento de redes neurais (shallow e deep learning) e trabalha em conjunto com o TensorFlow.**
- **Modelos de redes de Deep Learning pré-treinados, como VGG16, VGG19 e ResNet50, podem ser importados via Keras para serem aplicados em novos problemas.**
- **ImageNet é um dataset com mil classes de objetos e muitas imagens, cujo treinamento pode ser aproveitado para novos projetos através do Transfer Learning.**

## O que esta nota responde

- Quais são os principais frameworks e ambientes de desenvolvimento para Machine Learning e IA?
- Como o Keras se integra com o TensorFlow para facilitar a criação e uso de redes neurais?
- O que é Transfer Learning e qual a importância do dataset ImageNet nesse contexto?

## Conceitos

**Frameworks** · **TensorFlow** · **PyTorch** · **Keras** · **Deep Learning** · **Transfer Learning** · **ImageNet** · **GPU**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e hoje vamos ver um conteúdo relacionado às bibliotecas de Machine Learning e também aos frameworks que utilizamos para facilitar nossos projetos nesse cenário.

Utilizando vários tipos de frameworks, usamos aquela frase da computação: na computação nada se cria, tudo se copia. Isso ocorre porque, para Machine Learning, atualmente há muita coisa pronta.

Se você precisa de uma rede de Deep Learning para classificar imagens, você precisa de uma rede do tipo Deep Learning. Isso também é usado para classificar diferentes tipos de problemas na área rural, como, por exemplo, detecção de pragas ou detecção de desmatamento. Temos praticamente tudo isso pronto, basta que realizemos o treinamento.

Nesse caso, nem precisamos fazer um treinamento do zero. Aplicamos um *transfer learning* para retreinar a rede com base no aprendizado passado, influenciando o aprendizado futuro.

### Ambientes de Desenvolvimento em ML e IA

Vou mostrar os ambientes que trabalhamos atualmente e que são utilizados pelas maiores empresas e indústrias na área de Machine Learning, Inteligência Artificial, Data Science e Big Data.

A primeira ferramenta, que na verdade não é uma biblioteca, mas um framework de desenvolvimento, é o `TensorFlow`. Ele é um dos melhores ambientes para desenvolvimento.

O `TensorFlow` possui uma camada entre o programador e o código. Isso nos permite desenvolver nossos projetos com o auxílio de bibliotecas, com o auxílio de códigos no `GitHub`, por exemplo.

O que conseguimos com isso? Gerenciar o *workflow* de tudo. Isso é importante porque, quando trabalhamos com Python, temos muitas dependências, muitas bibliotecas e muitas coisas que não são apenas dependentes do nosso código; acabamos usando muitas outras ferramentas. Por isso, é crucial gerenciar tudo isso, e o `TensorFlow` é uma grande ferramenta para isso.

Basicamente, tudo que desenvolvemos para Machine Learning, o `TensorFlow` tem suporte.

Além disso, em Python, sempre acabamos linkando com o `TensorFlow` outro ambiente de programação também muito conhecido, que também é um framework: o `PyTorch`.

O `PyTorch` também tem um grande potencial em desenvolvimento. No início, houve uma mini guerra entre essa ferramenta e o `TensorFlow`, mas hoje os algoritmos trabalham em conjunto com esses dois ambientes.

Não há um cenário de que se deve saber trabalhar apenas para `TensorFlow` ou apenas para `PyTorch`. Atualmente, utilizamos os dois ambientes, independente do projeto. Eles se complementam em alguns aspectos, mas ainda é mais utilizado o `TensorFlow`.

Os dois são ambientes para desenvolvimento de Machine Learning.

### O Papel dos Frameworks

Para resumir, o `TensorFlow` e o `PyTorch` são frameworks que desenvolvem uma camada entre o programador e o sistema de bibliotecas. Eles também gerenciam o sistema de dependências, o que facilita muito a programação.

Esses frameworks meio que vão linkar o nosso código com todas as ferramentas que precisamos, e não somente com a parte de bibliotecas, mas também com o gerenciamento do nosso hardware. Por exemplo, se estamos usando uma GPU para processar dados, podemos, com o auxílio do `TensorFlow`, habilitar a GPU para processar nossa rede neural ou desabilitar a GPU.

`⏱ 05:40`

compatível e processar só em processador. É um ambiente que ajuda muito o nosso desenvolvimento de projeto. Tanto o `TensorFlow` como o `PyTorch` facilitam muito a nossa vida de desenvolvimento.

### Keras

Depois, temos o Keras. O Keras é um ambiente de desenvolvimento que é considerado, às vezes, como uma biblioteca, porém, eu o considero como um *framework* de redes neurais.

Ele suporta tanto as redes neurais mais básicas, que consideramos redes neurais *shallow*, quanto as redes neurais profundas, as redes de *deep learning*. O Keras auxilia o desenvolvimento dos nossos projetos, tanto para iniciantes quanto para quem já trabalha no mercado de *deep learning*.

Atualmente, existe uma união entre o `TensorFlow` e o `Keras`, trabalhando de forma conjunta. Se você precisa, por exemplo, utilizar uma rede no `TensorFlow`, pode importar um modelo do `Keras`.

Como isso acontece? Se pesquisarmos no Google por `Keras Models`, aparecerão as redes de *Deep Learning* que podemos usar em nossos projetos.

Por exemplo, se eu pegar alguns modelos de redes como:
- `VGG16`
- `VGG19`
- `ResNet50`
- `ResNet50v2`

Eu não preciso implementar ou conectar uma rede. Eu venho no `Keras` e faço um `import` dentro do `TensorFlow` de um modelo de rede pronto, e então o aplico ao meu problema.

Essa é a vantagem de trabalhar com o `Keras`: conseguimos importar os modelos de rede que estão disponíveis. Estes são apenas alguns modelos; existem outros modelos suportados dentro do `Keras`.

### Como o Keras funciona

Basicamente, nesta primeira linha de código, estamos chamando o `TensorFlow` com o `Keras Application` e importando o modelo de rede neural que é a `ResNet50`.

O que estamos fazendo é colocar, dentro do `TensorFlow`, um bloquinho que é uma rede neural do tipo *deep learning*, a `ResNet50`. Eu não preciso definir a estrutura nem implementar a rede; estou apenas chamando o modelo.

Eu poderia chamar outro modelo, como `Inception`, uma `VGG`, `BG16` ou `BGG19`. Dependendo do modelo que eu quero, é só fazer o `import`.

Aqui, temos como modelo a rede `ResNet50`, trabalhando com os pesos de entrada. Estou utilizando como entrada da minha rede o aprendizado feito com a `ResNet50` em cima do *dataset* do `ImageNet`.

### O que é o ImageNet?

Para recordar, o `ImageNet` é um *dataset* com mil classes de objetos e muitas imagens de diferentes classes.

Podemos aproveitar o treinamento que foi feito em cima desse conjunto de dados para o nosso novo treinamento. Isso gera um estado diferente de treinamento, que é aproveitar o treinamento passado para o futuro. Isso se chama *transfer learning*.

Para mostrar um pouco das imagens do `ImageNet`, ele trabalha com imagens desse tipo. Há imagens de diferentes formatos.

Se você pegar, por exemplo, uma baleia orca, haverá fotos de baleias orcas reais e também fotos de pelúcias de baleia orca, de estátuas de baleia orca, ou uma camiseta que tem uma foto de uma baleia orca.

Isso facilita o reconhecimento de objetos em diferentes tipos de formatos. Esse *dataset*, na área de imagens, é um *dataset* que é o mais...

`⏱ 11:00`

O `Keras` é o mais conhecido e o mais utilizado pela proporção de exemplos que a gente tem aqui dentro.

Nesse caso que eu mostrei para vocês, ele está pegando as imagens. Na verdade, está pegando os pesos que foram treinados sobre essas imagens.

E aí a gente aplica para o nosso novo treinamento um Transfer Learning. Não precisa implementar uma rede neural do zero. Eu gero o meu treinamento com base em uma rede neural pronta.

Posso também aplicar o treinamento que foi feito de forma passada para o futuro, reaproveitando o que a gente tem de aprendizado da rede.

### Importância dos Frameworks

Esses seus clientes são muito importantes para que a gente entenda como importar uma rede, como utilizar uma rede, como integrar tudo o que a gente precisa.

Tanto `Keras` quanto `PyTorch` quanto `TensorFlow` ajudam muito a gente na área de projetos.

### Visão Geral e Próximos Passos

O conteúdo hoje é esse para mostrar um pouco a visão desses ambientes.

E depois a gente vai começar a ver um pouco sobre bibliotecas.

## Relacionado

- [[../Python para ML/visualizacao-de-dados-e-regressao-com-matplotlib-e-scikit-learn]]
- [[../Python para ML/tipos-de-dados-em-python-inteiros-flutuantes-complexos-strings-e-booleanos]]
- [[../Introdução ao Machine Learning/redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[../Python para ML/python-para-machine-learning-paradigmas-ecossistema-e-ambientes-de-execucao]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Então, muito obrigado, e até a próxima.

</details>
