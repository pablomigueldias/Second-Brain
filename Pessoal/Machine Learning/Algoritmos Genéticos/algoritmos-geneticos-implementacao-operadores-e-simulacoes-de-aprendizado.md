---
titulo: "Algoritmos Genéticos: Implementação, Operadores e Simulações de Aprendizado"
tags: [machine-learning, algoritmos, otimizacao, conceitos, caso-pratico]
data: 2026-08-22
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 27
conceitos: [População inicial, Espaço de busca, Seleção por roleta, Diversidade genética, Recombinação, Mutação, Comportamento de agentes]
---

# Algoritmos Genéticos: Implementação, Operadores e Simulações de Aprendizado

> [!resumo] Do que se trata
> A aula detalha o funcionamento computacional dos algoritmos genéticos, desde a definição da população inicial em um espaço de busca até os métodos de seleção, recombinação e mutação. São exploradas as dinâmicas de seleção probabilística por roleta, que preservam a diversidade genética ao manter amostras minoritárias. Por fim, são demonstradas aplicações práticas em jogos digitais, simulação de locomoção de agentes e resolução de problemas clássicos de otimização.

## Para lembrar

- **A geração da população inicial (passo zero) define uma região de busca com limites mínimos e máximos antes de gerar amostras aleatórias.**
- **O método de seleção por roleta distribui probabilidades proporcionais ao desempenho, sem excluir indivíduos de menor aptidão para manter a diversidade.**
- **O cruzamento entre uma amostra boa e uma ruim pode gerar indivíduos melhores do que o cruzamento exclusivo entre duas amostras boas.**
- **Em jogos digitais e simulações, algoritmos genéticos permitem gerar comportamentos não repetitivos em inimigos e treinar locomoção ao longo de centenas de gerações.**

## O que esta nota responde

- Como funciona o método de seleção por roleta em um algoritmo genético?
- Por que é importante manter amostras com baixa aptidão na seleção de indivíduos?
- De que forma os algoritmos genéticos são aplicados para simular aprendizado e locomoção em jogos?

## Conceitos

**População inicial** · **Espaço de busca** · **Seleção por roleta** · **Diversidade genética** · **Recombinação** · **Mutação** · **Comportamento de agentes**

## Conteúdo

`⏱ 00:00`

### Métodos do Algoritmo Genético

Vimos como o algoritmo genético se comporta a partir da sua inspiração na biologia e na natureza. Agora, veremos a parte computacional: como o algoritmo manipula os dados numéricos de forma eficiente para gerar a resposta esperada.

### População Inicial (Passo Zero)

Para implementar um algoritmo genético, o chamado "passo zero" consiste em gerar a população inicial. Ele é classificado como passo zero porque, muitas vezes, é uma etapa *offline*: você já pode ter uma população gerada pelo algoritmo ou estar usando uma base de dados prévia com amostras, não sendo necessário gerá-las do zero.

Essa população inicial é criada dentro de uma região de busca. São definidos limites para que as soluções sejam geradas inicialmente. Isso não significa que já se conhece a resposta final necessária, mas que se tem uma noção do espaço de busca em que se quer trabalhar. 

A exemplo da busca por um parceiro, uma parceira ou um funcionário: sabe-se mais ou menos o que se espera na procura, mas não há certeza de quão boa será a amostra para solucionar o problema. 

Por isso, define-se uma região de busca com valores mínimos e máximos, e a população inicial é gerada de forma aleatória. Em um exemplo com valores entre 0 e 1, o processo envolve:

- Definir a quantidade de casas decimais a serem trabalhadas;
- Definir o tamanho da população a ser gerada (por exemplo, 100 valores);
- Definir os limites mínimos e máximos;
- Gerar a população inicial.

### Método de Seleção

Após a geração da população inicial, passa-se para o método de seleção, no qual são selecionados os melhores indivíduos.

O método mais utilizado é a seleção por roleta. Ele funciona de forma semelhante a uma roleta de sorteio de prêmios de programas de TV — como no *Bom Dia e Cia* com o apresentador Yudi, em que as crianças queriam o PlayStation e a roleta parava no Jogo da Vida.

A nossa roleta computacional funciona dessa forma, dividida em regiões de probabilidade. Não se trata de uma roleta viciada, mas de uma roleta com diferentes proporções de probabilidade. 

Pensando no estoque de prêmios do programa: se houvesse muitas bicicletas para sortear, seria definida uma região maior (por exemplo, uma região C4) com mais bicicletas, tornando a probabilidade de sorteá-las bem mais alta. 

