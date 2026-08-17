---
titulo: "Lógica Proposicional 3 — Conectivos, Parte 2"
tags: [logica-proposicional, conectivos, condicional, bicondicional, equivalencia-logica]
data: 2026-08-17
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 23
conceitos: [Condicional, Bicondicional, Contrapositiva, Equivalência lógica, Condição suficiente e necessária]
---

# Lógica Proposicional 3 — Conectivos, Parte 2

> [!resumo] Do que se trata
> Parte 2 dos conectivos: o condicional (`→`) em quatro casos — contrapositiva, tabela verdade, suficiente/necessário e distratores — e o bicondicional (`↔`). Traz os macetes "inverte negando", "Vera Fischer" e "sem noção".

## Para lembrar

- **Condicional `P → Q`: só é falso em `V → F` (macete "Vera Fischer é Famosa").**
- **A única equivalência do condicional é a contrapositiva: `P → Q` ≡ `¬Q → ¬P` (macete "inverte negando").**
- **A recíproca `Q → P` e a inversa `¬P → ¬Q` NÃO são equivalentes — é o erro que a banca cobra.**
- **Em `P → Q`, o P é a condição suficiente e o Q é a necessária (macete "sem noção"). "P somente se Q" é `P → Q`.**
- **Bicondicional `P ↔ Q`: verdadeiro só quando os dois lados são iguais. Aceita as quatro conclusões, negando os dois lados ou nenhum.**

## O que esta nota responde

- Qual é a única equivalência válida do condicional, e por que a recíproca não vale?
- Quando o condicional dá falso?
- Como reconhecer um condicional escondido em "quando", "quem", "logo", "pois" ou "somente se"?
- O que muda quando a questão diz "necessária **e** suficiente"?

## Conceitos

**Condicional** · **Bicondicional** · **Contrapositiva** · **Equivalência lógica** · **Condição suficiente e necessária**

## Conteúdo

`⏱ 00:00`

Quem está assistindo o vídeo pela primeira vez, sugiro que não comece por ele. Este é o terceiro vídeo de lógica proposicional. Assim como na matemática, as coisas têm um encadeamento que vai organizando o pensamento. Ou seja, se você deixar de assistir um ou outro, vai acabar afetando o aprendizado. Vamos começar!

### Lógica Proposicional: Conectivos

Estamos em Lógica Proposicional, a famosa "P e Q", conectivos parte 2 — na verdade o terceiro vídeo. No vídeo passado, falamos sobre quatro conectivos:

- Negação (`¬`)
- Conjunção (`∧`)
- Disjunção (`∨`)
- Disjunção exclusiva (`⊻`)

### O Conectivo Condicional

Hoje, eu trago o conectivo de número 5, que é o conectivo mais importante de todos.

Por que ele é o mais importante? Não existe uma hierarquia dentro do estudo da lógica. Ele é mais importante porque é o que mais aparece em concursos e em alguns vestibulares. Os vestibulares aqui da Bahia, feitos pela Consultec, e as provas da UNEB, por exemplo, trazem esse assunto. O condicional é o conectivo que mais aparece.

#### O que é o Condicional?

Na vida real, quando você diz:

- "Se amanhã fizer sol, eu acho que vou pegar uma praia";
- "Caso eu me atrase, ligue para a minha secretária";
- "Quando eu estou com sede, eu bebo cerveja gelada".

Todas essas frases são frases que estão no formato de uma condicional: se uma coisa acontecer, outra vai acontecer. Este é o nosso quinto conectivo: o condicional, que é chamado de "se então".

#### Representação e Leitura

A representação do "se então" é esta: `P → Q`.

Observem o detalhe: essa seta só é legítima **para a direita**. Eu vou colocar aqui duas palavras que me preocupam: **implica** e **consequentemente**. Se vocês virem essas palavrinhas numa prova de lógica, vocês têm que saber que o assunto é condicional.

Exemplo: "Estudar com o Vaguinho implica aprender matemática." Isso quer dizer que, se eu estudo com o Vaguinho, aprendo matemática.

A ideia central desse assunto é: Se `P` acontece, se o ponto está dentro da bola `P`, consequentemente estará dentro da bola `Q`. Essa é a ideia desse assunto.

