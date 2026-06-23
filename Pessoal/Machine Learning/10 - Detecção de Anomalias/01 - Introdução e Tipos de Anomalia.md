---
tags:
  - machine-learning
  - detecção-anomalias
  - fundamentos
---

# 1. Introdução e Tipos de Anomalia

> [!info] O que esta nota cobre
> O que é uma **anomalia**, por que detectá-las **depende do contexto**, os **três tipos** (pontual, contextual e coletiva), as aplicações e o panorama das técnicas.

---

## 1.1. Não existem "regras gerais"

> [!important] A grande verdade da detecção de anomalias
> **Não existem regras gerais — tudo depende do contexto.**
> - Uma **compra** pode ser suspeita para um perfil de usuário e **normal** para outro.
> - Um **acesso** pode ser normal num contexto de negócio e **anormal** em outro.

> [!example]
> Uma compra de R$ 10.000 é "anomalia" na conta de um estudante, mas rotina na de uma empresa. O mesmo número, contextos diferentes, conclusões opostas.

---

## 1.2. Os três tipos de anomalia

### 1. Pontual (Point Anomalies)
> [!note]
> Um **único ponto** de dado que se desvia significativamente do restante.
> ```
>   • • • • • • • • • • • ✗ • • • • •
>                         ↑ ponto muito fora
> ```
> Ex.: uma transação de valor absurdamente alto isolada.

### 2. Contextual
> [!note]
> A anormalidade é **específica ao contexto**. Comum em **séries temporais**.
> ```
>   Gastar R$ 500 com sorvete... → normal no verão, anômalo no inverno
> ```
> O mesmo valor é normal ou anômalo **dependendo de quando/onde** ocorre.

### 3. Coletiva (Collective Anomalies)
> [!note]
> Um **conjunto de instâncias** que, **juntas**, formam uma anomalia — mesmo que cada uma isolada pareça normal.
> ```
>   Um login às 3h → talvez normal.
>   500 logins às 3h, todos da mesma conta → anomalia coletiva.
> ```

> [!summary] Comparação rápida
> | Tipo | A anomalia é... |
> |---|---|
> | **Pontual** | um ponto isolado fora do padrão |
> | **Contextual** | normal em geral, anômalo **naquele** contexto |
> | **Coletiva** | o **conjunto** é anômalo, não os pontos isolados |

---

## 1.3. Aplicações

> [!summary] Onde é usada
> - **Detecção de fraudes** em cartões de crédito ou seguros
> - **Detecção de intrusão** (segurança)
> - **Vigilância militar**
> - **Comportamento anormal de equipamentos** (manutenção preditiva)

---

## 1.4. As quatro famílias de técnicas

> [!note] O caminho do módulo
> | Família | Exemplos | Nota |
> |---|---|---|
> | **Estatísticas** | Z-Score, IQR | [[02 - Técnicas Estatísticas]] |
> | **Machine Learning** | LOF, Isolation Forest, One-Class SVM | [[03 - Machine Learning para Anomalias]] |
> | **Deep Learning** | Autoencoders, LSTM | [[04 - Deep Learning para Anomalias]] |
> | **Séries Temporais** | Moving Average, ARIMA | [[05 - Séries Temporais]] |

---

## 1.5. Resumo

> [!summary] O essencial
> - Anomalia **depende do contexto** — não há regra universal.
> - Três tipos: **pontual** (um ponto), **contextual** (depende do contexto), **coletiva** (o conjunto).
> - Aplicações: fraude, intrusão, vigilância, falhas em equipamentos.
> - Quatro famílias de técnicas: **estatística, ML, deep learning, séries temporais**.

---

## 🔗 Próximos passos
- [[02 - Técnicas Estatísticas]] — começando pelo mais simples: contar desvios em relação à média.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
