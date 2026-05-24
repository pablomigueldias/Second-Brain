---
tags:
  - machine-learning
  - tópicos-avançados
  - classificação
  - multilabel
  - métricas
---

# 8. Classificação Multilabel

> [!info] O que esta nota cobre
> A **Classificação Multilabel**: o caso em que uma instância pode ter **várias classes ao mesmo tempo**. Veremos a diferença entre binária, multiclasse e multilabel, as estratégias para resolver (Binary Relevance, Classifier Chains, Label Powerset) e as métricas próprias (Exact Match e Hamming Loss).

---

## 8.1. Relembrando: O que é Classificação

> [!note] Classificação
> **Classificação** é prever ou definir uma **classe**. A classe faz parte dos atributos do fenômeno (geralmente a última coluna).

> [!tip] Pré-requisito
> Os fundamentos de classificação estão em [[04 - Classificação]] e as métricas básicas em [[05 - Avaliação de Performance e Matriz de Confusão]] (módulo Fundamentos).

---

## 8.2. Os Três Tipos de Classificação

> [!important] A diferença central
>
> | Tipo | Quantas classes possíveis? | Quantas a instância recebe? |
> |---|---|---|
> | **Binária** | 2 | exatamente 1 |
> | **Multiclasse** | 3 ou mais | exatamente 1 |
> | **Multilabel** | 3 ou mais | **1 ou mais** (várias ao mesmo tempo) |

### Classificação Binária

> Só **2 classes** possíveis, e a instância é **uma OU outra**.
> **Exemplo:** Crédito → `Bom` **OU** `Mau`.

### Classificação Multiclasse

> **3+ classes** possíveis, mas a instância é **só uma** delas.
> **Exemplo:** Iris → `Versicolor` **OU** `Virginica` **OU** `Setosa`.

### Classificação Multilabel

> **3+ classes**, e a instância pode ter **VÁRIAS ao mesmo tempo** (relação "E", não "OU").
> **Exemplo:** uma música pode ser `Calma` **E** `Triste` **E** `Encantadora` — tudo junto.

```
   Binária:      ● ── Bom    OU    Mau

   Multiclasse:  ● ── Versicolor  OU  Virginica  OU  Setosa

   Multilabel:   ● ── Agitada E Alegre E Relaxante E Calma E ...
                       (qualquer combinação de várias)
```

---

## 8.3. Exemplo: Classificando Músicas

> [!example] O caso das músicas
> Imagine classificar músicas por **humor**. Os rótulos possíveis: `Agitada`, `Alegre`, `Relaxante`, `Calma`, `Triste`, `Encantadora`.
>
> Uma música **não é** só um humor — ela pode ser **Calma E Triste E Encantadora** ao mesmo tempo. Esse é um problema **multilabel** clássico.
>
> Comparando:
> - **Binária**: a música é `Calma` ou `Triste`.
> - **Multiclasse**: a música é `Calma` ou `Triste` ou `Encantadora`.
> - **Multilabel**: a música é `Calma` e/ou `Triste` e/ou `Encantadora`.

### Como ficam os dados

Num problema multilabel, em vez de **uma** coluna de classe, há **várias colunas binárias** (uma por rótulo):

| ... atributos ... | Agitada | Alegre | Relaxante | Calma | Triste | Encantadora |
|---|---|---|---|---|---|---|
| ... | 1 | 0 | 1 | 0 | 1 | 0 |
| ... | 0 | 1 | 0 | 1 | 0 | 1 |
| ... | 1 | 0 | 1 | 0 | 1 | 0 |

> Cada `1` indica que aquele rótulo **se aplica** à instância. Uma instância pode ter vários `1`s.

---

## 8.4. Estratégias para Resolver Multilabel

Há duas grandes abordagens: **adaptar o problema** ou **adaptar o algoritmo**.

```
   RESOLVER MULTILABEL
        │
        ├─ Transformação de Problema (adapta os DADOS ao classificador)
        │   ├─ Binary Relevance
        │   ├─ Classifier Chains
        │   └─ Label Powerset
        │
        └─ Algoritmos Adaptados (adapta o CLASSIFICADOR aos dados)
            ├─ Clare (C4.5)
            ├─ AdaBoost.MH
            └─ ML-kNN
```

