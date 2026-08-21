---
titulo: "Redes Neurais, Deep Learning e Aplicações Práticas de Machine Learning"
tags: [machine-learning, ia, conceitos, caso-pratico, fundamentos]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 27
conceitos: [Aprendizado por reforço, Redes neurais artificiais, IA restrita, Veículos autônomos, Robótica assistiva, Deep Learning, Visão computacional]
---

# Redes Neurais, Deep Learning e Aplicações Práticas de Machine Learning

> [!resumo] Do que se trata
> Apresenta os conceitos de aprendizado por reforço e redes neurais artificiais bioinspiradas no cérebro humano. Demonstra casos práticos de aplicação de machine learning em veículos autônomos, monitoramento de saúde pública e robótica assistiva com Raspberry Pi. Explica o funcionamento de redes de Deep Learning inspiradas no córtex visual para processamento de imagens e reconhecimento de padrões.

## Para lembrar

- **No aprendizado por reforço, o sistema recebe pesos positivos ao executar um aprendizado efetivo e valores negativos em caso de falha.**
- **As redes neurais artificiais utilizam dezenas a centenas de neurônios para executar aprendizado focado em funções restritas específicas.**
- **Sensores acústicos que identificam a frequência do bater de asas de insetos permitem mapear focos de mosquitos da dengue com precisão.**
- **Redes de Deep Learning utilizam múltiplas camadas neurais inspiradas no córtex visual animal para reconhecer formas, texturas e contornos em imagens.**

## O que esta nota responde

- Como funciona a lógica de recompensa no aprendizado por reforço?
- De que forma redes neurais e visão computacional são aplicadas em veículos autônomos e robôs assistivos?
- Como as redes de Deep Learning processam e classificam características visuais em imagens?

## Conceitos

**Aprendizado por reforço** · **Redes neurais artificiais** · **IA restrita** · **Veículos autônomos** · **Robótica assistiva** · **Deep Learning** · **Visão computacional**

## Conteúdo

`⏱ 00:00`

Vamos abordar um pouco da inteligência artificial restrita, que por meio de um método de `machine learning`, conseguimos obter esse tipo de inteligência atualmente e de uma forma bem tranquila.

Um exemplo de aprendizado dentro do `Machine Learning` é o aprendizado por reforço. Se compararmos o nosso dia a dia com o nosso aprendizado, ou até mesmo o aprendizado de um cachorro, ele acontece dessa forma.

Como ocorre o aprendizado quando você está treinando um cachorro? Se ele faz o que você está querendo — se ele dá a patinha, se ele rola, se ele deita — você recompensa ele com um biscoitinho. Assim, você o reforça positivamente por meio da atividade que ele fez e que você esperava. Caso ele não faça aquilo que você está querendo, você não vai recompensá-lo. Ele entende que, se você pede algo e ele faz, ele ganha uma recompensa. O aprendizado de máquina por reforço funciona mais ou menos dessa forma.

Na rede, por exemplo, há uma recompensa. Uma rede neural recebe um peso positivo caso execute um aprendizado positivo. Caso ela não aprenda de forma efetiva, ela recebe um valor negativo. Também podemos comparar com o nosso aprendizado: quem nunca ouviu dos pais que, se você passar de ano, vai ganhar seu videogame? O aprendizado por reforço busca recompensar o sistema por meio de um aprendizado que aconteceu de forma efetiva. Ele é um dos tipos de aprendizado de máquina e um dos tipos de aprendizado mais comuns na área científica.

### Redes Neurais Artificiais

Falando de inteligência artificial restrita, um dos modelos mais utilizados atualmente e mais robustos para diferentes situações são as redes neurais.

As redes neurais artificiais são baseadas nos neurônios biológicos do nosso cérebro. Com isso, conseguimos gerar algoritmos bioinspirados que se comportam como pequenas partes do nosso cérebro, englobando neurônios para que obtenhamos uma rede não tão complexa quanto o nosso cérebro.

Na verdade, não é nem um pouco próxima da realidade do nosso cérebro, que tem bilhões de neurônios. Acabamos usando alguns neurônios, cerca de centenas no máximo, e com isso conseguimos realizar um aprendizado para uma determinada função específica. É por isso que chamamos de aprendizado restrito, gerando uma inteligência artificial que é restrita.

