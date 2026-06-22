---
tags:
  - machine-learning
  - xai
  - explicabilidade
---

# 1. O que é XAI

> [!info] O que esta nota cobre
> O conceito de **XAI (eXplainable AI)**: o que significa "explicável", por que a explicabilidade **não é absoluta**, e a relação dela com complexidade e confiança.

---

## 1.1. O significado de "Explicável"

> [!note] Definição do dicionário
> **Explicável** (adjetivo): *"que se consegue explicar; em que há ou pode haver explicação"*.

**XAI** (eXplainable Artificial Intelligence) é o campo que busca tornar os modelos de IA **compreensíveis para humanos** — conseguir responder *"por que o modelo decidiu isso?"*.

---

## 1.2. Explicabilidade não é "tudo ou nada"

> [!important] Um espectro, não um interruptor
> A explicabilidade **não é uma avaliação absoluta**. Um modelo pode ser **mais ou menos** explicável. Não existe "explicável" vs. "não explicável" — existe um **grau**.

```
   Menos explicável  ◄─────────────────────►  Mais explicável
   Redes Neurais        SVM        Random Forest      Árvore     Regressão
   (caixa-preta)                                                  Linear
```

---

## 1.3. A relação: Complexidade × Capacidade × Explicabilidade

> [!warning] O trade-off central de XAI
> $$ \text{Complexidade} \;\uparrow\; \Rightarrow\; \text{Capacidade} \;\uparrow\; \Rightarrow\; \text{Explicabilidade} \;\downarrow $$
> Quanto **mais complexo** o modelo, **mais capacidade** ele tem de aprender padrões difíceis — mas **menos explicável** ele fica.

> [!example] Exemplo
> Uma **regressão linear** é simples e totalmente explicável (você lê os coeficientes), mas tem capacidade limitada. Uma **rede neural profunda** resolve problemas que a regressão nem sonha, mas é praticamente impossível dizer "por que" ela deu uma resposta específica.

---

## 1.4. Explicabilidade ≠ Confiança

> [!important] Cuidado com essa confusão
> **EXPLICABILIDADE NÃO SIGNIFICA NECESSARIAMENTE CONFIANÇA.**

> [!example] Por quê?
> Você pode ter um modelo **totalmente explicável** e descobrir, justamente por isso, que ele toma decisões por **razões erradas ou preconceituosas** — ou seja, explicar pode **revelar que NÃO se deve confiar**. Explicar é uma ferramenta para **avaliar** a confiança, não um carimbo de confiança.

---

## 1.5. Se você precisa de XAI

> [!summary] Duas estratégias
> 1. **Usar modelos com maior explicabilidade** (white-box: regressão, árvores) desde o início.
> 2. **Usar técnicas que melhoram a explicabilidade** de modelos complexos (ex.: LIME, SHAP — ver [[03 - Conceitos de Explicabilidade]]).

---

## 1.6. Resumo

> [!summary] O essencial
> - **XAI** = tornar a IA **compreensível** para humanos.
> - Explicabilidade é um **grau** (espectro), não um sim/não.
> - Trade-off: **+complexidade → +capacidade, −explicabilidade**.
> - **Explicar ≠ confiar** — explicar ajuda a **decidir** se dá para confiar.

---

## 🔗 Próximos passos
- [[02 - Por que um Modelo Precisa ser Explicável]] — as razões concretas (e os escândalos reais) que tornam XAI indispensável.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
