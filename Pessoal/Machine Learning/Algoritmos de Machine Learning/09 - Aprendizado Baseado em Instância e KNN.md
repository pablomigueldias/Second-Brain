---
tags:
  - machine-learning
  - algoritmos
  - knn
  - aprendizado-baseado-em-instância
  - classificação
  - supervisionado
---

# 9. Aprendizado Baseado em Instância e KNN

> [!info] O que esta nota cobre
> Uma abordagem **diferente** de classificação: o **aprendizado baseado em instância**, onde **não se constrói um modelo**. Veremos a comparação com o aprendizado baseado em modelos, o conceito de **vizinho mais próximo**, a **distância euclidiana** e o algoritmo **KNN** (incluindo como escolher o valor de K).

---

## 9.1. Duas Filosofias de Classificação

### Classificação Baseada em Modelos

> [!note] Como funciona
> 1. Os **dados de treino** são submetidos a um **algoritmo**.
> 2. Esse algoritmo produz um **modelo**.
> 3. O **modelo** é usado para prever novos casos.

É o que vimos até agora — [[04 - Naive Bayes]], [[06 - Árvores de Decisão]], [[08 - Random Forest]] todos constroem um modelo.

```
   Dados de treino ──▶ Algoritmo ──▶ MODELO ──▶ prevê novos casos
```

### Classificação Baseada em Instância

> [!note] Como funciona
> **Não existe modelo!** Para classificar um caso novo, busca-se a **instância de treino mais semelhante** a ele, e usa-se a classe dela.

```
   Caso novo ──▶ procura a instância de treino mais parecida
             ──▶ copia a classe dessa instância
```

> [!tip] Analogia
> - **Baseado em modelo** = estudar a matéria, montar um resumo, e usar o resumo na prova.
> - **Baseado em instância** = não estudar nada; na hora da prova, procurar a questão mais parecida no livro e copiar a resposta. (Também chamado de **"aprendizado preguiçoso"** / *lazy learning*.)

---

## 9.2. Comparação: Modelo vs. Instância

> [!important] Onde está o "custo" de cada abordagem
> - **Baseado em Modelo** → **maior custo no pré-processamento** (treinar o modelo demora), mas a previsão depois é rápida.
> - **Baseado em Instância** → **maior custo na classificação** (cada previsão precisa comparar com todas as instâncias de treino), mas não há "treino".

| Aspecto | **Baseado em Modelo** | **Baseado em Instância** |
|---|---|---|
| Existe um modelo? | ✅ Sim | ❌ Não |
| Custo do treino | **Alto** (construir o modelo) | Praticamente zero |
| Custo da previsão | Baixo | **Alto** (compara com tudo) |
| Apelido | — | "Lazy learning" (preguiçoso) |

> [!tip] Quando o custo na classificação é problema?
> Se você tem **milhões** de instâncias de treino, cada nova previsão exige milhões de comparações. Para datasets gigantes, isso pode ser lento.

---

## 9.3. O Conceito de Vizinho Mais Próximo

> [!note] Ideia central
> Para classificar um caso novo, encontra-se a(s) instância(s) de treino **mais próxima(s)** dele — seus **vizinhos** — e usa-se a classe delas.

> [!example] Exemplo
> Considere instâncias com 2 atributos (AtrbA, AtrbB) e suas distâncias até um caso novo `(0,5 ; 0,3)` cuja classe é desconhecida `?`:
>
> | AtrbA | AtrbB | Classe | Distância até o caso novo |
> |---|---|---|---|
> | 0,5 | 0,8 | A | 0,5 |
> | 0,7 | 0,7 | A | 0,447 |
> | 0,9 | 0,3 | B | **0,4** ← mais próximo! |
> | 0,4 | 0,8 | B | 0,509 |
> | 0,1 | 0,6 | B | 0,5 |
>
> O vizinho mais próximo (distância 0,4) tem classe **B** → o caso novo é classificado como **B**.

---

## 9.4. Distância Euclidiana

> [!note] Como medir "proximidade"
> A forma mais comum de medir a distância entre dois pontos é a **Distância Euclidiana** — a distância "em linha reta" entre eles.

### Fórmula

Para dois pontos com atributos $(x_1, y_1)$ e $(x_2, y_2)$:

$$
d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
$$

(Para mais atributos, soma-se o quadrado da diferença de cada um, antes da raiz.)

> [!example] Exemplo de cálculo
> Distância entre o ponto `(0,9 ; 0,3)` e o ponto `(0,5 ; 0,3)`:
> $$ d = \sqrt{(0{,}9 - 0{,}5)^2 + (0{,}3 - 0{,}3)^2} = \sqrt{0{,}16 + 0} = \sqrt{0{,}16} = 0{,}4 $$

```
        (0,9 ; 0,3)
            ●
            │
       0,4  │  ← distância euclidiana
            │
            ●
        (0,5 ; 0,3)
```

> [!warning] Cuidado: escala dos atributos!
> Como a distância euclidiana soma os atributos, um atributo em escala muito maior **domina** o cálculo. Por isso, para KNN, costuma-se aplicar **dimensionamento de características** (veja [[08 - Dimensionamento de Características]] no módulo de Fundamentos).