No algoritmo genético ocorre algo semelhante: após gerar a população inicial, obtêm-se valores de avaliação para cada amostra, permitindo identificar quais delas estão mais próximas ou mais distantes da solução final esperada.

`⏱ 05:20`

### Seleção e Manutenção da Diversidade

Ele vai ter, por exemplo, amostras dentro de `C4`, que é uma região maior da roleta. Isso significa que `C4` tem muito mais chance de ser escolhido, porque a sua função de valores é mais próxima do objetivo desejado.

Por que mantemos `C6` se ele tem um valor de certeza tão baixo? Porque não adianta selecionar sempre os melhores. Às vezes, o cruzamento entre uma amostra boa e uma não tão boa — ou entre uma boa e uma ruim — é melhor do que o cruzamento entre duas amostras boas. Existe essa dinâmica dentro dos algoritmos genéticos e, por isso, temos uma seleção por probabilidade que não exclui as minorias da população.

### Recombinação de Indivíduos

Depois de selecionados os indivíduos, aplica-se um método de recombinação, que consiste em recombinar as duas melhores soluções. 

Neste caso, utiliza-se um método de recombinação de ponto único:
- Há um ponto em que o vetor é dividido;
- Os dois últimos números são quebrados;
- Realiza-se a inversão: a parte verde vai para a amarela e a parte amarela vai para a verde.

Dessa forma, trocam-se os genes do pai e da mãe para gerar a recombinação. 

Esse algoritmo de recombinação já é aplicado diretamente nos valores binários. Esse procedimento é padrão na execução do algoritmo, pois rodar diretamente nos dados que operam no processador gera maior precisão e velocidade.

A recombinação vai atuar sobre os dois melhores indivíduos selecionados pelo método da roleta, com a meta de gerar um indivíduo melhor. Nem sempre isso dá certo; às vezes, o filho é pior do que seus pais. Quando isso ocorre, em vez de selecionar o filho, os pais continuam valendo como as melhores amostras.

### Mutação

A mutação é aplicada para evitar a convergência prematura do algoritmo. Conforme a população vai sendo gerada e recombinada, pode chegar um momento em que todos os indivíduos fiquem iguais, sem diferença entre um elemento e outro.

Na natureza, a mutação ocorre com a mesma finalidade. Existem casais, por exemplo, que não possuem ninguém ruivo na família e geram um filho ruivo, evitando que a espécie entre em uma convergência prematura na qual filhos e netos se tornem todos iguais. A mutação impede a geração de uma população excessivamente idêntica à família anterior dentro da árvore genealógica.

Na prática do algoritmo, a mutação é um processo simples:
- Em uma cadeia de valores binários, escolhe-se uma posição para mutar;
- Dada a cadeia `1, 1, 0, 0`, escolhe-se mutar o terceiro valor (poderia ser qualquer outro);
- Se o valor for `1`, ele passa a ser `0`; se for `0`, passa a ser `1`.

Embora pareça uma alteração simples de apenas um bit, o cromossomo passa a representar uma amostra completamente diferente, evitando a convergência prematura.

`⏱ 10:00`

A mutação é feita de forma aleatória. Eu posso mutar um valor da população ou mais valores, e isso vai depender do meu método de escolha. 

### Algoritmos Genéticos em Jogos Digitais

Sobre o funcionamento do algoritmo genético, há muitos jogos digitais, principalmente os games atuais, em que estamos cada vez mais exigentes tanto com a parte gráfica quanto com a jogabilidade. 

Cada vez mais queremos jogar algo em que, ao entrar numa fase e morrer, ao passar de novo por aquele mesmo agente inimigo, ele não tenha o mesmo comportamento. Você espera que ele esteja numa posição diferente e que o ataque dele seja diferente. Caso contrário, fica muito fácil: você passa por ali, morre, volta e já sabe o que vai acontecer na sua tomada de decisão.

Nos algoritmos genéticos para games, temos a possibilidade de gerar uma população de respostas para o agente, como o inimigo, e gerar um comportamento diferente. Parece que não é um diferencial tão grande para um jogo, mas é. Para quem gosta de videogame, sabe o que estou dizendo: jogar algo cujo comportamento sai da mesmice e, ao zerar novamente o jogo, ele apresenta um novo comportamento, sem ser sempre igual, evitando que o jogo perca a graça.

O algoritmo genético é muito usado para isso: gerar novas soluções, evitando comportamentos repetitivos do agente do game e gerando comportamentos novos para cada agente. Essa é a base quando falamos de jogos digitais envolvendo inteligência artificial dentro desse cenário, falando também de redes neurais.

