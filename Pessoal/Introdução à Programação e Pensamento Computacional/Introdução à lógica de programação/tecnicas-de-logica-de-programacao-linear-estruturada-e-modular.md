---
titulo: "Técnicas de Lógica de Programação: Linear, Estruturada e Modular"
tags: [pensamento-computacional, fundamentos, conceitos, raciocinio-logico, estudo]
data: 2026-08-19
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 8
conceitos: [Técnica linear, Técnica estruturada, Técnica modular, Decomposição de problemas, Manutenção de software, Fluxo de processamento de dados]
---

# Técnicas de Lógica de Programação: Linear, Estruturada e Modular

> [!resumo] Do que se trata
> A aula apresenta os diferentes modelos de raciocínio e estruturação lógica aplicados à resolução de problemas na programação de computadores. São exploradas a técnica linear, caracterizada por operações sequenciais em uma única dimensão, e a técnica estruturada, que adiciona hierarquia e desvios condicionais para facilitar a escrita e manutenção do código. Por fim, detalha-se a técnica modular, demonstrando como a decomposição em módulos independentes com entradas, transformações e saídas simplifica algoritmos e isola alterações.

## Para lembrar

- **A técnica linear caracteriza-se pela execução sequenciada de operações em uma única dimensão e com recursos limitados, onde as ações possuem dependência direta entre si.**
- **A técnica estruturada introduz hierarquias e condições com múltiplas opções de fluxo, atuando como facilitadora na validação e manutenção de sistemas.**
- **A técnica modular divide o problema em partes independentes controladas por regras próprias, seguindo o fluxo padrão de dados de entrada, processo de transformação e dados de saída.**
- **A modularização permite decompor problemas complexos em partes menores e realizar verificações e alterações isoladas em módulos específicos, evitando inconsistências no restante do código.**

## O que esta nota responde

- Qual é a diferença fundamental entre uma abordagem linear e uma estruturada na programação?
- Quais são as principais vantagens de utilizar a técnica modular no desenvolvimento de algoritmos?
- Como funciona a estrutura padrão de processamento de dados dentro de um módulo independente?

## Conceitos

**Técnica linear** · **Técnica estruturada** · **Técnica modular** · **Decomposição de problemas** · **Manutenção de software** · **Fluxo de processamento de dados**

## Conteúdo

`⏱ 00:00`

Vamos começar com as técnicas existentes no nosso mundo de programação que estão associadas à lógica.

Para um exemplo próximo da nossa realidade, vamos supor que estamos analisando um projeto de planejamento de construção de um prédio.

Neste cenário, temos:

1.  Um arquiteto, que vai terminar a planta baixa. Ele abstrai qual o tipo de construção é — se é um prédio, uma casa, enfim, o tipo de construção.
2.  Há uma planta baixa associada a esse projeto de planejamento.
3.  Em seguida, teremos o projeto dessa construção, dessa edificação, que será realizado pelo engenheiro.
4.  Posteriormente, o planejamento da área responsável determinará a viabilidade do projeto.

Todos esses profissionais seguem uma lógica e determinam instruções a fim de conseguir o objetivo.

*   Qual é o objetivo do arquiteto? Preparar a planta baixa.
*   Qual o objetivo do engenheiro? Preparar o projeto a partir da planta baixa fornecida.
*   E, por sua vez, o planejamento vai definir as estratégias a partir do projeto fornecido pelo engenheiro.

Nós temos duas técnicas. A primeira delas é a técnica linear.

### Técnica Linear

Ela vem do modelo tradicional. Não tem vínculo e possui uma estrutura hierárquica. É bastante utilizada na programação de computadores.

Podemos entender essa técnica como um modelo de desenvolvimento e resolução de problemas. É uma técnica muito associada à matemática pela sua característica linear.

O que podemos entender por técnica linear é que ela é a execução sequenciada de uma série de operações, a ordenação de elementos, em uma única propriedade. Isso ocorre quando temos recursos limitados e uma única dimensão.