---

## 9.5. KNN (K-Nearest Neighbors)

> [!note] Definição
> O **KNN** (K-Vizinhos Mais Próximos) é o **algoritmo mais comum** de aprendizado baseado em instância.

### Como funciona

> [!important] Os 3 passos do KNN
> 1. Sua principal configuração é o **K** — o **número de vizinhos** mais próximos a considerar.
> 2. Usa uma **técnica de distância** (geralmente euclidiana) para encontrar esses K vizinhos.
> 3. Um **processo de votação** entre os K vizinhos define a classe.

```
   Caso novo: ?
        │
        ├─ 1. Definir K (ex: K=3)
        ├─ 2. Achar os 3 vizinhos mais próximos (por distância)
        └─ 3. Os 3 vizinhos votam → classe mais votada vence
```

---

## 9.6. A Importância do Valor de K

A escolha do **K** muda o resultado. Vamos ver os casos.

### K = 3 (caso típico)

```
            ● B
        ┌ ─ ─ ─ ─ ┐
        │  ● A    │
        │    ?    │  ← os 3 vizinhos: A, A, B
        │  ● A    │     votação: A=2, B=1 → classe A
        └ ─ ─ ─ ─ ┘
            ● B
```

### Quando K não afeta a classificação

> [!note] Caso K=4 sem mudança
> Às vezes, aumentar o K **não muda nada** — se os vizinhos extras são da mesma classe que já estava vencendo, o resultado se mantém.

### O problema do EMPATE

> [!warning] Empate na votação
> Se **K for par**, pode dar **empate**.
>
> **Exemplo K=4:** se os 4 vizinhos são 2 da classe A e 2 da classe B → **empate!** O algoritmo não sabe decidir.

```
   K=4:  vizinhos = A, A, B, B
         votação: A=2, B=2  →  EMPATE ❌
```

### Minimizando empates

> [!tip] Soluções para empates
> - **Usar K ímpar** (1, 3, 5, 7...) — com classificação binária, K ímpar **nunca** empata.
> - **K=1** é o caso extremo: pega só o vizinho mais próximo, **impossível empatar** (mas fica sensível a ruído).

> [!important] Regra prática para escolher K
> - **K ímpar** → evita empates (em problemas binários).
> - **K muito pequeno** (ex: 1) → sensível a ruído/outliers.
> - **K muito grande** → "borra" as fronteiras entre classes, perde detalhe.
> - O ideal é testar alguns valores e ver qual dá melhor desempenho.

---

## 9.7. Exemplo em Python (notebook do curso)

O curso usou o `KNeighborsClassifier` do scikit-learn com o dataset `mt_cars`:

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import numpy as np

# Carregar dados
mtcars = pd.read_csv('mt_cars.csv')

# Usar 'mpg' e 'hp' para prever o número de cilindros 'cyl'
X = mtcars[['mpg', 'hp']].values
y = mtcars['cyl'].values

# Criar o KNN com K=3
knn = KNeighborsClassifier(n_neighbors=3)
modelo = knn.fit(X, y)

# Avaliar
y_prev = modelo.predict(X)
print(f'Acurácia: {accuracy_score(y, y_prev)}')
print('Matriz de confusão:\n', confusion_matrix(y, y_prev))

# Prever um caso NOVO: carro com mpg=19.3 e hp=105
new_data = np.array([[19.3, 105]])
previsao = modelo.predict(new_data)
print(previsao)

# Ver QUAIS foram os vizinhos usados
distances, indices = modelo.kneighbors(new_data)
print("Distâncias:", distances)
print("Índices dos vizinhos:", indices)
```

> [!tip] O método `.kneighbors()`
> Esse método mostra **exatamente quais** instâncias foram os vizinhos escolhidos e suas distâncias — ótimo para entender **por que** o KNN deu determinada resposta. É a "transparência" do algoritmo baseado em instância.

---

## 9.8. Vantagens e Desvantagens

| ✅ Vantagens | ❌ Desvantagens |
|---|---|
| **Simples** de entender e implementar | Previsão **lenta** em datasets grandes |
| **Não tem treino** (ou é trivial) | Sensível à **escala** dos atributos |
| Funciona bem com fronteiras complexas | Sensível a **ruído** (se K for pequeno) |
| Naturalmente **multiclasse** | Precisa guardar **todos** os dados de treino |

---

## 9.9. Resumo

> [!summary] O essencial do KNN
> - **Aprendizado baseado em instância** = **sem modelo**; compara com os dados de treino na hora.
> - Custo: baixo no treino, **alto na previsão** (oposto do baseado em modelo).
> - **KNN** = classifica pelos **K vizinhos mais próximos**, por **votação**.
> - **Distância euclidiana** = a "régua" mais comum (linha reta).
> - **K ímpar** evita empates; K pequeno = sensível a ruído; K grande = perde detalhe.
> - Escalar os atributos é importante (a distância é afetada pela escala).

---

## 🔗 Próximos passos
- [[10 - K-means]] — agora os algoritmos **não supervisionados**, começando pelo agrupamento.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
