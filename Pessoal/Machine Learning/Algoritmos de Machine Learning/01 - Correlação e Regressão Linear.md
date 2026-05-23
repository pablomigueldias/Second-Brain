---
tags:
  - machine-learning
  - algoritmos
  - regressão-linear
  - correlação
  - supervisionado
---

# 1. Correlação e Regressão Linear

> [!info] O que esta nota cobre
> O ponto de partida da regressão: como saber se **duas variáveis têm relação**, como **medir a força** dessa relação (correlação **R** e coeficiente de determinação **R²**), e como uma **reta de regressão** é construída para fazer previsões.

---

## 1.1. A Pergunta Central

> [!question] As três perguntas da regressão
> 1. **Existe uma relação matemática** entre estas duas variáveis?
> 2. Se existe, **como medir sua força**?
> 3. Posso usar essa relação para **fazer previsões**?

> [!example] Exemplo que vamos usar o tempo todo
> *"Qual vai ser o custo para o plano de saúde de um paciente com 45 anos de idade?"*
>
> Temos duas variáveis: **idade** e **custo**. Será que a idade ajuda a prever o custo?

---

## 1.2. Gráfico de Dispersão

A primeira ferramenta é o **gráfico de dispersão** (scatter plot): cada ponto é uma instância, posicionado pelas duas variáveis.

### Os dois eixos têm nomes importantes

| Eixo | Nome | Papel na regressão |
|---|---|---|
| **Y** (vertical) | Variável de **Resposta** ou **Dependente** | O que **queremos prever** |
| **X** (horizontal) | Variável **Explanatória** ou **Independente** | O que **explica** / usamos para prever |

> [!example] No nosso caso
> - **X (independente)** = Idade → é o que usamos para prever.
> - **Y (dependente)** = Custo → é o que queremos descobrir.

```
 Custo (Y)
   │                              •
   │                       •   •
   │                 •  •
   │           •  •
   │      • •
   │   •
   └──────────────────────────────▶ Idade (X)
```

Olhando o gráfico, já dá pra "sentir" se há relação: se os pontos formam uma tendência (sobem ou descem juntos), há relação.

---

## 1.3. Correlação (R)

> [!note] Definição
> A **correlação (R)** mostra a **força** e a **direção** da relação entre duas variáveis. É um valor entre **-1 e 1**.

### Propriedade importante

> [!tip] Correlação é simétrica
> A correlação de **A ~ B** é a **mesma** que **B ~ A**. A ordem não importa para medir a relação.
> *(Isso é diferente da regressão, onde X e Y têm papéis distintos.)*

### Força e Direção da Correlação

O **sinal** indica a **direção**; o **valor absoluto** indica a **força**:

| Valor de R | Força | Direção |
|---|---|---|
| **+1** | Perfeita | Positiva |
| **+0,7** a +1 | Forte | Positiva |
| **+0,5** a +0,7 | Moderada | Positiva |
| **+0,25** a +0,5 | Fraca | Positiva |
| **~0** | Inexistente | — |
| **-0,25** a -0,5 | Fraca | Negativa |
| **-0,5** a -0,7 | Moderada | Negativa |
| **-0,7** a -1 | Forte | Negativa |
| **-1** | Perfeita | Negativa |

### O que "direção" significa?

```
   Correlação POSITIVA          Correlação NEGATIVA
   (sobem juntas)               (uma sobe, outra desce)

   Y │        •                 Y │  •
     │      •                     │     •
     │    •                       │        •
     │  •                         │           •
     └──────────▶ X               └──────────────▶ X
```

- **Positiva**: quando X aumenta, Y também aumenta.
- **Negativa**: quando X aumenta, Y diminui.

---

## 1.4. Coeficiente de Determinação (R²)

> [!note] Definição
> O **R²** mostra **o quanto o modelo consegue explicar** os valores. Quanto maior, mais explicativo o modelo é.

### Características do R²

- 📏 Varia entre **0 e 1** — **sempre positivo**.
- 🧮 Calcula-se com o **quadrado do coeficiente de correlação**: $R^2 = R \times R$.
- 📊 Quanto **maior**, mais o modelo explica.
- ⚠️ O restante da variabilidade está em **variáveis não incluídas** no modelo.

> [!example] Interpretação prática
> Se a **correlação R = 0,93**, então:
> $$ R^2 = 0{,}93^2 \approx 0{,}86 $$
>
> **Significado:** **86%** da variável dependente consegue ser explicada pelas variáveis explanatórias presentes no modelo. Os outros 14% dependem de fatores que **não estão** no modelo.

> [!tip] R vs. R² — não confundir
> - **R** (correlação) → mede **força e direção**, vai de **-1 a 1**.
> - **R²** (determinação) → mede **quanto o modelo explica**, vai de **0 a 1**.

---

## 1.5. Como a Reta de Regressão é Construída?

