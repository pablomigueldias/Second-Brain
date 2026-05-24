---
tags:
  - machine-learning
  - tópicos-avançados
  - classificação
  - desbalanceamento
  - smote
---

# 9. Datasets Desbalanceados

> [!info] O que esta nota cobre
> O problema das **classes desbalanceadas**: quando uma classe é muito mais rara que a outra. Veremos por que isso atrapalha os modelos e as soluções: coleta balanceada, métricas apropriadas, **undersampling**, **oversampling** e o método **SMOTE**.

---

## 9.1. O que é uma Classe Desbalanceada?

> [!note] Definição
> Uma classe **desbalanceada** ocorre quando uma classe aparece **muito mais** que a(s) outra(s) no dataset.

> [!example] Exemplos do mundo real
> - A **maioria das transações** não são fraudulentas.
> - A **maioria dos pacientes** não estão doentes.
> - A **maioria dos clientes** não vai abandonar a empresa (churn).
> - A **maioria dos acessos** a uma rede não são ataques.
>
> Em todos esses casos, a classe que **interessa** (fraude, doença, churn, ataque) é justamente a **minoritária** — a rara.

```
   Dataset DESBALANCEADO (típico de fraude)

   Legítimas:  ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●  (95%)
   Fraudes:    ●○                              (5%)
                ↑ a classe que importa é a minoria!
```

---

## 9.2. Por que o Desbalanceamento é um Problema?

> [!warning] O perigo
> Com classes desbalanceadas, o modelo tende a **"se acomodar"** prevendo sempre a classe **majoritária** — e ainda assim ter uma **acurácia alta**.

> [!tip] Conexão: a Armadilha da Acurácia
> Esse é exatamente o problema da **classe rara** visto em [[05 - Avaliação de Performance e Matriz de Confusão]]: um modelo que prevê "tudo legítimo" num dataset com 99% de transações legítimas teria **99% de acurácia** — e seria **totalmente inútil** (recall de fraude = 0%).

---

## 9.3. As Soluções

O curso apresenta **5 soluções** para lidar com datasets desbalanceados:

> [!note] As 5 soluções
> 1. **Coletar dados de forma balanceada** (desde o início).
> 2. **Gerar amostras estratificadas e balanceadas** (se houver dados em abundância).
> 3. **Usar métricas de avaliação apropriadas**.
> 4. **Utilizar modelos que penalizam o classificador** ao errar a classe minoritária.
> 5. **Gerar dados artificialmente**, balanceando a classe.

Vamos detalhar cada uma.

---

### Solução 1: Coletar Dados de Forma Balanceada

> [!note] A ideia
> Se possível, **coletar** os dados já equilibrados — garantir desde a origem que as classes tenham proporções parecidas.

> [!tip] Nem sempre é possível
> Em fraude, doença rara, etc., a realidade já é desbalanceada — você não "fabrica" mais fraudes. Por isso as outras soluções existem.

---

### Solução 2: Amostras Estratificadas e Balanceadas

> [!note] A ideia
> **Havendo dados em abundância**, criar **amostras estratificadas e balanceadas** — selecionar subconjuntos que mantenham proporções iguais entre as classes.

> [!example] Exemplo
> De 1 milhão de transações (5% fraude), montar uma amostra de treino com **50% legítimas e 50% fraudes**, em vez de manter a proporção original.

---

### Solução 3: Métricas Apropriadas

> [!important] Não use só acurácia!
> Em datasets desbalanceados, use métricas que **expõem** o desempenho na classe minoritária:
> - **Recall** → o modelo está pegando os casos raros?
> - **F1-Score** → equilíbrio entre precisão e recall.
> - **AUC-ROC** → desempenho geral, robusto a desbalanceamento.
>
> (Todas detalhadas em [[05 - Avaliação de Performance e Matriz de Confusão]].)

---

### Solução 4: Modelos que Penalizam o Erro na Classe Minoritária

> [!note] A ideia
> Usar modelos (ou configurá-los) para **penalizar mais** o classificador quando ele **erra a classe minoritária**.

> [!tip] Como isso funciona
> É como dizer ao modelo: *"errar uma fraude é muito mais grave que errar uma transação legítima"*. Muitos algoritmos têm um parâmetro de "peso de classe" (`class_weight`) para isso. O modelo passa a "se esforçar mais" para acertar a classe rara.

---

### Solução 5: Gerar Dados Artificialmente

> [!note] A ideia
> Criar dados **artificiais** para equilibrar a classe minoritária. Há duas abordagens opostas:

```
   Dataset desbalanceado
        │
        ├─ UNDERSAMPLING → remove dados da classe MAIORITÁRIA
        │
        └─ OVERSAMPLING → cria dados da classe MINORITÁRIA
```

#### Undersampling

> [!note] Undersampling
> **Excluir dados** da classe com **maior presença** (a majoritária), até equilibrar com a minoritária.

