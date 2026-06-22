---
tags:
  - machine-learning
  - deep-learning
  - hiperparametros
  - regularização
  - redes-neurais
---

# 4. Deep Learning e Hiperparâmetros

> [!info] O que esta nota cobre
> O que é **Deep Learning**, e os **hiperparâmetros** que controlam o treino de uma rede: **funções de ativação**, **regularização** (early stopping, dropout, L1/L2, data augmentation) e o **gradient descent**.

---

## 4.1. O que é Deep Learning

> [!note] Definição
> **Deep Learning** = Redes Neurais Artificiais com **múltiplas camadas**, geralmente **totalmente conectadas** (*fully connected*: cada neurônio de uma camada se liga a todos da próxima).

> [!example] A intuição mais importante
> **Cada camada se especializa em identificar uma característica.** Numa rede que reconhece rostos: a 1ª camada detecta **bordas**, a 2ª combina bordas em **formas** (olhos, narizes), a 3ª combina formas em **rostos**. A profundidade permite ir do simples ao complexo, camada a camada.

> [!summary] Onde brilha
> - Reconhecimento de **fala**
> - Reconhecimento de **imagens** (Computer Vision)
> - **Processamento de Linguagem Natural** (NLP)

---

## 4.2. Hiperparâmetros principais

> [!note] Os "botões" que você ajusta antes de treinar
> | Hiperparâmetro | O que controla |
> |---|---|
> | `hidden_layer_sizes` | Nº de neurônios nas camadas ocultas (e, na prática, quantas camadas). |
> | `batch_size` | Nº de instâncias por batch usadas para atualizar a rede. |
> | `epochs` (`max_iter`) | Nº de vezes que os dados passam pela rede. |
> | `early_stopping` | Parar quando a performance **não melhora mais**. |
> | `learning_rate` | O quanto os pesos mudam a cada iteração (ver [[02 - Perceptron|taxa de aprendizado]]). |
> | `activation` | A função de ativação (`logistic`, `tanh`, `relu`…). |

---

## 4.3. Funções de Ativação

A função de ativação decide **como o neurônio "dispara"** a partir da soma ponderada. Trocar a função muda como a rede aprende.

| Função | Formato | Saída | Observação |
|---|---|---|---|
| **Threshold (degrau)** | Salto abrupto | 0 ou 1 | A do perceptron clássico. |
| **Sigmoid (logistic)** | "S" suave | 0 a 1 | Boa para probabilidades; pode "saturar". |
| **Rectifier (ReLU)** | Linear ≥ 0, zero abaixo | 0 a ∞ | A **mais usada** em deep learning; rápida. |
| **Tanh (tangente hiperbólica)** | "S" suave | −1 a 1 | Centrada em zero. |

> [!tip] Na prática
> **ReLU** (`relu`) é o ponto de partida padrão para camadas ocultas em redes profundas, por ser simples e eficiente. **Sigmoid/Softmax** costumam ficar na saída quando se quer probabilidade.

---

## 4.4. Regularização: evitando overfitting

> [!warning] O problema
> **Overfitting** = a rede "decora" os dados de treino e vai mal em dados novos. **Regularização** = técnicas para combater isso.

### Técnicas

> [!note] As principais
> - **Early Stopping:** interrompe o treino quando a performance estabiliza por muitas epochs (ou começa a piorar).
> - **Data Augmentation:** **gera novos exemplos** de treino a partir dos existentes (ex.: girar/espelhar imagens). Mais dados → menos overfitting.
> - **Dropout:** **desliga neurônios aleatoriamente** durante o treino (segundo uma probabilidade). Isso obriga a rede a **não depender** de um único neurônio, aprendendo de forma mais robusta.
> - **L1 e L2:** adicionam um termo de penalidade à função de custo (ver abaixo).

### Regularização L1 e L2

> [!note] Como funcionam
> Adicionam um **termo extra à loss function** (que o treino tenta minimizar), multiplicado por um hiperparâmetro **alfa (α)**:
> - **L1 (Lasso):** penaliza o **valor absoluto** dos pesos.
> - **L2 (Ridge):** penaliza o **quadrado** dos pesos.
>
> O efeito: os pesos tendem a ficar **menores** → o modelo fica **menos complexo** → **menos overfitting**.

> [!example] Intuição
> É como dizer ao modelo: "resolva o problema, mas **sem usar números gigantes nos pesos**". Forçar simplicidade evita que ele decore ruído.

---

## 4.5. Gradient Descent (Descida do Gradiente)

> [!important] O motor do aprendizado
> **Gradient Descent** é o algoritmo de **otimização** que ajusta os pesos para **minimizar o erro** entre o previsto e o real. Ele diz **a direção** e **o quanto** cada peso deve mudar.

> [!example] Analogia clássica
> Imagine estar no topo de um morro no escuro, querendo chegar ao vale (erro mínimo). Você sente a inclinação sob seus pés (o **gradiente**) e dá um passo na direção mais íngreme para baixo. Repete até não dar mais para descer. O **learning rate** é o tamanho do passo.

> [!note] Momentum
> **Momentum** é um ajuste que usa a "inércia" das atualizações anteriores antes de aplicar a nova, tornando a descida **mais estável** e ajudando a não ficar preso em pequenas covas.

---

## 4.6. Exemplo em Python (MLP do scikit-learn)

O curso usou redes neurais (MLP — *Multi-Layer Perceptron*) com Keras e scikit-learn. Um esqueleto típico:

```python
from sklearn.neural_network import MLPClassifier

modelo = MLPClassifier(
    hidden_layer_sizes=(100, 50),  # 2 camadas ocultas: 100 e 50 neurônios
    activation='relu',             # função de ativação
    batch_size=32,
    max_iter=200,                  # epochs
    early_stopping=True,           # regularização
    learning_rate_init=0.001,
)
modelo.fit(X_treino, y_treino)
previsoes = modelo.predict(X_teste)
```

---

## 4.7. Resumo

> [!summary] O essencial
> - **Deep Learning** = redes com **muitas camadas**; cada camada aprende uma característica.
> - **Funções de ativação:** ReLU (padrão das ocultas), Sigmoid, Tanh, degrau.
> - **Regularização** combate overfitting: **early stopping, dropout, data augmentation, L1/L2**.
> - **L1/L2** penalizam pesos grandes (α controla a força).
> - **Gradient Descent** ajusta os pesos descendo o "morro" do erro; **momentum** estabiliza.

---

## 🔗 Próximos passos
- [[05 - CNN - Redes Convolucionais]] — uma arquitetura profunda especializada em **imagens**.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
