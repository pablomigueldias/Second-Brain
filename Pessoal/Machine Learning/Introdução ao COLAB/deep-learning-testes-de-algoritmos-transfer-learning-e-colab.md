---
titulo: "Deep Learning: Testes de Algoritmos, Transfer Learning e Colab"
tags: [machine-learning, redes-neurais-artificiais, algoritmos, ferramentas, dados, ia, otimizacao]
data: 2026-08-27
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 15
conceitos: [Deep Learning, Algoritmos de treinamento, Transfer Learning, Classificação de imagens, Colab, Teste de rede neural, Pesos (de modelo), ImageNet]
---

# Deep Learning: Testes de Algoritmos, Transfer Learning e Colab

> [!resumo] Do que se trata
> A aula demonstra como testar algoritmos de Deep Learning na plataforma Colab, utilizando imagens externas para validação. Explica a aplicação do Transfer Learning para refinar a classificação de dados e corrigir problemas de detecção. Por fim, apresenta o Colab como um ambiente de execução online que facilita o desenvolvimento de projetos de Machine Learning sem a necessidade de hardware potente.

## Para lembrar

- **Para testar algoritmos de Deep Learning, utiliza-se o algoritmo de treinamento que já gerou os pesos, aplicando-o a imagens encontradas na internet.**
- **O Transfer Learning corrige problemas de classificação ao adaptar um modelo pré-treinado para detectar e reconhecer categorias mais específicas de dados.**
- **O Colab é um ambiente de execução online que permite rodar código de Machine Learning independentemente da máquina local, eliminando a necessidade de investir em hardware potente.**
- ⚠ **Um teste de rede neural deve ser realizado com imagens que a rede nunca viu para evitar que o sistema 'decore' as respostas e garantir uma avaliação correta de seu desempenho.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Como realizar testes em algoritmos de Deep Learning com imagens externas?
- O que é Transfer Learning e como ele ajuda a corrigir problemas de classificação?
- Quais as vantagens de usar o Colab para projetos de Machine Learning em comparação com uma máquina local?

## Conceitos

**Deep Learning** · **Algoritmos de treinamento** · **Transfer Learning** · **Classificação de imagens** · **Colab** · **Teste de rede neural** · **Pesos (de modelo)** · **ImageNet**

## Conteúdo

`⏱ 00:00`

Olá, tudo bem? Meu nome é Diego Bruno e hoje a gente vai ver um pouco sobre os testes destes algoritmos de Deep Learning aqui na plataforma do `Collab`.

Para isso, a gente vai usar o algoritmo de treinamento, que já gerou os pesos, e a gente vai testar com imagens encontradas na internet.

Eu vou mostrar como a gente faz isso. Vindo aqui na aba lateral esquerda, eu criei uma pasta. Para criar uma pasta, é só abrir aqui com o botão direito, selecionar `nova pasta` e colocar um nome, por exemplo, `testes`.

Eu já criei uma pasta aqui com o nome `imagens`. Nela, eu coloquei:
- uma imagem que eu salvei do Google, uma imagem dos Beatles;
- uma imagem de carros;
- e uma imagem de `cats and dogs`.

### Testando com Imagens

Eu vou mostrar para vocês que, no nosso `image path`, que é o caminho da nossa imagem, no caso, estamos pegando uma imagem da internet. Porém, eu quero colocar uma imagem carregada pelo meu computador. Então, eu vou passar o caminho da minha imagem.

Qual é o caminho, por exemplo, da imagem dos Beatles? É `./imagens/beatles.jpg`.

Agora, eu vou colocar meu ambiente de execução para executar tudo. Vocês vão ver que ele leu a famosa imagem dos Beatles atravessando a rua. Porém, deu um erro para mim: essa imagem tem uma dimensão que não é aceita pela rede. Eu posso fazer um algoritmo para tratar esse problema, mas não é o objetivo da nossa aula agora.

Então, eu vou trocar a imagem. Vou trocar essa imagem dos Beatles e vou colocar a nossa imagem dos carros, tudo minúsculo.