> [!warning] Desvantagem
> Você **joga fora dados** — e dados são valiosos. Se a classe majoritária tinha informação útil, parte dela se perde.

#### Oversampling

> [!note] Oversampling
> **Produzir artificialmente** dados para a classe com **menor presença** (a minoritária), até equilibrar com a majoritária.

> [!tip] Vantagem
> Não joga dados fora. Mas é preciso **gerar** os dados novos de forma inteligente — é aqui que entra o SMOTE.

---

## 9.4. O Método SMOTE

> [!note] Definição
> **SMOTE** (Synthetic Minority Over-sampling Technique) é um método de **oversampling** que gera dados artificiais usando o **"vizinho mais próximo"** da classe minoritária.

> [!important] Como o SMOTE funciona
> Em vez de simplesmente **duplicar** instâncias da classe rara, o SMOTE:
> 1. Pega uma instância da classe minoritária.
> 2. Encontra seus **vizinhos mais próximos** (também da classe minoritária).
> 3. **Cria uma instância nova** num ponto **"entre"** a original e um vizinho.

```
   Antes do SMOTE          Depois do SMOTE
   (classe rara: 3 pontos)  (pontos sintéticos "entre" os reais)

   ●       ●                ●  ✦  ●
        ●                    ✦ ● ✦
                                ✦
   (✦ = instância sintética criada entre vizinhos)
```

> [!tip] Por que SMOTE é melhor que só duplicar?
> Duplicar instâncias só **repete** a mesma informação (e favorece overfitting). O SMOTE **cria variações novas e plausíveis**, "preenchendo" o espaço da classe minoritária de forma mais natural. Lembra a ideia de **vizinho mais próximo** do [[09 - Aprendizado Baseado em Instância e KNN|KNN]].

---

## 9.5. Exemplo em Python (notebook do curso)

O notebook `Unbal.ipynb` usou o **SMOTENC** (variante do SMOTE para dados com atributos categóricos) no dataset `credit_simple.csv`:

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTENC

credito = pd.read_csv("credit_simple.csv", sep=';')

# Verificar o desbalanceamento ANTES
count = credito.groupby(['CLASSE']).size()
print(count)   # mostra a diferença entre as classes

y = credito['CLASSE'].values
X = credito.iloc[:, :-1].values

# Codificar atributos categóricos
labelencoder = LabelEncoder()
for i in range(X.shape[1]):
    if X[:, i].dtype == 'object':
        X[:, i] = labelencoder.fit_transform(X[:, i])

# Aplicar SMOTE (versão SMOTENC, que lida com atributos categóricos)
# categorical_features indica QUAIS colunas são categóricas
sm = SMOTENC(random_state=0, categorical_features=[3, 5, 6])
X_res, y_res = sm.fit_resample(X, y)

# Verificar o balanceamento DEPOIS
df = pd.DataFrame({'CLASSE': y_res})
print(df.value_counts())   # agora as classes estão equilibradas!
```

> [!tip] Detalhes do código
> - A biblioteca é a **`imblearn`** (imbalanced-learn), especializada em desbalanceamento.
> - **`SMOTENC`** é a versão do SMOTE para datasets que **misturam atributos numéricos e categóricos** — o `categorical_features=[3,5,6]` diz quais colunas são categóricas.
> - Compare o `groupby` (antes) com o `value_counts` (depois): o SMOTE **equilibra** as classes gerando instâncias sintéticas.

---

## 9.6. Resumo das Soluções

| Solução | O que faz | Cuidado |
|---|---|---|
| Coletar balanceado | Equilibra na origem | Nem sempre possível |
| Amostra estratificada | Subconjunto balanceado | Precisa de dados em abundância |
| Métricas apropriadas | Recall, F1, AUC em vez de acurácia | — |
| Penalizar erro | Modelo "se esforça" na classe rara | — |
| **Undersampling** | Remove da classe maior | Perde dados |
| **Oversampling / SMOTE** | Cria dados da classe menor | SMOTE > duplicar |

---

## 9.7. Resumo

> [!summary] O essencial dos Datasets Desbalanceados
> - **Desbalanceado** = uma classe muito mais rara — e geralmente é **ela que importa** (fraude, doença).
> - Risco: o modelo prevê só a majoritária e tem **acurácia alta mas inútil**.
> - **Soluções**: coletar balanceado, amostra estratificada, **métricas apropriadas** (recall/F1/AUC), penalizar erro na classe rara, gerar dados.
> - **Undersampling** = remove da classe maior (perde dados).
> - **Oversampling** = cria dados da classe menor.
> - **SMOTE** = oversampling inteligente, cria instâncias sintéticas usando o **vizinho mais próximo**.

---

## 🔗 Próximos passos
- [[10 - AutoML e Tuning de Modelos]] — o último tópico: automatizar a busca pelo melhor modelo.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
