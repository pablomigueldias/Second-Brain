---
tags:
  - machine-learning
  - tópicos-avançados
  - automl
  - tuning
  - hiperparâmetros
---

# 10. AutoML e Tuning de Modelos

> [!info] O que esta nota cobre
> O **AutoML** (Machine Learning Automatizado) e o **tuning de hiperparâmetros**: por que ajustar modelos manualmente é inviável, a diferença entre **parâmetros e hiperparâmetros**, as estratégias de busca (Grid Search, Random Search, Otimizador Bayesiano, Algoritmos Genéticos) e a técnica de **Multi-Fidelity**.

---

## 10.1. Por que AutoML?

> [!warning] O problema com processos de ML
> Processos de Machine Learning são:
> - **COMPLEXOS**
> - de **ALTO CUSTO HUMANO**
> - de **ALTO CUSTO COMPUTACIONAL**
> - de **RISCOS GRANDES**

> [!note] O que o AutoML busca
> - **Automatizar o processo** de ML.
> - **Reduzir a interferência humana**.
> - **Melhorar a performance computacional**.
> - **Melhorar a performance dos modelos**.

### Por que usar AutoML?

> [!info] Motivações
> - Criar modelos de ML **mais eficientes**.
> - Construir **produtos orientados a dados**.
> - **Participar de competições** de Machine Learning.

---

## 10.2. AutoML é Tuning!

> [!important] O ponto central
> AutoML **não se trata apenas de automatizar** — trata-se de automatizar **buscando melhor performance**. O objetivo é que o AutoML consiga uma performance **melhor do que um humano** conseguiria ajustando à mão.

---

## 10.3. Onde o AutoML Atua no Processo de ML

> [!example] O processo de ML
> ```
> Problema → Fontes de → Pré-       → Treinamento → Teste do  → Implantação
>            Dados        processamento  do Modelo    Modelo
>                          └──────────── 80% do esforço ──────┘
> ```
> O **treinamento e ajuste do modelo** consomem cerca de **80%** do esforço. É aí que o AutoML mais ajuda.

---

## 10.4. Ótimo Local vs. Ótimo Global

> [!note] Um conceito-chave do treinamento
> Durante o treino, o modelo busca a melhor configuração. Mas há um risco:
> - **Ótimo Local** → uma solução "boa", mas não a melhor possível.
> - **Ótimo Global** → a **melhor solução** que existe.

```
   Performance
        │     ╱╲              ╱╲
        │    ╱  ╲    ╱╲      ╱  ╲
        │   ╱    ╲  ╱  ╲    ╱    ╲
        │  ╱      ╲╱    ╲  ╱      ╲
        │ ╱   ótimo     ╲╱  ótimo  ╲
        │      LOCAL         GLOBAL
        └──────────────────────────────▶
```

> [!warning] O perigo
> O treinamento pode "ficar preso" num **ótimo local**, achando que terminou — quando na verdade existe uma solução bem melhor (o **ótimo global**) em outro lugar. Boas estratégias de busca tentam **escapar** de ótimos locais.

> [!example] Por que isso importa (exemplo do curso)
> Num sistema de detecção de fraude em varejo (10 mil transações/dia), melhorar os Falsos Positivos em apenas **0,5%** pode significar reduzir as perdas de **R$ 450 mil/mês para R$ 300 mil/mês**. Sair de um ótimo local para o global vale **muito dinheiro**.

---

## 10.5. Parâmetros vs. Hiperparâmetros

> [!important] A diferença fundamental
>
> | | **Parâmetros** | **Hiperparâmetros** |
> |---|---|---|
> | Quem configura | O **próprio algoritmo**, durante o treino | O **implementador** (cientista de dados), **antes** do treino |
> | Quando | Durante o aprendizado | Antes do aprendizado |
> | Exemplo | Pesos de uma rede neural, probabilidades de uma Rede Bayesiana | Taxa de aprendizado, número de épocas, batch size |

> [!example] Analogia
> Pense em assar um bolo:
> - **Hiperparâmetros** = temperatura do forno e tempo (você define **antes**).
> - **Parâmetros** = como a massa cresce e doura (acontece **durante**, sozinho).

### Dois tipos de hiperparâmetros

> [!note] Hiperparâmetros de Modelo vs. de Algoritmo
> - **Hiperparâmetros de Modelo** → **interferem na performance** do modelo final.
> - **Hiperparâmetros de Algoritmo** → **não interferem na performance** do modelo, mas no **processo de aprendizado** (ex: velocidade do treino).

### Domínios dos hiperparâmetros

> [!info] Tipos de valor que um hiperparâmetro pode ter
> - **Inteiros** → ex: número de épocas (epochs).
> - **Valores Reais** → ex: taxa de aprendizado (learning rate).
> - **Binários** → ex: normalizar atributos? (sim/não).
> - **Categóricos** → ex: qual estimador usar.

