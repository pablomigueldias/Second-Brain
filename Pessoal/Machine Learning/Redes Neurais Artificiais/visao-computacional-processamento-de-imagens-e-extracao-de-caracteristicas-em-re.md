---
titulo: "Visão Computacional: Processamento de Imagens e Extração de Características em Redes Neurais"
tags: [estudo, ia, conceitos, fundamentos, machine-learning, algoritmos, dados]
data: 2026-08-21
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 31
conceitos: [Redes Neurais Artificiais, Visão Computacional, Análise de Características (Feature Analysis), Pixels, Matriz, Caixa Preta, Processamento de Imagem]
---

# Visão Computacional: Processamento de Imagens e Extração de Características em Redes Neurais

> [!resumo] Do que se trata
> A aula explica como as redes neurais artificiais processam imagens, comparando o processo computacional com a visão humana. É abordado o conceito de que o processamento ocorre em camadas, e como a análise de características (features) é realizada varrendo a imagem em matrizes. Por fim, são discutidas as diferenças de processamento entre imagens coloridas e em tons de cinza, e o conceito de 'caixa preta' do aprendizado.

## Para lembrar

- **Os olhos capturam a imagem (reflexão da luz) e a enviam para o cérebro, mas a interpretação é feita pelas redes neurais.**
- **Na visão computacional, a imagem de entrada é um conjunto de pixels com valores, e o computador precisa de algoritmos baseados em redes neurais biológicas para fazer o reconhecimento.**
- **A análise de características (features) é feita percorrendo a imagem com uma matriz, detectando partes importantes como olhos, orelhas ou focinho.**
- **Uma imagem colorida exige o processamento de três matrizes (Red, Green e Blue), enquanto uma imagem em tons de cinza utiliza apenas uma matriz.**
- **O modelo de aprendizado é chamado de 'caixa preta' porque, embora a rede saiba o que está aprendendo, não conseguimos visualizar o processo interno de aprendizado.**

## O que esta nota responde

- Como uma rede neural artificial consegue aprender a reconhecer padrões em uma imagem?
- Qual é a diferença de processamento de uma imagem colorida em comparação com uma imagem em tons de cinza?
- Por que o processo de aprendizado em redes neurais é chamado de 'caixa preta'?

## Conceitos

**Redes Neurais Artificiais** · **Visão Computacional** · **Análise de Características (Feature Analysis)** · **Pixels** · **Matriz** · **Caixa Preta** · **Processamento de Imagem**

## Conteúdo

`⏱ 00:00`

Falando de dados de entrada e de saída, como uma rede neural artificial consegue aprender um determinado tipo de padrão para que ela consiga gerar um valor para um determinado problema? Vamos ver um pouco sobre isso.

Para simplificar, vamos imaginar como funciona a nossa visão humana, ou a visão de qualquer animal que utilize a visão como um de seus sistemas de percepção, além do olfato, paladar, tato e audição.

### Visão Humana e Processamento de Imagens

Nossos olhos são sensores que capturam a imagem por meio da entrada. Recebemos uma imagem pela visão, uma imagem que foi reproduzida graças à iluminação da cena. Nossos olhos capturam a reflexão da luz — seja do sol, seja de uma luz interna, como fluorescente — sobre um objeto.

Os olhos capturam essa imagem e a enviam para o nosso cérebro. Sem o nosso cérebro, sem as nossas redes neurais, essa imagem não tem interpretação nenhuma.

Quando chega uma imagem — por exemplo, de uma pessoa no espaço — como reconheço que essa pessoa é um astronauta? Eu já tenho uma base de conhecimento acumulada ao longo da minha vida. Eu já vi exemplos do que é um astronauta, de como é o chão da Lua. Eu sei que essa pessoa está na Lua e que ela é um astronauta, porque eu já tenho uma base de conhecimento para isso.

Se eu não tiver na minha base de conhecimento neural o que é um astronauta, a imagem terá outra interpretação.

As nossas redes neurais, ou o nosso cérebro, são eles que interpretam as imagens que capturamos. Os nossos olhos não fazem nada além de capturar a imagem; toda a interpretação vem das redes neurais.

O processamento ocorre passando camada por camada dessa imagem. Por exemplo, reconhecemos o fundo: "O que eu tenho no fundo? Eu tenho a Lua." E o que temos mais à frente? "Eu tenho o astronauta." Tudo isso é baseado no reconhecimento da imagem. Fazemos isso de forma tão natural que às vezes não damos valor à complexidade de ter que fazer tudo isso.

### Redes Neurais Artificiais e Visão Computacional

Falando de redes neurais artificiais, o quanto o nosso cérebro trabalha para gerar uma resposta de uma imagem — dizendo, por exemplo, "Nessa imagem tem um gato, tem um cachorro" — é algo computacionalmente muito complexo, e é algo que muitas vezes não damos valor pelo que acontece instantaneamente no nosso cérebro.

