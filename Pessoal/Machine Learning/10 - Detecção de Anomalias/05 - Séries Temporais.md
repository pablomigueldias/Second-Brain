---
tags:
  - machine-learning
  - detecção-anomalias
  - séries-temporais
  - arima
  - moving-average
---

# 5. Séries Temporais

> [!info] O que esta nota cobre
> Técnicas de **séries temporais** para detectar anomalias em dados que dependem do tempo: **Moving Average**, **Exponential Smoothing**, **Seasonal-Trend Decomposition** e **ARIMA**.

---

## 5.1. A ideia geral

> [!note] O padrão comum dessas técnicas
> A maioria funciona assim: **suavizar** a série para encontrar o "comportamento esperado", e então **comparar o valor real** com essa expectativa. Se a diferença ultrapassa um **limiar**, é anomalia.

---

## 5.2. Moving Average (Média Móvel)

> [!note] Como funciona
> **Suaviza** os dados calculando a **média em subconjuntos** (janelas) da série.

> [!important] Para detectar anomalias
> Compara-se o **valor real** com a **média móvel**. Se estiver **acima ou abaixo** de um parâmetro (limiar), é anomalia.
> ```
>   valor real ●        ← muito acima da média móvel = anomalia
>             ╱╲
>   ────────╱──╲────  (média móvel suavizada)
> ```

---

## 5.3. Exponential Smoothing (Suavização Exponencial)

> [!note] Como funciona
> Parecido com a média móvel, mas **atribui pesos que diminuem exponencialmente** para os dados mais antigos — ou seja, **dados mais recentes têm mais influência** sobre a média calculada.

> [!important] Para detectar anomalias
> Funciona como a média móvel: gera a suavização, compara com o valor real. Se a **diferença ultrapassa um limiar**, é anomalia.

> [!tip] Diferença para a média móvel
> A média móvel trata todos os pontos da janela **igualmente**. A suavização exponencial dá **mais peso ao recente** — reage mais rápido a mudanças. Bom quando o passado distante importa menos.

---

## 5.4. Seasonal and Trend Decomposition

> [!note] Como funciona
> Técnica que **decompõe** uma série temporal em **três componentes**:
> | Componente | O que é |
> |---|---|
> | **Tendência (Trend)** | a direção geral de longo prazo (subindo? descendo?) |
> | **Sazonalidade (Seasonality)** | padrões que se repetem em ciclos (ex.: vendas no Natal) |
> | **Resíduos (Residuals)** | o que sobra depois de remover tendência e sazonalidade |

> [!important] Onde mora a anomalia
> Depois de separar tendência e sazonalidade (que são esperadas), as **anomalias aparecem nos resíduos** — o "inexplicável". Um resíduo muito grande = anomalia.

---

## 5.5. ARIMA

> [!note] Definição
> O modelo **ARIMA** é composto por **três componentes**:
> - **AR (Autoregressivo):** usa valores **passados** da própria série para prever.
> - **I (Integrado):** **diferenciação** para tornar a série estacionária (remover tendência).
> - **MA (Média Móvel):** usa os **erros** de previsões passadas.

> [!tip] Como detecta anomalias
> O ARIMA **prevê** o próximo valor da série. Como nas LSTMs, se o valor real **diverge muito** da previsão, é sinal de anomalia. ARIMA é um clássico estatístico robusto para séries.

---

## 5.6. Esqueleto em Python

```python
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

serie = pd.read_csv("Salestrain.csv")["sales"]

# Média móvel
media_movel = serie.rolling(window=7).mean()
anomalias = serie[(serie - media_movel).abs() > limiar]

# ARIMA
modelo = ARIMA(serie, order=(1, 1, 1)).fit()   # (AR, I, MA)
previsao = modelo.forecast(steps=10)
```

> [!example] No curso
> Foram usados os arquivos `Salestrain.csv` e `Salestest.csv` para demonstrar essas técnicas em dados de vendas.

---

## 5.7. Resumo

> [!summary] O essencial
> - Padrão geral: **suavizar/prever → comparar com o real → diferença grande = anomalia**.
> - **Moving Average:** média em janelas (pesos iguais).
> - **Exponential Smoothing:** mais peso ao recente.
> - **Decomposição:** separa **tendência + sazonalidade + resíduos**; anomalia nos resíduos.
> - **ARIMA:** AR (passado) + I (diferenciação) + MA (erros); prevê e detecta desvios.

---

## 🔗 Próximos passos
- Fim do módulo de Anomalias! Volte ao [[00 - Índice]] ou siga para [[../11 - Algoritmos Genéticos/00 - Índice|Algoritmos Genéticos]].

---
[[00 - Índice|⬅️ Voltar ao Índice]]
