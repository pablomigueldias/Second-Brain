---
titulo: "Instalação, Operações Básicas e Estruturas de Programação no SciLab"
tags: [machine-learning, linguagens-de-programacao, ferramentas, setup, algoritmos, estudo]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 25
conceitos: [SciLab, SciNotes, Toolbox de Processamento de Imagens, Operadores Matemáticos, Entrada e Saída de Dados, printf, Estruturas Condicionais]
---

# Instalação, Operações Básicas e Estruturas de Programação no SciLab

> [!resumo] Do que se trata
> Apresenta o processo de download, instalação e configuração de módulos adicionais no SciLab, como as toolboxes de processamento de imagem e visão computacional. Demonstra a execução de operações matemáticas diretas no terminal e a distinção entre modelo algorítmico e implementação em código. Ensina a utilizar o editor SciNotes para criar scripts com entrada de dados via input, cálculos de área, exibição com printf e controle de fluxo condicional.

## Para lembrar

- **Após instalar uma nova toolbox ou módulo no SciLab, é necessário reiniciar a aplicação para que os componentes sejam carregados corretamente.**
- **O SciNotes é o ambiente integrado de edição de código do SciLab, utilizado para escrever, salvar e executar scripts estruturados.**
- **O algoritmo representa o modelo lógico e computacional do problema, enquanto o programa é a implementação desse modelo no código executável.**
- ⚠ **Os operadores matemáticos fundamentais no console do SciLab utilizam + para soma, - para subtração, * para multiplicação, / para divisão e ^ para potenciação.**
- ⚠ **A leitura de dados digitados pelo usuário no console é realizada por meio da função input(), permitindo capturar parâmetros para o algoritmo.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Como instalar pacotes e toolboxes adicionais no ambiente do SciLab?
- Qual a diferença entre a modelagem de um algoritmo e a sua implementação em código no SciLab?
- Como estruturar um script no SciNotes utilizando funções de entrada, cálculo e saída de dados?

## Conceitos

**SciLab** · **SciNotes** · **Toolbox de Processamento de Imagens** · **Operadores Matemáticos** · **Entrada e Saída de Dados** · **printf** · **Estruturas Condicionais**

## Conteúdo

`⏱ 00:00`

A ideia é que façamos a instalação da ferramenta. Vou mostrar o passo a passo.

No navegador, digitei simplesmente `baixar SciLab`. Vou entrar neste primeiro link, que é o `www.scilab.org`. Entrando nesse link, chegaremos à página das versões. Vamos baixar a versão mais recente, que é a `6.1.1`. Vou baixar para o Windows, porque a máquina que estou usando é o Windows, e também vou baixar a versão 64 bits.

Isso depende da máquina de vocês: tem para Linux, tem para MacOS. Eu vou baixar para Windows 64, que é o que tenho aqui na minha máquina. Rapidinho, baixar ali, só 168 MB.

Existem várias versões. Temos essas versões antigas porque às vezes há algum programa em que precisamos reaproveitar uma versão mais antiga, e acabamos instalando essa versão para trabalhar com esses projetos. Mas, como vamos criar projetos tudo novo, vamos usar o SciLab `6.1.1`.

Já baixou e vou abrir. Não vou permitir instalação; vou instalar a versão em português, pois é mais fácil compreender a ferramenta. É só dar avançar, concordar aqui, deixar tudo habilitado, o que ele pede. Deixar tudo habilitado e dar avançar. Criar o desktop, um ícone no desktop. Costumo deixar essas arquivos de associação também, deixem todos. Agora é só dar avançar e instalar.

É um software bem leve, rodará em qualquer máquina. Se você tiver um Celeron com 2 GB de RAM, vai rodar tranquilamente. Roda em qualquer máquina mesmo, ele é muito leve para a parte de processamento.

### Finalizando a Instalação e Usando a Ferramenta

Terminando aqui a nossa instalação, vou mostrar como começar a usar essa ferramenta. Ele tem alguns pacotes que instala, mas rapidamente já temos a instalação dele falando sobre o funcionamento da ferramenta.

Temos além da parte de computação numérica, também a parte de módulos do SciLab. No nosso curso, vamos usar o módulo de processamento de imagens e visão computacional. Por que vamos usar esses módulos? Porque os resultados do processamento de imagem e visão computacional envolvendo *machine learning* são mais visuais. Vamos ver uma imagem processada, vamos entender o que está acontecendo naquele algoritmo.

Os primeiros exemplos que vamos ver são exemplos matemáticos mesmo.