### Aplicações e Foco em Veículos Autônomos

Depois de falar dessa introdução ao `machine learning`, vamos começar a ver as aplicações, envolvendo principalmente a área de veículo autônomo, que é a área que eu trabalho atualmente e minha área principal de pesquisa.

Vou focar alguns exemplos para vocês verem o potencial que temos no desenvolvimento de `Machine Learning`. Atualmente, trabalho com pesquisas na área de veículos. Meu mestrado, doutorado, pós-doutorado e pós-graduação em `Internet das Coisas` são todas voltadas para a área de veículos. Foi nessa área que desenvolvi alguns projetos para algumas empresas, e é na área de `Machine Learning` que eu foco.

Vou comentar alguns exemplos, principalmente na área de visão computacional, para que vocês tenham uma noção do potencial desses métodos na prática. Falando de veículo autônomo, temos algumas repartições que focam em diferentes tipos de aplicações, como, por exemplo, a Waymo, que é uma repartição da Google.

`⏱ 05:20`

Ela quer trazer para nós um veículo que utilizemos no nosso dia a dia e que tenhamos em casa, para que possamos ir ao lugar que queremos, tendo mais liberdade. Isso é especialmente importante para pessoas deficientes ou em outras situações que não podem dirigir um veículo.

A Uber também busca trazer frotas de veículos com maior segurança, tanto no trânsito quanto na relação entre o motorista e o passageiro. São grandes potências que já estão acontecendo. Por exemplo, nos Estados Unidos, você pode chamar um Uber e ele vir como um carro autônomo.

### Projetos de Veículos Autônomos

Nos projetos que eu trabalhei junto à USP de São Carlos, começamos desenvolvendo o `Carina 1`. Este era um carro de golfe e foi o primeiro carro autônomo da América Latina. Implementamos o controle nele, e ele anda sem motorista.

Depois, migramos para o `Carina 2`, que é um carro convencional, um carro comercial. A única coisa que veio para nós foi o câmbio automático, e automatizamos esse carro para ele andar sem motorista. Colocamos motor na direção, motor no freio, motor no acelerador, e um computador que controla o carro e toda a parte de sensoriamento que vou mostrar depois.

O nome `Carina` significa Carro Robótico Inteligente de Navegação Autônoma.

### Aplicações em Outras Áreas

A gente também desenvolve projetos na área agrícola. Por exemplo, desenvolvemos um trator que navega sem o tratorista.

Algumas pessoas podem perguntar: "Mas por que um trator sem tratorista não vai tirar o emprego dele?"

A resposta é que esse trator é usado para aplicar pesticida. Ele fica o tempo todo aplicando pesticida, e uma pessoa em contato o dia todo com esse elemento químico pode gerar danos à saúde. Nosso objetivo é eliminar o trabalho humano em situações que são danosas à saúde humana.

Outro projeto que trabalhamos e que ainda está em desenvolvimento é o de um caminhão autônomo, um Scania. Neste projeto, usamos um Scania convencional e trouxemos uma forma de navegação autônoma, a mesma implementada nos carros do projeto Carina. Este também foi o primeiro caminhão autônomo da América Latina, e temos sensores de grande precisão para que o caminhão navegue sem um motorista.

Qual é a ideia de fazer um projeto desse? É tirar o trabalho do motorista? Não. É trazer uma maior segurança, principalmente em viagens de longa distância.

Por quê? Há motoristas que assumem dirigir por 30, 40 horas direto, tomando alguns estimulantes, por exemplo, cafeína e até outros tipos de drogas. Isso acaba gerando problemas e acidentes fatais.

Portanto, buscamos trazer para o motorista um piloto automático, como se fosse um avião. Ele entra no caminhão, liga o automático, e o caminhão vai para onde foi programado. Quando ele chega no momento de descarregar o caminhão ou fazer uma manobra mais complicada, como estacionar o caminhão dentro de um armazém, o motorista assume o controle. Isso facilita a vida dele, principalmente em relação ao fator de descanso.

### Inteligência Artificial e Saúde

