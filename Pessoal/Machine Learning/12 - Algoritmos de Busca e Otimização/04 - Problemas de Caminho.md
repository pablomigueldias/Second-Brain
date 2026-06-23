---
tags:
  - machine-learning
  - busca
  - otimização
  - grafos
  - labirinto
---

# 4. Problemas de Caminho

> [!info] O que esta nota cobre
> **Problemas de caminho** (como labirintos): por que exigem **busca cega**, como **transformar um labirinto em grafo**, o **Lee Algorithm**, e por que o Hill Climbing falha aqui.

---

## 4.1. Por que problemas de caminho são especiais

> [!warning] Não dá para avaliar o "quanto falta"
> Em problemas de **caminho** (achar a saída de um labirinto), normalmente **não conseguimos avaliar o quão otimizada está a solução atual** — não dá para saber se um beco te aproxima ou te afasta da saída só olhando localmente.

> [!important] Consequência
> Por isso, esses problemas **só podem ser resolvidos com algoritmos baseados em Blind Search** (busca cega). É preciso explorar sistematicamente, sem heurística confiável de distância.

> [!note] Lee Algorithm
> O **Lee Algorithm**, baseado em **[[03 - Busca Cega (BFS, DFS, Best-First)|Breadth-First Search]]**, é o clássico para encontrar o **caminho mais curto** em labirintos/grades (muito usado em roteamento de circuitos).

---

## 4.2. Transformar o labirinto em grafo

> [!important] A modelagem (labirinto 10×10)
> Para resolver, convertemos o labirinto em um **grafo** (nós + arestas):
> | Vira nó... | Quando |
> |---|---|
> | **Nó inicial** | no ponto de partida |
> | **Nó final** | no ponto de chegada |
> | **Nó intermediário** | a cada **divisão** (bifurcação) do labirinto |
> | **Nó "local optima"** | a cada **ponto sem saída** (beco) |
>
> **Regra:** apenas o nó inicial e os intermediários podem ter **mais de uma aresta** (becos e o fim são "pontas").

> [!example] No exemplo do curso
> Um labirinto 10×10 virou um grafo com **21 nós**, dos quais **11 eram becos sem saída** (local optima).

---

## 4.3. Por que o Hill Climbing fracassa aqui

> [!example] A conta da probabilidade
> O curso calculou a chance de o **[[02 - Hill Climbing|Hill Climbing]]** achar a saída **na primeira tentativa**, multiplicando as probabilidades de acertar a direção em cada bifurcação:
>
> | Nó | 1 | 3 | 5 | 6 | 9 | 12 | 13 | 16 |
> |---|---|---|---|---|---|---|---|---|
> | Prob. | 1/2 | 1/2 | 1/2 | 1/2 | 1/3 | 1/2 | 1/3 | 1/2 |
>
> $$ 0{,}5 \times 0{,}5 \times 0{,}5 \times 0{,}5 \times 0{,}33 \times 0{,}5 \times 0{,}33 \times 0{,}5 \approx \mathbf{0{,}0017} $$
>
> Ou seja, **~0,17% de chance** — praticamente nula! A cada bifurcação ele pode entrar num beco (local optima) e travar.

> [!important] A lição
> Em labirintos, a busca **local** (Hill Climbing) é quase inútil porque os **becos são armadilhas de local optima** por toda parte. Só a **busca cega** (BFS/Lee), que explora sistematicamente e faz backtracking, **garante** achar a saída.

---

## 4.4. Como avaliar a evolução?

> [!question] Distância do estado inicial?
> Uma tentativa de heurística seria medir a **distância percorrida desde o início**. Mas, como vimos, em muitos labirintos **não é possível avaliar** o quanto a solução atual está perto da meta — daí a dependência de busca cega.

---

## 4.5. Resumo

> [!summary] O essencial
> - Problemas de **caminho** não permitem avaliar "quanto falta" → exigem **busca cega**.
> - **Lee Algorithm** (baseado em BFS) acha o caminho mais curto.
> - **Modelagem em grafo:** nós no início, fim, bifurcações e becos; becos = **local optima**.
> - **Hill Climbing fracassa** (no exemplo, ~0,17% de sucesso) porque becos são armadilhas em toda parte.

---

## 🔗 Próximos passos
- [[05 - Tabu Search e Simulated Annealing]] — metaheurísticas espertas que **escapam** dos local optima.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
