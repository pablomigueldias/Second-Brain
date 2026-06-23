---
tags:
  - machine-learning
  - moc
  - índice
  - detecção-anomalias
aliases:
  - Detecção de Anomalias
  - Anomaly Detection
---

# Detecção de Anomalias

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do módulo **10 — Detecção de Anomalias**. Como encontrar o que **foge do padrão** (fraudes, falhas, intrusões) usando quatro famílias de técnicas: **estatísticas, machine learning, deep learning e séries temporais**.

---

## Roteiro de Estudo

- [[01 - Introdução e Tipos de Anomalia]] — O que é anomalia, por que depende de contexto, e os 3 tipos (pontual, contextual, coletiva).
- [[02 - Técnicas Estatísticas]] — Z-Score, Modified Z-Score e IQR.
- [[03 - Machine Learning para Anomalias]] — LOF, Isolation Forest e One-Class SVM.
- [[04 - Deep Learning para Anomalias]] — Autoencoders e LSTM.
- [[05 - Séries Temporais]] — Moving Average, Exponential Smoothing, decomposição e ARIMA.

---

## Visão Geral em uma Imagem Mental

```
                Detecção de Anomalias
                         │
       ┌─────────┬───────┴────────┬──────────────┐
  Estatística    ML          Deep Learning   Séries Temporais
  Z-Score      LOF           Autoencoder     Moving Average
  IQR          Isolation F.  LSTM            ARIMA
               One-Class SVM
```

---

## Conceito-Chave Rápido (cola)

> [!summary] Para não esquecer
> - **Não existem "regras gerais"** — anomalia **depende do contexto**.
> - Três tipos: **pontual** (um ponto fora), **contextual** (fora **naquele** contexto), **coletiva** (o conjunto é anômalo).
> - Quatro famílias de técnicas: **estatística → ML → deep learning → séries temporais**.

---

## 🏷️ Tags Relacionadas
#machine-learning #anomalias #fraude #séries-temporais #estudos

---
[[_Índice Machine Learning|⬅️ Voltar ao Índice do Curso]]
