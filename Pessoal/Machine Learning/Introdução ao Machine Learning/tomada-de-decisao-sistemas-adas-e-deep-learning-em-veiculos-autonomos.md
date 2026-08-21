---
titulo: "Tomada de Decisão, Sistemas ADAS e Deep Learning em Veículos Autônomos"
tags: [machine-learning, ia, conceitos, caso-pratico, estudo]
data: 2026-08-21
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 19
conceitos: [tomada de decisão autônoma, sistemas ADAS, Neuro FSM, visão computacional, oclusão visual, rede SegNet, detecção de infrações]
---

# Tomada de Decisão, Sistemas ADAS e Deep Learning em Veículos Autônomos

> [!resumo] Do que se trata
> Apresenta a arquitetura de tomada de decisão em veículos autônomos, destacando o papel dos módulos de inteligência artificial como o elemento julgador em cenários dinâmicos. Explora aplicações práticas de segurança, assistência ao motorista (ADAS) e monitoramento comportamental por meio de visão computacional e do modelo Neuro FSM. Discute os desafios de detecção de placas com oclusão e o uso de redes de deep learning, como a SegNet, na navegação e identificação de vias.

## Para lembrar

- **O módulo de tomada de decisão atua como o juiz centralizado do veículo, avaliando o contexto dinâmico para evitar colisões antes de executar comandos como frenagem brusca.**
- **A visão computacional associada a machine learning permite que o veículo navegue com segurança fora do mapa de GPS ao detectar trechos em obras, desvios e vias não mapeadas.**
- **O sistema Neuro FSM combina redes neurais artificiais com máquinas de estados para avaliar e transicionar entre diferentes condições de trânsito e sinalizações.**
- **Sistemas ADAS utilizam predições inteligentes para executar manobras de emergência, como conduzir o caminhão ao acostamento quando detectam sonolência no motorista.**
- **Modelos preditivos mantêm alta taxa de acerto na identificação de placas com oclusão parcial (como placas de pare e sentido), mas perdem precisão quando valores numéricos específicos estão cobertos.**

## O que esta nota responde

- Como funciona a arquitetura de tomada de decisão e o sistema Neuro FSM em veículos autônomos?
- De que forma a visão computacional auxilia a navegação do veículo quando o mapa de GPS está desatualizado?
- Por que oclusões parciais afetam mais o reconhecimento de placas de velocidade do que de placas de sinalização padrão?

## Conceitos

**tomada de decisão autônoma** · **sistemas ADAS** · **Neuro FSM** · **visão computacional** · **oclusão visual** · **rede SegNet** · **detecção de infrações**

## Conteúdo

`⏱ 00:00`

A arquitetura de um carro autônomo é complexa e gigante, mas ela é dividida em módulos.

O meu módulo, por exemplo, é o de detecção de sinais de trânsito. Existem outros módulos, como:

- O módulo de planejamento de rota, que visa planejar o caminho menor possível para economizar combustível e tempo.
- Um módulo de mapa.
- Um módulo de interface humana, onde o usuário pode dizer por áudio, digitar ou clicar em uma tela para indicar o destino.

O sistema possui vários módulos, e na maioria deles, envolve `machine learning` e `inteligência artificial`. O elemento centralizado que toma a decisão é o nosso "juiz".

### A Necessidade da Tomada de Decisão

Por que um veículo precisa tomar uma decisão? Porque o nosso mundo é dinâmico. O veículo precisa tomar uma decisão para não gerar um acidente ou para tomar a melhor decisão possível.

Vou dar um exemplo. Meu sistema detecta placas de trânsito. Eu estou navegando e detecto uma placa de 40 km/h. Obviamente, a decisão é reduzir a velocidade para 40. No entanto, eu posso estar entrando em um trecho em obra, onde a redução de velocidade é para 40, mas o veículo que está atrás de mim, um caminhão carregado, não viu isso. Se eu reduzir bruscamente, esse caminhão vai bater atrás de mim.

