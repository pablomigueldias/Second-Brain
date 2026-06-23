---
tags:
  - machine-learning
  - algoritmos-genéticos
  - fundamentos
---

# 1. Inspiração Biológica e Introdução

> [!info] O que esta nota cobre
> A **inspiração biológica** dos algoritmos genéticos (a evolução de Darwin), o que eles são, onde se aplicam, e o conceito central de **adaptação (fitness)**.

---

## 1.1. A inspiração: a evolução de Darwin

> [!note] A origem
> Os Algoritmos Genéticos se inspiram na obra de **Charles Darwin**, *A Origem das Espécies*, e na **seleção natural**:
> - Indivíduos mais **adaptados** ao ambiente têm **mais chance de sobreviver e se reproduzir**.
> - Seus genes passam adiante; ao longo das gerações, a população **melhora**.

---

## 1.2. O que é um Algoritmo Genético

> [!note] Definição
> **Algoritmos Genéticos (GA)** buscam **imitar o processo de evolução das espécies**. É uma versão **simplificada, porém eficiente**, da natureza.

> [!important] Onde se aplica
> Problemas de **busca, otimização, agendamento** — situações onde há um **espaço enorme de soluções possíveis** e queremos achar a melhor (ou uma muito boa).

> [!note] Uma diferença importante para a natureza
> Na natureza **não existe condição de parada** — a evolução continua para sempre. No algoritmo, precisamos definir **quando parar** (nº de gerações, tempo, ou quando a solução para de melhorar).

---

## 1.3. Adaptação (Fitness): o motor da evolução

> [!important] O conceito-chave
> A cada **geração**, quanto **maior a adaptação (fitness)** de um descendente, **maior a chance** de ele ser escolhido para gerar a próxima geração — e assim aumentam as chances de sucesso (igual à natureza).

> [!example] Intuição
> Pense numa competição: os candidatos com **melhor desempenho** (maior fitness) são os que "passam seus genes" adiante. Os fracos tendem a ser descartados. Geração após geração, a população converge para soluções cada vez melhores.

---

## 1.4. O ciclo completo (visão geral)

```
   Problema
      │
      ▼
   1ª Geração: propõe soluções ALEATÓRIAS (inicialização)
      │
      ▼
   Avalia a Adaptação (Fitness)
      │
      ▼
   É a solução ideal (ou acabou o tempo)?
      │ Não → Cruzamento (crossover) → Mutação → Nova Geração ──┐
      │                                                          │
      └──────────────────── (repete) ◄──────────────────────────┘
      │ Sim
      ▼
   Fim
```

> [!summary] Os termos que vêm a seguir
> - **População** = conjunto de **cromossomos** (soluções propostas).
> - **Inicialização** = a primeira geração, criada **aleatoriamente**.
> - **Cruzamento (crossover)** e **mutação** = como nascem os descendentes.
> Tudo isso é detalhado em [[02 - Como Funciona]].

---

## 1.5. Resumo

> [!summary] O essencial
> - GA imita a **evolução das espécies** (Darwin / seleção natural).
> - Servem para **busca, otimização e agendamento** em espaços enormes.
> - **Fitness (adaptação)** = nota de cada solução; melhores têm mais chance de se reproduzir.
> - Diferente da natureza, o algoritmo precisa de uma **condição de parada**.

---

## 🔗 Próximos passos
- [[02 - Como Funciona]] — os mecanismos: cromossomos, genes, crossover, mutação e elitismo.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
