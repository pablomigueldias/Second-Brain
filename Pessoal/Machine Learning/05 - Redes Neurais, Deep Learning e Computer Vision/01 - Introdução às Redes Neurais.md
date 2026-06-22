---
tags:
  - machine-learning
  - redes-neurais
  - deep-learning
  - fundamentos
---

# 1. Introdução às Redes Neurais

> [!info] O que esta nota cobre
> A **ideia central** das redes neurais artificiais: por que elas se inspiram no cérebro, o que é um neurônio (natural e artificial) e onde essa tecnologia é aplicada.

---

## 1.1. A inspiração: o cérebro

> [!note] A ideia
> **Redes Neurais Artificiais (RNA)** buscam **simular o funcionamento do cérebro** dos seres vivos. Não é uma cópia fiel — é uma inspiração matemática.

No cérebro, a unidade básica é o **neurônio natural**, formado por três partes que importam para a analogia:

| Parte do neurônio | Função | Equivalente na RNA |
|---|---|---|
| **Dendritos** | Recepção dos sinais de entrada | Entradas (atributos) |
| **Corpo** | Processa/soma os sinais | Soma ponderada + ativação |
| **Axônio** (terminal) | Transmite o sinal adiante | Saída |

> [!example] Pense assim
> Um neurônio recebe vários "cutucões" (dendritos). Se a soma deles passar de um certo limite, ele "dispara" e manda um sinal pelo axônio para os próximos neurônios. A rede neural artificial faz exatamente isso, só que com **números e pesos** no lugar de impulsos elétricos.

---

## 1.2. O que é uma Rede Neural Artificial

Uma RNA é um conjunto de **neurônios artificiais conectados em camadas**. Cada conexão tem um **peso** (importância), e a rede "aprende" ajustando esses pesos a partir dos dados — exatamente como vimos no resto do curso, mas agora com uma estrutura inspirada no cérebro.

> [!tip] Conexão com o que você já sabe
> No fundo, continua sendo o mesmo jogo do ML: a rede recebe **atributos de entrada**, faz contas, e produz uma **saída** (uma classe ou um número). A diferença é a **arquitetura** rica em camadas, que permite aprender padrões muito mais complexos.

---

## 1.3. Onde redes neurais são usadas

> [!summary] Aplicações
> - **Previsão** (regressão de valores futuros)
> - **Classificação de imagens** (é um gato ou um cachorro?)
> - **Reconhecimento de fala** (áudio → texto)
> - **Tradução** (um idioma → outro)
> - **Detecção de anomalias** (fraudes, falhas em equipamentos)
> - … e praticamente todo o campo moderno da IA.

---

## 1.4. Resumo

> [!summary] O essencial
> - RNAs **imitam** (de forma simplificada) o cérebro.
> - Unidade básica = **neurônio artificial**: entradas → soma ponderada → ativação → saída.
> - **Aprender** = ajustar os **pesos** das conexões usando dados.
> - São a base de **deep learning**, **computer vision** e **NLP**.

---

## 🔗 Próximos passos
- [[02 - Perceptron]] — vamos abrir o neurônio artificial mais simples e ver, número a número, como ele aprende.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
