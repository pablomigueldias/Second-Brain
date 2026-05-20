---
tags:
  - machine-learning
  - moc
  - índice
aliases:
  - ML
  - Fundamentos de ML
---

# Fundamentos de Machine Learning

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do tópico **Fundamentos de Machine Learning**. Aqui estão organizadas as anotações de tudo que foi visto: o que é ML, onde é aplicado, os principais conceitos, e as tarefas mais comuns (classificação, regressão, agrupamento e regras de associação).

---

## Roteiro de Estudo

A ordem abaixo é a recomendada para ler/revisar. Cada tópico se conecta ao próximo.

### 1. Fundamentos Conceituais
- [[01 - Introdução ao Machine Learning]] — O que é Machine Learning? Como uma máquina “aprende”?
- [[02 - Aplicações do Machine Learning]] — Onde ML é usado no mundo real.
- [[03 - Definições e Conceitos Básicos]] — Vocabulário essencial: instâncias, atributos, classes, tipos de dados e tarefas.

### 2. Aprendizado Supervisionado
- [[04 - Classificação]] — Como prever categorias. Treino, validação e teste. Overfitting e underfitting.
- [[05 - Avaliação de Performance e Matriz de Confusão]] — Métricas de classificação: acurácia, precisão, recall, F1, ROC.
- [[06 - Avaliação de Performance para Regressão]] — Métricas de erro: ME, MAE, RMSE, MPE, MAPE.

### 3. Preparação de Dados
- [[07 - Codificação de Categorias]] — Como transformar texto em número: Label Encoding e One-Hot Encoding.
- [[08 - Dimensionamento de Características]] — Padronização (Z-score) e Normalização (Min-Max).

### 4. Aprendizado Não Supervisionado
- [[09 - Agrupamentos (Clustering)]] — K-means, K-medoid, DBSCAN, hierárquico.
- [[10 - Regras de Associação]] — Suporte, Confiança, Lift. Apriori e FP-Grow.

---

## Visão Geral em uma Imagem Mental

```
                    Machine Learning
                          |
        ┌─────────────────┼──────────────────┐
        |                 |                  |
  Supervisionado     Não Supervisionado     Outros
        |                 |                  |
   ┌────┴────┐       ┌────┴─────┐    (Reforço, NLP,
   |         |       |          |     Semi-supervisionado,
Classificação Regressão Agrupamento Regras Assoc.  Redes Neurais...)
```

---

##  Conceitos-Chave Rápidos (cola)

> [!summary] Para você não esquecer
> - **Supervisionado** = tem rótulo (sabemos a “resposta certa”). Ex: classificar e-mail como spam.
> - **Não Supervisionado** = não tem rótulo (procuramos padrões). Ex: segmentar clientes.
> - **Classificação** = prever uma **categoria** (spam/não spam).
> - **Regressão** = prever um **número** (preço da casa).
> - **Agrupamento** = juntar coisas parecidas em grupos.
> - **Regras de Associação** = descobrir "quem compra X também compra Y".

---

## 🏷️ Tags Relacionadas
#machine-learning #ia #estudos #fundamentos