Falando também na área de inteligência artificial, junto ao ICMC USP, há um projeto do professor Gustavo Batista, junto com os alunos de mestrado e doutorado. Eles desenvolveram um sensor que, por meio do bater das asas do mosquito ou de qualquer outro inseto, é detectado qual é o tipo desse inseto. O foco deles é saber se é um mosquito da dengue ou não.

Para que isso? Para que tenhamos uma forma de centralizar...

`⏱ 10:00`

As equipes de combate à dengue atuam em regiões onde o mosquito está em maior quantidade. Atualmente, o método é que as equipes se espalham pela cidade procurando os focos do mosquito. No entanto, isso não é tão eficiente quanto descobrir onde há uma maior aglomeração de mosquitos.

O que se faz é usar um sensor que é espalhado pela cidade, como se fossem algumas gaiolinhas. Esses sensores detectam onde há uma maior quantidade de mosquitos. O mosquito é atraído por dióxido de carbono e, em seguida, é puxado por um fluxo de ar em direção ao sensor.

O mosquito é identificado por meio de fototransistores. Ao passar por esses fototransistores, é possível ver a frequência do batimento das asas e até detectar se o mosquito é macho ou fêmea. A armadilha possui um dispositivo de emissão de luz para avaliar o tipo de mosquito, se é um mosquito comum ou um mosquito da dengue.

Com isso, a equipe de combate à dengue é direcionada para procurar os focos naquela região. O sensor é capaz de identificar e distinguir até o *Aedes aegypti*, tanto o macho quanto a fêmea. Isso é importante porque são as fêmeas que transmitem doenças, como o zika e a dengue.

Como se avalia essa frequência do batimento das asas? Por meio de uma rede neural artificial, que é um método de *machine learning*.

### Aplicações em Agricultura

Outra aplicação bem interessante é na área agrícola: um robô desenvolvido pela Alemanha. Ele detecta onde há ervas daninhas ou pragas usando uma câmera e um algoritmo de aprendizado de máquina baseado em *Deep Learning*, que é um método de *Machine Learning*.

Este método é muito utilizado atualmente e tem a capacidade de avaliar onde a praga está. O sistema dispara um raio laser que queima somente a praga. Isso garante que o alimento produzido não seja contaminado por pesticidas, pois a praga é queimada com um laser, sem a aplicação de nenhum tipo de pesticida.

### Projeto Pessoal e Machine Learning

Um projeto legal para entender a importância da aplicação de *Machine Learning* na prática é o que desenvolvemos com a Red Bull: um cão-guia robótico.

A ideia desse projeto veio principalmente da minha família. Minhas avós são deficientes visuais. Minha avó sempre dizia: "Eu queria tanto um carro que me levasse onde eu preciso, sem precisar sempre de uma pessoa para me levar onde eu quero." Ela queria essa liberdade. Embora ela tivesse visão, era uma visão muito baixa, o que causava esse problema.

Eu também trabalhei em uma escola que tinha o instituto do deficiente visual. Lá, sempre precisávamos levar alguém ao banheiro ou ao refeitório. O deficiente não gostava e tentava pegar na mão de quem o guiava. Eu ficava pensando se seria vergonha estar de mão dada com ele.

Um dia, perguntei para a psicóloga, e ela disse que não. Eles querem segurar no ombro e ficar atrás de você para se sentirem protegidos. Assim, se você se esbarrar em alguma coisa ou tropeçar, você está na frente e vai proteger o deficiente.

Eu entendi que fazia sentido. Comecei a pensar: é por isso que o cão-guia vai à frente. Só que um cão-guia tem um valor muito alto, cerca de 40%.

`⏱ 15:00`

O tempo de uso de um cão-guia é de cerca de 3 anos. Isso ocorre porque ele demora 4 anos apenas para ser treinado. Depois, quando ele começa a perder a audição ou o olfato, o que precisa ser feito? Ele precisa ser aposentado.

Foi assim que desenvolvemos o trabalho. Primeiramente, criamos um cão-guia robótico, em parceria com meu aluno Marcelo de Assis. A estrutura utilizada é baseada em um aspirador de pó, que é o robô à esquerda. Posteriormente, desenvolvemos outro robô à direita, com o apoio da Red Bull. Com esse projeto, ficamos entre os cinco melhores projetos maker do Brasil e também entre os projetos mundiais espalhados em outros polos de tecnologia da Red Bull.

