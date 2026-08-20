---
titulo: "Fundamentos de Algoritmos: Vetores, Matrizes e Estruturas de Dados"
tags: [algoritmos, fundamentos, dados, variaveis, pensamento-computacional, estruturas-de-dados]
data: 2026-08-20
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 9
conceitos: [Vetor, Matriz, Estruturas de Dados, Container, Índices, Memória Contígua, Estrutura Abstrata de Dados]
---

# Fundamentos de Algoritmos: Vetores, Matrizes e Estruturas de Dados

> [!resumo] Do que se trata
> A aula aborda a definição e o uso de vetores e matrizes como estruturas de dados para organizar informações em memória. São apresentados exemplos práticos de como essas estruturas otimizam o código e a alocação de memória em comparação com variáveis separadas. Por fim, o conteúdo expande o conceito para outras estruturas de dados abstratas, como Pilha, Lista, Árvore e Grafo.

## Para lembrar

- **Um vetor é uma variável dimensionada com tamanho prefixado, podendo ser encarado como um *container* ou uma matriz unidimensional.**
- **Uma matriz é uma tabela organizada em linhas e colunas (M por N), sendo uma coleção de variáveis ou de vetores.**
- **As matrizes são contíguas em memória, o que permite o uso de índices (linha e coluna) para pesquisar e acessar elementos de forma eficiente.**
- **O uso de vetores e matrizes otimiza o código e a alocação de memória, além de melhorar a legibilidade e a manutenção do código.**
- **Estruturas de dados abstratas incluem Pilha, Lista, Árvore, Grafo, Lista Encaixada e Lista Circular, sendo cada uma adequada para diferentes cenários de resolução de problemas.**

## O que esta nota responde

- Qual a diferença entre usar variáveis separadas e usar vetores/matrizes para armazenar dados?
- Como as matrizes são organizadas na memória do computador e por que isso é importante?
- Quais são os principais tipos de estruturas de dados que um programador deve conhecer?

## Conceitos

**Vetor** · **Matriz** · **Estruturas de Dados** · **Container** · **Índices** · **Memória Contígua** · **Estrutura Abstrata de Dados**

## Conteúdo

`⏱ 00:00`

### Fundamentos de Algoritmo: Vetores e Matrizes

Um vetor é caracterizado por uma variável dimensionada com tamanho prefixado. Ou seja, um vetor é uma variável que possui uma sequência e um tamanho prefixado que irá receber $N$ valores.

Um vetor também pode ser encarado como um *container* ou visto como uma matriz unidimensional.

### Matrizes

Uma matriz é uma tabela organizada em linhas e colunas no formato $M$ por $N$, onde $M$ representa o número de linhas (vertical) e $N$ o número de colunas (horizontal).

*Nota: A descrição de $M$ e $N$ foi invertida na fala, mas o conceito de $M$ linhas e $N$ colunas deve ser mantido.*

As matrizes são uma coleção de variáveis, uma coleção de vetores. Podemos enxergar cada linha aqui como um vetor, ou seja, uma variável com tamanho prefixado unidimensional.

Para navegar por essa coleção de variáveis — essa coleção de vetores — precisamos dos índices, que vão determinar a linha e a coluna onde está cada elemento. Por isso, elas são contíguas em memória, ou seja, estão armazenadas juntamente dentro da memória do computador. É por isso que utilizamos os índices para que possamos pesquisar e puxar as informações dentro dessa matriz.

### Exemplo Prático: Notas Escolares

Para exemplificar, podemos colocar as notas dentro de um vetor de duas posições. Não estou dizendo que esta é a melhor maneira de fazer, é apenas para que vocês possam exemplificar e visualizar como seria um vetor.

Suponhamos que temos as notas:
*   Nota 1 do aluno 1: 10
*   Nota 2 do aluno 1: 5
*   Nota 1 do aluno 2: 12
*   Nota 2 do aluno 2: 2

