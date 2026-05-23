---
tags:
  - machine-learning
  - algoritmos
  - moc
  - índice
aliases:
  - Algoritmos de ML
---

# Algoritmos de Machine Learning

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do tópico **Algoritmos de Machine Learning**. Enquanto o módulo de [[00 - Índice|Fundamentos]] explicava *o que é* ML e *quais tarefas* existem, aqui aprendemos **os algoritmos concretos** que resolvem essas tarefas — como funcionam por dentro, suas fórmulas e exemplos práticos em Python.

---

## Roteiro de Estudo

### 1. Regressão Linear
- [[01 - Correlação e Regressão Linear]] — Relação entre variáveis, correlação (R), R², como a reta é construída.
- [[02 - Regressão Linear - Condições e Regressão Múltipla]] — Quando confiar no modelo, regressão simples vs. múltipla, colinearidade.
- [[03 - Cálculos da Regressão Linear]] — Passo a passo: correlação de Pearson, inclinação, interceptação, previsão.

### 2. Algoritmos Probabilísticos
- [[04 - Naive Bayes]] — Classificação usando o Teorema de Bayes e probabilidades.
- [[05 - Redes Bayesianas]] — Versão mais sofisticada, com relações de dependência entre atributos.

### 3. Árvores e Florestas
- [[06 - Árvores de Decisão]] — Estrutura, indução, medidas de pureza, poda.
- [[07 - Cálculos das Árvores de Decisão]] — Entropia e Ganho de Informação na prática, construindo uma árvore do zero.
- [[08 - Random Forest]] — Conjunto de árvores votando juntas (aprendizado em grupo/ensemble).

### 4. Aprendizado Baseado em Instância
- [[09 - Aprendizado Baseado em Instância e KNN]] — O algoritmo KNN, distância euclidiana, escolha do K.

### 5. Algoritmos Não Supervisionados
- [[10 - K-means]] — Agrupamento passo a passo com centróides.
- [[11 - Apriori]] — Regras de associação na prática, contando suporte.

---

## Mapa Mental: Qual Algoritmo Para Qual Tarefa?

```
                       ALGORITMOS DE ML
                              |
        ┌─────────────────────┼──────────────────────┐
        |                     |                      |
  SUPERVISIONADO       NÃO SUPERVISIONADO        (medir relação)
        |                     |                      |
  ┌─────┴──────┐        ┌──────┴──────┐         Regressão Linear
  |            |        |             |
Classificação Regressão Agrupamento  Regras Assoc.
  |            |          |             |
  • Naive Bayes • Regressão • K-means    • Apriori
  • Redes Bayes.  Linear
  • Árvore Decisão
  • Random Forest
  • KNN
```

---

## Resumo Ultra-Rápido (cola)

> [!summary] O que cada algoritmo faz
> - **Regressão Linear** → traça uma reta para prever números.
> - **Naive Bayes** → usa probabilidades; assume que atributos são independentes.
> - **Redes Bayesianas** → como Naive Bayes, mas modela dependências entre atributos.
> - **Árvore de Decisão** → série de perguntas "sim/não" até chegar na resposta.
> - **Random Forest** → várias árvores votando juntas.
> - **KNN** → "me diga com quem andas..." → classifica olhando os vizinhos mais próximos.
> - **K-means** → agrupa dados em K grupos usando centróides.
> - **Apriori** → encontra itens que aparecem frequentemente juntos.

---

## 🏷️ Tags Relacionadas
#machine-learning #algoritmos #ia #estudos

> [!tip] Conexão com o outro módulo
> Vale ter aberto também o módulo [[00 - Índice|Fundamentos de Machine Learning]] — conceitos como overfitting, matriz de confusão e tipos de tarefa são pré-requisito para este aqui.