Por exemplo, lembre do vetorzinho da busca binária: uma única dimensão, recursos limitados e execução sequenciada. Isso é o que caracteriza a técnica linear.

**Exemplo do dia a dia:**

Todo mundo acorda e toma seu cafezinho, ou pelo menos a grande maioria. Eu, por exemplo, quando estou cansada, preciso de um cafezinho.

Eu levanto, teço as escadas, ou simplesmente ando pelo corredor, chego na cozinha, preparo meu café na cafeteira, e aí sento, leio o jornal e tomo meu café.

Este é um exemplo de uma técnica linear, onde temos uma execução sequenciada e uma única dimensão. Eu tenho uma sequência de ações a serem executadas de maneira ordenada e que possuem dependência entre si.

### Técnica Estruturada

Nós entramos na parte da técnica estruturada, onde temos a organização e disposição e ordem dos elementos essenciais que compõem o corpo concreto ou abstrato.

O que isso quer dizer? Dado o processamento de dados, o objetivo da técnica estruturada é a parte da escrita de programas, entendendo, validando e mantendo o sistema.

Na manutenção, por exemplo, é caracterizado como facilitador.

Vamos pensar em uma técnica estruturada. Por exemplo, de repente, ter alguma condição. A parte de estruturação define uma hierarquia. Aqui eu posso ter mais de uma opção. Ela não é linear.

Por exemplo: eu acordo, faço meu café ou faço o suco, para quem não tomar café, e depois disso tomo café da manhã.

Em uma técnica linear, nós não teríamos esse tipo de escolha; seria ou suco ou seria café.

`⏱ 05:00`

Em uma técnica estruturada, você adiciona um pouco mais de complexidade, mas isso acarreta uma série de vantagens.

Nós temos a técnica modular, onde definimos partes independentes que são controladas por um conjunto de regras. Cada `módulo` tem o seu conjunto de regras específico.

Dentro da técnica modular, temos:
1. Os dados de entrada.
2. O processo de transformação.
3. Os dados de saída.

Este é o modelo padrão de uma técnica modular.

#### Vantagens da Modularidade

O que conseguimos com isso é a simplificação do algoritmo e da resolução do problema. Podemos decompor o problema em problemas menores e, assim, também fazer a verificação por `módulo`.

Em vez de verificar todo o código, ou de repente se mexer em uma parte do código que vai alterar outra e acarretar em erros de inconsistências, eu posso concentrar as alterações dentro de um `módulo` específico — aquele que eu estou querendo modificar.

#### Exemplo Prático: O Café da Manhã

Para seguir com o nosso exemplo do café da manhã, podemos identificar vários módulos:

*   **Módulo Preparar para Acordar:** Este módulo tem suas regras definidas. Por exemplo, para que eu acorde, eu preciso tirar o descansa-olho, levantar da minha cama, sentar na minha cama, levantar e ir em direção à escada, ao corredor.
*   **Módulo Preparar Bebida:** No próximo `módulo`, teremos as regras associadas a cada tipo de bebida. Podemos receber por `argumento` ou por `parâmetro` se a bebida é quente ou fria, e a gente executa as ações e as regras a partir de determinado `argumento`.
*   **Módulo Tomar Café da Manhã:** O último `módulo` seria o de tomar café da manhã, com as regras e as ações relacionadas a este processo.

É essa a ideia.

#### Conclusão das Técnicas

Essas são as técnicas existentes: linear, estruturada e modular. Vamos perceber que utilizaremos isso de maneira muito intuitiva quando chegarmos ao fundamento de algoritmo.

## Relacionado

- [[conceitos-fundamentais-de-logica-e-logica-de-programacao]]
- [[visao-geral-da-carreira-em-ti-da-rede-a-ciencia-de-dados-e-programacao]]
- [[raciocinio-logico-inducao-deducao-e-abducao]]
- [[fundamentos-de-algoritmos-conceito-estruturacao-e-formas-de-representacao]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Então, até a próxima etapa.

</details>
