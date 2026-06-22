---
tags:
  - machine-learning
  - redes-neurais
  - arquitetura
  - topologia
---

# 3. Arquitetura de Redes Neurais

> [!info] O que esta nota cobre
> Como **organizar** os neurônios em uma rede: o que é **topologia** e **arquitetura**, a diferença entre redes **feed-forward** e **recorrentes**, e como decidir **quantas camadas** e **quantos nós** usar.

---

## 3.1. Topologia vs. Arquitetura

> [!note] Dois conceitos próximos
> - **Topologia** = a **estrutura** de nós e camadas (quantos neurônios, como estão dispostos).
> - **Arquitetura** = o **tipo de fluxo** dos dados pela rede (para frente? com retorno?).

A **largura da camada** é o número de **nós (neurônios)** nela.

---

## 3.2. Arquitetura: Feed-Forward vs. Recorrente

| Tipo | Como o dado flui | Imagem mental |
|---|---|---|
| **Feed-Forward** (alimentação para frente) | Só **para frente**: entrada → ocultas → saída. Sem voltas. | Uma esteira de produção. |
| **Recorrente** (bidirecional / com retorno) | Tem **conexões de retorno**: a saída de um neurônio pode voltar como entrada. | Um eco / memória. |

> [!tip] Quando usar cada uma
> - **Feed-forward** serve para a maioria dos problemas de classificação/regressão "estáticos".
> - **Recorrente** serve quando há **dependência temporal/sequencial** (texto, séries temporais) — é a base das **[[06 - LSTM e Redes Recorrentes|LSTM]]**.

---

## 3.3. Quantas camadas?

Uma rede tem três tipos de camada:

```
   [Entrada]  →  [Oculta 1] → [Oculta 2] → ... → [Saída]
```

> [!note] Regras práticas
> - **Camada de entrada:** sempre **1**.
> - **Camada de saída:** sempre **1**.
> - **Camadas ocultas:** **n** (zero, uma ou várias). É aqui que mora a "profundidade".

> [!important] É a quantidade de camadas ocultas que define "deep learning"
> Muitas camadas ocultas = **rede profunda** = **[[04 - Deep Learning e Hiperparâmetros|Deep Learning]]**.

---

## 3.4. Quantos nós (neurônios) em cada camada?

> [!summary] Como dimensionar
> | Camada | Quantos nós |
> |---|---|
> | **Entrada** | **Um para cada atributo/valor** de entrada. |
> | **Saída** | **Classificação:** um nó por classe. **Regressão:** apenas **1** nó. |
> | **Oculta** | Não há fórmula fixa — é um **hiperparâmetro** que você ajusta (testando). |

> [!example] Exemplo
> Se você tem 10 atributos e quer classificar entre 3 categorias: **10 nós** na entrada e **3 nós** na saída. Quantos nós nas ocultas e quantas ocultas? Isso você descobre **experimentando** (ver [[04 - Deep Learning e Hiperparâmetros]]).

---

## 3.5. Resumo

> [!summary] O essencial
> - **Topologia** = estrutura (nós/camadas); **arquitetura** = fluxo (feed-forward vs. recorrente).
> - **Feed-forward:** dados só para frente. **Recorrente:** com retorno (memória) → para sequências.
> - Entrada = 1 camada (1 nó por atributo); saída = 1 camada (1 nó/classe ou 1 para regressão); ocultas = n.
> - Mais camadas ocultas = rede mais **profunda** (deep learning).

---

## 🔗 Próximos passos
- [[04 - Deep Learning e Hiperparâmetros]] — o que muda quando empilhamos muitas camadas, e como controlar o treino (ativação, regularização, gradient descent).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
