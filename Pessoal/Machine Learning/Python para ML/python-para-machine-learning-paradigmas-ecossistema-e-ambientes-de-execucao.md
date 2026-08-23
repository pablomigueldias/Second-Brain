---
titulo: "Python para Machine Learning: Paradigmas, Ecossistema e Ambientes de Execução"
tags: [machine-learning, linguagens-de-programacao, ia, ferramentas, setup, estudo]
data: 2026-08-23
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 17
conceitos: [Python multiparadigma, Ambientes de execução, Google Colab, Gerenciamento de dependências, Bibliotecas de Machine Learning, Aceleração por GPU]
---

# Python para Machine Learning: Paradigmas, Ecossistema e Ambientes de Execução

> [!resumo] Do que se trata
> Apresenta a linguagem Python como o padrão dominante para pesquisa e desenvolvimento em Machine Learning e Inteligência Artificial. Explora sua natureza multiparadigma e a vasta disponibilidade de bibliotecas essenciais como Pandas, Scikit-learn, Matplotlib e NumPy. Discute a configuração do ambiente de desenvolvimento, comparando a execução local com aceleração por GPU ao uso de plataformas em nuvem como o Google Colab e o gerenciamento de dependências.

## Para lembrar

- **Python é uma linguagem multiparadigma que combina programação orientada a objetos, funcional e imperativa.**
- **O ecossistema principal de Machine Learning em Python fundamenta-se em bibliotecas como Pandas, Scikit-learn, Matplotlib e NumPy.**
- **Ambientes locais permitem o aproveitamento máximo do hardware dedicado e GPUs, enquanto plataformas em nuvem como o Google Colab dispensam instalações manuais.**

## O que esta nota responde

- Por que Python se tornou a linguagem predominante em pesquisas e aplicações de Machine Learning?
- Quais são os principais paradigmas de programação suportados pela linguagem Python?
- Qual a diferença prática entre executar modelos de Machine Learning localmente com GPU e no Google Colab?

## Conceitos

**Python multiparadigma** · **Ambientes de execução** · **Google Colab** · **Gerenciamento de dependências** · **Bibliotecas de Machine Learning** · **Aceleração por GPU**

## Conteúdo

`⏱ 00:00`

### Introdução ao Python para Machine Learning

Olá, tudo bem? Meu nome é Diego Bruno e a nossa aula de hoje é sobre Python para Machine Learning.

Nesse cenário, vamos aprender a parte básica dessa linguagem para quem nunca teve contato com ela. Começaremos com uma base sólida para que todos consigam acompanhar de forma tranquila. Se você nunca programou em Python, pode ficar tranquilo, pois apresentarei o conteúdo do zero. Para quem já tem uma noção, servirá para fluir muito bem o conhecimento em aplicações envolvendo machine learning.

A linguagem Python é a mais utilizada atualmente na área de Machine Learning e Inteligência Artificial. Vamos focar bastante nela para conseguirmos desenvolver adequadamente os modelos de treinamento e aplicações específicas.

Veremos modelos de machine learning aplicados a:
- visão computacional;
- processamento de imagens;
- criação de modelos para sistemas de recomendação.

Nesse contexto, a linguagem Python é fundamental. Para começar a programar, veremos inicialmente alguns conceitos importantes para compreender a relevância dessa linguagem.

### Adoção em Pesquisa e Mercado

De forma geral, Python é uma linguagem que vários grupos de pesquisa no mundo todo utilizam em seus projetos. Isso é importante tanto para estabelecer relações e contribuir com esses grupos quanto para futuras oportunidades de atuação profissional nessas empresas.

Além disso, quando surge a necessidade de uma biblioteca ou ferramenta, há uma grande oferta disponível para Python.

Como exemplo: quando entrei no doutorado, eu não programava em Python. Ao implementar uma rede neural ou uma rede de Deep Learning, eu programava em `C`. Quando precisava de uma biblioteca para trabalhar com imagens, não havia em `C`, apenas em Python, e eu precisava desenvolvê-la. Posteriormente, ao precisar de outra biblioteca para analisar dados, também não havia disponível e eu precisava implementar. Chegou um momento em que percebi que tudo aquilo já existia pronto em Python e que eu estava perdendo tempo. Por esse motivo, desenvolvi meu doutorado em Python, que é a linguagem em evidência para a área de machine learning.

