---
tags:
  - machine-learning
  - regressão
  - métricas
  - avaliação
---

# 6. Avaliação de Performance para Regressão

> [!info] O que esta nota cobre
> Métricas para avaliar modelos de **regressão** — modelos que preveem **valores numéricos** (reais ou inteiros) em vez de categorias. As cinco métricas principais são: **ME**, **MAE**, **RMSE**, **MPE** e **MAPE**.

---

## 6.1. Contexto: O Que é Regressão?

> [!note] Lembrete
> **Regressão** = prever um **valor numérico**.

Exemplos:
- Prever o **preço de uma casa**.
- Prever a **temperatura amanhã**.
- Prever **vendas no próximo trimestre**.
- Prever **quanto tempo** um servidor vai durar.

Diferente da classificação, aqui não tem "acerto" ou "erro" puro — o que existe é **diferença** entre o **valor previsto** e o **valor real**. Quanto **menor a diferença**, melhor o modelo.

> [!tip] Onde usar essas métricas?
> - **Regressão clássica** (linear, polinomial, etc.)
> - **Regressão por Machine Learning** (random forests, XGBoost, redes neurais para regressão...)
> - **Séries Temporais** (previsão de demanda, finanças...)
> - Etc.

> [!warning] Princípio importante
> Métricas de erro devem ser **interpretadas no contexto** do problema e **em comparação com outras métricas**. Um erro de "5" pode ser ótimo prevendo o preço de uma casa, mas catastrófico prevendo nota de prova.

---

## 6.2. Dataset de Referência

Vamos usar a mesma tabela ao longo de todas as métricas (7 previsões):

| Previsto | Realizado |
|---|---|
| 3,34 | 3,00 |
| 4,18 | 4,00 |
| 3,00 | 3,00 |
| 2,99 | 3,00 |
| 4,51 | 4,50 |
| 5,18 | 4,00 |
| 8,18 | 4,50 |

Vamos calcular cada métrica com esses números.

---

## 6.3. ME — Mean Error (Erro Médio)

> [!note] O que mede
> A **média da diferença** entre o realizado e o previsto. Pode dar **negativo** ou **positivo**.

**Fórmula:**
$$
ME = \frac{1}{N} \sum_{i=1}^{N} (p_i - t_i)
$$

Onde $p_i$ é o previsto e $t_i$ é o realizado (target).

**Cálculo da diferença para cada linha:**

| Previsto | Realizado | Diferença ($p_i - t_i$) |
|---|---|---|
| 3,34 | 3,00 | -0,34 *(material original tem esse sinal)* |
| 4,18 | 4,00 | -0,18 |
| 3,00 | 3,00 | 0 |
| 2,99 | 3,00 | 0,01 |
| 4,51 | 4,50 | -0,01 |
| 5,18 | 4,00 | -1,18 |
| 8,18 | 4,50 | -3,68 |
| **Soma** |  | **-5,38** |

$$
ME = \frac{-5{,}38}{7} = -0{,}76
$$

### Características do ME

- 🟡 **Dependente de escala**: o valor depende da escala dos seus dados.
- 🟡 **Pode ser qualquer número real** (positivo, negativo ou zero).

### Interpretação do exemplo

> [!summary] ME ≈ −0,76 (ou pense em outro exemplo do material: -2)
> Um valor negativo significa que o modelo está prevendo, em média, **valores menores** que o real — ele está **subestimando**.
>
> **Exemplo:** se ME = -2 numa previsão de notas, o modelo prevê em média **2 unidades a menos** do que a nota real.

### ⚠️ Problema do ME

> [!warning] O grande risco
> Erros **positivos** e **negativos** se **cancelam**! Um modelo que prevê +10 numa instância e -10 em outra teria ME = 0, fingindo estar perfeito quando na verdade erra muito.
>
> Por isso normalmente preferimos **MAE** ou **RMSE**, que não têm esse problema.

---

## 6.4. MAE — Mean Absolute Error (Erro Médio Absoluto)

> [!note] O que mede
> A média da **diferença absoluta** (em valor) entre o realizado e o previsto. Ignora o sinal.

