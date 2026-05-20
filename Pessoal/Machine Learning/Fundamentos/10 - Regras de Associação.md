---
tags:
  - machine-learning
  - regras-associação
  - apriori
  - fp-growth
  - market-basket
---

# 10. Regras de Associação

> [!info] O que esta nota cobre
> A tarefa de **Regras de Associação**: descobrir relações frequentes entre itens. As três métricas principais — **Suporte**, **Confiança** e **Lift** — com exemplos práticos. E os algoritmos clássicos: **Apriori** e **FP-Grow**.

---

## 10.1. Definição e Aplicações

> [!note] Definição
> **Regras de Associação** = tarefa que **busca a relação entre itens** em um conjunto de transações.

A regra clássica tem o formato:
> `{Item A} → {Item B}` (lê-se: "se Item A, então Item B")

### Aplicações

> [!example] Onde se aplica
> - 🛒 **Cesta de compras** (market basket analysis) → quem compra X também compra Y.
> - 🔒 **Detecção de intrusão** → identificar padrões de ataque.
> - 💬 **Análise de avaliações de consumidores**.
> - 🏥 **Diagnóstico médico** → padrões de sintomas que aparecem juntos.

O caso clássico (lendário no marketing): a história, real ou não, de que "**quem compra fralda também compra cerveja**" — descoberta por análise de cesta de compras em supermercados.

---

## 10.2. Os Três Conceitos Centrais

Toda regra de associação é avaliada por **três métricas**:

```
   Para a regra:  A  →  B   ("quem compra A também compra B")
                  │
       ┌──────────┼──────────┐
       │          │          │
    Suporte    Confiança    Lift
   (frequência) (probab.)  (força)
```

---

### 10.2.1. Suporte

> [!note] O que é
> O **suporte** indica a **frequência** com que os itens aparecem juntos no conjunto de transações.

Em outras palavras: nos ajuda a entender **com que frequência** dois itens são encontrados **juntos**.

#### Fórmulas

**Suporte de um item A:**
$$
\text{Suporte}(A) = \frac{\text{Número de transações contendo A}}{\text{Total de transações}}
$$

**Suporte de dois itens A e B juntos:**
$$
\text{Suporte}(A, B) = \frac{\text{Número de transações contendo A e B}}{\text{Total de transações}}
$$

> [!tip] Pense em suporte como "popularidade"
> Suporte alto = combinação frequente. Suporte baixo = combinação rara, talvez não vale a pena considerar.

---

### 10.2.2. Confiança

> [!note] O que é
> A **confiança** indica a **probabilidade** de que, havendo o item A, **também haverá** o item B na mesma transação.

#### Fórmula

$$
\text{Confiança}(A \rightarrow B) = \frac{\text{Suporte}(A, B)}{\text{Suporte}(A)}
$$

> [!tip] Pense em confiança como "probabilidade condicional"
> "Dado que A foi comprado, qual a chance de B também ter sido comprado?"

> [!warning] Atenção: confiança não é simétrica!
> $\text{Confiança}(A \rightarrow B) \neq \text{Confiança}(B \rightarrow A)$.
>
> Veja o exemplo na seção 10.3 — fica claro.

---

### 10.2.3. Lift (Força da Regra)

> [!note] O que é
> O **lift** mostra **se a associação entre os itens é positiva ou negativa**. É a "força" da regra — o quanto a presença de A **influencia** a presença de B.

#### Fórmula

$$
\text{Lift}(A \rightarrow B) = \frac{\text{Confiança}(A \rightarrow B)}{\text{Suporte}(B)}
$$

#### Interpretação

| Lift | Significado |
|---|---|
| **= 1** | A e B são **independentes** — a presença de A **não afeta** a probabilidade de B ser comprado. |
| **> 1** | **Associação positiva** — a presença de A **aumenta** a probabilidade de B ser comprado. |
| **< 1** | **Associação negativa** — a presença de A **diminui** a probabilidade de B ser comprado. |

