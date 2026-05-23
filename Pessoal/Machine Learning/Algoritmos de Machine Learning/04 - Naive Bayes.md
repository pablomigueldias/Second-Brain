---
tags:
  - machine-learning
  - algoritmos
  - naive-bayes
  - classificação
  - probabilidade
  - supervisionado
---

# 4. Naive Bayes

> [!info] O que esta nota cobre
> O algoritmo **Naive Bayes**: como usar **probabilidade** para classificar. Vamos ver o **Teorema de Bayes** como base, como o modelo é construído a partir de dados históricos, o cálculo da **probabilidade posterior** passo a passo, e como lidar com valores contínuos.

---

## 4.1. A Ideia: Probabilidade para Classificação

> [!question] A pergunta
> Como usar **probabilidade** para prever um fato?

> [!note] A resposta
> Uma das opções é o **Teorema de Bayes**. A ideia é: **olhar dados históricos** e **calcular a chance** de a classe ser influenciada por determinados atributos.

### Como criar um modelo a partir de probabilidade?

> [!example] Exemplo intuitivo
> Se historicamente, **80% dos e-mails que contêm a palavra "grátis"** eram spam, então quando chega um e-mail novo com "grátis", há uma forte probabilidade de ser spam. Naive Bayes formaliza esse raciocínio.

### Duas abordagens probabilísticas

```
   Classificação probabilística
        │
        ├──▶ Naive Bayes      (esta nota)
        │
        └──▶ Redes Bayesianas (nota 05)
```

---

## 4.2. O Dataset de Exemplo: "Jogar ou não?"

Vamos usar o clássico dataset do tempo. A pergunta: **dado o clima, vamos jogar (play)?**

| outlook | temperature | humidity | windy | **play** |
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

São **14 instâncias**: **9 "yes"** e **5 "no"**.

> [!note] Por que "Naive" (ingênuo)?
> Naive Bayes assume que **todos os atributos são independentes entre si** — que `outlook`, `temperature`, `humidity` e `windy` não se influenciam. Na vida real isso raramente é 100% verdade (dias quentes costumam ter umidade baixa, por exemplo), mas o algoritmo **funciona surpreendentemente bem** mesmo com essa simplificação "ingênua".

---

## 4.3. Passo 1: Probabilidade Condicional da Classe

Primeiro, calculamos a probabilidade de cada classe **sem olhar nada** (probabilidade "a priori"):

| | Yes | No |
|---|---|---|
| Contagem | 9/14 | 5/14 |
| **Probabilidade** | **0,64** | **0,35** |

> Ou seja: sem saber nada sobre o dia, há 64% de chance de jogar e 35% de não jogar.

---

## 4.4. Passo 2: Probabilidade Condicional dos Atributos com a Classe

Agora, para **cada valor de cada atributo**, calculamos a probabilidade dele aparecer **dado** que a classe é "yes" ou "no".

### Tabela completa de probabilidades (o "modelo")

| Atributo | Valor | Yes | No | Yes (%) | No (%) |
|---|---|---|---|---|---|
| **outlook** | Sunny | 2/9 | 3/5 | 0,22 | 0,6 |
| | Overcast | 4/9 | 0/5 | 0,44 | 0 |
| | Rainy | 3/9 | 2/5 | 0,33 | 0,4 |
| **temperature** | Hot | 2/9 | 2/5 | 0,22 | 0,4 |
| | Mild | 4/9 | 2/5 | 0,44 | 0,4 |
| | Cool | 3/9 | 1/5 | 0,33 | 0,2 |
| **humidity** | High | 3/9 | 4/5 | 0,33 | 0,8 |
| | Normal | 6/9 | 1/5 | 0,66 | 0,2 |
| **windy** | TRUE | 3/9 | 3/5 | 0,33 | 0,6 |
| | FALSE | 6/9 | 2/5 | 0,66 | 0,4 |
| **(classe)** | | 9/14 | 5/14 | 0,64 | 0,35 |

> [!example] Como ler a tabela
> A linha `Sunny → Yes = 2/9 = 0,22` significa: *"dos 9 dias em que se jogou, apenas 2 eram ensolarados"*. Já `Sunny → No = 3/5 = 0,6` significa: *"dos 5 dias em que NÃO se jogou, 3 eram ensolarados"*.

> [!note] Esse é o "modelo treinado"
> Essa tabela **inteira** é o modelo do Naive Bayes. Treinar = construir essa tabela. Prever = usar essa tabela.

---

## 4.5. Passo 3: Cálculo da Probabilidade Posterior

> [!important] A regra de decisão
> Faz-se o cálculo da **probabilidade posterior** para **cada classe**. **A classe que tiver o maior valor "vence"** — é a previsão.

A probabilidade posterior de uma classe é o **produto** de: a probabilidade da classe **×** as probabilidades de cada atributo dado aquela classe.

---

### Exemplo de previsão 1: dia `sunny, hot, high, FALSE`

**Probabilidade YES:**
$$
P(\text{yes}) \times P(\text{sunny}|\text{yes}) \times P(\text{hot}|\text{yes}) \times P(\text{high}|\text{yes}) \times P(\text{FALSE}|\text{yes})
$$
$$
= 0{,}64 \times 0{,}22 \times 0{,}22 \times 0{,}33 \times 0{,}66 = \mathbf{0{,}006747}
$$

