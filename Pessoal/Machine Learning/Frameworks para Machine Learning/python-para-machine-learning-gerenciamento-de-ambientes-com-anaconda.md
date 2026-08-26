---
titulo: "Python para Machine Learning: Gerenciamento de Ambientes com Anaconda"
tags: [machine-learning, python, ferramentas, setup, conceitos, estudo]
data: 2026-08-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [Anaconda, Ambientes de programação, Gerenciamento de dependências, Versões de Python, Instalação de bibliotecas, TensorFlow, Scikit-Learn, SciPy]
---

# Python para Machine Learning: Gerenciamento de Ambientes com Anaconda

> [!resumo] Do que se trata
> Esta aula aborda o Anaconda como uma solução para criar e gerenciar ambientes de programação isolados, permitindo trabalhar com diferentes versões de Python e bibliotecas sem conflitos. Ela explica como o Anaconda facilita a instalação de dependências específicas para cada projeto, como TensorFlow e SciPy. A nota detalha os benefícios de usar ambientes virtuais e demonstra a instalação de bibliotecas com o comando `conda install`.

## Para lembrar

- **A função do Anaconda é permitir a criação de ambientes de programação isolados dentro da mesma máquina para evitar conflitos de dependências.**
- **Ambientes isolados no Anaconda permitem rodar projetos com diferentes versões de Python (ex: 2.7 e 3.10) e bibliotecas (ex: TensorFlow, Scikit-Learn) simultaneamente.**
- **Para criar um novo ambiente no Anaconda, escolhe-se a versão desejada do Python ou R, e ele não interfere na instalação nativa da máquina.**
- **A instalação de bibliotecas dentro de um ambiente Anaconda é realizada utilizando o comando `conda install [nome_da_biblioteca]`.**
- **O Anaconda é uma solução para o problema de gerenciar múltiplas dependências e versões de bibliotecas em projetos Python, sendo útil para Machine Learning.**

## O que esta nota responde

- Qual a principal função do Anaconda no desenvolvimento de projetos de Machine Learning?
- Como o Anaconda resolve o problema de conflito de versões e dependências entre diferentes projetos Python?
- Qual o comando correto para instalar uma biblioteca específica, como o SciPy, dentro de um ambiente Anaconda?

## Conceitos

**Anaconda** · **Ambientes de programação** · **Gerenciamento de dependências** · **Versões de Python** · **Instalação de bibliotecas** · **TensorFlow** · **Scikit-Learn** · **SciPy**

## Conteúdo

`⏱ 00:00`

Olá, tudo bem? Meu nome é Diego Bruno e hoje a gente vai ver um pouco sobre o Anaconda.

### A Função do Anaconda
A função desse ambiente é que a gente consiga criar ambientes diferentes dentro da mesma máquina.

Eu vou dar um exemplo. A gente está trabalhando em um projeto onde tem uma versão do `Python 3.6`, o `TensorFlow 2.4`, e uma determinada versão de algumas bibliotecas. Esse projeto está rodando tranquilamente.

Você quer testar um novo projeto disponível no `GitHub`, só que as dependências são diferentes. Você teria que desinstalar tudo do seu computador para rodar o projeto de outra pessoa. Isso acaba prejudicando o seu projeto e te dando tanto trabalho que às vezes você até desiste de testar o projeto de outra pessoa ou simplesmente comparar com o seu.

Quem trabalha com ciência e desenvolvimento de pesquisa, às vezes precisa comparar o seu modelo com o de outra pessoa, e você vai ter que rodar o modelo da pessoa em cima da sua base de dados. É interessante conseguir rodar na sua máquina e comparar resultados.

Se eu pegar aqui, por exemplo, no meu terminal e abrir o `Python`, eu estou utilizando a versão do `Python 3.10`. Aqui eu já instalei, por exemplo, o `Scikit-Learn`. Porém, se eu precisar rodar um projeto que está em uma versão anterior do `Python`, uma versão `2.7`, por exemplo, não vai rodar aqui.

