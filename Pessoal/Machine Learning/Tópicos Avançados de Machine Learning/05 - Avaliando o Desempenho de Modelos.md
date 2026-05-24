---
tags:
  - machine-learning
  - tópicos-avançados
  - avaliação
  - teste-de-hipótese
  - estatística
---
 
# 5. Avaliando o Desempenho de Modelos

> [!info] O que esta nota cobre
> Como **comparar dois modelos** de forma estatisticamente rigorosa. Quando o modelo A dá 78% e o B dá 80%, essa diferença de 2% é **real** ou é **acaso**? A resposta vem do **Teste de Hipótese comparando duas médias**.

---

## 5.1. Cenário: Qual Modelo Escolher?

> [!example] A situação
> Você busca o modelo com melhor desempenho. No primeiro teste:
> - **Naive Bayes** → desempenho de **78%**.
> - **Multilayer Perceptron (MLP)** → desempenho de **80%**.
>
> Mas o **custo computacional** é bem diferente:
> - **Naive Bayes** → cria o modelo em **3 minutos**.
> - **Multilayer Perceptron** → cria o modelo em **2 horas**.

### O dilema

> [!question] A pergunta
> Existe **diferença estatisticamente significante** entre os modelos (78% vs. 80%), ou essa diferença é **devida ao acaso**?
>
> - Se os **2% forem reais** → vale a pena usar o MLP (mais lento, mas melhor).
> - Se for **acaso** → usar o Naive Bayes (muito mais rápido, e igualmente bom).

> [!important] Por que isso importa
> 2% pode parecer pequeno, mas a decisão muda **completamente** o projeto: 3 minutos vs. 2 horas de treino é uma diferença enorme em custo. Precisamos ter **certeza estatística** antes de decidir.

---

## 5.2. A Solução: Teste de Hipótese Comparando Duas Médias

> [!note] A ideia
> Vamos usar um **Teste de Hipótese comparando duas médias populacionais** para decidir se a diferença é real.

### Passo 1: Coletar amostras

> [!important] Criar vários modelos
> Primeiro, coletamos **amostras aleatórias** dos dois casos: criamos **vários modelos** de cada algoritmo e anotamos os resultados. No exemplo: **40 testes com cada algoritmo**.

> [!example] Resultados parciais
> | Naive Bayes | Multilayer Perceptron |
> |---|---|
> | 78 | 80 |
> | 78 | 79 |
> | 78 | 82 |
> | 79 | 79 |
> | 80 | 80 |
> | 79 | 79 |
> | 82 | 78 |
> | ... | ... |

> [!warning] Atenção: aleatoriedade é obrigatória
> Você precisa usar um **processo aleatório** de geração dos dados de treino/teste para cada modelo. **Caso contrário, todos os modelos terão exatamente o mesmo resultado** — e não haveria o que comparar.

---

## 5.3. Os Ingredientes do Teste

Considerando **x = Naive Bayes** e **y = Multilayer Perceptron**, calculamos:

> [!example] Estatísticas das amostras
> | Estatística | Naive Bayes (x) | MLP (y) |
> |---|---|---|
> | **Média** | 79,2 | 79,8 |
> | **Desvio padrão** | 2,61 | 2,31 |
> | **Tamanho da amostra** | 40 | 40 |

---

## 5.4. A Hipótese Nula

> [!note] Hipótese Nula (H₀)
> A **hipótese nula** é que a **diferença entre as médias das duas populações é igual a zero**:
> $$ \mu_x - \mu_y = 0 $$

> [!tip] O que isso significa
> A hipótese nula é a posição "cética": *"não há diferença real entre os modelos; qualquer diferença observada é só acaso"*. O teste vai decidir se temos **evidência suficiente para rejeitar** essa hipótese.

---

## 5.5. Calculando a Estatística de Teste

### Passo 1: Diferença entre as médias

$$
\bar{x} - \bar{y} = 79{,}2 - 79{,}8 = -0{,}6
$$

### Passo 2: Erro padrão

A fórmula combina os desvios padrão das duas amostras:

$$
\text{Erro Padrão} = \sqrt{\frac{\sigma_x^2}{n_x} + \frac{\sigma_y^2}{n_y}}
$$