Na visão computacional, a imagem de entrada que você tirou com a câmera não é levada para uma pessoa avaliar. Ela é levada para um circuito computacional, um processador e uma memória.

Como esse sistema vai conseguir reconhecer que a foto capturada pela câmera é na Lua e tem um astronauta?

Eu preciso de algoritmos que são baseados nas nossas redes neurais biológicas para que o sistema consiga reconhecer essa imagem.

`⏱ 05:00`

Que foi capturada pela câmera. Se eu não fizer esse reconhecimento, uma imagem para o computador é um conjunto de pixels com valores. O computador não sabe o que tem dentro de uma foto. Só sabemos isso graças às tecnologias.

Por exemplo, eu queria saber se era uma aranha venenosa ou não. Tirei uma foto da aranha, coloquei no Google Lens e ele me disse a espécie da aranha. Eu não sabia se era uma aranha venenosa, o que eu teria que, sei lá, pedir para um biólogo me dizer. A inteligência artificial do Google me retornou essa resposta.

Vejam que a inteligência artificial, hoje, para uma imagem de entrada, ela tem uma interpretação muito boa.

Outro exemplo é quando a gente coloca uma foto no Facebook. O próprio Facebook já detecta todas as faces e já te indica: "Essa pessoa é sua mãe, essa pessoa aqui é sua esposa." Ele coloca lá o nome da pessoa para você. Às vezes, o sistema não é tão preciso, mas na maioria das vezes funciona muito bem.

Por quê? Há uma inteligência artificial ali, baseada em redes neurais biológicas, ou melhor, baseada no comportamento biológico, mas implementada na forma de rede artificial, que reconhece essa imagem. A complexidade disso, hoje, é muito fácil de se implementar. Porém, os algoritmos são bastante robustos para que a gente tenha esse tipo de processamento.

#### O Processo de Processamento de Imagem

A entrada é basicamente capturar a imagem e levar para o nosso sistema de processamento. Depois, tudo que vem é a parte de processamento. E no final, a gente vai ter o quê? Os dados interpretados na saída. São os dados que foram lidos pela câmera e que serão interpretados.

Vamos ver alguns exemplos sobre isso.

Quando um algoritmo recebe uma imagem de entrada, como aqui, estamos recebendo a imagem do astronauta. O computador não sabe avaliar uma imagem como nós avaliamos. Eu estou olhando essa imagem do astronauta e eu sei que tem um astronauta aí, só de olhar.

Mas quando um computador tem que avaliar uma imagem, por exemplo, esse gato. É a nossa imagem de entrada. Vocês só olharam para essa imagem e já viram um gato. O computador tem um trabalho muito maior para isso.

#### Capacidade Humana vs. Computacional

Eu costumo dizer que o computador é muito bom para cálculos e situações objetivas. Porém, para a capacidade de abstração, para a capacidade de enxergar uma imagem, isso é muito mais complexo para um computador, porque a nossa capacidade de percepção é muito melhor do que a de um computador.

Até hoje, daqui para frente, não sabemos como vai ser, mas basicamente o computador é muito melhor em cálculos matemáticos, e o ser humano é muito melhor em abstração.

A abstração de uma imagem para nós é instantânea. Você está andando para a rua, você vê um gato, um cachorro, um carro. Tudo isso você está enxergando em tempo real e já detectando o que é cada objeto. Para o computador é muito mais complicado, porque vocês estão vendo esse pedacinho da boca do gato, gera essa matriz de dados, e quando eu vou avaliar uma imagem de um gato para...

`⏱ 09:40`

Tentar descobrir o que é essa imagem não tem como eu colocar esse gato todo numa matriz. Então eu tenho que percorrer a matriz sobre a imagem para reconhecer o que é cada partinha, para depois tentar descobrir o que é esse objeto de forma.

O que é esse objeto de forma? Depois a gente vai ver que quando uma matriz passa na ponta da orelha do gato, ela detecta que possivelmente é um gato por meio dessa característica. Quando a matriz bate aqui nos olhos, os olhos do gato têm um formato bem característico, a boca também, o focinho, os bigodes. Então tudo isso é uma característica muito importante para que a gente reconheça o gato.

Mas a entrada da imagem não é igual para a gente. Quando a gente olha para a imagem, ah, é um gato. O computador ele tem que avaliar cada parte da imagem, porque a imagem toda seria impossível dele olhar de uma vez só.

### Análise de Características (Feature Analysis)

Fazendo agora uma visão sobre a análise de características, análise de *features*. Assim como eu estava comentando com vocês, quando eu tenho uma imagem de entrada aqui, a gente tem outro exemplo de gato. Eu gosto muito de gatos, então vocês vão ver vários exemplos com as minhas imagens com os gatinhos.