A instalação terminou e vai abrir aqui a ferramenta. Essa é a ferramenta que vamos utilizar. Ela tem essa cara aqui, e depois vou explicar um pouco mais dela.

Só vou instalar aqui um módulo que precisamos. Vocês vão entrar nessa caixinha aqui, que é a caixinha de *toolbox*, e vão na parte de *Image Processing*. Vão clicar nessa caixinha. A minha já está verde porque eu já tenho instalado, e eu fiz, desinstalei tudo, mas mesmo assim ela fica dentro do módulo, porque está vinculada à minha máquina.

Vão clicar nessa pastinha de `Image Processing and Computer Vision Toolbox` e vamos colocar aqui em instalar.

Só para vocês verem, vou instalar outra biblioteca aqui, outra *toolbox*, que é o `Scilab Computer Vision`. E aí, eu cliquei...

`⏱ 05:20`

A caixinha que está marrom, eu ainda não tenho o componente. Vou clicar aqui em `instalar`. A instalação é rápida, apenas 55 MB. Ele está instalando esse módulo.

Depois que a instalação de um módulo for feita, é preciso fechar o SciLab e abrir de novo.

*   Se eu instalei uma biblioteca que não vou usar agora, não preciso fechar.
*   Mas, quando vocês instalarem a biblioteca de processamento de imagens e divisão computacional, fechem o SciLab. Abram e abram de novo.

### Operações Matemáticas no Terminal

Aqui temos um terminal. Consigo fazer, por exemplo, uma conta de 2 mais 2 vezes 3.

*   2 mais 2 vezes 3 dá quanto?
*   Primeiro eu faço a multiplicação.
*   O resultado é 2 vezes 3, que é 6, mais 2, que dá 8. Certo?

Ele entende também a regra de parênteses. Se eu colocar 2 mais 2 entre parênteses e multiplicar por 3, aí sim vai dar 12. Isso acontece porque ele faz primeiro o que está dentro de parênteses e depois multiplica por meio daquilo que está fora.

Mas vamos voltar ao nosso conteúdo de aula, pois temos alguns tópicos ainda para ver.

### Fundamentos Matemáticos do SciLab

A ideia é que a gente veja um conteúdo relacionado à base para o SciLab, que é a parte matemática. O SciLab é um software matemático, um software de computação numérica. A ideia é que a gente entenda o funcionamento da parte básica de matemática.

O SciLab é um ambiente de computação numérica multiprograma. Vimos os paradigmas de programação; vimos que existem, por exemplo, algumas linguagens orientadas a objetos, vimos que existem linguagens estruturadas, e linguagens funcionais.

O SciLab é uma linguagem multiparadigma, um ambiente de programação multiparadigma que nos permite usar vários tipos de paradigmas da computação, mais especificamente para a programação de computadores dentro desse ambiente.

#### Por que um ambiente multiparadigma?

Para facilitar para todo mundo que programa trabalhar com SciLab. Eu não preciso ser um programador que trabalha com linguagem orientada a objetos, nem preciso ser um programador específico para programação funcional. Eu sou um programador, entendo como que é um `if`, um `else`, um `while`, entendo como funciona uma estrutura de repetição, uma estrutura lógica. Já basta.

#### Interação com o SciLab

O sinal de prontidão que vocês têm aí no programa, que é este aqui com uma flechinha (`>`), indica que o SciLab está aguardando você digitar um comando ou uma expressão para ele.

Voltando aqui na nossa ferramenta, ele tem esses dois tracinhos com o símbolo de maior (`>>`). Ele está esperando que você insira o valor de uma função ou um valor para ele calcular.

Este é um exemplo básico. Podemos fazer, por exemplo, 5 menos 2, que é 3. Mais 8, que dá 11. Ele está liberado para a gente fazer as nossas operações.

Depois que lotou a tela, eu posso dar um `limpar`. Vou limpar a minha tela para ficar mais fácil vocês visualizarem o que estou fazendo.

### Comandos e Operações Básicas

A gente tem aqui os comandos. As operações matemáticas básicas:

*   Soma é o símbolo de mais (`+`).
*   Subtração é este tracinho (`-`) aí que a gente tem no teclado do computador.
*   Multiplicação a gente vai usar o asterisco (`*`).
*   A divisão é a barra (`/`).
*   E a potenciação a gente vai usar aí.

`⏱ 10:20`

