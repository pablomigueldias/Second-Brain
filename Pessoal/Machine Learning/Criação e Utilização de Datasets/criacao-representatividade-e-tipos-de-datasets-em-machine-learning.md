---
titulo: "Criação, Representatividade e Tipos de Datasets em Machine Learning"
tags: [machine-learning, dados, ia, redes-neurais-artificiais, conceitos, fundamentos]
data: 2026-08-22
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 28
conceitos: [Dataset, Representatividade, Classificação de imagens, Detecção de objetos, Segmentação de imagens, MNIST, ImageNet]
---

# Criação, Representatividade e Tipos de Datasets em Machine Learning

> [!resumo] Do que se trata
> Apresenta a definição e a importância da representatividade e da variabilidade de amostras em datasets para o treinamento eficaz de modelos de inteligência artificial. Explora as diferenças estruturais entre bases de dados para classificação, detecção com caixas delimitadoras e segmentação sem fundo. Detalha exemplos clássicos de bases públicas, como MNIST e ImageNet, além das diretrizes para estruturar e coletar dados próprios.

## Para lembrar

- **Um dataset representativo exige ampla variedade de características, como diferentes raças, cores, posições e expressões, para garantir que o modelo generalize com alta confiança.**
- **Para tarefas de classificação simples, a organização pode ser feita separando arquivos em pastas nomeadas por classe, enquanto a detecção exige caixas delimitadoras e a segmentação requer o contorno exato do objeto isolado do fundo.**
- **O MNIST é uma base de dados clássica de dígitos manuscritos amplamente usada em tarefas de transcrição e reconhecimento óptico de caracteres.**
- **O ImageNet é uma base de referência em visão computacional contendo milhares de categorias de objetos para ranqueamento e validação de algoritmos de inteligência artificial.**

## O que esta nota responde

- O que torna um dataset verdadeiramente representativo para o treinamento de um modelo?
- Qual é a diferença na anotação de dados entre classificação, detecção e segmentação de imagens?
- Quais são os principais datasets públicos de referência para visão computacional e OCR?

## Conceitos

**Dataset** · **Representatividade** · **Classificação de imagens** · **Detecção de objetos** · **Segmentação de imagens** · **MNIST** · **ImageNet**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e hoje vamos ver um conteúdo relacionado a `data sets`.

Os `data sets` são conjuntos de dados representativos, que nos permitem classificar problemas por meio de imagens, por meio de valores numéricos e por aí vai. Vamos ver um conteúdo que abrange teoria e prática. Já vimos alguns *spoilers* em nossas aulas sobre `datasets` e a importância deles. Mas agora teremos um conteúdo focado nisso, principalmente também em como criar uma base de dados e em como usar uma base de dados disponível gratuitamente.

### O que é um Dataset?

Um `dataset` é um conjunto de dados que representa muito bem um problema que estamos querendo tratar.

Vamos dar um exemplo sobre classificação de gato e cachorro. Não adianta eu pegar uma imagem de um cachorro, por exemplo, e colocar apenas 100 imagens de Pinscher e 100 imagens de gato Siamês. É uma boa quantidade de imagens? É, é uma boa quantidade. Porém, eu não estou gerando uma base de dados representativa para o meu problema.

Por quê? Porque eu tenho infinitas outras raças de gato e cachorro. Se eu colocar apenas uma, eu não vou ter uma base de dados que representa bem o meu problema. Eu preciso colocar várias raças de cachorro — não precisa ser todas, mas precisa ser uma boa quantidade delas. Eu preciso colocar várias raças de gato também, com diferentes cores.

Um `dataset` deve representar muito bem o meu problema. Não adianta eu colocar várias fotos de um mesmo tipo de animal, uma única raça, uma única cor, pois isso não vai representar bem o meu problema.

Se eu treinar com gatos e cachorros Pinscher, quando eu mostrar um Poodle, o modelo vai até definir que é um cachorro, mas com uma certeza baixa. E não é isso que a gente espera de um modelo de Machine Learning.

