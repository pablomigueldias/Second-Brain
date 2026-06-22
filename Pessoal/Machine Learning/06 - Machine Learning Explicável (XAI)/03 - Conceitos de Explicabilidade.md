---
tags:
  - machine-learning
  - xai
  - explicabilidade
  - lime
  - shap
---

# 3. Conceitos de Explicabilidade

> [!info] O que esta nota cobre
> O vocabulário técnico de XAI: **funções monotônicas**, a diferença entre interpretar o **algoritmo** e o **modelo**, interpretação **local vs. global** e técnicas **agnósticas vs. específicas** (LIME e SHAP).

---

## 3.1. Funções: Linear, Monotônica e Não Monotônica

Entender **como uma variável afeta a saída** é central em explicabilidade. Há três comportamentos:

| Tipo | Comportamento | Exemplo (idade → custo) |
|---|---|---|
| **Linear / Monotônica** | Mesma direção, mudança **proporcional**. | Idade +1 → custo +x; idade +2 → custo +2x. |
| **Monotônica** | Direção sempre no **mesmo sentido**, mas a proporção **varia**. | Idade +1 → custo +x; idade −2 → custo −5,3x. |
| **Não Monotônica** | Direção **e** proporção podem mudar. | Idade +1 → custo −3,2x; idade −1 → custo +2,2x. |

> [!tip] Por que isso importa
> Modelos com relações **monotônicas** são muito mais **fáceis de explicar** ("quanto mais velho, mais caro, sempre"). Relações **não monotônicas** são confusas de justificar — e modelos complexos costumam criá-las.

---

## 3.2. Algoritmo vs. Modelo

> [!important] Duas coisas diferentes de "interpretar"
> - **Interpretar o algoritmo** = visão **agnóstica de dados**: entender *como o método funciona em geral* (ex.: como uma árvore de decisão escolhe divisões via **entropia** e **ganho de informação**).
> - **Interpretar o modelo** = visão de **caso específico**: entender *o modelo treinado com aqueles dados* (ex.: a árvore concreta que saiu, com "se aparência = ensolarado e umidade = alta → não joga").

> [!example] Interpretação de Algoritmo (árvore de decisão)
> A árvore decide as divisões maximizando o **Ganho de Informação**:
> $$ IG = \text{Entropia}_{pai} - \sum \text{Entropia}_{filhos} $$
> Isso é **agnóstico aos dados** — vale para qualquer árvore.

> [!example] Interpretação de Modelo (a árvore concreta)
> ```
>                 Aparência
>        ┌────────────┼────────────┐
>   Ensolarado     Nublado        Chuva
>      │             │              │
>   Umidade        SIM            Vento
>    │   │                        │    │
>  Alta Baixa                  Falso Verdad.
>  NÃO  SIM                     NÃO   NÃO
> ```
> Aqui você lê **decisões específicas** daquele modelo treinado.

---

## 3.3. Interpretação Local vs. Global

> [!note] Duas escalas de explicação
> - **Global:** explica o comportamento do modelo **como um todo** (quais variáveis ele mais usa, em geral).
> - **Local:** explica **uma previsão específica** (por que *este* cliente teve o crédito negado).

> [!example]
> Numa árvore: olhar a **árvore inteira** é global; seguir o **caminho de uma única instância** da raiz à folha é local.

---

## 3.4. Técnicas: Agnóstica vs. Específica

> [!note] Como aplicar XAI a modelos black-box
> - **Agnóstica (model-agnostic):** funciona com **qualquer** modelo, tratando-o como caixa-preta.
>   - Exemplo: **LIME** (*Local Interpretable Model-agnostic Explanations*).
> - **Específica (model-specific):** feita sob medida para **um tipo** de modelo.
>   - Exemplo: **Tree SHAP** (específico para árvores de decisão / ensembles).

> [!tip] Na prática
> - **LIME** aproxima localmente um modelo complexo por um modelo simples, para explicar **uma previsão**.
> - **SHAP** atribui a cada atributo uma "contribuição" para a previsão (baseado em teoria dos jogos — valores de Shapley). **Tree SHAP** é a versão otimizada para árvores.

---

## 3.5. Resumo

> [!summary] O essencial
> - **Funções monotônicas** são mais fáceis de explicar que não monotônicas.
> - **Interpretar algoritmo** (agnóstico aos dados) ≠ **interpretar modelo** (caso específico).
> - **Global** = o modelo todo; **Local** = uma previsão específica.
> - **Agnóstico** (LIME, qualquer modelo) vs. **Específico** (Tree SHAP, só árvores).

---

## 🔗 Próximos passos
- [[04 - Modelos White-Box e Black-Box]] — quais modelos já nascem interpretáveis e quais precisam dessas técnicas.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
