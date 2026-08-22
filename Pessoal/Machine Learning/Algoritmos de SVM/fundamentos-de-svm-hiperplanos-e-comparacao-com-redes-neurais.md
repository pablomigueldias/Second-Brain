---
titulo: "Fundamentos de SVM, Hiperplanos e Comparação com Redes Neurais"
tags: [machine-learning, algoritmos, conceitos, fundamentos, redes-neurais-artificiais, otimizacao]
data: 2026-08-22
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 24
conceitos: [Máquinas de Vetores de Suporte (SVM), Aprendizado Supervisionado, Hiperplano de Separação, Fronteira de Decisão, Maximização de Margem, Mínimo Global, Outliers]
---

# Fundamentos de SVM, Hiperplanos e Comparação com Redes Neurais

> [!resumo] Do que se trata
> Apresenta o funcionamento das Máquinas de Vetores de Suporte (SVM) como um modelo discriminativo de aprendizado supervisionado para classificação de dados. Compara a definição de hiperplanos e maximização de margens na SVM com o processo de minimização de erro até o mínimo global em Redes Neurais Artificiais. Explica a construção da fronteira de decisão, o estabelecimento de margens de segurança e o tratamento de cenários com separação não linear e outliers.

## Para lembrar

- **A SVM é um modelo supervisionado discriminativo que busca encontrar um hiperplano divisor ótimo maximizando a distância entre as classes.**
- **A diferença central entre os modelos é que a SVM posiciona um hiperplano com margens ótimas, enquanto a Rede Neural foca em reduzir o erro contínuo até alcançar o mínimo global.**
- **A margem de uma SVM é calculada a partir da distância entre a fronteira de decisão e os pontos amostrais mais próximos de cada classe.**
- **Maximizar a margem de segurança do hiperplano reduz o risco de classificação errada para elementos fronteiriços com alta similaridade entre classes diferentes.**

## O que esta nota responde

- Qual é a diferença fundamental no treinamento de uma SVM em comparação a uma Rede Neural Artificial?
- O que é a margem de segurança de um hiperplano e por que a SVM busca maximizá-la?
- Como a SVM atua na classificação de dados dentro do aprendizado supervisionado?

## Conceitos

**Máquinas de Vetores de Suporte (SVM)** · **Aprendizado Supervisionado** · **Hiperplano de Separação** · **Fronteira de Decisão** · **Maximização de Margem** · **Mínimo Global** · **Outliers**

## Conteúdo

`⏱ 00:00`

Meu nome é Diego Bruno e hoje vamos ver um conteúdo muito importante para a área de Machine Learning: os modelos de aprendizado baseados em Máquinas de Vetores de Suporte (*Support Vector Machines*). 

Este cenário é muito importante dentro do Machine Learning porque é um método muito utilizado e também muito robusto, principalmente em situações onde alguma amostra dentro da nossa população tem uma diferença muito grande comparada à sua classe. Vamos ver melhor esse contexto, mas esse tipo de algoritmo é bem parecido com as redes neurais artificiais, porém, na prática, o funcionamento tem algumas diferenças que vamos discutir.

### O que são Máquinas de Vetores de Suporte (SVM)?

Uma Máquina de Vetores de Suporte, ou pela sigla em inglês, SVM, é um algoritmo que terá uma base de treinamento para classificar amostras que têm uma diferença considerável, criando um hiperplano entre essas amostras. 

A criação desse hiperplano dividindo duas classes, como na imagem, é a base desse tipo de algoritmo. Nossa principal tarefa é definir esse plano que vai dividir as classes. O resultado esperado desse tipo de algoritmo é essa divisão das classes.

### SVM e o Aprendizado Supervisionado

Alguns podem pensar que isso é muito fácil, mas o algoritmo precisa fazer isso da melhor forma possível. Para entender isso, vamos primeiro saber o que são SVMs. Primeiramente, vamos trabalhar com um algoritmo supervisionado. 