Um `dataset` é a base para que tenhamos um modelo de inteligência artificial que foi treinado com base no modelo de Machine Learning, com uma base de dados bem definida, que representa bem o meu problema. Sem isso, não conseguimos obter o treinamento de um modelo de Machine Learning, nem conseguimos gerar uma inteligência.

### Representatividade e Classificação

Se pegarmos o problema do gato e do cachorro, a minha rede — aqui estou dizendo uma rede neural, mas poderia ser outro método de classificação, como uma SVM ou outro método — quando receber uma imagem, ela vai ter que classificar essa imagem por meio do aprendizado que ela teve.

É muito importante que a nossa base de conhecimento, a nossa base de dados, o nosso `dataset`, tenha uma representação bem ampla dos meus tipos de animais que representam a minha base.

Dizendo como devem ser as nossas amostras: não adianta também eu fazer variações de raças e de cores dos animais. Eu posso também gerar imagens com posicionamento e um comportamento diferente.

Por exemplo, vou treinar o meu celular para reconhecer a minha face. Ele vai pedir para eu tirar várias fotos e tentar alterar a posição do meu rosto, porque ele pede para olhar para a esquerda e para a direita.

`⏱ 05:00`

### Importância da Variação nos Dados de Treinamento

Quando eu faço isso, o sistema vai sendo alimentado com imagens do meu rosto em posições diferentes. Ele vai pedir para alterar a posição na hora de capturar a face, registrando diferentes variações:

- Sorrindo ou sério;
- Olhos fechados ou olhos abertos;
- Cabeça abaixada ou cabeça erguida.

Quando o sistema for reconhecer a face no dia a dia, na prática, nem sempre o rosto vai estar alinhado perfeitamente para a câmera. Faz sentido ter posições diferentes na base de dados.

Do mesmo modo, ao treinar um sistema, faz sentido ter:

- Foto de gato em cima da mesa;
- Foto de gato em cima da árvore;
- Foto de gato deitado;
- Foto de gato pulando;
- Foto de cachorro no colo da dona;
- Foto de cachorro nadando;
- Foto de cachorro comendo.

Quando o sistema estiver funcionando e for apontado para um cachorro comendo, se nunca viu aquela situação na base de treinamento, ele pode até reconhecer o cachorro, mas com uma certeza menor pela posição diferente. 

Se o sistema foi treinado apenas com imagens de cachorro com a boca fechada, ele não sabe como é um cachorro de boca aberta. Isso atrapalha o treinamento, porque as características de um cachorro com a boca aberta não foram representadas. 

Quanto mais variações houver na base de dados, melhor vai ser o treinamento.

### Tamanho da Base e Custo Computacional

Não faz sentido ter uma base de dados com 10 imagens de gato e 10 imagens de cachorro. É muito pouco. O sistema até consegue treinar, porém o treinamento não vai ser eficiente e a acurácia e a certeza do sistema serão muito baixas. É preciso ter uma base de dados suficiente.

No caso de gato e cachorro, alguns estudos mostram que a partir de 100 a 200 imagens já se tem uma base suficiente. Quanto mais aumentar a base de dados, melhor. Com 1.000 imagens de gato e 1.000 imagens de cachorro, o sistema terá uma acurácia e certeza maiores, só que com um custo computacional mais elevado.

Quanto mais a base de dados é aumentada, mais aumenta a precisão e a certeza do sistema, mas também aumentam:

- A quantidade de processamento;
- A quantidade de tempo;
- A quantidade de memória.

A quantidade de imagens é diretamente proporcional ao volume de custo computacional e ao custo de tempo.

### Treinamento Offline e Criação de `dataset`

O treinamento é uma fase offline do sistema. Sendo offline, às vezes o tempo não é tão influente no problema. É possível ter um sistema que demore mais para ser treinado — um dia, dois dias, uma semana —, mas que apresente um bom [inaudível], se comparado a um sistema com treinamento muito rápido que não gera um bom resultado.

Para gerar uma base de dados, um `dataset`, o processo é feito de forma bem fácil. Por exemplo, eu quero

`⏱ 09:40`

Para criar um *dataset* de gato — um conjunto de imagens de gato — e um conjunto de imagens de cachorro, eu não preciso tirar fotos com o meu celular. Eu posso baixar imagens do Google. Eu baixo essas imagens do Google e crio a minha base de dados.

