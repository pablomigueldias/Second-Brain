---
tags:
  - machine-learning
  - deep-learning
  - autoencoders
  - não-supervisionado
  - redes-neurais
---

# 7. Autoencoders

> [!info] O que esta nota cobre
> Os **Autoencoders**: redes neurais de **aprendizado não supervisionado** que aprendem a **comprimir** e **reconstruir** dados. Sua arquitetura (encoder–code–decoder), suas variantes e aplicações.

---

## 7.1. O que é um Autoencoder

> [!note] Definição
> Um **Autoencoder** é uma categoria especial de rede neural usada para **aprendizagem não supervisionada**. O objetivo dele é, curiosamente, **reproduzir a própria entrada na saída** — mas passando por um "gargalo" que o força a aprender uma representação compacta.

> [!example] Analogia
> É como pedir para alguém **resumir** um texto e depois **reescrevê-lo** a partir do resumo. Para o resumo funcionar, a pessoa precisa capturar **a essência**. O autoencoder faz isso com dados: aprende a essência ao ser forçado a comprimir e reconstruir.

---

## 7.2. Arquitetura: Encoder → Code → Decoder

```
   Entrada → [ ENCODER ] → code → [ DECODER ] → Reconstrução
   (grande)   comprime   (pequeno)  reconstrói    (≈ entrada)
```

> [!note] As três partes
> - **Encoder:** **comprime** os dados de entrada.
> - **Code** (camada latente / *espaço latente*): a **versão comprimida** dos dados — o "gargalo".
> - **Decoder:** **reconstrói** os dados de entrada a partir do code.

---

## 7.3. Como é treinado

> [!important] Função de custo
> O autoencoder é treinado com **gradient descent**, e a **função de custo mede a diferença entre a entrada original e a saída reconstruída**. Quanto menor essa diferença, melhor ele aprendeu a representar os dados.

> [!tip] Por que isso detecta anomalias
> Se o autoencoder aprendeu a reconstruir bem os dados **normais**, então quando aparece um dado **anormal** ele vai ter **dificuldade de reconstruir** → o erro de reconstrução fica **grande** → sinal de anomalia. (Ver [[../10 - Detecção de Anomalias/04 - Deep Learning para Anomalias|Detecção de Anomalias]].)

---

## 7.4. Aplicações

> [!summary] Para que servem
> - **Redução de dimensionalidade** (alternativa ao [[../Tópicos Avançados de Machine Learning/02 - PCA - Redução de Dimensionalidade|PCA]])
> - **Detecção de anomalias**
> - **Geração de dados sintéticos**
> - **Sistemas de recomendação**
> - **Super-resolução de imagens**
> - **Preenchimento de dados faltantes**

---

## 7.5. Variantes de Autoencoder

| Variante | Ideia central | Uso típico |
|---|---|---|
| **Variacional (VAE)** | Em vez de um code fixo, aprende os **parâmetros de uma distribuição de probabilidade**; o espaço latente é uma distribuição da qual se **amostra**. | Geração de dados, anomalias, melhoria de imagens. |
| **Denoising** | Treinado para **remover ruído** dos dados de entrada. | Limpar imagens, remover ruído de áudio. |
| **Esparso (Sparse)** | Usa uma **restrição de esparsidade** no code, forçando representações mais significativas. | Extração de características, redução de dimensionalidade, anomalias. |

> [!note] O VAE é a base de muita IA generativa
> Ao aprender uma **distribuição** (e não um ponto fixo), o autoencoder variacional consegue **gerar amostras novas** parecidas com os dados de treino — ponte com a [[../08 - LLMs e IA Generativa/00 - Índice|IA Generativa]].

---

## 7.6. Atividade do curso: removendo ruído de dígitos

> [!example] O exercício prático
> Usando imagens de **dígitos manuscritos** (28×28 pixels; 60 mil treino, 10 mil teste):
> 1. Criar uma versão **com ruído** dos dados.
> 2. Treinar um **autoencoder simples** (entrada → camada oculta de encoding → saída de decoding).
> 3. Pegar uma imagem aleatória, adicionar ruído.
> 4. Usar `predict` do modelo para **remover o ruído**.
> 5. Comparar o resultado com o original.
>
> Esse é um **Denoising Autoencoder** na prática.

```python
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

entrada = Input(shape=(784,))           # 28x28 = 784 pixels
encoded = Dense(64, activation='relu')(entrada)   # gargalo (code)
decoded = Dense(784, activation='sigmoid')(encoded)  # reconstrução

autoencoder = Model(entrada, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.fit(X_treino_ruido, X_treino, epochs=50)   # entrada com ruído → saída limpa
```

---

## 7.7. Resumo

> [!summary] O essencial dos Autoencoders
> - Rede **não supervisionada** que aprende a **comprimir (encoder)** e **reconstruir (decoder)** dados.
> - O **code** é a versão comprimida (espaço latente).
> - Treinado minimizando a **diferença entre entrada e reconstrução**.
> - Variantes: **Variacional** (gera dados), **Denoising** (tira ruído), **Esparso** (representações significativas).
> - Aplicações: dimensionalidade, **anomalias**, geração de dados, super-resolução.

---

## 🔗 Próximos passos
- [[08 - Detecção de Objetos]] — fechando o módulo com computer vision aplicada a vídeos.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