Nesse caso, eu tenho que verificar se há um veículo atrás. Se não houver, eu verifico se a minha redução de velocidade é segura. Se não for, eu não posso reduzir a velocidade drasticamente. Eu terei que ir reduzindo aos poucos.

Quem toma a decisão do que o veículo deve fazer é esse sistema de tomada de decisão, que é o "juiz" do carro.

No nosso caso, quem é o nosso juiz quando estamos dirigindo um carro? É o nosso cérebro. Ele vai avaliar o que pode ser feito da melhor forma, com base nas situações que já passamos e que colocamos para o sistema do veículo treinar.

Por exemplo:

- O que eu faço quando detecto um pedestre na faixa? Eu tenho que frear.
- O que eu faço quando o sistema detecta que a pista está molhada? Reduzir a velocidade e ligar o controle de tração.

Tudo isso é baseado em situações que são exemplos para o veículo funcionar. Por meio desses exemplos, treinamos o sistema e ele começa a funcionar de forma inteligente.

### Exemplos de Sistemas de Segurança

Aqui tem um sistema, por exemplo, que desenvolvi no doutorado, que é o sistema de planejamento de rotas. Esse sistema consegue nos dar uma base.

Por exemplo, eu desenvolvi um sistema que, quando detecto que o motorista dormiu no volante, eu entro em uma rota vermelha, que é a rota de solução, e estaciono o caminhão no acostamento. É uma medida de segurança previamente treinada na base de dados do veículo.

Outras situações problemáticas:

- Uma via perto da minha cidade onde a ponte caiu. A sinalização foi colocada muito em cima, e várias pessoas caíram com o carro aí dentro. O trecho auxiliar é muito mal sinalizado, então poucas pessoas viam isso.
- Agora, quando a gente pega uma obra bem mais estruturada, o que acontece? Eles começam a colocar cone antes, placa de velocidade reduzida, lombada.

`⏱ 04:40`

O sistema de visão computacional consegue detectar essas situações e fazer com que o veículo navegue fora do mapa de GPS até encontrar novamente a rota de GPS. Ou seja, até sair desse trecho não mapeado. Para isso, precisamos usar visão computacional, utilizando processamento de imagem e *machine learning*.

#### Demonstração de Avaliação de Via

Aqui temos um exemplo de situação onde conseguimos avaliar a via com a câmera. Assim, conseguimos avaliar não apenas a via, mas também as faixas dela, possibilitando fazer uma ultrapassagem e detectando a distância dos carros à frente.

*   O carro contornado em vermelho está a 10 metros do meu carro.
*   Aquele carro à esquerda está a 18 metros.
*   Aquele outro da faixa da direita está a 41 metros.

Por que é importante saber isso? Para saber se a minha manobra é possível de ser realizada. E quem detecta essa via e os carros? É uma rede de *deep learning*, e nós vamos aprender a treinar esse tipo de rede para diferentes situações.

#### Aplicações em Outras Áreas

Um aluno pergunta: "Professor, eu quero treinar uma rede para detectar pragas na plantação. Eu quero treinar uma rede para detectar animais numa floresta e contar quantos tipos? Quantos de cada tipo tem? Quantas onças, sei lá, quantas capivaras? O sistema consegue fazer isso?"

#### Objetivo do Sistema: Assistência ao Motorista

Nossa ideia, basicamente, não é somente trazer um sistema autônomo para o veículo; é também trazer um sistema para ajudar o motorista. A gente acompanha o que está acontecendo com o motorista e o que está acontecendo lá fora.

#### A Importância da Prevenção

Por que tudo isso é importante? Vamos dar um exemplo. Todo mundo já deve ter feito uma viagem onde se vê aquelas frenagens de caminhão ou de carro. Você pensa: "Nossa, o motorista aqui, olha, ele dormiu no volante e saiu da pista."