Isso é bem tranquilo porque, se você pegar a base de dados do Google, ela terá muita imagem de gato, de cachorro, de diferentes raças, então se torna fácil.

Eu posso até fazer um *script* que vai baixar as imagens automaticamente para mim. Basta digitar a chave de busca, por exemplo, `gato semessa`. Aí o sistema vai lá e baixa mil imagens de `gato semessa`. Pronto. Eu posso fazer dessa forma. Eu vou gravando as minhas imagens de gatos dentro de uma pastinha e de cachorro dentro de outra pastinha, e é assim que funciona.

### Base de Dados para Detecção

Uma outra base de dados que utilizamos bastante é a base de dados para detecção. Essa base de dados é mais complexa de ser feita.

Porque essa base de dados não basta eu colocar uma imagem dentro de uma pasta e apontar para ela dizendo que tem, por exemplo, um gato ou cachorro. Eu tenho que rotular a imagem com uma ferramenta de rotulação específica. Existem várias gratuitas para isso.

Mas eu tenho que fazer uma região que delimita a minha imagem. Não é só simplesmente criar uma pastinha e colocar a imagem dentro.

Por exemplo, aqui eu tenho que dizer para a minha rede no treinamento onde que está a placa de 20 km por hora. Eu tenho que circular ela. E aí a rede vai receber a imagem e vai receber a coordenada X e Y dessa região da placa.

Isso vale para a placa de pedestres, para estudantes. Eu tenho que mostrar essa imagem toda, que tem todas essas placas, e eu tenho que dar a coordenada X e Y de onde está essa placa.

Portanto, é um treinamento que exige uma base de dados mais trabalhosa. Eu vou capturar essas imagens com uma câmera e depois eu vou ter que rotular com essas regiões que a gente chama de *bounding box* — regiões delimitadoras. E aí a gente vai ter que ter um trabalho para fazer isso.

O resultado de uma rede de detecção vai gerar exatamente onde está a placa. Ele não vai pegar essa imagem toda e falar: "Nessa imagem que tem uma estrada, tem um acostamento, tem árvores. Nessa imagem toda tem uma placa de 50 km por hora." Mas onde está, eu não sei.

Não é igual a uma rede de classificação. Se tiver uma imagem aí de uma placa, se tiver um gato, ela vai dizer: "Ó, na imagem tem um gato, na imagem tem um cachorro." Mas onde ela não vai dizer?

A rede de detecção é diferente. Ela vai dizer para a gente onde que está o objeto que ela detectou e ela vai também fazer esse quadrado, que é a região delimitadora, o *bounding box*, sobre o objeto e mostrar para a gente. É aqui que está o problema.

No meu trabalho de doutorado, eu trabalhei com isso: detectar a placa de trânsito ou semáforo para o veículo. Eu tenho que falar para o veículo: "Veículo, onde está a sinalização?" para ele saber qual a decisão que ele vai tomar.

Por exemplo, eu detectei um semáforo vermelho, mas é para a via que eu estou passando ou é para a via de cruzamento? Para quem é que está verde e para quem está vermelho? Eu preciso saber qual a posição do semáforo.

`⏱ 14:20`

### Imagens de Detecção e Segmentação

Os algoritmos e as redes de detecção trabalham com imagens rotuladas, algo que é mais difícil e trabalhoso de criar. 

Existem também as redes que trabalham com imagens de segmentação, cujo processo é ainda mais complexo. Nelas, não basta apenas desenhar um quadrado em volta do objeto. É necessário ir até a imagem — como se estivesse utilizando o pincel do Paint — e pintar todo o objeto. 

Se houver um cachorro e um gato na imagem, por exemplo, não basta apenas contorná-los com um quadrado (`bounding box`). É preciso pintar cada um com precisão para indicar à rede que a mancha azul-escura representa o cachorro, a mancha azul-clara representa o gato e o fundo branco representa o *background* (o fundo da imagem que não interessa para a aplicação).

