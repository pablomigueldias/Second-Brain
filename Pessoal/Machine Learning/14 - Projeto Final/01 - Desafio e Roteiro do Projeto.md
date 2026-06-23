---
tags:
  - machine-learning
  - projeto-final
  - prática
  - f1-score
  - classificação
---

# 1. Desafio e Roteiro do Projeto

> [!info] O que esta nota cobre
> A descrição completa do desafio final, o dataset, a divisão dos arquivos, os requisitos obrigatórios e um **roteiro prático** para executar o projeto de ponta a ponta.

---

## 1. O objetivo

> [!abstract] Atividade prática
> Criar um modelo de **Machine Learning** cujo objetivo é a **melhor performance** possível.
> - **Métrica principal: F1 Score.**
> - O projeto resultante deve ser **publicado na plataforma** (e no seu portfólio).

---

## 2. O dataset — Adult Income

> [!note] Características
> - **15 atributos** + a classe.
> - **Classe (alvo):** `income` → `<=50K` ou `>50K` (classificação **binária**).
> - **~45.225 instâncias.**
> - Referência: `http://www.cs.toronto.edu/~delve/data/adult/desc.html`

**Atributos disponíveis:**

```
age, workclass, fnlwgt, education, educational-num, marital-status,
occupation, relationship, race, gender, capital-gain, capital-loss,
hours-per-week, native-country, income (alvo)
```

> [!tip] Mistura de tipos
> Há atributos **numéricos** (`age`, `hours-per-week`, `capital-gain`…) e **categóricos** (`workclass`, `occupation`, `native-country`…) — por isso a **codificação de categorias** é obrigatória.

---

## 3. Os arquivos (e a regra de ouro)

| Arquivo | Dados | Objetivo |
|---|---|---|
| `train.csv` | 70% (~34 mil) | **Treinar** o modelo |
| `validation.csv` | 15% (~7,3 mil) | Avaliação, performance, **tuning** |
| `test.csv` | 15% (~7,3 mil) | Avaliar performance **apenas** |

> [!warning] Regra de ouro
> O `test.csv` deve ser usado **apenas na avaliação final** — **nunca** para tuning. As métricas nele são o **resultado final** do projeto. Ajustar o modelo olhando o teste é **vazamento de dados (data leakage)** e invalida o resultado.

---

## 4. Requisitos obrigatórios

> [!example] Checklist do projeto
> **Pré-processamento**
> - [ ] Tratar **NANs** (valores ausentes)
> - [ ] Tratar **outliers**
>
> **Engenharia de atributos**
> - [ ] **Codificação de categorias** (One-Hot / Ordinal / Target encoding)
> - [ ] **Dimensionamento de características** (scaling / normalização)
> - [ ] **Seleção de atributos**
>
> **Tuning**
> - [ ] **Registrar** as mudanças na performance a cada etapa
> - [ ] Mostrar **o que foi mudado** e demonstrar resultados (sugestão: **tabela** comparativa)
>
> **Avaliação e entrega**
> - [ ] Usar as **principais métricas** (com destaque para **F1 Score**)
> - [ ] Usar **XAI** para explicar o modelo
> - [ ] **Publicar o código** do projeto
> - [ ] Apresentar um **relatório** com os resultados
> - [ ] Publicar no **portfólio**

---

## 5. Roteiro prático sugerido

> [!abstract] Pipeline ponta a ponta

### Passo 1 — Carregar e explorar
```python
import pandas as pd
train = pd.read_csv("train.csv")
val   = pd.read_csv("validation.csv")
test  = pd.read_csv("test.csv")

train.info()
train.describe()
train['income'].value_counts(normalize=True)   # checar desbalanceamento
```

> [!tip] Classe desbalanceada
> Em geral há **mais** `<=50K` que `>50K`. Por isso a **acurácia engana** e o **F1 Score** é a métrica certa — ele equilibra **precisão** e **recall** da classe positiva.

### Passo 2 — Pré-processamento
```python
# NANs (no Adult costumam vir como "?")
train = train.replace("?", pd.NA)
# imputar categóricos pela moda, numéricos pela mediana
```

### Passo 3 — Engenharia de atributos
```python
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

cat = train.select_dtypes("object").columns.drop("income")
num = train.select_dtypes("number").columns

pre = ColumnTransformer([
    ("num", StandardScaler(), num),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat),
])
```

### Passo 4 — Modelar
```python
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

X_train, y_train = train.drop(columns="income"), (train["income"].str.strip() == ">50K").astype(int)
X_val,   y_val   = val.drop(columns="income"),   (val["income"].str.strip() == ">50K").astype(int)

model = Pipeline([("pre", pre), ("clf", RandomForestClassifier(random_state=42))])
model.fit(X_train, y_train)
```

### Passo 5 — Avaliar (na validação) e tunar
```python
from sklearn.metrics import f1_score, classification_report

pred_val = model.predict(X_val)
print("F1:", f1_score(y_val, pred_val))
print(classification_report(y_val, pred_val))
```

> [!note] Documente o tuning
> A cada mudança (novo atributo, novo hiperparâmetro, outro algoritmo), registre o **F1 na validação** numa tabela:
>
> | Versão | Mudança | F1 (val) |
> |---|---|---|
> | v1 | baseline RandomForest | 0,xx |
> | v2 | + tratamento de outliers | 0,xx |
> | v3 | + tuning de `max_depth` | 0,xx |

### Passo 6 — Avaliação final (no teste, uma vez)
```python
X_test, y_test = test.drop(columns="income"), (test["income"].str.strip() == ">50K").astype(int)
print("F1 FINAL (test):", f1_score(y_test, model.predict(X_test)))
```

### Passo 7 — Explicar com XAI
```python
import shap
explainer = shap.TreeExplainer(model.named_steps["clf"])
# shap.summary_plot(...) → quais atributos mais pesam na previsão
```
Ver [[06 - Machine Learning Explicável (XAI)/00 - Índice|módulo de XAI]] para SHAP/LIME.

---

## 6. Resumo

> [!summary] Para entregar bem
> 1. **Nunca** tune no `test.csv`.
> 2. **F1 Score** é o que importa (classe desbalanceada).
> 3. **Documente cada mudança** em tabela.
> 4. **Explique** o modelo com XAI.
> 5. **Publique** código + relatório no portfólio.

---

## 🏷️ Tags Relacionadas
#machine-learning #projeto-final #f1-score #classificação #prática #estudos

---
[[00 - Índice|⬆️ Voltar ao Índice do Módulo]]
