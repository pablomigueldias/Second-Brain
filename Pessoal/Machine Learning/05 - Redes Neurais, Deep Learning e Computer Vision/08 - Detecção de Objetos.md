---
tags:
  - machine-learning
  - deep-learning
  - computer-vision
  - deteccao-objetos
  - opencv
---

# 8. Detecção de Objetos

> [!info] O que esta nota cobre
> **Detecção de objetos**: a tarefa de **identificar E localizar** objetos em imagens e vídeos. A diferença para classificação, aplicações reais, e o uso de **OpenCV** com modelos pré-treinados.

---

## 8.1. O que é Detecção de Objetos

> [!note] Definição
> **Detecção de Objetos** = **identificação E localização** de objetos em imagens.

> [!important] Classificação ≠ Detecção
> - **Classificação** ([[05 - CNN - Redes Convolucionais|CNN]]) responde: *"o que é esta imagem?"* → "é um gato".
> - **Detecção** responde: *"o que existe na imagem E onde?"* → "há **um gato aqui** (caixa) e **um carro ali** (outra caixa)".
>
> A detecção desenha **caixas delimitadoras** (*bounding boxes*) ao redor de cada objeto.

---

## 8.2. Aplicações

> [!summary] Onde é usada
> - **Veículos autônomos** (detectar pedestres, carros, placas)
> - **Sistemas de vigilância**
> - **Análise de imagens médicas**
> - Identificar **produtos faltantes em prateleiras**
> - **Contagem** de veículos ou objetos
> - **Rastreamento** de jogadores ou da bola (esportes)

---

## 8.3. OpenCV: a ferramenta

> [!note] OpenCV
> **OpenCV** = *Open Source Computer Vision Library*. É **a** biblioteca padrão de visão computacional.
> - Em Python, o módulo se chama **`cv2`**.
> - Pode **carregar modelos pré-treinados** — você não precisa treinar do zero.

> [!tip] Modelos pré-treinados poupam muito trabalho
> O curso usou o **MobileNet-SSD** (arquivos `MobileNetSSD_deploy.caffemodel` e `.prototxt`), um modelo já treinado para detectar dezenas de classes de objetos. Você só **carrega** e **usa**.

---

## 8.4. Esqueleto em Python (OpenCV + MobileNet-SSD)

```python
import cv2

# Carregar o modelo pré-treinado (arquitetura .prototxt + pesos .caffemodel)
net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)

# Ler um vídeo de teste
video = cv2.VideoCapture("people.mp4")

while True:
    ok, frame = video.read()
    if not ok:
        break

    # Preparar o frame e passar pela rede
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    deteccoes = net.forward()

    # Para cada detecção com confiança alta, desenhar a caixa
    for i in range(deteccoes.shape[2]):
        confianca = deteccoes[0, 0, i, 2]
        if confianca > 0.5:
            # ... extrair coordenadas e desenhar o bounding box no frame
            pass

    cv2.imshow("Deteccao", frame)
    if cv2.waitKey(1) == 27:  # ESC para sair
        break
```

> [!example] No curso
> Foram usados dois vídeos de teste (`people.mp4` e `nopeople.mp4`) para mostrar o modelo detectando (ou não) pessoas em movimento, desenhando caixas em tempo real.

---

## 8.5. Resumo

> [!summary] O essencial
> - Detecção de objetos = **identificar + localizar** (caixas delimitadoras).
> - Diferente de **classificação**, que só diz "o que é" a imagem inteira.
> - **OpenCV (`cv2`)** é a biblioteca padrão; carrega **modelos pré-treinados** (ex.: MobileNet-SSD).
> - Aplicações: carros autônomos, vigilância, contagem, rastreamento esportivo.

---

## 🔗 Próximos passos
- Você terminou o módulo de Redes Neurais! Volte ao [[00 - Índice]] ou siga para o próximo módulo do curso: [[../06 - Machine Learning Explicável (XAI)/00 - Índice|Machine Learning Explicável (XAI)]].

---
[[00 - Índice|⬅️ Voltar ao Índice]]
