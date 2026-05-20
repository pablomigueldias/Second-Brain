---
tags:
  - machine-learning
  - pré-processamento
  - codificação
  - encoding
  - dados-categóricos
---

# 7. Codificação de Categorias (Categorical Encoding)

> [!info] O que esta nota cobre
> Como **transformar dados categóricos em números** para que algoritmos de ML consigam processá-los. Vamos ver as duas técnicas principais: **Label Encoding** e **One-Hot Encoding**, suas armadilhas e quando usar cada uma.

---

## 7.1. Por que Codificar Categorias?

> [!important] A regra
> **Algoritmos de Machine Learning entendem apenas números.** Eles **não conseguem trabalhar diretamente** com texto como `"Red"`, `"Small"`, `"Bom"`, etc.

> [!note] Definição
> **Categorical Encoding** = o processo de **transformar categorias em números** para que possam ser usadas em modelos de ML.

### Dataset de exemplo

| Color | Size | Price |
|---|---|---|
| Red | Small | 10 |
| Green | Medium | 20 |
| Blue | Large | 30 |
| Red | Large | 25 |
| Green | Small | 15 |

`Color` e `Size` são **categóricos** — precisam ser codificados. `Price` já é numérico, fica como está.

### As duas formas principais

```
   Categorical Encoding
        │
        ├──▶ Label Encoding   (cada categoria vira um número)
        │
        └──▶ One-Hot Encoding (cada categoria vira uma coluna binária)
```

---

## 7.2. Label Encoding

> [!note] Como funciona
> Cada categoria recebe **um número único**, normalmente em **ordem alfabética**.

### Exemplo

A partir do nosso dataset:

| Categoria | Encoded Value |
|---|---|
| Color: Blue | 0 |
| Color: Green | 1 |
| Color: Red | 2 |

| Categoria | Encoded Value |
|---|---|
| Size: Large | 0 |
| Size: Medium | 1 |
| Size: Small | 2 |

*(Ordem alfabética; alguns implementações usam ordem de aparição.)*

**Dataset resultante:**

| Color_Encoded | Size_Encoded | Price |
|---|---|---|
| 2 | 2 | 10 |
| 1 | 1 | 20 |
| 0 | 0 | 30 |
| 2 | 0 | 25 |
| 1 | 2 | 15 |

*(No material do curso, foi usada outra ordem; o importante é entender o princípio.)*

> [!example] Outra ordem possível (a do material original)
> | Categoria | Encoded |
> |---|---|
> | Color: Red | 0 |
> | Color: Green | 1 |
> | Color: Blue | 2 |
>
> | Categoria | Encoded |
> |---|---|
> | Size: Small | 0 |
> | Size: Medium | 1 |
> | Size: Large | 2 |

---

### 7.2.1. ⚠️ Problema do Label Encoding

> [!warning] A grande armadilha
> O algoritmo pode interpretar os números como **ordem de grandeza** — como se uma categoria fosse "maior" ou "melhor" que outra.

Pense: se `Color_Encoded` tem os valores `0, 1, 2`, um modelo matemático vai assumir que `2` é maior que `1` e que `1` é maior que `0`. Mas...

> **Vermelho não é "maior" que verde.** **Azul não é o "dobro" de verde.** São apenas categorias diferentes.

Esse tipo de interpretação errada pode levar o modelo a aprender padrões inexistentes e atrapalhar as previsões.

---

### 7.2.2. Quando Label Encoding é Adequado?

> [!tip] Use Label Encoding quando...
> **Existe uma ordem natural** entre as categorias (categórico **ordinal**).

> [!example] Exemplos onde faz sentido
> - **Nível de cargo**: Junior < Pleno < Sênior → `0, 1, 2` ✅
> - **Nota da escola**: Ruim < Regular < Bom < Ótimo → `0, 1, 2, 3` ✅
> - **Tamanho de camiseta**: PP < P < M < G < GG → `0, 1, 2, 3, 4` ✅
>
> Nesses casos, a "ordem de grandeza" **é real**.

---

## 7.3. One-Hot Encoding

> [!note] Como funciona
> **Cada categoria** é transformada em **uma nova coluna** (atributo) chamada **dummy variable**. Um valor binário (0 ou 1) indica a **presença ou ausência** daquela categoria.

### Exemplo

Dataset original:

| Color | Size | Price |
|---|---|---|
| Red | Small | 10 |
| Green | Medium | 20 |
| Blue | Large | 30 |
| Red | Large | 25 |
| Green | Small | 15 |

Após One-Hot Encoding:

| Color_Red | Color_Green | Color_Blue | Size_Small | Size_Medium | Size_Large | Price |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1 | 0 | 0 | 10 |
| 0 | 1 | 0 | 0 | 1 | 0 | 20 |
| 0 | 0 | 1 | 0 | 0 | 1 | 30 |
| 1 | 0 | 0 | 0 | 0 | 1 | 25 |
| 0 | 1 | 0 | 1 | 0 | 0 | 15 |

> Cada linha agora tem **exatamente um `1`** no grupo de colunas de `Color` e **exatamente um `1`** no grupo de `Size`.

### Vantagens

✅ Evita o problema da ordem falsa do Label Encoding.
✅ Trata categorias como **independentes**, sem hierarquia.
✅ Funciona com qualquer algoritmo numérico.

---

### 7.3.1. ⚠️ Problemas do One-Hot Encoding

#### Problema 1: Alta Dimensionalidade

> [!warning] Maldição da Dimensionalidade
> Muitas categorias = muitas colunas novas. Isso gera um **espaço de características de alta dimensão**, que pode causar:
> - **Super ajuste** (overfitting).
> - **Custo computacional muito alto**.
> - **Dados esparsos**: muitas colunas com valor zero, tornando difícil encontrar padrões.

> [!example] Exemplo prático
> Se você tem um atributo `Cidade` com **5.000 cidades diferentes**, o One-Hot Encoding cria **5.000 novas colunas**. Aí o modelo trava ou aprende ruído.

---

#### Problema 2: Dummy Variable Trap (Armadilha das Variáveis Dummy)

> [!warning] Multicolinearidade
> Os valores das colunas binárias **podem ser previstos a partir dos valores das outras colunas**. Isso gera **multicolinearidade** — variáveis independentes correlacionadas entre si — que prejudica modelos como **regressão linear**.

##### Vendo o problema na prática

Olhe essa parte do dataset com algumas células ocultas:

| Color_Red | Color_Green | Color_Blue |
|---|---|---|
| 1 | ? | ? |
| 0 | ? | 0 |
| ? | ? | 1 |
| ? | 0 | 0 |
| 0 | ? | 0 |

Você consegue **preencher as células com `?`** mesmo sem ver os valores originais. Por quê?

> **Porque a soma de cada linha precisa ser 1.** Se duas colunas são 0, a terceira **obrigatoriamente** é 1. Se uma já é 1, as outras **obrigatoriamente** são 0.

| Color_Red | Color_Green | Color_Blue |
|---|---|---|
| 1 | **0** | **0** |
| 0 | **1** | 0 |
| **0** | **0** | 1 |
| **1 ou 0** | 0 | 0 |
| 0 | **1** | 0 |

> [!summary] Conclusão
> Os atributos são **altamente previsíveis** uns a partir dos outros. Eles carregam **informação redundante**.

##### Solução

> [!tip] Como resolver a Dummy Variable Trap
> - **Excluir uma das colunas** binárias (a informação não se perde — pode ser deduzida pelas outras).
> - **Combinar** colunas binárias quando fizer sentido.
>
> Por isso muitas bibliotecas têm a opção `drop_first=True` no One-Hot.

---

## 7.4. Label Encoding vs. One-Hot Encoding: Qual Usar?

| Critério | **Label Encoding** | **One-Hot Encoding** |
|---|---|---|
| **Há ordem entre as categorias?** | Sim (ex.: Junior < Pleno < Sênior) | Não |
| **Número de categorias?** | Funciona bem com muitas | Melhor com **poucas** |
| **Cria quantas colunas?** | Mesma (substitui texto por número) | **N colunas** (uma por categoria) |
| **Risco principal** | Modelo "inventar" ordem | Alta dimensionalidade / multicolinearidade |

### Regra prática

> [!tip] Em uma frase
> - **Categórico ordinal** (com ordem natural) → **Label Encoding**
> - **Categórico nominal** (sem ordem) → **One-Hot Encoding** (se poucas categorias)
> - **Muitas categorias nominais** → buscar técnicas mais avançadas (target encoding, embeddings, etc.) que não foram cobertas neste tópico.

---

## 7.5. Pipeline Mental

```
   Dado categórico
        │
        ▼
   Tem ordem natural?
        │
   ┌────┴────┐
   │         │
  SIM       NÃO
   │         │
   ▼         ▼
 Label    Poucas categorias?
Encoding      │
         ┌────┴────┐
         │         │
        SIM       NÃO
         │         │
         ▼         ▼
      One-Hot   Técnicas avançadas
      Encoding  (Target Encoding, etc.)
```

---

## 🔗 Próximos passos
- [[08 - Dimensionamento de Características]] — depois de codificar, muitas vezes precisamos **escalar** os números numéricos.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