#### Estrutura do Assunto

Para dar aula desse assunto, há alguns anos eu venho dividindo esse assunto em quatro casos. Diferentemente dos outros conectivos, por ser mais complexo, eu explico ele dividido em quatro momentos. Os casos são as maneiras pelas quais você pode ser cobrado em prova sobre esse assunto.

Eu quero bem delimitar com vocês: você pode ser cobrado desta maneira, ou desta, ou desta. São os quatro casos, e eles organizam o resto desta nota:

1. **Equivalência** — a contrapositiva ("inverte negando");
2. **Tabela verdade** — o macete da Vera Fischer;
3. **Suficiente e necessário** — o macete "sem noção", e o "somente se";
4. **Distratores** — as palavras que escondem um condicional.

Eu vou começar pelo caso um.

*Observação importante:* Não é só essa equivalência que existe na lógica. No nosso vídeo de número 4, eu vou voltar a esse assunto. Eu vou abranger, eu vou trazer mais equivalências. Na verdade, estou devendo duas coisas para vocês: aprofundar negação e aprofundar esse assunto, equivalência. E eu farei isso no nosso vídeo de número 4 de lógica proposicional.

### Exemplo Prático e Regras Lógicas

O seguinte, se liga no exemplo e vai acompanhando o meu raciocínio, que vai ficar tudo massa até o final. Eu vou pegar uma frase da nossa vida real para ficar mais fácil de entender. Mas na prova não vai ter frase de vida real; na prova vai ter uma maluquice.

Por exemplo: "Se a cadeira é um `NFL` bata, então o cronôpio é verde." Vai ter que aplicar regra, entendeu?

Vamos usar a frase: "Se Ivete é baiana, então ela é brasileira."

Eu vou fazer algumas provocações para vocês.

**O que NÃO é equivalente — 1: a recíproca (`Q → P`)**

Nossa frase é `P → Q`: "Se Ivete é baiana, então ela é brasileira."

Eu posso dizer que "se Ivete é brasileira, então ela é baiana"? Usando o português, faz sentido? Não — ela pode ser brasileira tendo nascido em outro estado, concordam? Mas vamos para a teoria, que é mais seguro: nos conjuntos, o ponto pode estar dentro de `Q` sem estar dentro de `P`.

Essa estrutura, `Q → P`, é chamada de **recíproca**.

> `P → Q` **não** equivale a `Q → P`

Sabe quando você fala "foi um prazer conhecer" e a pessoa responde "a recíproca é verdadeira"? Na lógica, **a recíproca nem sempre é verdadeira**. Essa é uma estrutura que vocês estão proibidos de marcar em prova: não se pode simplesmente virar a frase.

**O que NÃO é equivalente — 2: a inversa (`¬P → ¬Q`)**

"Se Ivete **não** é baiana, então ela **não** é brasileira"? Vamos ver: se Ivete não é baiana, ela ainda pode ser brasileira tendo nascido em Manaus, sei lá, em outro lugar. Então isso aqui também é proibido.

> `P → Q` **não** equivale a `¬P → ¬Q`

`⏱ 08:20`

Chega de proibido. Vamos falar da coisa certa agora, do que você **vai** marcar na sua prova.

**O que É equivalente: a contrapositiva (`¬Q → ¬P`)**

"Se Ivete é baiana, então Ivete é brasileira." Fechou? Eu posso dizer que isso é igual a: "Se Ivete **não** é brasileira, então ela **não** é baiana."

Faz sentido: se ela não é brasileira, se está fora do mapa do Brasil, então ela está fora da Bahia. Claro que sim. Nos conjuntos: se o ponto está fora de `Q`, consequentemente ele está fora de `P`. **Isso aqui é a coisa mais importante do vídeo de hoje.**

> `P → Q` **equivale a** `¬Q → ¬P`

### O Conceito de Equivalência Lógica

Essa equivalência cai demais em concurso. Equivalência são **duas proposições que têm o mesmo valor lógico**. Se eu tivesse muito tempo, eu faria uma tabela verdade para o lado esquerdo e uma para o lado direito, e vocês veriam que dá o mesmo valor lógico no final — daí a gente bate o martelo e diz que são equivalentes.

