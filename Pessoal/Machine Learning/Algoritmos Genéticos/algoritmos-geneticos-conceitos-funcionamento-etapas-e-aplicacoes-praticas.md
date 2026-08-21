---
titulo: "Algoritmos Genéticos: Conceitos, Funcionamento, Etapas e Aplicações Práticas"
tags: [machine-learning, algoritmos, otimizacao, ia, agentes-de-ia, fundamentos]
data: 2026-08-21
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 30
conceitos: [Algoritmos genéticos, Função fitness, População inicial, Recombinação (Crossover), Mutação, Convergência prematura, Busca heurística, Comportamento de agentes]
---

# Algoritmos Genéticos: Conceitos, Funcionamento, Etapas e Aplicações Práticas

> [!resumo] Do que se trata
> Apresenta os fundamentos dos algoritmos genéticos como métodos bioinspirados de otimização e busca heurística em machine learning. Explica o ciclo evolutivo composto por população inicial, avaliação por função fitness, seleção, recombinação (crossover) e mutação. Demonstra a utilidade na exploração de regiões de busca complexas e aplicações práticas no comportamento de agentes em jogos, chatbots e otimização de rotas.

## Para lembrar

- **A função fitness é responsável por avaliar o desempenho e selecionar os melhores indivíduos de uma população para a próxima geração.**
- **A recombinação cruza os cromossomos (vetores de parâmetros, frequentemente binários) dos pais selecionados para gerar filhos com soluções potencialmente melhores.**
- **A etapa de mutação altera aleatoriamente parâmetros nos cromossomos para introduzir diversidade genética e evitar a convergência prematura para ótimos locais.**
- **Algoritmos genéticos operam delimitando regiões de busca para encontrar soluções heurísticas ótimas em problemas onde testar todas as combinações seria inviável.**
- **Em jogos e chatbots, algoritmos genéticos são aplicados para variar o comportamento de agentes e recombinações de diálogos, impedindo respostas repetitivas e previsíveis.**

## O que esta nota responde

- Qual é a função da mutação dentro do ciclo de um algoritmo genético?
- Como a função fitness atua na seleção e evolução dos indivíduos de uma população?
- Quais são as principais etapas de execução de um algoritmo genético?

## Conceitos

**Algoritmos genéticos** · **Função fitness** · **População inicial** · **Recombinação (Crossover)** · **Mutação** · **Convergência prematura** · **Busca heurística** · **Comportamento de agentes**

## Conteúdo

`⏱ 00:00`

Meu nome é Diego Bruno e hoje vamos ver um conteúdo relacionado aos algoritmos genéticos. Vamos ver uma teoria sobre esse assunto e também a parte prática.

Os algoritmos genéticos são de essencial importância para a área de *machine learning*. Eles vieram da computação bioinspirada com a ideia de criar modelos baseados no comportamento genético biológico. Há uma relação direta entre os algoritmos genéticos e a genética biológica.

Basicamente, utilizamos a base dos algoritmos genéticos voltados para o que existe nas espécies biológicas, como os seres humanos e os animais.

Por exemplo, podemos observar a evolução humana, desde um macaco até o que somos hoje. Trabalhamos com adaptações ao mundo que vivemos. Se pegarmos o início, andávamos de quatro, e hoje andamos em pé. Essa evolução genética acontece porque as espécies são melhoradas para o contexto em que sobrevivem.

Outro exemplo é o dos peixes que vivem em cavernas totalmente escuras, sem luz. Eles acabam não desenvolvendo mais a visão e desenvolvendo outros sensores para perceber o ambiente. A genética acontece em diversas situações. Na raça humana, por exemplo, seres mais evoluídos já nascem sem o dente do siso, porque é um dente que só causa problemas. A genética busca melhorar o que somos, não só para a raça humana, mas também para outras espécies.

### Estrutura do Algoritmo Genético

O algoritmo genético gera uma população de indivíduos. Essa população de indivíduos será avaliada por uma função que chamamos de `função fitness`. Essa função vai avaliar quais são os melhores indivíduos que foram gerados na nossa população inicial.

Imagine que temos uma população mundial que é gerada de forma não coordenada. Depois, usamos uma função para avaliar os melhores indivíduos. Isso é parecido com o mundo de hoje, por exemplo, ao avaliar um funcionário com as especialidades que estamos buscando em programação em JavaScript para uma determinada área de conhecimento.

Temos uma seleção dos melhores elementos.

O processo funciona assim:

