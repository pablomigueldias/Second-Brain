---
tags:
  - machine-learning
  - xai
  - explicabilidade
  - white-box
  - black-box
---

# 4. Modelos White-Box e Black-Box

> [!info] O que esta nota cobre
> A grande divisão da explicabilidade: modelos **White-Box** (transparentes, fáceis de interpretar) e **Black-Box** (opacos, alta capacidade mas difíceis de explicar). Quais são quais, e por quê.

---

## 4.1. A divisão

> [!note] Duas famílias
> - **White-Box (caixa-branca):** modelos de **fácil interpretação/entendimento**. Você consegue ler **por que** decidiram.
> - **Black-Box (caixa-preta):** modelos que **não podem ser interpretados diretamente** — entram dados, saem decisões, e o "meio" é opaco.

```
   Dados → [  MODELO  ] → Decisão
            White-box: você vê o porquê
            Black-box: você só vê a saída
```

---

## 4.2. Modelos White-Box

> [!summary] Os transparentes
> - **Regressão Linear** — lê-se direto nos coeficientes (peso de cada variável).
> - **Regressão Logística** — idem, para classificação.
> - **Árvores de Decisão** — segue-se o caminho de regras.
> - **Modelos Baseados em Regras** — `SE (umidade = alta) E (aparência = ensolarado) ENTÃO não joga`.
> - **Naive Bayes** — probabilidades explícitas por atributo.
> - **Redes Bayesianas** — grafo de dependências probabilísticas.

> [!example] Regras são o ápice da transparência
> ```
> (humidity = high) and (outlook = sunny)  => play = no  (3.0/0.0)
> (outlook = rainy) and (windy = TRUE)     => play = no  (2.0/0.0)
>                                          => play = yes (9.0/0.0)
> ```
> Qualquer pessoa lê e entende **exatamente** por que o modelo decide.

---

## 4.3. Modelos Black-Box

> [!warning] Os opacos (alta capacidade, baixa transparência)
> - **Redes Neurais Artificiais** — milhares de pesos sem significado individual legível.
> - **Máquina de Vetor de Suporte (SVM)** — fronteiras em espaços de alta dimensão.
> - **Modelos baseados em grupos / ensembles** — **Random Forests**, **Gradient Boosting**, **XGBoost**.

> [!example] Por que uma rede neural é black-box
> Um modelo treinado vira uma lista enorme de pesos assim:
> ```
> Sigmoid Node 2:
>   Threshold -0.4838
>   Attrib outlook=sunny   1.8088
>   Attrib outlook=rainy   0.6504
>   Attrib humidity=normal -3.6163
>   ...
> ```
> Tecnicamente está "tudo ali", mas é **humanamente impossível** olhar esses números e dizer *por que* o modelo classificou uma instância de um jeito. Daí o nome caixa-preta.

---

## 4.4. Como escolher (o trade-off na prática)

> [!important] A decisão de projeto
> | Você precisa de... | Prefira... |
> |---|---|
> | **Explicar cada decisão** (crédito, saúde, justiça) | **White-box** (ou black-box + LIME/SHAP) |
> | **Máxima performance** e a explicação é secundária | **Black-box** (RF, XGBoost, redes) |
>
> Se você **precisa** de um black-box mas também de explicação, aplique as técnicas da nota [[03 - Conceitos de Explicabilidade|anterior]] (**LIME**, **SHAP**).

---

## 4.5. Resumo

> [!summary] O essencial
> - **White-box** (transparentes): regressão linear/logística, árvores, regras, Naive Bayes, redes bayesianas.
> - **Black-box** (opacos): redes neurais, SVM, Random Forest, Gradient Boosting/XGBoost.
> - Trade-off: white-box explica fácil; black-box rende mais mas precisa de **LIME/SHAP** para ser explicado.

---

## 🔗 Próximos passos
- Fim do módulo de XAI! Volte ao [[00 - Índice]] ou siga para [[../07 - Processamento de Linguagem Natural (NLP)/00 - Índice|Processamento de Linguagem Natural (NLP)]].
- No [[../14 - Projeto Final/Projeto Final - Adult Income|Projeto Final]], usar XAI para explicar o modelo é **obrigatório**.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
