---
titulo: "Visão Computacional, IA e Aplicações em Sistemas Autônomos"
tags: [ia, machine-learning, conceitos, caso-pratico, estudos, pensamento-computacional, sistema]
data: 2026-08-21
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 45
conceitos: [Visão 3D, Visão Computacional, Veículos Autônomos, Rede YOLO, Reconhecimento Facial 2D, Conhecimento Especialista, Robótica Colaborativa, Machine Learning]
---

# Visão Computacional, IA e Aplicações em Sistemas Autônomos

> [!resumo] Do que se trata
> A aula explora a importância da visão 3D em sistemas autônomos, detalhando como a imagem 2D falha em detectar objetos e profundidade, o que é crucial para veículos e reconhecimento facial. Além disso, aborda o papel do conhecimento especialista em Machine Learning e Inteligência Artificial, mostrando aplicações práticas em indústrias como a classificação de carnes e a robótica colaborativa.

## Para lembrar

- **A imagem 2D falha em veículos autônomos porque não permite ver se todos os elementos estão na mesma profundidade da traseira do veículo, levando a falsos positivos (ex: adesivos ou desenhos).**
- **O reconhecimento facial feito por imagens 2D pode ser burlado (ex: usando uma foto de perfil no Facebook), sendo necessário o uso de câmeras 3D ou detectores de movimento.**
- **O treinamento de um sistema de Machine Learning depende do conhecimento especialista, que é o conhecimento humano passado para a máquina para que ela se comporte de forma útil.**

## O que esta nota responde

- Por que é necessário que os sistemas autônomos utilizem visão 3D em vez de apenas imagens 2D?
- Como o Machine Learning é aplicado em cenários industriais, como a classificação de carnes ou a robótica colaborativa?
- O que é o conhecimento especialista e como ele é fundamental no treinamento de sistemas de IA?

## Conceitos

**Visão 3D** · **Visão Computacional** · **Veículos Autônomos** · **Rede YOLO** · **Reconhecimento Facial 2D** · **Conhecimento Especialista** · **Robótica Colaborativa** · **Machine Learning**

## Conteúdo

`⏱ 00:00`

### Visão 2D vs. Visão 3D

O nosso mundo é 3D. Os objetos são 3D. A nossa visão também é 3D. É por isso que temos dois olhos. Esteticamente, ter dois olhos é mais bonito, mas não é por isso que os temos. Temos os dois para ter noção de profundidade.

Se você tampar um olho e tentar tocar alguma coisa, você perde a noção de profundidade. O mundo, principalmente para os veículos autônomos, precisa ser enxergado de forma 3D. Enxergar o mundo em 3D nos permite ter uma visão mais próxima da visão humana, que é o que buscamos quando falamos de visão computacional.

### Problemas da Imagem 2D em Veículos Autônomos

Existe um problema de imagem 2D.

Um problema foi detectado pelo MIT. Há um carro com um adesivo. Não há pessoas. É um adesivo colado. O sistema, utilizando a rede YOLO, detectou isso como pessoa e bicicleta.

Imagine você andando com um carro autônomo na rodovia, e ele detecta um adesivo atrás de um carro, por exemplo, de uma loja que tem uma pessoa desenhada. O carro freia com tudo porque acha que há alguém no meio da pista.

Isso é um problema. Não podemos usar a imagem 2D para veículos porque, em 2D, eu não consigo ver que todos os elementos estão na mesma profundidade da traseira do veículo. Em 3D, eu consigo ver: "Pera lá, não tem ninguém ali, é um carro e naquela superfície não tem mais nada."

Outro exemplo é uma parada obrigatória do McDonald's com um semáforo vermelho. Imagine um carro autônomo detectando isso e pensando que é uma parada obrigatória. Ele vai ficar parado até alguém remover essa propaganda.

Outro caso é o Leonardo DiCaprio com os braços abertos, em uma propaganda. Se o sistema detectar como uma pessoa querendo se matar, de braços abertos, ele não será eficiente.

Para resolver isso, precisamos de 3D. Com a visão 3D, avaliamos se o objeto é real ou não. Só com o 3D conseguimos isso.

