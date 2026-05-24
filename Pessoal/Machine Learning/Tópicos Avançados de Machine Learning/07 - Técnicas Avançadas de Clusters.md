---
tags:
  - machine-learning
  - tópicos-avançados
  - clustering
  - agrupamento
  - não-supervisionado
---

# 7. Técnicas Avançadas de Clusters

> [!info] O que esta nota cobre
> Como **avaliar a qualidade** de um agrupamento. Antes de confiar nos clusters, é preciso responder: **existem mesmo grupos nos dados? Quantos? São bons? Usei o melhor algoritmo?** Vamos ver as ferramentas que respondem cada pergunta.

> [!tip] Pré-requisito
> Esta nota assume que você conhece os conceitos de agrupamento e os algoritmos **K-means**, **DBSCAN** e **hierárquico** — vistos em [[09 - Agrupamentos (Clustering)]] (Fundamentos) e [[10 - K-means]] (Algoritmos).

---

## 7.1. As 4 Perguntas Críticas sobre Clusters

> [!warning] O problema fundamental
> Quando você roda um K-means, ele **SEMPRE** vai te entregar grupos — **mesmo que não exista nenhum grupo real nos dados**! O algoritmo nunca diz "não há clusters aqui". Por isso, precisamos **questionar** o resultado.

> [!question] As 4 perguntas
> 1. **De fato existem clusters nos dados?**
> 2. **O número de clusters está certo?** (usamos K=3 só porque... conhecíamos os rótulos!)
> 3. **Foram produzidos bons clusters?**
> 4. **Usamos o melhor algoritmo de agrupamento?**

> [!important] A armadilha do exemplo
> No exemplo do curso, foi usado K=3 — mas só porque o dataset (IRIS) **já tinha 3 classes conhecidas**. Na vida real, **você não sabe** o número certo. Cada pergunta abaixo tem uma ferramenta para respondê-la.

---

## 7.2. Pergunta 1: Existem Clusters nos Dados?

> [!note] A ferramenta: Estatística de Hopkins
> A **Estatística de Hopkins** mede a **tendência de agrupamento** dos dados — se eles têm "vontade natural" de formar grupos ou se estão aleatoriamente espalhados.

### Como interpretar o valor de Hopkins (H)

| Valor de H | Significado |
|---|---|
| **Perto de 0** | Dados **uniformemente distribuídos** (sem clusters) |
| **Perto de 0,5** | Dados **aleatórios** — não há tendência de agrupamento |
| **Perto de 1** | Dados com **forte tendência** a formar clusters |

> [!example] Exemplo do curso
> Foram mostrados dois conjuntos:
> - **H = 0,48** → próximo de 0,5 → dados sem tendência clara de agrupamento (não vale a pena agrupar).
> - **H = 0,82** → próximo de 1 → dados com forte tendência de agrupamento (faz sentido agrupar!).

> [!tip] A regra
> Só faz sentido aplicar clustering se a estatística de Hopkins indicar que **há tendência de agrupamento** (valor alto, perto de 1). Se der perto de 0,5, agrupar é forçar grupos que não existem.

---

## 7.3. Pergunta 2: Qual o Número Ideal de Clusters?

> [!note] As ferramentas
> Para descobrir o melhor **K** (número de grupos), há vários métodos:
> - **Elbow** (método do cotovelo)
> - **Average Silhouette** (silhueta média)
> - **Gap** (estatística de gap)
> - **Hubert index** e **D index**

### Método Elbow (Cotovelo)

> [!info] Como funciona
> Roda-se o clustering para vários valores de K e plota-se uma métrica de erro. O gráfico forma uma curva — o ponto onde ela "dobra" como um **cotovelo** indica o K ideal: depois dele, aumentar K quase não melhora.

```
   Erro │●
        │ ●
        │  ●
        │   ● ← "cotovelo" aqui = K ideal
        │    ●●●●●●●
        └──────────────▶ K
        1  2  3  4  5  6
```

### Average Silhouette (Silhueta Média)

> [!info] Como funciona
> Mede, para cada ponto, quão bem ele se encaixa no seu cluster comparado aos outros clusters. O **K** com a **maior silhueta média** é o melhor.

> [!tip] Silhueta — interpretação rápida
> O score de silhueta vai de **-1 a 1**:
> - Perto de **1** → ponto bem agrupado.
> - Perto de **0** → ponto na fronteira entre clusters.
> - Negativo → ponto provavelmente no cluster errado.

### Gap, Hubert e D index

> [!note] Outros índices
> - **Gap statistic** → compara o agrupamento real com um agrupamento de dados aleatórios.
> - **Hubert index** e **D index** → outros índices estatísticos para estimar o número ideal de clusters.

---

## 7.4. Pergunta 3: Os Clusters São Bons?