Isso ocorre porque já fazemos um pré-julgamento. Porém, ao observar o que o motorista fez em relação ao que aconteceu lá fora, podemos observar que talvez um carro fechou ele ou uma vaca entrou na pista, e aí vemos que ele freou bruscamente para evitar uma colisão.

#### Detecção de Infrações

Apenas 1% do que é feito de errado no trânsito é detectado por policiamento, por radares ou por comandos da polícia. Isso é muito pouco. 99% das infrações não são detectadas.

Se o meu veículo está navegando e o motorista não está dentro da velocidade, ele passou por uma placa de 90 e está a 120, o meu sistema consegue penalizá-lo automaticamente.

#### Avaliação Comportamental e Benefícios

Nosso sistema consegue avaliar como o motorista está dirigindo. É uma espécie de *Big Brother* dentro do carro, mas é pela segurança.

Um aluno questiona: "Professor, mas no final do dia, o motorista, dependendo de como ele dirigir, ele vai perder a carreira, a carteira de motorista?"

É bom que ele perca a carteira de motorista e não matar uma família por meio de um acidente de trânsito.

Sabendo que o nosso carro já avalia como estamos dirigindo, não vamos ficar dirigindo de qualquer jeito, porque o nosso próprio carro vai avaliar como estamos dirigindo e vai reduzir muito os acidentes de trânsito.

Além disso, há o lado de trazer um benefício para o motorista. Se você não cometeu nenhuma infração de trânsito, a gente vai descontar um valor do seu IPVA.

Isso é legal para o governo? Sim, porque um acidente de trânsito gera um impacto muito negativo para o financeiro do serviço público de saúde. Ao economizar nessa parte, conseguimos...

`⏱ 09:40`

dar um auxílio para o imposto do veículo, por exemplo. Nossa ideia é acompanhar o que acontece lá fora do carro e dentro do carro.

Acompanhamos:
- A placa de velocidade e a velocidade do carro;
- O semáforo e se o freio está sendo acionado ou não para o semáforo vermelho;
- Como o motorista está dirigindo o carro ou o caminhão.

Neste caso, por exemplo, usamos um Kinect. O Kinect do Xbox fica dentro do caminhão, e conseguimos saber se o motorista está:
- Com a mão na orelha;
- Falando no celular;
- Se abaixou a cabeça e dormiu;
- Se teve um mal súbito.

O que faremos? Vamos ajudar ele, por exemplo, estacionando o caminhão no acostamento ou simplesmente dando um alerta, como: "Você está falando no celular, pare com isso." Se ele não parar, vamos reduzindo a velocidade do caminhão até parar.

### Sistema Neuro FSM

O sistema que usamos para avaliar tudo isso se chama Neuro FSM. É uma rede neural junto com uma máquina de estados.

O que é cada estado?
- Quando detecta uma placa de velocidade, é um estado.
- Quando eu detecto um semáforo vermelho, é um estado.
- Ficou amarelo, outro estado.
- Ficou verde, outro estado.

A gente avalia os estados por meio de um método de *machine learning* baseado em rede neural artificial. Assim, conseguimos acompanhar tudo o que está acontecendo com o veículo.

### Aplicação em Simulação e ADAS

Aqui temos um exemplo de simulação do caminhão em funcionamento no simulador. Implementamos esses algoritmos no caminhão para manobras.

O sistema é o ADAS, que significa Sistemas Avançados de Suporte ao Motorista. Ele consegue ajudar o motorista em uma manobra de emergência.

**Cenário de Exemplo:**
Eu detectei que o motorista dormiu no volante, mas há um carro impedindo a manobra. Eu começo a reduzir a velocidade, deixo o carro ir embora e estaciono o caminhão no acostamento.

Para isso, utilizei três métodos de *machine learning*:
1. Um método para detectar o problema do motorista.
2. Um outro método para conseguir estacionar esse veículo no acostamento.
3. Um terceiro método com câmeras externas para ver se é possível fazer essa manobra, se não há ninguém pedindo, e se há mesmo acostamento ou não.

### Primeiro Artigo de Pesquisa (2017)