Essa equivalência é chamada de **contrapositiva**, e eu inventei um macete para vocês decorarem: **inverte negando**.

*   **Inverte:** porque eu troquei o `P` e o `Q` de lugar.
*   **Negando:** porque os dois ficaram com "não".

Quando eu perguntar qual foi a equivalência que vocês aprenderam com o Vaguinho, é essa: **inverte negando**.

### Aplicando a Contrapositiva (Inverte Negando)

Vou fazer um exemplo no próximo slide para deixar isso claro.

**Prova FGV 2017:**

Atenção. Considere a sentença: "Se Juvenal foi trabalhar, então Alva não saiu de casa." É correto concluir que...?

Ele precisa aprender a fazer uma prova de lógica. É assim que faz prova de lógica.

"Juvenal foi trabalhar" — eu vou chamar de `P`, e não vou ficar pensando em Juvenal nem em trabalho; esquece, minha preocupação é a forma. Eu marco o **então** aqui. "Alva não saiu de casa" — apesar de ter o "não", você pode chamar de `Q`.

Então, qual é a forma dessa questão? `P → Q`. Esquece o texto, se liga na forma. O conectivo é o "se… então", achei o conectivo — toda prova de lógica tem um conectivo e tem um **comando**. O comando aqui é a expressão **"é correto concluir"**, que se lê como **"equivale"**. Toda vez que tiver "é correto concluir", é igual a "equivale".

E aí você vai aplicar a contrapositiva, que a gente chama de **inverte negando**. (Vaguinho, só existe essa equivalência? Não — tem outras, que eu vejo no próximo vídeo.)

Vamos lá, inverte negando. É só começar do final: o que eu tenho no final? "Alva não saiu de casa". Joga isso para o início, só que **negando**. Qual é a negação de "Alva não saiu de casa"? "Alva saiu de casa".

Vamos ser espertos: só tem uma alternativa que começa desse jeito. "Se Alva saiu de casa, então…" — e agora joga o Juvenal para cá, negando: "…então Juvenal não foi trabalhar."

> `P → Q` ≡ `¬Q → ¬P`
> "Se Juvenal foi trabalhar, então Alva não saiu de casa"
> ≡ "Se Alva saiu de casa, então Juvenal não foi trabalhar"

### Caso 2 — A Tabela Verdade do Condicional

Só que ainda tem o caso 2, que é mais coisa sobre o condicional. Para decorar a tabela verdade, usamos o macete: **Vera Fischer é Famosa**.

O que eu quero dizer é que, nesse assunto, a gente decora **pela falsidade**. Para dar falso, tem que ser verdadeiro com falso — é o único jeito. **V** de Vera, **F** de Fischer, e o resultado **F**. Ou seja, só vai dar falso nesta linha: `V → F`. O resto é tudo verdade.

| P | Q | P → Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **V** |
| F | F | **V** |

Posso explicar rapidinho? Foca na segunda linha. Ela diz que está dentro do `P` e **não** está dentro do `Q` — e isso é impossível, se todo `P` está dentro de `Q`. Por isso é falso. Então o macete está decorado: Vera Fischer, a loira famosa. `V` com `F` dá `F`. Segura esse macete aí.

### Caso 3 — Suficiente e Necessário: o "Sem Noção"

Mas tem mais coisa ainda. Eu gosto tanto da Vera Fischer, ela é minha musa, que tem mais para falar sobre ela: além de famosa, ela é **Sem Noção** (`SN`). Claro que ela tem muita noção — é só a brincadeira do macete.

`S` e `N` são as iniciais que interessam aqui, e eu uso esse macete quando o concurso ou o vestibular cobra as **linguagens possíveis do condicional**.

#### Definições: Suficiente e Necessário

Eu não vou entrar na epistemologia das palavras — em concurso isso é cobrado na forma mais rasteira possível, então deixa eu ser direto. O `S` é de **Suficiente** e o `N` é de **Necessário**, e o que decide qual é qual é a **posição** na seta:

