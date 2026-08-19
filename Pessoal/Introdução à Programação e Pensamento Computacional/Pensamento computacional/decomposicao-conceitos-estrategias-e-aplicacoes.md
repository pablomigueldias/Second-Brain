---
titulo: "Decomposição: Conceitos, Estratégias e Aplicações"
tags: [pensamento-computacional, fundamentos, conceitos, estudo]
data: 2026-08-19
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 13
conceitos: [Decomposição, Análise, Síntese, Execução sequencial, Paralelismo, Modularização]
---

# Decomposição: Conceitos, Estratégias e Aplicações

> [!resumo] Do que se trata
> Apresenta a decomposição como o primeiro pilar do pensamento computacional voltado a dividir problemas complexos em partes menores e gerenciáveis. Explora as estratégias de análise e síntese, além da execução sequencial ou paralela das subtarefas. Demonstra a aplicação prática do conceito em cenários cotidianos, projetos de software e estruturação modular de ações.

## Para lembrar

- **A decomposição divide um problema complexo em subproblemas menores, resolvíveis e mais fáceis de gerenciar.**
- **O processo envolve duas etapas complementares: a análise (quebra e exame detalhado do contexto) e a síntese (recombinação e reconstrução coerente das partes na solução final).**
- **A ordem de execução das tarefas menores pode ser sequencial, quando há dependências diretas entre elas, ou paralela, quando são independentes e podem rodar concorrentemente para ganhar eficiência.**
- **A decomposição de ações permite estruturar comportamentos complexos em funções modulares e reutilizáveis, como desdobrar a ação de correr em mover a perna e impulsionar.**

## O que esta nota responde

- Qual é a diferença entre as estratégias de análise e síntese na decomposição?
- Quando a ordem de execução das subtarefas deve ser sequencial ou paralela?
- Como a decomposição pode ser aplicada na modelagem de software e no cotidiano?

## Conceitos

**Decomposição** · **Análise** · **Síntese** · **Execução sequencial** · **Paralelismo** · **Modularização**

## Conteúdo

`⏱ 00:00`

### Decomposição

Vamos falar sobre decomposição. Nesta etapa, vamos entender mais detalhadamente o que se trata este pilar.

George Poila, professor de matemática, afirma o seguinte: "Se você tem um problema que não consegue resolver, existe um problema mais fácil que você pode resolver. Encontre-o."

É justamente esta a ideia de decompor, segmentar: dado um grande problema complexo, você o divide em problemas menores.

Este é o primeiro passo na resolução de problemas, o primeiro passo dentro do conceito de pensamento computacional. Dado o problema complexo, podemos quebrar, segmentar, decompor problemas menores, resolvíveis e fáceis de gerenciar. Essa é a ideia.

### Estratégias de Decomposição

Temos as estratégias:

*   **Análise:** Consiste em um processo de quebra e determinar partes menores e gerenciáveis, o que está diretamente relacionado à decomposição. Para isso, você precisa estudar e explorar o seu contexto, tentando decompor os elementos constituintes daquele seu problema. O objetivo é realizar um exame bem detalhado do que você precisa determinar ou resolver. Você encontra as partes principais, quebra esse problema maior e examina esses problemas menores.

*   **Síntese:** A ideia de construção, onde você combina os elementos recompondo o problema original. Na verdade, esta estratégia é um passo a passo:
    1.  Primeiro, você faz a parte da análise, onde quebra o contexto.
    2.  Depois, você tem que recombinar e recompor o problema original de maneira que ele faça sentido.

Não basta simplesmente pegar as peças separadas e juntá-las; elas têm que fazer sentido. Elas precisam ter um porquê. Às vezes, precisam de algo a mais para se encaixarem.

Dentro desse processo, a síntese consiste em reunir os elementos distintos de um único grande elemento, dentro de um processo de reconstrução. Você funde esses elementos de maneira coerente, dando sentido à sua solução.

### Ordem de Execução