**Probabilidade NO:**
$$
P(\text{no}) \times P(\text{sunny}|\text{no}) \times P(\text{hot}|\text{no}) \times P(\text{high}|\text{no}) \times P(\text{FALSE}|\text{no})
$$
$$
= 0{,}35 \times 0{,}6 \times 0{,}4 \times 0{,}8 \times 0{,}4 = \mathbf{0{,}03}
$$

> [!summary] Decisão
> `NO (0,03)` > `YES (0,006747)` → o modelo prevê **NO** (não vai jogar). ☔

---

### Exemplo de previsão 2: dia `rainy, cool, normal, TRUE`

**Probabilidade YES:**
$$
0{,}64 \times 0{,}33 \times 0{,}33 \times 0{,}66 \times 0{,}33 = \mathbf{0{,}01518}
$$

**Probabilidade NO:**
$$
0{,}35 \times 0{,}4 \times 0{,}2 \times 0{,}2 \times 0{,}6 = \mathbf{0{,}00336}
$$

> [!summary] Decisão
> `YES (0,01518)` > `NO (0,00336)` → o modelo prevê **YES** (vai jogar). ⛅

> [!tip] Atenção: os valores não somam 1
> As probabilidades posteriores calculadas assim **não são probabilidades "reais"** que somam 100% — elas servem só para **comparar** qual classe é mais provável. Quem dá o maior número, vence. Para virar probabilidade real, seria preciso normalizar (dividir pela soma).

---

## 4.6. Lidando com Valores Contínuos

> [!warning] O problema
> O Naive Bayes da forma vista acima funciona com **atributos categóricos** (sunny, hot, etc.). Mas e atributos **numéricos contínuos** como idade, salário, temperatura exata?

Há **duas soluções**:

### Solução 1: Discretização

> [!note] O que é
> **Transformar valores contínuos em categorias** (faixas).

> [!example] Exemplo
> Transformar `idade` (número) em categorias: `Criança`, `Adulto`, `Idoso`.
> - 0–12 anos → "Criança"
> - 13–59 anos → "Adulto"
> - 60+ anos → "Idoso"

### Solução 2: Gaussian Naive Bayes

> [!note] O que é
> Converter o valor na probabilidade segundo a **distribuição normal (Gaussiana)**. Em vez de contar frequências, o algoritmo assume que cada atributo numérico segue uma curva normal e calcula a probabilidade a partir dela.

> Essa variante se chama **Gaussian Naive Bayes** — é a usada quando os dados são numéricos.

---

## 4.7. Exemplo em Python (notebook do curso)

O curso usou o `GaussianNB` do scikit-learn no dataset `insurance.csv`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Carregar dados
base = pd.read_csv("insurance.csv", keep_default_na=False)
base = base.drop(columns=['Unnamed: 0'])

# Separar X (atributos) e y (classe na coluna 7)
y = base.iloc[:, 7].values
X = base.drop(base.columns[7], axis=1).values

# Codificar atributos categóricos em números (Label Encoding)
labelencoder = LabelEncoder()
for i in range(X.shape[1]):
    if X[:, i].dtype == 'object':
        X[:, i] = labelencoder.fit_transform(X[:, i])

# Dividir em treino e teste (70/30)
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=12)

# Treinar o modelo Gaussian Naive Bayes
modelo = GaussianNB()
modelo.fit(X_treinamento, y_treinamento)

# Prever e avaliar
previsoes = modelo.predict(X_teste)
accuracy = accuracy_score(y_teste, previsoes)
print(f'Acurácia: {accuracy}')
```

> [!tip] Conexão com Fundamentos
> Repare que aqui aparecem conceitos do outro módulo: **Label Encoding** ([[07 - Codificação de Categorias]]), divisão **treino/teste** ([[04 - Classificação]]) e métricas como **acurácia, precisão, recall, F1** ([[05 - Avaliação de Performance e Matriz de Confusão]]).

---

## 4.8. Vantagens e Desvantagens

| ✅ Vantagens | ❌ Desvantagens |
|---|---|
| Simples e **rápido** de treinar | Assume **independência** entre atributos (raramente 100% verdade) |
| Funciona bem com **poucos dados** | Se um valor nunca apareceu com uma classe, a probabilidade vira 0 e "zera" tudo |
| Bom para **classificação de texto** (spam, sentimento) | Menos preciso que modelos mais complexos em alguns casos |
| Fácil de **interpretar** | |

---

## 4.9. Resumo

> [!summary] O essencial do Naive Bayes
> - Classifica usando **probabilidade** (Teorema de Bayes).
> - "Naive" = assume que os **atributos são independentes**.
> - **Treinar** = construir a tabela de probabilidades condicionais.
> - **Prever** = calcular a probabilidade posterior de cada classe; **a maior vence**.
> - Posterior = P(classe) × P(atributo₁|classe) × P(atributo₂|classe) × ...
> - Valores **contínuos** → discretizar **ou** usar **Gaussian Naive Bayes**.

---

## 🔗 Próximos passos
- [[05 - Redes Bayesianas]] — a evolução do Naive Bayes, que abandona a suposição de independência total.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