> [!tip] Resumo prático
> - **Lift > 1** → regra interessante! Há uma associação real.
> - **Lift = 1** → regra "vazia", não conta uma história.
> - **Lift < 1** → A e B se "evitam" no carrinho.

---

## 10.3. Exemplo Prático Detalhado

Vamos imaginar **6 transações** de uma loja de roupas. Como exemplo conceitual:
- Número de transações com **camisa** = 3 → suporte de camisa = 3/6 = 0,5
- Número de transações com **calça** = 6 → suporte de calça = 6/6 = 1,0
- Número de transações com **boné** = 4 → suporte de boné = 4/6 ≈ 0,67
- Número de transações com **camisa E calça** = 3 → suporte conjunto = 3/6 = 0,5

Vamos analisar **três perguntas** diferentes.

---

### Pergunta 1: Quem compra **camisa** também compra **calça**?

Regra: **camisa → calça**

- **Suporte(camisa, calça)**: $\frac{3}{6} = 0{,}5$ (50% das transações têm os dois)
- **Confiança(camisa → calça)**: $\frac{\text{Suporte}(camisa, calça)}{\text{Suporte}(camisa)} = \frac{0{,}5}{0{,}5} = 1{,}0$
- **Lift(camisa → calça)**: $\frac{\text{Confiança}}{\text{Suporte}(calça)} = \frac{1{,}0}{1{,}0} = 1$

> [!summary] Interpretação
> - **Confiança = 100%** → sempre que alguém comprou camisa, comprou calça também.
> - **Lift = 1** → mas como calça é comprada por **todo mundo** (suporte = 1), isso na verdade **não diz muita coisa**. As compras de camisa e calça são **independentes**: o fato de alguém comprar camisa não aumenta nem diminui a probabilidade de comprar calça (porque todo mundo já compra calça mesmo).

---

### Pergunta 2: Quem compra **calça** também compra **camisa**?

Regra: **calça → camisa** *(direção contrária)*

- **Suporte(calça, camisa)**: $\frac{3}{6} = 0{,}5$ (mesmo valor — suporte é simétrico)
- **Confiança(calça → camisa)**: $\frac{0{,}5}{1{,}0} = 0{,}5$
- **Lift(calça → camisa)**: $\frac{0{,}5}{0{,}5} = 1$

> [!summary] Interpretação
> - **Confiança = 50%** → de quem comprou calça, só metade comprou camisa.
> - **Lift = 1** → mesma conclusão: as compras são independentes.
> - **Note que a confiança mudou!** Camisa → calça é 100%, mas calça → camisa é 50%. **A direção importa**.

> [!important] A grande lição
> Mesmo a confiança sendo 100% em "camisa → calça", o **lift = 1** revelou que a regra é **inútil**: ela só parecia forte porque calça é vendida em **todas** as transações. Se você comprar qualquer outra coisa, vai sempre dar 100% pra "calça também".

---

### Pergunta 3: Quem compra **boné** também compra **calça**?

Regra: **boné → calça**

- **Suporte(boné, calça)**: $\frac{4}{6} \approx 0{,}67$
- **Confiança(boné → calça)**: $\frac{0{,}67}{0{,}67} = 1{,}0$
- **Lift(boné → calça)**: $\frac{1{,}0}{1{,}0} = 1$

> [!summary] Interpretação
> Mesma história: confiança 100%, mas lift 1 → como calça é comprada por todo mundo, esse 100% de confiança não significa muita coisa.

---

### Conclusão dos exemplos

> [!important] Por que olhar os 3 juntos é crucial
> Em todos os exemplos, **confiança** dava **valores aparentemente bons**, mas o **lift** revelou que **não há associação real**. Por isso a regra prática é:
> 1. **Suporte alto** → a regra é frequente o suficiente para importar.
> 2. **Confiança alta** → a regra acerta com frequência.
> 3. **Lift > 1** → a regra é genuinamente útil (há associação real).
>
> **Procure regras com os três valores altos.**

---

## 10.4. Algoritmos: Apriori e FP-Grow