### Hiperparâmetros condicionais

> [!note] Hiperparâmetros condicionais
> Às vezes a escolha de um hiperparâmetro **depende ou invalida outro**. Ex: um método de busca depende de qual avaliador de atributo foi escolhido. Isso cria um **grafo de dependências** entre os hiperparâmetros.

> [!important] Conclusão sobre hiperparâmetros
> A definição **ótima dos hiperparâmetros é vital** para a performance do modelo. Mas surgem duas perguntas difíceis:
> - **Quais valores escolher** para os hiperparâmetros?
> - Será que o **classificador que estou usando é o melhor**?
>
> Existem boas práticas e valores *default*, mas o número de configurações é **gigante** e o custo computacional **altíssimo**.

---

## 10.6. O Problema da Explosão Combinatória

> [!danger] Um exemplo assustador
> Imagine testar 3 classificadores (A, B, C), cada um com vários hiperparâmetros e seus possíveis valores. O número de combinações para testar **todas as opções**:
>
> $$(10 \times 20 \times 100) + (100 \times 5) + (10 \times 2 \times 1000 \times 20 \times 3)$$
> $$= 1.220.500 \text{ treinos diferentes}$$
>
> Supondo **1 minuto** por treino... daria **2,3 anos** de processamento! 😱

> [!important] A lição
> Testar **todas** as combinações (força bruta) é **inviável**. O AutoML existe para buscar de forma **inteligente** — encontrar boas configurações sem testar tudo.

---

## 10.7. Os 3 Componentes de uma Técnica de AutoML

> [!note] Toda técnica de AutoML deve conter
> 1. **Espaço de busca** — o conjunto de todas as configurações possíveis.
> 2. **Estratégia de busca** — como explorar esse espaço de forma eficiente.
> 3. **Medida de performance** — como avaliar se está melhorando.

### Componente 1: Espaço de Busca

> [!note] O que é
> O **espaço de busca** é o universo de todas as combinações de classificadores + hiperparâmetros. Pode ser **reduzido** — por exemplo, limitando faixas de valores — para ficar mais gerenciável (no exemplo do curso, de 1.220.500 para 120.050 combinações).

### Componente 2: Estratégia de Busca

O AutoML busca **otimizar** a procura pela melhor combinação. As estratégias:

#### Grid Search

> [!note] Grid Search (Busca em Grade)
> Especifica um **subconjunto de valores** para cada hiperparâmetro e testa **TODAS as combinações** desse subconjunto.

> [!tip] Característica
> Completo dentro do grid definido, mas pode ser lento se o grid for grande.

#### Random Search

> [!note] Random Search (Busca Aleatória)
> Especifica um subconjunto de valores, mas testa apenas **algumas combinações aleatórias**, até um **limite de tempo**.

> [!tip] Grid vs. Random
> O Random Search costuma ser **mais eficiente** que o Grid Search: explorando aleatoriamente, ele frequentemente acha boas configurações **mais rápido**, sem precisar testar tudo.

#### Otimizador Bayesiano

> [!note] Otimizador Bayesiano
> Está **entre os melhores** modelos de otimização. Características:
> - É **iterativo**.
> - Usa um **modelo substituto**, que tem custo menor de otimização.
> - **Avalia os resultados** dos modelos já testados **antes de escolher** os próximos hiperparâmetros.

> [!tip] A sacada do Otimizador Bayesiano
> Diferente do Grid/Random (que testam "às cegas"), o Otimizador Bayesiano **aprende com os testes anteriores** — usa o que já descobriu para escolher de forma esperta o que testar a seguir.

#### Algoritmos Genéticos

> [!note] Algoritmos Genéticos
> Inspirados na **evolução natural**:
> - **Gerações** de hiperparâmetros são testadas.
> - Depois do treino, passam por **elitismo**, **mutação** e **crossover**.
> - Novas gerações tendem a ter **melhor performance**.

> [!info] Os operadores genéticos
> - **Elitismo** → as melhores configurações "sobrevivem" para a próxima geração.
> - **Crossover** → combina características de duas boas configurações.
> - **Mutação** → introduz pequenas mudanças aleatórias (explora novas possibilidades).

#### CMA-ES

> [!note] CMA-ES
> **Covariance Matrix Adaptation Evolution Strategy** — outra estratégia evolutiva avançada de otimização.

### Componente 3: Medida de Performance

> [!note] Como saber se está melhorando
> Usa-se uma **métrica de performance** do modelo, por exemplo: **MPE**, **RMSE**, **MSE**.

> [!tip] Conexão
> Essas são as métricas de erro para regressão vistas em [[06 - Avaliação de Performance para Regressão]] (módulo Fundamentos).

---

