---
tags:
  - machine-learning
  - classificação
  - métricas
  - matriz-de-confusão
  - avaliação
---
# 5. Avaliação de Performance e Matriz de Confusão

> [!info] O que esta nota cobre
> Como **medir** o desempenho de um classificador. Vamos entender a **Matriz de Confusão** (o ponto de partida de tudo), e a partir dela derivar todas as métricas clássicas: **acurácia**, **precisão**, **recall**, **especificidade**, **F1-Score** e **ROC/AUC**. Também vamos ver por que **só olhar acurácia é uma armadilha**.

---

## 5.1. O Exemplo de Referência: Concessão de Crédito

Para entender as métricas, vamos usar este dataset de **10 clientes** de um banco. Cada cliente tem uma classe real (`Class`: `good` ou `bad`) e uma previsão do modelo (`Prediction`).

| ID | Class (real) | Prediction (modelo) | Resultado |
|---|---|---|---|
| 1 | good | good | ✅ Correto |
| 2 | bad | bad | ✅ Correto |
| 3 | good | good | ✅ Correto |
| 4 | bad | **good** | ❌ Incorreto |
| 5 | good | good | ✅ Correto |
| 6 | bad | bad | ✅ Correto |
| 7 | good | **bad** | ❌ Incorreto |
| 8 | bad | **good** | ❌ Incorreto |
| 9 | good | good | ✅ Correto |
| 10 | bad | bad | ✅ Correto |

Considerando **`good` como a classe positiva**:

- **ID 1, 3, 5, 9** → previsto positivo, era positivo → **Verdadeiro Positivo (VP)**
- **ID 2, 6, 10** → previsto negativo, era negativo → **Verdadeiro Negativo (VN)**
- **ID 4, 8** → previsto positivo, era negativo → **Falso Positivo (FP)**
- **ID 7** → previsto negativo, era positivo → **Falso Negativo (FN)**

---

## 5.2. Matriz de Confusão

> [!note] Definição
> A **Matriz de Confusão** é uma tabela que **resume** os acertos e erros do classificador, separando por tipo.

### Estrutura geral

|  | **Classe Real Positiva** | **Classe Real Negativa** |
|---|---|---|
| **Classe Prevista Positiva** | Verdadeiros Positivos (**VP**) | Falsos Positivos (**FP**) |
| **Classe Prevista Negativa** | Falsos Negativos (**FN**) | Verdadeiros Negativos (**VN**) |

### Os 4 tipos de "resultado"

| Sigla | Nome | O que significa | Exemplo (good/bad) |
|---|---|---|---|
| **VP** | Verdadeiro Positivo | Previsto positivo, era positivo | Modelo disse "good", era "good" |
| **VN** | Verdadeiro Negativo | Previsto negativo, era negativo | Modelo disse "bad", era "bad" |
| **FP** | Falso Positivo | Previsto positivo, era negativo | Modelo disse "good", era "bad" |
| **FN** | Falso Negativo | Previsto negativo, era positivo | Modelo disse "bad", era "good" |

> [!tip] Macete para lembrar
> O **primeiro nome** diz se o modelo **acertou** (Verdadeiro) ou **errou** (Falso).
> O **segundo nome** diz **o que o modelo disse** (Positivo ou Negativo).

### Matriz de Confusão do nosso exemplo

Contando os 10 clientes:

|  | **Verd. Good** | **Verd. Bad** |
|---|---|---|
| **Prev Good** | 4 (VP) | 2 (FP) |
| **Prev Bad** | 1 (FN) | 3 (VN) |

> [!example] Verificando
> - VP = 4 (IDs 1, 3, 5, 9)
> - FP = 2 (IDs 4, 8 — previu "good" mas era "bad")
> - FN = 1 (ID 7 — previu "bad" mas era "good")
> - VN = 3 (IDs 2, 6, 10)
> - **Total**: 4 + 2 + 1 + 3 = 10 ✅

---

## 5.3. Métricas Derivadas da Matriz de Confusão

A partir da matriz, calculamos várias métricas, cada uma respondendo a uma **pergunta diferente**.

---

### 5.3.1. Acurácia

> [!note] Pergunta que responde
> "No total, **quantas previsões o modelo acertou**?"

**Fórmula:**
$$
\text{Acurácia} = \frac{VP + VN}{VP + VN + FP + FN}
$$

**Cálculo no exemplo:**
$$
\text{Acurácia} = \frac{4 + 3}{4 + 3 + 2 + 1} = \frac{7}{10} = 0{,}70 = 70\%
$$

> [!summary] Interpretação
> O modelo classificou **corretamente 70%** das instâncias.

