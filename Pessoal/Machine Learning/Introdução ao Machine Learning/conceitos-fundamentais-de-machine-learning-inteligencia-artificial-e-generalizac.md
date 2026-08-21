---
titulo: "Conceitos Fundamentais de Machine Learning, Inteligência Artificial e Generalização"
tags: [machine-learning, ia, conceitos, fundamentos, dados]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 26
conceitos: [Machine Learning, Inteligência Artificial, Datasets, Generalização, Teste de Turing, Treinamento de Modelos]
---

# Conceitos Fundamentais de Machine Learning, Inteligência Artificial e Generalização

> [!resumo] Do que se trata
> Apresenta os conceitos essenciais de aprendizado de máquina como o mecanismo responsável por gerar inteligência artificial a partir de dados e exemplos. Explora a analogia do ensino, o papel histórico da ficção científica e o Teste de Turing na avaliação de sistemas inteligentes. Demonstra como funciona a capacidade de generalização para reconhecer padrões inéditos e a importância de decisões racionais sem viés emocional.

## Para lembrar

- **Machine Learning é o método de treinar computadores para aprender comportamentos e padrões automaticamente a partir de exemplos fornecidos em datasets.**
- **O Machine Learning funciona como a etapa de ensino que gera a inteligência necessária para a constituição de uma Inteligência Artificial.**
- **A generalização permite que um modelo classifique corretamente elementos que nunca estiveram presentes no seu conjunto de dados de treino.**
- **A tomada de decisão sem interferência emocional é uma vantagem prática de sistemas inteligentes em áreas como investimentos e robótica.**
- **O Teste de Turing consiste em verificar se um participante consegue distinguir entre as respostas dadas por um humano e por uma máquina em salas separadas.**

## O que esta nota responde

- Qual é a relação entre Machine Learning e Inteligência Artificial?
- O que é o conceito de generalização no aprendizado de máquina?
- Como funciona a analogia do ensino aplicada ao treinamento de algoritmos de ML?

## Conceitos

**Machine Learning** · **Inteligência Artificial** · **Datasets** · **Generalização** · **Teste de Turing** · **Treinamento de Modelos**

## Conteúdo

`⏱ 00:00`

Olá. Meu nome é Diego Bruno e hoje vamos ver uma introdução ao Machine Learning, focando principalmente nas tecnologias existentes. Vamos desenvolver uma parte teórica bem forte para que possamos realizar o estudo de aplicações e desenvolvimento de forma mais precisa, tendo um referencial teórico bem preciso para o desenvolvimento do nosso curso.

Hoje, vamos ver a introdução ao Machine Learning, focando em entender como funcionam os métodos de machine learning na prática. Também vamos entender como cada ferramenta que ouvimos falar em diferentes situações — em aplicações envolvendo veículos autônomos, em aplicações envolvendo robótica, em aplicações envolvendo sistemas de recomendação — é desenvolvida na prática e como podemos contribuir junto a esse cenário.

### O Conceito de Aprendizado de Máquina

Primeiramente, há uma ligação com os humanos, onde temos uma relação com máquinas que pensam como seres humanos. Um sistema de aprendizado de máquina é capaz de aprender por meio de exemplos, assim como uma pessoa aprende.

Basicamente, para gerar um método de Machine Learning, é preciso treinar esse sistema para que ele consiga aprender.

### A Analogia do Ensino

Eu sempre dou o exemplo de ensinar um aluno. Passamos toda a parte teórica, fazemos exemplos e, depois disso, trazemos para o aluno formas de resolver problemas que são baseados naquilo que foi ensinado previamente.

Se eu ensinar um conteúdo para o aluno de forma de resolver problemas que são baseados em uma forma errada, ele vai aprender errado, e esse método de aprendizado não foi eficiente.

Vamos pensar, por exemplo, como um aluno aprende. Damos exemplos, damos um referencial teórico para ele e, quando fazemos uma avaliação em uma sala de 30 alunos, por exemplo, eu tenho que verificar, por meio da prova, não somente se o aluno aprendeu, mas também se a forma que eu ensinei o aluno foi correta.

Se eu tenho uma sala com 50 alunos e apenas 2% da minha sala, ou até uma taxa maior, 5%, foi bem e o resto foi mal, significa que o problema não é só a sala; significa também que o problema é a minha forma de transferir conhecimento. Nesse caso, eu tenho que reavaliar a forma que estou ensinando.

Agora, se for o inverso, 95% da sala foi bem e 5% foi mal, significa que a minha aula foi boa e eu tenho alguns alunos que não se saem bem com esse conteúdo. Assim, a prova é o método de avaliar o meu ensino para a sala.

