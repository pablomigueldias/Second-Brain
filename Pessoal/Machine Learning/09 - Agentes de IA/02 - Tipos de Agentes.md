---
tags:
  - machine-learning
  - agentes-ia
  - tipos-agentes
---

# 2. Tipos de Agentes

> [!info] O que esta nota cobre
> Os **sete tipos de agentes**, do mais simples ao mais complexo: reativos, autônomos, baseados em modelo, em objetivos, em utilidade, com aprendizado e multiagente — cada um com exemplos reais.

---

## 2.1. A escala de sofisticação

> [!note] Uma ideia organizadora
> Os tipos vão de "**reage ao agora**" (reativo) até "**aprende, planeja e coopera**" (com aprendizado / multiagente). Quanto mais para baixo na lista, mais o agente leva em conta **modelo do mundo, objetivos, valor esperado e experiência**.

---

## 2.2. Os sete tipos

### 1. Agentes Reativos
> [!note]
> Reagem **diretamente ao estado atual**, sem memória nem planejamento.
> - Robôs que **desviam de obstáculos**.
> - Climatização que liga/desliga conforme a temperatura **atual**.
> - **NPCs** (personagens não jogáveis) em jogos.

### 2. Agentes Autônomos
> [!note]
> Operam por conta própria em tarefas longas e complexas.
> - **Carros autônomos** em longos trajetos.
> - Agentes em jogos complexos (**StarCraft II, Dota 2**).
> - Monitoramento e **resposta a incidentes** (segurança cibernética).
> - Robôs exploradores em **Marte** (Perseverance).

### 3. Agentes Baseados em Modelo
> [!note]
> Mantêm um **modelo interno do ambiente** para prever o que vai acontecer.
> - Robôs que **mapeiam o ambiente** (SLAM).
> - Agentes de trânsito que **preveem** onde o tráfego vai piorar.
> - Drones que ajustam o voo com base em **estimativas de vento**.

### 4. Agentes Baseados em Objetivos
> [!note]
> Agem para **alcançar uma meta**, planejando os passos.
> - Planejadores de **rotas (GPS)**.
> - Agentes que traçam **estratégia para vencer** um jogo.
> - Bots que **minimizam custos** em logística.

### 5. Agentes Baseados em Utilidade
> [!note]
> Não só atingem o objetivo — buscam a **melhor** forma, maximizando uma "utilidade" (valor esperado).
> - Agentes de **negociação** (melhor acordo possível).
> - Carros autônomos que **equilibram** segurança, conforto e tempo.
> - Recomendação que prioriza opções de **maior valor esperado**.

### 6. Agentes com Aprendizado
> [!note]
> **Melhoram com a experiência**.
> - **AlphaGo** (aprendeu a jogar Go).
> - Recomendação de conteúdo que **se adapta** ao seu gosto.
> - Robôs que **aprendem a caminhar** em terrenos novos.

### 7. Agentes Multiagente
> [!note]
> **Vários agentes** interagindo/cooperando.
> - **Tráfego inteligente** com veículos coordenados.
> - E-commerce com agentes **vendedores e compradores**.
> - Ambientes simulados com **agentes sociais** (ex.: economia simulada).

---

## 2.3. Tabela-resumo

> [!summary] Visão rápida
> | Tipo | O que o caracteriza |
> |---|---|
> | **Reativo** | Reage ao estado atual, sem memória |
> | **Autônomo** | Opera sozinho em tarefas complexas |
> | **Baseado em Modelo** | Tem modelo interno do mundo (prevê) |
> | **Baseado em Objetivos** | Planeja para atingir uma meta |
> | **Baseado em Utilidade** | Otimiza a melhor forma (valor esperado) |
> | **Com Aprendizado** | Melhora com a experiência |
> | **Multiagente** | Vários agentes interagindo |

---

## 🔗 Próximos passos
- [[03 - RAG (Retrieval-Augmented Generation)]] — uma técnica essencial para dar a um agente conhecimento sobre **seus** documentos.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
