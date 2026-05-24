---
tags:
  - machine-learning
  - tópicos-avançados
  - seleção-de-atributos
  - pré-processamento
---

# 3. Seleção de Atributos

> [!info] O que esta nota cobre
> A **Seleção de Atributos** (feature selection): como decidir **quais características** — entre as naturais e as geradas — são realmente importantes. É a etapa 5 da [[01 - Engenharia de Atributos]].

---

## 3.1. O que é Seleção de Atributos?

> [!note] Definição
> **Seleção de Características Importantes** = definir **quais características** (tanto as "naturais" quanto as produzidas pela engenharia de atributos) são **mais importantes para a performance do modelo**.

> [!tip] Diferença para o PCA
> - **PCA** ([[02 - PCA - Redução de Dimensionalidade]]) → **cria** atributos novos.
> - **Seleção de Atributos** → **escolhe** um subconjunto dos atributos **originais**, mantendo a interpretabilidade.

---

## 3.2. Por que Selecionar? A Maldição da Dimensionalidade

> [!warning] Maldição da Dimensionalidade
> A inclusão de **muitas características** no modelo **deteriora sua performance**, tornando o modelo **super ajustado** (overfitting).

> [!important] Contra-intuitivo, mas verdadeiro
> Pode parecer que "mais atributos = mais informação = melhor". **Errado!** Atributos demais:
> - **Espalham** os dados (ficam esparsos).
> - Trazem **ruído** e redundância.
> - Aumentam o **custo computacional**.
> - Causam **overfitting** (o modelo "decora" detalhes inúteis).

> [!tip] Conexão
> Esse mesmo problema apareceu no One-Hot Encoding em [[07 - Codificação de Categorias]] e justifica o PCA em [[02 - PCA - Redução de Dimensionalidade]]. É um tema central em ML.

---

## 3.3. As Duas Perguntas: Quantos? Quais?

A seleção de atributos responde a duas perguntas:

> [!question] As perguntas centrais
> 1. **Quantos** atributos manter?
> 2. **Quais** atributos manter?

A pergunta que orienta tudo:

> [!important] A pergunta-guia
> *"Qual é o **subconjunto de atributos** que torna o modelo **mais genérico**?"*
>
> (Lembrando: "genérico" = que generaliza bem para dados novos, sem overfitting nem underfitting — ver [[04 - Classificação]] no módulo Fundamentos.)

---

## 3.4. O que Procurar em um Bom Conjunto de Atributos

> [!note] Critérios para um bom subconjunto
> - **Atributos generalistas** > atributos específicos demais — atributos que capturam padrões amplos generalizam melhor que atributos super-específicos.
> - **Atributos não correlacionados** entre si — atributos correlacionados carregam **informação repetida**; manter os dois não ajuda (relembra a **colinearidade** de [[02 - Regressão Linear - Condições e Regressão Múltipla]]).

> [!example] Generalista vs. específico
> Para prever se alguém vai pagar um empréstimo:
> - **Generalista**: `renda mensal` — útil para qualquer cliente.
> - **Específico demais**: `número exato da casa do cliente` — quase não ajuda a generalizar.

---

## 3.5. Técnicas de Seleção de Atributos

> [!note] Algumas técnicas
> - **Força Bruta** — testar **todas** as combinações possíveis de atributos e ver qual dá o melhor modelo.
> - **Testes Estatísticos** — usar estatística para medir a relação de cada atributo com a classe:
>   - **ANOVA** (Análise de Variância)
>   - **Chi-Square** (Qui-Quadrado)

### Força Bruta

> [!warning] Cara, mas completa
> A força bruta **garante** achar o melhor subconjunto, mas é **inviável** com muitos atributos — o número de combinações explode. Com 20 atributos, são mais de 1 milhão de combinações possíveis.

### Testes Estatísticos

> [!tip] Mais eficientes
> ANOVA e Chi-Square avaliam **cada atributo** quanto à sua relação estatística com a classe, e ranqueiam os mais relevantes. Bem mais rápido que força bruta.
> - **Chi-Square** → bom para atributos **categóricos**.
> - **ANOVA** → bom para atributos **numéricos** vs. classe categórica.

---

## 3.6. Exemplo em Python (notebook do curso)

O notebook `SelecaoAtributos.ipynb` usou **Chi-Square** para selecionar atributos do dataset `ad.data` (detecção de anúncios):

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import chi2, SelectKBest

anuncio = pd.read_csv('ad.data', header=None)
X = anuncio.iloc[:, :-1].values
y = anuncio.iloc[:, -1].values

# --- MODELO 1: usando TODOS os atributos ---
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)
modelo1 = GaussianNB()
modelo1.fit(X_tr, y_tr)
print("Acurácia com TODOS os atributos:",
      accuracy_score(y_te, modelo1.predict(X_te)))

# --- SELEÇÃO: escolher os 7 melhores atributos via Chi-Square ---
selecao = SelectKBest(chi2, k=7)
X_novo = selecao.fit_transform(X, y)
print("Atributos selecionados:", selecao.get_support())

# --- MODELO 2: usando só os 7 atributos selecionados ---
X_tr, X_te, y_tr, y_te = train_test_split(X_novo, y, test_size=0.3, random_state=0)
modelo2 = GaussianNB()
modelo2.fit(X_tr, y_tr)
print("Acurácia com 7 atributos:",
      accuracy_score(y_te, modelo2.predict(X_te)))
```

> [!tip] O `SelectKBest`
> `SelectKBest(chi2, k=7)` significa "selecione os **K=7 melhores** atributos segundo o teste **Chi-Square**". O `get_support()` mostra quais atributos foram escolhidos (True) e quais descartados (False).
>
> A lição do exercício: com **muito menos atributos**, o modelo pode manter (ou até melhorar) a acurácia — mais leve, mais rápido, menos overfitting.

---

## 3.7. Resumo

> [!summary] O essencial da Seleção de Atributos
> - **Selecionar** = escolher o melhor **subconjunto dos atributos originais** (mantém interpretabilidade).
> - Motivo: a **Maldição da Dimensionalidade** — atributos demais causam overfitting e custo.
> - Procure atributos **generalistas** e **não correlacionados** entre si.
> - **Técnicas**: Força Bruta (completa, mas cara) e Testes Estatísticos (**ANOVA**, **Chi-Square**).
> - Menos atributos, bem escolhidos → modelo mais genérico, leve e rápido.

---

## 🔗 Próximos passos
- [[04 - Avaliando a Variabilidade de um Modelo]] — começando a parte de avaliação rigorosa: o acerto de um modelo não é um número fixo.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