Eu tenho aqui um gato e, como eu disse para vocês, não tem como eu jogar essa imagem toda na entrada de uma rede neural. Então o que eu tenho que fazer? Eu tenho que percorrer com uma matriz essa imagem e tentar fazer pequenas leituras dessa imagem para depois eu unir tudo e tentar fazer uma previsão e classificar se esse objeto é um gato, se é um cachorro, qual é o tipo desse objeto.

Vocês podem observar que nas camadas do meio da minha rede, eu tenho algumas características que a rede detectou como importantes para definir que esse animal é um gato.

Quais características que foram importantes?

*   A orelha, por conta do formato.
*   O focinho.
*   A outra parte da orelha, tendo uma vista por outra perspectiva.
*   Os olhos e o rabo.

Professor, por que não pegou uma parte... uma partinha aqui da coxa do gato? Porque se eu pegar a textura do pelo desse gato, poderia ser desde um gato até outro tipo de animal.

Uma parte apenas do couro do gato não vai trazer informação nenhuma, porque tem cachorro que tem essa cor, tem outros tipos de animais, hienas que tem essa cor, outros também que às vezes eu não me lembro agora. Mas só uma parte do couro do animal não vai me dar uma boa classificação.

Então eu tenho pontos característicos para entender qual é o tipo do animal que eu estou enxergando. E principalmente aqui para o gato foram os objetos:

*   Orelha.
*   Focinho.
*   Olhos.
*   Rabo.

E quem é que define isso? Que esses objetos são importantes para a rede? Ela mesma. Ela mesma que vai fazer essa avaliação e dizer que esses pontos da imagem, essas características que são importantes para dizer que esse objeto é um gato mesmo.

A rede faz isso automaticamente. E ela consegue retornar para a gente o que é que foi importante.

É a mesma coisa eu perguntar para vocês: O que é importante para classificar o que é um carro e uma motocicleta? Vocês vão me dizer assim: ah, um carro tem quatro rodas e uma motocicleta tem duas. E para classificar uma motocicleta e um triciclo? Vocês vão me dizer: ah, um triciclo, o nome já diz, ele tem três rodas e uma motocicleta tem duas rodas. Essa é a diferença.

`⏱ 14:40`

Tem outras diferenças? Tem. Mas se você observar essas diferenças entre as rodas, você já consegue dizer se é um triciclo ou uma motocicleta. Vejam como é simples para a gente dizer quais as características importantes.

Outra característica, se eu pedir para vocês definirem rapidamente, como que eu faço para diferenciar um gato de um cachorro? Vocês vão me dizer: um gato mia e um cachorro late. Para a gente é muito fácil dizer as características. Para uma rede, ela tem um trabalho maior, e eu vou mostrar um pouco disso ao longo dessa aula.

### O Processamento de Dados em Redes Neurais

Sempre a gente vai ter a rede avaliando os dados de entrada, percorrendo uma matriz sobre a imagem. Essa matriz, ao percorrer a imagem, vai trazer para a gente um valor de percepção sobre o objeto, que é o campo receptivo da imagem.

Por meio dessas imagens, a gente vai ter convoluções que vão ser feitas sobre a imagem. O que seriam convoluções? É algo que se adapta sobre a imagem, percorrendo a imagem até varrer todos os dados de entrada. Depois disso, a gente vai ter o mapa de características.

O que seria o mapa de características? Seriam os dados que a rede interpretou e detectou com dados importantes. Eu vou ter lá os olhos do gato, como parte do mapa de características, as orelhas, o focinho, o rabo. Esse é o meu mapa de características que é levado para a rede.

E como que é feito isso na prática? O algoritmo vai varrer pixel a pixel. Por isso que eu sempre falo que um algoritmo neural trabalha de uma forma muito mais complexa do que uma pessoa com sua visão.

### Imagens Coloridas vs. Tons de Cinza

Aqui a gente tem, por exemplo, a mesma imagem de entrada. Se eu estou avaliando ela em preto e branco, vou ter uma matriz de entrada. Se eu estiver avaliando a imagem colorida, eu vou ter três matrizes: a matriz `Red`, a matriz `Green` e a matriz `Blue`.

Uma imagem colorida tem uma diferença de processamento ainda maior, porque eu não tenho só uma matriz, eu tenho três matrizes. Isso é um problema maior para processamento.

Por isso, tem algumas situações que a gente faz o seguinte: transforma a imagem em tons de cinza para ficar preta e branca. É mais fácil de avaliar a imagem com uma matriz única.

**Professor:** Mas as cores não são importantes?