### ML e o Processo de Aprendizagem

O método de aprendizado de máquina trabalha também dentro desse cenário.

Por meio do treinamento de um sistema de Machine Learning, conseguimos gerar sistemas de inteligência artificial. Conseguimos gerar sistemas de tomada de decisão com suporte de base de regras bem definidas. Também conseguimos gerar sistemas que realizam tomada de decisão sem se basear na emoção.

Às vezes, pensamos: "Mas na robótica, na inteligência artificial, um sistema não tem emoção; ele age de forma friamente calculada. Isso é bom ou ruim?"

Isso é bom. Quando trazemos a emoção para uma tomada de decisão, ela não é ideal. Um sistema de machine learning não leva a emoção em consideração, na maioria dos casos. E isso é uma forma...

`⏱ 05:40`

Imagina um robô que está realizando um investimento. Se ele ficar pensando: "Nossa, eu posso perder", ou se ele levar a emoção junto, ele não consegue fazer nada. A emoção não é um parâmetro importante quando trabalhamos com *machine learning*. Por isso, a gente pega esse lado dos humanos e corta.

Outro ponto é a automação para correção e suporte de falhas humanas. Por meio do *Machine Learning*, conseguimos ajudar os humanos a tomarem decisões. Temos robôs de investimentos, robôs que dão suporte para auxiliar um motorista dirigindo.

Por exemplo, vou mostrar um sistema que desenvolvi. Quando detecto que o motorista de um caminhão dormiu no volante, eu assumo o controle do caminhão e estaciono ele no acostamento. Isso é uma medida de segurança muito importante e pode evitar um grave acidente.

### A Inteligência Artificial e a Ficção Científica

Existe uma relação bem interessante que vemos, e que assistimos nos filmes, e que tentamos relacionar com a nossa existência. Pensamos: "Nossa, será que a inteligência artificial vai dominar a raça humana? Será que um dia a gente vai ser escravizado por meio de uma inteligência artificial?"

Vemos nos filmes diferentes tipos de inteligências, e pensamos que isso está muito próximo da nossa realidade. Isso não é real, pelo menos por enquanto, ainda não existe algo assim.

Para entender isso, precisamos definir três tipos de inteligência.

1.  **Inteligência Artificial Geral (AGI):** É aquela que vemos nos filmes. Um robô dirigindo um carro, cozinhando, dominando o mundo, dirigindo um disco voador. É uma inteligência artificial geral, que sabe fazer tudo. Ela é geral.
2.  **Inteligência Artificial Restrita (Narrow AI):** É o que está acontecendo no mundo. Um sistema para reconhecer sua face no celular, um sistema para fazer um investimento, um sistema para ajudar você a dirigir um carro, um sistema que faz uma recomendação de compra para você. Isso é inteligência artificial restrita. Ou seja, ela sabe te recomendar um livro, mas ela não sabe cozinhar para você. Ela sabe reconhecer sua face, porém ela não sabe dirigir um carro.

Atualmente, vivemos em um mundo de inteligências artificiais restritas, que são restritas a pequenos problemas.

### Machine Learning e o Papel da Ficção

O que é *Machine Learning*? Qual é a relação do *Machine Learning* com a inteligência artificial? Veremos isso já.

A ficção científica nos traz um cenário meio doido: robôs dominando a Terra, robôs escravizando a raça humana. Vemos isso nos filmes e já pensamos em como controlar isso no futuro.

A ficção científica tem esse lado negativo de colocar medo nas pessoas, mas ela tem um papel muito importante. É o papel de alguns produtores de filmes trazerem para a gente uma visão sobre o futuro, de como ele pode ser.

A palavra robótica, inclusive, surgiu da ficção científica, de uma peça de teatro onde idealizaram um humano metálico, mecânico, que podia fazer funções humanas.

A ficção científica ajuda muito. Por exemplo, no filme *Ex-Machine*, temos um robô que faz parte de um processo de treinamento. Há uma pessoa escolhida para ir para uma casa onde está o dono do projeto, o dono da IA. Há também um robô trancado dentro de uma sala, e a pessoa que está passando pelo teste no filme não é deixado claro, mas...

`⏱ 11:00`

### O Teste de Turing

O Teste de Turing é um teste onde se coloca uma pessoa em uma sala e um robô em outra. O participante do teste deve descobrir, por meio de perguntas e respostas, quem é o robô e quem é a pessoa.

Se o participante errar, se ele disser que o robô é o humano, o robô passou no Teste de Turing porque ele conseguiu enganá-lo.

Isso acontece em filmes. O robô consegue enganar a pessoa que está passando pelo teste. Ou seja, ele engana a pessoa e faz com que o participante entenda que o robô é o inocente.

