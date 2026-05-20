---
tags:
  - machine-learning
  - introdução
  - fundamentos
---

# 1. Introdução ao Machine Learning

> [!question] O que é Machine Learning?
> **Machine Learning (ML)** = **Aprendizado de Máquina**. É a capacidade de um **computador aprender** — sem ser programado explicitamente para cada situação possível.

A pergunta importante é: **mas o que é aprender?**

---

## 1.1. O que é Aprendizagem?

> [!note] Definição
> **Aprendizagem** é o **processo de adquirir conhecimento**.

Repare em duas palavras-chave:

- **Processo** → porque é **contínuo e evolutivo**. Ninguém aprende tudo de uma vez; aprende-se aos poucos, com o tempo, com novas experiências.
- **Conhecimento** → o resultado, aquilo que fica.

### Como ocorre a aprendizagem?

Através da **relação com o ambiente**. Um ser que aprende:

1. **Interage** com o que está ao redor.
2. **Recebe estímulos** (informações, dados, feedback).
3. **Ajusta** seu comportamento.
4. **Melhora** com o tempo.

> [!example] Exemplo humano
> Uma criança aprende a não tocar em algo quente porque um dia tocou e sentiu dor. A relação com o ambiente (estímulo de dor) gerou conhecimento.

---

## 1.2. A Máquina Também é Capaz de Aprender

A máquina aprende seguindo princípios parecidos com os seres vivos:

> [!info] Como a máquina aprende
> - **Interage com o ambiente** — através de **dados** e, em alguns casos, de **reforço** (recompensa/punição).
> - **Os dados** são a "experiência" que alimenta o aprendizado.
> - O aprendizado é **persistido** em um **modelo** (o conhecimento "salvo").
> - O aprendizado **evolui** com mais dados ou novos exemplos.
> - O aprendizado **pode ser medido** (avaliamos se está bom ou ruim).

### Comparação rápida: humano vs. máquina

| Conceito | Humano | Máquina |
|---|---|---|
| Fonte do aprendizado | Experiências e sentidos | Dados |
| Onde fica o conhecimento | Memória/cérebro | Modelo |
| Como melhora | Praticando | Treinando com mais dados |
| Como saber se aprendeu | Provas, testes da vida | Métricas de avaliação |

---

## 1.3. Como a Máquina Aprende? (O Fluxo Básico)

Esse é **o coração** de tudo em ML:

```
   ┌─────────┐       ┌─────────────────┐       ┌──────────┐
   │  DADOS  │  ──▶  │   ALGORITMO +   │  ──▶  │  MODELO  │
   │         │       │  PROCESSAMENTO  │       │          │
   └─────────┘       └─────────────────┘       └──────────┘
```

> [!example] Exemplo concreto: "vou poder jogar?"
> Imagine que você quer prever se vai dar para jogar bola lá fora baseado no clima.
>
> **Dados (entrada)**: uma tabela com várias situações já vividas.
>
> | Aparência | Temperatura | Umidade | Ventoso | Jogar? |
> |---|---|---|---|---|
> | ensolarado | quente | alta | FALSO | não |
> | nublado | quente | alta | FALSO | sim |
> | chuvoso | amena | alta | FALSO | sim |
> | chuvoso | frio | normal | VERDADEIRO | não |
> | ... | ... | ... | ... | ... |
>
> **Algoritmo + Processamento**: o algoritmo "olha" para esses dados e descobre padrões (ex: "quando chove e venta, ninguém joga").
>
> **Modelo (saída)**: uma estrutura — por exemplo uma **árvore de decisão** — que consegue responder a pergunta para situações **novas** que ele nunca viu antes.

### O ciclo continua: nova informação

Quando chega uma **nova informação** (um dia novo, com condições diferentes), o modelo:

1. Recebe os dados desse dia.
2. Usa o que aprendeu.
3. Retorna uma **previsão** ("hoje dá pra jogar").

E, melhor ainda, novos dados podem ser usados para **atualizar e melhorar o modelo** ao longo do tempo.

---

## 1.4. Resumo da Introdução

> [!summary] Em uma frase
> Machine Learning é o processo pelo qual um computador **aprende padrões a partir de dados** e gera um **modelo** capaz de fazer **previsões ou decisões** em situações novas.

### Para gravar
- ML ≠ programação tradicional. Em vez de escrevermos as regras, **as regras são descobertas a partir dos dados**.
- Três componentes que sempre aparecem: **DADOS → ALGORITMO → MODELO**.
- O modelo é o "conhecimento congelado" da máquina.

---

## 🔗 Próximos passos
- [[02 - Aplicações do Machine Learning]] — onde tudo isso é usado de verdade.
- [[03 - Definições e Conceitos Básicos]] — vocabulário técnico para entender tudo daqui em diante.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
