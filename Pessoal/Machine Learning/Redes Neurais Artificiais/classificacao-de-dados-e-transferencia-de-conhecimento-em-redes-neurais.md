---
titulo: "Classificação de Dados e Transferência de Conhecimento em Redes Neurais"
tags: [machine-learning, redes-neurais-artificiais, conceitos, algoritmos, dados, estudos]
data: 2026-08-21
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 16
conceitos: [Classificação, Redes Neurais, Matrizes Convolucionais, Rótulo, Base de Dados de Treino, Pesos, Transferência de Conhecimento]
---

# Classificação de Dados e Transferência de Conhecimento em Redes Neurais

> [!resumo] Do que se trata
> A aula aborda o problema de classificação, explicando como redes neurais podem ser treinadas para diferenciar classes de objetos, como gatos e cachorros. São detalhados os processos de treinamento, desde a necessidade de rótulos e a montagem de bases de dados, até a estrutura dos pesos e a capacidade de transferir conhecimento entre diferentes tarefas ou robôs.

## Para lembrar

- **Para um sistema binário, o valor de saída pode ser 1 (se for a classe) ou 0 (se não for a classe).**
- **A classificação é feita por matrizes convolucionais que leem a imagem em pedaços, e essas matrizes são unidas em todas as camadas da rede para gerar o valor de saída.**
- **O treinamento de uma rede neural requer uma imagem de entrada e um rótulo (nome) que define o tipo de objeto, ensinando o sistema o que é cada classe.**
- **Os pesos são gerados entre as conexões das camadas da rede e representam o aprendizado do método de machine learning, sendo o arquivo de pesos o arquivo de treinamento.**
- **É possível transferir o aprendizado de um robô para outro (ex: cozinheiro para motorista), fazendo com que ambos os robôs tenham o mesmo conhecimento sobre os dois aspectos.**

## O que esta nota responde

- Como uma rede neural é usada para resolver problemas de classificação?
- O que é necessário para treinar um modelo de classificação em redes neurais?
- Como o conhecimento aprendido em uma tarefa pode ser aplicado em outra?

## Conceitos

**Classificação** · **Redes Neurais** · **Matrizes Convolucionais** · **Rótulo** · **Base de Dados de Treino** · **Pesos** · **Transferência de Conhecimento**

## Conteúdo

`⏱ 00:00`

Falando de classificação, um dos problemas que mais utilizamos redes neurais para soluções é o problema baseado em classificação.

O que seria um problema baseado em classificação? Eu quero que minha rede neural diferencie os alunos que eu tenho dentro da minha sala. Eu reconheço um rosto e digo: "É a minha filha." Eu reconheço outro rosto e digo: "É o Pedro." Esse é o tipo de problema.

O problema mais conhecido na literatura e também na parte de projetos é o seguinte:

Por exemplo, a gente pode treinar um sistema para reconhecer apenas gato e cachorro. O sistema vai dizer se é um gato. Se for gato, ele vai me dar o valor 1. Se não for gato, ele vai dar valor 0 na saída, porque é um sistema binário, pois eu só tenho duas classes. Então, se deu valor 1, é gato; se deu valor 0, não é gato, então é cachorro.

Isso não daria certo, por exemplo, se eu incluir o animal raposa. Porque daí eu tenho três valores de saída: gato, cachorro e raposa. Já não é mais uma saída binária. Eu vou ter que reconhecer o tipo desse animal por meio de um valor de saída que representa essa classe. Pode ser um código binário.

Por exemplo:
- `000` vai ser gato.
- `001` vai ser cachorro.
- `011` vai ser raposa.

Pronto, já está definido.

### Como Funciona a Classificação

A classificação, como eu disse para vocês, é o seguinte: uma imagem é capturada e essa imagem é levada para as matrizes convolucionais. Essas matrizes vão ler a minha imagem. Elas vão ler a imagem em cada parte, cada pedacinho da imagem, que vai ser lido por uma matriz, certo?

Depois, essas matrizes são unidas entre todas as camadas da rede. E lá no final, eu vou ter a minha resposta, que esse animalzinho é um gato, ok? O animal de baixo não é um gato, então depois de passar por toda a classificação, ele vai dizer: "É um cachorro." Ou simplesmente: "Não é um gato."

Se não é um gato, eu sei que é um cachorro, porque eu só tenho dois tipos de objetos a serem classificados por meio do meu sistema, certo?

O que a gente tem representado aqui nessa imagem são as camadas de neurônios da minha rede, porque são todas conectadas para gerar o meu valor de saída.