A regressão linear traça uma **reta** que melhor representa os pontos. Toda reta é definida por **dois números**:

### Interseção (Intercepto)

> [!note] Definição
> O **ponto de encontro da linha com o eixo Y** — ou seja, o valor de Y quando **X = 0**.

### Inclinação (Coeficiente angular)

> [!note] Definição
> A cada **unidade que aumenta** a variável independente (X), a variável de resposta (Y) **sobe o valor da inclinação**.

> [!example] Exemplo com números reais
> Para o dataset idade × custo:
> - **Interseção** = -558,94
> - **Inclinação** = 61,86
>
> Isso significa: a cada **1 ano a mais** de idade, o custo sobe **R$ 61,86**.
>
> | Idade | Custo previsto |
> |---|---|
> | 33 anos | 1356 |
> | 34 anos | 1356 + 61,86 = **1417,86** |

---

## 1.6. Fazendo Previsões

> [!important] A fórmula da previsão
> $$ \text{Previsão} = \text{Interseção} + (\text{Inclinação} \times \text{Valor a prever}) $$

> [!example] "Quanto vai custar um cliente de 56 anos?"
> $$ X = -558{,}94 + (61{,}86 \times 56) $$
> $$ X = -558{,}94 + 3464{,}16 $$
> $$ X = 2905{,}22 $$
>
> O modelo prevê um custo de aproximadamente **R$ 2.905,22**.

---

## 1.7. Resíduos e Valores Ajustados

Nenhum modelo é perfeito. Os pontos reais quase nunca caem **exatamente** sobre a reta.

> [!note] Definições
> - **Valor ajustado** = o valor que o modelo **previu** (o ponto **na reta**).
> - **Resíduo** = a **diferença** entre o valor **real** e o valor **ajustado**.

$$ \text{Resíduo} = \text{Valor Real} - \text{Valor Ajustado} $$

> [!example] Exemplo
> Se o modelo previu um custo de **1500** (valor ajustado) mas o valor real era **1000**:
> $$ \text{Resíduo} = 1000 - 1500 = -500 $$

### Resíduos podem ser positivos ou negativos

```
   Y │           • (real)
     │          ╱│  ← resíduo POSITIVO (real acima da reta)
     │        ╱  │
     │      ╱────• (ajustado, na reta)
     │    ╱      │
     │  ╱       ╱│
     │╱       ╱  • (real)
     │      ╱  ← resíduo NEGATIVO (real abaixo da reta)
     └──────────────▶ X
```

> [!tip] Por que os resíduos importam?
> Eles são a base para avaliar se a regressão é **confiável**. Resíduos bem comportados = modelo confiável. Veremos as condições em [[02 - Regressão Linear - Condições e Regressão Múltipla]].

---

## 1.8. Exemplo em Python (do notebook do curso)

O curso trouxe uma classe `LinearRegression` feita "na mão", sem bibliotecas, só para entender a lógica:

```python
from numpy import *

class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__correlation_coefficient = self.__correlacao()
        self.__inclination = self.__inclinacao()
        self.__intercept = self.__interceptacao()

    def __correlacao(self):
        covariacao = cov(self.x, self.y, bias=True)[0][1]
        variancia_x = var(self.x)
        variancia_y = var(self.y)
        return covariacao / sqrt(variancia_x * variancia_y)

    def __inclinacao(self):
        stdx = std(self.x)
        stdy = std(self.y)
        return self.__correlation_coefficient * (stdy / stdx)

    def __interceptacao(self):
        mediax = mean(self.x)
        mediay = mean(self.y)
        return mediay - mediax * self.__inclination

    def previsao(self, valor):
        return self.__intercept + (self.__inclination * valor)

# Uso:
x = array([1, 2, 3, 4, 5])
y = array([2, 4, 6, 8, 10])

lr = LinearRegression(x, y)
previsao = lr.previsao(6)
print(previsao)   # Resultado: 12.0
```

> [!note] O que esse código mostra
> A classe calcula os três ingredientes (correlação → inclinação → interceptação) e depois usa a fórmula da previsão. Como `y` é exatamente `2x`, prever para `x=6` dá `12`. As fórmulas exatas estão detalhadas em [[03 - Cálculos da Regressão Linear]].

---

## 1.9. Resumo

> [!summary] O essencial
> - **Correlação (R)** → força e direção da relação (de -1 a 1).
> - **R² (determinação)** → quanto o modelo explica (0 a 1) = R².
> - A **reta** é definida por **interseção** + **inclinação**.
> - **Previsão** = Interseção + (Inclinação × valor).
> - **Resíduo** = valor real − valor ajustado.

---

## 🔗 Próximos passos
- [[02 - Regressão Linear - Condições e Regressão Múltipla]] — quando podemos confiar no modelo e como usar várias variáveis.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
