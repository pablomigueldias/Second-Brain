---
tags:
  - machine-learning
  - algoritmos
  - árvores-de-decisão
  - entropia
  - cálculos
  - supervisionado
---

# 7. Cálculos das Árvores de Decisão

> [!info] O que esta nota cobre
> O **passo a passo matemático** de como uma árvore de decisão escolhe as divisões. Vamos calcular a **Entropia** e o **Ganho de Informação (Information Gain)** e usar essas medidas para **construir uma árvore do zero**, nó por nó.

> [!tip] Este é o conteúdo "opcional/avançado"
> No curso, esta parte é marcada como opcional. Mas entender estes cálculos faz você compreender **de verdade** por que a árvore escolhe um atributo e não outro. Pré-requisito: [[06 - Árvores de Decisão]].

---

## 7.1. O Dataset (de novo o "jogar ou não")

| outlook | temperature | humidity | windy | play |
|---|---|---|---|---|
| sunny | hot | high | FALSE | no |
| sunny | hot | high | TRUE | no |
| overcast | hot | high | FALSE | yes |
| rainy | mild | high | FALSE | yes |
| rainy | cool | normal | FALSE | yes |
| rainy | cool | normal | TRUE | no |
| overcast | cool | normal | TRUE | yes |
| sunny | mild | high | FALSE | no |
| sunny | cool | normal | FALSE | yes |
| rainy | mild | normal | FALSE | yes |
| sunny | mild | normal | TRUE | yes |
| overcast | mild | high | TRUE | yes |
| overcast | hot | normal | FALSE | yes |
| rainy | mild | high | TRUE | no |

**14 instâncias: 9 "yes", 5 "no".**

> [!question] A pergunta-chave da construção
> Temos **4 atributos candidatos** a nó raiz: `outlook`, `temperature`, `humidity`, `windy`. **Qual escolher?**
>
> **Resposta:** o que tiver o **maior Ganho de Informação**!

---

## 7.2. Entropia

> [!note] Definição
> A **Entropia** vem da **Teoria da Informação**. Ela mede a **"desordem"** ou **impureza** de um conjunto.

### Fórmula

$$
E(S) = -\sum_{i} p_i \cdot \log_2(p_i)
$$

Onde $p_i$ é a proporção de cada classe no conjunto S.

### Os dois casos extremos

> [!important] Limites da entropia
> - Se **todas as instâncias** de S pertencem à **mesma classe** → **E(S) = 0** (conjunto puro, sem desordem).
> - Se S contém o **mesmo número** de instâncias de cada classe → **E(S) = 1** (máxima desordem).

```
   E = 0 (puro)        E = 1 (máxima desordem)
   ●●●●●●●●            ●●●●○○○○
   tudo igual          metade/metade
```

> [!tip] Intuição
> Entropia baixa = "já sei a resposta". Entropia alta = "está tudo misturado, não dá pra prever". A árvore quer **reduzir a entropia** a cada divisão.

---

## 7.3. Calculando a Entropia da Classe

Primeiro, a entropia do conjunto inteiro (a classe `play`): 9 "yes" e 5 "no" em 14.

$$
E(\text{classe}) = -\frac{9}{14}\log_2\frac{9}{14} - \frac{5}{14}\log_2\frac{5}{14} \approx \mathbf{0{,}94}
$$

> [!summary] Resultado
> A entropia da classe é **0,94** — alta (perto de 1), porque os dados estão bem misturados. Esse é o ponto de partida: queremos divisões que **baixem** esse 0,94.

---

## 7.4. Calculando a Entropia de Cada Atributo

Agora calculamos a entropia **de cada valor** de cada atributo. Vou mostrar os resultados:

### Atributo `outlook`

| Valor | Distribuição (yes/no) | Entropia |
|---|---|---|
| sunny | 2 yes, 3 no | **0,97** |
| overcast | 4 yes, 0 no | **0** (puro!) |
| rainy | 3 yes, 2 no | **0,97** |

> Repare: `overcast` tem entropia **0** — sempre que está nublado, joga-se. É um valor "puro"!

### Atributo `temperature`

| Valor | Distribuição | Entropia |
|---|---|---|
| hot | 2 yes, 2 no | **1** (máxima desordem) |
| mild | 4 yes, 2 no | **0,91** |
| cool | 3 yes, 1 no | **0,81** |

### Atributo `humidity`

| Valor | Distribuição | Entropia |
|---|---|---|
| high | 3 yes, 4 no | **0,98** |
| normal | 6 yes, 1 no | **0,59** |

### Atributo `windy`

| Valor | Distribuição | Entropia |
|---|---|---|
| TRUE | 3 yes, 3 no | **1** (máxima desordem) |
| FALSE | 6 yes, 2 no | **0,81** |

---

## 7.5. Ganho de Informação (Information Gain)

> [!note] Definição
> O **Ganho de Informação (IG)** mede **quanto a entropia diminui** ao dividir por um atributo. Quanto **maior o ganho**, **melhor** o atributo para dividir.

### Fórmula

$$
IG(S, A) = E(S) - \sum_{v} \frac{|S_v|}{|S|} \cdot E(S_v)
$$

Em palavras: **entropia original** menos a **média ponderada** das entropias dos pedaços resultantes da divisão.

> [!tip] Intuição
> "Quanto de desordem eu **eliminei** ao usar esse atributo?" O atributo que elimina mais desordem é o escolhido.

---