> `P → Q`
> `P` (à esquerda) é a condição **Suficiente**
> `Q` (à direita) é a condição **Necessária**

Vou dar um exemplo: "Se estudo com o Vaguinho (`P`), então aprendo matemática (`Q`)." Esta mesma frase pode vir de outras maneiras no concurso, e você tem que reconhecer pelas posições:

- "Estudar com o Vaguinho" está na posição do `P`, então é a condição **suficiente** para aprender matemática. Não vá além disso, porque no concurso não precisa: fica só na questão da posição.
- "Aprender matemática" está na posição do `Q`, então é a condição **necessária** para estudar com o Vaguinho.

Eu tenho ainda outra expressão que eu queria que vocês memorizassem, que é o **"somente se"**.

`⏱ 16:00`

O "somente se" é o próprio "se… então", na mesma ordem: "estudo com o Vaguinho **somente se** aprendo matemática" é o mesmo que "**se** estudo com o Vaguinho, **então** aprendo matemática".

> `P` somente se `Q` ≡ `P → Q`

É preciso decorar e memorizar, e o macete "**sem noção**" ajuda: `S` de Suficiente à esquerda, `N` de Necessário à direita.

### Caso 4 — Distratores em Concursos

Alguns concursos usam distratores. Um distrator é uma expressão feita para distrair o concureiro. Se você não tiver esse saque, terá dificuldade de resolver as provas. Quais são as expressões que devem ser transformadas em condicional?

*   "Quando acredito que estou certo, não me importo com a opinião dos outros."
    *   A palavra "quando" dá a ideia de condição. A frase deve ser reescrita: "Se acredito que estou certo, então não me importo com a opinião dos outros."
*   [inaudível: um exemplo sobre DNA e a influência do continente africano]
*   "Quem doa sangue doa vida."
    *   Se não se ligasse que a palavra "quem" significa "se", teria dificuldade. A frase é: "Se doa sangue, então doa vida."
*   "Penso, logo, existo."
    *   O "logo" também dá a ideia de "se... então". A frase é: "Se penso, então existo."

#### O caso especial: o "se" ou o "pois" no meio da frase

Este caso é diferente de todos os outros. Observe: "Vou ao mercado, **se** preciso comprar frutas." O "se" no meio já complica um pouco.

A regra: quando o "se" ou o "pois" está **no meio** da frase, ela tem que ser reescrita **do final para o início**.

Exemplo: "Vou ao mercado, **pois** preciso comprar frutas." Fica assim:

> "**Se** preciso comprar frutas, **então** vou ao mercado."

Falei dos quatro casos da condicional. Guardem esses quatro casos, porque eles ajudam muito quando for partir para os exercícios.

### O Conectivo Bicondicional

Fechamos o bloco falando do nosso sexto conectivo, o **bicondicional**. É muito fácil: o "bi" significa condicional **dobrada**. A condicional só aceita ir para a direita; a bicondicional vai para os dois lados — é a seta **dupla**, `↔`.

O que significa `P ↔ Q` ("P se e somente se Q")? Se `P` acontece, `Q` acontece; **e** se `Q` acontece, `P` também acontece. Nos conjuntos, seriam dois conjuntos **coincidentes**: `P` e `Q` são o mesmo conjunto.

### Tabela Verdade do Bicondicional

Para ser verdade, os dois lados devem ser **iguais** — não pode ser verdade num e falso no outro, porque o conjunto tem que ser o mesmo. Então só é verdade na primeira e na última linha: **ou `V` com `V`, ou `F` com `F`**.

| P | Q | P ↔ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **F** |
| F | F | **V** |

A palavra-chave aqui é **"iguais"**.

### Bicondicional na Prática

Para encerrar, quero trazer esta frase para discutir: "Você lavar o carro é a condição **necessária e suficiente** para eu emprestar o carro para você."

Observe que não tem só "necessária" ou só "suficiente", como no caso 3. Tem os **dois** adjetivos — e é isso que denuncia o bicondicional. A outra forma de dizer a mesma coisa é: "Você lava o carro **se e somente se** eu emprestar para você."