Qual é a ordem de execução dessas tarefas menores, desses pequenos problemas? Pode ser sequencial ou paralelo, dependendo do seu contexto, dependendo se há dependências, dependendo do que você precisa.

*   **Sequencial:** Provavelmente existirá uma dependência entre as tarefas, uma execução em fila. Pode ser simplesmente uma ordem, mas às vezes um problema depende do outro. Uma variável está inserida dentro do contexto do outro, e para você resolver aquele problema, você precisa do problema anterior resolvido. Isso pode acontecer, ou então, simplesmente são problemas separados e você pode determinar uma ordem qualquer para resolvê-los.

*   **Paralelismo (Computação Paralela):** É uma estratégia em que você ganha em eficiência e tempo. As tarefas podem ser executadas concomitantemente, concorrentemente, de maneira que elas são isoladas e independentes. Depois que essas tarefas terminam de ser resolvidas, elas são agregadas de maneira que faça sentido e resolve o problema.

### Conclusão

Dentro da decomposição, temos as variáveis que estão presentes dentro desses problemas pequenos, que são determinadas pela segmentação do problema maior.

No entanto, não basta você aplicar esse tipo de coisa. Você tem que entender e desenvolver a decomposição por você mesmo. Não basta eu falar aqui o que é decomposição. Vocês têm que pegar um exemplo e fazer, treinar. Assim como eu falei que o raciocínio lógico é uma habilidade que se treina, a decomposição é a mesma coisa. O pensamento computacional é uma habilidade gerenalista.

`⏱ 05:00`

Em que você precisa treiná-la. Na verdade, qualquer matéria, qualquer área do conhecimento, você precisa de treino. Afinal de contas, o cérebro é um músculo.

Você precisa treinar maneiras distintas de estrutura. Pode acontecer de ter o mesmo problema com soluções diferentes, e às vezes uma mais eficiente do que a outra. Você precisa entender quando utilizar cada uma ou não. Nem sempre existe apenas uma maneira, aquela maneira melhor de resolver, ou aquela maneira mais eficiente.

Por exemplo, um computacional. Às vezes, o seu ganho em eficiência é muito pequeno comparado ao custo que você tem para executar daquela forma. Então, você tem que fazer uma balança, um *trade-off*.

### Como decompor o problema

Como fazer isso?

1.  Você identifica ou coleta os dados que estão relacionados ao seu problema.
2.  A partir do momento que você identifica e segmenta essas informações, esses problemas menores, você depois agrega os dados para entregar a funcionalidade, o resultado, a resolução do seu problema.

### Exemplos de decomposição

**1. Cozinhar (Exemplo do Cotidiano)**

Você pensa, dependendo de qualquer receita, você precisa identificar os ingredientes, cada um com seu grau de complexidade diferente. Você precisa determinar as etapas que vai realizar.

As etapas podem ser sequenciais, pois elas não seguem uma ordenação aleatória, visto que existem dependências entre elas.

*   **Exemplo: Fazer arroz.**
    *   Primeiro, você tem que cortar o alho.
    *   Colocar o azeite na panela.
    *   Colocar o alho na panela.
    *   Fritar o alho para depois colocar o arroz.

Se você alterar essa ordem, pode ser que o gosto saia diferente e não seja tão interessante quanto executado da maneira correta. Ou ele pode ser colocado em paralelo.

Você vai determinar qual é a melhor maneira de executar as suas tarefas, as suas etapas. Você executa cada etapa, e depois você agrega os ingredientes para finalizar e recompor com coerência. A partir daquela segmentação do prato, do que você está fazendo na cozinha, você vai agregar e recompor depois e, aí sim, apresentar o prato final.

**2. Funcionamento de um Objeto (Exemplo da Bicicleta)**

Um outro exemplo está relacionado ao funcionamento de um objeto, como, por exemplo, uma bike. Como é o funcionamento desse sistema?

Você identifica os componentes, o papel de cada componente dentro desse sistema e a interdependência entre as peças.

