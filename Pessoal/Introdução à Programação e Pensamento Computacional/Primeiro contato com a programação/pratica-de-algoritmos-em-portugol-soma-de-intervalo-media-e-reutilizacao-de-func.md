---
titulo: "Prática de Algoritmos em Portugol: Soma de Intervalo, Média e Reutilização de Funções"
tags: [pensamento-computacional, algoritmos, caso-pratico, fundamentos, raciocinio-logico]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 16
conceitos: [Portugol Web Studio, Funções, Reutilização de código, Parâmetros, Raciocínio lógico algorítmico, Variáveis e tipos de dados]
---

# Prática de Algoritmos em Portugol: Soma de Intervalo, Média e Reutilização de Funções

> [!resumo] Do que se trata
> A aula demonstra a implementação prática de algoritmos utilizando o Portugol Web Studio para exercitar o raciocínio lógico sem barreiras de sintaxe. São desenvolvidos dois exemplos com definição de funções: o cálculo da soma em um intervalo numérico e o cálculo da média de notas de alunos. Destaca-se a importância da reutilização de código proporcionada por funções e as possibilidades de exploração de bibliotecas e algoritmos na ferramenta online.

## Para lembrar

- **O Portugol utiliza uma sintaxe simplificada e próxima da linguagem natural para facilitar o desenvolvimento do raciocínio lógico sem a barreira das linguagens de programação formais.**
- **A função de soma de intervalo foi implementada calculando o resultado parcial (y + x) multiplicado pelo total da divisão do limite por 2.**
- **O Portugol Web Studio roda direto no navegador, oferecendo exemplos nativos de laços, condicionais e bibliotecas embutidas como matemática e texto.**
- ⚠ **A utilização de funções permite a reutilização de código, garantindo que futuras alterações de regra ou lógica precisem ser feitas em apenas um único local.**

> [!atenção] Confira os marcados com ⚠
> Citam um número ou fórmula que não aparece na transcrição. Pode ser erro do modelo, ou pode ser a aula tendo dito e o Whisper não ter ouvido.

## O que esta nota responde

- Por que utilizar Portugol em vez de uma linguagem de programação tradicional no início dos estudos?
- Como a criação de funções contribui para a reutilização e manutenção de código?
- Como implementar a leitura de dados e chamada de funções no Portugol Web Studio?

## Conceitos

**Portugol Web Studio** · **Funções** · **Reutilização de código** · **Parâmetros** · **Raciocínio lógico algorítmico** · **Variáveis e tipos de dados**

## Conteúdo

`⏱ 00:00`

Agora vou mostrar dois exemplos simples para fazermos os dois exemplos de pesamento computacional.

Os exemplos são:
- Somando o intervalo.
- A média da nota do aluno.

Vou utilizar o site `Portugal Web Studio`.

***

### Configuração do Ambiente

Ao acessar o site, é interessante notar que ele possui a opção "Explorar exemplo". Ele passa alguns exemplos numerados e vai incrementando a dificuldade, por exemplo, de estruturas condicionais, laços e repetição fatorial. Há uma série de exemplinhos que vocês podem observar e aprender a usar.

No nosso caso, vamos fazer a soma do intervalo. Para isso, vou olhar a estrutura que apresentei antes.

***

### Implementação do Código

Dentro da função `início`, vou definir duas variáveis, `X` e `Y`. Posso ler do teclado ou adicionar diretamente. Vou optar por ler do teclado.

Vou escrever: "Digite os números para executar a soma do intervalo".

Em seguida, vou colocar `label` para `X` e depois `label` para `Y`. Abaixo, escrevo e chamo a função `soma_em_intervalo`, passando os parâmetros `X` e `Y`.

Abaixo, vou definir minha função.

`Função` do tipo `inteiro`.

Preciso definir o tipo e o nome, que será `intervalo`. Novamente, o tipo `inteiro`.

`x` inteiro
`y` inteiro

Vou seguir o mesmo nome que dei lá, que é `total`.

`total` recebe `y` dividido por 2 e vou colocar em cima `resultado_parcial`. Foram essas duas variáveis que coloquei no slide.

`resultado_parcial` igual a `y` mais `x`. Este é o resultado parcial.

Vou retornar o resultado. Posso colocar: atribuir uma variável é igual a `total` vezes `resultado_parcial` e aí eu não retorno resultado. Não esqueci de nada.

Vamos executar. É bem simples. Vou colocar o número 1 e depois vou colocar o número 200. Corresponde exatamente ao valor que encontramos no nosso exemplo dos slides.

***

### Teste e Conclusão

Vamos testar com outro número. Vamos supor... número 500. Também retornou perfeito.

Aqui vocês podem modificar o nome para, por exemplo, `soma_intervalo`. E podem começar a explorar o site.

O legal dele é que, como ele tem uma sintaxe bem simplificada, por exemplo, `função inteiro`, ele está próximo da nossa linguagem natural. Assim, vocês não têm a barreira da sintaxe da linguagem de programação.

`⏱ 06:20`

Aqui, vocês conseguem exercitar um raciocínio lógico, o tipo de raciocínio que vocês precisam para estar criando algoritmos. Esse tipo de coisa é bem legal.