Um algoritmo supervisionado é aquele onde o modelo de treinamento recebe uma entrada e um rótulo de saída para essa entrada. Para imaginar, pense em quando estou ensinando uma criança o que é um gato e o que é um cachorro. Eu mostro para a criança a foto de um gato e digo: "É um gato". Eu tenho uma entrada, que é a informação de uma imagem, e eu tenho um rótulo dizendo para a criança: "É um gato". Isso é diferente de pegar várias fotos e ir mostrando para a criança sem dizer o que é. 

O nosso método baseado em SVM mostra a entrada e fala o que é na saída, criando uma relação e aprendendo de uma forma que chamamos de aprendizado supervisionado. 

Nesse processo, teremos:
- Uma entrada com valores dentro de um espaço de busca;
- As características dessas amostras.

Por meio dessas características, conseguimos diferenciar cada objeto de forma supervisionada, criando um plano que divide as nossas duas classes.

### Comparação com Redes Neurais

É verdade que é muito parecido com uma rede neural artificial, mas essa aplicação tem algumas diferenças que vamos comentar logo a seguir.

### Tipos de Aprendizagem

Eu dei um *spoiler* sobre aprendizado supervisionado e não supervisionado. Mas o que seria um aprendizado não supervisionado? 

O aprendizado não supervisionado é quando eu quero mostrar uma base de dados em que eu não tenho rótulos e, por meio dessa base de dados, eu tenho que ser possível de aprender. 

Vou dar um exemplo: vou separar 500 imagens, incluindo fotos de gato e cachorro, e vou dar para uma criança que já tem uma certa inteligência separar essas imagens por meio de duas classes: classe gatos e classe cachorros. Mas, nesse aprendizado, ela vai ter que relacionar o que está acontecendo ali. 

Ela vai olhar para a imagem desse gato (que ela não sabe que é um gato, sendo um animal qualquer para ela), olhar para o outro gato e dizer: "Esses animais se parecem. Eles têm bigode, orelha pontuda, têm o rabo erguido". Essas relações trazem uma união dentro de um *cluster* de objetos. 

Vamos imaginar que os nossos gatos são essas bolinhas verdes. Ela vai continuar olhando fotos de cachorro e gato e vai começar a relacionar que tem um outro tipo de animal, que é o cachorro. Ela vai ver: "Esse cachorro aqui da raça Pinscher é bem parecido com esse aqui que é um Rottweiler, um Doberman". Ela começa: "Bom, isso aqui não é aquela primeira classe que eu defini, que é a classe gato". 

Levando a princípio que a criança não sabe o que é cada classe, ela vai pegar um monte de imagens e vai separar as imagens pela relação que elas têm. Não é um treinamento supervisionado, ninguém está dizendo para ela o que é; ela está tendo que separar. Eu só vou pedir para ela: "Separe para mim esses objetos em duas classes. Você vai fazer um montinho de um tipo e um montinho de outro". Ela tem que se virar. Isso é um treinamento não supervisionado.

É isso que acontece quando a gente aplica esse tipo de algoritmo em dados computacionais. Os dados têm as suas características e a gente tem que criar *clusters*. O que são *clusters*? Pontos centralizados onde as minhas amostras vão se agrupando pela similaridade de características. 

Eu criei um *cluster* que é uma cruzinha verde, uma cruzinha vermelha e uma cruzinha azul, e os objetos que são próximos e parecidos vão se aglomerando. No final, eu tenho a minha classificação de três classes sem saber o que eu tenho de rótulo, sem ter etiquetado o que é isso. Igual ao exemplo da criança: ela vai ter um montinho de foto de cachorro e um montinho de foto de gato, mas ela não sabe o que é, ela só classificou em duas classes.

Falando do treinamento supervisionado, um algoritmo supervisionado já é diferente. Eu vou mostrar para a criança as imagens e vou dizer para ela o que é. Vou pegar esse mesmo conjunto de imagens e vou mostrar para ela: "Olha, filha, está vendo essa foto? Aqui é um gato". Vou mostrar outro: "Outro gato". Vou mostrar um cachorro: "Aqui é um cachorro, não é gato agora". Mostro outro cachorro, outro cachorro, outro gato, outro gato, outro cachorro. E digo para ela o que é cada amostra. 

