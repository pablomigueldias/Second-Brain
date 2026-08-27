---
titulo: "Transfer Learning e Otimização de Treinamento de Redes Neurais"
tags: [machine-learning, redes-neurais-artificiais, ia, python, dados, ferramentas, otimizacao]
data: 2026-08-27
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 11
conceitos: [Transfer Learning, TensorFlow, Keras, Inception V3, Acurácia, Dataset, Data Augmentation, GPU]
---

# Transfer Learning e Otimização de Treinamento de Redes Neurais

> [!resumo] Do que se trata
> Esta aula demonstra a aplicação prática de Transfer Learning usando TensorFlow e Keras no Google Colab, abordando a aquisição de dados do Kaggle e o treinamento de redes neurais como Inception V3. Explora a análise de resultados, destacando a importância da variedade do dataset e do tempo de treinamento para a acurácia do modelo. Por fim, apresenta técnicas como data augmentation e o uso de GPU em nuvem para otimizar o processo de treinamento.

## Para lembrar

- **Transfer Learning utiliza redes pré-treinadas, como a Inception V3, para classificação de imagens, otimizando o processo de treinamento.**
- **A acurácia ideal de um modelo de Machine Learning é alcançada quando a acurácia do treinamento e do teste são equivalentes.**
- ⚠ **Data augmentation é uma técnica que replica e modifica imagens (ex: rotação, tons de cinza) para expandir a base de dados de treinamento de uma rede neural.**
- ⚠ **O treinamento de modelos de Deep Learning pode ser executado em nuvem com GPU, liberando recursos da máquina local para outras tarefas.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Como aplicar Transfer Learning para classificação de imagens usando frameworks como TensorFlow e Keras?
- Quais fatores influenciam a acurácia e o desempenho no treinamento de redes neurais?
- De que forma a técnica de data augmentation contribui para a melhoria de modelos de Deep Learning?

## Conceitos

**Transfer Learning** · **TensorFlow** · **Keras** · **Inception V3** · **Acurácia** · **Dataset** · **Data Augmentation** · **GPU**

## Conteúdo

`⏱ 00:00`

Olá, tudo bem? Meu nome é Diego Bruno e agora a gente vai ver um pouco sobre Transfer Learning na prática dentro do Collab.

Neste exemplo, o que estou fazendo? Estou importando algumas bibliotecas, como por exemplo o `TensorFlow` e o `Keras` para o `TensorFlow`. Estou importando também uma biblioteca para manipular arquivos do tipo zip.

### Aquisição de Dados

A primeira coisa que é feita aqui nesse algoritmo é entrar na base de dados do Kaggle. Para quem nunca ouviu falar do Kaggle, a gente vai usar algumas bases deles. O Kaggle é uma base que tem alguns datasets para a gente manipular. Aqui, estou pegando um dataset deles que é o mesmo usado pelo `TensorFlow`, só que ali estava um dataset mais tratado, com um volume menor de dados. Estou buscando este dataset, fazendo o download dele e definindo um local para depois chamá-lo no meu algoritmo.

Essa biblioteca que estou usando, `Zipfile`, já trata de pegar as imagens, alocá-las e também extrair desse arquivo zipado. Há um momento em que é feito o download dessa pasta e depois temos a chamada dos arquivos de imagem, tudo certinho. A rede sendo definida aqui, no caso, a rede que estamos rodando é a `Inception V3`, que é uma rede de classificação de imagens.

### Treinamento da Rede

Nesta etapa, onde acontece efetivamente o treinamento da rede, vocês podem ver o treinamento rolando.

Estamos na época 90. Neste momento, estamos com 97% de acurácia, indo para 98% de acurácia para o treinamento, e estou com 79% para o teste. A ideia é que esse treinamento chegue a um ponto em que a acurácia do treinamento e do teste seja a mesma. O treinamento ainda está acontecendo. Isso é apenas para mostrar como está acontecendo um treinamento aqui dentro da plataforma.

Estamos usando a GPU para processamento. Todo o processamento é em nuvem; não estou usando nada da minha máquina. A única coisa que estou usando na minha máquina é o processamento para rodar o Google Chrome, mais nada.

### Análise de Resultados

Tenho aqui depois a biblioteca `Matplotlib` para gerar essas imagens de resultado para a gente. Eu já rodei esse treinamento aqui. Tudo que vai gerar naquele treinamento que está rodando agora, é isso aqui que vou mostrar agora. Por que fiz isso? Porque sei que o treinamento demora um pouco, então já rodei uma vez para ter o que mostrar aqui para vocês de exemplo.

Temos o treinamento aqui, o resultado do treinamento. Temos tanto a parte da relação da acurácia com o valor do erro. Conseguimos observar, por exemplo, na parte de validação, que o erro vai caindo até um certo ponto e depois a rede estabiliza porque não consegue aprender mais. Existem dois problemas para isso acontecer:

