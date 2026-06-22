---
tags:
  - machine-learning
  - deep-learning
  - lstm
  - redes-recorrentes
  - series-temporais
---

# 6. LSTM e Redes Recorrentes

> [!info] O que esta nota cobre
> As **LSTM (Long Short-Term Memory)**: redes neurais **recorrentes** capazes de lidar com **dependências de longo prazo** em dados sequenciais. Quando usar (e quando não), e o exemplo de previsão de ações do curso.

---

## 6.1. O que é uma LSTM

> [!note] Definição
> **LSTM (Long Short-Term Memory)** é um tipo de **Rede Neural Recorrente (RNN)**. "Recorrente" significa que ela é **capaz de tratar dados com dependências** — onde o que vem **agora** depende do que veio **antes**.

> [!tip] A palavra-chave é MEMÓRIA
> Diferente de uma rede feed-forward (que esquece tudo a cada entrada), a LSTM **mantém memória** do que já viu. Por isso o nome: memória de **longo e curto prazo**.

---

## 6.2. Recorrência: quando ela importa?

A grande pergunta é: **os dados dependem uns dos outros em sequência?**

| Sem dependência (NÃO precisa de LSTM) | Com dependência (LSTM brilha) |
|---|---|
| **Transações fraudulentas:** uma transação ser fraude **não afeta** a próxima. | **Tradução de texto:** a próxima palavra **depende** das anteriores. |
| Cada caso é independente. | **Vendas:** ligadas ao **tempo** (sazonalidade, demanda, marketing). |

> [!example] Por que a ordem importa
> Na frase "Eu **não** gostei do filme", a palavra "não" muda todo o sentido. Uma rede sem memória poderia ver "gostei" e errar. A LSTM **lembra** do "não" anterior. O mesmo vale para prever vendas de dezembro: depende da tendência dos meses anteriores.

---

## 6.3. Benefícios e aplicações

> [!summary] Benefícios
> - **Lembra de informações a longo prazo** (não só do último passo).
> - **Adapta o comportamento** mesmo para padrões complexos.

> [!note] Aplicações
> - Reconhecimento de **voz**
> - **Tradução**
> - **Previsão de séries temporais** (vendas, preços)
> - **Processamento de Linguagem Natural** (NLP)

---

## 6.4. Exemplo do curso: prever o preço da ação do Google

> [!example] O problema
> Prever o **preço de fechamento** das ações do Google.
> - **Treino:** `Google_Stock_Price_Train.csv` → 2012–2016 (5 anos).
> - **Teste:** `Google_Stock_Price_Test.csv` → Jan/2017 (20 dias).

> [!important] A transformação dos dados (o pulo do gato)
> A LSTM aprende com **janelas deslizantes**:
> - **Variável de resposta (Y):** o fechamento de **1 dia**.
> - **Variáveis explicativas (X):** os **60 dias anteriores**.
>
> Ou seja, para prever o dia 61, a rede olha os dias 1–60. Para prever o dia 62, olha os dias 2–61. E assim por diante:
>
> | ... | X58 | X59 | X60 | **Y** |
> |---|---|---|---|---|
> | ... | 22 | 23 | 24 | **25** |
> | ... | 23 | 24 | 25 | **26** |
> | ... | 24 | 25 | 26 | **27** |

> [!warning] "Transformação intensa de dados!"
> O maior trabalho aqui não é treinar a rede — é **preparar os dados** nesse formato de janelas. Isso é típico de séries temporais.

---

## 6.5. Resumo

> [!summary] O essencial da LSTM
> - É uma **RNN** com **memória** de longo prazo.
> - Use quando os dados têm **dependência sequencial/temporal** (texto, séries, voz).
> - **Não** use quando os casos são independentes (ex.: detecção de fraude por transação isolada).
> - Em séries temporais, os dados viram **janelas deslizantes** (ex.: 60 dias → prever o próximo).

---

## 🔗 Próximos passos
- [[07 - Autoencoders]] — outra arquitetura especial, focada em **comprimir e reconstruir** dados.
- Veja também o uso de LSTM em [[../10 - Detecção de Anomalias/04 - Deep Learning para Anomalias|detecção de anomalias]].

---
[[00 - Índice|⬅️ Voltar ao Índice]]
