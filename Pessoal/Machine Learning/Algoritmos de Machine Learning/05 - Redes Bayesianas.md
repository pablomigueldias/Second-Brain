---
tags:
  - machine-learning
  - algoritmos
  - redes-bayesianas
  - classificação
  - probabilidade
  - supervisionado
---

# 5. Redes Bayesianas

> [!info] O que esta nota cobre
> As **Redes Bayesianas**: uma evolução do [[04 - Naive Bayes]] que **abandona a suposição de independência total** entre atributos. Veremos como elas modelam **dependências** (relações de "pai e filho" entre variáveis), como fazem previsões, e como o número de "pais" afeta a complexidade.

---

## 5.1. O Problema do Naive Bayes

> [!warning] Relembrando
> O [[04 - Naive Bayes]] assume que **todos os atributos são independentes** entre si. Mas na realidade, eles **se influenciam**.

> [!example] Exemplo
> No dataset do tempo, `temperature` e `humidity` **não são independentes** — dias quentes tendem a ter padrões de umidade específicos. O Naive Bayes **ignora** isso.

As **Redes Bayesianas** resolvem exatamente esse ponto: elas **modelam as dependências** entre as variáveis.

---

## 5.2. O que é uma Rede Bayesiana?

> [!note] Definição
> Uma **Rede Bayesiana** é um modelo probabilístico que representa as variáveis e suas **relações de dependência** na forma de um **grafo** (diagrama de setas).

Cada variável é um **nó**; as setas indicam **quem influencia quem**. Uma variável que aponta para outra é chamada de **"pai"**.

```
   Naive Bayes (tudo depende só da classe):

        play
       ╱ │ │ ╲
      ╱  │ │  ╲
  outlook temp humid windy
   (todos independentes entre si)


   Rede Bayesiana (há dependências entre atributos):

           play
          ╱    ╲
     outlook    ...
       │  ╲
       │   ╲
   temperature  windy
       │
   humidity
   (atributos podem depender uns dos outros)
```

> [!tip] A diferença central
> - **Naive Bayes** → estrutura **fixa e simples**: todo atributo depende **só** da classe.
> - **Rede Bayesiana** → estrutura **flexível**: atributos podem depender da classe **e de outros atributos**.

---

## 5.3. Como Funciona a Previsão

Numa Rede Bayesiana, cada nó tem uma **tabela de distribuição de probabilidade** que leva em conta seus **pais**.

### Tabela de probabilidades (exemplo do dataset do tempo)

| Class | Outlook P(outlook\|Play) | Temperature P(temp\|outlook, play) | Humidity P(humid\|temp, play) | Windy P(windy\|outlook, play) |
|---|---|---|---|---|
| **P(Yes)** = 0,633 | 0,238 | 0,143 | 0,5 | 0,5 |
| **P(No)** = 0,367 | 0,538 | 0,556 | 0,833 | 0,5 |

> [!note] Repare na diferença
> No Naive Bayes era `P(temperature | play)`. Aqui é `P(temperature | outlook, play)` — a temperatura depende **também** do `outlook`. Isso é a dependência sendo modelada.

### Cálculo da previsão

Para um dia `sunny, hot, high, FALSE`, multiplicamos as probabilidades:

**Probabilidade YES:**
$$
P(\text{yes}) = 0{,}633 \times 0{,}238 \times 0{,}143 \times 0{,}5 \times 0{,}5 = \mathbf{0{,}00538588}
$$

**Probabilidade NO:**
$$
P(\text{no}) = 0{,}367 \times 0{,}538 \times 0{,}556 \times 0{,}833 \times 0{,}5 = \mathbf{0{,}045723}
$$

> [!summary] Decisão
> `NO (0,0457)` > `YES (0,0054)` → o resultado é **NO**.
>
> A regra de decisão é a **mesma do Naive Bayes**: a classe com maior probabilidade vence. O que muda é **como** as probabilidades são calculadas (considerando os pais).

---

## 5.4. O Número de "Pais" e a Complexidade

