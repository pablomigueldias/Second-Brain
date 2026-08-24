---
titulo: "Implementação e Treinamento de Redes Neurais para Classificação de Imagens (MNIST)"
tags: [conceitos, estudo, ia, fundamentos, machine-learning, redes-neurais-artificiais, dados]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 30
conceitos: [MNIST, Rede Neural, Tensor, PyTorch, Classificação, Otimização, CUDA, Dataset]
---

# Implementação e Treinamento de Redes Neurais para Classificação de Imagens (MNIST)

> [!resumo] Do que se trata
> A aula demonstra a implementação completa de uma rede neural do zero, utilizando o problema MNIST (reconhecimento de números manuscritos) como estudo de caso. São abordados desde a configuração do ambiente e a transformação do dataset de imagens para o formato Tensor, até a estruturação do treinamento, otimização de pesos e a verificação de dispositivos (CUDA vs. CPU). Por fim, o processo de treinamento e validação do modelo é executado, mostrando o ciclo completo de um projeto de Machine Learning.

## Para lembrar

- **O problema MNIST é um problema numérico de classificação, treinado para reconhecer números escritos à mão (0 a 9).**
- **O PyTorch é um framework de programação similar ao TensorFlow, auxiliando no desenvolvimento de projetos de Machine Learning.**
- **Imagens em Machine Learning, quando usadas em PyTorch e TensorFlow, precisam ser transformadas para o formato Tensor, que é um padrão numérico que representa a imagem.**
- **A otimização da rede envolve a atualização dos pesos, sendo necessário um otimizador para guiar o processo de treinamento.**

## O que esta nota responde

- Como implementar uma rede neural do zero para resolver um problema de classificação de imagens?
- Qual é o formato de dados que as bibliotecas de ML (como PyTorch e TensorFlow) utilizam para processar imagens?
- Quais passos são necessários para configurar e treinar um modelo de rede neural, desde a preparação do dataset até a otimização dos pesos?

## Conceitos

**MNIST** · **Rede Neural** · **Tensor** · **PyTorch** · **Classificação** · **Otimização** · **CUDA** · **Dataset**

## Conteúdo

`⏱ 00:00`

### O Problema do MNIST

Olá, tudo bem? Meu nome é Diego Bruno e hoje a ideia é vermos uma implementação de uma rede neural do zero.

Primeiramente, vamos trabalhar com o problema do MNIST, falando na parte de imagens. É um tipo de rede neural treinada para reconhecer problemas numéricos: números que são escritos à mão. Trata-se de um problema apenas numérico, não temos letras, apenas números de 0 a 9.

Quando precisamos de uma implementação um pouco mais complexa, vamos fazendo as combinações dos números. Isso é muito importante, por exemplo, para quando precisamos interpretar o CEP de uma carta automaticamente. Grandes empresas como a Amazon e o Mercado Livre já têm um departamento para reconhecer o CEP da rua do remetente.

Quando eles mandam a encomenda, já geram o QR code de forma digital. Porém, quando recebem um produto de volta — uma devolução ou algo que foi para a garantia —, a pessoa escreve à mão o endereço de destino. Precisa-se reconhecer aquilo de forma automática para não haver uma pessoa o tempo todo recebendo a encomenda.

Esse é um dos problemas envolvendo o reconhecimento numérico, mas existem outras situações também, como:
- Compensação de cheques (quase ninguém usa mais, porém ainda há problemas aplicados para cheque);
- Digitalização de cartas;
- Manuscritos antigos.

O problema do MNIST é um problema numérico e vamos aprender como tratá-lo.

### Configuração do Ambiente e Bibliotecas

Primeiramente, vou definir o nome do nosso projeto no Colab como `rede neural do zero`.

A primeira parte a ser inserida no projeto são as nossas bibliotecas:

- A primeira importação será o `import` do `NumPy`, cuja importância já discutimos.
- Agora, vamos importar também um ambiente que se chama `torch`. Vamos usar um framework de programação chamado `PyTorch`. Já falamos muito sobre `TensorFlow`; o `torch` é bem parecido, tem as mesmas funções e também auxilia no desenvolvimento de projetos.
- Realizo o `import` para o `torch`, utilizando funções para as redes que vamos usar.
- Faço a importação do `torchvision`, que é a biblioteca do `PyTorch` voltada para visão computacional, que é o foco do nosso trabalho.
- Realizo o `import` do `math`.
- Importo também a biblioteca `time`. A biblioteca `time` é importante para trabalharmos com valores de tempo do nosso algoritmo, como o tempo de execução e o tempo de resposta da rede.
- Finalizo com as importações do `torchvision` e do `torch`.

