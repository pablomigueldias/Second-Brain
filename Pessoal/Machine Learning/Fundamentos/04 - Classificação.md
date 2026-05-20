---
tags:
  - machine-learning
  - classificação
  - supervisionado
  - validação
  - overfitting
---

# 4. Classificação

> [!info] O que esta nota cobre
> O conceito de classificação, como construir e medir o desempenho de um classificador, as **técnicas de validação** (Hold-Out, Validação Cruzada, Leave-One-Out, K-Fold, Subamostragem) e os problemas de **super ajuste** (overfitting) e **sub ajuste** (underfitting).

---

## 4.1. O que é Classificação?

> [!note] Definição
> **Classificação** é a tarefa de **prever ou descrever a classe** de um evento/instância.

A classe normalmente está em um atributo **especial**, posicionado como **última coluna** da tabela.

### Exemplos rápidos
- E-mail → **spam** ou **não spam**.
- Compra → **fraudulenta** ou **legítima**.
- Paciente → **saudável** ou **doente**.
- Cliente de banco → empréstimo **aprovado** ou **reprovado**.
- Imagem → **gato**, **cachorro** ou **pássaro**.

> [!tip] Binária vs. multiclasse
> - **Classificação binária** = 2 classes (spam/não spam).
> - **Classificação multiclasse** = mais de 2 classes (gato/cachorro/pássaro).

---

## 4.2. Como um Modelo de Classificação "Pensa"?

Um modelo aprende a associar **características da instância** à **classe**. Por exemplo, num filtro de spam:

| Palavra | P(Spam) | P(Não Spam) |
|---|---|---|
| oferta | 0,9 | 0,1 |
| ganhe | 0,8 | 0,2 |
| preço | 0,3 | 0,7 |
| grátis | 0,7 | 0,3 |

O modelo aprendeu que "oferta" e "ganhe" são fortemente associadas a spam, enquanto "preço" aparece mais em e-mails legítimos. Para um e-mail novo, ele combina essas probabilidades e decide a classe.

> [!note] Importante
> Esse é só um esquema didático. Existem muitos algoritmos diferentes para classificação (árvores de decisão, Naive Bayes, KNN, SVM, redes neurais, etc.), cada um com sua forma de "pensar".

---

## 4.3. Medindo o Desempenho do Modelo

> [!warning] Pergunta-chave
> Como saber se o modelo aprendeu **de verdade**, e não só **decorou** os exemplos do treino?

A resposta é: **separar os dados** em conjuntos diferentes.

### Os três conjuntos típicos

```
   DADOS ORIGINAIS
        │
        ├──▶ TREINO       — algoritmo processa os dados e CRIA o modelo
        │
        ├──▶ VALIDAÇÃO    — dados usados para AJUSTAR o modelo
        │                   (escolher hiperparâmetros, comparar versões)
        │
        └──▶ TESTE        — dados usados para AVALIAR a performance final
```

- **Treino** → "estudar". O modelo vê esses dados e ajusta seus parâmetros.
- **Validação** → "fazer simulado". Usados para ajustar configurações (hiperparâmetros) e comparar versões do modelo.
- **Teste** → "prova final". Dados que o modelo **nunca viu** — servem para medir a performance real.

> [!warning] Regra de ouro
> O modelo **nunca** pode "espiar" os dados de teste durante o treino. Caso contrário, a avaliação fica viciada.

---

## 4.4. Técnicas de Validação

Como exatamente separamos os dados em treino/teste? Existem várias estratégias.

### 4.4.1. Hold-Out

> [!note] Como funciona
> **Divide os dados em treino e teste**, geralmente uma única vez. Ex.: 70% treino / 30% teste, ou 80/20.

```
   ┌──────────────────────┬──────────┐
   │       TREINO         │   TESTE  │
   │        (70%)         │   (30%)  │
   └──────────────────────┴──────────┘
```

✅ **Prós:** simples, rápido.
❌ **Contras:** o resultado depende muito da sorte da divisão — uma divisão "ruim" pode dar uma avaliação enganosa.

---

### 4.4.2. Validação Cruzada (Cross-Validation)

> [!note] Como funciona
> **Divide os dados em vários conjuntos menores** e faz várias rodadas de treino/teste, alternando qual conjunto é o teste.

A ideia é tirar a sorte da equação: o modelo é treinado e testado várias vezes, em divisões diferentes, e o desempenho final é a **média** das rodadas.

---

### 4.4.3. K-Fold (uma forma de Validação Cruzada)

> [!note] Como funciona
> Divide o conjunto de dados em **k subconjuntos** (folds). Treina em **k − 1** subconjuntos e avalia no **subconjunto restante**. Repete **k vezes**, mudando qual fold é o teste.

```
   K = 5 folds:

   Rodada 1:  [TESTE] [trein] [trein] [trein] [trein]
   Rodada 2:  [trein] [TESTE] [trein] [trein] [trein]
   Rodada 3:  [trein] [trein] [TESTE] [trein] [trein]
   Rodada 4:  [trein] [trein] [trein] [TESTE] [trein]
   Rodada 5:  [trein] [trein] [trein] [trein] [TESTE]

   Performance final = média das 5 rodadas
```

✅ **Prós:** usa todos os dados tanto pra treino quanto pra teste. Avaliação mais estável.
❌ **Contras:** treina o modelo **k vezes** — mais lento.

> [!tip] Valor comum
> `k = 5` ou `k = 10` são os mais usados na prática.

---

### 4.4.4. Leave-One-Out (LOO)

> [!note] Como funciona
> É um **caso extremo** de validação cruzada: treina com **todos os dados menos um** e testa com **esse único exemplo**. Repete o processo para **cada instância** do conjunto.

Se você tem 100 instâncias, você treina 100 modelos diferentes, cada um testado em uma única instância.

