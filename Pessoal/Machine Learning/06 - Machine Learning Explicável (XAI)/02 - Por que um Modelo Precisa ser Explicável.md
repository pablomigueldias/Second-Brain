---
tags:
  - machine-learning
  - xai
  - explicabilidade
  - ética-ia
---

# 2. Por que um Modelo Precisa ser Explicável

> [!info] O que esta nota cobre
> As **6 razões** pelas quais explicar um modelo importa — com os casos reais que motivam cada uma. Quando algoritmos decidem por nós, a pergunta é inevitável: **até que ponto podemos confiar?**

---

## 2.1. O pano de fundo

> [!note] O contexto
> Algoritmos estão tomando **cada vez mais decisões**, de forma **automática**. Em muitas dessas decisões, o impacto na vida das pessoas é enorme:
> - **Diagnóstico médico**
> - **Aprovação de crédito**
> - **Veículos autônomos**
> - **Decisões judiciais**
> - **Contratação de funcionários**

> [!question] A pergunta central
> Até que ponto podemos **confiar** nesses modelos — especialmente quando não entendemos como eles decidem?

---

## 2.2. As 6 razões para exigir explicabilidade

### 1. Questões Legais
> [!note]
> A **legislação obriga**. Em vários domínios (crédito, dados pessoais), a lei exige que decisões automatizadas possam ser **justificadas** ao cidadão. Conecta-se com regulações como o [[../../Criar valor com IA, automação e bots/Modulos/06 - Guardar Dados na Era da IA|GDPR]].

### 2. Reputação
> [!warning] Quando a IA toma uma decisão preconceituosa
> Modelos podem **reproduzir vieses** dos dados de treino e gerar decisões **discriminatórias**, causando dano de imagem. (Há reportagens conhecidas de "5 vezes em que a IA foi discriminatória".)

### 3. Segurança Jurídica / Financeira
> [!example] O caso do carro autônomo
> Um **veículo autônomo provoca um acidente** (houve um caso fatal real, da Uber, em 2018, no Arizona). **Como planejar uma defesa** sem entender por que o modelo agiu daquele jeito? Sem explicabilidade, não há como apurar responsabilidade.

### 4. Depuração (Debugging)
> [!important] Precisão não basta
> Normalmente o modelo é testado por **precisão e outras métricas**. Mas isso é **suficiente**? Um modelo pode ter ótima precisão e ainda assim ter **enviesamento no treino** (aprendeu a coisa certa pela razão errada). Explicar ajuda a **caçar esse tipo de bug**.

### 5. Prevenção de Ataques
> [!warning] Um modelo pode ser "hackeado"
> Existe o **One Pixel Attack**: mudar **um único pixel** de uma imagem pode enganar uma rede neural profunda e fazê-la classificar errado. Entender o modelo ajuda a **identificar e prevenir** essas vulnerabilidades.

### 6. Questão "Pessoal"
> [!note]
> Às vezes é simplesmente humano: um **executivo quer entender** a decisão antes de bancá-la. Confiança organizacional também conta.

---

## 2.3. Resumo

> [!summary] As 6 razões
> 1. **Legal** — a lei obriga.
> 2. **Reputação** — evitar decisões discriminatórias.
> 3. **Jurídico/Financeiro** — apurar responsabilidade (ex.: acidente de carro autônomo).
> 4. **Depuração** — precisão não revela viés no treino.
> 5. **Ataques** — detectar vulnerabilidades (ex.: one pixel attack).
> 6. **Pessoal** — pessoas querem entender antes de confiar.

---

## 🔗 Próximos passos
- [[03 - Conceitos de Explicabilidade]] — o vocabulário técnico de XAI (monotonicidade, local vs. global, agnóstico vs. específico).

---
[[00 - Índice|⬅️ Voltar ao Índice]]