## 10.8. Multi-Fidelity: Acelerando a Busca

> [!note] A ideia do Multi-Fidelity
> Em vez de avaliar **cada configuração** com todo o rigor (caro!), o Multi-Fidelity faz avaliações **mais baratas e aproximadas** primeiro, para descartar rapidamente as ruins.

> [!info] Formas de "baratear" a avaliação (Multi-Fidelity)
> - **Usar subconjunto de partições** — em vez de validação cruzada completa, usar só algumas partições.
> - **Parte dos dados** — treinar com um subconjunto dos dados (ou dados simplificados, como imagens menores).
> - **Poucas iterações** — treinar com poucas epochs.
> - **Poucos atributos** — treinar com um subconjunto de atributos.
> - **Testar o domínio de apenas um hiperparâmetro** por vez.

> [!tip] A lógica
> Se uma configuração já vai mal com "meio treino", provavelmente vai mal com o treino completo. Multi-Fidelity **elimina os fracos cedo**, gastando o tempo caro só nos candidatos promissores.

---

## 10.9. Curva de Aprendizado

> [!note] Estratégia da Curva de Aprendizado
> Em vez de testar todos os hiperparâmetros até o fim:
> - O treino vai até um **limite de tempo/aprendizado** e **congela**.
> - Depois, decide-se por **quais configurações continuar** (as mais promissoras).

> [!info] Técnicas relacionadas
> - **Freeze-Thaw Bayesian Configuration** — "congela e descongela" configurações conforme a curva de aprendizado.
> - **Hyper Band** — seleciona configurações aleatórias e elimina as ruins progressivamente.
> - **BOHB** — *Bayesian Optimization and Hyper Band* — combina o Otimizador Bayesiano com o Hyper Band.

```
   Loss
   1 ┤●
     │ ●●
     │   ●●●  ← configuração ruim (descartar cedo)
     │      ●●●●●●
     │ ●
     │  ●●
     │    ●●●  ← configuração promissora (continuar)
   0 ┤        ●●●●●
     └──────────────────▶ Tempo
```

---

## 10.10. Exemplo em Python (notebook do curso)

O notebook `AutoML.ipynb` compara **vários classificadores** automaticamente no dataset de câncer de mama:

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (RandomForestClassifier,
                              GradientBoostingClassifier, AdaBoostClassifier)
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Um "dicionário" de vários classificadores para comparar de uma vez
models = {
    'Logistic Regression': LogisticRegression(solver='liblinear', max_iter=10000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(gamma='scale'),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'Gradient Boosting': GradientBoostingClassifier(),
    'AdaBoost': AdaBoostClassifier()
}
# A ideia: treinar e avaliar TODOS automaticamente,
# e escolher o de melhor desempenho.
```

> [!tip] O que o código mostra
> Esse é o AutoML em sua forma mais simples: em vez de escolher **um** algoritmo na intuição, você define uma **lista de candidatos** e deixa o código testar **todos** — depois compara os resultados (idealmente com `cross_val_score`) e escolhe o vencedor por **evidência**.

---

## 10.11. Resumo

> [!summary] O essencial do AutoML e Tuning
> - **AutoML** = automatizar o ML **buscando melhor performance** que um humano.
> - **Parâmetros** = ajustados pelo algoritmo no treino. **Hiperparâmetros** = definidos por você, antes.
> - Testar todas as combinações é **inviável** (explosão combinatória — anos de processamento).
> - Uma técnica de AutoML tem: **espaço de busca**, **estratégia de busca**, **medida de performance**.
> - **Estratégias**: Grid Search (testa tudo do grid), Random Search (aleatório), Otimizador Bayesiano (aprende com testes anteriores), Algoritmos Genéticos (evolução), CMA-ES.
> - **Multi-Fidelity** = avaliações baratas e aproximadas para descartar os fracos cedo.
> - **Curva de Aprendizado** (Hyper Band, BOHB) = congela e continua só os promissores.

---

## 🎓 Você terminou o módulo de Tópicos Avançados!

Parabéns! 🎉 Você completou a jornada pelos Tópicos Avançados de Machine Learning:

| Área | Tópicos |
|---|---|
| **Preparar dados** | Engenharia de Atributos, PCA, Seleção de Atributos |
| **Avaliar com rigor** | Variabilidade, Teste de Hipótese, Custo |
| **Casos especiais** | Clusters avançados, Multilabel, Desbalanceamento |
| **Automatizar** | AutoML e Tuning |

> [!tip] Você concluiu os 4 módulos!
> Com [[00 - Índice|Fundamentos]], [[00 - Índice|Algoritmos]] e este de Tópicos Avançados, você tem uma base sólida e profissional de Machine Learning. Os próximos passos naturais seriam **Deep Learning**, **NLP**, **MLOps** e projetos práticos de ponta a ponta.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