Essas duas frases são bicondicional: uma porque traz necessária **e** suficiente, a outra porque traz os dois "se", como se fossem as duas setinhas. Fique ligado nessa linguagem.

As conclusões que podem ser tiradas são **todas as quatro**:

- Se você lavar, eu te empresto. → `P → Q`
- Se você não lavar, eu não te empresto. → `¬P → ¬Q`
- Se eu te emprestar, você lava. → `Q → P`
- Se eu não te emprestar, você não lava. → `¬Q → ¬P`

Nesse assunto pode tudo. Só não pode negar um e não negar o outro: **ou nega todo mundo, ou não nega ninguém.**

### Conclusão

Acabamos os conectivos, fechamos os seis conectivos. Estamos prontos para resolver questões agora. Vão estudar um pouco, refletir sobre essas aulas. Ter um caderno organizado é muito importante.

## Relacionado

- [[logica-proposicional-2-conectivos-parte-1]]
- [[logica-proposicional-4-questoes-de-concurso]]
- [[logica-proposicional-1-proposicoes-e-tabela-verdade]]

---

## Revisão da transcrição

> [!nota] O conteúdo desta nota foi conferido e corrigido à mão
>
> **O erro que mais importava:** na tabela verdade do bicondicional, o texto
> dizia *"para ser verdade, os dois lados devem ser **verdadeiros**"*. Está
> errado — `F ↔ F` também é verdade. A regra é os dois lados serem **iguais**, e
> a própria aula corrige isso duas linhas depois ("ou V com V ou F com F").
> Corrigido, e a tabela foi desenhada.
>
> | o Whisper ouviu | é |
> |---|---|
> | "a famosa **PIQ**" | "a famosa **P e Q**" (o apelido do assunto, do vídeo 1) |
> | `$ p\rightarrow q$` (LaTeX cru) | `P → Q` |
> | "**Consulteca**, o **Neb**" | "**Consultec**" e "**UNEB**" |
> | "Se **Sivete** é baiana", "Se **Vete** não é" | "Se **Ivete**…" |
> | "**Vera Ficha** é Famosa" | "**Vera Fischer** é Famosa" — o macete `V → F = F` |
> | "eu troquei aqui **P-I-K-I-P**" | "troquei o `P` e o `Q` de lugar" |
> | "com o **vaguninho**" / "**vaguinha**" | "com o **Vaguinho**" |
> | "**IN** significa Necessário" | "**N** significa Necessário" |
> | "ou nega todo mundo, **eu** não nego ninguém" | "**ou** não nego ninguém" |
> | "concurso **investidural**" | "concurso" |
>
> **Reconstruído:** a seção da equivalência estava com as três estruturas
> (recíproca, inversa e contrapositiva) descritas em frases quebradas e sem nome
> — e é justo a distinção que a banca cobra. Ficaram nomeadas e separadas, com a
> fórmula de cada uma e o que é permitido marcar em prova.
>
> Os **quatro casos** do condicional, que a aula anuncia e depois não numera,
> foram numerados nos subtítulos.
>
> **Acrescentado:** as tabelas verdade do condicional e do bicondicional, e a
> forma `P` somente se `Q` ≡ `P → Q`, que a aula explica em voz alta.
>
> **Removido:** o pedido de direct no Instagram para receber o resumo em PDF. O
> filtro não pegava "me chamem no Instagram" — passou a pegar.
>
> Onde não deu para recuperar, ficou `[inaudível]`: um dos exemplos de distrator,
> sobre DNA e a influência do continente africano.

<details><summary>8 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Se quiser o resumo, me chamem no Instagram. No direct, vocês me pedem, e eu mando o resumo.
- Olá!
- Meu compromisso é descomplicar a matemática e o raciocínio lógico, trazendo conteúdos de forma objetiva.
- Seja em pré-vestibular, seja para concurso público, ou nos meus cursos online, o foco é sempre em uma matemática direta, objetiva e voltada para as provas de concurso, do ENEM e de vestibulares.
- O próximo vídeo que eu voltar será para trazer questões sobre os conectivos.
- Um beijo grande e um abraço.
- Desejo essa aprovação, seja no vestibular, no ENEM, no concurso.
- Tchau!

</details>