1.  **População Inicial:** É gerada uma população inicial.
2.  **Avaliação:** Avaliamos quais são as melhores amostras.
3.  **Seleção:** Isso gera uma população pré-selecionada, que será recombinada.
4.  **Recombinação:** Chamamos essa população que será recombinada de "pais". Esses pais vão recombinar para gerar filhos, que teoricamente serão elementos melhorados. Eles são melhorados porque recombinamos dois pais que têm um potencial bom e que foram selecionados.
5.  **Mutação:** Depois disso, aplicamos um parâmetro, uma função, que vai gerar uma mutação sobre os nossos parâmetros. Pegamos os nossos cromossomos, que são os elementos que foram recombinados, e geramos uma mutação que vai diferenciar os elementos, evitando uma convergência prematura.

`⏱ 06:20`

Que fosse em relação à humanidade, mesmo as pessoas realizando o cruzamento, chegaria um ponto em que todo mundo seria igual. A gente tem a mutação da cor dos olhos, da cor da pele, da cor do cabelo e outras características, não que são menos visuais, mas também acontecem para que a gente tenha pessoas que são diferentes e também são pessoas que podem, por meio da mutação, ter algumas melhorias, certo? É o que o algoritmo genético busca.

Mas, na verdade, a gente sabe que na biologia, uma mutação também pode gerar uma situação que não vai melhorar o indivíduo, na verdade vai piorar. Mas não é isso que a gente vai procurar dentro de um algoritmo genético, obviamente.

### Etapas do Algoritmo Genético

Eu expliquei as etapas do algoritmo genético por cima, e aqui a gente vai ver de uma forma mais completa. Tentei fazer uma explicação bem detalhada das etapas.

O algoritmo vai fazer o quê? Ele vai gerar uma população de forma aleatória. Vai gerar vários elementos.

Mas o que seria um elemento para um algoritmo genético? Seria uma posição de um GPS para que eu consiga gerar uma nova rota, seria uma quebra de senha, então seria um valor. Valores aleatórios gerados para ver se aqueles valores são gerados e satisfazem o meu...

É claro que quando a gente vai gerar uma população, a gente cria uma região de interesse, e dentro dessa região de interesse a gente gera os nossos valores. Eu defino muito bem a variação que as minhas amostras podem ter.

Lembrando do conteúdo introdutório de *machine learning*, voltado para computação heurística, onde a gente não tem uma solução pré-definida. Aqui, nesse caso, a gente não tem um valor pré-definido, um valor exato. A gente tem um universo de possibilidades que uma possibilidade pode satisfazer o meu problema.

O algoritmo genético é um algoritmo heurístico, ou seja, ele não é determinístico. Ele não vai gerar uma resposta exata. Vai gerar uma resposta aproximada do que eu espero como solução do meu problema.

### Geração e Avaliação da População

Essa população é gerada. Essa população é criada e a gente vai ter uma função *fitness*. Essa função vai ser uma função que vai avaliar as minhas amostras e se essas amostras estão dentro de um ranking aproximado do que eu quero.

A minha função vai avaliar quais são as minhas melhores opções dentro da minha geração da população inicial.

Vamos dar um exemplo numa navegação de um robô móvel, de um movimento autônomo ou até mesmo de um algoritmo que gera uma rota para você no seu carro, como um algoritmo do Waze e tudo mais.

Sempre a gente vai querer a solução que o desvio de rota, caso aconteça um acidente, por exemplo, o desvio de rota seja a solução menor possível, porque você quer economizar tempo e combustível, economizar a parte física do seu carro: pneu, freio, motor. Então, tudo isso é importante quando a gente tem um desvio de rota. Você quer pegar a menor distância possível para desviar.

A minha função *fitness* vai avaliar os indivíduos que têm a menor distância para realizar um desvio de rota, certo?

Se a gente pegar uma rota também de uma rede de comunicação de dados, também eu vou traçar a menor rota possível, com o menor custo. A função *fitness* vai avaliar isso.

E aí a gente tem uma população ordenada segundo o valor da função que a gente gerou da função *fitness*. A gente vai ter a população ordenada, certo? Por meio dessa população ordenada, entre os melhores, o que eu vou fazer?

`⏱ 11:20`

