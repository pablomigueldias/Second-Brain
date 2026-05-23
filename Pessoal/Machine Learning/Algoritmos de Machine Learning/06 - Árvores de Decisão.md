---
tags:
  - machine-learning
  - algoritmos
  - árvores-de-decisão
  - classificação
  - supervisionado
---

# 6. Árvores de Decisão

> [!info] O que esta nota cobre
> O algoritmo **Árvore de Decisão**: sua **estrutura**, métricas de **complexidade**, como ela **classifica** uma instância, o processo de **indução** (construção), as medidas de **pureza** (Gini, Entropia), as **condições de parada** e a **poda** para evitar overfitting.

---

## 6.1. O que é uma Árvore de Decisão?

> [!note] Ideia central
> Uma **Árvore de Decisão** classifica fazendo uma **sequência de perguntas** sobre os atributos, até chegar a uma resposta. É como um fluxograma de "se... então...".

> [!example] Analogia
> É como um jogo de "**Adivinha quem?**": você faz perguntas ("usa óculos?", "tem barba?") e, a cada resposta, elimina possibilidades, até descobrir quem é.

---

## 6.2. Estrutura da Árvore

Uma árvore é composta por **nós** conectados:

```
                  [ outlook ]   ← NÓ RAIZ (primeira pergunta)
                 ╱     │     ╲
            sunny   overcast   rainy
              │         │        │
         [humidity]  ( yes )  [ windy ]   ← NÓS INTERNOS
          ╱      ╲              ╱     ╲
        high   normal       TRUE     FALSE
         │        │           │        │
       (no)    (yes)        (no)     (yes)   ← FOLHAS (resposta final)
```

> [!note] Os tipos de nó
> - **Nó raiz** → o primeiro nó, no topo. A primeira pergunta.
> - **Nós internos** → perguntas intermediárias sobre atributos.
> - **Folhas** → os nós finais, que contêm a **classe** (a resposta).

---

## 6.3. Diferentes Estruturas

> [!important] Não existe uma única árvore
> Para o **mesmo conjunto de dados**, é possível construir **árvores diferentes** — mudando qual atributo vem primeiro, como dividir, etc. Umas são melhores, outras piores. O objetivo do algoritmo é achar uma **boa** árvore.

---

## 6.4. Métricas de Complexidade

Como medir o "tamanho" de uma árvore?

> [!note] Duas métricas
> - **Profundidade** → número de nós da **raiz até as folhas** (quão "fundo" a árvore vai).
> - **Largura** → número de nós em **cada nível** (quão "espalhada" ela é).

```
   Profundidade = 3                  Largura por nível:
   ┌─ nível 0 (raiz)        ●         nível 0: 1 nó
   │                       ╱ ╲
   ├─ nível 1            ●     ●      nível 1: 2 nós
   │                    ╱ ╲   ╱ ╲
   └─ nível 2          ● ● ● ●        nível 2: 4 nós
```

> [!warning] Por que a complexidade importa?
> Árvores **muito grandes** (profundas/largas) tendem ao **super ajuste (overfitting)** — decoram os dados em vez de generalizar. Voltaremos a isso na seção de **poda**.

---

## 6.5. Atributos Discretos vs. Contínuos

A árvore lida com os dois tipos de atributo, mas de formas diferentes:

- **Discretos/categóricos** (sunny, overcast, rainy) → cada valor pode virar um ramo.
- **Contínuos** (idade, temperatura exata) → a árvore cria pontos de corte (ex.: "idade > 30?").

Mais detalhes na seção de divisão abaixo.

---

## 6.6. Processo de Classificação

> [!note] Como a árvore classifica uma instância nova
> A instância "**percorre**" a árvore de cima para baixo, respondendo às perguntas, até cair numa **folha**. A classe da folha é a previsão.

> [!example] Classificando o dia `sunny, hot, high, FALSE`
> 1. **Nó raiz** `outlook`? → é `sunny` → vai para o ramo da esquerda.
> 2. **Nó** `humidity`? → é `high` → vai para o ramo da esquerda.
> 3. Chegou na **folha**: `no`.
>
> **Previsão: não vai jogar.** ☔

---

## 6.7. Indução da Árvore (Construção)

> [!note] O que é indução
> **Indução** é o processo de **construir** a árvore a partir dos dados de treino. O coração disso é decidir **como dividir** os nós.

### Tipos de divisão

> [!info] Formas de dividir um nó
> 1. **Em duas partes, ou em N partes** — a divisão pode ser binária ou múltipla.
> 2. **Binário** → divisão dupla (só dois ramos).
> 3. **Nominal** (categórico) → múltiplas divisões (um ramo por valor) **ou** agrupando valores em subconjuntos.
> 4. **Contínuo** → comparação de valores ("X > 30?") **ou** discretização (criando faixas, com duas ou múltiplas divisões).

---

## 6.8. Medidas de Pureza

> [!important] O objetivo de toda divisão
> Criar divisões o mais **"puras" possíveis**. Um nó **puro** é aquele onde **todas as instâncias pertencem à mesma classe**.

```
   Nó IMPURO (misturado)        Nó PURO (uniforme)
   ┌──────────────────┐         ┌──────────────────┐
   │ ● ● ○ ● ○ ○ ● ○  │         │ ● ● ● ● ● ● ● ●  │
   │ (5 sim, 3 não)   │         │ (8 sim, 0 não)   │
   └──────────────────┘         └──────────────────┘
   Queremos sair daqui...  →  ...e chegar aqui!
```