### Exemplos de Falhas de Profundidade

Um outro exemplo de teste que teve problemas é um monumento, que se eu não me engano, é no Texas. O carro vinha de longe na rodovia, e quando ele pegou uma lomba da rodovia, a câmera, vendo de longe, detectou que havia uma pessoa dentro da pista. Mas não era uma pessoa dentro da pista. Ela tinha o tamanho de uma pessoa dentro da pista porque a noção de distância mostrou que esse monumento era uma pessoa dentro da via, porém não era. Como não temos noção de profundidade, o sistema autônomo falhou.

Se for com 3D, eu consigo avaliar: "Não, esse objeto está ainda a 4 quilômetros do carro, então não é algo real."

Outro exemplo é uma mulher em cima de um caminhão. Não é uma mulher. É uma propaganda, é um desenho de uma mulher.

### Limitações do Reconhecimento Facial 2D

E os nossos celulares? Se a gente pegar até o Galaxy S8 ou S9, o reconhecimento facial era feito por meio de imagem 2D.

Se você quisesse desbloquear o celular do seu amigo, você vai lá, abre o Facebook dele, uma foto de perfil, coloca na frente da câmera dele e o que acontece? Você desbloqueia o celular. Esse é um problema que acontece com imagens 2D.

`⏱ 05:00`

Atualmente, o celular usa duas câmeras ou ele utiliza um detector de movimentos, ou algo assim. Existem alguns sistemas que pedem: dê um sorriso, mexa a cabeça para a direita e para a esquerda, para tentar ajustar esse erro.

No entanto, atualmente os celulares, na maioria das vezes, utilizam uma câmera 3D ou uma câmera 2D com um laser, para verificar se seu rosto é uma foto ou se ele é 3D mesmo.

Ao tentar tratar esse problema, começamos a trabalhar com 3D. Esse foi o meu artigo quando eu comecei a trabalhar com imagens 2D e 3D. Esse artigo foi publicado com o foco de eliminar problemas em imagens 2D. Com isso, conseguimos:

- Detectar um pedestre ou um ciclista e avaliar se ele é real ou não, para ver se ele é 3D mesmo ou não.
- Determinar qual é a distância dele em relação ao carro.
- Detectar se um semáforo é real ou se ele é uma pintura.
- Detectar se uma placa de trânsito é real ou se é uma pintura no muro da autoescola.

Assim, avaliamos o objeto 3D. Depois, dividimos o que é placa e o que não é placa de trânsito. Em seguida, pegamos as regiões das placas e utilizamos uma rede de Deep Learning para classificar qual é a placa.

A rede que eu usei foi a rede `Inception`. Ela mostra, por exemplo, que a placa detectada é a placa de obras na pista. O sistema passa essa informação para o veículo, para que ele tenha maior atenção, pois a via está passando por obras.

### Aplicações em Segurança e Trânsito

Outra coisa muito importante é sobre as leis de trânsito, no cenário de comunicação entre veículos. Há muitas situações onde um veículo não consegue detectar uma informação de trânsito. Nesses casos, um outro veículo pode passar essa informação para ele.

Por exemplo, se um acidente ou um engavetamento acontece na pista, e um carro vem atrás, o sistema que está no carro que bateu já consegue passar essa informação para os outros: "Teve um acidente, então reduza a velocidade."

O sistema consegue avaliar o que está acontecendo na via, como, por exemplo, um trecho em obra, e passar essa informação para os outros carros.

Tudo isso é realizado utilizando modelos de visão junto com *machine learning*, como eu mostrei para vocês:

- A rede `Inception`
- A rede `YOLO`
- A rede `MASC-CNN`
- A rede `DeepLab`

Veremos as implementações dessas redes ao longo desta trilha.

### Ética em Sistemas Inteligentes

Falando um pouco da parte ética para sistemas inteligentes. Dentro de tudo isso, quando falamos, principalmente em situações críticas como o trânsito, precisamos avaliar a parte ética.

O que seria a parte ética disso tudo? Avaliar se as decisões programadas no sistema de inteligência artificial são como esperado pela lei e pela parte ética. Precisamos avaliar tudo isso.