basicamente, o que a genética faz. A gente vai pegar os melhores indivíduos e vai fazer um cruzamento com eles. certo? E o que seria esse cruzamento para um valor numérico? A gente imagina lá na computação biológica que a gente está... Sendo inspirado pela natureza. Na natureza, a recombinação é feita por dois cromossomos. Os dois cromossomos são unidos, recombinados. Agora, e na computação biológica? O que a gente tem? A gente vai pegar esses dois vetores. de informação, como a gente já imagina uma computação bioinspirada em nível de hardware, lá no final mesmo da execução, você pode programar em outra linguagem, ter valores decimais, hexadecimais e tudo mais, porém, quando a gente executa lá no... processador, a gente imagina que o nosso cromossomo o nosso vetor de valores é um vetor binário então eu vou ter valores binários num vetor e eu vou cortar eles no meio e recombinar igual a gente está fazendo aqui na imagem Espera-se que por meio disso, eu tenho as duas melhores soluções. Eu vou recombinar elas, eu vou gerar um filho que é melhor do que os pais. Está certo? Então eu tenho uma geração de uma distância. Eu tenho as duas primeiras distâncias menores para o robô desviar a rota. Quando eu faço essa recombinação... eu teria uma distância menor ainda, certo? Então seria mais ou menos essa ideia. Com a função fitness, novamente, eu vou selecionar os indivíduos melhores depois do cruzamento, da recombinação, ? E depois disso eu vou ter... ter uma nova população de tamanho, N mais X, que é a população inicial mais a população recombinada, e eu vou rodar essa função fitness, então, para encontrar os melhores elementos, os melhores elementos da minha população, certo? Depois disso, a gente... vai ter a função de mutação. Depois de aplicar a recombinação, a gente vai aplicar a mutação, que vai fazer o quê? Vai pegar uma posição, que na biologia a gente... que a gente chama de gene, a gente vai pegar uma posição dessa e aplicar a mutação. Que no caso, seria a mesma coisa que inverter um valor binário. Então eu tenho um valor binário em 1, a mutação vai jogar ele para 0. E se ele é 0, ele vai para 1. Essa é a nossa mutação. Normalmente, a gente faz a mutação de um ponto só. Então, o valor que é zero vira 1, e se ele é 1, ele vira zero. Ou a gente pode também fazer a mutação de mais de um ponto, como a gente está indicando aqui. Só que o problema de uma mutação de mais de um ponto é mudar muito. minha amostra, então geralmente para um algoritmo normal, a gente vai usar a mutação de um ponto só, depois de feito a recombinação a mutação, a gente vai aplicar a função fitness para avaliar quais os melhores elementos, novamente, porque a minha população A partir da minha população inicial, eu criei uma nova população por meio do cruzamento e da mutação, certo? E aí eu vou ter, com a aplicação da função fitness, eu vou ter um novo ranking. Esse novo ranking vai me mostrar quais os... meus melhores indivíduos, ? E aí eu vou pegar a solução melhor, certo? Então, é mais ou menos dessa forma que acontece um algoritmo genético. Mostrando de forma sintetizada tudo isso, porque ali tinha muita informação. A população inicial vai ser gerada, a gente vai selecionar os melhores indivíduos, a gente vai fazer uma recombinação, gerar a combinação de melhores indivíduos para que tenha uma melhora na população inicial.

`⏱ 16:00`

Depois disso, há uma mutação que pega o meu melhor indivíduo gerado e vai mutar ele. Depois de ser feita a recombinação e gerado esse filho, esse filho será mutado. Eu tenho uma nova amostra na minha população inicial. Ela pode ser melhor ou pior.

A gente busca sempre uma população com indivíduos gerados cada vez melhores por meio da recombinação e da mutação.

### Soluções Heurísticas e Ótimas

É importante destacar novamente que as soluções que geramos são soluções heurísticas e não determinísticas. Não estamos buscando um valor exato; estamos buscando um valor dentro dessa nuvem de valores possíveis.

Quando encontramos a melhor solução aí dentro, chamamos ela de solução ótima global. Essa solução não é necessariamente a melhor solução possível, pode até ser, mas possivelmente ela não será a melhor solução de todas. Porém, ela será uma solução que satisfaz o meu problema.

### Fundamentos dos Algoritmos Genéticos

Os algoritmos genéticos são heurísticos. O fundamento principal para entender os algoritmos genéticos é que trabalhamos com modelos heurísticos.

Para ilustrar como funciona um algoritmo genético, vamos usar um exemplo de região de busca.

Por exemplo, se a gente pegar uma vaga de emprego no LinkedIn, às vezes a empresa vai definir que o trabalho deve ser presencial e não remoto. Ela vai definir prioridades para funcionários que moram naquela região. Por exemplo, a empresa pode definir que é preferível que os candidatos sejam de São Paulo ou Minas Gerais.

