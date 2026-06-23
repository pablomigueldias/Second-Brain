---
tags:
  - machine-learning
  - detecção-anomalias
  - estatística
  - z-score
  - iqr
---

# 2. Técnicas Estatísticas

> [!info] O que esta nota cobre
> As técnicas **estatísticas** de detecção de anomalias: **Z-Score**, **Modified Z-Score** e o **IQR Method**. São as mais simples e o ponto de partida natural.

---

## 2.1. Z-Score

> [!note] A ideia
> O **Z-Score** mede **quantos desvios-padrão** um valor está em relação à **média**. Definimos um limite: além de tantos desvios, é anomalia.

> [!important] Fórmula
> $$ Z = \frac{X - \mu}{\sigma} $$
> Onde **X** = o valor, **μ** = a média, **σ** = o desvio-padrão.

> [!example] Limite típico
> Um critério comum: **Z-Score > 3**. Ou seja, qualquer ponto a **mais de 3 desvios-padrão** da média é considerado anomalia.
> ```
>        média (μ)
>   ✗      |       ✗
>   ◄──3σ──┼──3σ──►
>   anomalia  normal  anomalia
> ```

> [!warning] Limitação
> O Z-Score usa **média e desvio-padrão**, que são **sensíveis a outliers** — ironicamente, os próprios valores extremos distorcem a média/desvio que deveriam detectá-los. Daí a variante a seguir.

---

## 2.2. Modified Z-Score

> [!note] A correção
> Variação do Z-Score que usa a **mediana** e o **Desvio Absoluto da Mediana (MAD)** em vez da média e do desvio-padrão — porque a **mediana é robusta a outliers**.

> [!important] Fórmula
> $$ M = 0{,}6745 \times \frac{X - \text{Med}}{\text{MAD}} $$
> Onde **Med** = mediana, **MAD** = *Median Absolute Deviation*. (O `0,6745` ajusta a escala para se aproximar do Z-Score normal.)

> [!tip] Quando preferir
> Use o **Modified Z-Score** quando os dados já têm outliers fortes que estragariam a média — ele "enxerga" melhor porque a mediana não se deixa puxar pelos extremos.

---

## 2.3. IQR Method (Intervalo Interquartil)

> [!note] A ideia
> Usa os **quartis** dos dados. O **IQR** é a faixa entre o **1º quartil (Q1, 25%)** e o **3º quartil (Q3, 75%)**:
> $$ IQR = Q3 - Q1 $$

> [!important] Regra dos outliers
> É anomalia (outlier) o valor que está:
> - **abaixo de** `Q1 − 1,5 × IQR`, **ou**
> - **acima de** `Q3 + 1,5 × IQR`.
>
> ```
>   ✗   |---[ Q1 ====== Q3 ]---|   ✗
>       └ Q1-1.5·IQR    Q3+1.5·IQR ┘
>   outlier   normal       outlier
> ```

> [!example] É o mesmo critério do "boxplot"
> Aquelas "bolinhas" que aparecem fora dos bigodes de um boxplot são exatamente os outliers detectados pelo método IQR. Também é **robusto a outliers** (usa quartis, não a média).

---

## 2.4. Esqueleto em Python

```python
import numpy as np

# Z-Score
z = (X - np.mean(X)) / np.std(X)
anomalias_z = X[np.abs(z) > 3]

# IQR
Q1, Q3 = np.percentile(X, [25, 75])
IQR = Q3 - Q1
limite_inf, limite_sup = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
anomalias_iqr = X[(X < limite_inf) | (X > limite_sup)]
```

---

## 2.5. Resumo

> [!summary] O essencial
> - **Z-Score:** desvios-padrão da **média** (`Z = (X−μ)/σ`); limite típico > 3. Sensível a outliers.
> - **Modified Z-Score:** usa **mediana e MAD** (robusto a outliers).
> - **IQR Method:** outlier fora de `[Q1 − 1,5·IQR, Q3 + 1,5·IQR]` (o critério do boxplot).
> - Métodos baseados em **mediana/quartis** são mais robustos que os baseados em média.

---

## 🔗 Próximos passos
- [[03 - Machine Learning para Anomalias]] — quando a estatística simples não basta e precisamos de modelos.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