### Estrutura e Funcionamento do Robô

A estrutura do robô é bastante simples. Utilizamos uma `webcam` de computador e uma `Raspberry Pi`, que é uma plaquinha eletrônica que simula um computador em menor escala. Essa abordagem é necessária porque seria inviável colocar um PC completo no robô para carregar.

Nosso robô consegue detectar vários obstáculos:

- Orelhões;
- Entradas de cadeira de rodas;
- Cachorros na rua.

**Por que detectar orelhões?**
O orelhão representa um problema para o deficiente. Quando ele está andando na rua, a bengala dele não detecta o orelhão porque ele é avançado. O deficiente pode bater a cabeça antes de detectar o obstáculo.

**Por que detectar a entrada de cadeira de rodas?**
Nosso robô possui rodas e não consegue subir uma guia. Por isso, ele precisa detectar a entrada de cadeira de rodas.

**Por que detectar cachorros?**
Há muitos cachorros na rua, e eles podem querer morder o deficiente. Por meio da câmera, o robô detecta o que está à frente, desvia e avisa o deficiente que há um cachorro à sua frente, indicando que ele deve desviar.

Com isso, o deficiente tem um melhor *feedback* do que está acontecendo ao seu redor.

### Treinamento do Sistema

Para treinar esse sistema, é necessário aprender sobre conjuntos de dados (*dataset*). Utilizamos:

- 150 imagens de orelhão;
- 100 imagens de entrada de cadeira de rodas;
- 300 imagens de cachorro.

### Sensores para Veículos e Robótica

Os sensores utilizados para veículos e robótica em geral são principalmente baseados em câmeras e lasers.

**1. Câmera Estéreo 3D**
Utilizamos a câmera chamada `Bubble Bee`. Ela enxerga tanto em 2D quanto em 3D. A diferença é que, em uma imagem 3D, sabemos a profundidade. Assim, sabemos onde está o nosso obstáculo ou onde está o objeto que o robô deve pegar, o que é importante na robótica.

**2. Laser (LiDAR)**
Utilizamos o `Velodyne`, que é um sensor que enxerga 360 graus.

**Por que usar o laser?**
Existem situações em que a câmera fica "cega". Por exemplo, quando o sol bate de frente, com uma luz muito forte, a câmera para de enxergar. Isso é semelhante a quando você está andando em uma rodovia e um carro com luz alta cruza com você, fazendo você perder parte da capacidade de visão. Da mesma forma, quando o sol bate muito de frente com o seu rosto, ele ofusca a imagem.

O laser não tem essa limitação. Ele não importa se está chovendo, se está nevando ou se há uma tempestade de areia; ele vai enxergar sempre da mesma forma. Essa é a visão do laser.

`⏱ 19:20`

Laser de 360 graus avalia toda a cena. Conseguimos detectar o que é carro, o que é pessoa, o que é árvore, o que é rua, com uma resolução menor que a de uma câmera. No entanto, essa imagem não importa qual é o período do dia ou qual é o clima; é sempre assim. Essa é uma grande vantagem em comparação com a câmera, que tem variações climáticas e gera problemas.

Por exemplo, temos uma imagem 3D da câmera. Por que uma imagem 3D é tão importante? Porque conseguimos avaliar o tamanho do objeto e a distância do objeto. O mundo é 3D, e isso é muito importante para quem fala de um método que usamos muito em Machine Learning: o método de Deep Learning.

### Redes de Deep Learning e Frameworks

Eu já comentei com vocês e vamos ver ao longo do curso como essa ferramenta, como esse método funciona. Para usar essas redes de Deep Learning, redes de aprendizado profundo, utilizamos um framework chamado `TensorFlow`.

O `TensorFlow` é um framework gratuito para Machine Learning que utiliza redes de Deep Learning. Esse tipo de rede é um modelo usado para detectar objetos e classificar. Por exemplo, a rede que está em um celular de vocês, quando você coloca o celular para reconhecer o rosto, tem uma rede desse rodando.