**Fórmula:**
$$
MAE = \frac{1}{N} \sum_{i=1}^{N} |p_i - t_i|
$$

**Cálculo:**

| Previsto | Realizado | \|Dif.\| |
|---|---|---|
| 3,34 | 3,00 | 0,34 |
| 4,18 | 4,00 | 0,18 |
| 3,00 | 3,00 | 0 |
| 2,99 | 3,00 | 0,01 |
| 4,51 | 4,50 | 0,01 |
| 5,18 | 4,00 | 1,18 |
| 8,18 | 4,50 | 3,68 |
| **Soma** |  | **5,40** |

$$
MAE = \frac{5{,}40}{7} \approx 0{,}77
$$

### Características do MAE

- 🟡 **Dependente de escala**.
- ✅ Sempre **≥ 0** (nunca negativo).
- ✅ **Não cancela erros**.

### Interpretação

> [!summary] MAE ≈ 0,77 (ou ex. = 3 do material)
> O modelo erra, **em média, 0,77 unidades** (na mesma escala dos dados).
>
> **Exemplo:** MAE = 3 numa previsão de temperatura significa que, em média, o modelo erra **3 °C**.

> [!tip] Quando usar MAE
> Quando você quer um erro **fácil de explicar** ("o modelo erra X unidades em média") e **não quer punir** erros grandes mais do que erros pequenos.

---

## 6.5. RMSE — Root Mean Squared Error (Raiz do Erro Quadrático Médio)

> [!note] O que mede
> Mais ou menos como o MAE, mas **eleva os erros ao quadrado** antes de tirar a média, e depois tira a raiz quadrada. Isso faz com que **erros grandes pesem muito mais** que erros pequenos.

**Fórmula:**
$$
RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (p_i - t_i)^2}
$$

**Cálculo:**

| Previsto | Realizado | Dif. ao quadrado |
|---|---|---|
| 3,34 | 3,00 | 0,1156 |
| 4,18 | 4,00 | 0,0324 |
| 3,00 | 3,00 | 0 |
| 2,99 | 3,00 | 0,0001 |
| 4,51 | 4,50 | 0,0001 |
| 5,18 | 4,00 | 1,3924 |
| 8,18 | 4,50 | 13,5424 |
| **Soma** |  | **15,083** |

$$
RMSE = \sqrt{\frac{15{,}083}{7}} = \sqrt{2{,}155} \approx 1{,}46
$$

### Características do RMSE

- ✅ Sempre **≥ 0**.
- ✅ **Pune muito mais** os erros grandes (porque eleva ao quadrado).
- 📝 No material aparece como "**independente de escala**", mas na prática o RMSE também depende da escala dos dados — apenas é menos volátil que o ME.

### Interpretação

> [!summary] RMSE ≈ 1,46 (ou ex. = 4 do material)
> O modelo tem um **erro médio ponderado** de 1,46 unidades (com mais peso para os erros grandes).

> [!tip] MAE vs. RMSE — qual usar?
> - **MAE** = média "honesta" do erro. Todos os erros pesam igual.
> - **RMSE** = média que **destaca outliers** (erros grandes).
> - Se erros grandes são particularmente ruins no seu problema (ex.: previsão de demanda crítica), prefira **RMSE**.
> - Se você quer uma medida fácil de explicar, **MAE**.

---

## 6.6. MPE — Mean Percentage Error (Erro Percentual Médio)

> [!note] O que mede
> A diferença **em percentual** entre realizado e previsto. Como o ME, **pode ser negativo**.

**Fórmula:**
$$
MPE = \frac{1}{N} \sum_{i=1}^{N} \frac{(t_i - p_i)}{t_i} \times 100
$$

**Cálculo:**

| Previsto | Realizado | Erro % |
|---|---|---|
| 3,34 | 3,00 | -11,33% |
| 4,18 | 4,00 | -4,50% |
| 3,00 | 3,00 | 0% |
| 2,99 | 3,00 | 0,33% |
| 4,51 | 4,50 | -0,22% |
| 5,18 | 4,00 | -29,50% |
| 8,18 | 4,50 | -81,78% |
| **Soma** |  | **-126,78%** |