`⏱ 06:20`

```python
import nn
```

Professor: Mas a gente não precisa instalar nada dessas bibliotecas, só está dando `import` aí? Não precisa? Porque o Colab já tem na máquina deles que a gente acerta essa, fica tudo instalado lá?

Professor: Agora, já criei esse bloco dos `import`s, e eu vou inserir aqui uma célula de código nova, para a gente ir separando.

Professor: Posso colocar tudo junto?

Professor: Pode, mas eu não gosto muito de fazer isso. Eu gosto de trazer tudo para a gente trabalhar em módulos.

### Transformação do Dataset para Tensor

O que eu vou fazer é entrar na base de dados do MNIST e copiar o download do dataset, e também já estou rodando aqui a transformação do dataset para arquivo tensor.

O que significa isso? A gente tem um dataset de imagens, porém o TensorFlow e o PyTorch trabalham com imagens em tensor.

O que seria uma imagem em Tensor? É uma imagem que tem um padrão relacionado numérico que representa essa imagem em um formato que as redes de Deep Learning, que rodam no TensorFlow, por exemplo, estão habituadas a trabalhar.

Eu posso subir uma imagem em JPEG ou PNG? Pode, mas as redes não apresentam o mesmo desempenho. Por isso, o motivo de usarmos o TensorFlow é trabalhar com a imagem em tensor.

### Baixando e Processando os Dados

Vocês estão vendo que o código que eu coloquei aqui está baixando as imagens lá no site do Ian LeCun, o dataset dele.

Ian LeCun é um dos principais nomes na área de inteligência artificial e é o responsável pela inteligência artificial do Facebook. O reconhecimento facial do Facebook, e a parte agora do metaverso, é tudo o Ian LeCun que coordena esses projetos. Ele é o diretor de A do Facebook.

O sistema baixou os datasets, que são conjuntos de imagens que formam, na verdade, um único dataset. Ele executou aqui tranquilo. Estou apenas baixando as imagens e convertendo para tensor.

Eu copiei esse código lá dentro do site mesmo, do MNIST, no site do Ian LeCun. Eu estou baixando tudo desse site. Eu só peguei o código aqui e colei para a gente usar. É a mesma coisa que você estivesse baixando uma base de dados de um código do GitHub; eu só estou reproduzindo aqui.

### Verificação da Estrutura de Dados

Agora, vou criar uma nova célula de código. Vou colocar aqui a representação de um dígito, só para conferir se a nossa estrutura de dados está representando a imagem corretamente.

Vou chamar essa imagem com uma função que lê a nossa imagem, carregando uma imagem do nosso treinamento (`trainloader`). Apareceu aqui o nome da função certinho.

Vou colocar aqui:

*   `Imagens`
*   `Etiquetas`
*   `Data`

Vou chamar esse conjunto de imagens e vou colocar para plotar essa imagem.

Para fazer isso, vamos usar:

*   `Matplotlib`, essa biblioteca.
*   `numpy`, a biblioteca que importamos.

Vou terminar essa função para não esquecer e depois eu explico para vocês. Vou imprimir essa imagem em tons de cinza (`gray`).

`⏱ 12:00`

Vamos executar aqui o nosso código. O que eu fiz? Eu peguei uma imagem da base de treinamento e estou dando um `plot` nela aqui para a gente visualizar uma imagem da base de dados, para conferir se estamos conseguindo ler a base de dados de forma correta.

Vou criar um novo bloco de código, uma nova célula de código. Agora, eu quero conferir o tamanho de uma imagem, para verificar o tamanho do tensor da imagem, o tamanho do tensor que representa a nossa imagem. Então, vou dar um `print` aqui, imagens, vou colocar aqui para representar o `shape` dela, o formato. O que está fazendo? Vamos deixar comentado para verificar as dimensões do tensor de cada imagem.

Agora, vou dar um outro `print` aqui, para a gente pegar a etiqueta da imagem lá do dataset e também apresentar essa imagem com o `shape` dela.

O que estamos fazendo aqui? Vamos representar a mesma coisa para verificar a dimensão, só que não da imagem, mas sim da etiqueta, para verificar as dimensões do tensor de cada etiqueta que estamos trabalhando.

Vou executar aqui. Pronto. Qual que é o nosso tamanho aqui? Estamos trabalhando com a dimensão 1 por 28 por 28. Essa é a relação que temos dessa imagem com o tensor que está representando ela, certo?

### Implementando a Rede Inception

O que vou fazer aqui? Já imprimimos o tensor dela, agora vamos começar a nossa rede especificamente.

