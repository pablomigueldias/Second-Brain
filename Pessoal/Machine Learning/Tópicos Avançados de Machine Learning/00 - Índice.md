---
tags:
  - machine-learning
  - tópicos-avançados
  - moc
  - índice
aliases:
  - Tópicos Avançados de ML
---

# 🚀 Tópicos Avançados de Machine Learning

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do tópico **Tópicos Avançados de Machine Learning**. Depois de ver os [[00 - Índice|Fundamentos]] e os [[00 - Índice|Algoritmos]], aqui aprendemos a **refinar, avaliar com rigor e automatizar** modelos de ML — o que separa um projeto amador de um projeto profissional.

---

## 🗺️ Roteiro de Estudo

### 1. Preparação Avançada de Dados
- [[01 - Engenharia de Atributos]] — Tratar dados faltantes, outliers, binning, gerar características.
- [[02 - PCA - Redução de Dimensionalidade]] — Comprimir muitos atributos em poucos atributos sintéticos.
- [[03 - Seleção de Atributos]] — Escolher quais características realmente importam.

### 2. Avaliação Rigorosa de Modelos
- [[04 - Avaliando a Variabilidade de um Modelo]] — Intervalos de confiança: o acerto "real" não é um número fixo.
- [[05 - Avaliando o Desempenho de Modelos]] — Teste de hipótese: a diferença entre dois modelos é real ou acaso?
- [[06 - Custo de um Modelo]] — Nem todo erro custa o mesmo; avaliar pelo dinheiro, não só pela métrica.

### 3. Técnicas Avançadas por Tarefa
- [[07 - Técnicas Avançadas de Clusters]] — Existem grupos de verdade? Quantos? São bons?
- [[08 - Classificação Multilabel]] — Quando uma instância pode ter várias classes ao mesmo tempo.
- [[09 - Datasets Desbalanceados]] — Quando uma classe é muito mais rara que a outra.

### 4. Automação
- [[10 - AutoML e Tuning de Modelos]] — Automatizar a busca pelo melhor modelo e hiperparâmetros.

---

## 🧭 Mapa Mental do Módulo

```
            TÓPICOS AVANÇADOS DE ML
                      |
   ┌──────────────────┼──────────────────────┐
   |                  |                      |
PREPARAR          AVALIAR COM            CASOS
OS DADOS          RIGOR                  ESPECIAIS
   |                  |                      |
 • Eng. Atributos  • Variabilidade      • Clusters avançados
 • PCA             • Teste de hipótese  • Multilabel
 • Seleção         • Custo (R$)         • Desbalanceamento
                      |
                   AUTOMATIZAR
                      |
                   • AutoML / Tuning
```

---

## 🔑 Resumo Ultra-Rápido (cola)

> [!summary] A ideia de cada tópico
> - **Engenharia de Atributos** → "lapidar" os dados antes de treinar.
> - **PCA** → comprimir muitos atributos em poucos.
> - **Seleção de Atributos** → manter só os atributos que ajudam.
> - **Variabilidade** → um modelo de "90%" na verdade varia numa faixa.
> - **Desempenho** → comparar modelos com teste estatístico, não no "olhômetro".
> - **Custo** → traduzir erros em dinheiro perdido.
> - **Clusters avançados** → verificar se o agrupamento faz sentido.
> - **Multilabel** → uma instância pode ter várias classes ao mesmo tempo.
> - **Desbalanceamento** → lidar com classes raras (fraude, doença).
> - **AutoML** → deixar a máquina buscar o melhor modelo sozinha.

---

## 🏷️ Tags Relacionadas
#machine-learning #tópicos-avançados #ia #estudos

> [!tip] Conexão com os outros módulos
> Este módulo usa muito do que veio antes. Conceitos como **overfitting**, **matriz de confusão**, **precisão/recall** ([[00 - Índice|Fundamentos]]) e algoritmos como **Random Forest**, **Naive Bayes**, **K-means** ([[00 - Índice|Algoritmos]]) são pré-requisito. Vale tê-los à mão.
