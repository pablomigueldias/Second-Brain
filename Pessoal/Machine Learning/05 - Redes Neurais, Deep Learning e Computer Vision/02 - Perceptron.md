---
tags:
  - machine-learning
  - redes-neurais
  - perceptron
  - classificação
  - supervisionado
---

# 2. Perceptron

> [!info] O que esta nota cobre
> O **perceptron**: o neurônio artificial mais simples. Como ele classifica de forma **linear**, como funciona a **função de ativação**, a **taxa de aprendizado**, o **ajuste de pesos** passo a passo, e os conceitos de **epoch, iteration e batch**.

---

## 2.1. O que é o Perceptron

> [!note] Definição
> O **Perceptron** é um **classificador simples de uma única camada**. Ele recebe **n atributos de entrada** e produz uma **saída binária** (no curso: **1** ou **−1**).

```
   x1 ──(w1)──┐
   x2 ──(w2)──┤
   x3 ──(w3)──┼──► Σ (soma ponderada) ──► Ativação ──► saída (1 ou -1)
   ...        │
   xm ──(wm)──┘
```

A conta interna é uma **soma ponderada**: cada entrada `x` é multiplicada pelo seu **peso** `w`, e tudo é somado. Esse resultado passa pela **função de ativação**.

---

## 2.2. A Função de Ativação

> [!note] Regra de decisão (função degrau)
> $$ \text{saída} = \begin{cases} \;\;1 & \text{se } f > 0 \\ -1 & \text{se } f \le 0 \end{cases} $$

Ou seja: se a soma ponderada for **positiva**, a saída é **1**; senão, é **−1**. É uma **função degrau** (threshold) — ela "corta" o resultado em duas classes. É isso que torna o perceptron um **classificador linear**: ele traça uma **reta (hiperplano)** que separa as duas classes.

---

## 2.3. Treinamento: ajustando os pesos

O perceptron **aprende** comparando a saída que ele deu (`Y`) com a saída esperada (`d`). Se errou, ajusta os pesos na direção certa.

> [!note] A regra de atualização
> Para cada peso:
> $$ w_{novo} = w_{antigo} + \alpha \cdot (d - Y) \cdot \frac{x}{2} $$
> Onde:
> - **Y** = saída que o modelo deu
> - **d** = saída esperada (o rótulo verdadeiro)
> - **α** = taxa de aprendizado (*step size*)
> - **x** = valor do atributo

> [!example] Exemplo do curso (um passo do ajuste)
> Com peso `−2,10137`, α = 0,5, saída esperada `d = −1`, saída dada `Y = 1` e atributo `x = 3,1`:
> $$ -2{,}10137 + 0{,}5 \times (-1 - 1) \times \frac{3{,}1}{2} = -3{,}65137 $$
> O peso foi corrigido "para baixo" porque o modelo errou (deu 1 quando devia dar −1).

> [!tip] Há também o ajuste do "bias" (fator de tendência)
> Além dos pesos dos atributos, ajusta-se um **fator de tendência** (bias), que desloca o hiperplano. Ele é tratado como um peso de uma entrada constante (= −1 no exemplo do curso).

---

## 2.4. A Taxa de Aprendizado (Step Size)

> [!warning] Escolher α é uma arte de equilíbrio
> | Valor de α | O que acontece |
> |---|---|
> | **= 0** | O modelo **nunca converge** (não muda os pesos). |
> | **Muito baixo** | Algoritmo **lento**: correções pequenas demais, demora a chegar lá. |
> | **Muito alto** | Algoritmo **lento/instável**: correções grandes demais, **ultrapassa** o ponto ideal e fica oscilando. |

> [!summary] Guarde isto
> A taxa de aprendizado controla **o tamanho do passo** a cada correção. Nem tão pequeno (lento), nem tão grande (passa do ponto). É um dos hiperparâmetros mais importantes de qualquer rede neural.

---

## 2.5. Margem e convergência

> [!note] Margem
> **Margem** é a **distância mínima entre uma instância e o hiperplano** que separa as classes. Quanto **mais próximas** as instâncias estão da fronteira, **mais difícil** é o treino (a separação é "apertada").

> [!warning] Limite do perceptron
> O perceptron simples só resolve problemas **linearmente separáveis** (que dá para separar com uma reta). Se os dados não puderem ser separados por uma reta, ele **não converge**. A solução para isso são as **redes com várias camadas** (próximas notas).

---

## 2.6. Epoch vs. Iteration vs. Batch

> [!important] Três palavras que você vai ver o tempo todo
> - **Iteration (iteração):** um passo de atualização do modelo (processar instância(s) e ajustar pesos).
> - **Epoch:** uma passagem **completa** por **todos** os dados de treino.
> - **Batch size:** **quantas** instâncias são processadas antes de atualizar os pesos.

### Aprendizado Online vs. Batch

| Modo | Quando os pesos são atualizados |
|---|---|
| **Online** | A **cada instância** (no fim de cada iteração). |
| **Batch** | Só **depois de ver todas** as instâncias (no fim da epoch). |

> [!example] Analogia
> **Online** = corrigir a prova questão por questão, mudando de estratégia a cada uma. **Batch** = corrigir a prova inteira e só então repensar a estratégia. Online aprende mais rápido mas é mais "nervoso"; batch é mais estável mas mais lento.

---

## 2.7. Resumo

> [!summary] O essencial do Perceptron
> - É o **neurônio artificial** de **uma camada**; classificador **linear**.
> - Faz **soma ponderada** das entradas → **função de ativação** (degrau) → saída 1 ou −1.
> - **Aprende** ajustando pesos: `w += α·(d−Y)·x/2`.
> - **α (taxa de aprendizado)**: nem alto nem baixo demais.
> - **Epoch** = volta completa nos dados; **batch** = nº de instâncias por atualização.
> - Só resolve problemas **linearmente separáveis** → motivação para redes profundas.

---

## 🔗 Próximos passos
- [[03 - Arquitetura de Redes Neurais]] — empilhando neurônios em camadas para resolver problemas que o perceptron sozinho não dá conta.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