### Simulação de Comportamento Humano e Dificuldade

Quando você joga um jogo de corrida atualmente contra a máquina e define o nível de dificuldade:

- No nível fácil: os carros começam a acelerar menos e a frear mais nas curvas para que você consiga competir, caso não tenha tanta habilidade no jogo.
- No nível difícil (*hard*): o comportamento dos agentes é melhorado e as velocidades aumentam para dificultar a partida.

Porém, isso costuma ficar muito artificial, pois o carro da máquina nunca bate e sempre dirige perfeitamente. 

O que fazem atualmente: quando alguém joga uma corrida online dentro de um circuito — por exemplo, jogando Fórmula 1 em Interlagos —, o jogador pode ganhar a prova, mas bater no *guardrail*, esquecer de abastecer na hora certa e cometer vários erros humanos. 

O sistema copia essa forma de jogar e a insere dentro de um agente da máquina no jogo. Ao jogar contra a máquina, você joga contra a cópia do comportamento de uma pessoa real. Isso torna o jogo mais real do que enfrentar um agente programado apenas para jogar de forma perfeita. É um agente que bate, sai da pista e encosta nos outros carros para tirar o oponente do trajeto. 

Tudo isso é uma cópia de comportamento de outros jogadores, enquadrando-se nessa capacidade de gerar agentes com comportamentos diferentes. Isso é cada vez mais valorizado nos games, sendo a razão pela qual uma atualização de jogo atual chega a ter 30 ou 40 gigas.

`⏱ 15:00`

### Aprendizado de Locomoção com Algoritmos Genéticos

Depois de falar sobre geração de comportamento, vamos ver como é o aprendizado de um sistema que utiliza algoritmo genético.

Trata-se de um vídeo de um artigo publicado na área de ciência da computação. Temos o modelo de uma pessoa e o sistema vai aprender a andar. Lembrando que o sistema não sabe o que é andar e vai começar do zero. 

Há criaturas com diferentes estruturas:
- Pessoas com pernas mais altas;
- Pessoas com pernas mais curtas;
- Dinossauros.

Vamos ver como o sistema aprende do zero. Primeiramente são mostradas as criaturas e, em seguida, o comportamento de cada uma delas durante o processo de aprendizado.

### Evolução Através das Gerações

O aprendizado começa de um ponto onde o objeto não tem certeza de como é o seu movimento:

- **Gerações 1, 6, 17 e 921:** a geração 17 já aprendeu um pouco a andar;
- **Gerações 1, 99, 216 e 900:** a geração 900 já aprendeu a andar;
- **Gerações 1, 20, 80 e 999:** a geração 80 está andando meio cambaleante, tentando se equilibrar, mas perdeu a rota e caiu; já a geração 999 está andando tranquilamente.

### Variações de Velocidade e Comportamento

Podemos observar também o caso de uma pessoa se deslocando em diferentes velocidades:
- 2 metros por segundo;
- 3,5 metros por segundo;
- 4,5 metros por segundo.

Quando o agente começa a correr, ele percebe que precisa movimentar os braços para obter um equilíbrio melhor.

No caso de um dinossauro de pescoço bem comprido:
- A 1 metro por segundo, ele anda tranquilamente;
- A 2 metros por segundo, ele compreende que é melhor se locomover pulando, pois isso torna o seu comportamento mais fácil e eficiente.

### Adaptação a Obstáculos e Analogia com o Aprendizado Humano

Vemos comportamentos de agentes em diferentes situações em que o próprio sistema precisa aprender. Por exemplo, o agente precisa correr enquanto caixas de 3 kg são arremessadas contra ele, precisando se manter em pé. Ele vai aprendendo a lidar com essa situação.

O aprendizado humano funciona de maneira similar:
- A pessoa começa aprendendo a engatinhar;
- Depois percebe que é mais eficiente ficar em pé para não ralar o joelho e as mãos no chão;
- Começa a andar em pé, caindo, tropeçando e se segurando nas paredes;
- Chega a um ponto em que aprende a controlar o corpo e passa a andar tranquilamente, sem problemas de navegação e superando obstáculos.

Contudo, ao encontrar uma pista de esqui, o piso é escorregadio e a forma de andar precisa mudar. Da mesma forma, se o objeto estiver andando na Lua, a maneira de andar terá que ser readaptada.

### Otimização e Tomada de Decisão

