---
tags:
  - machine-learning
  - moc
  - índice
  - algoritmos-genéticos
  - otimização
aliases:
  - Algoritmos Genéticos
  - GA
---

# Algoritmos Genéticos

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do módulo **11 — Algoritmos Genéticos (GA)**. Algoritmos inspirados na **evolução das espécies** de Darwin para resolver problemas de **busca e otimização**: criam "soluções", deixam as melhores se reproduzirem e evoluem geração após geração.

---

## Roteiro de Estudo

- [[01 - Inspiração Biológica e Introdução]] — A evolução de Darwin e como ela vira um algoritmo.
- [[02 - Como Funciona]] — Cromossomos, genes, população, crossover, mutação, elitismo e fitness.
- [[03 - Exemplos Práticos]] — Exemplo binário (mochila), valor real (equação) e o ciclo completo de gerações.

---

## Visão Geral em uma Imagem Mental

```
   População inicial (soluções aleatórias)
            │
            ▼
   ┌──► Avalia Fitness (adaptação)
   │        │
   │        ▼
   │   Seleção (roleta) → Crossover → Mutação → Elitismo
   │        │
   │        ▼
   └──── Nova Geração ──► (repete até critério de parada)
```

---

## Conceito-Chave Rápido (cola)

> [!summary] Para não esquecer
> - **Cromossomo** = uma solução proposta. **População** = conjunto de cromossomos.
> - **Fitness** = nota de adaptação (quão boa é a solução).
> - **Crossover** = combinar soluções; **Mutação** = alterar genes ao acaso; **Elitismo** = preservar os melhores.
> - É **heurística**: a melhor solução encontrada nem sempre é a ótima global.

---

## 🏷️ Tags Relacionadas
#machine-learning #algoritmos-genéticos #otimização #heurística #estudos

---
[[_Índice Machine Learning|⬅️ Voltar ao Índice do Curso]]
