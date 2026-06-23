---
tags:
  - machine-learning
  - busca
  - otimização
  - fundamentos
---

# 1. Introdução à Busca e Otimização

> [!info] O que esta nota cobre
> Por que precisamos de algoritmos de busca, o conceito de **espaço de busca**, os **elementos** de um problema de busca, **busca local vs. global**, o problema do **local optima** e a **função de avaliação**.

---

## 1.1. Por que Busca e Otimização?

> [!note] O problema
> Existem problemas computacionais que (ainda) **não se resolvem com uma equação ou fórmula**. É preciso **buscar** uma possível solução **entre todas as soluções possíveis** (o **espaço de busca**). Para muitos deles, acredita-se que **tal fórmula nem existe**.

> [!warning] Por que não fazer sempre uma busca completa?
> Na maioria dos problemas, testar **todas** as soluções é **impossível** em tempo/custo computacional.
> - **Exemplo:** o jogo **Go** (tabuleiro 19×19) tem cerca de **2×10¹⁷⁰** configurações — "**mais que o número de átomos conhecidos no Universo**". Não há computador que enumere isso.

---

## 1.2. Não existe algoritmo perfeito para tudo

> [!important] Verdade central
> **Não existe um algoritmo que atenda de forma ótima a todos os tipos de problema.** Quanto **mais informação** temos sobre o objetivo da busca, **mais fácil** ela fica.

> [!note] Três estratégias para otimizar a busca
> - **Redução do espaço de busca** (cortar caminhos sem solução).
> - **Algoritmos heurísticos** (usar "atalhos" inteligentes).
> - **Elementos estocásticos** (não determinísticos — usar aleatoriedade).

---

## 1.3. Como classificar os algoritmos

> [!note] Quatro perguntas para avaliar um algoritmo de busca
> 1. **Solução?** Há garantia de que ele **encontrará** alguma solução?
> 2. **Solução ótima?** A solução encontrada será **a melhor**?
> 3. **Complexidade de tempo:** quanto **tempo** vai levar?
> 4. **Complexidade de espaço:** quanta **memória** vai precisar?

---

## 1.4. Elementos de um problema de busca

> [!important] A definição formal
> Um problema de busca tem:
> | Símbolo | Significado |
> |---|---|
> | **S** | conjunto finito de **estados** (o *search space*) |
> | **I** | conjunto de **estados iniciais** |
> | **O** | conjunto de **objetivos** (estados-meta) |
> | **FS** | função que recebe o estado atual e retorna os **estados alcançáveis** |
> | **FC** | função de **custo**: dado o estado atual e um próximo, retorna o custo |

> [!example] Exemplo (grafo do curso)
> ```
>   S = {1,2,3,4,5,6}     (todos os estados)
>   I = {1}               (começa no 1)
>   O = {6}               (objetivo é o 6)
>   FS(2) = {3,4}         (do estado 2 alcanço 3 e 4)
>   FC(2,4) = 1           (ir de 2 para 4 custa 1)
> ```

---

## 1.5. Busca Local vs. Global

> [!note] Duas filosofias
> | | **Global** | **Local** |
> |---|---|---|
> | Explora | **todo** o espaço de busca (teoricamente) | apenas a **vizinhança** |
> | Encerra quando | acha o ótimo global, expira o tempo, ou esgota o espaço | expira o tempo ou não consegue mais melhorar |
> | Garante o ótimo? | Sim (mas é cara) | Não (mas é rápida) |

---

## 1.6. O problema do Local Optima

> [!warning] A grande armadilha
> Algoritmos de **busca local** procuram nas vizinhanças. Lá podem achar uma solução que é **a melhor localmente** — mas **não há garantia** de que seja a melhor **globalmente**.

```
              Global Optima
                   ╱╲
       Local      ╱  ╲
       Optima    ╱    ╲
        ╱╲      ╱      ╲
       ╱  ╲    ╱        ╲
   ───╱    ╲__╱          ╲___
      ↑ preso aqui!
```

> [!note] O trade-off da vizinhança
> Quanto **menor** a vizinhança explorada, **mais rápido** o algoritmo acha um ótimo local — mas **maior** o risco de ele estar longe do global. Muitos problemas são resolvidos **só até o local optima** (e isso pode ser "bom o suficiente").

---

## 1.7. Função de Avaliação (Custo)

> [!note] O que é
> A **função objetivo** (também chamada função de custo ou de adaptação) diz **o quão boa** está a solução encontrada.

> [!important] Três níveis de "avaliabilidade"
> | Situação | Exemplos |
> |---|---|
> | Posso avaliar se é o **ótimo global** | equação matemática/lógica; quebra-cabeças |
> | Só posso avaliar se é **boa**, mas não se é ótima global | jogada em jogo de tabuleiro; rota do caixeiro viajante |
> | **Difícil ou impossível** avaliar a qualidade | encontrar um **caminho** (labirinto) |

> [!tip] Por que isso importa
> A escolha do algoritmo depende disso: se você **consegue medir** quão boa é a solução, pode guiar a busca (heurística). Se **não consegue**, sobra a busca cega/força bruta.

---

## 1.8. Resumo

> [!summary] O essencial
> - Busca serve para problemas **sem fórmula**; o **espaço de busca** costuma ser gigantesco (Go > átomos do Universo).
> - Problema de busca = **S, I, O, FS, FC** (estados, inicial, objetivo, transição, custo).
> - **Busca local** (rápida, pode prender) vs. **global** (garante ótimo, cara).
> - **Local optima** = melhor da vizinhança, nem sempre o ótimo global.
> - A **função de avaliação** mede a qualidade — e nem sempre conseguimos medi-la.

---

## 🔗 Próximos passos
- [[02 - Hill Climbing]] — a busca local mais simples (e sua famosa armadilha).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
