---
tags:
  - machine-learning
  - deep-learning
  - computer-vision
  - cnn
  - redes-neurais
---

# 5. CNN — Redes Convolucionais (Computer Vision)

> [!info] O que esta nota cobre
> Como a máquina **enxerga** imagens com **Redes Neurais Convolucionais (CNN)**. Vamos pelos 4 passos: **Convolução → Max Pooling → Flattening → Full Connection**. Com o exemplo numérico do curso.

---

## 5.1. O problema: como reconhecer uma imagem?

> [!question] Analisar pixel a pixel?
> Uma imagem é só uma **matriz de números** (pixels). Comparar pixel a pixel **não funciona**: a mesma gato deslocado 1 pixel já viraria "outra imagem". A saída é **buscar características** (bordas, curvas, texturas), não pixels isolados.

> [!note] A ideia da CNN
> As **CNNs** simulam o modo como o **cérebro humano identifica padrões visuais**. São compostas por camadas de neurônios chamadas **mapas de características** (*feature maps*): cada uma aprende a detectar um padrão visual.

O pipeline tem **4 passos**:

```
   Imagem → [1] Convolução → [2] Max Pooling → [3] Flattening → [4] Full Connection → classe
```

---

## 5.2. Passo 1 — Convolução

> [!note] O que é
> Passamos um pequeno **filtro** (também chamado **kernel** ou **detector de características**) deslizando sobre a imagem. Em cada posição, multiplicamos e somamos → geramos um **mapa de características**.

> [!example] Exemplo do curso (números reais)
> **Imagem de entrada** 7×7 (com 1s formando um padrão) e um **detector 3×3**:
>
> ```
> Detector (kernel):
>   0  0  1
>   1  0  0
>   0  1  1
> ```
>
> Deslizando o detector pela imagem, posição a posição, montamos o **mapa de características** 5×5:
>
> ```
>   0  1  0  0  0
>   0  1  1  1  0
>   1  0  1  2  1
>   1  4  2  1  0
>   0  0  1  2  1
> ```

> [!tip] Por que isso ajuda
> Cada filtro **realça um tipo de padrão** (uma borda na vertical, uma curva…). Criamos **vários filtros** → vários mapas de características → juntos formam a primeira **Camada Convolucional**. Depois aplica-se a ativação **ReLU** (Rectifier) para zerar valores negativos.

---

## 5.3. Passo 2 — Max Pooling

> [!note] O que é
> **Reduzir o tamanho** do mapa de características mantendo o que importa. No **Max Pooling**, deslizamos uma janela e ficamos apenas com o **maior valor** de cada região.

> [!example] Continuando o exemplo
> O mapa 5×5 acima, com Max Pooling, vira um **mapa "em pool"** 3×3:
>
> ```
>   1  1  0
>   4  2  1
>   0  2  1
> ```

> [!summary] Por que fazer pooling
> - **Reduz a dimensionalidade** (menos cálculo).
> - Dá **invariância a pequenas translações**: se o objeto se move um pouco, o "máximo" da região continua sendo capturado.
> - Combate overfitting (menos parâmetros).

---

## 5.4. Passo 3 — Flattening

> [!note] O que é
> **Achatar** o mapa de características (matriz 2D) em um **vetor 1D** (uma coluna de números), para poder alimentar uma rede neural tradicional.

> [!example] No exemplo
> O mapa em pool 3×3:
> ```
>   1  1  0
>   4  2  1
>   0  2  1
> ```
> vira o vetor coluna: `[1, 1, 0, 4, 2, 1, 0, 2, 1]`.

Esse vetor é exatamente a **camada de entrada** de uma rede neural artificial comum (a "futura RNA").

---

## 5.5. Passo 4 — Full Connection

> [!note] O que é
> Conectamos o vetor achatado a uma **rede totalmente conectada** ([[04 - Deep Learning e Hiperparâmetros|fully connected]]), que faz a **classificação final**.

```
   [x1, x2, ..., xm]  →  Camada totalmente conectada  →  Camada de saída
        (flatten)                                            │
                                                   ┌─────────┴─────────┐
                                                 Cachorro            Gato
```

> [!example] Exemplo do curso: gato ou cachorro?
> A camada de saída tem um neurônio por classe. No fim, ela dá uma **probabilidade** para cada uma:
> - `Cachorro → 0,95` · `Gato → 0,05` → **classifica como Cachorro** 🐶
> - `Cachorro → 0,21` · `Gato → 0,79` → **classifica como Gato** 🐱

> [!tip] Conexão
> A camada de saída usa funções como **softmax** para transformar os números em probabilidades que somam 1. A maior vence — exatamente a mesma lógica de decisão do [[../Fundamentos/04 - Classificação|aprendizado supervisionado]].

---

## 5.6. O dataset CIFAR-10

O curso usou o **CIFAR-10** para treinar uma CNN de classificação de imagens:

> [!note] CIFAR-10
> - **60.000 imagens** coloridas de **32×32 pixels**
> - **10 classes** (avião, carro, pássaro, gato, cachorro…)
> - **6.000 imagens por classe**
> - **50.000** para treino + **10.000** para teste
> - 🔗 https://www.cs.toronto.edu/~kriz/cifar.html

---

## 5.7. Esqueleto em Python (Keras)

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

modelo = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),  # Convolução
    MaxPooling2D((2, 2)),                                            # Max Pooling
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),                                                       # Flattening
    Dense(64, activation='relu'),                                   # Full Connection
    Dense(10, activation='softmax'),                                # Saída: 10 classes
])
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

---

## 5.8. Resumo

> [!summary] O essencial da CNN
> 1. **Convolução:** filtros deslizam pela imagem → **mapas de características** (depois ReLU).
> 2. **Max Pooling:** reduz tamanho pegando o **máximo** de cada região.
> 3. **Flattening:** achata a matriz em um **vetor 1D**.
> 4. **Full Connection:** rede densa que **classifica** (softmax → probabilidades).
> - CNNs aprendem a ver **características**, não pixels isolados.

---

## 🔗 Próximos passos
- [[06 - LSTM e Redes Recorrentes]] — saindo das imagens para os dados **sequenciais** (texto, séries temporais).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
