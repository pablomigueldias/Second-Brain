---
tags:
  - machine-learning
  - algoritmos
  - regressão-linear
  - regressão-múltipla
  - supervisionado
---

# 2. Regressão Linear - Condições e Regressão Múltipla

> [!info] O que esta nota cobre
> **Quando podemos confiar** num modelo de regressão (as condições que ele precisa atender), a diferença entre regressão **simples** e **múltipla**, e os cuidados ao usar várias variáveis: **colinearidade**, **parcimônia** e **R² ajustado**.

---

## 2.1. Condições para uma Boa Regressão

Antes de confiar num modelo de regressão, ele precisa passar por algumas verificações.

### Condição 1: Correlação Moderada ou Forte

> [!note] Regra
> A correlação entre as variáveis deve ser **moderada ou forte**. Correlações fracas não geram modelos confiáveis.

(Relembrando a tabela de força em [[01 - Correlação e Regressão Linear#1.3. Correlação (R)|força da correlação]].)

### Condição 2: Coeficiente de Determinação (R²) Adequado

> [!note] Faixas de R²
> | R² | Avaliação |
> |---|---|
> | **> 0,7** | ✅ Ótimo |
> | **0,3 a 0,7** | ⚠️ Zona intermediária (depende do contexto) |
> | **0 a 0,3** | ❌ Ruim |

### Condição 3: Resíduos Padronizados Próximos da Normal

> [!note] Regra
> Os **resíduos padronizados** devem estar **próximos de uma distribuição normal**.

Como verificar isso? Há **três formas**:

1. **Histograma** — desenhar o histograma dos resíduos e ver se tem o formato de "sino".
2. **Diagrama de normalidade** (Q-Q plot) — se os pontos seguem a linha diagonal, são normais.
3. **Teste de Shapiro-Wilk** — um teste estatístico formal de normalidade.

> [!tip] Por que resíduos normais importam?
> Se os resíduos seguem uma distribuição normal, isso indica que os erros do modelo são **aleatórios** (sem padrão escondido). Se NÃO são normais, provavelmente existe alguma relação que o modelo **não capturou**.

---

## 2.2. Regressão Simples vs. Múltipla

### Regressão Simples

> [!note] Definição
> **Uma única** variável explanatória para prever uma variável dependente.
>
> Notação: $Y \sim X$

> [!example] Exemplo
> Prever o custo do plano de saúde usando **apenas a idade**.

### Regressão Múltipla

> [!note] Definição
> **Duas ou mais** variáveis explanatórias para prever uma variável dependente.
>
> Notação: $Y \sim X_1 + X_2 + \dots + X_n$

> [!example] Exemplo
> Prever o custo do plano usando **idade + IMC + número de filhos + se é fumante**.

> [!tip] Por que usar várias variáveis?
> Na vida real, raramente um único fator explica tudo. Quanto mais variáveis relevantes, melhor o modelo costuma prever — **mas há armadilhas** (veja abaixo).

---

## 2.3. Analisar Cada X com Y

> [!important] Boa prática antes da regressão múltipla
> Antes de jogar tudo no modelo, analise **cada variável independente individualmente** contra Y:
> - **Gere gráficos de dispersão individuais** (cada X contra Y).
> - **Busque redundâncias** — variáveis que têm o **mesmo efeito** sobre Y.

Se duas variáveis explicam a **mesma coisa**, manter as duas só atrapalha. Isso nos leva aos dois conceitos seguintes.

---

## 2.4. Colinearidade

> [!warning] Definição
> **Colinearidade** = quando **duas variáveis independentes são correlacionadas entre si**.

> [!danger] Por que é um problema?
> Incluir variáveis independentes **colineares** pode **prejudicar o modelo**, criando **previsões não confiáveis**. O modelo "se confunde" sobre qual variável está realmente causando o efeito.

> [!example] Exemplo
> Prever o preço de uma casa usando `área em m²` E `área em pés²`. As duas dizem **exatamente a mesma coisa** — são perfeitamente colineares. Manter ambas não adiciona informação, só causa instabilidade.

> [!tip] Conexão
> Isso é parente da **Dummy Variable Trap** vista em [[07 - Codificação de Categorias]] no módulo de Fundamentos — ambos são casos de variáveis redundantes/correlacionadas.

---

## 2.5. Parcimônia

> [!note] Definição
> **Parcimônia** = **não colocar variáveis que não melhorem o modelo** em nada. O objetivo é criar **modelos parcimoniosos** — simples, enxutos, só com o que importa.

> [!tip] Princípio geral (Navalha de Occam)
> Entre dois modelos que explicam igualmente bem, **o mais simples é melhor**. Variáveis a mais aumentam a complexidade, o risco de overfitting e a dificuldade de interpretar.

---

## 2.6. R² Ajustado

> [!warning] O problema do R² na regressão múltipla
> Lembre que **R²** é o percentual de variação da variável de resposta explicado pelo modelo. **MAS**: quando se colocam **mais variáveis** no modelo, a tendência é que o **R² aumente** — **mesmo que a variável nova não melhore em nada** a precisão!

Ou seja, o R² **sempre sobe** ao adicionar variáveis, o que o torna **enganoso** para comparar modelos com números diferentes de variáveis.

### A solução: R² Ajustado

> [!note] Definição
> O **R² ajustado** ajusta a variação do modelo de acordo com o **número de variáveis independentes** incluídas. Ele "penaliza" variáveis inúteis.

> [!important] Propriedade-chave
> O **R² ajustado** será **sempre menor** que o **R²**.
>
> - Se você adiciona uma variável **útil** → R² ajustado **sobe**.
> - Se você adiciona uma variável **inútil** → R² ajustado **cai** (o R² comum subiria, mas o ajustado expõe a verdade).

> [!tip] Regra prática
> Para comparar modelos de regressão **múltipla** com quantidades diferentes de variáveis, **use o R² ajustado**, não o R² comum.

---

## 2.7. Requisitos Básicos (Resumo das Condições)

> [!important] Os dois requisitos fundamentais
> 1. **Linearidade** entre a variável dependente e as variáveis independentes (a relação tem que ser, de fato, aproximadamente uma reta).
> 2. **Pouca ou nenhuma colinearidade** entre as variáveis independentes.

### E os resíduos devem ser:

> [!note] Três propriedades dos bons resíduos
> 1. **Próximos da distribuição normal**.
> 2. Com **variância constante** em relação à linha de melhor ajuste (não podem "abrir" como um funil).
> 3. **Independentes** — sem padrão visível (se há padrão, o modelo deixou algo escapar).

```
   Resíduos BONS                 Resíduos RUINS (variância
   (espalhados ao acaso)         crescente - formato funil)

   res │ • •   •  •  •           res │        •      •
       │•   • •  • •  •              │     •      •  •
    0 ─┼──•──•──•──•──•──         0 ─┼──•──•──•──────────
       │ •  •  • •   • •              │  •  •   •     •
       │•  •   • •  •  •               │       •    •   •
       └──────────────▶                └──────────────────▶
```

---

## 2.8. Correlograma

> [!note] O que é
> Um **correlograma** é uma representação visual (geralmente um **mapa de calor / heatmap**) que mostra a **correlação entre todas as variáveis** ao mesmo tempo.

É a ferramenta perfeita para **detectar colinearidade** rapidamente: você olha o mapa e vê quais variáveis independentes estão muito correlacionadas entre si.

> [!example] Em Python (notebook do curso — `statsmodels`)
> ```python
> import seaborn as sns
>
> corr = base.corr()
> sns.heatmap(corr, cmap='coolwarm', annot=True, fmt='.2f')
> ```
> Isso desenha o correlograma com os valores de correlação anotados em cada célula.

---

## 2.9. Exemplo em Python: Comparando Modelos (statsmodels)

O notebook do curso mostrou como **comparar modelos** de regressão múltipla. Repare nos comentários com **AIC** e **BIC** — métricas onde **menor é melhor**:

```python
import statsmodels.formula.api as sm

# Modelo 1 → aic 156.6, bic 162.5  (melhor!)
# modelo = sm.ols(formula='mpg ~ wt + disp + hp', data=base)

# Modelo 2 → aic 165.1, bic 169.5
# modelo = sm.ols(formula='mpg ~ disp + cyl', data=base)

# Modelo 3 → aic 179.1, bic 183.5  (pior)
modelo = sm.ols(formula='mpg ~ drat + vs', data=base)
modelo = modelo.fit()
modelo.summary()
```

Depois, para verificar a **condição dos resíduos**:

```python
import scipy.stats as stats
import matplotlib.pyplot as plt

residuos = modelo.resid

# Verificação 1: Histograma dos resíduos
plt.hist(residuos, bins=20)
plt.title("Histograma de Resíduos")
plt.show()

# Verificação 2: Q-Q plot (diagrama de normalidade)
stats.probplot(residuos, dist="norm", plot=plt)
plt.title("Q-Q Plot de Resíduos")
plt.show()
```

> [!info] AIC e BIC (mencionados no notebook)
> São critérios que **equilibram qualidade do ajuste com simplicidade do modelo** — exatamente a ideia de **parcimônia**. **Quanto menores, melhor.** No exemplo, o modelo `mpg ~ wt + disp + hp` venceu por ter o menor AIC/BIC.

> [!note] Sobre o dataset `mtcars`
> O notebook usa o famoso dataset `mtcars` (carros). Algumas colunas: `mpg` (consumo, milhas/galão), `cyl` (cilindros), `disp` (cilindrada), `hp` (potência), `wt` (peso), `drat` (relação do eixo), `qsec` (desempenho), `vs` (tipo de motor), `am` (transmissão), `gear` (marchas), `carb` (carburadores).

---

## 2.10. Resumo

> [!summary] O essencial
> - Confie no modelo só se: correlação **moderada/forte**, **R² adequado**, resíduos **normais**.
> - **Simples** = 1 variável X. **Múltipla** = várias variáveis X.
> - **Colinearidade** = variáveis independentes correlacionadas entre si → prejudica o modelo.
> - **Parcimônia** = só inclua variáveis que ajudam de verdade.
> - **R² ajustado** > use ele (não o R² comum) para comparar modelos múltiplos — ele penaliza variáveis inúteis.
> - **Correlograma** = heatmap para detectar colinearidade.

---

## 🔗 Próximos passos
- [[03 - Cálculos da Regressão Linear]] — agora vamos ver as fórmulas matemáticas passo a passo.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