Criar uma base de dados de segmentação exige muito esforço. O motivo para criá-la dessa forma é que, em certos casos, é necessário localizar o objeto e isolá-lo completamente do fundo. Ao detectar uma placa de 50 km/h, por exemplo, dentro do quadrado delimitador não fica apenas a placa: há também parte do fundo, um trecho de pista e galhos de árvore. Para determinados sistemas, isso não é o ideal. Para que o algoritmo consiga deletar o fundo, a imagem precisa ser segmentada na base de dados, permitindo que a resposta final da rede seja o objeto perfeitamente contornado.

### Bases de Dados de Dígitos e Reconhecimento de Imagens

Há também bases de dados voltadas para dígitos, como o `MNIST`, que é uma base de dados com números manuscritos.

A utilidade de uma base como essa se aplica à transcrição de documentos: ao trabalhar com cartas ou livros escritos à mão, evita-se o esforço humano de ler todo o material e digitá-lo no computador. Para isso, executa-se um algoritmo inteligente, uma rede neural ou um algoritmo baseado em reconhecimento de imagens que percorre o texto e reconhece as letras e os números.

### Aplicações Práticas: Google Tradutor e Captcha

No Google Tradutor, por exemplo, é possível tirar uma foto da capa de um livro ou de uma carta e selecionar o trecho desejado, ou o próprio aplicativo faz o enquadramento automático dependendo da resolução da imagem. Ao fotografar uma frase em inglês escrita na lousa pelo professor, o sistema processa a imagem e realiza a tradução executando uma IA sobre o texto. Para viabilizar esse processo, o sistema utiliza uma base de dados contendo palavras e números manuscritos para transcrever a resposta.

Antigamente, a digitação de documentos exigia a contratação de profissionais digitadores; atualmente, esse processo ocorre de forma automática.

Outro exemplo prático são os sistemas de Captcha. Ao acessar determinados sites, o sistema apresenta o recorte de uma palavra extraída de um livro para que o usuário a digite e comprove que não é um robô. Ao exibir esse mesmo recorte para diversos usuários simultaneamente, o sistema utiliza essas respostas para digitalizar o conteúdo dos livros.

`⏱ 19:00`

E isso é bem legal porque é um *double check* com várias pessoas para verificar se todo mundo digitou certo. Aí ele tem a certeza de que aquela palavra é aquilo mesmo e transcreve uma palavra já para o livro. O sistema está ali reescrevendo, certo?

### Bases de Dados Disponíveis

Temos várias bases de dados disponíveis. Podemos usar essas bases de dados para treinar o nosso sistema.

Existem diversas fontes, como:

- TensorFlow
- Base de dados do Google
- Amazon
- Kaggle
- Bases de dados governamentais

Muitas vezes, não precisamos criar uma base de dados, um *dataset*. Conseguimos essa base pronta. Na maioria dos casos, já existe alguma base que alguém fez.

### Quando Criar um Dataset

Há vezes em que não há base de dados pronta e precisamos criar a nossa.

Eu trabalhei em um problema uma vez que precisávamos detectar o bicho mineiro, que é uma praga do café. Não havia base de dados pronta. Tivemos que ir lá pegar uma especialista em café, e ela veio nos mostrar quase imagens que tinham praga do café. A gente ia lá criando o balde, o *inbox*, o quadradinho para rotular. Fizemos isso, acho que para duas mil imagens. Treinamos o sistema e ele funcionou muito bem.

É assim que funciona. Às vezes, temos que criar a nossa base de dados porque ela não existe.

### Como Escolher a Base de Dados

Como escolher a base de dados? Qual a base de dados melhor?

O exemplo da Praga do Café, do bicho mineiro, é... A gente tentou procurar, não achou, não tinha nada pronto, a gente criou a nossa base.

Mas haverá situações em que vocês vão encontrar uma base pronta. Então, como escolher essa base?

É lendo sobre ela, lendo artigos que utilizaram ela. Às vezes, tem um *ranking* sobre essas imagens.

#### Exemplos de Bases de Dados