Vou executar o algoritmo no ambiente de execução, executando tudo. Ele vai carregar a minha imagem dos carros e depois vai mostrar também o resultado da minha imagem classificada entre os objetos detectados.

Vocês conseguem ver que o algoritmo conseguiu detectar os carros e, além de detectar os carros, ele conseguiu também detectar as pessoas que estão dentro dos carros.

Existe um problema no nosso treinamento, mostrando o resultado que estamos tendo. Vocês podem ver que os carros foram classificados como caminhões. O que acontece é que, nesse conjunto de dados, tudo que é veículo foi colocado como uma única classe. Isso gerou esse problema.

### Corrigindo o Problema com Transfer Learning

Como consigo corrigir esse problema? Fazendo um Transfer Learning.

Eu vou pegar agora:
- uma classe de carros;
- uma classe de ônibus;
- uma classe de caminhão;
- uma classe de motocicleta.

E vou fazer um novo treinamento para detectar e reconhecer os veículos do trânsito por sua categoria.

Por exemplo, para que seria interessante usar essa tarefa? Imagine que eu tenho um sistema numa rodovia para detectar qual carro está acima da velocidade.

Geralmente, a gente tem uma placa de 110 km/h para carro e depois uma um pouco menos para caminhão, geralmente 100 km/h ou 90 km/h. Como eu sei se o veículo que está passando é um caminhão, se é um ônibus, se é um carro, se é uma moto?

Eu coloco uma câmera com um sistema de detecção desse. Se o sistema detectou que o veículo passou acima da velocidade, por exemplo, um veículo passando a 110 km/h.

`⏱ 05:20`

Se o sistema detectou que o carro passou acima da velocidade, sei lá, tem um veículo passando a 110. Então, o meu sistema vai ter que verificar se é um carro ou um caminhão, porque se for um carro, está dentro do limite; se for um caminhão, está acima do limite, certo?

A gente pode ter, por exemplo, essa aplicação ou também outras em que temos ruas onde não podem circular caminhões. Aí, a gente tem um sistema que detecta e, se detectou um caminhão, por exemplo, a gente consegue avaliar também a placa para multar aquele veículo, certo?

### Detecção de Gatos e Cachorros

Eu coloquei também uma outra imagem de gatos e cachorros. Vamos rodar esse algoritmo para essas imagens.

Só vou alterar aqui o caminho para `Cats and Dogs` e vou colocar o algoritmo para executar. Carregou a imagem dos gatinhos e dos cachorros: três cachorros e dois gatos. Agora, vou mostrar o resultado.

Esse cachorro foi detectado e classificado com 99% de acerto. Esse cachorro também, 99% de acerto. Esses dois gatos também, 99% de acerto.

Ah, professor, mas é 99% mesmo para todos? Deve estar dando 199.9989, tem um valor decimal depois da vírgula. Mas, como o algoritmo foi implementado só para mostrar o valor redondo, está dando esses valores.

Vocês podem ver que esse cachorro foi detectado como 72% de certeza para ser um gato, porque é um cachorro diferente, com a cara mais arredondada. Deu ruim para esse animal, um cachorro classificado e detectado como um gato. O resto foi muito bem.

### Novo Teste com Imagem Externa

Vamos tentar fazer outro teste? Vou abrir o Google, vou pegar gatos e cachorros novamente. Vou pegar uma imagem que tenha mais de um animal. Vou salvar essa imagem como `animais` no meu computador.

Agora, vou no meu drive, dentro da pasta `imagens`, e vou colocar essa imagem de `animais`. Vou abri-la e falar de novo que não sou um robô para o sistema.

Agora, tenho essa outra imagem, que é a imagem de `animais`. Vou mudar o nome da imagem que carreguei. Estou aqui com a imagem `Cats and Dogs`. Vou colocar essa imagem que coloquei na pasta, que se chama `animais.jpeg`.