O aprendizado dela é um aprendizado mais robusto, porque não é um aprendizado às cegas. Ela está sendo treinada por meio de exemplos que são rotulados. 

Nós temos:
- A entrada dos dados;
- A interpretação dos resultados (que é a comparação da entrada com a saída);
- A aplicação do nosso algoritmo;
- O processamento desses dados;
- As saídas, que são as respostas do nosso sistema.

Um algoritmo supervisionado vai ter, com seus algoritmos, a relação de uma saída com a entrada da base de dados, contendo um rótulo, da mesma forma dada no exemplo de ensinar uma criança.

`⏱ 10:20`

### Aprendizado Supervisionado e Rótulos

Ao mostrar uma imagem e indicar o que há nela, essa indicação é o rótulo. 

Uma rede neural funciona assim, e uma SVM também funciona assim: ao mostrar a imagem, é necessário ter um nome associado dizendo o que está presente naquela imagem. 

No aprendizado não supervisionado, a imagem é apresentada sem o nome e sem o rótulo.

### Comparação entre Redes Neurais e SVM

Existe uma relação muito forte entre uma rede neural artificial e uma SVM. Em termos de algoritmo, o funcionamento é bastante similar: o algoritmo analisa a entrada e, havendo um rótulo, realiza o treinamento com esse dado. 

Na prática, o principal fator de diferença é o modo de estabelecer o hiperplano.

### Hiperplano e Otimização de Margens na SVM

Em uma SVM, o foco é estabelecer o hiperplano otimizando as margens. 

O hiperplano faz a divisão em um ponto onde não fica nenhuma amostra azul do lado da vermelha e nenhuma amostra vermelha do lado da azul, mantendo uma certa distância entre os clusters de objetos para obter uma divisão perfeita. 

A SVM busca uma classificação em que fique muito bem definido o limite tanto da classe vermelha quanto da classe azul, permitindo que uma nova amostra seja classificada de forma correta ao chegar.

### O Mínimo Global nas Redes Neurais

Uma rede neural busca sempre o mínimo global. Ela treina continuamente até conseguir abaixar o valor do erro. 

Durante o treinamento de uma rede neural, busca-se alcançar acurácias de 90%, 95% ou 98%. O ideal seria atingir 100%, tentando chegar o mais próximo possível dessa marca. Contudo, devido às características da base de dados e do dataset, isso pode não ser viável. O treinamento deve ser interrompido ao atingir o mínimo global, que é o menor nível de erro dentro do treinamento global.

A diferença fundamental consiste em:
- **SVM:** busca dividir com precisão o hiperplano, traçando uma reta bem posicionada;
- **Rede Neural:** busca tratar o cenário reduzindo o erro do treinamento de forma contínua até o limite do mínimo global.

### Fronteira de Decisão

O resultado esperado de uma SVM é uma fronteira de decisão gerada por meio do hiperplano, dividindo as amostras. 

Trata-se de um modelo discriminativo, projetado para discriminar as amostras de forma precisa, otimizando ao máximo as margens da divisão dessa fronteira. A margem é definida como a distância entre a fronteira e as amostras — considerando, por exemplo, o ponto em azul mais próximo do hiperplano e da reta.

`⏱ 15:40`

É o nosso limite, é a nossa margem. Se pegarmos essa bolinha vermelha que está mais próxima da nossa reta, ela é o nosso limite. Vemos que ficou uma margem bem parecida dos dois lados, havendo uma decisão bem ao centro. É isso que se busca em uma SVM ao máximo.

Por que vetores? Por que máquina de vetores e de onde vem esse nome? Os vetores de suporte são simplesmente as coordenadas que temos da observação individual de cada ponto. 