No contexto do filme, o dono do projeto está gerando prejuízo, ou gerando danos ao robô, porque o robô está trancado, está indefeso. O robô tenta passar essa mentalidade por um jogo de sedução, já que ele tem a forma de uma mulher.

Quando falamos de Teste de Turing, é a capacidade de um robô conseguir enganar a gente em uma determinada situação. Esse teste avalia a capacidade de uma máquina exibir um comportamento inteligente, equivalente a um ser humano, ou indistinguível dele.

É possível ter uma noção disso em um filme muito interessante, que mostrou de forma bem mais clara como isso acontece.

### Robôs e a Cidadania

Há um robô chamado Sofia, que é o primeiro robô a ter cidadania. Ele é bem parecido com o robô do filme *Smashing*. No entanto, ele não tem uma inteligência próxima daquele robô do filme.

Este robô consegue reproduzir 62 expressões sociais. O objetivo é conseguir uma maior aceitação da robótica em um ambiente humano. Por meio desse robô, a ideia é trazer para a sociedade que um robô pode interagir com a gente e pode se comportar de forma relevante, sem trazer nenhum risco à humanidade.

Esse tipo de robô serve para que a gente comece a ver que é possível robôs humanoides estarem aqui conosco, no nosso dia a dia.

Esse robô não passa no Teste de Turing. Ele não consegue enganar uma pessoa porque o repertório de respostas dele é curto. Por exemplo, se você fizer a pergunta: "Você pode ter filhos?", o robô vai dizer "não". Aí você começa a desconfiar. Ele não pode ter filhos porque ele não é uma pessoa. Esses tipos de perguntas acabam tirando a identidade humana de um robô, e você consegue perceber que o robô é mesmo um robô e não uma pessoa.

### Machine Learning e Inteligência Artificial

Qual é a relação entre Machine Learning e Inteligência Artificial? Qual é a relação que existe entre esses dois tópicos da área de tecnologia? Muitas pessoas misturam, dizendo: "Ah, eu trabalho com Machine Learning", ou "Ah, eu trabalho com Inteligência Artificial". É preciso definir bem o que é cada um e qual a relação entre eles.

Para ter uma inteligência artificial, antes é preciso passar por um método de Machine Learning. Por quê? O Machine Learning é um método que vai gerar a inteligência que é necessária.

Por meio do Machine Learning — traduzindo o termo como aprendizado de máquina — o que é esse aprendizado de máquina? É conseguir ensinar o meu sistema a ponto de ele ter...

`⏱ 16:20`

...inteligência. Quando ele adquire essa inteligência, eu tenho uma inteligência artificial, certo?

Vou dar um exemplo bem simples para isso. Quando você compra um celular novo que tem reconhecimento facial, ele vai pedir para você tirar algumas fotos do seu rosto, para ele cadastrar na base de dados dele. Ele treina e ele sabe reconhecer a sua face. Mas, por exemplo, eu estou de barba, eu raspo a minha barba, o sistema continua me reconhecendo. Eu vou lá e pinto o meu cabelo, o sistema continua me reconhecendo. Eu vou lá, rasco a minha cabeça, o sistema continua me reconhecendo. Eu coloco um óculos de sol, o sistema continua me reconhecendo.

Por quê? Por mais que eu mude a minha aparência, ele tem outras métricas de avaliação:

- A distância entre os olhos;
- O tamanho da minha face na vertical e na horizontal;
- A cor da minha pele;
- A cor do cabelo;
- O formato geral da minha cabeça.

Então, por mais que eu mude uma variável, o sistema continua me reconhecendo. Se o meu sistema consegue fazer isso, é porque ele adquiriu uma inteligência. Por quê? Porque eu não estou mostrando para ele o meu rosto sempre da forma que ele foi treinado.

### Generalização e Inteligência Artificial

Ele consegue fazer uma coisa que para a inteligência artificial é muito importante: generalizar.

Quando um sistema de `machine learning` treinado consegue generalizar as coisas, então a gente obteve uma inteligência artificial. Se o meu sistema não consegue reconhecer ou conhecer coisas além do que ele foi treinado, ele não obteve inteligência.

Voltando lá no exemplo da escola, eu ensinando para o aluno:

1.  Se eu ensinar um exercício para o aluno e na prova eu cobrar o mesmo exercício, ele decorou. Ele não aprendeu.
2.  Agora, se eu ensino um tipo de exercício e na prova eu cobro um exercício parecido, mas não igual, significa que o aluno conseguiu aprender. Ele obteve mais um grau de inteligência no treinamento dele ao longo da sua vida.