Quando eu entrei no técnico, e acho que na faculdade um pouco também, mas no técnico eu aprendi primeiro a escrever algoritmo com o Portugol, na verdade, com essa estrutura aqui no papel. Depois a gente usou o VisualG, se eu não me engano, para fazer isso daqui, depois que nós fomos ver alguma linguagem de programação.

O que acontece? Como você está focado apenas em entender como você constrói seu algoritmo e não a sintaxe do programa, fica mais fácil para você desenvolver ali o seu raciocínio lógico voltado para a construção de algoritmos, entendeu?

### Exemplo Prático: Média de Alunos

Vou fazer da mesma média do aluno, só para ficar de exemplo para vocês também, que vocês podem estar fazendo junto comigo. Depois vocês podem fazer algum outro exercício, como por exemplo o de matrizes, usar o vetor para colocar as nossas os alunos.

Vamos lá. Dado o início, eu tenho como `real A` e `B`.

Aí aqui eu vou estar assim:
1. Escreva nota um do aluno.
2. Leia, digite a nota 2 do aluno. Ou a nota da P1, a nota da P2.
Então vou colocar `nota P2`, `P1`, `P2`. Leia `P`.

Aí eu vou fazendo assim: `escreva a média do vírgula`.

Aí eu vou criar uma função que vai ter um nome `média aluno`, A, aí a gente vai estar passando por parâmetro A e B.

Muito bem.
`função que retorna um número real média_aluno(real nota_A, real nota_B)`

Ó, vamos botar assim, por exemplo. E digite só para a gente poder verificar o reuso é a parte de reutilização de código.

Digite as notas da P1 e P2 do aluno A e a. Aí eu coloco:
`leia A`
`leia B`

A é aqui, vou copiar.
`escreva nota A`
`média do aluno A`
`média do aluno B`

Então, AB, eu botei lá em cima a nota 2, nota B, nota A. Então, aqui eu vou colocar nota A, nota B, ok.

Vamos continuar a nossa função. Aqui dentro eu vou fazer o seguinte:
`retorne (nota_A + nota_B) / 2`
Simplesmente isso.

Digite as notas do aluno A. Vamos botar 5, 7. Do aluno B é 8, 9.

Aí eu tenho que dar um barra entre ali. Mas ó, média do aluno é 6 e o médio do aluno é 8.5. Então, deixa eu só dar uma espassadinha aqui. Ok. Aqui eu tenho que dar barra entre. Vamos deixar só mais bonitinho agora.

Muito bem. Então a primeira nota foi 6, a segunda foi 7. A primeira do B foi 8 e a segunda foi 7.46. Então, a média do aluno A foi 6.5, a média do aluno B foi 7.73. Programa finalizado.

### Conceito de Reutilização de Código

O que a gente consegue perceber aqui? Reutilização de código.

Se eu, por acaso, modificasse a, por exemplo, ah, eu vou dar um ponto a mais para todos eles na média dentro da somatória nota A e B, eu só modifiquei um lugar. Eu não preciso modificar em todos os locais em que se eu tivesse colocado da chamada da função, colocada a operação. Aqui são só dois, mas em muitos casos você vai estar utilizando a mesma função diversas vezes, ok?

Então isso é muito interessante para a utilização de código.

Gente, isso aqui foi só uma palhinha para que vocês possam aí estar praticando sozinhos, praticando.

`⏱ 13:40`

...vendo como seria utilizar o `Portugal Web Studio`. O legal é que é mais rápido do que escrever. Qual é o bom de escrever? É que você fundamenta. Você tira da memória RAM e manda para o HD, vai para o disco rígido lá no seu cérebro, e você consegue fundamentar o seu conhecimento.

Eu, Juliana, quando estudo, gosto muito de escrever. É a maneira que eu mais fixo é quando estou escrevendo. Se eu puder dar uma dica, façam isso: com dificuldade de fixar algum tipo de conteúdo, escreva. Você vai fixar melhor.

### Explorando a Ferramenta

Aqui a gente fez os nossos dois exemplos tranquilinhos. Isso aqui é só para vocês começarem, e o bom é que vocês podem explorar os exemplos que já existem aqui, verificar as bibliotecas existentes: matemática, texto, enfim. Essa ferramenta é bem legal e vocês não precisam estar instalando nada.

Se vocês quiserem, podem fazer uma busca. Vocês podem verificar: não tem a busca binária, mas tem a pesquisa em vetor. Vocês podem estar utilizando ali a varredura, aquela varredura mais simples, que é passar da posição zero em diante.

Vocês podem dar uma procurada: "Como verificar o tamanho de um vetor com `Portugal Web Studio`". Tendo isso, vocês conseguem reproduzir tranquilamente a pesquisa binária, que é só verificar, dado na posição, se aquele valor é menor ou maior do que o meu alvo, o meu valor alvo. Se for menor, você já sabe qual é o seu início e qual é o seu fim.

### Conclusão

Espero que vocês tenham gostado e aproveitado bastante o curso. Vou passar as referências bibliográficas antes de finalizar.

## Relacionado

- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]
- [[aplicacao-pratica-dos-pilares-do-pensamento-computacional-em-estudo-de-caso]]
- [[logica-proposicional-2-conectivos-parte-1]]
- [[fundamentos-e-pilares-do-pensamento-computacional]]