Já existem algumas discussões para veículos autônomos, principalmente envolvendo a parte ética. Como programar um carro? Como implementar a ética dentro disso?

Um carro autônomo é programado para não bater em nada, assim como o nosso carro. Não importa se ele vai desviar de uma pessoa ou de uma árvore; ele tem que desviar dos dois. Mas qual é o grau de prioridade?

O que é preferível? Atropelar uma pessoa ou bater na árvore? Obviamente...

`⏱ 16:00`

É esse tipo de discussão que entra na parte ética de veículos.

Muitas pessoas veem as leis de Asimov, como por exemplo: um robô deve obedecer à raça humana; um robô deve proteger a raça humana desde que não faça mal a outro humano; e um robô deve proteger a sua própria existência desde que não entre em conflito com a primeira e a segunda lei. Resumindo, o robô deve se proteger.

Mas se ele tiver que se proteger e colocar em risco a vida de outra pessoa, ele tem que colocar a sua existência em risco. O robô não é prioridade em relação ao humano.

Se vocês pegarem, por exemplo, o filme *Eu Robô*, isso foi quebrado. Os robôs começaram a dominar a raça humana.

— Professor, mas quando a gente programa um robô, a gente tem que programar essas três leis?
— Não, isso é ficção científica.
— Professor, a gente programa robótica, a gente programa sistemas de *machine learning* para exterminar a raça humana?
— Também não. A gente programa os sistemas para evitar todo tipo de situação de risco, certo? Não atropelar ninguém, cometer colisões. Tudo isso, no final das contas, é para poupar vidas de pessoas.

### Dilemas Éticos em Veículos Autônomos

Existem situações em que a gente vai ter que tomar decisões, e são decisões mais delicadas.

Por exemplo, um carro autônomo está andando, levando o seu dono. Uma criança atravessa para pegar a bola. E aí? Se o carro desviar, ele cai numa ribanceira e mata o dono. E se o carro continuar reto e só frear, vai atropelar, porque o freio não dá tempo. Então, quem é que deve ser poupado?

Aí entram várias discussões sobre isso, e que a gente deve, num futuro próximo, ter isso implementado no sistema inteligente para que ele tome a melhor decisão possível.

Outra pesquisa do MIT: Um carro está vindo, ele perdeu o freio e não consegue desviar de todo mundo. Ele tem que atropelar ou a criança ou a velhinha. E aí, quem deve ser poupado? A criança ou a velhinha?

Vamos supor que a senhorinha aqui tem 100 anos de idade e a criança tem 1 ano de idade. Há 99 anos de diferença. Algumas pessoas dizem: "Poupe a vida da criança porque ela tem mais tempo de vida." Países mais desenvolvidos dizem: "Poupe a velhinha porque ela já contribuiu mais com a sociedade."

Isso mostra que depende do país que a gente está. A ética depende do local que a gente mora.

### Conhecimento Especialista e Treinamento de Sistemas

A parte de *machine learning*, quando a gente vai treinar um sistema, ela depende do contexto, depende daquilo que está ligado à nossa ética, daquilo que a gente espera.

Tudo isso vem de um conhecimento que se chama conhecimento especialista. É o conhecimento que a gente passa para uma máquina, para ela se comportar de forma que seja o mais possível dentro do que um humano faz.

### Aplicações de Machine Learning e Inteligência Artificial na Prática

Eu falei bastante da minha área, falei dos modelos de rede, falei de todo esse conjunto de técnicas, de situações de risco. Há uma ligação da ficção científica com a área de ciência e tecnologia. Não é porque a gente assiste um filme e fala que tudo isso é mentira, mas num futuro pode acontecer, e a ciência se inspira na ficção científica também.

A gente vai ver um pouco disso agora: Suporte para medicina. A gente desenvolve...

`⏱ 21:00`

Modelos de machine learning para dar suporte à área médica. Temos sistemas que conseguem avaliar diversas situações para ajudar o médico, como por exemplo, detectar um câncer de mama ou até mesmo uma microcalcificação.

