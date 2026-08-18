---
titulo: "Lógica Proposicional 5 — Negações e Equivalências"
tags: [logica-proposicional, negacao, equivalencia, leis-de-morgan, contrapositiva, concursos]
data: 2026-08-17
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 30
conceitos: [Leis de Morgan, Negação da Condicional, Negação do Bicondicional, Dupla Negação, Contrapositiva, Leis Comutativas]
---

# Lógica Proposicional 5 — Negações e Equivalências

> [!resumo] Do que se trata
> Quinta parte da série. Negação dos quatro conectivos — as duas Leis de Morgan,
> o macete "Mané" para a condicional, e o bicondicional que se nega com "ou" — e
> as duas equivalências que mais caem em concurso: Inverte Negando
> (contrapositiva) e $\neg P \lor Q \equiv P \to Q$.

## Para lembrar

- **$\neg(P \land Q) \equiv \neg P \lor \neg Q$** — negar o "e" vira "ou", negando as duas (Lei de Morgan).
- **$\neg(P \lor Q) \equiv \neg P \land \neg Q$** — negar o "ou" vira "e", negando as duas (Lei de Morgan).
- **$\neg(P \to Q) \equiv P \land \neg Q$** — mantém a primeira e nega a segunda (macete "Mané").
- **A negação do bicondicional é o "ou" exclusivo** — na tabela verdade as duas colunas são opostas.
- **$P \to Q \equiv \neg Q \to \neg P$** — Inverte Negando, a equivalência que mais cai (~70% das questões).
- **$P \to Q \equiv \neg P \lor Q$** — a segunda mais cobrada; macete "não pode ver queijo".
- **$\neg(\neg P) \equiv P$** — dupla negação: negar duas vezes é afirmar.

## O que esta nota responde

- Como se nega cada um dos quatro conectivos?
- Qual a diferença entre negação e equivalência na hora da prova?
- Quando usar Inverte Negando e quando usar "não pode ver queijo"?

## Conceitos

**Leis de Morgan** · **Negação da Condicional** · **Negação do Bicondicional** · **Dupla Negação** · **Contrapositiva** · **Leis Comutativas**

## Conteúdo

`⏱ 00:00`

Eu volto com mais um vídeo sobre lógica proposicional, um assunto que cai em todo concurso público. Se você vai fazer a área policial — Polícia Federal, Polícia Militar, Polícia Civil — cai. Se você vai fazer concursos da área da saúde, tem esse conteúdo lá. Concurso da área administrativa, fiscal, todos. A maioria dos concursos, 99%, cai esse assunto. Alguns vestibulares também, como o da Uneb, que cobra muito.

Nesse vídeo em especial, vamos falar sobre negações e equivalências.

Quem vem acompanhando os outros vídeos: eu dividi esse conteúdo em algumas partes, e esta é a quinta. Vejam os vídeos anteriores antes de assistir a este.

No vídeo 2 eu falei sobre negação e sobre equivalência, mas de forma mais ligeira, por alto. Chegou a hora de verticalizar esse conteúdo — de entender com profundidade qual é a ideia da negação, qual é a ideia da equivalência, e de que forma são cobradas em concursos.

### Negação das Operações Lógicas

A gente aprendeu que o símbolo de negação é $\neg$ (ou o traço sobre a letra). A negação transmite a ideia contrária da frase dada. Mas eu quero falar agora de negações de proposições **com conectivos**.

Antes de começar, nem toda prova vai trazer a palavra "negação". Quando o autor quer te distrair, ele lança mão de outras expressões:

- "**Não é verdade que** moro na Bahia."
- "**É falso que** matemática é uma disciplina difícil."

Tem outra forma de distrair. Se eu digo:

- "A avó disse aos seus netos que todas as laranjas estão maduras, **porém a avó se confundiu**." (foi questão da FCC)
- "O diretor determinou que todos os estudantes deveriam usar camisa branca na quarta-feira, **porém a ordem foi descumprida**."

"Ordem descumprida", "se confundiu" — tudo isso é ideia de negação. Toma cuidado.

