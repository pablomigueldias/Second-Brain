---
tags:
  - machine-learning
  - busca
  - otimização
  - bfs
  - dfs
---

# 3. Busca Cega (BFS, DFS, Best-First)

> [!info] O que esta nota cobre
> Os algoritmos de **força bruta / busca cega**: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)** e **Best-First Search**. Eles exploram o espaço de busca para **garantir** o ótimo global.

---

## 3.1. Força Bruta (Brute Force / Blind Search)

> [!note] A ideia
> Algoritmos de **Brute Force / Blind Search** **exploram todo o espaço de busca**. Por isso **garantem encontrar o Global Optima** — eles não "chutam", olham tudo.

> [!warning] O preço
> A garantia tem custo: explorar tudo é **caro** em tempo e memória. Viável só quando o espaço de busca não é astronômico.

---

## 3.2. Breadth-First Search (BFS) — Busca em Largura

> [!note] Como funciona
> Explora o grafo **por camadas**: primeiro todos os estados a **1 passo** do início, depois todos a **2 passos**, e assim por diante. É capaz de **retornar** de uma vizinhança em busca de uma solução melhor (**backtracking**).

> [!example] "Quais estados alcanço a partir do 1 com n passos?"
> ```
>   n=1: explora vizinhos diretos do 1
>   n=2: explora vizinhos dos vizinhos
>   n=3: e assim por diante...
> ```

> [!important] Custo do caminho
> O BFS pode comparar **caminhos** pelo custo total acumulado:
> ```
>   S1: 1 → 2 → 4 → 8           custo total Fc1 = 60
>   S2: 1 → 2 → 3 → 6 → 7 → 8   custo total Fc2 = 35  ← melhor!
> ```
> Mesmo sendo mais longo em nós, **S2 é mais barato** (35 < 60). BFS encontra isso.

> [!tip] Característica do BFS
> Encontra o caminho com **menos passos** primeiro, e é ótimo quando todos os passos têm o mesmo custo. Usa **mais memória** (guarda toda a "fronteira" de uma camada).

---

## 3.3. Depth-First Search (DFS) — Busca em Profundidade

> [!note] Como funciona
> Explora **uma vizinhança até o fim** (vai fundo num ramo), e só então **retorna** (backtrack) para tentar **outras ramificações**.

```
   Vai fundo no primeiro ramo:  1 → 2 → 3 → ... (fundo)
   Bateu num beco? Volta e tenta outro ramo.
```

> [!tip] DFS vs. BFS
> | | BFS (largura) | DFS (profundidade) |
> |---|---|---|
> | Estratégia | camada por camada | vai fundo, depois volta |
> | Memória | mais (guarda a fronteira) | menos (guarda só o caminho atual) |
> | Acha caminho mais curto? | sim (passos iguais) | não necessariamente |

---

## 3.4. Best-First Search

> [!note] Como funciona
> Usa uma **heurística** para avaliar o "valor" de cada nó e escolher **qual explorar primeiro** — vai sempre pelo nó **mais promissor**.

> [!important] Depende da heurística
> A **performance depende da heurística** escolhida. Uma boa heurística faz a busca convergir rápido; uma ruim pode atrapalhar. (É a ideia por trás de algoritmos famosos como o **A***.)

> [!example] Diferença para BFS/DFS
> BFS e DFS são **cegos** (exploram mecanicamente). O Best-First é **informado**: ele usa uma "dica" (heurística) sobre quão perto do objetivo cada nó parece estar, e segue por ali.

---

## 3.5. Resumo

> [!summary] O essencial
> - **Força bruta / busca cega** explora **todo** o espaço → **garante o ótimo global**, mas é cara.
> - **BFS (largura):** por camadas; acha o caminho mais curto; usa mais memória; faz backtracking.
> - **DFS (profundidade):** vai fundo num ramo e volta; usa menos memória.
> - **Best-First:** **informado** por uma **heurística**; performance depende dela.

---

## 🔗 Próximos passos
- [[04 - Problemas de Caminho]] — aplicando busca cega a labirintos modelados como grafos.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