chapéuzinho, ? Então, vamos fazer uma de cada, ? 2 mais 2 vai dar 4 2 menos 2 vai dar 0 2 vezes 2 vai dar 4 2 barra 2, 2 dividido por 2 vai dar 1. E tem também a potenciação, 2 elevado a 2 vai dar 4. 2 vezes 2, 4. Está certo? Então, aí os nossos modelinhos aritméticos... matemáticos básicos, ? Então, a gente tem também a questão aí da precedência de operadores, da matemática básica, ? Então, a gente tem que, quando uma expressão envolve diversos operadores, o SciLab, ele vai considerar essa ordem aqui. O primeiro valor a ser calculado... vai ser de uma potenciação. Depois, vai ser um valor de multiplicação e divisão. Então, primeiro ele vai calcular a multiplicação e depois a divisão. Então, essa é a ordem. Se aparecer uma multiplicação e uma divisão, ele faz primeiro... Primeiro a multiplicação e depois a divisão. E depois os valores de soma e subtração, ? Então, primeiro ele vai fazer soma e depois ele vai fazer subtração, ? Então, se a gente pegar, por exemplo, esse exemplo aqui, ó. 4 vezes 3 elevado a 2, então, 4 vezes 3 elevado a 2, ? Então, ele vai fazer primeiro, 3 elevado a 2, ? Então, 3 elevado a 2... vai dar 3 vezes 3, que vai dar 9. Aí ele vai fazer 9 vezes 4, que vai dar 36. Então, isso aí é a parte de operações de precedência que ele tem dentro da plataforma. dele, ? Como é um software matemático, ele trabalha tranquilamente com esse tipo de problema ? A gente tem também a parte de expressões com frações então vocês tem aqui como exemplo 1 sobre 2 mais 3 sobre... 5 menos 5 sobre 8. Como que a gente faz a expressão correspondente? A gente vai fazer 1 sobre 2 mais 3 sobre 5 menos 5 sobre 8. Como a gente só tem aqui valores de... soma e subtração, então não preciso colocar parênteses, nada, ? Então vamos fazer esse cálculo aqui, 1 sobre 2 mais 3 sobre 5 menos 5 sobre 8. Então, me deu aqui o valor 0.47, bom? Eu consigo aplicar aqui uma função para deixar esse valor inteiro, ? Não deixar ele... um valor quebrado assim, então poderia arredondar ele. para 0.5 ou deixar ele arredondado em 0.4 mesmo para ficar uma coisa mais formalizada para o meu problema aí tem como fazer todas essas equações aqui dentro do SciLab, ? Então, aqui, por exemplo, repare que se os parênteses não fossem utilizados a expressão 10 mais 4 sobre 2, ? Eu teria equivalência à expressão matemática como aqui, ó. Então, eu faria primeiro 4 sobre 2. e depois eu teria a soma com 10. Então, eu preciso definir que eu quero a minha equação 10 mais 4 sobre 2. Então, eu preciso definir como é a minha... separação por meio dos meus parênteses, ? Aqui, no caso, o que eu quero representar é 10 mais 4 sobre 2. Se eu não colocar o parênteses aqui, eu vou ter algo que não é igual, que seria 4 sobre 2 mais 10, bom? Acho que até aí tranquilo, ? Agora, falando da parte... parte de algoritmos é só para a gente fazer uma introdução algoritmos e deixar bem claro quando a gente fala de algoritmo é algo diferente de um programa o nosso algoritmo é o nosso modelo matemático, computacional, sobre o nosso problema que a gente está tratando. E o ideal é que a gente sempre faça um fluxograma antes para representar o nosso problema. Então, aqui a gente tem, por exemplo, o início. Aqui é um algoritmo.

`⏱ 16:00`

Para fazer um misto quente, o procedimento começa com a primeira entrada do nosso programa.

Os ingredientes necessários são:
- Manteiga
- Duas fatias de pão
- Uma fatia de queijo
- Uma fatia de presunto

O procedimento é o seguinte:
1. Passar a manteiga em ambas as fatias de pão.
2. Colocar o presunto sobre uma fatia de pão e o queijo sobre a outra.
3. Juntar as duas fatias, fechando o sanduíche.
4. Colocar o sanduíche em uma sanduicheira até o pão tostar.
5. Retirar o sanduíche da sanduicheira.

A saída do nosso programa é o sanduíche pronto. Esse é o fim do procedimento.

### Algoritmos e Modelagem de Problemas

Este exemplo é um algoritmo para fazer um misto quente. No entanto, quando vamos programar um problema, partimos desse algoritmo. Ele funciona como uma modelagem do nosso problema, que pode ser feita em pseudocódigo ou em fluxograma, como está aqui.