Vou começar com a negação da conjunção, que é o $P \land Q$:

$$\neg(P \land Q) \equiv \neg P \lor \neg Q$$

Quem provou isso para a gente foi um matemático chamado **Morgan** — por isso essa primeira e a segunda (a negação da conjunção e a negação da disjunção) são chamadas **Leis de Morgan**.

`⏱ 04:20`

Escrevam essa expressão no caderno. Quando a prova falar em Leis de Morgan, já sabe: está falando da negação do "e" e da negação do "ou".

Traduzindo a fórmula: **para negar o "e", basta trocar por "ou" e negar as duas proposições.**

**Exemplo (caiu em prova):** "Sou baiano ($P$) e gosto de acarajé ($Q$)."
A negação é: "Não sou baiano **ou** não gosto de acarajé."

E se for o contrário? A negação da disjunção é uma fórmula muito parecida — **no "ou" você coloca o "e" no meio e nega as duas**:

$$\neg(P \lor Q) \equiv \neg P \land \neg Q$$

Isso pode ser provado matematicamente, mas não é o objetivo aqui; o foco é prova. **Jeito fácil de decorar:** se pedirem a negação do "e", você bota "ou"; se pedirem a negação do "ou", você bota "e". Sempre negando as duas proposições.

**Exemplo:** "O número 2 é par ($P$) ou 3 é um número ímpar ($Q$)."
A negação: "O número 2 não é par **e** 3 não é ímpar." Observe que o "ou" virou "e".

Essas duas caem bastante em concurso e são as mais fáceis que existem.

Bora engrossar o caldo. Agora a **negação da condicional**. Pensei nesta frase: "Se Roberta procura, então ela acha."

A negação do "se… então" se faz com esta fórmula:

$$\neg(P \to Q) \equiv P \land \neg Q$$

E aí eu criei um macete chamado **Mané**:

- **Man** = **man**tém a primeira
- **é** = n**e**ga a segunda (com um "e" subentendido no meio)

Uso o Mané quando a prova pedir **negação da condicional**. Então, para "Se Roberta procura, então ela acha", a negação é: mantém a primeira —

`⏱ 08:20`

"Roberta procura" — tira o "se", não existe mais o "se" — e nega a segunda: "e ela não acha".

Isso não tem nada a ver com o Inverte Negando. **Inverte Negando é equivalência; aqui eu estou em negação.**

Para fechar as regras das negações, a **negação do bicondicional**. Eu sempre falei em sala que a gente tem que pecar pelo excesso, e choveram questões de negação do bicondicional e do "ou" nas provas de 2019 e 2020.

A negação do bicondicional pode ser escrita de três formas:

- ou você nega o $P$ e deixa o $Q$;
- ou você deixa o $P$ e nega o $Q$;
- ou você usa o **"ou" exclusivo**.

Se vocês montarem a tabela verdade, vão verificar que **a coluna do "ou" exclusivo é exatamente oposta à coluna do bicondicional** — por isso o "ou" também é uma forma de negar o bicondicional.

**Exemplo:** "Isabela é linda $\leftrightarrow$ Lucas é alto."
Uma das negações possíveis: "Isabela **não** é linda se e somente se Lucas é alto." (usei a primeira forma)

Agora, algumas questões de concurso sobre negação.

### Questão 1 — Negação de Conjunção

> Considere a afirmação: "Eu recebi o boleto **e** não paguei." A negação lógica dessa afirmação é…

O que se faz numa prova de lógica: procura o **comando** e o **conectivo**. O comando já achei — é a palavra "negação". O conectivo é o "e". Nada de ficar interpretando; isso é para quem não estudou. Quem estudou circula o "e", circula "negação" e mete a regra.

O "e" vira "ou", então só pode ser uma alternativa que tenha "ou".

Agora, cuidado com a segunda parte — a FGV gosta disso: a negação de "não paguei" é **"paguei"**.

Resultado: **"Eu não recebi o boleto ou paguei."** — letra E.

A regra usada foi $\neg(P \land Q) \equiv \neg P \lor \neg Q$, a Lei de Morgan.