Nesse caso, você se candidata porque está dentro dessa área de interesse deles. Eles podem ter um escritório em São Paulo e um em Minas, mas para eles não seria interessante alguém de fora, caso a pessoa não tenha interesse em mudar para essa cidade. Assim, eles definem uma região de interesse.

Muitas vagas de emprego são assim. Definimos uma região de interesse onde o nosso possível funcionário deve morar. Essa região de interesse, ou o estado que estamos definindo, é a nossa primeira região de busca.

Depois, podemos deixar essa distância geográfica de lado e ir para uma seleção por expertise. Queremos que o funcionário saiba JavaScript e que ele tenha noção de front-end. Começamos a definir nossa região de busca.

Não vamos definir um valor exato, como: "Eu quero que meu funcionário tenha 10 anos de experiência" ou "Ele mora em São Paulo, mas na cidade tal, uma cidade específica".

Quando acabamos especificando demais, fica muito mais difícil encontrar mão de obra qualificada para aquilo. Por isso, definimos uma região de busca.

Quando vierem os meus funcionários para fazer o teste, eu vou selecionar o melhor dentro dessa região de busca: quem tem mais experiência, quem se comporta melhor no teste, e tudo mais.

Eu defino uma região de busca para encontrar a minha solução, porque se eu definir muito específico as minhas características, eu não vou encontrar o que estou procurando.

`⏱ 20:40`

Meio aleatório para isso, ? Que um professor meu sempre dava, é assim. Imagina quando você vai encontrar um parceiro ou uma parceira para namorar, para casar. Você não tem como definir. Ah, eu quero uma pessoa que tem 1,90m de altura. Olhos azuis. Que seja programador Que jogue videogame Se eu definir muita coisa E muita coisa específica Eu não vou encontrar ninguém nunca Então a gente define algumas coisas Sei lá O gosto musical da pessoa É uma característica importante para mim. Então, nossa, se a pessoa gostar de sertanejo, nossa, não vou me dar muito bem com ela. Então, tem que ser uma pessoa que gosta de rock para ser do meu estilo e nos shows que eu gosto, ? Mas eu estou definindo uma coisa que é um ponto, ? que eu acho que é importante, e o resto eu deixo em aberto, ? A altura da pessoa, o gosto dela sobre as comidas, eu deixo em aberto, eu só estou definindo uma coisa específica, então isso eu posso até fazer, mas ser tudo de forma específica não é a ideia do... o algoritmo genético, certo? Definição para um algoritmo genético. Então, o algoritmo genético, é uma técnica de busca utilizada na ciência da computação para achar soluções aproximadas em problemas de otimização e busca. Então, a gente sempre vai ter... a aplicação de algoritmos genéticos para encontrar soluções dentro de um universo de busca bem definido, porém, trabalhando com otimização para encontrar a melhor possibilidade dentro do meu universo. E de forma não determinística, certo? Porque a gente já sabe que é um algoritmo que trabalha de forma heurística. Aplicações de algoritmos genéticos. Então, onde que a gente aplica algoritmos genéticos? A gente aplica na navegação robótica, para encontrar a melhor solução possível. para avaliar os obstáculos que eu tenho no meu caminho, qual é a melhor rota possível na inteligência artificial, para mapear um conjunto de conhecimento novo a geração de novos dados, então quando eu preciso gerar novos dados para o meu conjunto de dados e eu não tenho novas amostras. Então, eu vou aplicar algoritmo genético para que eu tenha a geração da minha população que complementa aquela população de elementos que eu já tenho. Então, por exemplo, eu vou gerar dados para... sistema de reconhecimento de imagens eu posso pegar as imagens que eu já tenho e aplicar o algoritmo genético para gerar novas imagens, além daquelas que eu já tenho então o algoritmo genético vai recombinar, mutar e vai gerar novas imagens, novas para minha base de dados. Jogos digitais também, muito aplicado. Então, todo mundo aqui já deve ter jogado um joguinho lá no passado, que sempre que você passava por aquele ponto na tela do jogo, era do mesmo jeito. Então, você sabia como o agente... o jogo se comporta, então você já sabia como derrotar ele, como passar sem ele te perceber, porque você já sabia como ele se comportava. Nos jogos mais modernos a gente pode ver que se você passa pelo mesmo ponto mais de uma vez, aquele agente que está ali, que é um inimigo seu, por exemplo, ele não vai se comportar da mesma forma. Então é uma forma do algoritmo genético mudar o comportamento de um agente que está ali no jogo, certo? Então esse ponto eu vou discutir depois, mas é um ponto bem interessante e uma aplicação muito grande dos algoritmos genéticos. É voltado para a área de games. Aqui uma outra aplicação de algoritmos genéticos é na aplicação em ensino e de chatboots. Então você tem uma conversa com um sistema robótico. Então imagina um robô ensinando uma criança.