$$
MPE = \frac{-126{,}78\%}{7} \approx -18{,}11\%
$$

### Características do MPE

- ✅ **Independente de escala** (é percentual).
- 🟡 **Pode ser negativo**.
- ⚠️ Erros positivos e negativos **se cancelam** (mesma armadilha do ME).

### Interpretação

> [!summary] MPE ≈ -18,11% (ou ex. = -5% do material)
> Um valor negativo significa que o modelo está **superestimando** os valores reais em média (depende da convenção; aqui, com a fórmula apresentada, negativo = previsão maior que o real).
>
> **Exemplo do material:** MPE = -5% → o modelo **subestima**, em média, 5% dos valores reais.
> *(O sinal depende da convenção da fórmula — atente-se à interpretação no seu material.)*

---

## 6.7. MAPE — Mean Absolute Percentage Error (Erro Absoluto Percentual Médio)

> [!note] O que mede
> A diferença **absoluta percentual** entre o realizado e o previsto. É o MPE sem o problema do sinal.

**Fórmula:**
$$
MAPE = \frac{1}{N} \sum_{i=1}^{N} \frac{|p_i - t_i|}{|t_i|}
$$

(Em geral multiplicada por 100 para virar percentual.)

**Cálculo:**

| Previsto | Realizado | \|Erro %\| |
|---|---|---|
| 3,34 | 3,00 | 0,1133 (11,33%) |
| 4,18 | 4,00 | 0,045 (4,5%) |
| 3,00 | 3,00 | 0 |
| 2,99 | 3,00 | 0,0033 (0,33%) |
| 4,51 | 4,50 | 0,0022 (0,22%) |
| 5,18 | 4,00 | 0,295 (29,5%) |
| 8,18 | 4,50 | 0,8178 (81,78%) |
| **Soma** |  | **1,2766** |

$$
MAPE = \frac{1{,}2766}{7} \approx 0{,}18 \, (\approx 18\%)
$$

### Características do MAPE

- ✅ **Independente de escala** (percentual).
- ✅ Sempre **≥ 0**.
- ✅ **Fácil de interpretar** ("erra X% em média").
- ⚠️ **Problema**: explode quando $t_i$ é zero ou muito pequeno.

### Interpretação

> [!summary] MAPE ≈ 18% (ou ex. = 8% do material)
> O modelo erra, **em média, 18% do valor real**.

> [!tip] MAPE = a métrica mais "comunicável"
> É a favorita de pessoas de negócio porque a explicação é simples: "o modelo erra 8%". Sem precisar conhecer a escala dos dados.

---

## 6.8. Tabela-Resumo Geral

| Métrica | Nome | Escala? | Pode ser negativo? | Pune erros grandes? | Pra que serve |
|---|---|---|---|---|---|
| **ME** | Erro Médio | Dependente | ✅ Sim | ❌ Não | Detectar **viés** (modelo super/subestima) |
| **MAE** | Erro Médio Absoluto | Dependente | ❌ Não | ❌ Não | Erro médio "honesto" |
| **RMSE** | Raiz do Erro Quad. Médio | Dependente | ❌ Não | ✅ **Sim** (muito) | Quando outliers importam |
| **MPE** | Erro Percentual Médio | Independente (%) | ✅ Sim | ❌ Não | Detectar viés em % |
| **MAPE** | Erro Abs. Percentual Médio | Independente (%) | ❌ Não | ❌ Não | Comunicar erro em % |

---

## 6.9. Dicas Práticas

> [!tip] Como escolher a métrica?
> 1. **Reportar uma só? → MAE ou MAPE** (mais fáceis de explicar).
> 2. **Outliers são problema? → RMSE** (pune fortemente).
> 3. **Quer saber se o modelo super/subestima? → ME ou MPE** (mostram a direção do erro).
> 4. **Quer comparar entre datasets de escalas diferentes? → MAPE** (em %).

> [!warning] Nunca olhe só uma métrica
> Reportar **várias métricas juntas** dá uma visão muito mais honesta do desempenho.

---

## 🔗 Próximos passos
- [[07 - Codificação de Categorias]] — antes de treinar qualquer modelo, precisamos transformar dados categóricos em números.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