O algoritmo não vai simplesmente tentar traçar uma reta no meio. Ele vai gerar vetores entre cada objeto individual e um indivíduo da outra classe. Uma SVM busca a fronteira que melhor separa as duas classes e, para isso, vai usar esses vetores de comparação individual. Por isso o nome Máquina de Vetores de Suporte. Teremos uma boa divisão entre os nossos elementos; é basicamente isso que ela busca. Parece algo complexo teoricamente, mas na prática o objetivo é bem simples.

### Desenvolvimento da Hipótese e Escolha de Hiperplanos

Como desenvolvemos essa estrutura e qual é o objetivo desse algoritmo, falando de forma matemática? É o desenvolvimento da hipótese.

Aqui temos três hiperplanos: o A, o B e o C. Qual é o nosso hiperplano certo para classificar a estrela e o círculo? 
- O hiperplano A não está certo;
- O hiperplano C também não está, pois está cortando a amostra no meio;
- O hiperplano B está correto e adequado.

Se tivermos que escolher, escolheremos o hiperplano B.

Em outro caso, temos também três hiperplanos: A, B e C, e todos dividem as classes. Todos estão satisfazendo a condição: tanto A, B quanto C estão dividindo as classes de forma correta. Mas qual é o melhor?

O melhor é o C, porque ele está deixando uma margem de segurança entre as nossas duas classes. Quando fazemos isso, obtemos a possibilidade de uma classificação melhor, pois temos uma região que é uma margem de segurança. 

Essa margem de segurança de treinamento vai permitir lidar com amostras que são mais parecidas entre si. Imagine que chegue um elemento da classe estrela que seja bem mais parecido com a bolinha vermelha — por exemplo, uma estrela vermelha. Ela vai ficar bem próxima da divisa. Se estivermos utilizando o plano B, ela vai passar para o outro lado, e começaremos a classificar a estrela como bolinha, o que estará errado. 

Se o limite for bem centralizado, é mais difícil uma classe passar para o outro lado. Buscamos maximizar as distâncias do nosso hiperplano, tornando-o o mais forte possível. Traçamos vetores de distância entre o hiperplano e as amostras, tanto das estrelas quanto das bolinhas.

### Separação Não Linear e Tratamento de Outliers

Neste caso, qual é o melhor hiperplano? Temos o hiperplano B, já que ele tem uma margem maior em comparação a A. O hiperplano B divide com uma margem muito boa. 

Porém, ao pegar o hiperplano B, uma estrelinha ficou junto com as bolinhas, gerando um erro. Existem situações onde não é possível separar perfeitamente as duas classes dessa forma. Em outro cenário, utiliza-se o hiperplano A e encerra-se o problema, pois ele deixa a estrelinha do lado correto e as bolinhas ficam todas separadas das estrelas.

Contudo, haverá situações em que o hiperplano traçado em linha reta não ficará correto de nenhum jeito. Ao tentar colocar a reta para dividir, não haverá como. É possível tentar separar as classes usando uma linha reta, porém haverá um território contendo um *outlier*. 

O que é esse *outlier*? É um valor fora do padrão que se misturou à outra classe. 

A SVM tem recursos para ignorar valores discrepantes. Ela reconhece que há uma amostra fora do padrão e a ignora. É melhor ignorá-la do que tentar classificá-la forçando o deslocamento da reta do hiperplano, o que prejudicaria toda a classificação. Se a reta fosse traçada no meio das bolinhas vermelhas para tentar englobar a amostra, não haveria classificação adequada e tudo ficaria misturado. É preferível aceitar a presença do *outlier*.

A SVM aceita essa condição. A rede neural é mais complexa para aceitar esse tipo de situação: ela tentará ajustar e classificar o problema até conseguir, demandando várias épocas de treinamento e tornando-se um sistema de alto custo computacional. A SVM é muito eficiente para situações em que trabalhamos com *outliers*. 

A seguir, veremos a parte relativa aos algoritmos.

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Olá.

</details>
