---
tags:
  - machine-learning
  - tópicos-avançados
  - engenharia-de-atributos
  - pré-processamento
---

# 1. Engenharia de Atributos

> [!info] O que esta nota cobre
> A **Engenharia de Atributos** (feature engineering): o conjunto de técnicas para **manipular as características dos dados** e melhorar o modelo. Veremos as 5 grandes etapas — pré-processamento, codificação, dimensionamento, geração/extração e seleção.

---

## 1.1. O que é um Atributo?

> [!note] Definição
> Um **atributo** é uma **característica do negócio** que está sendo modelado.

> [!example] Exemplos
> Num modelo de crédito, atributos são: `idade`, `salário`, `histórico de pagamento`, `estado civil`... Cada coluna dos dados é um atributo.

---

## 1.2. O que é Engenharia de Atributos?

> [!important] Definição
> **Engenharia de Atributos** é **manipular as características** dos dados de forma a **melhorar o modelo**.

> [!tip] Por que isso importa tanto?
> Existe um ditado em ML: *"garbage in, garbage out"* (lixo entra, lixo sai). Por melhor que seja o algoritmo, se os dados estão mal preparados, o modelo será ruim. A engenharia de atributos costuma dar **mais ganho** que trocar de algoritmo.

---

## 1.3. As 5 Etapas da Engenharia de Atributos

```
   ENGENHARIA DE ATRIBUTOS
        │
        ├─ 1. Pré-processamento (faltantes, outliers)
        ├─ 2. Codificação de Categorias  ← ver Fundamentos
        ├─ 3. Dimensionamento de Características  ← ver Fundamentos
        ├─ 4. Geração e Extração de características (binning, PCA, datas)
        └─ 5. Seleção de Características Importantes
```

> [!note] Etapas que já foram vistas
> - **Etapa 2 (Codificação de Categorias)** → detalhada em [[07 - Codificação de Categorias]] (módulo Fundamentos).
> - **Etapa 3 (Dimensionamento)** → detalhada em [[08 - Dimensionamento de Características]] (módulo Fundamentos).
> - **Etapa 4 (PCA)** → ver [[02 - PCA - Redução de Dimensionalidade]].
> - **Etapa 5 (Seleção)** → ver [[03 - Seleção de Atributos]].
>
> Esta nota foca nas partes **novas**: pré-processamento e geração de características.

---

## 1.4. Etapa 1: Pré-processamento

### Tratamento de Valores Faltantes

> [!warning] O problema
> A **maioria dos classificadores não tolera** valores faltantes (campos vazios). É preciso resolver isso antes de treinar.

> [!note] Como lidar com valores faltantes
> 1. **Investigar se não existe uma causa "natural"** — às vezes o vazio significa algo (ex.: "sem renda" = desempregado, não erro).
> 2. **Excluir instâncias** — apagar as linhas com dados faltando (se forem poucas).
> 3. **Completar (imputar)** os valores faltantes:
>    - **Valores numéricos** → preencher com a **mediana**.
>    - **Valores categóricos** → preencher com a **moda** (valor mais frequente) ou com a categoria **"Outros"**.

> [!tip] Por que mediana e não média?
> A **mediana** é resistente a outliers. Se um valor extremo distorce a média, a mediana continua representando bem o "típico". Por isso é a escolha mais segura para preencher numéricos.

### Tratamento de Outliers

> [!note] Outliers
> **Outliers** são valores muito fora do padrão (extremamente altos ou baixos).

> [!warning] Não existe "regra geral"
> O tratamento de outliers **depende do contexto**. Uma regra conhecida:
> - Considerar outlier o que está além de **3 desvios padrão da média**.
> - Mas atenção: regras do negócio importam. Ex.: `idade`, `teto salarial` têm limites naturais que você já conhece.

> [!note] O que fazer com outliers
> - **Remover** o outlier (excluir a instância ou o valor).
> - **"Normalizar"** — substituir o valor extremo por algo mais razoável (ex.: pela mediana).

---

## 1.5. Etapa 4: Geração e Extração de Características

Aqui criamos **atributos novos** a partir dos existentes — frequentemente o passo que mais melhora o modelo.

### Binning

> [!note] O que é Binning
> **Binning** é agrupar valores em **faixas** (bins / caixas).