É um pedacinho de um tumor que começou a crescer e é um quarto de um grão de arroz. O médico não consegue ver aquilo a olho nu. Se ele for detectar, pode ser depois de 5 ou 10 anos.

Um sistema de inteligência artificial consegue detectar até 10 anos antes, quando é apenas uma pontinha. Aí vai passar para o médico com a informação de que, nessa região, possivelmente há um tumor. O médico fará exames de sangue, fará uma biópsia e verificará se aquilo é mesmo um câncer ou um tumor benigno. Isso evita que a pessoa desenvolva ainda mais o problema dela, o que, em um futuro, faria com que o tratamento fosse muito mais agressivo.

A detecção de câncer de pele é outro exemplo. Existem vários tipos de lesões de pele, e nós utilizamos modelos de machine learning para detectar e verificar se é um câncer de pele mesmo ou não.

### Indústria 4.0 e Aplicações Industriais

Na Indústria 4.0, temos muito disso também. Dentro desse cenário, temos sistemas que ajudam o ser humano, principalmente em um contexto que envolve:

*   A Internet das Coisas (IoT);
*   A inteligência artificial;
*   A comunicação entre uma fábrica e outra;
*   A comunicação entre os robôs da fábrica e as máquinas.

Vou dar um exemplo: Antigamente, quando um robô pintava um carro, no final da linha de montagem, uma pessoa pegava um paninho de microfibra e passava na lataria para ver se estava tudo OK. Se havia uma peça mal pintada, ela voltava para ser feita novamente.

Hoje, o robô tem uma câmera com um algoritmo de machine learning que consegue detectar se a pintura está OK. O robô já sabe avaliar o que está fazendo e, se ficou alguma parte ruim, ele volta lá e faz de novo. Ele mesmo detecta o problema que ele gerou. Isso é uma evolução.

A inteligência artificial é aplicada dentro da fábrica para:

*   Pintura;
*   Verificar a solda se ficou correta;
*   Verificar a manutenção das máquinas, se está na hora ou não.

Isso está principalmente relacionado à manutenção preditiva. Nós avaliamos como está o estado do óleo da máquina, como está a característica mecânica da máquina, de forma geral, e agendamos uma manutenção preventiva.

### Evolução da Robótica e Controle

A revolução industrial envolve principalmente a parte robótica na Indústria 4.0. É um cenário onde estamos utilizando completamente a inteligência artificial, seja para soldar, seja para pintar. Tudo isso é muito importante para nós nos dias de hoje.

Antigamente, utilizávamos um braço robótico e programávamos linha por linha. Depois, começou a ser programado em `assembly`, onde você programava linha por linha do seu robô.

Em um futuro próximo, surgiu o controle. Você controla o robô como se fosse um videogame, com um controle remoto, como este aqui. O robô vai fazendo o movimento que você está querendo, ele grava esse movimento e depois ele executa. Assim, nós meio que não programamos mais esses braços.

Por que eu coloquei aqui o controle do homem morto? Esse controle tem um botão por baixo dele que, se você soltar, o robô para.

E por que isso é importante? Imagine que você está lá programando o robô, errou o movimento, e o robô veio e te deu uma porrada. Se você continuar ali, ele vai continuar te dando golpes. Agora, se você solta o controle, esse botão que atrasa o controle se chama botão do homem morto. Ao ser soltado, o robô para.

`⏱ 26:00`

### Robótica Colaborativa

O que é um robô colaborativo? Antigamente, com esses robôs, era necessário deixar um robô cercado e isolado, pois ele poderia causar danos a uma pessoa.

Muitos erros acontecem quando:

1.  Uma pessoa vê um robô na fábrica, ele está parado, e pensa: "Que bonitinho o robô, vamos tirar uma foto com ele."
2.  A pessoa se aproxima, mas o robô não está realmente parado; ele está em um estado de pausa, mas não está desligado.
3.  Nesse momento, chega uma peça na esteira. Para o robô, ele precisa pegar a peça para cortar ou soldar, e quem está ali do lado vai junto.

Por causa disso, era preciso deixar o robô isolado. A robótica colaborativa veio para melhorar esse cenário.