Se eu preciso colocar o mesmo exercício que eu dei na aula na prova, porque ele decorou, isso não é aprendizado. Ele não aprendeu, ele não obteve inteligência.

Um aprendizado de máquina, de forma resumida, é a forma de treinar um sistema para que ele obtenha inteligência ou não. Por meio do `machine learning`, do aprendizado de máquina, eu posso obter uma IA, uma inteligência artificial, ou não.

Existe outro meio de obter uma inteligência artificial? Não. Eu preciso passar por meio de um método de `machine learning`, seja ele qual for. A gente vai ver vários aqui para que eu obtenha uma inteligência artificial.

Isso é para deixar bem claro para todos qual a diferença de `Machine Learning` e Inteligência Artificial. É uma união que a gente faz para obter uma Inteligência Artificial.

### Definições Técnicas

O objetivo do aprendizado de máquina, ou `Machine Learning`, é programar computadores para aprender um determinado comportamento ou padrão automaticamente a partir de exemplos ou observações, utilizando `data sets`.

O que são `data sets`? São conjuntos de dados que eu consigo ensinar, por meio de exemplos, um sistema de `machine learning` para que ele obtenha uma inteligência artificial.

Vou dar um exemplo para vocês: eu vou pegar 100 fotos de gato, 100 fotos de cachorro e vou treinar o meu sistema. Aí ele vai conseguir reconhecer gato e cachorro. Mas, por exemplo, se eu tenho uma imagem no meu sistema...

`⏱ 21:20`

...e ela não está na minha base de dados. Eu peguei 100 fotos de cachorro, mas lá não tem nenhum poodle. Quando eu mostro uma foto de um poodle, ele tem que reconhecer que é um cachorro e que não é um gato.

Mas como ele consegue fazer isso? Ele generalizou a classificação do tipo de problema. Por mais que ele nunca tenha visto um Poodle no treinamento, ele consegue verificar que o Poodle também tem o formato de um cachorro. Ele tem:

- o formato das orelhas;
- o formato das patas;
- o formato do rabo;
- o formato do corpo;
- a textura do pelo.

Tudo isso é importante, e ele aprendeu em outros cachorros. Os gatos são diferentes. Eles têm orelhas pontudas e são menores, na maioria dos casos.

Portanto, o treinamento deve ser possível por meio de base de dados.

#### Reconhecimento de Pessoas

Se eu quero ensinar meu sistema a reconhecer pessoas, por exemplo, em uma sala com 30 alunos, e para que meu sistema reconheça quem é Maria, quem é João, quem é Pedro, eu tenho que dar algumas imagens. Geralmente, usamos 50 a 100 imagens de cada tipo de face para que ele consiga reconhecer.

#### O Aprendizado Humano

Se a gente parar para pensar, nós também aprendemos assim. Quando somos pequenos, nosso pai ou nossa mãe pega a gente pela mão e vai levar para passear. Aí você vê um bichinho e pergunta: "Nossa, que bichinho é aquele?". Seu pai e sua mãe falam: "Ah, é um gato". Você vê outro e pergunta: "Ah, é um cachorro".

Você vai vendo outros e começa a relacionar. "Meu pai me mostrou aquele cachorrinho, aqui tem outro. E isso eu acho que também é um cachorro", porque também está latindo, pelo formato, pelo comportamento. Assim, a gente vai criando inteligência.

Nossos pais não vão ficar a vida toda mostrando o que é gato e cachorro. Quando vemos outro exemplo, temos que entender pela relação de características: o que é aquele animal? Se é um gato, um cachorro, ou se surgiu um tipo novo de animal?

Por exemplo, uma raposa. Eu nunca vi uma raposa e estou vendo, e eu não sei que animal é esse. Mas você tem que saber. Eu tenho que buscar na internet, ir lá no zoológico e ver a plaquinha escrita "raposa" para começar a relacionar o objeto raposa com a classe dele, que é a classe raposa.

#### Machine Learning e IA

Isso é um aprendizado de máquina. Não há outra forma de realizar aprendizado de máquina senão por exemplos, senão por modelos que conseguimos mostrar exemplos e mostrar características.

Isso é muito importante para que continuemos o nosso curso dentro desses parâmetros, entendendo qual a relação de IA com Machine Learning e entendendo também como acontece um sistema de Machine Learning na prática.

E agora a gente começa a ver a parte de Inteligência Artificial restrita.

## Relacionado

- [[04 - Os Tipos de Agentes de IA]]
- [[fundamentos-e-pilares-do-pensamento-computacional]]
- [[01 - A Vantagem da IA]]
- [[reconhecimento-de-padroes-conceitos-aplicacoes-e-mecanismos-de-classificacao]]
