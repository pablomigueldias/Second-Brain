---
tags:
  - machine-learning
  - pré-processamento
  - normalização
  - padronização
  - feature-scaling
---

# 8. Dimensionamento de Características (Feature Scaling)

> [!info] O que esta nota cobre
> Como **colocar atributos numéricos em escalas comparáveis** antes do treino. As duas técnicas principais: **Padronização (Z-score)** e **Normalização (Min-Max)**, quando usar cada uma, e quando **não** usar.

---

## 8.1. Por que Dimensionar?

> [!warning] O problema
> Atributos numéricos podem estar em **escalas muito diferentes**. Isso faz com que eles **contribuam de forma desbalanceada** para o modelo.

### Dataset de exemplo

| House Size (sq. ft.) | Bedrooms | Distance to City (km) | Price (thousands) |
|---|---|---|---|
| 1800 | 3 | 10,5 | 250 |
| 2000 | 4 | 8,2 | 300 |
| 1500 | 2 | 15,0 | 200 |
| 2200 | 5 | 6,5 | 350 |
| 2400 | 4 | 7,8 | 375 |

Repare nas escalas:
- `House Size` → milhares (1500–2400)
- `Bedrooms` → unidades (2–5)
- `Distance` → unidades a dezenas (6,5–15)
- `Price` → centenas (200–375)

> [!example] O problema na prática
> Em modelos que usam **distância** (KNN, K-means, redes neurais), o atributo `House Size` vai **dominar** o cálculo simplesmente porque seus valores são gigantes comparados a `Bedrooms`. O modelo vai "ignorar" Bedrooms, mesmo que seja relevante.

---

## 8.2. O Que é Dimensionamento?

> [!note] Definição
> **Dimensionamento de Características** é o **processo de transformação de dados numéricos** para colocar todos em uma escala comparável.

### Por que isso ajuda?

1. **Variáveis em escalas diferentes contribuem de forma desbalanceada** → o dimensionamento equilibra a contribuição.
2. O **Gradient Descent** (algoritmo de otimização usado em muitos modelos, como regressão linear, redes neurais) **converge mais rapidamente** para o mínimo local quando os atributos estão na mesma escala.

> [!info] Curiosidade: Gradient Descent
> É o algoritmo que "afina" o modelo durante o treino, ajustando os parâmetros para minimizar o erro. Quando as features estão em escalas muito diferentes, ele "anda em zigue-zague" e demora muito a chegar no resultado.

---

## 8.3. Técnica 1: Padronização (Z-score)

> [!note] Definição
> **Padronização** transforma os dados para terem **média 0** e **desvio padrão 1**. Os valores ficam "próximos da média" da distribuição.

### Fórmula

$$
Z = \frac{x - \mu}{\sigma}
$$

Onde:
- $x$ = valor original
- $\mu$ = média do atributo
- $\sigma$ = desvio padrão do atributo

### Características

- ✅ Dados ficam **aproximadamente** com **média 0** e **desvio padrão 1**.
- ✅ Os valores transformados **podem ser negativos** (qualquer valor abaixo da média vira negativo).
- ✅ **Não afeta outliers** (eles continuam aparecendo como extremos).
- ✅ **Deve ser usada na maioria dos casos** — é o padrão da indústria.

### Quando usar
- Quando a distribuição dos dados é **aproximadamente normal** (ou pelo menos próxima disso).
- Para a maioria dos algoritmos: regressão linear, regressão logística, SVM, KNN, redes neurais.
- Quando você quer manter a influência de outliers no modelo.

---

## 8.4. Técnica 2: Normalização (Min-Max)

> [!note] Definição
> **Normalização Min-Max** transforma os dados para uma **escala fixa**, geralmente entre **0 e 1**.

### Fórmula

$$
X_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}
$$

Onde:
- $x$ = valor original
- $x_{min}$ = menor valor do atributo
- $x_{max}$ = maior valor do atributo

### Características

- ✅ Transforma os dados para uma **escala comum**, normalmente entre **0 e 1**.
- ✅ Usado em **processamento de imagens** (pixels já tem range 0-255 → vira 0-1) e **Redes Neurais Artificiais (RNA)**.
- ✅ Usar quando **não sabemos a distribuição** dos dados.
- ✅ Usar quando os dados **precisam ser positivos**.
- ⚠️ **Algoritmos não "requerem" dados normais** (não força distribuição normal).
- ⚠️ **Remove outliers** porque impõe **limites** (qualquer valor extremo é "achatado" para o mínimo ou máximo).