✅ **Vantagem:** simples de entender.
❌ **Desvantagem:** **enganosa em datasets desbalanceados** (veja [[05 - Avaliação de Performance e Matriz de Confusão#5.4. A Armadilha da Acurácia]]).

---

### 5.3.2. Precisão (Precision)

> [!note] Pergunta que responde
> "**Das vezes que o modelo previu positivo**, quantas estavam realmente certas?"

**Fórmula:**
$$
\text{Precisão} = \frac{VP}{VP + FP}
$$

**Cálculo no exemplo:**
$$
\text{Precisão} = \frac{4}{4 + 2} = \frac{4}{6} \approx 0{,}67 = 67\%
$$

> [!summary] Interpretação
> Das instâncias previstas como positivas, **67% eram realmente positivas**.

> [!tip] Quando focar em precisão
> Quando o **custo de um falso positivo é alto**. Ex: filtros de spam — você prefere deixar um spam passar do que mandar um e-mail importante para a lixeira.

---

### 5.3.3. Recall (Sensibilidade / Taxa de Verdadeiros Positivos)

> [!note] Pergunta que responde
> "**Dos casos que eram realmente positivos**, quantos o modelo conseguiu identificar?"

**Fórmula:**
$$
\text{Recall} = \frac{VP}{VP + FN}
$$

**Cálculo no exemplo:**
$$
\text{Recall} = \frac{4}{4 + 1} = \frac{4}{5} = 0{,}80 = 80\%
$$

> [!summary] Interpretação
> O modelo identificou corretamente **80% das instâncias positivas** (good).

> [!tip] Quando focar em recall
> Quando o **custo de um falso negativo é alto**. Ex: diagnóstico de câncer — é muito pior deixar passar um caso real do que dar um alarme falso.

---

### 5.3.4. Especificidade (Specificity)

> [!note] Pergunta que responde
> "**Dos casos que eram realmente negativos**, quantos o modelo conseguiu identificar como negativos?"

**Fórmula:**
$$
\text{Especificidade} = \frac{VN}{VN + FP}
$$

**Cálculo no exemplo:**
$$
\text{Especificidade} = \frac{3}{3 + 1} = \frac{3}{4} = 0{,}75 = 75\%
$$

> [!summary] Interpretação
> O modelo identificou corretamente **75% das instâncias negativas** como negativas.

> [!tip] Especificidade vs. Recall
> - **Recall** mede acerto na classe **positiva**.
> - **Especificidade** mede acerto na classe **negativa**.

---

### 5.3.5. F1-Score

> [!note] Pergunta que responde
> "Como está o **equilíbrio** entre precisão e recall?"

O F1-Score é a **média harmônica** entre precisão e recall — uma forma de combinar as duas métricas em um único número.

**Fórmula:**
$$
F1 = 2 \times \frac{\text{Precisão} \times \text{Recall}}{\text{Precisão} + \text{Recall}}
$$

**Cálculo no exemplo:**
$$
F1 = 2 \times \frac{0{,}67 \times 0{,}80}{0{,}67 + 0{,}80} = 2 \times \frac{0{,}536}{1{,}47} \approx 0{,}73
$$

> [!summary] Interpretação
> O valor **0,73** indica que há um **equilíbrio razoável** entre precisão e recall.

> [!tip] Por que média harmônica e não média comum?
> A média harmônica **pune valores muito baixos**. Se a precisão for 0,99 e o recall for 0,01, a média comum daria 0,50 (parece OK), mas o F1 daria apenas 0,02 (reflete que algo está errado). Ou seja, **F1 só é alto se precisão E recall forem altos**.

---

## 5.4. A Armadilha da Acurácia

> [!warning] Atenção, este é um dos pontos mais importantes!
> Em muitos problemas reais, **só olhar acurácia leva a conclusões completamente erradas**.

### Caso 1: Dataset Desbalanceado

Imagine um dataset com:
- **990 instâncias** da classe `bad`
- **10 instâncias** da classe `good`

Agora suponha que o modelo seja **burro**: ele **sempre classifica tudo como `bad`**.

|  | Verd. Good | Verd. Bad |
|---|---|---|
| Prev Good | 0 | 0 |
| Prev Bad | 10 | 900 |

> Obs.: foram usadas 910 instâncias no exemplo do material (não as 1000), mas a lógica é a mesma.

**Métricas desse modelo "burro":**
- **Acurácia: 99%** (acerta quase tudo, porque a classe majoritária é gigantesca)
- **Recall (good): 0%** (não identificou **nenhum** caso positivo)

> [!danger] Lição
> Um modelo com **99% de acurácia** pode ser **completamente inútil**. Se a tarefa era achar os "good" (a classe minoritária), esse modelo falhou totalmente.

#### Causa: Problema da Classe Rara

Quando uma classe é muito rara, o modelo "se acomoda" prevendo sempre a majoritária. Soluções incluem:

- **Amostragem aleatória sem reposição** balanceada (forçar proporções iguais).
- Ex.: de 1 milhão de transações (5% fraudulentas), pegar 10.000 com 50% legítimas e 50% fraudulentas, em vez de manter a proporção original.

### Caso 2: Custos Diferentes (Doença Rara)

População de 1000 pessoas:
- **950 Saudáveis**
- **50 Doentes**

Resultados do modelo:

|  | Verd. Saudável | Verd. Doente |
|---|---|---|
| Prev Saudável | 950 | 30 |
| Prev Doente | 10 | 20 |

**Métricas:**
- **Acurácia: 96%** — parece ótimo!
- **Precisão: 67%**
- **Recall: 40%** — só identificou 40% dos doentes!
- **F1-Score: 50%**

> [!danger] Lição
> Em diagnóstico médico, **deixar passar um doente** (FN) é MUITO pior do que **dar um alarme falso** (FP). A acurácia esconde isso. **Recall** mostra a verdade: o modelo só pega 40% dos doentes — inaceitável.

### Moral da história

> [!important] Regra prática
> **Nunca avalie um classificador olhando apenas a acurácia.** Sempre olhe a **matriz de confusão completa** e escolha as métricas adequadas ao seu problema:
> - Precisa achar **todos os casos positivos**? → **Recall**
> - Precisa que os alarmes sejam **confiáveis**? → **Precisão**
> - Precisa de **equilíbrio**? → **F1-Score**
> - Classes desbalanceadas? → **Recall, F1, ROC/AUC**

---

## 5.5. ROC e AUC-ROC

> [!note] O que são
> - **ROC** (*Receiver Operating Characteristic*): um **gráfico** que mostra a **performance de um classificador binário** em diferentes limiares de decisão.
> - **AUC-ROC** (*Area Under the ROC Curve*): a **área embaixo da curva ROC** — um **número único** entre 0 e 1.

### Como interpretar o AUC-ROC

| Valor de AUC | Interpretação |
|---|---|
| **= 1** | Classificador perfeito |
| **0,9 – 1,0** | Excelente |
| **0,8 – 0,9** | Bom |
| **0,7 – 0,8** | Razoável |
| **0,6 – 0,7** | Fraco |
| **= 0,5** | Equivalente a chute aleatório (moeda) |
| **< 0,5** | Pior que aleatório (algo está invertido) |

> [!summary] Em uma frase
> **Quanto mais próximo de 1**, melhor a performance do classificador.

✅ **Vantagem do ROC/AUC:** não depende de um limiar específico, funciona bem em dados desbalanceados.

---

## 5.6. Problemas de Atributos Desconhecidos

> [!warning] Cuidado adicional
> Pode acontecer do modelo ver, **em produção**, valores de atributos que **nunca apareceram** no treino.

> [!example] Exemplo
> - **No treino**: regiões `"Sul"`, `"Sudeste"`, `"Centro-Oeste"` e `"Norte"`.
> - **Em produção**: aparece uma instância da região `"Nordeste"`.
>
> O modelo nunca viu `"Nordeste"` — como vai reagir?

Esse é um problema sério: o modelo pode dar resultados imprevisíveis, ou simplesmente quebrar. Estratégias para lidar com isso:

- **Tratar valores desconhecidos** durante o pré-processamento (categoria "outros").
- **Re-treinar** o modelo periodicamente com dados atualizados.
- **Monitorar** as previsões em produção e detectar **data drift** (mudança na distribuição dos dados).

---

## 5.7. Tabela-Resumo das Métricas

| Métrica | Fórmula | O que mede | Ideal quando... |
|---|---|---|---|
| **Acurácia** | `(VP+VN)/(VP+VN+FP+FN)` | % de acertos totais | Classes balanceadas |
| **Precisão** | `VP/(VP+FP)` | Confiabilidade dos positivos previstos | FP é caro (spam) |
| **Recall** | `VP/(VP+FN)` | Cobertura dos positivos reais | FN é caro (câncer) |
| **Especificidade** | `VN/(VN+FP)` | Cobertura dos negativos reais | FP é caro |
| **F1-Score** | `2·(P·R)/(P+R)` | Equilíbrio entre P e R | Quer um número só |
| **AUC-ROC** | Área sob curva ROC | Performance geral entre limiares | Comparação de modelos |

---

## 🔗 Próximos passos
- [[06 - Avaliação de Performance para Regressão]] — agora as métricas para quando a saída é um **número**, não uma categoria.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