Nós teríamos:
*   Notas do aluno 1: 10 e 5.
*   Notas do aluno 2: 12 e 2.

Os valores que anteriormente eram colocados em quatro variáveis distintas, nós estamos, então, aqui atribuindo a vetores.

**Comparação de Eficiência:**

Imagine se tivéssemos mais uma nota, vamos supor a P.F. Então, teríamos três variáveis para cada aluno, totalizando seis variáveis.

1.  **Usando variáveis separadas:** Seriam seis variáveis distintas.
2.  **Usando vetores:** Estaríamos utilizando apenas dois vetores de três posições.

Ao utilizar vetores, você economiza em código e em alocação de memória, e elas estão contíguas em memória, o que é muito interessante.

**Definindo o Vetor de Outra Forma:**

Outra forma de definir seria colocar as notas de todos os alunos dentro de um mesmo vetor. Novamente, não estou dizendo que é a melhor maneira de se fazer isso, estou apenas exemplificando.

Neste caso, o que teríamos é que a cada duas posições, eu teria as notas de um aluno. Poderíamos estar definindo um vetor igual a um conjunto, por exemplo, de 1 a 8.

`⏱ 05:40`

Dentro de um intervalo, um `range` de 1 a 8, 8 posições, de inteiros. Ou então, um vetor entre parênteses `(15)` ou vetor igual a... colchetes? Colchetes. Sem nada. Cada um quer dizer a mesma coisa. Tudo bem que aqui são 15 e aqui são 8, mas todos são vetores, são representações de um vetor. O último ali, no caso, seria uma representação em `C`, por exemplo.

A gente poderia colocar os dados dos alunos em matrizes. Olhando essa tabela aqui, nós poderíamos extrapolar isso para uma matriz, onde:

*   A primeira coluna está relacionada ao `ID` do aluno.
*   A segunda coluna é a nota 1.
*   A terceira coluna é a nota 2.
*   A quarta coluna é a nota 3.
*   A quinta coluna é a nota 4.
*   A sexta coluna é a média do aluno.

Cada linha dessa matriz seria como se fosse uma instância de todas as notas relacionadas a um determinado aluno, o aluno que está representado pela primeira coluna.

Agora, você imagina colocar isso em variáveis distintas. A quantidade vai ser utilizada. Essas estruturas mais complexas acabam facilitando nosso entendimento do código e a manutenção do código. Consequentemente, isso também é escrito no código.

Por exemplo, se eu quiser saber a média do quinto aluno, eu vou na coluna 1, aí é quinta posição, e eu sei que vou na 2, 3, 4, 5, 6, na sexta coluna, `M` igual a. No caso, a sexta coluna seria `N`. Então, seria 5 e 6, `5x6`, é exatamente o índice correspondente à média do aluno, do quinto aluno.

Com isso, o que conseguimos?

*   Uma menor quantidade de linhas.
*   Otimização.
*   Melhor legibilidade.
*   Uma série de vantagens.

### Estruturas de Dados

Essa é uma das estruturas existentes. Se a gente começar a entrar mais em estruturas de dados, estruturas, por exemplo, estruturas abstratas. Na verdade, é tipo de abstrato de dados. A gente começa a extrapolar para:

*   Pilha
*   Lista
*   Árvore
*   Grafo
*   Lista Encaixada
*   Lista Circular

Tem uma série aí de outras estruturas que podem ser utilizadas para outros fins. Cada cenário vai demandar uma estrutura diferente, que possa resolver o seu problema, a sua particularidade de uma maneira mais eficiente.

A próxima etapa vai estar falando sobre o que é uma função.

## Relacionado

- [[estruturas-de-repeticao-em-algoritmos-tipos-funcionamento-e-aplicacoes]]
- [[05 - CNN - Redes Convolucionais]]
- [[fundamentos-de-algoritmos-variaveis-tipos-de-dados-e-estruturas-de-controle]]
- [[reconhecimento-de-padroes-conceitos-aplicacoes-e-mecanismos-de-classificacao]]