### Treinamento do Modelo

Como é que eu vou dizer para a minha rede o que é gato e o que é cachorro? Eu tenho que ensinar a rede sobre isso.

Eu vou ter uma imagem de entrada, que é a imagem do animal. Uma imagem de um gato, uma imagem de um cachorro, outra imagem de um gato. Para dizer o que é cada bichinho desses, eu vou ter que ter um rótulo.

O que é um rótulo? É um nomezinho para esse tipo de objeto. Então, eu vou dizer que esse objeto é um gato. Se ele é um gato, eu tenho que dizer de forma verbal, colocando ali o rótulo e rotulando, então, esse animal como gato.

E aí, no final, o meu sistema de classificação ele vai ter que dizer se é um gato, se é um cachorro. Basicamente, a gente vai dizer se é gato ou não é gato. Se não for gato, obviamente é um cachorro.

Aqui a gente tem um exemplo. Esse primeiro exemplo, a gente viu que a gente só tem duas classes a serem classificadas: gato e cachorro. Mas a gente pode partir para exemplos onde a gente tem mais classes.

`⏱ 05:00`

Se pensarmos nos números de 1 a 9, temos 9 classes de números. No entanto, se começarmos a contar do zero, temos 10 classes: 0, 1, 2, 3, 4, 5, 6, 7, 8 e 9.

Ao utilizarmos ferramentas como os OCRs (Optical Character Recognition), que percorrem um texto escrito à mão ou um livro físico digitalizado, conseguimos reescrever e digitalizar esse texto para que ele possa ser utilizado para outras finalidades. Além do conjunto numérico de 0 a 9, essas ferramentas lidam também com o alfabeto, as acentuações e tudo mais.

Uma rede neural, neste caso, recebe um valor de entrada, como a letra A. A rede terá que classificar qual é o tipo dessa letra: se é uma letra A, se é uma letra B. A imagem é percorrida por matrizes, e no final, o sistema deve dizer que a letra na entrada é a letra A.

É importante notar que em situações com muitas classes, quanto mais classes tivermos, mais fácil é o nosso sistema errar.

### Erros de Classificação em OCR

O OCR, ferramenta que avalia números e letras, comete erros frequentes em pares de caracteres parecidos.

*   **1 e 7:** O erro é muito comum entre o 1 e o 7. Isso ocorre principalmente quando o 1 é desenhado com uma ponta e uma base. Se a pessoa desenha o 1 apenas como um risquinho, é fácil de classificar. Mas quando o 1 tem uma ponta e uma base, ele fica muito parecido com o 7.
*   **4 e 9:** Outro erro comum é entre o 4 e o 9, pois o 9 é essencialmente um 4, mas fechado.
*   **6 e 8:** O número 6 e o 8 também geram confusão, pois a parte de baixo é igual, e apenas a parte de cima muda um pouco.

Quanto mais classes temos, mais fácil é a confusão.

### Montando a Base de Dados de Treino

Para montar uma base de dados ou uma base de treino, o método mais fácil é o seguinte:

1.  **Definir a Tarefa:** Queremos classificar gatos e cachorros.
2.  **Criar Pastas:** Criamos uma pasta e a enchemos de fotos de gatos. Quanto mais exemplos de gato, melhor. Colocamos fotos de diferentes tipos:
    *   Um gato preto.
    *   Um gato amarelo e branco.
    *   Um gato acinzentado.
    *   Um gato siamês.
    *   Um gato preto e branco.
    *   Um gato tricolor.
3.  **Nomear a Pasta:** Nomeamos a pasta simplesmente como `gatos`. Dessa forma, o sistema, na hora do treinamento, saberá que tudo que está dentro dessa pasta são gatos e fará a classificação.
4.  **Criar a Segunda Classe:** Para diferenciar gato e cachorro, criamos outra pasta e a enchemos de fotos de cachorro. O nome dessa pasta deve ser `cachorros` (ou `cachorro`, no singular).

Quanto mais exemplos, mais robusto ficará o sistema.

Para classificar gato e cachorro, cerca de 100 imagens é um valor bom. No entanto, se aumentarmos isso, colocando mil imagens de cada, o sistema treinará com uma capacidade maior. Isso fará com que o treinamento demore um pouco mais, mas a resposta do aprendizado será muito melhor.

`⏱ 09:40`

Pensando tudo isso que vimos até agora, é o que gera um valor de treinamento. O que é um treinamento? Depois que a rede rodar, o que é gerado nesse treinamento?

