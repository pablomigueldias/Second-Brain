---
tags:
  - machine-learning
  - algoritmos
  - regressão-linear
  - cálculos
  - supervisionado
---

# 3. Cálculos da Regressão Linear

> [!info] O que esta nota cobre
> O **passo a passo matemático** para construir uma regressão linear simples: calcular a **correlação de Pearson**, a **inclinação**, a **interceptação** e, finalmente, fazer a **previsão**. Tudo com o mesmo exemplo numérico.

> [!tip] Antes de começar
> Esta nota é a parte "mão na massa" de [[01 - Correlação e Regressão Linear]]. Se os conceitos (correlação, inclinação, etc.) ainda estão confusos, revise aquela nota primeiro.

---

## 3.1. O Dataset de Exemplo

Vamos usar este conjunto de 11 pacientes (idade × custo):

| Idade | Custo |
|---|---|
| 18 | 871 |
| 23 | 1100 |
| 25 | 1393 |
| 33 | 1654 |
| 34 | 1915 |
| 43 | 2100 |
| 48 | 2356 |
| 51 | 2698 |
| 58 | 2959 |
| 63 | 3000 |
| 67 | 3100 |

O objetivo é construir a reta `Custo = Interceptação + (Inclinação × Idade)`.

A construção tem **4 etapas**:

```
   1. Correlação  →  2. Inclinação  →  3. Interceptação  →  4. Previsão
```

---

## 3.2. Etapa 1: Correlação de Pearson

> [!note] O que é
> A **correlação de Pearson** mede a força e direção da relação linear. É o "R" visto em [[01 - Correlação e Regressão Linear]].

### Fórmula

$$
r = \frac{\text{cov}(x, y)}{\sigma_x \cdot \sigma_y}
$$

Onde:
- $\text{cov}(x, y)$ = **covariância** entre x e y (o quanto variam juntas)
- $\sigma_x$ = desvio padrão de x
- $\sigma_y$ = desvio padrão de y

> [!info] Versão equivalente usada no material
> O material também apresenta a fórmula na forma de somatórios. A ideia é a mesma: dividir o "quanto variam juntas" pelo "quanto cada uma varia sozinha". O resultado é um número entre **-1 e 1**.

### Resultado no exemplo

Aplicando a fórmula aos dados de idade × custo:

$$
r \approx 0{,}9879
$$

> [!summary] Interpretação
> Uma correlação de **0,99** é praticamente **perfeita e positiva** — idade e custo crescem juntas, de forma quase linear. Excelente sinal para fazer regressão.

---

## 3.3. Etapa 2: Inclinação (m)

> [!note] O que é
> A **inclinação** diz **quanto Y sobe** para cada unidade que X aumenta.

### Fórmula

$$
m = r \times \frac{\sigma_y}{\sigma_x}
$$

Onde:
- $r$ = correlação (já calculada: 0,9879)
- $\sigma_y$ = desvio padrão de Y (custo)
- $\sigma_x$ = desvio padrão de X (idade)

### Cálculo no exemplo

Com os desvios padrão dos dados:

$$
m = 0{,}9879 \times \frac{751{,}62}{15{,}99} \approx 46{,}45
$$

> [!summary] Interpretação
> A inclinação de **≈ 46,45** significa: a cada **1 ano a mais** de idade, o custo do plano sobe **≈ R$ 46,45**.

---

## 3.4. Etapa 3: Interceptação (b)

> [!note] O que é
> A **interceptação** é o valor de Y quando **X = 0** — onde a reta "corta" o eixo Y.

### Fórmula

$$
b = \bar{y} - m \times \bar{x}
$$

Onde:
- $\bar{y}$ = média de Y (custo)
- $\bar{x}$ = média de X (idade)
- $m$ = inclinação (já calculada: 46,45)

### Cálculo no exemplo

Com as médias dos dados ($\bar{y} \approx 2104{,}18$ e $\bar{x} \approx 42{,}09$):