✅ **Prós:** máximo aproveitamento dos dados (importante para datasets pequenos).
❌ **Contras:** **muito** lento. Inviável para datasets grandes.

---

### 4.4.5. Subamostragem (Subsampling)

> [!note] Como funciona
> Técnica que envolve a **seleção aleatória** de uma **amostra** do conjunto de dados original para treinar o modelo.

> [!example] Quando é útil
> Quando o dataset é **gigante** e você quer treinar mais rápido, ou quando há um problema de **classes desbalanceadas** (mais sobre isso em [[05 - Avaliação de Performance e Matriz de Confusão]]).

---

### 4.4.6. Tabela-Resumo das Técnicas de Validação

| Técnica | Em uma frase | Quando usar |
|---|---|---|
| **Hold-Out** | Divide uma vez em treino/teste | Rápido, datasets grandes |
| **Validação Cruzada** | Várias divisões diferentes | Avaliação mais robusta |
| **K-Fold** | Divide em k partes, alterna teste | Padrão da indústria |
| **Leave-One-Out** | Cada instância vira teste uma vez | Datasets muito pequenos |
| **Subamostragem** | Treina com uma amostra aleatória | Dados gigantes ou desbalanceados |

---

## 4.5. Generalização vs. Super Ajuste vs. Sub Ajuste

Aqui chegamos ao **conceito mais importante** sobre classificação (e sobre ML em geral).

> [!important] O objetivo
> O objetivo de **todo classificador** é criar **modelos genéricos** — modelos que funcionem bem em dados **novos**, que ele **nunca viu**. Isso se chama **generalização**.

Quando o modelo não generaliza bem, ele cai num de dois extremos: **super ajuste** (overfitting) ou **sub ajuste** (underfitting).

```
              Sub Ajuste  →   Genérico   ←  Super Ajuste
            (muito simples)   (ideal)     (muito complexo)
```

---

### 4.5.1. Super Ajuste (Overfitting)

> [!warning] Definição
> O modelo super ajustado **funciona muito bem com dados de treino**, mas tem **desempenho pobre em dados de teste ou de produção**.

É como um aluno que **decora** as questões do livro, mas não consegue resolver uma questão nova da prova. Ele aprendeu **detalhes específicos** dos exemplos em vez de **padrões gerais**.

#### Causas do Super Ajuste

1. **Tamanho insuficiente** do conjunto de dados (poucos exemplos para o modelo entender o que generaliza).
2. **Complexidade excessiva** do modelo de treinamento (modelo "complicado demais" para o problema).
3. **Ruído** nos dados de treinamento (o modelo aprende erros como se fossem padrões).
4. **Seleção inadequada** de atributos (atributos que confundem o modelo).
5. **Falta de validação cruzada** (sem validar, não percebemos o problema).

#### Como combater
- Mais dados de treino.
- Modelo mais simples.
- **Regularização** (técnicas que penalizam modelos muito complexos).
- Validação cruzada para detectar.
- Limpeza/remoção de ruído.

---

### 4.5.2. Sub Ajuste (Underfitting)

> [!warning] Definição
> O modelo de machine learning **não consegue se ajustar bem aos dados de treinamento**, e portanto também **não generaliza** para dados novos.

É o oposto do super ajuste: aqui o modelo é tão **simplório** que nem nos dados que ele viu ele acerta direito.

#### Causas do Sub Ajuste

1. **Modelo muito simples** (não dá conta da complexidade do problema).
2. **Conjunto de dados muito pequeno** (não tem informação suficiente).
3. **Seleção inadequada de atributos** (faltam características importantes).
4. **Falta de ajuste de hiperparâmetros** (modelo mal configurado).

#### Como combater
- Modelo mais complexo / poderoso.
- Adicionar atributos relevantes (engenharia de features).
- Ajustar hiperparâmetros.
- Treinar por mais tempo (em modelos iterativos).

---

### 4.5.3. Comparação Visual

| Aspecto | Sub Ajuste | Genérico (ideal) | Super Ajuste |
|---|---|---|---|
| Desempenho no **treino** | 😞 Ruim | 🙂 Bom | 🤩 Excelente |
| Desempenho no **teste** | 😞 Ruim | 🙂 Bom | 😞 Ruim |
| Complexidade do modelo | Muito baixa | Adequada | Muito alta |
| Diagnóstico | Modelo "burro" | ✅ ideal | Modelo "decorou" |

> [!tip] Sinal de overfitting
> Se a **acurácia no treino** é **muito maior** que a **acurácia no teste**, provavelmente tem overfitting.

> [!tip] Sinal de underfitting
> Se as **duas acurácias são ruins** (treino baixo, teste baixo), provavelmente tem underfitting.

---

## 4.6. Resumo Visual do Capítulo

```
 ┌────────────────────────────────────────────────────────────┐
 │                       CLASSIFICAÇÃO                         │
 │                                                            │
 │   1. Separar os dados (Hold-Out, K-Fold, etc.)             │
 │                          │                                  │
 │                          ▼                                  │
 │   2. Treinar o modelo (treino)                             │
 │                          │                                  │
 │                          ▼                                  │
 │   3. Ajustar (validação)                                   │
 │                          │                                  │
 │                          ▼                                  │
 │   4. Avaliar (teste)                                       │
 │                          │                                  │
 │                          ▼                                  │
 │   5. Verificar: super ajustou? sub ajustou? generalizou?   │
 └────────────────────────────────────────────────────────────┘
```

---

## 🔗 Próximos passos
- [[05 - Avaliação de Performance e Matriz de Confusão]] — agora que sabemos *separar* os dados, vamos aprender as **métricas** que medem o desempenho.

---
[[00 - Índice|⬅️ Voltar ao Índice]]