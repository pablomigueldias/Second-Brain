---
tags:
  - machine-learning
  - busca
  - otimização
  - tabu-search
  - simulated-annealing
---

# 5. Tabu Search e Simulated Annealing

> [!info] O que esta nota cobre
> Duas **metaheurísticas** que melhoram a busca local escapando do **local optima**: o **Tabu Search** (memória de lugares proibidos) e o **Simulated Annealing** (inspirado no resfriamento de metais).

---

## 5.1. O problema que ambas resolvem

> [!note] Recapitulando
> O [[02 - Hill Climbing|Hill Climbing]] prende no **local optima** porque **só aceita melhorar**. Estas duas técnicas adicionam mecanismos para **fugir** dessa armadilha e chegar mais perto do **global optima**.

---

## 5.2. Tabu Search

> [!note] A ideia
> Mantém uma **lista de locais proibidos** (a *Tabu list*) na **memória**. Um local entra na lista por:
> - **já ter sido visitado**, ou
> - **não otimizar** a função objetivo.

> [!important] Por que isso ajuda
> Ao **proibir** revisitar lugares, o algoritmo é **forçado a explorar regiões novas** — não fica girando em círculo nem voltando ao mesmo topo. Bom para **problemas combinatórios** (muitas combinações discretas).

> [!note] Critérios de parada
> - Número de **iterações**.
> - **Tempo**.
> - Iterações **sem melhoria** na função objetivo.

> [!example] Analogia
> É como explorar uma cidade anotando num caderno os lugares que **não vale a pena revisitar**. Isso te empurra a conhecer **bairros novos**, em vez de ficar dando voltas na mesma praça.

---

## 5.3. Simulated Annealing (Recozimento Simulado)

> [!important] O princípio: subir vs. explorar
> Diferente do Hill Climbing, o Simulated Annealing **nem sempre busca otimizar** — às vezes ele **aceita piorar** de propósito, para **explorar** e escapar de um local optima.

> [!note] A inspiração física
> **Annealing** = o processo de **aquecer e resfriar metal** para alterar sua estrutura. Ao resfriar lentamente, o metal se acomoda numa estrutura estável e melhor. O algoritmo imita isso com uma variável **"temperatura"**:
> | Temperatura | Comportamento do algoritmo |
> |---|---|
> | **Alta** | **Explora** muito — aceita soluções que aparentemente **pioram**, saindo de local optima. |
> | **Baixa** | **Explora a vizinhança** e tende a **aceitar o local optima** (que, a essa altura, deve estar perto do global). |

> [!important] A temperatura cai dinamicamente
> A "temperatura" começa **alta** (muita exploração/aleatoriedade) e vai **diminuindo** ao longo do tempo (cada vez mais conservador). Isso equilibra **exploração** (no início) e **refinamento** (no fim).

```
   Temperatura ALTA  →  aceita pular para soluções piores (escapa de armadilhas)
        │  (resfria com o tempo)
        ▼
   Temperatura BAIXA →  só aceita melhorar (refina a solução final)
```

> [!example] Exemplo do curso: Função de Rosenbrock
> O Simulated Annealing foi usado para achar o **mínimo global** da **função de Rosenbrock** (uma função não linear, clássica para testar otimizadores):
> $$ f(x,y) = (1 - x)^2 + 100\,(y - x^2)^2 $$
> O **mínimo global** é `f(x,y) = 0`, em **x = 1, y = 1**. Essa função tem um "vale" curvo traiçoeiro onde métodos simples se perdem — perfeito para mostrar o valor da exploração.

---

## 5.4. Comparação

> [!summary] Como cada uma escapa do local optima
> | Técnica | Mecanismo de fuga |
> |---|---|
> | **Hill Climbing** | (nenhum — prende) |
> | **Tabu Search** | **proíbe** revisitar lugares (memória) → força explorar o novo |
> | **Simulated Annealing** | **aceita piorar** quando "quente" → pula para fora da armadilha |

---

## 5.5. Resumo

> [!summary] O essencial
> - Ambas são **metaheurísticas** que escapam do **local optima**.
> - **Tabu Search:** mantém **lista de proibidos** (memória); bom para problemas **combinatórios**.
> - **Simulated Annealing:** usa uma **"temperatura"** que cai com o tempo; quente = explora (aceita piorar), frio = refina.
> - SA equilibra **exploração** (cedo) e **refinamento** (tarde) — ex.: mínimo da função de Rosenbrock.

---

## 🔗 Próximos passos
- Fim do módulo de Busca e Otimização! Siga para [[../13 - Lógica Difusa (Fuzzy)/00 - Índice|Lógica Difusa (Fuzzy)]].

---
[[00 - Índice|⬅️ Voltar ao Índice]]
