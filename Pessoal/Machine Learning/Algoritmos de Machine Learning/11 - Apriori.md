---
tags:
  - machine-learning
  - algoritmos
  - apriori
  - regras-de-associação
  - não-supervisionado
---

# 11. Apriori

> [!info] O que esta nota cobre
> O algoritmo **Apriori** para mineração de **regras de associação**: o princípio que o torna eficiente, e um exemplo **passo a passo** de como ele conta ocorrências, calcula suporte e elimina conjuntos não-frequentes até chegar ao conjunto final de regras.

> [!tip] Conexão com Fundamentos
> As **regras de associação** e suas métricas (**suporte**, **confiança**, **lift**) foram explicadas em [[10 - Regras de Associação]] no módulo de Fundamentos. Aqui detalhamos o **algoritmo Apriori funcionando na prática**.

---

## 11.1. O Princípio do Apriori

> [!important] O princípio fundamental (em duas partes)
> 1. **Se um conjunto de itens é frequente, um subconjunto dele também é frequente.**
> 2. **Se um conjunto de itens NÃO é frequente, nenhum superconjunto dele será frequente.**

> [!example] Entendendo o princípio
> - Se `{pão, leite, queijo}` é frequente → então `{pão, leite}`, `{pão, queijo}` e `{leite, queijo}` **também são**.
> - Se `{pão, abacaxi}` **não** é frequente → então `{pão, abacaxi, manteiga}` **com certeza também não é**.

> [!tip] Por que esse princípio é genial?
> Ele permite **podar** (descartar) gigantescas quantidades de combinações **sem precisar testá-las**. Se um par já é raro, nem adianta olhar os trios que o contêm. Isso torna o Apriori **eficiente**.

---

## 11.2. Exemplo Passo a Passo

Vamos minerar regras a partir destas **7 transações** de um supermercado:

| Transação | Itens comprados |
|---|---|
| 1 | Cerveja, Pizza, Sorvete, Refrigerante, Bolo |
| 2 | Cerveja, Pizza, Sorvete, Frutas |
| 3 | Pizza, Refrigerante, Amendoim |
| 4 | Pipoca, Sorvete, Suco, Amendoim |
| 5 | Suco, Amendoim, Refrigerante |
| 6 | Panqueca, Pizza, Amendoim |
| 7 | Cerveja, Sorvete, Bolo, Suco, Pizza |

**Suporte mínimo definido: 40%** (qualquer item/conjunto abaixo disso é descartado).

---

### Etapa 1: Contar as ocorrências de cada item

Quantas transações contêm cada item:

| Item | Frequência |
|---|---|
| Cerveja | 3 |
| Pizza | 5 |
| Sorvete | 4 |
| Refrigerante | 3 |
| Bolo | 2 |
| Frutas | 1 |
| Amendoim | 4 |
| Pipoca | 1 |
| Panqueca | 1 |
| Suco | 3 |

---

### Etapa 2: Calcular o suporte e cortar quem está abaixo de 40%

Suporte = frequência ÷ total de transações (7).

| Item | Frequência | Suporte | Passa? (≥ 40%) |
|---|---|---|---|
| Cerveja | 3 | 42% | ✅ |
| Pizza | 5 | 71% | ✅ |
| Sorvete | 4 | 57% | ✅ |
| Refrigerante | 3 | 42% | ✅ |
| Bolo | 2 | 28% | ❌ cortado |
| Frutas | 1 | 14% | ❌ cortado |
| Amendoim | 4 | 57% | ✅ |
| Pipoca | 1 | 14% | ❌ cortado |
| Panqueca | 1 | 14% | ❌ cortado |
| Suco | 3 | 42% | ✅ |

> [!summary] Itens frequentes (sobreviventes)
> **Cerveja, Pizza, Sorvete, Refrigerante, Amendoim, Suco** — só esses continuam. Bolo, Frutas, Pipoca e Panqueca foram **eliminados**.

> [!tip] O princípio em ação
> Como `Bolo` não é frequente, **nenhum par ou trio que contenha Bolo** precisa ser testado. Já economizamos trabalho!

---

### Etapa 3: Buscar pares de itens (só entre os frequentes)

Agora montamos **pares** apenas com os 6 itens que sobreviveram, e contamos quantas transações contêm cada par:

| Par | Frequência | Suporte |
|---|---|---|
| Cerveja - Pizza | 3 | 42% |
| Cerveja - Sorvete | 3 | 42% |
| Cerveja - Refrigerante | 1 | 14% |
| Cerveja - Amendoim | 0 | 0% |
| Cerveja - Suco | 1 | 14% |
| Pizza - Sorvete | 2 | 28% |
| Pizza - Refrigerante | 2 | 28% |
| Pizza - Amendoim | 2 | 28% |
| Pizza - Suco | 0 | 0% |
| Sorvete - Refrigerante | 1 | 14% |
| Sorvete - Amendoim | 1 | 14% |
| Sorvete - Suco | 2 | 28% |
| Refrigerante - Amendoim | 2 | 28% |
| Refrigerante - Suco | 1 | 14% |
| Amendoim - Suco | 1 | 14% |

---

### Etapa 4: Cortar os pares abaixo de 40%

| Par | Suporte | Passa? |
|---|---|---|
| **Cerveja - Pizza** | 42% | ✅ |
| **Cerveja - Sorvete** | 42% | ✅ |
| Todos os outros pares | ≤ 28% | ❌ cortados |