O algoritmo genético executa diversas iterações até que chega um momento em que define que aprendeu a andar ou a pular. O algoritmo toma a decisão do que é melhor para ele.

O dinossauro, ao aprender a correr, passou a ir pulando em vez de dar passos curtos, pois reconheceu que o salto é mais eficiente do que o passo contínuo. Essa é a base da geração de...

`⏱ 20:00`

### Comportamento de Agentes e Simulação de Aprendizado

O comportamento para um agente acontece nos games: ele é aplicado para que os personagens tenham movimentos e comportamentos diferentes. Isso se torna uma inteligência artificial, porque o próprio personagem começa a variar seus movimentos.

Nesse processo, ocorrem vários ajustes automáticos, como o tamanho do pescoço e a velocidade:
- O dinossauro aprendeu que pode usar o rabo para ajudar na manobra;
- O personagem humano aprendeu um novo tipo de corrida, dando alguns pulinhos.

Cada um vai definindo um aprendizado diferente, sem que haja controle manual direto sobre tudo isso.

Além do comportamento dos personagens em um jogo, esse conceito também é aplicado em:
- Robótica;
- Comportamento de pedestres em simuladores;
- Comportamento de agentes em diferentes cenários.

Além de seres complexos como uma pessoa ou um dinossauro, há aplicações variadas, como alterar a cor do céu de um jogo. Quando não se quer sempre a mesma cor, roda-se um algoritmo genético para misturar as cores e gerar um cenário diferente. Tudo isso consiste em uma simulação do aprendizado por meio de algoritmo genético.

### Evolução das Gerações

Analisando a evolução dos agentes ao longo das gerações:
- Na simulação do humano andando, a geração 921 é a que sabe andar corretamente;
- Nos dinossauros, a geração 900 consegue andar bem e controlar o pescoço;
- A geração 999 já sabe andar perfeitamente;
- A geração 80 já apresentava aprendizado preliminar, assemelhando-se a um dinossauro filhote que começa a andar e cai.

A necessidade de atingir a geração 999, mesmo que a 80 já tenha aprendido a se mover, deve-se ao fato de a solução mais avançada ser mais refinada, tendo eliminado os erros existentes nas etapas anteriores.

### Exemplo: Jogo do Dinossauro do Google Chrome

Há um exemplo prático que consiste em usar o algoritmo genético para ensinar o dinossauro do jogo offline do Google Chrome a jogar.

Os comportamentos e fatores analisados incluem:
- O tamanho do obstáculo (como rochas e cactos);
- A velocidade de corrida do dinossauro;
- O momento exato de ativação dos comandos.

Os comandos do jogo resumem-se a:
- Pressionar a seta para cima para pular;
- Pressionar a seta para baixo para agachar quando um obstáculo vem por cima (como um dinossauro voador).

Os parâmetros de treinamento envolvem basicamente a altura dos elementos presentes na cena, como a altura do cacto e a altura do objeto sobrevoando, determinando se o agente deve pular ou agachar.

### Implementação Prática e Problema da Mochila

Na parte de implementação, há um exemplo dentro do `Colab` que estrutura o algoritmo genético definindo uma população de amostras e evoluindo essa população por meio de:
- Seleção;
- Recombinação;
- Mutação.

Esses operadores atuam gerando amostras sucessivamente melhores. Na sequência, o algoritmo genético será aplicado para resolver o problema da mochila.

`⏱ 25:40`

### O Problema da Mochila

O problema da mochila é um problema da computação chamado NP-completo. Essa classe de problemas reúne problemas que estão no nível hard da computação. Se não me engano, temos 21 problemas na computação que são NP-completos, definidos como o problema do caixeiro-viajante e outros.

Aqui temos o problema da mochila, que é um problema de otimização combinatória. Nesse caso, a mochila suporta uma certa carga e o objetivo é preenchê-la com uma certa quantidade de objetos. 

Cada objeto vai ter um peso e um valor. O objetivo central é preencher a mochila com o maior valor possível, sem ultrapassar a carga dela.

Por exemplo, se a minha mochila suporta 15 kg:
- Quais objetos eu posso levar sem passar dos 15 kg e também sem que fique muito abaixo dos 15 kg? 
- Qual é a melhor solução?

Tendo alguns objetos, temos um algoritmo que gera essa solução por meio da computação bioinspirada, utilizando algoritmo genético. 

Logo a seguir, veremos o comportamento desses algoritmos na prática.

## Relacionado

- [[algoritmos-geneticos-conceitos-funcionamento-etapas-e-aplicacoes-praticas]]