**1. ImageNet**
Se vocês procurarem o `ImageNet`, é uma base de dados que tem mil objetos: caneca, vaso sanitário, pente, controle de TV, notebook. É uma base de dados muito conhecida na área de IA. Se você olhar a base de dados deles, tem lá milhares de pessoas usando e ranqueando seus algoritmos. Se tem tanta gente usando, é uma base de dados boa. O `ImageNet` é uma base de dados bem tradicional aí na área de reconhecimento de imagens.

**2. TensorFlow**
Podemos usar também, por exemplo, uma base de dados do TensorFlow. Aqui no TensorFlow tem esse exemplo que é clássico na área, que é o reconhecimento de gato e cachorro. Eu sempre dou esse exemplo porque é um exemplo clássico para IA.

Você vai lá e tem a sua base de dados pronta, certo? É só baixar e rodar seu algoritmo de treinamento para ver como ele se comporta.

**3. Bases de Dados Numéricas**
A gente também tem bases de dados numéricas, e não somente com imagens. Meus exemplos até agora são todos com imagens porque é algo mais fácil de a gente enxergar. Se eu fico mostrando o exemplo numérico, vocês vão ficar meio perdidos.

Mas também há bases de dados numéricas, por exemplo, a base de dados por meio do nosso CPF. O CPF de cada pessoa vai gerar um *score*, que é o valor que aquela pessoa tem em relação às compras que ela faça, às dívidas que ela tem. Aí um banco consegue ver esse valor pelo CPF da pessoa e não vai disponibilizar um cartão de crédito com limite.

`⏱ 23:40`

...maior ou menor, declarar se essa pessoa é um bom cliente ou não, ou disponibilizar um financiamento.

Nesse contexto, o banco de dados por meio do CPF é muito importante, principalmente para essas situações.

Se, por exemplo, você entrar no aplicativo do Serasa, ele vai gerar uma pontuação que temos por meio do nosso CPF. Com isso, você consegue enxergar o porquê de sua pontuação ser baixa. Às vezes, você tem dívidas que não foram pagas, e ele te indica como fazer um acordo.

A base de dados por meio do CPF gera um universo de valores — quanto você compra, quanto você paga em dia, quanto você deve — e tudo isso, pelo número do CPF, é utilizado por várias empresas e bancos para tratar o cliente de forma única.

***

### Atividade Prática: Criação de Base de Dados

Aqui, no final deste módulo do nosso curso, teremos uma atividade relacionada à criação de uma base de dados.

Para ilustrar, eu coloquei um exemplo onde você vai criar uma rede para classificar o Debb e o Lloyd. Você deve:

1.  Entrar no Google e baixar as imagens deles.
2.  Definir como nossa atividade: 200 imagens para cada amostra.
3.  Pegar 200 imagens do Debb e 200 imagens do Lloyd.
4.  Criar um *dataset* com essas imagens e subir no GitHub.

#### Estrutura do Dataset

O *dataset* que vocês vão criar deve ser organizado em um GitHub com duas pastinhas:

*   Uma pastinha com a classe 1 (que pode ser o Debb).
*   Uma pastinha 2 (que pode ser o Lloyd).

**Exemplos de Bases de Dados:**

*   Pode ser uma pastinha com gato e outra com cachorro.
*   Você também pode criar sua base de dados de uma forma mais otimizada:
    *   Pegar seu celular e tirar 200 fotos suas e 200 fotos do seu irmão, da sua esposa, da sua namorada.

Durante as próximas aulas, usaremos essas imagens para rodar um algoritmo de treinamento, que irá reconhecer:

*   Você e sua namorada.
*   Você e sua esposa.
*   Você e seu irmão.
*   O Debb e o Lloyd.
*   Um gato e um cachorro.

Vamos rodar uma rede para reconhecer essas imagens. A escolha é de vocês: baixar do Google, tirar fotos, ou escolher quais serão as classes.

***

O nosso conteúdo por hoje é esse. Muito obrigado e até uma próxima.

## Relacionado

- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
- [[classificacao-de-dados-e-transferencia-de-conhecimento-em-redes-neurais]]
- [[01 - Conceitos Banco de Dados]]
- [[fundamentos-de-svm-hiperplanos-e-comparacao-com-redes-neurais]]