A partir desse modelo feito em algoritmo, que eu vou codificar, é fundamental seguir este passo. Muitas pessoas não fazem isso; elas começam codificando do nada. Mas modelar o problema primeiro facilita muito a nossa vida, pois nos ajuda a não entrar em contradição na nossa programação.

### Algoritmo com Condicionais

Aqui temos outro fluxograma de um algoritmo que calcula a nota do aluno.

O requisito é que a nota do aluno seja maior do que 7. Para isso, eu vou receber:
1. A nota 1
2. A nota 2
3. A nota 3

Em seguida, farei uma soma e atribuirei o resultado à nota final. Depois, utilizo um comparador:
- Se a nota final for maior ou igual a 70, o aluno é aprovado.
- Caso contrário, ele é reprovado.

Esta é uma pequena demonstração de um algoritmo com condicionais. A partir desses exemplos, é que vamos começar a desenvolver os nossos algoritmos.

### Ambiente de Codificação

Em relação ao ambiente, vou mostrar na parte prática que eu tenho um ambiente de trabalho onde posso digitar meu programa, salvar o programa e executar o meu programa. Ele funciona dessa forma.

Vamos fazer um exemplo para ver isso funcionando dentro do nosso ambiente.

Aqui, tenho um exemplo de entrada e saída de dados: calcular a área de um quadrado.

Vou abrir o `SciNotes`, que é o ambiente de codificação do SciLab. Vamos usar o mesmo exemplo do nosso slide.

Para calcular a área de um quadrado, vou definir o lado como uma entrada.

Primeiro, eu defino o lado como um valor de `input`:
`lado = input()`

Em seguida, eu informo uma mensagem para o terminal, para quem está executando o meu programa:
`print("Informe a medida do lado de um quadrado.")`

Agora, defino que a área do meu quadrado é lado vezes lado:
`area = lado * lado`

Por fim, na minha saída, que é o meu `display`, eu coloco a área do quadrado:
`print("A área do quadrado é:", area)`

`⏱ 20:40`

### Executando o Programa no SciLab

A saída do valor que eu quero representar é o valor da área. Eu vou colocar a área aqui e colocar ponto e vírgula. 

Agora, tem aqui o *play*. Só que, para dar o *play*, eu tenho que salvar primeiro o meu programa para executar. Eu vou salvá-lo em uma pastinha que criei aqui, `Scilab Exemplos`, e vou colocar o nome `Exemplo 1`. 

Agora eu vou dar *play*. Quando eu dou *play* no meu programa, tenho que ir lá no meu terminal, na área de trabalho do Scilab. Ele pergunta: "Informe a medida do lado de um quadrado". Eu vou colocar a medida como `2`. Ele me dá que a área do quadrado é igual a `4`. 

Vejam que eu criei e executei o programa no SciNotes, dei o *play*, e a interface de comunicação homem-computador fica no próprio terminal dele.

### Utilizando o printf

Pegando outro exemplo agora com o `printf`: a gente fez algo que é meio que uma gambiarra, pois jogamos o valor na saída definindo no nosso display a informação de área do quadrado e, depois, colocamos o display de novo para informar o valor da variável `area`, referente ao cálculo que foi feito. 

Aqui nós vamos fazer diferente pegando a mesma questão do lado e fazendo o cálculo. Eu só vou ter que apagar as minhas duas últimas linhas. 

Vou colocar um `printf` com o texto: `"A área do quadrado calculada é: %f", area`. Eu fecho as aspas depois do `%f`, tiro a aspa que está em `area` e fecho com ponto e vírgula.

Vocês vão ver que, quando eu executar o meu programa — salvando antes, como ele pede —, lá no meu terminal vai aparecer: "Informe a medida do lado de um quadrado". Coloco `2` de novo. 

Ele calculou para mim: "A área do quadrado calculada é 4". Ele deu uma quantidade incorreta de argumentos na saída. Deixa eu ver o porquê: lado vezes lado... Ah, eu coloquei a entrada `2.0` ali, teria que colocar o valor `2`. 

A gente consegue ajustar também esses valores decimais. Isso serve para vermos que conseguimos printar um valor como na linguagem C ou no Python.

### Estruturas Condicionais

Agora a gente vai ver um pouco sobre estruturas condicionais.

## Relacionado

- [[scilab-ferramenta-para-modelagem-e-programacao-em-machine-learning]]
- [[visualizacao-de-dados-e-regressao-com-matplotlib-e-scikit-learn]]
- [[paradigmas-e-linguagens-de-programacao-para-machine-learning]]