Minha área de atuação é veículos autônomos, na qual utilizamos fortemente a linguagem Python. Vários grupos de pesquisa com os quais tive contato utilizam a linguagem:
- o grupo em que trabalhei na USP de São Carlos, no Brasil;
- a Toyota, nos Estados Unidos;
- o Kiki, na Alemanha.

Todos esses grupos utilizam a linguagem Python, sendo ela essencial para atuar nesse cenário.

### Paradigmas de Programação

Outro ponto muito importante é que a linguagem Python adota uma estrutura multiparadigma. Enquanto existem linguagens puramente imperativas, funcionais, lógicas ou orientadas a objetos, o Python mescla diferentes paradigmas:
- paradigma orientado a objetos;
- paradigma funcional;
- paradigma imperativo.

É uma linguagem muito evoluída para esse cenário e que recebe constante investimento em projetos, resultando na criação de bibliotecas de grande relevância.

`⏱ 05:20`

### Introdução ao Python e Machine Learning

Para quem está começando com Machine Learning, Python é a linguagem recomendada. E não é só para iniciantes: quem já é sênior e atua no universo da Inteligência Artificial e do Machine Learning há muito tempo também está utilizando Python. Trata-se de uma linguagem que abrange um grande volume de pesquisas, motivo pelo qual vamos nos dedicar a ela.

Nesse cenário, veremos desde a parte básica — partindo de um exemplo de [inaudível] até o Word — até aplicações mais dedicadas à área de Machine Learning, tais como:
- Multiplicação de matrizes;
- Leitura de uma matriz de entrada;
- Leitura de imagens;
- Treinamento de modelos a partir dos valores dessas imagens.

### Matrizes na Visão Computacional

O foco em matrizes, multiplicação de matrizes e convoluções se justifica pelo fato de que a representação matemática de uma imagem é, essencialmente, uma matriz. Como as nossas aplicações são direcionadas para a área de visão computacional e processamento de imagens, esse conteúdo será abordado evidenciando a fundamentação matemática subjacente.

### Estrutura das Aulas e Ambientes de Execução

O conteúdo abordará inicialmente a programação básica em `Python` para nivelar o conhecimento de todos os alunos e revisar pontos fundamentais. 

Em seguida, abordaremos:
- Instalação nativa de dependências necessárias para a execução dos algoritmos locais na máquina;
- Execução do mesmo código no `Colab`, ambiente em nuvem disponibilizado pelo Google onde não há necessidade de instalações locais;
- Comparação detalhada entre esses dois ambientes.

Aprender a instalar dependências localmente é fundamental para cenários onde há uma máquina dedicada ao projeto. Por exemplo, caso um laboratório invista em uma infraestrutura potente para o desenvolvimento da sua pesquisa, não faz sentido restringir o uso ao navegador para rodar algoritmos no `Colab`. É necessário aproveitar ao máximo a capacidade do hardware disponível.

Dessa forma, o percurso prático incluirá:
- Programação básica;
- Instalação de dependências;
- Principais bibliotecas de Machine Learning;
- Processamento de dados de imagens e redes de Deep Learning por meio de GPUs utilizando `CUDA`.

### Evolução do Uso de GPUs

O uso de processamento gráfico tornou-se indispensável. Antigamente, GPUs da NVIDIA e da AMD eram adquiridas majoritariamente para a execução de jogos pesados. No início do processamento neural, utilizavam-se essas mesmas placas voltadas ao mercado de games. 

Atualmente, o cenário mudou: as GPUs são aplicadas prioritariamente em Machine Learning, existindo linhas de hardware desenvolvidas exclusivamente para o treinamento de redes neurais e modelos de Deep Learning.

`⏱ 10:20`

Hoje, existem placas específicas para esse cenário. Mas sem problema eu usar uma GPU que é para game? Eu sempre trabalhei com essas mesmo, porque são placas mais acessíveis.

### Configuração de Programação e Ferramentas

