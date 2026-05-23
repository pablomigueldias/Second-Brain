---
tags:
  - machine-learning
  - algoritmos
  - random-forest
  - ensemble
  - classificação
  - supervisionado
---
 
# 8. Random Forest

> [!info] O que esta nota cobre
> O algoritmo **Random Forest** (Floresta Aleatória) e a ideia de **aprendizado baseado em grupos** (ensemble): por que **vários classificadores juntos** superam um classificador único, como a floresta é construída (**bootstrap** + subconjuntos de atributos) e como faz a previsão por **votação**.

---

## 8.1. A Ideia: Aprendizado em Grupo (Ensemble)

> [!important] O princípio fundamental
> Um **"conjunto" de classificadores independentes** pode ter uma **performance melhor** do que um **classificador único**.

> [!example] Analogia: a sabedoria das multidões
> Imagine adivinhar quantas balas há num pote. Uma pessoa sozinha pode errar feio. Mas se **100 pessoas** chutam e você tira a **média**, o resultado costuma ser surpreendentemente preciso. Vários "palpites independentes" se corrigem mutuamente.

### Como criar classificadores diferentes?

Para o ensemble funcionar, os classificadores precisam ser **diferentes entre si**. Há três formas:

> [!note] Gerando diversidade
> 1. **Alterando parametrizações** nos classificadores (mudando os **hiperparâmetros**).
> 2. **Escolhendo subconjuntos de atributos** diferentes para cada classificador.
> 3. **Alternando os dados de treinamento** de cada classificador.

---

## 8.2. Exemplos de Métodos de Ensemble

> [!info] Técnicas de aprendizado em grupo
> - **Random Forest** ← o foco desta nota
> - **Bagging** (Bootstrap Aggregating)
> - **Boosting**
> - **AdaBoost**

> [!tip] Bagging vs. Boosting (resumo)
> - **Bagging** → treina vários modelos em **paralelo**, com dados sorteados, e combina (Random Forest é um tipo de bagging).
> - **Boosting** → treina modelos em **sequência**, cada um focando nos **erros** do anterior (AdaBoost é um tipo de boosting).

---

## 8.3. O que é uma Random Forest?

> [!note] Definição
> Uma **Random Forest** (Floresta Aleatória) é um conjunto de muitas **Árvores de Decisão** trabalhando juntas. O nome diz tudo: uma **"floresta"** de **árvores**, criadas de forma **"aleatória"**.

### As três etapas

```
   1. Induz diversas árvores de decisão
            │
            ▼
   2. Executa a classificação em CADA árvore
            │
            ▼
   3. Faz uma VOTAÇÃO para decidir a classe final
```

> [!tip] Pré-requisito
> A Random Forest é construída sobre [[06 - Árvores de Decisão]]. Se aquela nota ainda está confusa, revise antes.

---

## 8.4. Como as Múltiplas Árvores São Criadas?

A "aleatoriedade" da floresta vem de **dois mecanismos**:

### Mecanismo 1: Bootstrap (amostragem com reposição)

> [!note] Definição
> Cada árvore é treinada com um conjunto de dados de treino criado de forma **aleatória, mas com reposição** — isso se chama **bootstrap**.

> [!example] O que significa "com reposição"
> Imagine sortear instâncias de um saco e **devolvê-las** após cada sorteio. Resultado: cada árvore recebe um conjunto de treino **ligeiramente diferente**, e algumas instâncias podem aparecer **repetidas** (ou não aparecer) num dado conjunto.

### Mecanismo 2: Subconjunto aleatório de atributos

> [!note] Definição
> Do **total de atributos** da relação, é selecionado um **subconjunto de atributos aleatórios** para **cada árvore**.

> [!example] Exemplo
> Se o dataset tem 10 atributos, a árvore 1 pode usar só 4 deles (sorteados), a árvore 2 outros 4, e assim por diante.

> [!important] Por que esses dois mecanismos?
> Eles garantem que cada árvore seja **diferente** das outras. Se todas fossem iguais, votar não adiantaria nada — seria como perguntar a mesma coisa para clones. A diversidade é o que faz o ensemble funcionar.

```
   Dataset original
        │
        ├──▶ Bootstrap 1 + atributos {A,C,E,G} ──▶ 🌳 Árvore 1
        ├──▶ Bootstrap 2 + atributos {B,C,F,H} ──▶ 🌳 Árvore 2
        ├──▶ Bootstrap 3 + atributos {A,D,E,I} ──▶ 🌳 Árvore 3
        └──▶ ...                                   ──▶ 🌳 Árvore N
```