### As três medidas de pureza

> [!note] Como medir pureza
> - **Gini** — mede a "impureza" de Gini.
> - **Entropia** — vinda da Teoria da Informação.
> - **Erro de classificação** — taxa de erro no nó.

> [!tip] Qual é mais usada?
> **Entropia** (junto com o **Ganho de Informação**) é a mais clássica e a que o curso detalha nos cálculos. Veja [[07 - Cálculos das Árvores de Decisão]] para o passo a passo completo.

---

## 6.9. Condição de Parada

> [!note] Quando a árvore para de crescer?
> A indução para quando atinge uma destas condições:
> 1. **Chega-se a uma classe pura** — todas as instâncias do nó são da mesma classe.
> 2. **Número mínimo de observações** em um nó — o nó ficou pequeno demais para continuar dividindo.
> 3. **A última partição não aumentou a métrica de pureza** — dividir mais não ajuda.

> [!warning] Sem condição de parada...
> ...a árvore cresceria até cada folha ter **uma única instância** — overfitting garantido.

---

## 6.10. Poda (Pruning)

> [!note] Definição
> **Poda** é o processo de **reduzir o tamanho da árvore depois da indução** — cortar partes que não ajudam.

> [!important] Por que podar?
> **Árvores muito grandes estão sujeitas ao super ajuste (overfitting)**. A poda corta o excesso, tornando a árvore mais simples e mais capaz de **generalizar**.

### Mecanismos de poda

> [!info] Como a poda funciona
> - **Checar se pares de nós podem ser fundidos**, aumentando a pureza.
> - **Checar se as partições realmente aumentaram a pureza** — se não aumentaram, podem ser cortadas.

```
   ANTES da poda (grande)         DEPOIS da poda (enxuta)
          ●                              ●
        ╱   ╲                          ╱   ╲
      ●       ●                      ●       ●
     ╱ ╲     ╱ ╲                            ╱ ╲
    ●   ●   ●   ●            →               ●   ●
   ╱╲                       (ramos que não
  ●  ●                       ajudam foram cortados)
```

> [!tip] Conexão com Fundamentos
> A poda é uma técnica **anti-overfitting**. Relembre o conceito de super ajuste em [[04 - Classificação#4.5. Generalização vs. Super Ajuste vs. Sub Ajuste|generalização vs. super ajuste]].

---

## 6.11. Exemplo em Python (notebook do curso)

O curso usou o `DecisionTreeClassifier` do scikit-learn com `insurance.csv`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import graphviz

# Carregar e preparar os dados
base = pd.read_csv("insurance.csv", keep_default_na=False)
base = base.drop(columns=['Unnamed: 0'])

y = base.iloc[:, 7].values
X = base.drop(base.columns[7], axis=1).values

# Codificar categóricos
labelencoder = LabelEncoder()
for i in range(X.shape[1]):
    if X[:, i].dtype == 'object':
        X[:, i] = labelencoder.fit_transform(X[:, i])

# Treino/teste
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=12)

# Criar a árvore — note os limites de complexidade!
modelo = DecisionTreeClassifier(random_state=1, max_depth=8, max_leaf_nodes=6)
modelo.fit(X_treinamento, y_treinamento)

# Visualizar a árvore graficamente
dot_data = export_graphviz(modelo, out_file=None, filled=True,
                           feature_names=base.columns[:-1],
                           class_names=True, rounded=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree", format="png")

# Prever e avaliar
previsoes = modelo.predict(X_teste)
print(f'Acurácia: {accuracy_score(y_teste, previsoes)}')
print(classification_report(y_teste, previsoes))
```

> [!tip] Parâmetros que controlam a complexidade
> No código, `max_depth=8` (profundidade máxima) e `max_leaf_nodes=6` (número máximo de folhas) são formas de **limitar o tamanho da árvore** — uma poda "preventiva" para evitar overfitting. São os conceitos da seção 6.4 aplicados na prática.

---

## 6.12. Vantagens e Desvantagens

| ✅ Vantagens | ❌ Desvantagens |
|---|---|
| **Fácil de interpretar** (parece um fluxograma) | Propensa a **overfitting** se não podada |
| **Não precisa** de dimensionamento de atributos | Pequenas mudanças nos dados podem mudar muito a árvore |
| Lida com dados **categóricos e numéricos** | Uma única árvore pode ser **instável** |
| Rápida para classificar | (resolvido com [[08 - Random Forest]]) |

> [!tip] Lembra disto?
> Em [[08 - Dimensionamento de Características]] foi dito que "árvores de decisão não precisam de dimensionamento". Aqui está o porquê: a árvore divide por **comparações** (X > valor), e a escala não muda o resultado dessas comparações.

---

## 6.13. Resumo

> [!summary] O essencial das Árvores de Decisão
> - Classificam por uma **sequência de perguntas** (raiz → nós internos → folhas).
> - **Complexidade**: profundidade (altura) e largura (nós por nível).
> - **Indução** = construir a árvore decidindo as divisões.
> - O objetivo de cada divisão é a **pureza** (Gini, Entropia, Erro de classificação).
> - **Condição de parada**: classe pura, nó pequeno demais, ou pureza não melhora.
> - **Poda** = cortar a árvore depois de pronta para evitar **overfitting**.

---

## 🔗 Próximos passos
- [[07 - Cálculos das Árvores de Decisão]] — o passo a passo de como a árvore escolhe as divisões usando Entropia e Ganho de Informação.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
