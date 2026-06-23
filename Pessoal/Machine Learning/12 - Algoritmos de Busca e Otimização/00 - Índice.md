---
tags:
  - machine-learning
  - moc
  - índice
  - busca
  - otimização
aliases:
  - Busca e Otimização
---

# Algoritmos de Busca e Otimização

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do módulo **12 — Algoritmos de Busca e Otimização**. Para muitos problemas **não existe fórmula** — só dá para **buscar** a melhor solução entre todas as possíveis. Aqui vemos as estratégias: de buscas locais rápidas (Hill Climbing) a buscas completas (BFS/DFS) e metaheurísticas (Tabu Search, Simulated Annealing).

---

## Roteiro de Estudo

- [[01 - Introdução à Busca e Otimização]] — Por que busca? Espaço de busca, busca local vs. global, local optima e função de avaliação.
- [[02 - Hill Climbing]] — A subida da montanha e o problema de ficar preso no ótimo local.
- [[03 - Busca Cega (BFS, DFS, Best-First)]] — Força bruta que garante o ótimo global.
- [[04 - Problemas de Caminho]] — Labirintos como grafos (Lee Algorithm).
- [[05 - Tabu Search e Simulated Annealing]] — Metaheurísticas que escapam do ótimo local.

---

## Visão Geral em uma Imagem Mental

```
                 Busca e Otimização
                        │
        ┌───────────────┴────────────────┐
   Busca Local                     Busca Global (Cega)
   (rápida, pode prender)          (completa, garante ótimo)
        │                                │
   Hill Climbing                     BFS / DFS / Best-First
   Tabu Search
   Simulated Annealing  ◄── escapam do local optima
```

---

## Conceito-Chave Rápido (cola)

> [!summary] Para não esquecer
> - **Espaço de busca** = todas as soluções possíveis (muitas vezes gigantesco).
> - **Local optima** = melhor solução de uma vizinhança (≠ ótimo global).
> - **Busca local** = rápida, mas pode prender no local optima. **Busca global/cega** = garante o ótimo, mas é cara.
> - **Heurística** = "atalho" inteligente; **estocástico** = usa aleatoriedade para escapar de armadilhas.

---

## 🏷️ Tags Relacionadas
#machine-learning #busca #otimização #heurística #estudos

---
[[_Índice Machine Learning|⬅️ Voltar ao Índice do Curso]]