Um robô colaborativo é um robô que possui sensoriamento inteligente para verificar se há alguém por perto ou não. Se o robô faz um movimento e vê que há alguém ao lado, ele para, sem gerar dano à pessoa. Isso é muito importante para que possamos otimizar o nosso chão de fábrica, de modo que não tenhamos vários locais com robôs confinados, mas sim robôs trabalhando junto com as pessoas.

Por exemplo, em uma aplicação, o robô pode pegar algo pesado, enquanto a pessoa vai lá e coloca algo pequenininho. O robô ajuda a pessoa.

### Aplicações Industriais (Carnes)

Em uma aplicação industrial envolvendo carnes, estudei um problema em que a indústria tinha vários tipos de carnes:

*   Tipo A
*   Tipo B
*   Tipo C
*   Tipo D
*   Até o Tipo E

Imagine uma pessoa fazendo essa classificação o dia todo. Ela pode ficar tão cansada, ou ter um problema de memória, e ao olhar a carne, ela pode classificar incorretamente.

O que acontece se eu mandar uma carne tipo A para alguém que está esperando uma carne tipo E? A pessoa vai pensar: "Nossa, que carne boa, hein? Foi melhor para ela."

Mas se eu mandar uma carne tipo E para alguém que está esperando uma carne tipo A, eu vou perder o meu consumidor.

Esse é um grande problema, e precisamos utilizar métodos de classificação usando `Machine Learning`. O sistema deve classificar a carne com base em:

*   Quantidade de gordura.
*   Quantidade de perfuração que teve no couro do animal na hora de tirar o couro.

Se a carne tem muita gordura e muita perfuração, ela é um nível mais baixo. Se a carne é bem vermelhinha e sem gordura, ela é um nível mais alto. Uma IA consegue fazer isso tranquilamente.

Treinar um sistema de `machine learning` para isso é muito simples.

### Visão Computacional e Outras Indústrias

Algo assim já era feito dessa forma. Se pegarmos as indústrias antigamente, havia uma pessoa o dia todo sentada em uma cadeira, olhando garrafa por garrafa para ver se o nível estava certo de uma marquinha numa chapa de acrílico. A pessoa conferia:

*   O nível.
*   Se estava com a tampa certa.
*   Se estava com a etiqueta da garrafa certa.
*   A gravatinha da garrafa.

Aí começaram a colocar uma câmera que tira uma foto da garrafa e verifica se está tudo OK.

Portanto, ter um sistema de visão computacional na indústria utilizando `machine learning` já vem de muito tempo atrás.

Na área agrícola, as máquinas agrícolas coletam dados da lavoura.

`⏱ 30:40`

Por exemplo, vou comparar a minha produção de batata no ano de 2020 com o ano de 2021. 2021 produziu muito mais. Por que produziu muito mais? Eu vou comparar nos meus dados de produção com a máquina agrícola e vou verificar se ficou tudo dentro do esperado ou se produziu menos porque eu coloquei uma quantidade de adubo menor, ou porque a irrigação foi menor, ou porque a colheita foi em um momento errado. Assim, por meio desse volume de dados, eu consigo avaliar o que eu fiz de melhor para o ano em que eu produzi mais.

### Sistemas de Recomendação

Todo mundo passa por isso diariamente. Você entrou no Google e pesquisou um smartphone novo. Quando você entrar no seu Facebook, vai estar lá o anúncio. No seu e-mail vai estar lá o anúncio.

O que a gente tem também são sistemas de recomendação dentro de lojas. Por exemplo, você vai lá comprar uma cerveja. E quem compra a cerveja também compra a camiseta daquela cerveja. O sistema detecta isso como algo similar, porque todo mundo acaba fazendo essa compra. Aí, quando você vai comprar a cerveja, ele te diz: "Essa cerveja também acaba comprando essa camiseta. Você quer levar os dois por 10% de desconto?".

O sistema de recomendação observa o comportamento de outras pessoas para indicar esse comportamento e ver se para você faz sentido ou não. Assim, a gente tem uma base de dados para o sistema de *machine learning* de recomendação fazer a recomendação para você.