$$
b = 2104{,}18 - 46{,}45 \times 42{,}09 \approx 149{,}13
$$

> [!summary] Interpretação
> A interceptação de **≈ 149,13** é o valor "base" da reta. Sozinha ela tem pouco sentido prático (uma pessoa com 0 anos), mas é essencial para posicionar a reta corretamente.

---

## 3.5. Etapa 4: Previsão

> [!important] A fórmula final da reta
> $$ y = b + (m \times x) $$
>
> Ou, em palavras:
> $$ \text{Previsão} = \text{Interceptação} + (\text{Inclinação} \times \text{Valor a prever}) $$

### Cálculo no exemplo: prever o custo para 54 anos

$$
y = 149{,}13 + (46{,}45 \times 54)
$$
$$
y = 149{,}13 + 2508{,}30
$$
$$
y \approx 2657{,}43
$$

> [!summary] Resultado
> O modelo prevê que um paciente de **54 anos** terá um custo de aproximadamente **R$ 2.657,43**.

---

## 3.6. O Processo Completo em um Diagrama

```
   DADOS (idade, custo)
        │
        ▼
   ┌─────────────────────────────────────┐
   │ 1. CORRELAÇÃO (r)                    │
   │    r = cov(x,y) / (σx · σy)          │
   │    → r ≈ 0,99                        │
   └─────────────────────────────────────┘
        │
        ▼
   ┌─────────────────────────────────────┐
   │ 2. INCLINAÇÃO (m)                    │
   │    m = r · (σy / σx)                 │
   │    → m ≈ 46,45                       │
   └─────────────────────────────────────┘
        │
        ▼
   ┌─────────────────────────────────────┐
   │ 3. INTERCEPTAÇÃO (b)                 │
   │    b = ȳ - m · x̄                     │
   │    → b ≈ 149,13                      │
   └─────────────────────────────────────┘
        │
        ▼
   ┌─────────────────────────────────────┐
   │ 4. PREVISÃO                          │
   │    y = b + (m · x)                   │
   │    → para x=54: y ≈ 2657             │
   └─────────────────────────────────────┘
```

---

## 3.7. Conferindo com o Código Python

Esta é exatamente a lógica da classe `LinearRegression` do notebook do curso (veja [[01 - Correlação e Regressão Linear#1.8. Exemplo em Python (do notebook do curso)|nota 01]]):

```python
def __correlacao(self):           # Etapa 1
    covariacao = cov(self.x, self.y, bias=True)[0][1]
    variancia_x = var(self.x)
    variancia_y = var(self.y)
    return covariacao / sqrt(variancia_x * variancia_y)

def __inclinacao(self):           # Etapa 2
    return self.__correlation_coefficient * (std(self.y) / std(self.x))

def __interceptacao(self):        # Etapa 3
    return mean(self.y) - mean(self.x) * self.__inclination

def previsao(self, valor):        # Etapa 4
    return self.__intercept + (self.__inclination * valor)
```

> [!tip] Conexão código ↔ fórmula
> Cada método do código é **exatamente uma das 4 etapas** desta nota. Ler o código junto com as fórmulas é uma ótima forma de fixar.

---

## 3.8. Resumo

> [!summary] As 4 fórmulas para decorar
> 1. **Correlação**: $r = \dfrac{\text{cov}(x,y)}{\sigma_x \cdot \sigma_y}$
> 2. **Inclinação**: $m = r \cdot \dfrac{\sigma_y}{\sigma_x}$
> 3. **Interceptação**: $b = \bar{y} - m \cdot \bar{x}$
> 4. **Previsão**: $y = b + (m \cdot x)$
>
> A ordem importa: cada etapa usa o resultado da anterior.

---

## 🔗 Próximos passos
- [[04 - Naive Bayes]] — saindo da regressão e entrando nos algoritmos de **classificação**, começando pelos probabilísticos.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
