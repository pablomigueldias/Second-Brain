---
tags:
  - machine-learning
  - tópicos-avançados
  - avaliação
  - custo
  - negócio
---

# 6. Custo de um Modelo

> [!info] O que esta nota cobre
> Por que **nem todo erro custa o mesmo**, e por que o melhor modelo nem sempre é o de maior precisão. Vamos aprender a avaliar modelos pelo **custo em dinheiro** dos seus erros — a métrica que realmente importa para o negócio.

---

## 6.1. O Cenário: Prevenção de Fraude

> [!example] A situação
> Um sistema de concessão de empréstimos, treinado com **1.000 registros**. Temos dois modelos candidatos:
>
> | | **Modelo A** | **Modelo B** |
> |---|---|---|
> | **Precisão** | 70% | 69% |
> | **Falsos Positivos** | 250 (25%) | 230 (23%) |
> | **Falsos Negativos** | 50 (5%) | 80 (8%) |

> [!question] A pergunta óbvia (e enganosa)
> O Modelo A tem **70%** de precisão e o B tem **69%**. Então o **A é melhor**, certo?
>
> **Não necessariamente!** Vamos ver por quê.

---

## 6.2. O que Significam os Erros Aqui?

> [!important] Os dois tipos de erro têm naturezas DIFERENTES
> No contexto de empréstimos:
>
> - **Falso Positivo (FP)** → maus pagadores que o modelo **aprovou** por engano. Você **cede o empréstimo** e a pessoa não paga. → **Prejuízo direto!**
> - **Falso Negativo (FN)** → bons pagadores que o modelo **rejeitou** por engano. Você **não cede** o empréstimo a quem pagaria. → **Perdeu o negócio.**

> [!note] Resumindo o impacto
> - **Falso Positivo** → **Perda de Dinheiro** (você emprestou e levou o calote).
> - **Falso Negativo** → **Perda de Oportunidade** (você deixou de ganhar com um bom cliente).

> [!tip] Relembrando
> Os conceitos de FP e FN vêm da **Matriz de Confusão**, em [[05 - Avaliação de Performance e Matriz de Confusão]] no módulo Fundamentos. A novidade aqui é dar a eles um **valor em reais**.

---

## 6.3. A Chave: Cada Erro Tem um Custo Diferente

> [!important] Os custos no exemplo
> - **Ceder empréstimo a um mau pagador** (FP): perda média de **R$ 1.000,00**.
> - **Perder uma oportunidade de empréstimo** (FN): perda média de **R$ 450,00**.

> [!warning] Ponto crucial
> Um Falso Positivo custa **mais que o dobro** de um Falso Negativo! Isso significa que o modelo que comete **menos Falsos Positivos** pode ser melhor — **mesmo tendo precisão menor**.

---

## 6.4. Calculando o Custo Real de Cada Modelo

Agora vamos traduzir os erros em **dinheiro**.

### Modelo A (250 FP, 50 FN)

| Tipo de Perda | Cálculo | Valor |
|---|---|---|
| Perda de Dinheiro (FP) | 250 × R$ 1.000 | R$ 250.000 |
| Perda de Oportunidade (FN) | 50 × R$ 450 | R$ 22.500 |
| **PERDA TOTAL** | | **R$ 272.500** |

### Modelo B (230 FP, 80 FN)

| Tipo de Perda | Cálculo | Valor |
|---|---|---|
| Perda de Dinheiro (FP) | 230 × R$ 1.000 | R$ 230.000 |
| Perda de Oportunidade (FN) | 80 × R$ 450 | R$ 36.000 |
| **PERDA TOTAL** | | **R$ 266.000** |

### A comparação final

| Modelo | Precisão | **Perda Total** |
|---|---|---|
| **Modelo A** | 70% (maior) | R$ 272.500 |
| **Modelo B** | 69% (menor) | **R$ 266.000** ✅ |

---

## 6.5. A Conclusão Surpreendente

> [!success] O Modelo B é melhor!
> Apesar de ter **precisão menor** (69% vs. 70%), o **Modelo B custa R$ 6.500 a menos** por rodada.
>
> Por quê? Porque o Modelo B comete **menos Falsos Positivos** — e Falso Positivo é o erro **caro** (R$ 1.000 cada). Ele troca erros caros (FP) por erros baratos (FN).

> [!important] A grande lição desta nota
> **A métrica que importa é o custo do negócio, não a métrica de ML.** Um modelo com precisão menor pode ser **financeiramente melhor** se errar "do jeito certo" — cometendo os erros que custam menos.
>
> Sempre que possível, avalie modelos pelo **impacto em R$**, não só por acurácia/precisão.

---

## 6.6. Por que Isso é Tão Importante?

> [!tip] Conexão com a "Armadilha da Acurácia"
> Em [[05 - Avaliação de Performance e Matriz de Confusão]] vimos que "não devemos olhar apenas a acurácia". Esta nota leva isso adiante: **nem mesmo precisão/recall contam a história toda**. O que conta é: *quanto isso custa (ou rende) para o negócio?*

> [!example] Outro jeito de ver
> Imagine um modelo médico:
> - Falso Negativo (dizer que um doente está saudável) → pode **custar uma vida**.
> - Falso Positivo (dizer que um saudável está doente) → custa um exame extra.
> Aqui o FN é incomparavelmente mais "caro". O modelo deve ser escolhido considerando **essa assimetria**, não a acurácia.

---

## 6.7. Como "Melhorar" um Modelo?

Já que queremos reduzir o custo, como melhoramos um modelo? O curso lista as opções:

> [!note] Formas de melhorar um modelo
> 1. **Testar diferentes algoritmos** — Naive Bayes, Árvores, Random Forest, etc.
> 2. **Parametrizar algoritmos** — ajustar os hiperparâmetros (tema de [[10 - AutoML e Tuning de Modelos]]).
> 3. **Selecionar e tratar os dados** — engenharia de atributos ([[01 - Engenharia de Atributos]]).
> 4. **Seleção de atributos** — escolher as melhores características ([[03 - Seleção de Atributos]]).

```
   MELHORAR UM MODELO
        │
        ├─ Trocar de algoritmo
        ├─ Ajustar hiperparâmetros  ──▶ ver AutoML
        ├─ Tratar os dados          ──▶ ver Engenharia de Atributos
        └─ Selecionar atributos     ──▶ ver Seleção de Atributos
```

> [!tip] O objetivo de "melhorar"
> No fim, "melhorar" significa **reduzir o custo total** dos erros — não apenas subir uma métrica abstrata.

---

## 6.8. Resumo

> [!summary] O essencial do Custo de um Modelo
> - **Nem todo erro custa o mesmo** — Falso Positivo e Falso Negativo têm impactos diferentes.
> - **FP** → perda de **dinheiro**; **FN** → perda de **oportunidade** (no contexto de empréstimo).
> - Traduza os erros em **R$**: `custo = (nº FP × custo FP) + (nº FN × custo FN)`.
> - Um modelo com **precisão menor** pode ter **custo menor** — e ser a melhor escolha.
> - Avalie modelos pelo **impacto no negócio**, não só pela métrica de ML.
> - Para melhorar: trocar algoritmo, ajustar hiperparâmetros, tratar dados, selecionar atributos.

---

## 🔗 Próximos passos
- [[07 - Técnicas Avançadas de Clusters]] — entrando nas técnicas avançadas por tarefa, começando por agrupamento.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