Para algumas coisas não. Para o gato, por exemplo, as cores não são importantes para avaliar que esse objeto é um gato.

Mas a gente tem que levar em consideração. Agora, por exemplo, para o trânsito, um carro autônomo, as cores são muito importantes, porque a sinalização de trânsito com as cores trazem recursos que são muito importantes para o trânsito. Se o semáforo está amarelo, se ele está vermelho, se ele está verde... uma placa de atenção, uma placa de advertência. As cores são muito importantes para quando a gente fala de um sistema computacional funcionando no trânsito.

Vamos imaginar também que o nosso sistema estava avaliando uma partida de futebol. As cores dos uniformes também são importantes, para que o sistema consiga fazer uma previsão de qual é aquele jogador, de qual time é aquele jogador. Então isso é muito importante para a gente.

As cores não são importantes?

Então a gente pode reduzir o espaço dimensional de cores e trabalhar só com o espaço de cores reduzidas, que seriam imagens em tons de cinza. E aqui vocês conseguem ver a imagem...

`⏱ 19:40`

Com as características. Vocês estão vendo só o contorno do gato: o contorno, os olhos, o nariz, o focinho. Essas informações são muito importantes para reconhecer o gato.

Por exemplo, a sombra que está aqui no peito dele. Essa informação não é importante. Ela deixa a imagem mais bonita, mais realista, mas para a rede é insignificante.

Tudo isso acontece dentro de uma rede neural quando ela está avaliando uma cena. A mesma coisa acontece conosco. Quando peço para vocês reconhecerem uma pessoa, alguns detalhes da pessoa vocês não vão levar em conta.

Por exemplo:
- A cor da camisa da pessoa? Não importa.
- Se a pessoa está com uma caneta no bolsinho da camisa?
- Se a pessoa está bem vestida ou mal vestida?
- Se a pessoa está com o cabelo penteado ou não?
- Se a pessoa fez a barba ou não?

Essas informações, às vezes, não são relevantes para que o sistema faça uma avaliação. Quando fazemos uma avaliação computacional de uma imagem, acabamos jogando muita informação fora que não é relevante. O problema é como avaliar qual informação é relevante e qual não é.

### O Conceito de Caixa Preta (Black Box)

As características que a rede avalia como importantes são o que chamamos de caixa preta.

Se eu pedir para uma rede classificar tipos de carros — como o Gol, o Uno, o Jetta, o Jeep — quais características foram importantes para reconhecer esses tipos de carros? Obviamente, serão as linhas de design do carro.

No entanto, eu não consigo ver internamente a rede quais características foram importantes para ela. É uma caixa preta. Tudo que a rede neural aprende fica dentro de uma caixa preta, e não conseguimos interpretar esses valores. Existem alguns métodos que dão suporte para isso, mas são pouco eficientes.

Isso acontece também com o nosso cérebro. Sabemos muita coisa, mas se eu tentar interpretar os dados do que está dentro da sua cabeça, não consigo. Conheço uma pessoa muito inteligente e eu gostaria de copiar o cérebro dela, mas não consigo porque não sei como o cérebro dela se comporta em relação às variáveis, às características e aos dados de aprendizado. Não adianta eu copiar o cérebro da pessoa porque não vou saber interpretar os valores.

É por isso que chamamos o modelo de caixa preta: tudo fica ali dentro, muito bem escondido. A rede sabe, está ali dentro, é parte dela, porém, não conseguimos visualizar o que está ali dentro, que é o aprendizado.

### Exemplos de Extração de Características

Falando de características, vimos basicamente as características do exemplo do gato:
- Orelha
- Rabo
- Focinho
- Bigode

Essas características foram importantes para reconhecer o gato. Mas e outros objetos?

Aqui temos, por exemplo, as características para reconhecer uma face humana. Quais características são importantes?
- A boca
- O nariz
- Os olhos
- O contorno da face
- O tamanho do nariz

E temos também o *shape* do rosto, que é o formato geral do rosto.

Imagine que você vai desenhar o rosto da sua mãe, um desenho bem simples. O que você vai absorver mais? O formato do rosto, o formato dos olhos, da boca.

## Relacionado

- [[redes-neurais-artificiais-conceitos-estrutura-e-aplicacoes-em-machine-learning]]
- [[logica-difusa-redes-neurais-generalizacao-e-algoritmos-bioinspirados]]
- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
- [[metodos-bioinspirados-redes-neurais-e-logica-fuzzy-em-machine-learning]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- tecnologias de machine learning dentro das bases de dados então não sei se todo mundo já usou o Google Lens o Google Lens você vai lá tirou uma foto aí você consegue pegar essa foto clicar no botãozinho do Google Lens contornar o que você quer Então esses dias teve uma aranha que entrou na nossa casa, uma aranha bem diferente e grande.

</details>