## 7.6. Calculando o IG de Cada Atributo

A entropia da classe é **0,94**. Vamos calcular o ganho de cada candidato:

### `outlook`
$$
IG = 0{,}94 - \left(\tfrac{5}{14}\cdot 0{,}97 + \tfrac{4}{14}\cdot 0 + \tfrac{5}{14}\cdot 0{,}97\right) = \mathbf{0{,}2471}
$$

### `temperature`
$$
IG = 0{,}94 - \left(\tfrac{4}{14}\cdot 1 + \tfrac{6}{14}\cdot 0{,}91 + \tfrac{4}{14}\cdot 0{,}81\right) = \mathbf{0{,}0328}
$$

### `humidity`
$$
IG = 0{,}94 - \left(\tfrac{7}{14}\cdot 0{,}98 + \tfrac{7}{14}\cdot 0{,}59\right) = \mathbf{0{,}16}
$$

### `windy`
$$
IG = 0{,}94 - \left(\tfrac{6}{14}\cdot 1 + \tfrac{8}{14}\cdot 0{,}81\right) = \mathbf{0{,}048}
$$

### Comparação

| Atributo | Ganho de Informação |
|---|---|
| **`outlook`** | **0,2471** ← maior! 🏆 |
| `humidity` | 0,16 |
| `windy` | 0,048 |
| `temperature` | 0,0328 |

> [!summary] Decisão
> **`outlook` vence** — tem o maior ganho de informação. Ele será o **nó raiz** da árvore.

---

## 7.7. Construindo a Árvore

### Primeiro nó (raiz): `outlook`

```
              [ outlook ]
             ╱     │     ╲
        sunny   overcast   rainy
          ?      ( yes )     ?
```

> [!note] O ramo `overcast` já terminou!
> Lembra que `overcast` tinha **entropia 0**? Todas as 4 instâncias `overcast` são "yes". Então esse ramo já é uma **folha pura**: `overcast → yes`. ✅
>
> Os ramos `sunny` e `rainy` ainda estão "misturados" — precisam de mais divisões.

---

### Particionando o ramo `sunny`

Agora olhamos **só** as instâncias `sunny`: são 5 (2 yes, 3 no). A entropia desse subconjunto é **0,97**.

Recalculamos o IG **dentro do ramo sunny**, para os atributos restantes:

| Atributo | IG (dentro de `sunny`) |
|---|---|
| **`humidity`** | **0,97** ← maior! 🏆 |
| `temperature` | 0,57 |
| `windy` | 0,024 |

> [!summary] Decisão
> Dentro do ramo `sunny`, **`humidity` vence** com IG = 0,97 (o máximo possível!).
>
> E mais: ao dividir `sunny` por `humidity`, **os dois ramos ficam puros**:
> - `sunny + high` → **no** (entropia 0)
> - `sunny + normal` → **yes** (entropia 0)

```
              [ outlook ]
             ╱     │     ╲
        sunny   overcast   rainy
          │       ( yes )    ?
     [ humidity ]
       ╱      ╲
     high    normal
     (no)    (yes)
```

---

### Particionando o ramo `rainy`

Mesmo processo no ramo `rainy`. Os cálculos do material indicam que **`windy`** é o melhor atributo para dividir esse ramo, e ele também resulta em **folhas puras**:
- `rainy + windy=FALSE` → **yes**
- `rainy + windy=TRUE` → **no**

---

## 7.8. A Árvore Final

```
                     [ outlook ]
                  ╱       │        ╲
             sunny     overcast      rainy
               │         │             │
        [ humidity ]   ( yes )      [ windy ]
          ╱      ╲                   ╱      ╲
        high    normal            FALSE     TRUE
         │        │                 │        │
       (no)    (yes)              (yes)     (no)
```

> [!success] Pronto!
> A árvore está completa — **todas as folhas são puras**. Foi construída escolhendo, a cada passo, o atributo com **maior Ganho de Informação**.

---

## 7.9. O Algoritmo em Resumo

```
   CONSTRUIR_ÁRVORE(dados):
        │
        ├─ 1. Calcular a entropia da classe
        │
        ├─ 2. Para cada atributo, calcular o Ganho de Informação
        │
        ├─ 3. Escolher o atributo com MAIOR ganho → vira o nó
        │
        ├─ 4. Para cada ramo gerado:
        │       • Se o ramo é puro (entropia 0) → vira FOLHA
        │       • Se não → repetir o processo nesse ramo (recursão)
        │
        └─ 5. Parar quando todos os ramos forem folhas
              (ou atingir uma condição de parada)
```

> [!tip] Esse é o algoritmo ID3
> Esse método de construir árvore usando Entropia + Ganho de Informação é a base do clássico algoritmo **ID3** (e seu sucessor, o **C4.5**).

---

## 7.10. Resumo

> [!summary] O essencial dos cálculos
> - **Entropia** = mede desordem. 0 = puro, 1 = totalmente misturado.
> - **Ganho de Informação** = quanto de entropia uma divisão **elimina**.
> - A cada nó, escolhe-se o atributo com **maior ganho de informação**.
> - Ramos com **entropia 0** viram **folhas** (resposta final).
> - O processo se **repete recursivamente** até a árvore terminar.

---

## 🔗 Próximos passos
- [[08 - Random Forest]] — e se, em vez de **uma** árvore, usássemos **várias** votando juntas?

---
[[00 - Índice|⬅️ Voltar ao Índice]]