A primeira coisa que vou fazer é usar com vocês um modelo de rede que é a rede Inception. Como encontro o modelo dela? Venho aqui, `Keras InceptionV3`. Temos aqui as redes que podem ser utilizadas, então não preciso implementar nada do zero.

Eu venho aqui e pego o modelo da rede que quero usar. O modelo que estou usando aqui com vocês é o Inception V3, uma rede que gosto muito de usar e a mesma rede que o Google — ou melhor, que o Facebook — implementou aí para o reconhecimento facial. É claro que atualmente eles devem ter uma rede mais moderna, mas a rede Inception é muito boa para quem está começando a entender, principalmente a estrutura dela.

O que vou fazer aqui é copiar as camadas da rede Inception para o nosso módulo. Então, vou pegar aqui a nossa rede. Copiei aqui da rede Inception. Agora vou criar um novo módulo aqui, ambiente de execução, inserir célula de código, vou inserir aqui as camadas da rede.

Estamos carregando o modelo. Deixei aqui comentado certinho para vocês verem.

A camada de entrada da rede, vamos usar 784 neurônios que se ligam a 128 neurônios. Esses 128 neurônios estão na segunda camada. Cada camada interna da nossa rede vai trabalhar com 128 neurônios e se ligam a 64 neurônios. A camada interna que temos, trabalhamos com 64 neurônios que se ligam a 10.

— Ah, professor, mas como foi definido isso? Isso é a estrutura da rede Inception? Quem treinou ela ali, quem modelou ela e testou, definiu isso? Posso mudar? Posso tirar 128 e colocar 256? Posso tirar 64 e dobrar? Pode? Você pode tentar melhorar.

`⏱ 17:40`

Lembrando que o que acontece é que quanto mais camadas você colocar, mais pesada a sua rede vai ficar. Pode ser que ela tenha um maior desempenho, porém o custo dela vai aumentando. Cada vez que você aumenta neurônios, o custo aumenta.

Aqui temos a nossa camada da função de ativação. Para quem já viu a parte de redes neurais básicas que passei, aqui temos uma função de ativação da camada de entrada para a camada interna. Estamos usando uma função que é a função `ReLU`, também uma função linear que ativa as camadas internas da rede. E estamos usando os dados para calcular a perda usando a função `softmax`.

Vou executar isso aqui para que eu leia a estrutura da rede.

### Otimização e Estrutura de Treinamento

Vou colocar a parte de otimização da rede para que tenhamos a primeira vista, que é a atualização dos pesos da rede. Vamos usar neurônios e baias, e vamos usar a atualização dos pesos. Para isso, temos que usar um otimizador bom.

Vamos carregar o otimizador da rede, que é quem vai trazer o nosso treinamento. Montamos a estrutura da nossa rede e agora vamos colocar a estrutura de treinamento dela.

Estou definindo que o número de épocas de treinamento é 30, mas vou colocar um número menor para vocês verem o treinamento acontecer.

Estamos colocando aqui os valores de treinamento da nossa rede, alguns parâmetros, como o parâmetro de `bias` e tudo mais. Temos o incremento de cada época e a inicialização da perda acumulada da época em que estamos trabalhando. Vamos partir sempre da mesma época, por isso que estamos dentro de um laço, que vai partir de um treinamento e época em época.

O modelo que estou usando aqui é o `Keras Inception v3`, então essa estrutura de treinamento é própria deles, mas basicamente é isso.

### Execução do Treinamento e Validação

Defini que o número de épocas é 10, então vai treinar durante 10 épocas. Em um bom treinamento, a gente tem que colocar no mínimo 100 épocas. Coloquei 10 para não ficar um tempo tão longo, senão a gente fica uma aula só vendo o treinamento acontecer.

Vou executar aqui. Executou, tranquilamente, não deu nenhum erro.

O foco que temos é colocar a rede para executar com o otimizador que definimos. Já colocamos a otimização. Agora precisamos rodar a nossa validação.

A validação é o algoritmo que vai verificar a base de dados de treino com o que está acontecendo no treinamento, o que está sendo esperado.

Vou inserir um módulo de código aqui que também é da Inception para trabalhar com esse modelo. É um modelo de validação que está pronto e implementado.

Estamos chamando esse modelo de validação na saída da rede. Ele vai mostrar para a gente a quantidade de imagens que foram testadas e a precisão que temos no modelo. Ele vai mostrar para a gente o valor da acurácia.

`⏱ 22:40`

Este algoritmo de validação chama as imagens para a rede que foram treinadas e compara uma imagem que nunca foi treinada com a rede e seus pesos de treinamento.