### Questão 2 — Negação de Condicional

> (FGV, 2018) A negação lógica de "Se como demais, então passo mal".

Marquei a palavra "negação". E aqui vem a grande dúvida dos meus alunos:

*"Wagner, agora é Inverte Negando ou é Mané?"*

`⏱ 12:20`

Calma. **Inverte Negando é quando pedem equivalência. Aqui está pedindo negação — então é Mané**, porque o conectivo é "se… então".

O que é Mané? Mantém a primeira, nega a segunda. Mantém a primeira: "Como demais". Nega a segunda: "e não passo mal".

Só pode ser a letra C — a única que começa mantendo a primeira: **"Como demais e não passo mal."**

Minha experiência é de mais de 20 anos dando aula de matemática e lógica para concursos e em pré-vestibulares. Trago as dúvidas, as inquietações e os conflitos dos alunos para cá.

### Questão 3 — Negação da Disjunção Exclusiva

> Dada a disjunção exclusiva: "**Ou** Carlos é advogado, **ou** Luísa é professora." Qual a negação?

É uma questão rara, mas a partir de 2018–2020 começou a aparecer forte.

Temos: "Carlos é advogado" = $P$; "Luísa é professora" = $Q$. O autor está pedindo a negação do "ou" exclusivo.

**O "se e somente se" nega com "ou", e o "ou" nega com "se e somente se".**

Então a resposta é: **"Carlos é advogado se e somente se Luísa é professora."** — letra C.

Encerramos as negações. Vamos às equivalências.

### Equivalências Lógicas

É novidade? Não — vocês já viram uma comigo, o Inverte Negando. O que eu quero agora é abrir as outras.

**Definição:** equivalência são duas proposições, duas frases, ditas de maneiras diferentes, mas que para a lógica têm o mesmo efeito. Ou, dito de outro jeito: **se eu construir a tabela verdade das duas, elas batem igual no final.**

Existem N equivalências; vou trazer as mais importantes.

**Dupla Negação**

$$\neg(\neg P) \equiv P$$

A negação da negação é a própria afirmação. "Não é verdade que o amor não é fiel" é o mesmo que "o amor é fiel".

`⏱ 16:20`

Outro exemplo. Em português, quando você diz "Amanhã não vai ter aula, não", você está reforçando a negação. Em lógica, não: **não com não é sim**. É aquele ditado — quem mente duas vezes fala a verdade.

### Leis Comutativas

Vocês já aprenderam comutatividade na escola, na adição: $3 + 5 = 5 + 3$. Também existe comutatividade na lógica:

$$P \land Q \equiv Q \land P \qquad P \lor Q \equiv Q \lor P$$

Onde isso aparece? Resolvi uma questão enorme e cheguei em "o cachorro late **e** a caneta é preta". Não encontrei essa alternativa para marcar — mas a letra D trazia "a caneta é preta **e** o cachorro late". Pode marcar a letra D.

### Negação é um tipo de equivalência (e por que eu separo)

Prestem atenção agora, porque este assunto é o mais importante do vídeo.

Vejam as Leis de Morgan de novo:

$$\neg(P \lor Q) \equiv \neg P \land \neg Q \qquad \neg(P \land Q) \equiv \neg P \lor \neg Q$$

*"Você não estava falando de equivalência? Por que voltou para a negação?"*

Chegamos no ponto. **Tecnicamente, a negação é um braço da equivalência — é um tipo de equivalência.** Quando comecei a dar aula para concurso, lá no começo dos anos 2000 em Salvador, eu ensinava assim: bonito, teoria correta, reproduzindo o que aprendi na faculdade de matemática. Só que os alunos não acertavam questão, porque misturava tudo.

Aí eu resolvi "enganar" meus alunos para o bem: **negação é uma coisa, equivalência é outra.** É mentira do ponto de vista formal, mas é o que faz acertar prova.

**Como saber qual usar? Pelo comando.** O enunciado vai pedir "negação" ou vai pedir "equivalência".

`⏱ 20:00`