Vou colocar um ambiente de execução, executar tudo. Carregou a minha imagem do gatinho e do cachorro, e agora o algoritmo vai apresentar a predição.

Detecto esse cachorro com 98% de certeza. O rótulo do gato ficou recortado, mas está mostrando 80% de certeza, porque vocês podem ver que o cachorro está um pouquinho na frente do gato, pode ser que isso tenha atrapalhado.

Aqui, a gente tem um ambiente rodando essas imagens. Eu já tenho um treinamento e estou executando o meu teste. O teste foi com a imagem que peguei do Google. Essas imagens não participaram do treinamento da rede, certo?

### Como um Teste é Realizado

Lembrando de como é feito um teste, é como se um professor aplicasse uma prova. Na sala de aula, o professor resolve uns exercícios de exemplo. No dia da prova, o professor tem que dar um exercício diferente.

Por quê? Porque ele é chato? Não. Porque senão você decora o exercício e na prova você tira 10. E não é isso que a gente...

`⏱ 11:00`

E não é isso que a gente quer. Se a gente mostrar a mesma imagem do treinamento, o sistema decorou aquela imagem e vai acertar com 100%, mas não é a forma correta, certo? Para testar, a gente tem que colocar uma imagem que a rede nunca viu.

### ImageNet

Vou mostrar para vocês um pouco mais do ImageNet. A gente falou do ImageNet, mas eu não mostrei como é a base de dados deles. Colocando aqui, por exemplo, no Google Imagens, o ImageNet é isso aqui: várias classes de imagens, com vários exemplos.

Se eu não me engano, são um milhão de imagens. É muita imagem: um milhão de imagens para treinamento e cem mil imagens para teste. É uma base de dados bem grande.

Esse desafio testa vários algoritmos que as pessoas vão desenvolvendo. A gente está rodando aqui um algoritmo que é baseado no sistema do ImageNet, na base de dados do ImageNet. Foi pré-treinado. A gente rodou um novo treinamento, fez o `Transfer Learning`, e agora a gente testou para gato e cachorro e está funcionando.

### O que é o Colab

A ideia do Colab é que a gente consiga rodar nosso código onde a gente for. É independente da máquina que vocês estão usando. Não precisa investir em máquina.

Ah, eu vou fazer esse curso de Machine Learning. Vou ter que investir num computador potente? Não precisa. A gente vai usar ambiente de execução online. Isso vai facilitar muito vocês trabalharem nos projetos e também vai facilitar a minha parte, porque eu consigo compartilhar o meu código com vocês.

A ideia até o momento foi mostrar para vocês o que é o Colab. A gente não desenvolveu nada do zero aqui, porém, a gente vai desenvolver os nossos projetos de Machine Learning aqui dentro do Colab.

### Colab vs. Máquina Local

Alguns outros projetos a gente vai executar na máquina, instalando tudo, porque às vezes a gente precisa disso.

Às vezes a gente vai trabalhar num grupo de pesquisa que investiu numa máquina super potente. Aí você vai falar: "Ah, não vou usar, vou usar o Colab". Não é assim. Porque uma máquina dedicada para o teu projeto é bem melhor do que a gente usar o processamento em nuvem.

Porém, quando a gente não tem recurso para isso, a gente acaba usando o Colab, que ajuda muito o nosso projeto.

### Próximos Passos

Nosso conteúdo sobre teste em imagens no Colab terminou aqui. A gente vai ver nos nossos próximos conteúdos os algoritmos desenvolvidos nessa plataforma do zero.

## Relacionado

- [[criacao-representatividade-e-tipos-de-datasets-em-machine-learning]]
- [[visualizacao-de-dados-e-regressao-com-matplotlib-e-scikit-learn]]
- [[classificacao-de-dados-e-transferencia-de-conhecimento-em-redes-neurais]]
- [[machine-learning-frameworks-e-ambientes-de-desenvolvimento-tensorflow-pytorch-ke]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Um abraço para vocês e até a próxima!

</details>
