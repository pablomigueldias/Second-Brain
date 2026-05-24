---
tags:
  - machine-learning
  - tópicos-avançados
  - pca
  - redução-de-dimensionalidade
  - pré-processamento
---

# 2. PCA - Redução de Dimensionalidade

> [!info] O que esta nota cobre
> O **PCA** (Principal Component Analysis / Análise de Componentes Principais): uma técnica para **reduzir o número de atributos**, criando atributos sintéticos que mantêm a informação importante. É a etapa 4 da [[01 - Engenharia de Atributos]].

---

## 2.1. O Problema: Alta Dimensionalidade

> [!warning] Por que muitos atributos é ruim?
> A **alta dimensionalidade** (muitos atributos) leva a uma **menor capacidade de generalização** do modelo.

> [!tip] Lembra da Maldição da Dimensionalidade?
> Esse é o mesmo problema visto em [[07 - Codificação de Categorias]] e [[03 - Seleção de Atributos]]: quanto mais atributos, mais "espalhados" ficam os dados, mais difícil aprender, e maior o risco de **overfitting**.

A solução pode ser **reduzir a dimensionalidade** — e o PCA é uma das formas de fazer isso.

---

## 2.2. O que é o PCA?

> [!note] Definição
> O **PCA** é uma técnica de **redução de dimensionalidade** que **cria atributos sintéticos** (novos), sem compreensão funcional, que buscam **manter as características importantes** dos dados.

### Características do PCA

> [!important] Pontos-chave do PCA
> - Cria **atributos sintéticos** — não são os atributos originais, são novos, calculados.
> - Esses novos atributos buscam **manter as características importantes** dos dados originais.
> - Funciona por **projeção** — os atributos originais são "projetados" num espaço menor.
> - ⚠️ **Não permite avaliar a importância de atributos** e os novos atributos **não representam mais o negócio** analisado.

> [!warning] O grande trade-off do PCA
> O PCA **comprime** os dados, mas em troca você **perde a interpretabilidade**. Depois do PCA, você tem "Componente 1", "Componente 2"... que **não significam nada** no mundo real (não é mais "idade" ou "salário"). Você ganha eficiência, perde explicação.

---

## 2.3. A Ideia por Trás (Projeção)

> [!example] Analogia: a sombra
> Imagine um objeto 3D iluminado, projetando uma **sombra 2D** na parede. A sombra tem **uma dimensão a menos**, mas ainda mostra o "formato geral" do objeto. O PCA faz algo parecido: projeta dados de muitas dimensões em poucas, tentando preservar o máximo do "formato".

```
   ANTES (4 atributos)          DEPOIS do PCA (2 componentes)

   AtribA  AtribB  AtribC  AtribD     Comp1   Comp2
     ...     ...     ...     ...        ...     ...
     ...     ...     ...     ...   →    ...     ...
     ...     ...     ...     ...        ...     ...

   (atributos reais do negócio)   (atributos sintéticos,
                                   sem significado direto)
```

> [!tip] Como o PCA escolhe as projeções
> O PCA encontra as direções (componentes) onde os dados **mais variam** — porque é nessa variação que está a informação. Os primeiros componentes capturam a maior parte da informação; os últimos quase só capturam ruído e podem ser descartados.

---

## 2.4. Etapas de Uso do PCA

> [!important] Como aplicar o PCA corretamente
> 1. **Redução da dimensionalidade** — aplicar o PCA para reduzir os atributos.
> 2. **Treinamento do modelo** — treinar o modelo com os dados já reduzidos.
> 3. **Testes e previsões devem ser aplicados com dados que passaram pelo MESMO processo** — os dados de teste/produção precisam passar pela mesma transformação PCA do treino.

> [!warning] Erro comum
> Se você aplica PCA no treino mas **esquece** de aplicar a mesma transformação nos dados de teste, o modelo recebe atributos "incompatíveis" e os resultados ficam errados. **O PCA é parte do pipeline** — treino e teste passam pela mesma transformação.

---

## 2.5. Exemplo em Python (notebook do curso)

O notebook `PCA.ipynb` comparou o desempenho de um Random Forest **com e sem PCA** no dataset IRIS:

```python
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets

iris = datasets.load_iris()
previsores = iris.data      # 4 atributos
classe = iris.target

# É recomendado padronizar ANTES do PCA
sc = StandardScaler()
previsores = sc.fit_transform(previsores)

# --- SEM PCA: treina com os 4 atributos originais ---
X_tr, X_te, y_tr, y_te = train_test_split(previsores, classe,
                                          test_size=0.3, random_state=123)
floresta = RandomForestClassifier(n_estimators=100, random_state=1234)
floresta.fit(X_tr, y_tr)
print("Acurácia sem PCA:", accuracy_score(y_te, floresta.predict(X_te)))

# --- COM PCA: reduz de 4 para 3 componentes ---
pca = PCA(n_components=3)
previsores_pca = pca.fit_transform(previsores)

X_tr, X_te, y_tr, y_te = train_test_split(previsores_pca, classe,
                                          test_size=0.3, random_state=123)
floresta = RandomForestClassifier(n_estimators=100, random_state=1234)
floresta.fit(X_tr, y_tr)
print("Acurácia com PCA:", accuracy_score(y_te, floresta.predict(X_te)))
```

> [!tip] O parâmetro `n_components`
> `PCA(n_components=3)` diz "quero reduzir para 3 componentes". O exercício mostra a comparação: às vezes o PCA mantém (ou quase mantém) a acurácia usando **menos atributos** — o que significa modelo mais leve e rápido.

> [!note] Padronizar antes do PCA
> Note o `StandardScaler` antes do PCA. Isso é importante: como o PCA olha a **variação** dos atributos, atributos em escalas diferentes distorceriam o resultado. Relembre [[08 - Dimensionamento de Características]].

---

## 2.6. Quando Usar PCA?

| ✅ Use PCA quando... | ❌ Evite PCA quando... |
|---|---|
| Há **muitos atributos** (alta dimensionalidade) | Você **precisa interpretar** os atributos |
| Atributos são **correlacionados** (redundantes) | Há poucos atributos já |
| O custo computacional é um problema | A explicabilidade é requisito (ex.: área médica/jurídica) |
| Você quer **visualizar** dados em 2D/3D | |

---

## 2.7. PCA vs. Seleção de Atributos

> [!important] Não confundir
> Tanto o PCA quanto a [[03 - Seleção de Atributos]] reduzem o número de atributos, mas de formas **diferentes**:
>
> | | **PCA** | **Seleção de Atributos** |
> |---|---|---|
> | O que faz | **Cria** atributos novos (combinações) | **Escolhe** um subconjunto dos originais |
> | Interpretabilidade | ❌ Perde (atributos sintéticos) | ✅ Mantém (atributos reais) |
> | Resultado | Componentes sem significado | Atributos do negócio, só que menos |

---

## 2.8. Resumo

> [!summary] O essencial do PCA
> - **Alta dimensionalidade** prejudica a generalização → reduzir ajuda.
> - **PCA** cria **atributos sintéticos** (componentes) por **projeção**.
> - Mantém a informação importante, mas **perde a interpretabilidade**.
> - O **mesmo processo PCA** deve ser aplicado a treino, teste e produção.
> - Diferente da **seleção**: PCA *cria* atributos novos; seleção *escolhe* os originais.

---

## 🔗 Próximos passos
- [[03 - Seleção de Atributos]] — a outra forma de reduzir dimensionalidade, mantendo os atributos originais.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