Calcular suporte/confiança/lift para **todas as combinações possíveis** de itens é computacionalmente **caro** — explodem rapidamente. Por isso usamos algoritmos especializados.

### 10.4.1. Apriori

> [!note] Definição
> **Apriori** é baseado no princípio de que:
>
> > **Se um conjunto de itens é frequente, um subconjunto destes itens também será frequente.**
>
> O princípio **contrário** também é válido:
>
> > **Se um conjunto de itens NÃO é frequente, nenhum superconjunto também será.**

#### O que isso quer dizer na prática?

Se `{pão, leite, queijo}` é frequente, então **com certeza** `{pão, leite}`, `{pão, queijo}` e `{leite, queijo}` também são frequentes.

Se `{pão, abacaxi}` **não** é frequente, então **com certeza** `{pão, abacaxi, qualquer-coisa}` também **não** é.

> [!tip] Por que isso ajuda?
> Permite **podar o espaço de busca**. O algoritmo descarta combinações sem chance, sem precisar avaliá-las uma por uma.

#### Fluxo simplificado do Apriori

1. Conte o suporte de **todos os itens individuais** (`L1`).
2. Filtre os que têm suporte ≥ mínimo definido.
3. Gere **pares** apenas com itens frequentes (`L2`).
4. Repita: gere **triplas**, **quádruplas**, etc., sempre usando só conjuntos frequentes do nível anterior.
5. A partir dos conjuntos frequentes, calcule **confiança** e **lift** para gerar as regras.

---

### 10.4.2. FP-Grow (Frequent Pattern Growth)

> [!note] Definição
> **FP-Grow** induz **árvores** e busca **sobreposições** dessas árvores, onde os itens são frequentes.

A grande sacada do FP-Grow é que ele **compacta** os dados em uma estrutura de árvore (a FP-tree) que evita ter que varrer o dataset inteiro várias vezes (problema clássico do Apriori).

> [!tip] FP-Grow vs. Apriori
> - **Apriori** → mais simples, mais didático, mas pode ser **lento** em datasets grandes (faz muitos passes pelos dados).
> - **FP-Grow** → mais complexo de implementar, porém geralmente **mais rápido** em datasets reais.

Os dois são os algoritmos **mais comuns** em mineração de regras de associação.

---

## 10.5. Resumo Final

> [!summary] O essencial de Regras de Associação
> - **Tarefa**: descobrir relações entre itens em transações.
> - **Aplicação clássica**: cesta de compras ("quem compra X também compra Y").
> - **Três métricas**:
>   - **Suporte** → quão frequente é a combinação.
>   - **Confiança** → probabilidade de Y dado X.
>   - **Lift** → se a associação é real (>1) ou ilusória (=1) ou negativa (<1).
> - **Sempre olhe as três juntas** — só confiança alta engana.
> - **Algoritmos**: **Apriori** (mais didático) e **FP-Grow** (mais rápido).
> - Pode ser supervisionado ou não supervisionado (geralmente é **não supervisionado**).

---

## 🎓 Você terminou o módulo!

Parabéns por chegar até o final dos **Fundamentos de Machine Learning**! 🎉

Você agora conhece:
- O que é ML e onde é aplicado.
- O vocabulário básico (instâncias, atributos, classes, tipos).
- As 4 tarefas principais (**classificação**, **regressão**, **agrupamento**, **regras de associação**).
- Como **avaliar** modelos de classificação e regressão.
- Como **preparar dados** (codificação e escalonamento).
- Como **agrupar** dados sem rótulo.
- Como **descobrir associações** entre itens.

> [!tip] Próximos estudos sugeridos (não estavam neste tópico)
> - Algoritmos específicos: **Árvores de Decisão**, **Random Forest**, **KNN**, **SVM**, **Naive Bayes**.
> - **Regressão Linear** e **Regressão Logística**.
> - **Redes Neurais** e **Deep Learning**.
> - **Aprendizado por Reforço**.
> - **Engenharia de Features** mais avançada.
> - **MLOps** (colocar modelos em produção).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
