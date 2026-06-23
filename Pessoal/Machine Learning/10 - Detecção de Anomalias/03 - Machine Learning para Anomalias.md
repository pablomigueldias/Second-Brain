---
tags:
  - machine-learning
  - detecção-anomalias
  - lof
  - isolation-forest
  - one-class-svm
---

# 3. Machine Learning para Anomalias

> [!info] O que esta nota cobre
> As técnicas de **machine learning** para detectar anomalias: **LOF (Local Outlier Factor)**, **Isolation Forest** e **One-Class SVM**. Cada uma com uma estratégia diferente de "isolar o estranho".

---

## 3.1. Local Outlier Factor (LOF)

> [!note] A ideia
> O **LOF** é uma aplicação do **[[../Algoritmos de Machine Learning/09 - Aprendizado Baseado em Instância e KNN|KNN]]** para detecção de anomalias. Ele calcula um **score de anormalidade** para cada ponto com base nas **distâncias aos seus vizinhos locais**.

> [!important] "Local" é a palavra-chave
> O LOF compara a **densidade** ao redor de um ponto com a densidade ao redor dos vizinhos dele. Se um ponto está numa região **muito mais vazia** que a dos vizinhos, ele é um outlier.

> [!example] Intuição
> Imagine bairros: numa região densa (muitas casas próximas), uma casa isolada no meio do mato "destoa" — mesmo que, em outra região do mapa, casas isoladas sejam normais. O LOF capta esse desvio **relativo à vizinhança**, não global.

---

## 3.2. Isolation Forest

> [!note] A ideia
> **Outliers são isolados em árvores** (uma "floresta"). O insight: anomalias são **fáceis de separar** do resto.

> [!important] Como funciona
> - O algoritmo faz **divisões aleatórias** dos dados, repetidamente, formando árvores.
> - Dados que ficam **isolados cedo** (poucas divisões para separá-los) são **discrepantes** (anomalias).
> - Dados normais tendem a ser isolados **mais tarde** (precisam de muitas divisões).

> [!example] Intuição
> É como o jogo "20 perguntas". Se com **2 ou 3 perguntas** você já isolou alguém, essa pessoa é **bem diferente** de todo mundo. Se precisa de 20 perguntas, ela é "média", parecida com os outros. Anomalia = isolada com poucas perguntas.

---

## 3.3. One-Class SVM

> [!note] A ideia
> Uma **variação do SVM** (Support Vector Machine). Em vez de separar duas classes, ele aprende uma **fronteira que envolve os dados normais**.

> [!important] Como detecta
> O One-Class SVM traça uma fronteira ao redor do "normal". **Dados que caem fora dessa fronteira são considerados anomalias.**
> ```
>        ╭───────────╮
>        │  • • • •   │   ✗  ← fora da fronteira = anomalia
>        │ • normal • │
>        ╰───────────╯
> ```

> [!tip] Quando usar
> Útil quando você tem **muitos exemplos do normal** e poucos (ou nenhum) de anomalia — ele aprende só a "cara do normal" e sinaliza tudo que difere.

---

## 3.4. Comparação

> [!summary] Qual a estratégia de cada um
> | Técnica | Estratégia | Pensa em termos de... |
> |---|---|---|
> | **LOF** | Densidade relativa à vizinhança (KNN) | distância aos vizinhos locais |
> | **Isolation Forest** | Quão fácil é isolar o ponto | nº de divisões para separá-lo |
> | **One-Class SVM** | Fronteira em volta do normal | dentro/fora da fronteira |

---

## 3.5. Esqueleto em Python (scikit-learn)

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM

# -1 = anomalia, 1 = normal (nas três)
lof  = LocalOutlierFactor(n_neighbors=20).fit_predict(X)
iso  = IsolationForest(contamination=0.05).fit_predict(X)
ocsvm = OneClassSVM(nu=0.05).fit_predict(X)
```

---

## 3.6. Resumo

> [!summary] O essencial
> - **LOF:** baseado em KNN; compara densidade do ponto com a dos vizinhos (anomalia = região vazia relativa).
> - **Isolation Forest:** anomalias são **isoladas cedo** em divisões aleatórias.
> - **One-Class SVM:** aprende a fronteira do **normal**; fora dela = anomalia.

---

## 🔗 Próximos passos
- [[04 - Deep Learning para Anomalias]] — quando os padrões são complexos demais para ML clássico.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