### Inverte Negando: as equivalências mais cobradas

Das equivalências, duas são as que mais caem — e há uma terceira, do bicondicional, menos frequente. Coloquem estas duas no caderno.

A primeira vocês já conhecem: **Inverte Negando** (a contrapositiva).

$$P \to Q \equiv \neg Q \to \neg P$$

Inverte a ordem e nega as duas. Essa não cai em concurso — **despenca**.

### A segunda equivalência

A outra que cai demais é esta:

$$P \to Q \equiv \neg P \lor Q$$

Deixa eu mostrar de onde ela vem, por transitividade. Já sabemos que $\neg(P \to Q) \equiv P \land \neg Q$. Negando os dois lados e aplicando Morgan em $\neg(P \land \neg Q)$, chega-se em $\neg P \lor Q$. Se $A \equiv B$ e $B \equiv C$, então $A \equiv C$.

Se Inverte Negando cai em 70% das questões de equivalência, os outros 30% são esta.

### Macete para memorizar

Vai ter macete, sim. Para lembrar de $\neg P \lor Q$, eu decoro como **"não pode ver queijo"**:

- **"não pô"** → $\neg P$
- **"ver"** → o "ou" ($\lor$)
- **"queijo"** → $Q$

### As duas que caem

Em termos de equivalência para concurso, são estas duas:

1. **Inverte Negando** — $P \to Q \equiv \neg Q \to \neg P$
2. **Não pode ver queijo** — $P \to Q \equiv \neg P \lor Q$

Vamos fazer duas questões.

`⏱ 24:00`

### Questão 4 — do "ou" para o "se… então"

> "Pedro não é pedreiro **ou** Paulo é paulista." Do ponto de vista lógico, isso é o mesmo que dizer que…

Quem não estudou fica viajando. Quem estudou faz o seguinte: **"o mesmo que dizer" significa equivalência.**

Qual das duas usar? Olhe o conectivo do meio: é **"ou"**. Portanto é "não pode ver queijo" — é a única das duas que tem "ou" no meio. Inverte Negando está descartada por isso.

Queremos sair do lado $\neg P \lor Q$ e ir para o lado $P \to Q$:

- O primeiro termo é o $\neg P$: "Pedro não é pedreiro". Logo $P$ = "Pedro é pedreiro".
- O segundo termo é $Q$: "Paulo é paulista".

Escrevendo como "Se $P$, então $Q$": **"Se Pedro é pedreiro, então Paulo é paulista."** — letra A.

### Questão 5 — do "se… então" para o "ou"

> "Se o aluno se formou, então conseguiu um emprego." Qual a equivalente?

Agora é o caminho contrário. Eu costumo tentar primeiro o Inverte Negando, que é a que mais cai — mas aqui o resultado dela não aparece nas alternativas. Então é a segunda, a do queijo:

$$P \to Q \equiv \neg P \lor Q$$

$\neg P$ = "o aluno não se formou". Resposta: **"O aluno não se formou ou conseguiu emprego."** — letra C.

`⏱ 28:00`

Uma das minhas filosofias é não fazer vídeo muito longo — no máximo 23, 24, 25 minutos. Este extrapolou um pouco por causa da complexidade do assunto.

### Questão 6 — equivalência com negação dentro

> Considere a sentença: "Se nasci em Rondônia **ou** Roraima, então sou brasileiro." Assinale a opção que apresenta uma sentença equivalente.

Vamos pelo clássico, o Inverte Negando. Esta questão é um pouco mais complicada porque tem uma coisa a mais dentro.

Temos: "nasci em Rondônia" = $P$; "nasci em Roraima" = $Q$; "sou brasileiro" = $R$. A sentença é $(P \lor Q) \to R$.

Aplicando Inverte Negando, o $R$ vem para a frente negado, e o parêntese vai para o outro lado negado:

$$(P \lor Q) \to R \;\equiv\; \neg R \to \neg(P \lor Q)$$

E aí entra a Lei de Morgan dentro da equivalência: $\neg(P \lor Q) \equiv \neg P \land \neg Q$. Fica:

$$\neg R \to (\neg P \land \neg Q)$$

Ou seja: **"Se não sou brasileiro, então não nasci em Rondônia nem em Roraima."** — letra D.

Essa questão é boa justamente porque tem uma equivalência **e** uma negação dentro. E note: a palavra "nem", em lógica, significa "e não".

## Relacionado

- [[logica-proposicional-3-conectivos-parte-2]]
- [[logica-proposicional-1-proposicoes-e-tabela-verdade]]
- [[logica-proposicional-4-questoes-de-concurso]]

---

## Revisão da transcrição

> Nota revisada à mão em 17/08/2026. O que segue é o registro do que foi
> alterado em relação à saída do pipeline — a regra do projeto é que correção
> feita em silêncio é correção em que não dá para confiar.

**Conteúdo devolvido ao corpo.** O filtro de ruído descartou um trecho de ~90
palavras que continha a explicação de **por que as leis se chamam Leis de
Morgan**. O trecho vinha sem pontuação nenhuma e continha a expressão "esse
nosso canal", que casa com a regra `(meu|nosso) canal` — como não havia ponto
final, o filtro tratou as 90 palavras como uma frase só e levou a explicação
junto. Devolvida ao §"Negação das Operações Lógicas".

**Destaques refeitos.** O pipeline gerou quatro, e um deles estava **errado**:

- ~~"A negação de P ou Q é P e Q"~~ → o correto é $\neg P \land \neg Q$. Do jeito
  que estava, era uma Lei de Morgan sem as negações — decorar aquilo custaria a
  questão na prova.
- ~~"Inverte Negando é uma fórmula de equivalência"~~ e ~~"Não pode ver queijo é
  outra fórmula de equivalência"~~ nomeavam os macetes sem dizer as fórmulas, que
  é justamente o que se precisa lembrar.

**Bloco `04:20` reescrito.** Saiu do pipeline em texto cru, sem pontuação — o
guarda anti-resumo rejeitou a reescrita do modelo e manteve o original, que é o
comportamento certo, mas deixa o bloco ilegível.

**Erros de transcrição corrigidos** (o áudio sustenta a correção):

| estava | virou | por quê |
|---|---|---|
| "negação do **i**" | "negação do **e**" | o Whisper ouve o conectivo "e" falado como "i" — é o §6.6 dos docs, ainda aberto |
| "Eu recebi o boleto e não recebi o boleto" | "Eu não recebi o boleto ou paguei" | a própria aula dá a resposta (letra E) duas linhas depois |
| "cheguei na letra R" | "letra E" | idem |
| "O conectivo já achei. É a palavra negação" | comando ≠ conectivo | a aula separa os dois no parágrafo seguinte |
| "Luiz é professora" | "Luísa é professora" | o nome aparece nas duas formas; a segunda é a usada na resolução |
| "Ou você usa o ou" (bicondicional) | "ou exclusivo" | a aula explica pela tabela verdade logo depois |

**Trechos que a transcrição perdeu e que eu não reconstruí** — porque não dá
para sustentar pelo áudio:

- **O macete "Vera Fischer".** A aula usa a atriz como gancho de memória para
  $\neg P \lor Q$, mas o trecho ("ela é famosa, ela é sem noção e ela também
  não pode… o V tem a letra V e tem o queijo") saiu embaralhado. Mantive só a
  parte que se sustenta — "não pode ver queijo" mapeando $\neg P$, $\lor$, $Q$.
- **"Com a base 44, uma simples frase se transforma em…"** — provavelmente um
  número de slide ou "com base nisso". Removido por ser ruído puro.
- **Uma leitura de patrocínio** ("se você assinou o seu chat EPT pelo Google")
  passou pelo filtro de ruído e foi removida à mão.

**Também retirado:** o wikilink `[[cronograma-coren-sp-90-dias-v2 (3)]]`, que
entrou em "Relacionado" como quarto vizinho por borda de corte (§6.7 dos docs) —
um cronograma de estudos não é assunto irmão de uma aula de lógica.