*   Por exemplo, para que eu consiga andar de bike, eu preciso estar acionando o pedal.
*   O pedal, por sua vez, aciona a correia, ou a corrente.
*   A corrente, por sua vez, aciona uma engrenagem que gira as rodas.

Você entendeu uma parte do sistema. Você continua subindo e aumentando a sua gama de peças para entender como funciona. Para aquele sistema, você segmentou e depois vai passando para outros problemas e, aos poucos, recompondo aquele problema original.

**3. Criação de um Aplicativo (Projeto de Software)**

Outro exemplo seria a criação de um aplicativo, um projeto de aplicativo. Vamos supor:

*   Primeiro, você precisa saber para que ele serve, com a passagem.
*   Depois, qual o tipo de interface, como que você vai projetar, qual é a ideia que você tem e às vezes de esboçar.

Depende quais são as funcionalidades atreladas a ele que você quer que seu usuário tenha de acesso ou de função dentro daquele aplicativo, e quais são os pré-requisitos para que ele funcione.

Tudo isso, você segmentou, decompôs o problema original. Depois, uma vez que você determine essas etapas, você define os componentes. Você definiu os componentes de etapas e, uma vez que isso ocorra, você consegue resolver o seu problema maior, que é o de determinar o projeto.

`⏱ 09:20`

De um aplicativo, assim você consegue um desenvolvimento mais eficiente.

Um artigo, por exemplo, dá para aplicar o pensamento computacional, a decomposição, nesse sentido, para a escrita de um artigo. Vamos definir os componentes e as etapas a serem executados.

O que deve ser abordado dentro desse artigo? Qual é o tema? O que eu preciso estar abordando para que a pessoa que está lendo o meu artigo entenda do que eu estou falando?

Você tem que falar sobre assuntos relacionados antes de falar do seu tema principal. A partir daí, você consegue determinar a estrutura do seu artigo.

A estrutura básica inclui:
- Introdução
- Desenvolvimento (ou corpo do texto)
- Conclusão

Mas dentro desse desenvolvimento, você precisa saber o que vai colocar. Já é mais um passo: o conteúdo de cada tópico.

A parte de implementação, a parte de configuração e a parte de análise, cada uma está separada. E aí, entram os textos de conexão, que vão dar sentido e conectividade ao texto, de maneira que você agregue e dê coerência à sua resolução final.

### Decomposição de Movimentos e Ações

Isso é interessante também: estamos segmentando os movimentos de um avatar.

Vamos supor que eu tenho as ações e aqui eu tenho padrão e movimento.

*   **Movimento:** É andar, correr, sentar, levantar.
    *   *Exemplo:* Dentro de `correr`, eu tenho `mover a perna` e `impulsionar`.
    *   Neste caso, eu tenho duas funções que são chamadas pela minha função principal, pela minha função maior, `correr`. E essa, por sua vez, é chamada como movimento por ação.

No lado esquerdo, podemos ver que temos o padrão `virar` e `mover`.

*   `Virar`: Por exemplo, nós temos `virar para a direita` e `virar para a esquerda`.

### Benefícios da Estrutura Modular

O que é interessante desse tipo de situação, desse tipo de estrutura?

Se eu precisar realizar algum tipo de modificação na minha função, ela será pontual. Isso ocorre porque o padrão `virar` depende de `virar` e de `mover`, e `virar` depende de `direita` e `esquerda`.

Portanto, qualquer modificação que eu faça em `esquerda` e `direita` estará automaticamente refletindo essa mudança nas funções subsequentes que eles estão chamando.

O interessante disso é que você otimiza linhas de código, evita a redundância e melhora o sentido de que você não precisa fazer modificação em vários pontos do seu programa. Basta em um ou em poucos pontos.

É isso que eu queria passar para vocês. Na próxima aula, já entraremos na parte de reconhecimento de padrões.

## Relacionado

- [[fundamentos-e-pilares-do-pensamento-computacional]]
- [[raciocinio-logico-inducao-deducao-e-abducao]]