Vou falar do meu primeiro resultado utilizando *Machine Learning* com redes de *Deep Learning*. Este foi meu primeiro artigo, da minha primeira pesquisa de doutorado, publicado no ano de 2017.

O que fiz? Uma janela que percorre a imagem, uma matriz que percorre a imagem toda. Quando ela bate num local que tem uma placa, ela recorta ela e classifica.

No entanto, esse método não é inteligente. Por quê? O algoritmo fica percorrendo a tela o tempo todo. Numa imagem, ele chega a fazer 500 recortes. É muita coisa! Ele tem que classificar 500 imagens para ver se tem uma placa ou não. O tempo disso é muito alto, e o custo computacional é grande.

Foi meu primeiro artigo e funcionou bem. Mas é algo que a gente não usa mais hoje.

Por que estou mostrando esse trabalho? Porque mesmo que a gente tenha uma placa pela metade ou só um pedaço dela, como por exemplo essas três primeiras, que são recortes da placa de pare, a gente já consegue classificar a placa.

`⏱ 14:20`

A rede consegue fazer uma previsão do que está faltando no restante, que está ocluso.

Professor, mas onde é que vai ter uma placa pela metade? Em locais onde tem grama tampando, árvore, e tem muito disso, a gente consegue avaliar essas placas também, certo?

Quando é uma situação que a gente não consegue avaliar? Quando algum dígito está totalmente tampado, por exemplo, essa placa C, final zero, que placa que é? Não sei, pode ter um 8 ali, pode ter um 7, pode ter o 10. Então eu não sei fazer uma previsão.

Agora, uma placa de pare, uma placa de pedestre, uma placa de sentido obrigatório, eu consigo fazer uma previsão daquilo que está na oclusão, e a taxa de acerto é bem alta.

Os resultados da nossa rede, quando a gente usa valores numéricos, são menores, porque as oclusões geram problemas em valores numéricos, que são esses problemas que comentei aqui com vocês.

### Redes de Deep Learning para Detecção

Falando um pouco das redes, a gente tem:

*   **Rede SegNet:** É uma rede de *deep learning* que roda sobre as imagens. O resultado da rede é essa aqui, e é um resultado bom. A gente está conseguindo ver o que é rua, o que é carro, que a pessoa, que a árvore, o que é placa. O que é que precisa melhorar nisso? A gente vai ver o que precisa melhorar.

*   **YOLO (You Only Look Once):** É outra rede. A YOLO tem uma detecção das regiões de interesse. Ela fala para você onde tem carro, onde tem pessoa, onde tem placa, onde tem semáforo. A YOLO é muito utilizada em sistemas de detecção de criminosos. Japão, a China, eles têm sistemas, por exemplo, no estádio de futebol, que conseguem detectar uma pessoa e, por meio do rosto dela, ver se é um foragido. Isso auxilia para ver se o policiamento está dando conta daquele problema.

*   **Mask R-CNN:** Essa rede consegue, além de detectar com a caixa o objeto, ela consegue segmentar o objeto. Segmentando o objeto, a gente consegue definir onde é que está o objeto mais precisamente. Vocês podem ver aqui que tem um motociclista que foi detectado, até a mochila dele, a mochila, a pessoa e a moto, foi tudo detectado, certo?

*   **DeepLab:** Aqui é outra rede. A imagem parece uma pintura de tão perfeita que ela consegue detectar tudo isso na imagem.

Nossa, mas precisa melhorar algo ainda nisso? Lembrando que aqui é uma rede em 2D, uma rede que trabalha em imagens 2D. Então, precisa ter melhoria nessas imagens, nesse método de *Machine Learning*.

Perfeito. Se a gente pegar essa ciclista, ela foi pintada corretamente, a bike dela também. O que precisa melhorar aqui? A gente vai ver o que precisa melhorar.

## Relacionado

- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
- [[03 - Desbloquear Soluções com IA Generativa]]
- [[01 - A Vantagem da IA]]