> [!important] O que define um BOM cluster
> Em um bom agrupamento:
> - **Diâmetro do cluster pequeno** → os pontos **dentro** de um grupo estão **próximos** entre si (grupos compactos).
> - **Distância entre os clusters grande** → grupos **diferentes** estão **bem separados** uns dos outros.

```
   Clusters BONS                Clusters RUINS
   (compactos e separados)      (espalhados e sobrepostos)

   ●●●        ●●●               ●  ●    ●  ●
   ●●●●       ●●●●               ● ● ●  ● ●
   ●●●        ●●●                ●  ● ● ● ●  ●
        ↑ longe ↑                  ↑ misturados ↑
```

### A ferramenta: Índice de Dunn

> [!note] Índice de Dunn
> O **Índice de Dunn** mede a **qualidade** do cluster, combinando as duas ideias acima (compactação interna + separação entre grupos).
>
> **Busca-se MAXIMIZAR este índice** — quanto maior o Dunn, melhor o agrupamento.

> [!tip] Intuição do Dunn
> Simplificando, o Dunn é mais ou menos:
> $$ \text{Dunn} \approx \frac{\text{menor distância entre clusters}}{\text{maior diâmetro de cluster}} $$
> Quanto **maior** esse valor, mais **separados** e **compactos** estão os grupos.

---

## 7.5. Pergunta 4: Usei o Melhor Algoritmo?

> [!note] Comparar algoritmos
> Não existe um "melhor algoritmo de cluster" universal. K-means, DBSCAN e hierárquico se comportam diferente em cada dataset. É preciso **comparar** — testando cada um e medindo a qualidade (ex.: pela silhueta).

---

## 7.6. Exemplo em Python (notebook do curso)

O notebook `BestCluster.ipynb` compara **três algoritmos** automaticamente, usando o **score de silhueta** como medida de qualidade:

```python
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score

def compare_algorithms(X, max_clusters):
    results = []
    cluster_range = range(2, max_clusters + 1)

    # K-means: testa vários valores de K
    for n_clusters in cluster_range:
        kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto')
        clusters = kmeans.fit_predict(X)
        score = silhouette_score(X, clusters)
        results.append(('KMeans', n_clusters, score))

    # Agrupamento Hierárquico: testa vários K
    for n_clusters in cluster_range:
        agglo = AgglomerativeClustering(n_clusters=n_clusters)
        clusters = agglo.fit_predict(X)
        score = silhouette_score(X, clusters)
        results.append(('Agglomerative', n_clusters, score))

    # DBSCAN: testa vários valores de eps
    for eps in np.arange(0.1, 0.9, 0.1):
        dbscan = DBSCAN(eps=eps, min_samples=5)
        clusters = dbscan.fit_predict(X)
        if len(set(clusters)) > 1:   # só se formou mais de 1 grupo
            score = silhouette_score(X, clusters)
            results.append(('DBSCAN', eps, score))
    return results

# Rodar no dataset IRIS (padronizado)
iris = datasets.load_iris()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(iris.data)

results = compare_algorithms(scaled_data, 10)
df = pd.DataFrame(results, columns=['Agrupador', 'Clusters', 'Score'])
# A linha com maior 'Score' indica a melhor combinação!
```

> [!tip] O que o código faz
> Ele responde às **perguntas 2 e 4** de uma vez: testa **3 algoritmos** com **vários números de clusters**, e mede a **silhueta** de cada combinação. A combinação com **maior score** é a vencedora — algoritmo e número de clusters ideais, escolhidos por evidência, não por chute.

---

## 7.7. Resumo: As Perguntas e suas Ferramentas

| Pergunta | Ferramenta |
|---|---|
| 1. Existem clusters? | **Estatística de Hopkins** (perto de 1 = sim) |
| 2. Quantos clusters? | **Elbow**, **Silhouette**, **Gap**, Hubert, D index |
| 3. Os clusters são bons? | **Índice de Dunn** (maximizar) |
| 4. Melhor algoritmo? | **Comparar** algoritmos pela silhueta |

---

## 7.8. Resumo

> [!summary] O essencial dos Clusters Avançados
> - O K-means **sempre** entrega grupos — mesmo quando não há grupos reais. Questione o resultado!
> - **Hopkins** → verifica se **existe** tendência de agrupamento (perto de 1 = sim).
> - **Elbow / Silhouette / Gap** → estimam o **número ideal** de clusters.
> - **Índice de Dunn** → mede a **qualidade** (compacto dentro, separado fora) — maximizar.
> - **Comparar algoritmos** (K-means, DBSCAN, hierárquico) pela **silhueta** para achar o melhor.

---

## 🔗 Próximos passos
- [[08 - Classificação Multilabel]] — quando uma instância pode pertencer a **várias classes** ao mesmo tempo.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