A parte de programação básica será feita com Python. Depois, vamos ver a ideia de programar em um software chamado `Sublime`. Eu vou mostrar como instalar ele. Ele é bem interessante porque conseguimos executar nosso `código`, e ele já mostra na saída o resultado da nossa execução. Vou mostrar depois como baixar e como está tudo certinho.

A parte básica do Python, sempre, tem o `Hello World`. Dizem que se o primeiro exemplo que aprendemos em uma nova linguagem não for o `Hello World`, teremos azar. Para não correr esse risco, vamos começar conversando desse exemplo.

No entanto, eu estou entrando neste curso de Machine Learning e já estou esperando um conteúdo mais potente para o meu aprendizado. Eu prometo que não vou perder muito tempo com a parte básica de programação. Vou mostrar alguns exemplos, uns 3 ou 4 exemplos básicos, mostrando a parte básica de funções em Python, e depois já vou começar dedicando para Machine Learning.

Aqui está um exemplo bem trivial: um `print`. Veremos isso depois no `Sublime`, que é o software que usamos para programar em Python. Aqui só tem um `print` do meu programa, mas depois vou mostrar como criar o programa do zero e como executar.

### Foco em Machine Learning

Neste cenário, vamos treinar mais relacionando a parte de Python com outros problemas que temos, principalmente no cenário de Machine Learning.

Como o nosso curso é voltado para Machine Learning, vou tentar direcionar a parte de programação sempre para exemplos que têm relação com o que vamos ver em:

- Redes neurais;
- Máquinas de vetores de suporte;
- Algoritmos de classificação em geral.

É muito importante que vejamos um pouco mais que vai além da parte básica de Python. Neste cenário, principalmente, vamos envolver as nossas bibliotecas. Vamos aprender como usar uma biblioteca para um determinado problema.

Nosso objetivo dentro deste cenário de programação é mais forte do que simplesmente aprender a programar Python. Nosso objetivo será:

- Trabalhar com modelos estatísticos;
- Trabalhar com modelos de validação de dados;
- Modelos de plotar os nossos resultados;
- Plotar imagens;
- Aprender a quantificar os nossos problemas matematicamente.

Para isso, vamos usar bibliotecas como:

- `Pandas`;
- `Scikit-learn`;
- `Matplotlib`;
- `NumPy`.

Essas bibliotecas vão ajudar muito no que precisamos neste cenário de Machine Learning.

### Gerenciamento de Dependências

Uma coisa que vamos aprender também é sobre instalar dependências. Dependências são algumas situações que precisamos definir muito bem, porque às vezes acabamos, por exemplo, subindo um `código` no GitHub. E aí falamos: "Ah, preciso instalar tal dependência para rodar o meu algoritmo." A pessoa instala tudo e continua pedindo outras, porque às vezes fazemos a instalação e no nosso computador já tem outras coisas que instalamos em outro momento.

Vou dar um exemplo para vocês: neste computador que estou usando, eu tenho tanta coisa instalada desde a época do meu doutorado.

`⏱ 15:40`

bibliotecas, várias redes. Não adianta eu falar que o meu algoritmo precisa de algumas dependências apenas; eu tenho que ver exatamente o que eu preciso.

### O Desafio das Dependências em Python

Se tem uma coisa que é chata na parte de Python, são as dependências e as versões dessas dependências.

Às vezes, você desenvolve um `código` e compartilha ele. Quando a pessoa vai rodar seu `código`, pode ser que a versão do Python que ela tem não seja a correta, e ela tenha que mudar a versão. Além disso, pode não estar na versão do TensorFlow que ela utiliza.

Mudar a versão do TensorFlow acaba sendo uma questão chata, relacionada a tanta dependência com o `código`.

Se tem uma coisa que todo mundo reclama é essa parte de dependências: as extensões que precisamos para conseguir executar determinado `código`.

Dentro desse cenário de programação, a parte básica que eu queria comentar é justamente essa.

## Relacionado

- [[paradigmas-e-linguagens-de-programacao-para-machine-learning]]
- [[conceitos-fundamentais-de-machine-learning-inteligencia-artificial-e-generalizac]]
- [[visao-computacional-ia-e-aplicacoes-em-sistemas-autonomos]]
- [[paradigmas-de-programacao-estruturado-e-orientacao-a-objetos]]
