---
tags:
  - machine-learning
  - busca
  - otimização
  - hill-climbing
---

# 2. Hill Climbing

> [!info] O que esta nota cobre
> O **Hill Climbing** (subida da encosta): a busca local mais intuitiva, como ela funciona, sua tendência de **ficar presa no local optima** e a estratégia de **random restart**.

---

## 2.1. Como funciona

> [!note] O algoritmo, passo a passo
> 1. **Inicia** a busca em um **único ponto**.
> 2. **Escolhe um novo ponto** na vizinhança.
> 3. Se o novo ponto é uma **solução melhor**, passa a ser a melhor solução.
> 4. Se não, **escolhe outro** ponto na vizinhança.
> 5. Repete **até não ter mais como "subir"** (melhorar) ou acabar o tempo.

> [!example] A analogia do nome
> Imagine escalar uma montanha **no escuro e na neblina**. Você só enxerga o chão ao seu redor. A estratégia: dar passos sempre **para cima**. Você chega a um topo... mas pode ser apenas uma **colina menor**, não o pico mais alto da cordilheira.

```
              Global Optima (8)
                   ╱╲
                  ╱  7
                 8    5
                ╱
            3  4
           ╱
          2
         1   ← Hill Climbing sobe 1→2→3→4... e pode parar num topo menor
```

---

## 2.2. A grande limitação: Local Optima

> [!warning] O problema central
> O Hill Climbing tem **grande probabilidade de ficar preso no local optima**. Como ele **só aceita subir**, ao chegar no topo de uma colina ele para — mesmo que exista uma montanha bem mais alta logo adiante (mas que exigiria **descer** primeiro).

> [!note] Por quê
> Ele **segue apenas em um sentido**, explorando só a vizinhança imediata. Isso o torna rápido, mas **não garante** alcançar o **global optima**.

---

## 2.3. Estratégia: Random Restart

> [!tip] Como mitigar
> **Reiniciar o algoritmo** a partir de **outro ponto inicial aleatório**, na esperança de cair perto de uma encosta melhor. Roda-se o Hill Climbing **várias vezes** de pontos diferentes e fica-se com o melhor resultado.

```
   Tentativa 1: começa aqui → prende num topo baixo
   Tentativa 2: começa lá   → alcança o Global Optima ✓
```

> [!note] Variações
> Existem **muitas variações** do Hill Climbing, principalmente incluindo **elementos não determinísticos** (aleatórios) no algoritmo — a ideia que leva ao [[05 - Tabu Search e Simulated Annealing|Simulated Annealing]].

---

## 2.4. Resumo

> [!summary] O essencial
> - Hill Climbing = busca local que **só aceita melhorar** (subir), até travar.
> - **Simples e rápido**, mas **prende facilmente no local optima**.
> - **Random restart** (recomeçar de pontos aleatórios) ajuda a escapar.
> - Não garante o **ótimo global**.

---

## 🔗 Próximos passos
- [[03 - Busca Cega (BFS, DFS, Best-First)]] — algoritmos que, ao contrário do Hill Climbing, **garantem** encontrar o ótimo global (ao custo de explorar muito).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
