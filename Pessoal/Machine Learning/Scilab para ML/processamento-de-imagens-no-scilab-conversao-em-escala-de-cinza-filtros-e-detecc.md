---
titulo: "Processamento de Imagens no Scilab: Conversão em Escala de Cinza, Filtros e Detecção de Bordas"
tags: [machine-learning, ferramentas, algoritmos, fundamentos, dados]
data: 2026-08-24
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 8
conceitos: [Processamento de Imagens, Toolbox de Visão Computacional, Escala de Cinza, RGB, Detecção de Bordas, Filtro de Sobel, Domínio da Frequência]
---

# Processamento de Imagens no Scilab: Conversão em Escala de Cinza, Filtros e Detecção de Bordas

> [!resumo] Do que se trata
> Apresenta o potencial do Scilab e suas toolboxes para processamento de imagens e visão computacional. Demonstra a conversão de imagens coloridas RGB em matrizes de níveis de cinza para reduzir o custo computacional do processamento. Explora também técnicas de filtragem espacial e em frequência para detecção de bordas, além de funções de detecção e rastreamento de objetos.

## Para lembrar

- **A escala de cinza possui 255 níveis de intensidade para representar variações tonais entre o branco e o preto absoluto.**
- **Filtros de detecção de bordas, como o Sobel, percorrem a matriz da imagem para identificar contornos sem a necessidade de processar cores ou preenchimentos completos.**
- **O processamento de imagens no Scilab inclui operações no domínio do espaço e no domínio da frequência, além de recursos para object detection e tracking ao longo de frames.**
- ⚠ **A conversão de uma imagem RGB (3 canais) para níveis de cinza reduz a representação para uma única matriz, diminuindo a carga computacional no processamento.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Por que converter uma imagem RGB para níveis de cinza antes do processamento computacional?
- Como funciona a detecção de bordas em matrizes de imagens usando filtros no Scilab?
- Quais são os principais recursos oferecidos pelas toolboxes de visão computacional do Scilab?

## Conceitos

**Processamento de Imagens** · **Toolbox de Visão Computacional** · **Escala de Cinza** · **RGB** · **Detecção de Bordas** · **Filtro de Sobel** · **Domínio da Frequência**

## Conteúdo

`⏱ 00:00`

A gente vai ver um pouco da parte de processamento de imagens. A ferramenta `Scilab` é uma das melhores ferramentas para processamento de imagens.

Ela possui várias bibliotecas e *toolboxes* que conseguimos utilizar para:

- Pré-processamento da imagem;
- Pós-processamento;
- Algoritmos de detecção de face, como reconhecimento facial;
- Detecção de objetos em cenas;
- *Tracking* da imagem, que é o acompanhamento do objeto ao longo de vários *frames*.

Assim como a ferramenta `MATLAB`, elas foram as primeiras ferramentas de processamento de imagens aplicadas no mercado da computação.

### Conteúdo da Aula

Nesta aula, vamos ver um conteúdo com exemplos. Depois desses exemplos, e evoluindo ao longo do nosso curso, principalmente quando a gente vê um conteúdo novo, vamos ver algoritmos de segmentação.

Aí, vamos ver um algoritmo de segmentação aqui usando o `Scilab`. Mas agora a ideia é que a gente veja o potencial dessa ferramenta, que a gente aprenda a usar o `Scilab`. Já vimos uma parte introdutória e exemplos de código. Agora vamos ver exemplos de processamento de imagens e visão computacional.

### Configurando o Ambiente

Aqui dentro do `Scilab`, na área de trabalho, se vocês clicarem nesse sinalzinho de interrogação, do lado de Aplicativos, vocês vão em `Ajuda do SILAB`.

Vindo aqui na `Ajuda do SILAB`, vão ter algumas pastinhas relacionadas com as *toolboxes* que a gente instalou. Vamos usar, por exemplo, as *toolboxes* de processamento de imagens.

### Exemplo: Conversão de Cor para Níveis de Cinza

