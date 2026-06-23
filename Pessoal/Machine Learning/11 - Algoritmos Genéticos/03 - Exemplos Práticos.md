---
tags:
  - machine-learning
  - algoritmos-genéticos
  - exemplos
  - mochila
---

# 3. Exemplos Práticos

> [!info] O que esta nota cobre
> Os algoritmos genéticos em ação: um **ciclo completo de gerações** com fitness numérico, o exemplo de **valor real** (resolver uma equação) e o exemplo **binário** (problema da mochila).

---

## 3.1. Exemplo: maximizar a soma de bits

> [!note] O problema
> **Objetivo:** chegar ao cromossomo `1 1 1 1 1 1 1 1` (todos os genes = 1).
> **Função de fitness:** `F = Σ` (a soma dos genes). Quanto mais 1s, maior o fitness.

### Passo 1 — Inicialização e avaliação
> [!example] 1ª Geração (aleatória) e seu fitness
> | Cromossomo | Fitness |
> |---|---|
> | Ag1 | 3 |
> | Bg1 | **5** |
> | Cg1 | 2 |
> | Dg1 | 3 |
> | Eg1 | 3 |
> | Fg1 | 4 |
>
> **Adaptação total da geração = 20.**

### Passo 2 — Elitismo
> [!note]
> O melhor cromossomo (**Bg1**, fitness 5) é **copiado intacto** para a próxima geração (vira Ag2). Garante que não perdemos o melhor.

### Passo 3 — Seleção (roleta) + Crossover
> [!example]
> Selecionam-se pais pela **roleta** (Bg1, com fitness 5, tem mais chance). Aplica-se **crossover de ponto único**:
> - `Bg1 × Cg1` → herdeiros **Bg2, Cg2**
> - `Bg1 × Fg1` → herdeiros **Dg2, Eg2**

### Passo 4 — Mutação
> [!note]
> Aplica-se mutação (probabilidade baixa) a alguns genes dos herdeiros (ex.: em Cg2).

### Passo 5 — Nova geração e melhora
> [!example] 2ª Geração
> | Cromossomo | Fitness |
> |---|---|
> | Ag2 | 5 |
> | Bg2 | 3 |
> | Cg2 | 4 |
> | Dg2 | 4 |
> | Eg2 | 4 |
> | Fg2 | 3 |
>
> **Adaptação total = 23** → **melhora de 15%** em relação à geração anterior (20 → 23). 🎉

> [!important] A lição
> Em **uma única geração**, a população já evoluiu de 20 para 23. Repetindo o ciclo, ela converge para o objetivo (`F = 8`, todos os bits = 1).

---

## 3.2. Exemplo de valor real: resolver uma equação

> [!note] O problema
> Resolver `2x + 5 = 20` → o GA precisa **achar o X**.

> [!important] A função de fitness
> O GA busca **maximizar o retorno** de uma função. Aqui, queremos que `2x + 5` chegue **o mais perto de 20** possível. Uma função de adaptação possível:
> ```
> valor = 2*x + 5
> if (valor > 20):   fitness = 20 - valor    # penaliza passar do alvo
> else:              fitness = valor - 20     # quanto mais perto de 20, melhor (menos negativo)
> ```
> O GA testa vários X, mede a "nota" de cada um e evolui em direção ao X que dá exatamente 20 (ou seja, **x = 7,5**).

> [!tip] O funcionamento é igual para todos os tipos
> Binário, permutação ou valor real: a função de fitness **recebe uma entrada e retorna um valor real**; o GA busca a entrada que **maximiza** esse retorno. A estrutura do algoritmo não muda — só a **codificação** dos genes.

---

## 3.3. Exemplo binário: o problema da mochila

> [!note] O problema (mochila / knapsack)
> Você vai para uma **aventura** com uma mochila de capacidade limitada (ex.: **15 kg**, mas os itens somam 30 kg). Objetivo:
> - Levar o **maior número de itens** possível.
> - **Priorizar os mais importantes** (que valem mais pontos).
> - **Sem estourar** o peso máximo.

> [!important] Codificação binária
> Cada item é um **gene binário**: **1 = levar**, **0 = deixar**.
> ```
>   Item:    A  B  C  D  E  F  G
>   Gene:    1  0  1  0  1  0  1     ← esta solução leva A, C, E, G
> ```
> O fitness soma os **pontos** dos itens levados — mas **zera (ou penaliza)** se o peso passar de 15 kg. O GA evolui combinações até achar a mochila de maior valor dentro do limite.

> [!example] Por que GA é bom aqui
> Com 7 itens há 2⁷ = 128 combinações; com 50 itens, são mais de 10¹⁵. Testar todas é inviável. O GA **busca de forma inteligente** sem precisar avaliar tudo — é o tipo de problema de [[../12 - Algoritmos de Busca e Otimização/00 - Índice|busca e otimização]] onde ele brilha.

---

## 3.4. Resumo

> [!summary] O essencial
> - O ciclo (inicializa → fitness → elitismo → seleção → crossover → mutação → nova geração) faz a população **melhorar** a cada rodada.
> - **Valor real:** a função de fitness mede a distância ao alvo; o GA maximiza-a (ex.: achar X em `2x+5=20`).
> - **Binário (mochila):** genes 1/0 = levar/não levar; fitness = pontos, penalizando excesso de peso.
> - Funciona igual para qualquer codificação — muda só a representação dos genes.

---

## 🔗 Próximos passos
- Fim do módulo de Algoritmos Genéticos! Siga para [[../12 - Algoritmos de Busca e Otimização/00 - Índice|Algoritmos de Busca e Otimização]] — outras estratégias para os mesmos tipos de problema.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
