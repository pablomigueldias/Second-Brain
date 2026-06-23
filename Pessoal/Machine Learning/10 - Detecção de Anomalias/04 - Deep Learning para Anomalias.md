---
tags:
  - machine-learning
  - detecção-anomalias
  - deep-learning
  - autoencoders
  - lstm
---

# 4. Deep Learning para Anomalias

> [!info] O que esta nota cobre
> Como usar **deep learning** para detectar anomalias: **Autoencoders** (via erro de reconstrução) e **LSTM** (via erro de previsão). Ambos partem da mesma ideia genial: *aprenda o normal e meça o quanto algo difere dele.*

---

## 4.1. A ideia comum

> [!important] O truque central
> As duas técnicas seguem o mesmo raciocínio:
> 1. Treinar um modelo para aprender **muito bem o comportamento normal**.
> 2. Quando aparece algo **anormal**, o modelo **falha** — e essa falha é o sinal.

---

## 4.2. Autoencoders

> [!note] Como detecta anomalias
> Um **[[../05 - Redes Neurais, Deep Learning e Computer Vision/07 - Autoencoders|Autoencoder]]** (aprendizado **não supervisionado**) aprende a **comprimir e reconstruir** os dados:
> - Aprende a representar os dados com **codificação (encoder) e decodificação (decoder)**.
> - Para dados **normais**, reconstrói bem (erro pequeno).
> - Para dados **anormais**, tem **dificuldade de reconstruir** → **erro grande** → anomalia.

> [!example] Intuição
> É como alguém que só viu gatos a vida toda. Peça para desenhar um gato de memória: sai perfeito. Peça para desenhar um animal exótico que nunca viu: sai torto. O "quanto saiu torto" (erro de reconstrução) denuncia que aquilo é **fora do padrão aprendido**.

```
   Dado normal   → autoencoder → reconstrução ≈ original   (erro baixo ✓)
   Dado anômalo  → autoencoder → reconstrução ✗ original   (erro ALTO → anomalia)
```

---

## 4.3. LSTM

> [!note] Como detecta anomalias
> A **[[../05 - Redes Neurais, Deep Learning e Computer Vision/06 - LSTM e Redes Recorrentes|LSTM]]** (rede recorrente para sequências) é usada para **prever os próximos dados** de uma série:
> - Se houver **anomalia**, a LSTM terá **dificuldade de prever**.
> - A **diferença entre a previsão e o valor real** será **grande** → anomalia.

> [!example] Intuição
> A LSTM aprendeu o "ritmo" normal das vendas. Ela prevê: "amanhã ~100 unidades". Se vier **2.000**, a previsão errou feio — e esse erro gritante é o alarme de anomalia.

> [!tip] LSTM é para dados sequenciais/temporais
> Use LSTM quando a anomalia depende da **ordem temporal** (uma sequência estranha), e não de um ponto isolado. Conecta-se diretamente com [[05 - Séries Temporais]].

---

## 4.4. Comparação

> [!summary] O sinal de anomalia em cada um
> | Técnica | Aprende a... | Sinal de anomalia |
> |---|---|---|
> | **Autoencoder** | reconstruir os dados | **erro de reconstrução** alto |
> | **LSTM** | prever o próximo valor da sequência | **erro de previsão** alto |

---

## 4.5. Resumo

> [!summary] O essencial
> - Deep learning detecta anomalia **aprendendo o normal** e medindo o **desvio**.
> - **Autoencoder:** anomalia = **erro de reconstrução** alto (não consegue reconstruir o estranho).
> - **LSTM:** anomalia = **erro de previsão** alto (não consegue prever o estranho); para dados **temporais**.

---

## 🔗 Próximos passos
- [[05 - Séries Temporais]] — técnicas específicas para anomalias em dados que dependem do tempo.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