Vou mostrar aqui para vocês uma delas: a leitura de uma imagem colorida e a transformação dessa imagem colorida para preto e branco, ou seja, para níveis de cinza.

Por que fazemos isso? Eu vou mostrar aqui para vocês. Estou pegando uma imagem, lendo essa imagem e apresentando ela, plotando ela em uma matriz.

Esta imagem é a imagem da Lena. Para quem não conhece, eu comentei um pouco dela já durante nossa trilha de Machine Learning. A Lena é uma imagem que foi a primeira imagem a ser escaneada por um computador, a primeira imagem digital. Ela foi feita em um laboratório de pesquisa americano.

Por curiosidade, é uma imagem de uma revista da Playboy. Lena foi uma atriz que posou para a revista da Playboy. Obviamente, só colocaram o rosto dela aqui. E essa imagem é a primeira imagem digital do mundo, a primeira imagem digital lida por um computador. Ela foi escaneada assim, colorida.

Por ser colorida, ela está sendo representada em três canais de cores: o R (Red), o G (Green) e o B (Blue).

Porém, tem situações em que eu não preciso ter informações de cores. Se eu pegar essa imagem, por exemplo, ela está colorida, está bonita, mas às vezes eu não preciso que essa imagem tenha cores. Então, eu reduzo ela a níveis de cinza.

Vou rodar um algoritmo aqui: a imagem será capturada, essa imagem colorida, e eu vou jogar essa imagem para níveis de cinza.

Essa imagem em níveis de cinza, eu estou fazendo com este algoritmo. Eu vou mostrar essa imagem.

A gente chama ela de preto e branco, mas chamamos ela de forma errada. Por quê? Uma imagem preto e branco só teria a cor preta e branca. Aqui vocês podem ver que há vários tons de branco e de cinza. Por isso que a gente chama uma imagem em níveis de cinza.

Isso ocorre porque há 255 níveis de cinza, desde o zero, que é o branco (igual ao fundo da imagem aqui), até o 255, que é o preto absoluto.

`⏱ 04:40`

A cor preta absoluta permite que tenhamos níveis de variação. Por exemplo, a pena na cabeça dela tem vários níveis de cinza, assim como o cabelo, a cor dos olhos, o fundo e o chapéu. 

Dessa forma, conseguimos representar a imagem exatamente como ela é, mas reduzindo o espaço de cores de três matrizes para uma só. Isso se torna mais vantajoso para o processamento, pois trabalha com uma carga computacional menor. Por isso, em várias áreas de processamento de imagem, transformamos a imagem em níveis de cinza.

### Filtragem de Imagens e Detecção de Bordas

Outra aplicação envolvendo processamento de imagem é a filtragem de imagens (`Image Filtering`). O `Soul Bell` é um filtro de imagens aplicado para detectar as bordas da imagem. 

Na imagem da Lena, por exemplo, vemos as bordas presentes: a borda da cama e a borda do chapéu. Às vezes, não é necessário avaliar o objeto inteiro, suas cores ou seus níveis de cinza, sendo preciso identificar apenas a sua borda; para isso, o algoritmo funciona muito bem. Esse filtro percorre a imagem utilizando matrizes, detectando e definindo o que é borda.

### Outras Ferramentas e Domínio da Frequência

Temos várias ferramentas para o processamento de imagens:

- **Filtro de `Huffle`:** executado sobre a imagem para gerar a detecção de bordas, mas trabalhando no domínio da frequência da imagem (um caso em que não se detecta o comportamento direto dela);
- `Object Detection` (Detecção de Objetos);
- `Object Tracking` (Rastreamento de Objetos).

Há diversas funções disponíveis dentro do processamento de imagens.

## Relacionado

- [[estruturas-de-repeticao-com-while-no-scilab-e-introducao-ao-processamento-de-ima]]
- [[instalacao-operacoes-basicas-e-estruturas-de-programacao-no-scilab]]
- [[scilab-ferramenta-para-modelagem-e-programacao-em-machine-learning]]
- [[paradigmas-e-linguagens-de-programacao-para-machine-learning]]