O sistema de recomendação trabalha com uma coleção de dados, com o armazenamento desses dados, a análise e depois a recomendação.

### Aplicações em Saúde e Medicina

Hoje é amplamente utilizado isso, e às vezes a gente nem sabe que é um sistema de *machine learning* que está fazendo isso.

Como eu falei para vocês, na área médica, o suporte para detectar um problema de saúde também é muito importante. Não só na área de tumores, mas também uma IA que consegue avaliar outras variáveis da sua saúde:

- Há quanto tempo você não tem, sei lá, uma cólica de rim?
- Há quanto tempo você não fez exame de sangue?
- Há quanto tempo você não toma vacina da gripe?

Tudo isso vai gerar uma relação para tentar fazer uma previsão do que está acontecendo com sua saúde e passar por um médio.

### Iniciativa 2045 e Tecnologia Futura

Falando também da área de *machine learning*, a Iniciativa 2045 é uma iniciativa que acontece em um mundo onde a proposta dela para 2020 era fazer uma cópia robótica de um corpo humano controlada remotamente via interface cérebro-computador. Isso já existe, e eu vou mostrar depois.

Também existe a necessidade, a proposta deles de 2020 a 2025, de um avatar em que um cérebro humano é transplantado no final da vida. Eles querem até 2025 tirar o cérebro de uma pessoa e colocar um robô e seu cérebro viver ali naquele robô eternamente, digamos assim.

De 2030 a 2035, um avatar com cérebro artificial, no qual uma personalidade humana é transferida no final da vida. Eles querem transferir o que tem na sua memória, no seu cérebro, para um computador e você ter a vida eterna em um robô ou em outro meio.

Se vocês assistirem aquele filme *Transcendência*, aconteceu exatamente isso. Uma pessoa morre e eles sobem, digamos, a mente da pessoa, o cérebro, a vida dela, para uma rede de computadores, e ele vive lá depois.

E depois de 2040, 2045, um avatar semelhante é um holograma. Então você vai viver em uma nuvem e você vai interagir com outras pessoas via um avatar. Um holograma é uma viagem. Parece ser uma viagem quando a gente conversa sobre isso, mas sem muito investimento nisso.

`⏱ 36:20`

O machine learning é primordial para que isso aconteça. Como detectamos uma expressão do cérebro? Temos que avaliar um pulso elétrico, que é um gráfico elétrico, e saber que aquilo é o que a pessoa está querendo falar. Então, temos que interpretar todos os sinais do cérebro para conseguir armazená-lo em uma memória.

### Transumanismo e a Necessidade Humana

Falando sobre a vida eterna, alguém gostaria de ter vida eterna? A vida eterna é uma questão ampla em relação à ética. Mas se pensarmos, por que temos a necessidade de fazer algo hoje? Por que temos a necessidade de acordar e dizer para a pessoa que amamos que a gente ama essa pessoa? Porque sabemos que o nosso tempo aqui na Terra é limitado.

Agora, se a gente soubesse que tem vida eterna, eu acredito que levaríamos as coisas de qualquer jeito.

A parte de transumanismo busca trazer para as pessoas outros potenciais. Exemplos disso são:

- Uma pessoa perdeu a visão, e colocamos um olho biônico nela.
- Uma pessoa é ruim de matemática, e colocamos um chip que acelera o processamento matemático do cérebro dela.

Outra área que parece uma viagem, mas tem alto investimento, é o machine learning, que é primordial também para que a gente desenvolva tudo isso: máquinas que pensam como seres humanos.

### Exemplos de Estimulação Cerebral

Aqui eu tenho um exemplo de como estimular um cérebro. O macaco está segurando uma alavanca, e essa alavanca não está conectada em nada. É igual quando a gente recebia um primo em casa, quando era pequeno, e nossa mãe falava: "Ah, deixa ele jogar". Aí você dava um controle que não estava conectado ao videogame. É mais ou menos isso.