$$
= \sqrt{\frac{2{,}61^2}{40} + \frac{2{,}31^2}{40}} \approx 0{,}54
$$

### Passo 3: Dividir a diferença das médias pelo erro padrão

$$
\text{Estatística} = \frac{-0{,}6}{0{,}54} \approx -1{,}11
$$

> [!note] O que é essa estatística
> Esse valor (≈ 1,11 em módulo) diz **quantos "erros padrão"** as médias estão distantes uma da outra. Quanto maior, mais "significativa" a diferença.

---

## 5.6. Obtendo o Valor-p

### Passo 1: Consultar a tabela Z

> [!example] Procurando na tabela
> Procurar **1,11** na tabela Z → resultado: **0,1335**.

### Passo 2: Teste bicaudal

> [!note] Teste "não igual" (bicaudal)
> Como queremos saber se as médias são **diferentes** (em qualquer direção), o teste é **bicaudal** — multiplicamos o valor por 2:
> $$ p = 2 \times 0{,}1335 = 0{,}267 $$

> [!tip] Bicaudal vs. unicaudal
> - **Bicaudal** → "as médias são **diferentes**?" (não importa qual é maior).
> - **Unicaudal** → "a média de A é **maior** que a de B?" (direção específica).
> Aqui usamos bicaudal porque a pergunta é só "há diferença?".

---

## 5.7. A Decisão: Valor-p vs. Alfa

> [!note] O nível de significância (Alfa)
> Definimos **Alfa = 0,05** (5%). Esse é o "limite" para decidir.

### A regra de decisão

> [!important] Como decidir
> - Se **valor-p < Alfa** → a diferença é **significativa** (rejeitamos H₀).
> - Se **valor-p > Alfa** → a diferença **não é significativa** (não rejeitamos H₀).

### No nosso caso

$$
\text{Valor-p} = 0{,}267 \qquad > \qquad \text{Alfa} = 0{,}05
$$

---

## 5.8. Conclusão

> [!summary] Conclusão do teste
> Como **0,267 > 0,05**:
> - **Não há evidências para rejeitar** a hipótese nula.
> - **Não existe diferença estatisticamente significante** entre Naive Bayes e Multilayer Perceptron.

> [!success] Decisão prática
> Os 2% de diferença (78% → 80%) eram provavelmente **acaso**. Portanto, **use o Naive Bayes** — ele tem desempenho estatisticamente equivalente, mas treina em **3 minutos** em vez de 2 horas. 🎯

> [!important] A grande lição
> Sem o teste de hipótese, você teria escolhido o MLP (achando que 80% > 78%) e desperdiçado horas de processamento por uma vantagem que **não existe de verdade**. Comparar modelos "no olhômetro" é um erro caro.

---

## 5.9. O Processo em Resumo

```
   1. Criar VÁRIOS modelos de cada algoritmo (com aleatoriedade!)
        │
        ▼
   2. Calcular: médias, desvios padrão, tamanhos das amostras
        │
        ▼
   3. Hipótese Nula: "a diferença das médias é zero"
        │
        ▼
   4. Calcular a estatística de teste
      (diferença das médias ÷ erro padrão)
        │
        ▼
   5. Obter o valor-p (tabela Z, ×2 se bicaudal)
        │
        ▼
   6. Comparar com Alfa (0,05):
      • p < 0,05 → diferença REAL
      • p > 0,05 → diferença é ACASO
```

---

## 5.10. Resumo

> [!summary] O essencial da Avaliação de Desempenho
> - Comparar dois modelos exige **teste estatístico**, não "olhômetro".
> - **Teste de hipótese de duas médias**: cria vários modelos de cada um, compara as médias.
> - **Hipótese nula** = "não há diferença real".
> - **Estatística de teste** = diferença das médias ÷ erro padrão.
> - **Valor-p** vs. **Alfa (0,05)**: se p < 0,05, diferença é real; se p > 0,05, é acaso.
> - No exemplo: 78% vs. 80% deu p = 0,267 → diferença **não é significativa** → escolher o mais rápido.

---

## 🔗 Próximos passos
- [[06 - Custo de um Modelo]] — além da estatística, há outra dimensão: quanto cada erro custa em **dinheiro**.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