`⏱ 25:20`

Ele não pode ter sempre as mesmas respostas ou as mesmas perguntas, porque senão fica algo muito artificial, muito estranho.

Nesse caso, aplicamos algoritmos genéticos para que ele recombine as perguntas. Por exemplo, ele sempre pergunta: "Você gosta de sorvete?". Depois, ele pergunta: "Você gosta de chocolate?". Ele recombina essa pergunta e pergunta: "Você gosta de sorvete de chocolate?". Assim, a pergunta muda um pouco e a interação humano-robô fica melhor. Não fica algo tão repetitivo.

Se você vier aqui no menininho e perguntar dessa forma: "Você gosta de chocolate?", e depois for na menininha e perguntar: "Você gosta de chocolate?", fica algo muito repetitivo. Por isso, ele começa a recombinar as perguntas para fazer algo mais interativo, mais legal, e para influenciar mais as crianças no estudo.

Além das perguntas, ele também gera combinações de respostas. A criança pode fazer uma pergunta para o robô, e ele não dá sempre a mesma resposta. Ele pode recombinar as respostas que tem, falando, por exemplo: "Eu não gosto de chocolate, mas eu gosto de sorvete". Ele recombina as respostas que tem de forma automática. O sistema vai gerando, com essa recombinação, uma população de respostas, uma base de dados maior, o que torna o sistema mais robusto para aquela aplicação.

### Vantagens dos Algoritmos Genéticos

Perguntas e respostas é uma grande sacada dos algoritmos genéticos, porque podemos ir recombinando e mutando as nossas perguntas e respostas.

Na mutação de uma resposta, por exemplo, eu poderia, sei lá, falar que eu gosto de sorvete de chocolate, mas eu vou inverter o sabor, então eu falo: "Ah, eu gosto de sorvete de chocolate, mas eu prefiro de morango". Assim, eu complemento a minha resposta e gero uma resposta melhor para o usuário, deixando o sistema mais próximo de morango.

### Integração e Comportamento de Agentes

Tem toda essa parte de integrar o sistema com o usuário, mas há também a parte forte que é o foco da interação.

O algoritmo genético pode dar essa possibilidade para a gente, como é feito em um jogo (`game`). Eu posso mudar o comportamento dos meus agentes para ficar algo mais real, porque eu não preciso passar sempre no mesmo ponto do jogo e ter o agente com o mesmo comportamento. Fica algo meio chato. Agora, se eu tenho algo mais dinâmico, fica mais interessante.

A mesma coisa se aplica à aplicação de um algoritmo genético para mudar o comportamento do agente robótico, das perguntas que ele recebe, das respostas que ele vai dar e das perguntas que ele vai fazer. Isso torna o sistema mais próximo do que é humano.

### Aplicações Práticas

Aqui temos um exemplo do planejamento de rota, onde é gerado um desvio de rota. O robô está indo reto, encontra um obstáculo no caminho e ele tem que gerar um desvio. Quando ele gera esse desvio, ele vai tentar gerar a melhor solução possível. Ele vai tentar gerar a solução de desvio que é a menor possível, para gastar menos energia e menos tempo, e ter um desgaste menor do robô também.

O algoritmo genético vai gerar algumas amostras de desvio aqui: uma amostra na frente dessa pessoa, uma amostra mais aqui à direita, uma amostra mais para o centro. E aí ele vai selecionar qual é o ponto melhor para fazer esse desvio.

Isso acontece também no roteamento de redes. Por exemplo, redes de internet: encontrar o melhor caminho para o fluxo de dados. Quando eu tenho uma rede muito complexa, eu não tenho como fazer isso de forma determinística, definindo: "Ah, esse é o melhor caminho". Então, o algoritmo genético vai gerar para mim o melhor caminho possível.

`⏱ 30:00`

Vamos ver os métodos aplicados para algoritmos genéticos.

## Relacionado

- [[metodos-bioinspirados-redes-neurais-e-logica-fuzzy-em-machine-learning]]
- [[logica-difusa-redes-neurais-generalizacao-e-algoritmos-bioinspirados]]
- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
- [[redes-neurais-artificiais-conceitos-estrutura-e-aplicacoes-em-machine-learning]]