---

## 8.5. Previsão: O Processo de Votação

> [!note] Como a floresta decide
> Para classificar uma instância nova:
> 1. **Cada árvore** faz sua própria previsão.
> 2. As previsões são **contabilizadas** (votação).
> 3. A classe **mais votada** vence — é a previsão final.

> [!example] Exemplo de votação
> Uma instância nova é classificada por 5 árvores:
>
> | Árvore | Voto |
> |---|---|
> | 🌳 Árvore 1 | Yes |
> | 🌳 Árvore 2 | No |
> | 🌳 Árvore 3 | Yes |
> | 🌳 Árvore 4 | Yes |
> | 🌳 Árvore 5 | No |
>
> **Resultado da votação: Yes = 3, No = 2 → previsão final: Yes** ✅

> [!tip] Para classificação vs. regressão
> - **Classificação** → a floresta faz **votação** (classe mais votada).
> - **Regressão** → a floresta faz a **média** das previsões numéricas das árvores.

---

## 8.6. Por que a Random Forest é Melhor que Uma Árvore?

| Aspecto | **Uma Árvore de Decisão** | **Random Forest** |
|---|---|---|
| Estabilidade | Instável (muda muito com os dados) | **Estável** (média de muitas árvores) |
| Overfitting | Alta tendência | **Reduzida** (a votação "suaviza" erros) |
| Precisão | Boa | Geralmente **melhor** |
| Interpretabilidade | ✅ Fácil (um fluxograma) | ❌ Difícil (centenas de árvores) |
| Velocidade | Rápida | Mais lenta (treina N árvores) |

> [!summary] A grande sacada
> Uma árvore sozinha pode "decorar" o ruído dos dados (overfitting). Mas como cada árvore da floresta vê dados e atributos **diferentes**, os erros individuais tendem a **se cancelar** na votação. O resultado é um modelo mais **robusto**.

---

## 8.7. Exemplo em Python (notebook do curso)

O curso usou o `RandomForestClassifier` do scikit-learn com `insurance.csv`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Carregar e preparar dados
base = pd.read_csv("insurance.csv", keep_default_na=False)
base = base.drop(columns=['Unnamed: 0'])

y = base.iloc[:, 7].values
X = base.drop(base.columns[7], axis=1).values

labelencoder = LabelEncoder()
for i in range(X.shape[1]):
    if X[:, i].dtype == 'object':
        X[:, i] = labelencoder.fit_transform(X[:, i])

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=12)

# Criar a floresta — n_estimators=500 significa 500 ÁRVORES!
modelo = RandomForestClassifier(random_state=1, max_depth=20,
                                max_leaf_nodes=12, n_estimators=500)
modelo.fit(X_treinamento, y_treinamento)

# Dá pra "espiar" uma árvore individual da floresta
tree_to_visualize = modelo.estimators_[1]   # a árvore de índice 1
plt.figure(figsize=(20, 20))
plot_tree(tree_to_visualize, filled=True,
          feature_names=base.columns[:-1], class_names=True, rounded=True)
plt.show()

# Prever e avaliar
previsoes = modelo.predict(X_teste)
print(f'Acurácia: {accuracy_score(y_teste, previsoes)}')
print(classification_report(y_teste, previsoes))
```

> [!tip] O parâmetro mais importante: `n_estimators`
> `n_estimators=500` diz que a floresta terá **500 árvores**. Mais árvores = previsão mais estável (até certo ponto), mas treino mais lento. O `modelo.estimators_` é a lista com todas as árvores — dá pra inspecionar qualquer uma.

---

## 8.8. Resumo

> [!summary] O essencial do Random Forest
> - **Ensemble**: vários classificadores juntos superam um sozinho.
> - **Random Forest** = floresta de muitas **árvores de decisão**.
> - Cada árvore é diferente graças a: **bootstrap** (dados sorteados com reposição) + **subconjunto aleatório de atributos**.
> - **Previsão** = cada árvore vota, a **classe mais votada** vence.
> - Vantagem: **menos overfitting**, mais **estável** e preciso que uma árvore só.
> - Desvantagem: **menos interpretável** e mais **lento**.

---

## 🔗 Próximos passos
- [[09 - Aprendizado Baseado em Instância e KNN]] — uma abordagem totalmente diferente: classificar **sem construir modelo**.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