O que eu vou ter que fazer? Eu vou ter que mudar a minha versão do `Python`. Se já tem o `TensorFlow` e está usando outra versão do `TensorFlow`, eu vou ter que mudar a versão do `TensorFlow`. Vou ter que desinstalar a versão que eu tenho e instalar uma versão nova. Isso é bem chato. Eu acho que a parte mais chata de trabalhar com `Python` é esse monte de dependência, um monte de versão. Dá muita dor de cabeça.

### Criando Ambientes com Anaconda
O que a gente faz? A gente cria ambientes. A gente cria o ambiente que a gente quer trabalhar dentro do Anaconda.

Se a gente colocar aqui embaixo, `Create`, você consegue criar um novo ambiente. Eu vou criar aqui, por exemplo, o `ambiente 2`. O `ambiente 1` eu fiz de teste.

Aí aparece se eu quero trabalhar com `Python` ou com `R`. Se eu quero trabalhar com `Python`, é só escolher a versão que eu quero. No caso aqui tem a:
- `2.7`
- `3.5`
- `3.6`
- `3.7`
- `3.8`
- `3.9`
- `3.10`

Vamos supor que eu quero trabalhar com a versão `2.7`. Eu vou criar o meu ambiente para essa versão `2.7`.

### Benefícios dos Ambientes
Qual é a facilidade? Eu estou criando um ambiente que tenha essa versão do `Python` embutida, e eu não preciso desinstalar aquela versão `3.10` que eu tenho nativa aqui no meu computador.

Eu vou abrir aqui, por exemplo, esse ambiente, o `ambiente 1`. Como eu estou instalando o ambiente ainda, vai demorar um pouquinho para ele criar.

Comentando um pouco mais, eu consigo criar quantos ambientes eu quiser. Eu consigo criar um ambiente com as dependências que eu preciso, e ele não vai influenciar a minha instalação nativa na minha máquina.

É como se fosse uma camada entre o meu computador, o meu sistema operacional, e os ambientes que eu estou criando suspensos ao Anaconda.

`⏱ 05:00`

Eu vou abrir aqui, por exemplo, o ambiente 1. É só clicar aqui nesse símbolo do *play* dele. Ele vai me dar a opção aqui de abrir com o terminal. Vou abrir aqui com o terminal. Vocês estão vendo que aparece "ambiente 1". Esse ambiente 1 significa que eu estou dentro de um ambiente específico do Anaconda para o meu problema.

Eu poderia abrir o ambiente 2, mas eu estou dentro do ambiente 1. No ambiente 1, o que eu tenho aqui? Eu tenho a versão 3.9 do Python. Na minha máquina eu tenho a 3.10. Aqui no ambiente 1 eu tenho a 3.9. E no ambiente 2 eu tenho a versão 2.7. Vocês estão vendo que eu tenho três versões do Python já para eu usar na minha máquina?

E a mesma coisa funciona com as bibliotecas. Eu posso agora instalar tudo o que eu preciso aqui dentro do Anaconda, sem que eu tenha grandes problemas. Se eu preciso da versão 3.9, eu estou na versão 3.9. Agora eu preciso instalar uma versão do TensorFlow. Vou colocar a instalação do TensorFlow aqui desse ambiente, e não vou interferir no que eu tenho dentro do ambiente 2, nem no que está instalado nativo na minha máquina.

#### A Vantagem do Anaconda

Quando comecei a trabalhar com Python, todo o meu desespero, digamos assim, em trabalhar com dependências diferentes, toda hora ter que desinstalar as coisas, instalar de novo. Isso tudo acabou graças ao Anaconda.

O Anaconda é a solução para esse problema que a gente tem com Python, em trabalhar com várias dependências diferentes, versões diferentes. É um ambiente mais tranquilo para quem está começando a trabalhar com Python.

#### Instalando Bibliotecas no Ambiente

Mostrando aqui um pouco, ele já vem habilitado algumas coisas. Você também consegue instalar aí alguma versão que você precisa.

Um exercício específico: você entrando aí no Google colocando `conda install` e `tensorflow`, ele vai te mostrar o comando que você tem que dar para instalar o TensorFlow dentro do Anaconda.