> [!info] Benefícios do binning
> 1. **Reduz a complexidade** das características.
> 2. **Melhora a performance** do modelo.
> 3. Pode ser usado em atributos **numéricos ou categóricos**.
> 4. Para categorias de **baixa cardinalidade** (raras), cria uma categoria **"outros"**.

> [!example] Exemplo de binning numérico
> Em vez de usar a `idade` exata (18, 19, 20, 21...), agrupar em faixas:
> - 0–17 → "menor"
> - 18–30 → "jovem"
> - 31–60 → "adulto"
> - 60+ → "idoso"

> [!example] Exemplo de binning categórico
> Se o atributo `propósito do empréstimo` tem categorias raras como "Eletrodomésticos" (2 casos) e "qualificação" (1 caso), agrupá-las em "outros" simplifica o modelo.

### Geração de Características a Partir de Datas

> [!warning] O problema com datas
> Para o modelo, uma **data** é só um **"texto"** — ele não entende `15/03/2024` como uma data.

> [!note] A solução: extrair informação da data
> Extraindo **"Mês"**, **"Ano"**, **"Feriado"**, **"Dia da Semana"** de uma data, o modelo pode **descobrir padrões** que estavam escondidos.

> [!example] Exemplo prático
> Vendas de uma loja podem ter padrões por **dia da semana** (sábado vende mais) ou por **mês** (dezembro dispara). Sem extrair esses campos, o modelo nunca enxergaria isso.

---

## 1.6. Exemplo em Python (notebook do curso)

O notebook `EngAtributos.ipynb` mostrou várias dessas técnicas no dataset `credit_simple.csv`:

```python
import pandas as pd

dataset = pd.read_csv('credit_simple.csv', sep=';')
y = dataset['CLASSE']
X = dataset.iloc[:, :-1]

# --- VALORES FALTANTES ---
# Numérico → preencher com a MEDIANA
mediana = X['SALDO_ATUAL'].median()
X['SALDO_ATUAL'].fillna(mediana, inplace=True)

# Categórico → preencher com a MODA (valor mais frequente)
X['ESTADOCIVIL'].fillna('masculino solteiro', inplace=True)

# --- OUTLIERS ---
# Identificar valores além de 2 desvios padrão e trocar pela mediana
desv = X['SALDO_ATUAL'].std()
mediana = X['SALDO_ATUAL'].median()
X.loc[X['SALDO_ATUAL'] >= 2 * desv, 'SALDO_ATUAL'] = mediana

# --- BINNING: categorias raras viram "outros" ---
X.loc[X['PROPOSITO'] == 'Eletrodomésticos', 'PROPOSITO'] = 'outros'
X.loc[X['PROPOSITO'] == 'qualificação', 'PROPOSITO'] = 'outros'

# --- GERAÇÃO A PARTIR DE DATAS ---
X['DATA'] = pd.to_datetime(X['DATA'], format='%d/%m/%Y')
X['ANO'] = X['DATA'].dt.year          # extrai o ano
X['MES'] = X['DATA'].dt.month         # extrai o mês
X['DIASEMANA'] = X['DATA'].dt.day_name()  # extrai o dia da semana
```

> [!tip] O que o código mostra
> Repare como uma única coluna `DATA` virou **3 atributos novos** (`ANO`, `MES`, `DIASEMANA`). Isso é geração de características na prática — dar ao modelo informação que estava "escondida".

---

## 1.7. Resumo

> [!summary] O essencial da Engenharia de Atributos
> - É **manipular as características** para melhorar o modelo — costuma dar mais ganho que trocar de algoritmo.
> - **5 etapas**: pré-processamento, codificação, dimensionamento, geração/extração, seleção.
> - **Faltantes**: investigar a causa; excluir, ou imputar (mediana p/ numérico, moda p/ categórico).
> - **Outliers**: regra dos 3 desvios padrão; remover ou normalizar.
> - **Binning**: agrupar valores em faixas; simplifica e melhora.
> - **Datas**: extrair ano, mês, dia da semana, feriado revela padrões escondidos.

---

## 🔗 Próximos passos
- [[02 - PCA - Redução de Dimensionalidade]] — quando há atributos **demais**, como comprimi-los.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