> [!note] As duas filosofias
> - **Transformação de Problema** → os **dados são adaptados** ao classificador. Transforma o problema multilabel em vários problemas "normais".
> - **Algoritmos Adaptados** → o **classificador é adaptado** aos dados. Algoritmos modificados para entender multilabel diretamente (ex.: Clare, AdaBoost.MH, ML-kNN).

Vamos detalhar as três técnicas de **transformação de problema**.

---

### 8.4.1. Binary Relevance

> [!note] Como funciona
> Transforma o problema multilabel em **vários problemas de classificação binária independentes** — **um para cada rótulo**.

> [!example] No exemplo das músicas
> Cria-se um classificador separado para cada humor:
> - Classificador 1: "é Agitada? sim/não"
> - Classificador 2: "é Alegre? sim/não"
> - Classificador 3: "é Relaxante? sim/não"
> - ... e assim por diante.
>
> Cada um trabalha **isolado**, olhando só o seu rótulo.

> [!warning] Limitação do Binary Relevance
> Por tratar cada rótulo **independentemente**, ele **ignora as relações entre os rótulos**. Mas na prática há correlações (música "Triste" raramente é "Agitada"). O Binary Relevance perde essa informação.

---

### 8.4.2. Classifier Chains

> [!note] Como funciona
> Parecido com Binary Relevance, mas os classificadores formam uma **corrente (chain)**: a previsão de um rótulo **vira atributo de entrada** para o próximo classificador.

> [!example] No exemplo das músicas
> - Classificador 1: prevê `Agitada` usando os atributos.
> - Classificador 2: prevê `Alegre` usando os atributos **+ a previsão de Agitada**.
> - Classificador 3: prevê `Relaxante` usando os atributos **+ as previsões de Agitada e Alegre**.
> - ... e assim por diante, cada um herdando as previsões anteriores.

> [!tip] A vantagem sobre Binary Relevance
> Como cada classificador "vê" as previsões dos anteriores, o Classifier Chains **considera as relações entre os rótulos** — corrigindo a principal fraqueza do Binary Relevance.

---

### 8.4.3. Label Powerset

> [!note] Como funciona
> Transforma **cada combinação única de rótulos** em uma **classe própria**. O problema multilabel vira um problema **multiclasse**.

> [!example] No exemplo das músicas
> - A combinação `{Agitada, Relaxante, Triste}` vira a classe `C1`.
> - A combinação `{Alegre, Calma, Encantadora}` vira a classe `C2`.
> - E assim por diante — cada padrão de rótulos é uma classe.

> [!warning] Limitação do Label Powerset
> Se houver **muitas combinações possíveis** de rótulos, o número de classes **explode**. Com 6 rótulos, são até 2⁶ = 64 combinações possíveis. Funciona bem só quando as combinações observadas são **poucas**.

---

## 8.5. Métricas para Multilabel

> [!important] Por que métricas especiais?
> As métricas normais (acurácia, precisão...) não funcionam direto em multilabel. Numa previsão de 6 rótulos, o modelo pode acertar 5 e errar 1 — não é "certo" nem "errado", é **parcialmente certo**. Precisamos de métricas que lidem com isso.

### 8.5.1. Exact Match (Correspondência Exata)

> [!note] Definição
> **Exact Match** = a previsão só conta como **acerto** se **TODOS os rótulos** da instância estiverem corretos. Acertar 5 de 6 = erro total.

> [!example] Exemplo
> - Real: `[1, 0, 1, 1, 1, 0]` | Previsto: `[1, 0, 1, 1, 1, 0]` → ✅ **acerto** (idêntico).
> - Real: `[1, 0, 1, 1, 1, 0]` | Previsto: `[1, 0, 1, 1, 0, 0]` → ❌ **erro** (1 rótulo diferente).

> [!warning] Exact Match é severo
> É a métrica mais **rígida** — não dá "crédito parcial". Útil quando você precisa que **tudo** esteja certo, mas costuma dar valores baixos.

### 8.5.2. Hamming Loss