### Quando usar
- Em processamento de imagens.
- Em Redes Neurais (que costumam preferir entradas entre 0 e 1).
- Quando você sabe que os dados não têm distribuição normal.
- Quando outliers atrapalham mais do que ajudam.

---

## 8.5. Padronização vs. Normalização: Comparação Visual

Imagine os dados originais do **dataset IRIS** (famoso no ML, com características de flores). Aplicando as duas técnicas, temos algo assim:

```
   Original:           |---|---|--------|----------|---|---|
                       1   2   3        5          7   8   9

   Padronização:       ---|--|-----|-------|---|-----|---
                      -2 -1  0     1       2  3
                    (média = 0, desvio padrão = 1)

   Normalização:      |---|---|-----|------|----|----|
                      0   0,2 0,4   0,6   0,8   1
                      (sempre entre 0 e 1)
```

### Tabela-Resumo

| Aspecto | **Padronização (Z-score)** | **Normalização (Min-Max)** |
|---|---|---|
| Fórmula | $(x-\mu)/\sigma$ | $(x-x_{min})/(x_{max}-x_{min})$ |
| Range dos valores | Geralmente -3 a +3 | Tipicamente 0 a 1 |
| Pode ser negativo? | ✅ Sim | ❌ Não |
| Afeta outliers? | ❌ Não (mantém) | ✅ Sim (achata) |
| Distribuição preferida | Normal (ou próximo) | Qualquer (especialmente desconhecida) |
| Casos clássicos | Maioria dos algoritmos | Imagens, RNAs |

---

## 8.6. ⚠️ Quando NÃO Dimensionar

> [!warning] O dimensionamento NÃO é mágico
> Aplicar dimensionamento **não vai necessariamente melhorar seu modelo**. Há casos em que **não tem efeito** ou pode até atrapalhar.

### Casos para evitar

#### 1. Árvores de Decisão (e modelos baseados em árvores)

> [!note] Árvores não precisam de dimensionamento
> Algoritmos baseados em árvores (**Árvores de Decisão**, **Random Forest**, **XGBoost**, **LightGBM**, etc.) **não precisam** de nenhum tipo de dimensionamento.

**Por quê?** Porque árvores fazem **divisões** baseadas em comparações ("`House Size > 1800`?"). Não importa a escala — o que importa é se o valor está **acima ou abaixo** do ponto de corte. Mudar a escala não muda essas divisões.

#### 2. Atributos Categóricos Codificados

> [!warning] Não aplicar em One-Hot ou Label encoded
> O dimensionamento **não se aplica** a atributos categóricos já transformados (via Label Encoding ou One-Hot Encoding — veja [[07 - Codificação de Categorias]]).

**Por quê?** Esses valores **já são códigos** (0, 1, 2 ou colunas binárias). Padronizar/normalizar destruiria a representação. Imagine padronizar `Color_Red` (que é 0 ou 1) — vira algo sem sentido.

---

## 8.7. Fluxo Mental Recomendado

```
   Você tem atributos numéricos contínuos?
                  │
              ┌───┴───┐
             SIM    NÃO ──▶ Não precisa dimensionar
              │
              ▼
   Algoritmo é baseado em árvore?
              │
          ┌───┴───┐
         SIM    NÃO
          │      │
          ▼      ▼
   Não      Sabe a distribuição?
   precisa       │
            ┌────┴────┐
           SIM       NÃO
            │         │
            ▼         ▼
        Padronização Normalização
        (Z-score)   (Min-Max)
```

---

## 8.8. Resumo em Bullets

> [!summary] O essencial
> - **Dimensionar = colocar atributos numéricos na mesma escala.**
> - Ajuda algoritmos baseados em **distância** (KNN, K-means) e **gradiente** (regressão, redes neurais).
> - **Padronização (Z-score)** = média 0, desvio padrão 1. Padrão da indústria.
> - **Normalização (Min-Max)** = entre 0 e 1. Usada em imagens e redes neurais.
> - **Árvores de decisão NÃO precisam.**
> - **Atributos categóricos codificados NÃO devem ser dimensionados.**

---

## 🔗 Próximos passos
- [[09 - Agrupamentos (Clustering)]] — agora entrando no aprendizado **não supervisionado**.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