- O primeiro é que a base de dados não tem tantos exemplos e a rede não consegue aprender mais do que aquilo que ela já aprendeu. Aumentamos nossa base de dados e teremos um experimento assim aqui no nosso curso: mostrar um treinamento com uma base de dados pequena, depois uma base de dados grande, para ver a diferença.
- O segundo é o problema da variedade do dataset. Por exemplo, imagine que vou treinar...

`⏱ 05:20`

imagina que eu vou treinar um sistema para reconhecer uma pessoa, para reconhecer, no caso, a minha mãe.

Se eu colocar todas as fotos da minha mãe que foram tiradas na mesma hora, ah, o professor disse que 100 imagens é um tanto suficiente para treinar uma rede `deep learning`. Aí eu vou lá, pego meu celular e tiro 100 fotos dela na mesma hora. Isso é um problema, porque ela vai estar com a mesma roupa, o mesmo penteado, a mesma maquiagem (se ela estiver de maquiagem).

Isso vai gerar um problema de variedade no dataset. O ideal seria pegar várias fotos da minha mãe:
- uma foto de hoje;
- uma foto de ontem;
- uma foto da semana passada;
- uma foto do dia do aniversário dela;
- uma foto do Natal;
- uma foto do Ano Novo;
- uma foto dela segurando a gata dela;
- uma foto com o cabelo de uma cor diferente;
- depois, com um novo tipo de óculos.

Diversificando assim, o sistema se torna robusto a variações. Porque se eu treinar o sistema com as mesmas imagens, com o mesmo formato de representação da imagem, o que vai acontecer? Se caso ela tenha uma alteração no visual, apenas, sei lá, cortar o cabelo ou tomar sol e ficar um pouco bronzeada, por exemplo, isso vai gerar uma interferência na base de dados. Parece algo meio doido, mas é assim.

### Variedade do Dataset

A nossa base de dados precisa ter uma grande variedade. É a mesma coisa para este exemplo: estamos treinando gato e cachorro. Se eu colocar 100 imagens de `pincher` e 100 imagens de gato siamês, quando eu mostrar outra raça desses tipos de animais, a rede vai se comportar muito mal, porque ela não entende outros tipos de objetos na base. Assim, o meu treinamento se torna bem ruim.

### Tempo de Treinamento

Um problema é o tamanho da base de dados; o outro ponto é a variabilidade e qualidade do dataset. Outra coisa muito importante é relacionada com o tempo de treinamento.

Às vezes, se eu colocar mais épocas... Por exemplo, estamos na época 15 e vamos rodar 90 épocas. É uma quantidade boa? Sim, 100 épocas também é uma quantidade boa.

Porém, às vezes, se eu colocar mais tempo de treinamento, sei lá, vou colocar mil épocas, vou subir isso aí... O que vai acontecer? Eu vou conseguir melhorar um pouco o treinamento, porque o sistema vai visualizar novamente as imagens para treinar. Só que isso também não é uma solução muito viável. É resolver um problema por força bruta do algoritmo de treinamento. O ideal mesmo é ter uma solução de dados variada.

### Data Augmentation

"Ah, professor, mas eu não tenho uma base de dados tão grande. As imagens que eu tenho são essas. Eu não tenho mais imagens."

Nós temos um processo que se chama `data augmentation`. O que seria isso? Pegamos as imagens que temos e as replicamos. Como?
- Uma imagem colorida, eu a deixo em tons de cinza. Já é outra imagem.
- Uma imagem que está em pé, eu a rotaciono 90 graus. Depois eu rotaciono 180 graus.

Eu vou mudando as imagens. Só de rotacionar a imagem, eu já tenho um novo tipo de imagem para treinar a minha rede. Ela vai olhar com outra perspectiva a imagem de entrada. Então, uma imagem, se eu a rotacionei...

`⏱ 10:00`

Se eu rotacionei ela nos quatro ângulos possíveis, eu já tenho quatro imagens diferentes para o treinamento.

A gente vai aprender também a fazer esse tipo de relação.

### Treinamento na Nuvem

Aqui, eu queria mostrar para vocês um treinamento, como é feito na nuvem. Eu não estou usando nada de processamento da minha máquina.

Não temos desculpa para não trabalhar com Deep Learning ou com um modelo de Machine Learning porque exige muito processamento.

Aqui a gente consegue, porque para tudo a gente tem um jeito. Nosso jeito, neste caso, é usar o `Google Collab`.

## Relacionado

- [[machine-learning-frameworks-e-ambientes-de-desenvolvimento-tensorflow-pytorch-ke]]
- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[visualizacao-de-dados-e-regressao-com-matplotlib-e-scikit-learn]]
- [[classificacao-de-dados-e-transferencia-de-conhecimento-em-redes-neurais]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Por hoje é isso Muito obrigado aí E até a próxima

</details>