Você precisa instalar o Anaconda, ou melhor, instalar o TensorFlow dentro do Anaconda. Você não precisa instalar no teu terminal nativo da máquina. Você vai instalar naquele terminal que a gente abre no ambiente. Só que é diferente um pouco o comando para instalar. Antes, você tem que dar um `conda`.

O comando para você instalar as coisas que você precisa dentro do ambiente Anaconda é:
`conda install`

Se a gente fosse instalar, por exemplo, o TensorFlow nativo na máquina, não precisaria colocar esse `conda install`. Seria só `install` alguma coisa. O comando seria: `install tensorflow`.

Mas o TensorFlow é a versão que você quer. Agora aqui a gente precisa dar o `conda` antes.

#### Exemplo Prático de Instalação

É basicamente isso. Vamos pegar aqui, por exemplo, e instalar uma biblioteca pra gente ver.

O comando é:
`conda install scipy`

Ele vai mostrar para a gente aqui o comando para instalar o SciPy no Anaconda. Seria:
`conda install anaconda scipy`

Vamos abrir lá o nosso ambiente, o ambiente 1. Vou abrir aqui no terminal e vou colar esse comando. Ele está fazendo aqui a instalação. Pediu permissão, vou dar a permissão. Está instalando a base de dados para, no caso aqui, a gente chamou a SciPy.

Ele está instalando essa versão do SciPy dentro do Anaconda, não é nativo na minha máquina. Então eu estou instalando dentro desse ambiente. Se eu pegar nativo na minha máquina, não vai ter SciPy. Foi feita a instalação. Se eu precisar de SciPy instalado aqui dentro do Anaconda, dentro do ambiente, ele está instalado.

`⏱ 10:40`

Se eu precisar de SciPy instalado aqui dentro do Anaconda, dentro do ambiente, o ambiente 2 não vai ter SciPy, eu não instalei lá dentro. Também na máquina nativa aqui do meu computador não tem SciPy. Onde que vai ter SciPy? Somente no ambiente 1.

Vocês viram que a gente consegue modularizar nossa máquina em vários ambientes. Para quem trabalha com Machine Learning, isso é o sonho de consumo, por conta desse monte de dependência que a gente trabalha.

Tudo que a gente for usar na parte de projeto, quando a gente for implementar nossas redes, a gente vai instalar dessa forma. Não tem segredo, é só pesquisar o comando. Geralmente vai ser, igual eu mostrei para vocês: `Conda Install Scikit Learning Anaconda`. Pronto, é a instalação.

Sempre as bibliotecas seguem esse padrão: `Conda Install`, o nome da biblioteca, `Anaconda`. E está feita a instalação para toda a biblioteca que a gente precisar. A gente instalou uma aqui de exemplo. Tudo que a gente for precisando, a gente vai instalando também.

A gente vai usar o ambiente Anaconda, e ele serve tanto para quem está trabalhando com Windows quanto para quem está trabalhando com Linux.

### Alternativas para Instalação

Ah, mas eu não tenho um computador que suporta tudo isso. E aí? Aí a gente vai usar o Colab. Professor, mas o Colab precisa usar o Anaconda? Não. O Colab não precisa instalar nada, na verdade. No próprio servidor deles, as bibliotecas todas estão instaladas. E você consegue chavear a versão, porque lá dentro eles têm todas as versões instaladas.

Ah, eu preciso usar o `Python 2.7`. Tem lá instalado. Ah, eu preciso do `3.10`. Tem também.

Para todo mundo vai ficar tranquilo, tanto para quem vai instalar nativo na máquina quanto para quem vai usar o Colab.

## Relacionado

- [[python-para-machine-learning-bibliotecas-essenciais-e-gerenciamento-de-ambientes]]
- [[machine-learning-frameworks-e-ambientes-de-desenvolvimento-tensorflow-pytorch-ke]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `Python 3 → Python`

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Então por hoje é isso muito obrigado pela participação de vocês e até a próxima.

</details>
