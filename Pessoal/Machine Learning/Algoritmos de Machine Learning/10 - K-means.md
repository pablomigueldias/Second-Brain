---
tags:
  - machine-learning
  - algoritmos
  - k-means
  - agrupamento
  - clustering
  - não-supervisionado
---

# 10. K-means

> [!info] O que esta nota cobre
> O algoritmo **K-means** de agrupamento (clustering) **passo a passo**: o objetivo, como o algoritmo funciona em iterações usando **centróides**, e um exemplo numérico completo de uma rodada de agrupamento.

> [!tip] Conexão com Fundamentos
> O conceito de agrupamento foi introduzido em [[09 - Agrupamentos (Clustering)]] no módulo de Fundamentos. Aqui detalhamos o **K-means na prática**, com os cálculos.

---

## 10.1. O que é o K-means?

> [!note] Definição
> O **K-means** é um algoritmo de **agrupamento** que recebe **dados sem classe** e os organiza em grupos de forma **"orgânica"** — de acordo com o algoritmo e seus parâmetros.

### É aprendizado não supervisionado

> [!important] Sem classe!
> Diferente de todos os algoritmos anteriores (Naive Bayes, Árvores, KNN...), o K-means **não tem uma coluna de classe**. Ele **descobre** os grupos sozinho.

### O objetivo

> [!note] O que o K-means produz
> - **Centróides** → os "pontos centrais" de cada grupo.
> - Um **grupo (rótulo)** para **cada instância** — dizer a qual cluster cada ponto pertence.

---

## 10.2. O Algoritmo K-means Passo a Passo

> [!important] Os 5 passos do K-means
> 1. **Definir K** — o número de grupos desejado (ex: K = 2).
> 2. **Definir K centróides** iniciais (pontos de partida).
> 3. **Cada instância busca o centróide mais próximo** (e se junta a ele).
> 4. **Os centróides são atualizados** — recalculados como a **média dos pontos** do seu grupo.
> 5. **Repetir** os passos 3 e 4 até atingir um **critério de parada**.

```
   ┌─────────────────────────────────────────┐
   │ 1. Definir K                            │
   │ 2. Posicionar K centróides              │
   └─────────────────────────────────────────┘
                    │
                    ▼
   ┌─────────────────────────────────────────┐
   │ 3. Cada ponto → centróide mais próximo   │ ◀──┐
   └─────────────────────────────────────────┘    │
                    │                              │ repete
                    ▼                              │ até
   ┌─────────────────────────────────────────┐    │ estabilizar
   │ 4. Recalcular centróides (média grupo)   │ ───┘
   └─────────────────────────────────────────┘
                    │
                    ▼
              Critério de parada → FIM
```

> [!tip] Critério de parada
> Geralmente, o algoritmo para quando os centróides **param de se mover** (ou se movem muito pouco) entre uma iteração e outra — sinal de que os grupos se estabilizaram.

---

## 10.3. Exemplo Numérico Completo

Vamos acompanhar uma rodada do K-means com **6 instâncias** e **K = 2**.

### As instâncias a agrupar

| ID | AtributoA | AtributoB |
|---|---|---|
| 1 | 0,6 | -0,39 |
| 2 | 0,77 | 0,14 |
| 3 | 0,95 | 0,51 |
| 4 | 1,22 | 0,22 |
| 5 | 1,19 | -0,04 |
| 6 | 1,09 | -0,41 |

```
   B
   │        ● 3
   │              ● 4
   │     ● 2
   │              ● 6 (?)
   │
   │  ● 1        ● 5
   └──────────────────▶ A
```

---

### Passo 1 e 2: Definir K=2 e os centróides iniciais

| Centróide | x | y |
|---|---|---|
| **C1** | 1,2 | -0,31 |
| **C2** | 0,8 | -0,07 |

---

### Passo 3: Calcular a distância de cada ponto aos centróides

Usando a **distância euclidiana** (a mesma de [[09 - Aprendizado Baseado em Instância e KNN]]), calculamos a distância de cada instância até C1 e até C2:

| ID | AtribA | AtribB | Dist. até C1 | Dist. até C2 | Mais próximo |
|---|---|---|---|---|---|
| 1 | 0,6 | -0,39 | 0,60 | 0,37 | **C2** |
| 2 | 0,77 | 0,14 | 0,62 | 0,21 | **C2** |
| 3 | 0,95 | 0,51 | 0,85 | 0,59 | **C2** |
| 4 | 1,22 | 0,22 | 0,53 | 0,51 | **C2** |
| 5 | 1,19 | -0,04 | 0,27 | 0,39 | **C1** |
| 6 | 1,09 | -0,41 | 0,14 | 0,44 | **C1** |

### Atribuição aos grupos (resultado do passo 3)

> [!summary] Grupos formados nesta iteração
> - **Grupo C1**: instâncias **5 e 6** (as mais próximas de C1).
> - **Grupo C2**: instâncias **1, 2, 3 e 4** (as mais próximas de C2).

---

### Passo 4: Atualizar os centróides

Agora cada centróide se move para a **média dos pontos do seu grupo**:

| Centróide | Antigo (x, y) | **Atualizado (x, y)** |
|---|---|---|
| **C1** | (1,2 ; -0,31) | **(1,14 ; -0,22)** |
| **C2** | (0,8 ; -0,07) | **(0,88 ; 0,12)** |

> [!example] Como C1 foi recalculado
> O grupo C1 tem as instâncias 5 (1,19 ; -0,04) e 6 (1,09 ; -0,41). A média:
> - x = (1,19 + 1,09) / 2 = 1,14
> - y = (-0,04 + (-0,41)) / 2 = -0,22
> → Novo C1 = (1,14 ; -0,22) ✅

---

### Passo 5 (= repetir passo 3): Recalcular as distâncias

Com os centróides **novos**, recalculamos as distâncias de todos os pontos:

| ID | AtribA | AtribB | Dist. C1 (novo) | Dist. C2 (novo) | Mais próximo |
|---|---|---|---|---|---|
| 1 | 0,6 | -0,39 | 0,56 | 0,58 | **C1** |
| 2 | 0,77 | 0,14 | 0,51 | 0,11 | **C2** |
| 3 | 0,95 | 0,51 | 0,75 | 0,39 | **C2** |
| 4 | 1,22 | 0,22 | 0,44 | 0,35 | **C2** |
| 5 | 1,19 | -0,04 | 0,18 | 0,34 | **C1** |
| 6 | 1,09 | -0,41 | 0,19 | 0,57 | **C1** |

> [!note] O agrupamento mudou!
> Compare com a iteração anterior: a **instância 1** mudou de grupo (estava em C2, agora foi para C1). Como houve mudança, o algoritmo **continua** — repete os passos 3 e 4 de novo.

### Ajuste do agrupamento

```
   ANTES (iteração 1)            DEPOIS (iteração 2)

   B │     ● 3                   B │     ● 3
     │          ● 4                │          ● 4
     │  ● 2                        │  ● 2
     │       C2 ● 6                │       C2  ● 6
     │       C1                    │       C1
     │  ● 1      ● 5               │  ● 1      ● 5
     └──────────────▶             └──────────────▶
   (grupo 1 muda de membro)
```

> [!important] Quando o algoritmo para
> O K-means continua repetindo até que **nenhum ponto mude de grupo** entre iterações — aí os centróides estabilizaram e os grupos estão "finalizados".

---

## 10.4. Exemplo em Python (notebook do curso)

O curso usou o `KMeans` do scikit-learn no dataset **IRIS**, comparando com outros algoritmos de cluster:

```python
from sklearn import datasets
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import confusion_matrix

# Carregar o dataset IRIS
iris = datasets.load_iris()

# K-means com 3 grupos
kmeans = KMeans(n_clusters=3, n_init='auto')
kmeans.fit(iris.data)
print(kmeans.labels_)   # o grupo (rótulo) de cada instância

# Comparar os grupos descobertos com as classes reais
resultados = confusion_matrix(iris.target, kmeans.labels_)
print(resultados)

# O notebook também compara com DBSCAN e Hierárquico:
dbscan = DBSCAN(eps=0.5, min_samples=3)
dbscan_labels = dbscan.fit_predict(iris.data)

agglo = AgglomerativeClustering(n_clusters=3)
agglo_labels = agglo.fit_predict(iris.data)
```

> [!tip] O parâmetro `n_clusters`
> `n_clusters=3` é o **K** do K-means — você diz quantos grupos quer. Lembre que o **DBSCAN não precisa** desse parâmetro (descobre sozinho), conforme visto em [[09 - Agrupamentos (Clustering)]].

> [!note] Por que comparar com `confusion_matrix`?
> O IRIS na verdade **tem** classes conhecidas (3 espécies de flor). O truque didático é: rodar o K-means **fingindo** que não há classes, e depois comparar os grupos descobertos com as classes reais — para ver se o agrupamento "acertou".

---

## 10.5. Pontos de Atenção do K-means

> [!warning] Limitações (relembrando de Fundamentos)
> - Você precisa **definir o K** antecipadamente (nem sempre se sabe quantos grupos existem).
> - O resultado depende da **posição inicial** dos centróides — inicializações ruins levam a grupos ruins.
> - Tem dificuldade com grupos **não-esféricos** ou de **densidades muito diferentes**.
>
> Para esses casos, **DBSCAN** ou **agrupamento hierárquico** podem ser melhores — veja [[09 - Agrupamentos (Clustering)]].

---

## 10.6. Resumo

> [!summary] O essencial do K-means
> - Algoritmo de **agrupamento não supervisionado** (sem classe).
> - **Você define o K** (número de grupos).
> - **Ciclo**: cada ponto vai pro centróide mais próximo → centróides são recalculados (média) → repete.
> - **Para** quando os pontos não mudam mais de grupo.
> - Usa **distância euclidiana** para medir proximidade.
> - **Resultado**: centróides + um rótulo de grupo para cada instância.

---

## 🔗 Próximos passos
- [[11 - Apriori]] — o último algoritmo: regras de associação na prática.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