Um conceito central das redes bayesianas é **quantos pais cada nó tem**.

### Rede com 1 pai apenas

Cada atributo depende de **apenas uma** outra variável (geralmente só a classe). É a estrutura **mais simples** — bem próxima do Naive Bayes.

### Rede com 2 pais

Cada atributo pode depender de **duas** variáveis. Mais expressiva, captura mais relações.

### Aumentando o número de pais

> [!warning] O custo de mais pais
> Quanto **mais pais** um nó tem, **mais combinações de probabilidade** precisam ser calculadas e armazenadas. A complexidade **explode**.

### Exemplo concreto: explosão de combinações

Para o dataset do tempo, se considerássemos **todas as possibilidades** de combinação dos atributos:

$$
3 \times 3 \times 2 \times 2 \times 2 = 72 \text{ combinações}
$$

(3 valores de outlook × 3 de temperature × 2 de humidity × 2 de windy × 2 de play)

> [!danger] A lição
> Modelar **todas** as dependências possíveis gera uma quantidade enorme de probabilidades para calcular. Por isso é preciso **equilíbrio**: nem simples demais (Naive Bayes), nem complexo demais (todas as dependências).

---

## 5.5. Como Construir um Modelo de Rede Bayesiana

Construir uma rede bayesiana tem **duas partes**:

### Parte 1: Estrutura da Rede (número de pais)

> [!note] Definir a estrutura
> Decidir **quais nós se conectam** e **quantos pais cada um tem**. Isso é feito por **algoritmos de busca**, como:
> - **Hill Climbing** (subida de encosta) — vai testando pequenas mudanças e mantendo as que melhoram.
> - **Tabu Search** (busca tabu) — parecido, mas evita ficar preso repetindo as mesmas soluções.

### Parte 2: Tabelas de Distribuição de Probabilidade

> [!note] Preencher as probabilidades
> Uma vez definida a estrutura, é preciso **preencher as tabelas de probabilidade** de cada nó. Isso é feito por um **estimador**, que calcula as probabilidades a partir dos dados de treino.

```
   Construir uma Rede Bayesiana
        │
        ├──▶ 1. Estrutura (nº de pais)
        │       └─ Algoritmo de busca:
        │          Hill Climber, Tabu Search...
        │
        └──▶ 2. Tabelas de probabilidade
                └─ Estimador (calcula a partir dos dados)
```

---

## 5.6. Naive Bayes vs. Redes Bayesianas

| Aspecto | **Naive Bayes** | **Redes Bayesianas** |
|---|---|---|
| Suposição | Atributos **totalmente independentes** | Modela **dependências** entre atributos |
| Estrutura | Fixa e simples | Flexível (definida por busca) |
| Precisão | Boa, mas limitada pela suposição | Pode ser **mais precisa** |
| Complexidade | Baixa, rápido | Maior — cresce com o nº de pais |
| Construção | Direta (contar frequências) | Precisa de busca de estrutura + estimação |
| Quando usar | Datasets simples, classificação rápida (texto, spam) | Quando as dependências entre atributos importam |

> [!tip] Em resumo
> A Rede Bayesiana é o Naive Bayes "**crescido**": mais poderosa porque enxerga relações entre atributos, mas em troca é **mais cara** de construir e ajustar.

---

## 5.7. Resumo

> [!summary] O essencial das Redes Bayesianas
> - São modelos probabilísticos que representam variáveis e suas **dependências** num **grafo**.
> - Diferente do Naive Bayes, **não** assumem independência total entre atributos.
> - Cada nó tem uma tabela de probabilidade que considera seus **pais**.
> - **Previsão**: multiplica as probabilidades; a classe com maior valor vence (igual ao Naive Bayes).
> - **Mais pais** = mais expressivo, porém mais **complexo** (combinações explodem).
> - **Construir** = definir a estrutura (busca: Hill Climber, Tabu Search) + estimar as tabelas.

---

## 🔗 Próximos passos
- [[06 - Árvores de Decisão]] — saindo dos algoritmos probabilísticos e entrando nas árvores.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