Esse macaco está controlando uma alavanca que não está ligada em nada, e tem uma interface no cérebro do macaco com o computador. Quando o macaco faz o movimento e estimula a sua mão para pegar a alavanca e, com a garra, pegar o copo de suco, que é a recompensa dele. Na verdade, não é a mão dele que está movimentando nada. É o cérebro que está estimulando o sistema a movimentar o braço.

Isso é feito principalmente para a reabilitação humana.

Um exemplo disso foi a Copa de 2014, onde um cientista brasileiro colocou uma interface no cérebro de uma pessoa para controlar um exoesqueleto, e foi o primeiro chute da bola na Copa do Mundo. A pessoa foi lá e deu o primeiro chute, e a pessoa era paralítica. Ela conseguiu dar o primeiro chute na bola graças a essa interface.

### Interpretação de Sinais e Reabilitação Avançada

O machine learning é usado para interpretar o que o teu cérebro está querendo.

Há um problema, no entanto, quando a pessoa nasce sem os movimentos do corpo, ou quando ela perdeu ao longo da vida, mas quando ela já nasceu sem o movimento das pernas ou nasceu sem as pernas, ela não tem um estímulo de como é feito o movimento das pernas.

O que se faz lá no laboratório? Coloca-se um óculos de realidade aumentada, de realidade virtual. E aí coloca-se pernas *fakes* para a pessoa ficar olhando. A pessoa estimula essas pernas virtuais a se moverem, e aí o cérebro vai detectando esse padrão. Uma pessoa que nunca moveu as pernas consegue movimentar o exoesqueleto. É uma ideia bem legal.

Tudo isso é a camada entre o que está acontecendo...

`⏱ 41:00`

O que está acontecendo fisicamente com o nosso cérebro é uma camada de `machine learning`, que vai ver o que são os pulsos elétricos do nosso cérebro e vai acionar os atuadores do sistema para ele conseguir dar um chute na bola, por exemplo.

Um cientista brasileiro desenvolveu uma das maiores e melhores interfaces cérebro-computador com os melhores métodos de avaliação cerebral baseados em `machine learning`. Esse método dele, por exemplo, consegue ver o que você está pensando.

Como eles fizeram isso? Quando você está olhando um passarinho, no caso aqui uma águia, o seu cérebro tem uma área de ativação. Quando você olha um cachorro, seu cérebro tem uma área de ativação diferente. E quando você fecha os olhos e está pensando em alguma coisa — sei lá, estou pensando em um passarinho — a área de ativação do seu cérebro é a mesma de quando você está pensando em um cachorro ou quando está vendo um passarinho. Isso é o que vocês conseguem ver com o `Machine Learning`.

### Aplicações do Machine Learning

Não é algo tão simples. Ele começa de aplicações bem simples, como te recomendar um livro, mas vai até a área de transferência dos seus dados cerebrais para uma máquina, até controlar um carro autônomo ou fazer uma manobra de segurança.

Esse é o poder computacional que temos nas mãos hoje. As técnicas que existem estão aí, e vamos aprender muito sobre isso juntos.

Aqui, por exemplo, uma pessoa está controlando um robô por meio da interface cérebro-computador. Esse robô poderia ser um auxílio para uma pessoa paraplégica, para auxiliar nas atividades do dia a dia. É isso que conseguimos desenvolver com `machine learning`.

### Estrutura do Conteúdo

Hoje, o nosso conteúdo foi essa introdução ao `Machine Learning`, para entender como funciona esse mundo de tecnologia mais perto da nossa realidade.

Nos próximos conteúdos, vamos começar a ver a parte técnica e teórica disso tudo, e como a gente implementa.

É muito difícil implementar algo assim? Será que é complexo? Hoje, é algo fácil de fazer, porque temos auxílio de grandes ferramentas. Vamos aprender todas essas ferramentas e vamos trazer para o nosso dia a dia, para que, quando pensarmos em um problema, consigamos detectar uma solução com `machine learning` ideal para aquele caso.

## Relacionado

- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[reconhecimento-de-padroes-conceitos-aplicacoes-e-mecanismos-de-classificacao]]
- [[tomada-de-decisao-sistemas-adas-e-deep-learning-em-veiculos-autonomos]]
- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