Porque eu tenho uma rede neural com imagens na entrada, o que muda na rede neural? Um treinamento é formado por vários valores, que são chamados pesos. Os pesos são gerados entre as conexões. Os valores gerados entre as conexões são chamados de pesos.

Esses pesos são o nosso treinamento. Depois de um treinamento feito, as conexões entre os neurônios vão receber valores numéricos. Esses valores numéricos, que são os pesos, representam o meu treinamento.

Se pegarmos uma conexão aqui da rede, entre uma camada e outra camada, teremos um arquivo de pesos. Esse arquivo de pesos tem valores como 0, 1, 3, 30, 0, 2000, 2 e 3. Esse arquivo representa os pesos de treinamento dessa camada.

Esse arquivo de pesos geralmente é um arquivo `txt`. Ele representa o aprendizado da minha rede neural, do meu método de *machine learning*. Depois de rodar o treinamento, terei um arquivo `txt` com todos os pesos das conexões da rede. Esse arquivo é o meu arquivo de treinamento, é o meu arquivo de pesos que representa o meu conhecimento.

Por quê? Se eu pegar essa rede neural, que é um modelo matemático, e tirar os pesos dela, ela é apenas uma estrutura matemática. Esse arquivo de pesos que foi gerado no treinamento é o conhecimento da rede.

### Transferência de Conhecimento

Falando em filmes de ficção científica, quando vemos a mente de uma pessoa sendo transferida para outra, não seria transferir o cérebro, pois o cérebro é a máquina biológica. Seria transferir os valores matemáticos do nosso cérebro para outra pessoa.

No caso de uma rede, é a mesma coisa. A rede é só um modelo matemático. Para eu transferir esse modelo de treinamento para outra rede, basta pegar esse arquivo `TXT` e colocar na outra rede, em outra máquina, em outro servidor. Ela terá o aprendizado de forma efetiva.

A gente chama isso de *transfer learning*. Pegamos uma rede, tiramos o aprendizado dela, colocamos em outro lugar, e aquela rede terá o mesmo aprendizado da rede que foi treinada. Eu transfiro o aprendizado para outras coisas.

Isso é usado muito na robótica. Por exemplo, treinamos dois robôs: um para dirigir um carro e outro para cozinhar. Se eu quero que os dois tenham o mesmo conhecimento, eu transfiro o aprendizado do robô cozinheiro para o robô motorista, e transfiro o conhecimento do robô motorista para o robô cozinheiro. Assim, os dois robôs terão o mesmo conhecimento sobre os dois aspectos.

### Estrutura dos Pesos e Saída

Professor, mas o arquivo de peso deve ser muito complicado? Não. São arquivos, são valores que variam do valor negativo para o positivo, e representam a ponderação das sinapses neurais da minha rede neural artificial.

Aqui temos o arquivo de treinamento, o arquivo de pesos, e temos a saída, que é o nosso arquivo de resposta.

Podem ver, por exemplo, que tenho quatro valores de saída. Isso significa que a minha rede tem quatro neurônios de saída. Quando tenho um valor negativo, [inaudível].

`⏱ 14:40`

Significa que a resposta está negada. Quando há um valor positivo, significa que é um valor positivo para a minha resposta. Eu estou dizendo um sim para aquela saída.

Vamos supor que o meu primeiro neurônio é o neurônio cachorro. O meu segundo neurônio é a raposa. Meu terceiro neurônio é gato, e o quarto é passarinho.

Nesta saída, como o terceiro neurônio é gato, e só esse neurônio está positivo (o valor 1 positivo), significa que o que eu encontrei na minha saída da rede, por meio dos valores que eu li na entrada em relação aos pesos de treinamento, é um gato.

Se tivesse o último valor positivo apenas, significaria que o que eu encontrei é um passarinho. Se fosse o primeiro peso positivo, significaria ser um cachorro, e por aí vai.

### Funcionamento do Algoritmo de Rede Neural

Como funciona um algoritmo de rede neural? Implementar uma rede neural hoje não é difícil, porque temos várias bibliotecas para ajudar nisso. Vamos ver aqui algumas aplicações envolvendo isso.

## Relacionado

- [[visao-computacional-processamento-de-imagens-e-extracao-de-caracteristicas-em-re]]
- [[reconhecimento-de-padroes-conceitos-aplicacoes-e-mecanismos-de-classificacao]]
- [[logica-difusa-redes-neurais-generalizacao-e-algoritmos-bioinspirados]]
- [[redes-neurais-deep-learning-e-aplicacoes-praticas-de-machine-learning]]