> [!summary] Pares frequentes (sobreviventes)
> Apenas **Cerveja-Pizza** e **Cerveja-Sorvete** passaram.

---

### Etapa 5: Buscar conjuntos de três itens

Pelo princípio do Apriori, um trio só pode ser frequente se **todos os seus pares** forem frequentes. Os únicos pares frequentes envolvem `Cerveja`, `Pizza` e `Sorvete` — então o único trio candidato é `{Cerveja, Pizza, Sorvete}`:

| Trio | Frequência | Suporte | Passa? |
|---|---|---|---|
| Cerveja - Pizza - Sorvete | 3 | 42% | ✅ |

---

## 11.3. Conjunto Final de Regras

> [!success] Resultado da mineração
> Os conjuntos de itens **frequentes** encontrados foram:
>
> | Conjunto | Frequência | Suporte |
> |---|---|---|
> | Cerveja - Pizza | 3 | 42% |
> | Cerveja - Sorvete | 3 | 42% |
> | Cerveja - Pizza - Sorvete | 3 | 42% |

A partir desses conjuntos frequentes, geram-se as **regras de associação** (calculando confiança e lift, conforme [[10 - Regras de Associação]]). Por exemplo: *"quem compra Cerveja e Pizza tende a comprar Sorvete"*.

---

## 11.4. O Algoritmo em Resumo

```
   APRIORI:
        │
        ├─ 1. Contar itens individuais
        ├─ 2. Cortar os que têm suporte < mínimo
        │
        ├─ 3. Gerar PARES (só com itens frequentes)
        ├─ 4. Cortar pares com suporte < mínimo
        │
        ├─ 5. Gerar TRIOS (só com pares frequentes)
        ├─ 6. Cortar trios com suporte < mínimo
        │
        ├─ ... repetir para quádruplas, etc. ...
        │
        └─ 7. Conjuntos frequentes → gerar as REGRAS
              (calcular confiança e lift)
```

> [!tip] A cada nível, o universo encolhe
> Repare como o trabalho **diminui** a cada etapa: começamos com 10 itens, sobraram 6; testamos 15 pares, sobraram 2; testamos só 1 trio. O princípio do Apriori **poda agressivamente** o espaço de busca.

---

## 11.5. Exemplo em Python (notebook do curso)

O curso usou a biblioteca `mlxtend` para rodar o Apriori:

```python
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Ler as transações de um arquivo (cada linha = uma transação)
with open('Transacoes.txt', "r") as f:
    transactions = [line.strip().split(",") for line in f.readlines()]

# Transformar em formato de tabela binária (one-hot das transações)
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Rodar o Apriori — min_support=0.5 é o suporte mínimo (50%)
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
print(frequent_itemsets)

# Gerar as regras de associação a partir dos conjuntos frequentes
rules = association_rules(frequent_itemsets, metric="confidence",
                          min_threshold=0.5)
print(rules)
```

> [!note] Os dois parâmetros-chave
> - `min_support=0.5` → o **suporte mínimo** (a "régua de corte" da etapa 2, 4, 6...).
> - `min_threshold=0.5` em `association_rules` → o filtro mínimo de **confiança** para uma regra ser mantida.
>
> A função `association_rules` calcula automaticamente **suporte, confiança e lift** de cada regra.

---

## 11.6. Apriori vs. FP-Grow (relembrando)

> [!tip] Lembra de Fundamentos?
> Em [[10 - Regras de Associação]] foram citados **dois** algoritmos:
> - **Apriori** (este) → didático, baseado em "podar conjuntos não-frequentes". Pode ser lento em dados muito grandes (varre os dados várias vezes).
> - **FP-Grow** → usa uma estrutura de **árvore** (FP-tree), geralmente **mais rápido**.

---

## 11.7. Resumo

> [!summary] O essencial do Apriori
> - Algoritmo para minerar **regras de associação**.
> - **Princípio**: se um conjunto é frequente, seus subconjuntos também são (e o contrário também vale).
> - **Processo**: conta itens → corta os raros → forma pares → corta → forma trios → corta → ... → gera regras.
> - O **suporte mínimo** é o "corte" aplicado em cada nível.
> - O princípio permite **podar** o espaço de busca, tornando o algoritmo eficiente.

---


| Algoritmo | Tarefa | Tipo |
|---|---|---|
| **Regressão Linear** | Prever números | Supervisionado |
| **Naive Bayes** | Classificar (probabilístico) | Supervisionado |
| **Redes Bayesianas** | Classificar (com dependências) | Supervisionado |
| **Árvore de Decisão** | Classificar (perguntas) | Supervisionado |
| **Random Forest** | Classificar (ensemble) | Supervisionado |
| **KNN** | Classificar (por vizinhança) | Supervisionado |
| **K-means** | Agrupar | Não Supervisionado |
| **Apriori** | Regras de associação | Não Supervisionado |

> [!tip] Próximos estudos sugeridos
> - **Regressão Logística** e **SVM** (Support Vector Machines).
> - **Gradient Boosting** (XGBoost, LightGBM) — ensembles mais avançados.
> - **Redes Neurais** e **Deep Learning**.
> - **Ajuste de hiperparâmetros** (Grid Search, Random Search).
> - **MLOps** — colocar modelos em produção.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