> [!note] Definição
> **Hamming Loss** = a **fração de erros em relação ao total de rótulos**. Em vez de "tudo ou nada", conta **quantos rótulos individuais** o modelo errou.

#### Hamming Distance

> [!note] Hamming Distance
> A **Hamming Distance** é a **quantidade de posições em que há uma diferença** entre a previsão e o real.

> [!example] Calculando a Hamming Distance
> - Real: `[1, 0, 1, 0, 1]` | Previsto: `[1, 0, 1, 0, 1]` → diferenças: **0**
> - Real: `[1, 1, 0, 1]` | Previsto: `[1, 1, 1, 1]` → diferenças: **2** (posições 3 e... conta as que diferem)
> - Real: `[1, 0, 0, 1]` | Previsto: `[1, 1, 0, 1]` → diferenças: **1**

#### Hamming Loss = fração de erros

$$
\text{Hamming Loss} = \frac{\text{total de rótulos errados}}{\text{total de rótulos}}
$$

> [!important] Interpretação do Hamming Loss
> - Valor vai de **0 a 1**.
> - **Quanto MENOR, melhor** (0 = sem nenhum erro de rótulo).
> - Diferente do Exact Match, ele **dá crédito parcial**: acertar 5 de 6 rótulos é melhor que acertar 3 de 6.

```
   Hamming Loss
   1 ┤
     │
     │      Melhor ↓
   0 ┤   ◀──────────────
     └─────────────────
   (menor = melhor)
```

### Exact Match vs. Hamming Loss

| | **Exact Match** | **Hamming Loss** |
|---|---|---|
| O que mede | Acertou **todos** os rótulos? | **Fração** de rótulos errados |
| Crédito parcial? | ❌ Não (tudo ou nada) | ✅ Sim |
| Melhor valor | **Alto** (1 = tudo certo) | **Baixo** (0 = nenhum erro) |
| Severidade | Muito rígido | Mais tolerante |

---

## 8.6. Exemplo em Python (notebook do curso)

O notebook `Multilabel.ipynb` usou **Classifier Chains** para classificar músicas:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import hamming_loss
from sklearn.multioutput import ClassifierChain
from sklearn.preprocessing import StandardScaler

musica = pd.read_csv("Musica.csv")

# As 6 primeiras colunas são os RÓTULOS (multilabel)
classe = musica.iloc[:, 0:6].values
# As demais colunas são os atributos
previsores = musica.iloc[:, 7:78].values

# Padronizar os atributos
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

X_tr, X_te, y_tr, y_te = train_test_split(previsores, classe,
                                          test_size=0.3, random_state=0)

# Classifier Chains usando um SVM como classificador base
svm = SVC()
classifier_chain = ClassifierChain(base_estimator=svm, random_state=0)
classifier_chain.fit(X_tr, y_tr)

# Prever e avaliar com Hamming Loss
y_pred = classifier_chain.predict(X_te)
loss = hamming_loss(y_te, y_pred)
print(f"Hamming Loss: {loss}")   # quanto menor, melhor
```

> [!tip] O que o código mostra
> O `ClassifierChain` implementa a estratégia **Classifier Chains** — repare que ele recebe um `base_estimator` (aqui, um SVM): cada elo da corrente é um SVM. A avaliação usa **`hamming_loss`** — a métrica multilabel onde **menor é melhor**.

---

## 8.7. Resumo

> [!summary] O essencial da Classificação Multilabel
> - **Binária** = 1 de 2 | **Multiclasse** = 1 de várias | **Multilabel** = **várias ao mesmo tempo**.
> - Os dados multilabel têm **várias colunas binárias** (uma por rótulo).
> - **Estratégias**:
>   - **Binary Relevance** → um classificador por rótulo (ignora relações).
>   - **Classifier Chains** → corrente; cada um usa as previsões anteriores (considera relações).
>   - **Label Powerset** → cada combinação de rótulos vira uma classe (explode se há muitas).
> - **Métricas**: **Exact Match** (tudo ou nada, maximizar) e **Hamming Loss** (fração de erros, minimizar).

---

## 🔗 Próximos passos
- [[09 - Datasets Desbalanceados]] — o desafio de classes muito raras (fraude, doença).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