É como se fosse um exemplo de treinamento:

Quando uma pessoa ensina um aluno, por exemplo, um professor ensina o aluno vários exercícios de matemática. Na hora da prova, para validar o conhecimento do aluno, não podemos passar o mesmo exercício com os mesmos números, porque o aluno decora o exercício. Ele tira de memória, e eu entendo que ele aprendeu, mas ele apenas decorou.

Para uma rede neural é a mesma coisa. Não podemos treinar ela e depois mostrar para a rede o mesmo exemplo, porque ela não vai mostrar se realmente aprendeu ou não.

### Executando a Validação do Modelo

Vou colocar aqui para executar essa parte da validação. Agora, vamos chamar a leitura do modelo, que vai efetivamente rodar na nossa rede.

Vou colocar aqui um novo módulo. Eu chamei o modelo igual a `modelo`. Estamos chamando o nosso modelo de treinamento da Inception.

Em seguida, vou colocar um `device` igual a `torch.device`. A leitura lá do nosso `torch`. Vou colocar aqui a versão `CUDA` e vou colocar um `if` para verificar se eu tenho o `torch.cuda` disponível.

Também vou verificar o caso de não ter o nosso `CUDA` disponível na GPU, então a gente só vai rodar com o `CPU`.

#### Verificação de Dispositivo (CUDA vs. CPU)

O que estamos fazendo aqui nessa verificação? Estou verificando se tem o `CUDA` disponível para a nossa GPU.

*(Interrupção de diálogo)*

*(Continuação da explicação)*

A gente está verificando se tem essa placa ou não.

Nesse caso, estou mostrando para vocês como é a verificação, porque a gente está usando a máquina do Google, e lá obviamente eles têm a GPU para disponibilizar para a gente.

*(Execução do código)*

Teve um erro no `device torch.device CUDA` porque o `if torch.cuda.is_available()` é o que usamos. `else CPU`. Vamos executar aqui.

### Treinamento do Modelo

Agora, o que está faltando é a gente chamar o treino do nosso modelo.

O que vai acontecer? Eu tenho que colocar aqui em ambiente de execução, executar tudo. E aí a gente vai ter o início do nosso treinamento.

Em cada camada, o que está faltando mais?

A gente já colocou a parte de validação, e a gente já colocou a parte do nosso treino. Não está faltando mais nada.

Essa é a nossa estrutura de uma rede neural. A gente está chamando a cada módulo uma função, importando as bibliotecas, definindo a conversão das imagens do dataset para formato tensor, colocando aí uma representação de uma imagem. Cada vez que a gente rodar aqui, ele vai pegar uma imagem de exemplo. Vocês podem ver que tem vários exemplos aqui para a gente rodar.

`⏱ 28:20`

Os números que não conseguimos interpretar muito bem são os do tipo 1 e do tipo 7. Isso ocorre porque os números 7 são feitos de forma tão mal que parecem um 1, e vice-versa.

### Estrutura e Configuração da Rede

Colocamos a estrutura da nossa rede e também incluímos o modelo para treinar e o modelo para conseguirmos fazer a validação.

Além disso, incluímos uma verificação condicional para checar se há a instalação do CUDA. Caso não esteja instalado, o treinamento rodará somente no processador. Vocês podem rodar o treinamento na máquina de vocês, utilizando o Colab, mas isso pode demorar um pouco. Por isso, não vou executar toda a rede aqui.

No entanto, vocês viram que checamos cada módulo, e ele está funcionando perfeitamente. Esta é a primeira implementação em Python de uma rede de Deep Learning para reconhecer dígitos.

### Próximos Passos e Escopo

A ideia é que continuaremos trabalhando com exemplos menores. Embora eu tenha mostrado uma rede de Deep Learning aqui, vamos trabalhar com exemplos menores, implementando:

- Uma rede neural normal (shallow).
- Uma SVM.
- Um algoritmo genético.

O Python, utilizando bibliotecas para machine learning, oferece uma facilidade muito grande em nossa vida. A ideia era mostrar isso dentro do ambiente de colaboração que estamos usando.

Por hoje é isso.

## Relacionado

- [[classificacao-de-dados-e-transferencia-de-conhecimento-em-redes-neurais]]
- [[redes-neurais-artificiais-conceitos-estrutura-e-aplicacoes-em-machine-learning]]
- [[criacao-representatividade-e-tipos-de-datasets-em-machine-learning]]
- [[fundamentos-de-svm-hiperplanos-e-comparacao-com-redes-neurais]]