Essa rede utiliza várias camadas de neurônios. Por isso ela tem esse nome (Deep), ela tem um aprendizado profundo, por isso o nome Deep. Ela é uma rede profunda, e com isso conseguimos reconhecer imagens com grande capacidade.

Essa rede foi baseada no córtex visual frontal dos gatos. Foi por meio da visão dos gatos que essa rede veio a existir. Ela consegue interpretar a textura do animal, a textura do pelo, o formato da orelha, o formato do corpo, e tudo isso entra como característica para classificar o objeto.

Se é um gato, ele tem a orelha pontuda. Se é um gato, ele terá um tamanho menor, na maioria dos casos, e um formato diferente. Por exemplo, se eu olhar a sombra de um gato e a sombra de um cachorro, é diferente. Assim, só pelo formato eu já consigo avaliar o objeto. Essa rede tem um grande potencial para isso.

### Bibliotecas de Machine Learning

Falando sobre bibliotecas de Machine Learning, uma biblioteca muito utilizada é a `Scikit-Learn`. Essa biblioteca tem um grande potencial para modelos de Machine Learning. Você não precisa, às vezes, nem implementar uma rede neural ou um método de Machine Learning; você chama o modelo e ele já vem implementado, e você aplica ele para o seu problema.

Hoje, em Machine Learning, não precisamos basicamente programar tudo do zero. Temos muitas bibliotecas que nos auxiliam. Se você precisa de uma rede neural artificial, nós temos aqui dentro dessa biblioteca. Ao longo do curso, vamos ver como usar essa biblioteca e como implementar algoritmos com ela.

Outra biblioteca muito famosa é a `Pandas`, que dá suporte para avaliarmos os nossos dados. São dados que estamos utilizando, dados que são gerados por aprendizado, dados gerados por meio de testes e de treinamento.

Isso é muito importante para o nosso uso, porque precisamos validar os nossos sistemas. Não basta apenas treinar; precisamos, como eu disse para vocês lá no início, aplicar uma prova no nosso sistema, assim como um professor aplica uma prova para o seu aluno.

`⏱ 24:00`

Temos um exemplo de uma situação onde peguei uma imagem do Google e rodei uma rede que se chama `Mask RCNN`. Vocês podem ver que eu coloquei aquela imagem bem famosa dos Beatles, eles estão atravessando a faixa de pedestre. A rede detectou todos eles e detectou os carros lá atrás.

Essa rede está rodando dentro de um ambiente que é o `Colab`. O `Colab` é um ambiente que conseguimos usar para rodar os nossos algoritmos sem precisar instalar nada; está tudo instalado em nuvem. Isso facilita muito a nossa vida, principalmente quando não queremos perder tempo instalando bibliotecas, instalando dependências, ou quando não temos uma máquina potente. Basta ter um navegador na sua máquina rodando, é o suficiente para nós. Vamos usar também essa ferramenta para aplicações práticas.

### Contextualização e Motivação no Processamento de Imagens para Veículos

Meu trabalho de doutorado foi basicamente trazer as informações do trânsito para o veículo autônomo. Para isso, o veículo precisa detectar:

- Sinaleira vermelha;
- Placa de pare;
- Sinaleira verde;
- As faixas da rua (faixas horizontais);
- Trechos em obra;
- Situações que não estão no mapa de GPS.

Por exemplo, se uma ponte caiu, essa informação não estará no mapa de GPS. Se o veículo usar apenas o mapa, ele cairá nesse buraco. Meu sistema detecta os sinais de trânsito e passa essa informação para o veículo.

### Implementação Técnica

Para isso, eu usei uma rede que se chama `YOLO`, que é uma rede de Deep Learning. Utilizamos essa rede em conjunto com a rede `Inception V3`, que é uma rede de classificação e uma das mais utilizadas em projetos de imagens. Essa rede é a mesma que vocês têm no celular para reconhecer o rosto de vocês.

Vamos aprender a treinar uma rede dessa. Isso é muito importante para que possamos ver, além do algoritmo, como a rede se comporta para diferentes dificuldades de imagens.

## Relacionado

- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
- [[04 - Os Tipos de Agentes de IA]]
