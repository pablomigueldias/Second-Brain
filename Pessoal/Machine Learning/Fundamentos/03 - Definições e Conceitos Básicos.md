---
tags:
  - machine-learning
  - definições
  - conceitos
  - fundamentos
---

# 3. Definições e Conceitos Básicos

> [!info] Sobre esta nota
> Aqui está **o vocabulário** que você vai usar o tempo inteiro em ML. Sem isso, todo o resto fica confuso. Vamos do micro (cada célula da tabela de dados) até o macro (os tipos de tarefa de ML).

---

## 3.1. Estruturas de Dados em ML

Em Machine Learning, os dados quase sempre chegam em formato de **tabela** (linhas × colunas). Considere o exemplo abaixo, que vai aparecer várias vezes:

| Idade | Renda | Histórico de crédito | Valor do empréstimo | Classe |
|---|---|---|---|---|
| 25 | 3500 | bom | 10000 | aprovado |
| 30 | 4000 | bom | 15000 | aprovado |
| 35 | 4500 | ruim | 12000 | reprovado |
| 40 | 5000 | bom | 20000 | aprovado |
| 45 | 5500 | excelente | 25000 | aprovado |
| 50 | 6000 | bom | 18000 | aprovado |
| 55 | 6500 | ruim | 10000 | reprovado |
| 60 | 7000 | excelente | 30000 | aprovado |

Vamos dissecar cada parte dessa tabela.

---

### 3.1.1. Atributos (também chamados de Dimensões ou Características)

> [!note] Definição
> **Atributos** são as **colunas** da tabela — as **propriedades** que descrevem cada exemplo.

No exemplo acima, os atributos são:
- `Idade`
- `Renda`
- `Histórico de crédito`
- `Valor do empréstimo`
- `Classe`

> [!tip] Outros nomes para "atributo"
> Você vai encontrar todos esses sinônimos por aí:
> - **Atributo** (português, mais comum aqui)
> - **Dimensão**
> - **Característica** (em inglês: **feature**)
> - **Variável**
> - **Coluna**

---

### 3.1.2. Instâncias

> [!note] Definição
> Uma **instância** é uma **linha** da tabela — um **exemplo individual**, um caso específico do mundo real.

No nosso exemplo, **cada cliente é uma instância**. A primeira instância é:
> *"Pessoa de 25 anos, renda 3500, histórico bom, pediu 10.000, foi aprovada."*

> [!tip] Outros nomes para "instância"
> - **Registro**
> - **Exemplo**
> - **Linha**
> - **Observação**
> - **Amostra** (cuidado: "amostra" também pode significar um *subconjunto* de instâncias)

---

### 3.1.3. Classe

> [!note] Definição
> A **classe** é o atributo **especial** que indica **o que queremos prever** ou **descrever**. Por convenção, costuma ser **a última coluna** da tabela.

No exemplo:
- A coluna `Classe` mostra se o empréstimo foi **aprovado** ou **reprovado**.
- Esse é o **alvo** que queremos que o modelo aprenda a prever para clientes novos.

> [!tip] Outros nomes para "classe"
> - **Rótulo** (label)
> - **Variável alvo** / **target**
> - **Variável dependente** (em estatística)
> - **Saída** / **resposta**

> [!warning] Atenção
> **Nem toda tarefa de ML tem uma classe!** Quando temos uma classe (rótulo), o aprendizado é **supervisionado**. Quando não temos, é **não supervisionado** (mais sobre isso em [[03 - Definições e Conceitos Básicos#3.4. Aprendizado Supervisionado vs. Não Supervisionado|3.4]]).

---

### 3.1.4. Tipos de Dados

Os atributos podem ser de tipos diferentes, e isso afeta tudo: que algoritmo usar, como pré-processar, como avaliar.

#### Tipos numéricos
- **Numérico contínuo** — valores reais. Ex: `Renda = 4500,75`, `Altura = 1,73m`.
- **Numérico discreto** — valores inteiros, contáveis. Ex: `Idade = 35`, `Número de filhos = 2`.

#### Tipos categóricos
- **Categórico nominal** — categorias **sem ordem**. Ex: `Cor = vermelho, verde, azul`.
- **Categórico ordinal** — categorias **com ordem**. Ex: `Histórico de crédito = ruim < bom < excelente`.

> [!example] No nosso exemplo
> - `Idade`, `Renda`, `Valor do empréstimo` → numéricos.
> - `Histórico de crédito` → categórico **ordinal** (existe uma ordem natural: ruim < bom < excelente).
> - `Classe` → categórico **nominal** (aprovado / reprovado — não tem ordem).

> [!warning] Por que isso importa?
> Algoritmos de ML **só entendem números**. Se um atributo é categórico, ele precisa ser **convertido em número** antes de treinar o modelo. Esse processo é o tema de [[07 - Codificação de Categorias]].

---

## 3.2. Tarefas de Machine Learning

Toda aplicação de ML cai em uma destas **quatro tarefas principais** (já apresentadas no curso):

```
                    Tarefas Principais de ML
   ┌──────────────┬─────────────┬────────────────┬──────────────────┐
   │              │             │                │                  │
Classificação  Regressão   Agrupamentos   Regras de Associação
```

### Outras tarefas mencionadas

Além das quatro principais, ML também inclui:

- **Detecção de anomalias** — achar pontos fora do padrão.
- **Aprendizado por reforço** — aprender por tentativa e erro com recompensas.
- **Processamento de Linguagem Natural (NLP)** — entender texto/voz.
- **Redes neurais** — uma técnica que pode ser usada para várias tarefas.
- **Redução de dimensionalidade / Seleção de recursos** — diminuir o número de atributos.
- **Aprendizado semi-supervisionado** — só *parte* dos dados tem rótulo.

---

### 3.2.1. Classificação

> [!note] O que faz?
> **Classificação** = atribuir um **rótulo de classe** (categoria) a uma instância.

Há dois usos básicos:

**Descrição** (rotular o que já existe):
> Paciente com asma → classificar em: *intermitente*, *persistente leve*, *persistente moderada* ou *persistente grave*.

**Previsão** (rotular o futuro):
> Uma compra nova → prever se é *fraudulenta* ou *legítima*.

> [!tip] Sinal rápido
> Se a resposta é uma **palavra/categoria**, é classificação.

📖 Tópico completo em: [[04 - Classificação]]

---

### 3.2.2. Regressão

> [!note] O que faz?
> **Regressão** = prever um **valor numérico** (contínuo ou inteiro).

> [!example] Exemplo: preço de imóveis
>
> | Tamanho | Localização | Quartos | **Preço** |
> |---|---|---|---|
> | 120 m² | Central | 2 | **R$ 250.000** |
> | 150 m² | Norte | 3 | **R$ 350.000** |
> | 200 m² | Sul | 4 | **R$ 450.000** |
> | 90 m² | Leste | 1 | **R$ 150.000** |
>
> O modelo aprende a relação entre as características do imóvel e o preço, e consegue **prever o preço** de um imóvel novo.

> [!tip] Sinal rápido
> Se a resposta é um **número**, é regressão.

📖 Avaliação de regressão em: [[06 - Avaliação de Performance para Regressão]]

---

### 3.2.3. Agrupamento (Clustering)

> [!note] O que faz?
> **Agrupamento** = encontrar **grupos de instâncias parecidas**, sem ter um rótulo prévio.

> [!example] Exemplo: segmentação de clientes
>
> | Cliente | Idade | Renda | Compras Online | Preferência | **Segmento** |
> |---|---|---|---|---|---|
> | 1 | 32 | 3500 | Sim | Eletrônicos | Segmento 2 |
> | 2 | 45 | 4500 | Não | Roupas | Segmento 1 |
> | 3 | 28 | 2500 | Sim | Esportes | Segmento 2 |
> | 4 | 60 | 6500 | Não | Casa | Segmento 3 |
>
> O algoritmo **descobre sozinho** quais clientes têm comportamento parecido e os agrupa. Os "segmentos" não foram dados — foram descobertos.

> [!tip] Sinal rápido
> Se você **não tem rótulo** e quer **descobrir grupos**, é agrupamento.

📖 Tópico completo em: [[09 - Agrupamentos (Clustering)]]

---

### 3.2.4. Regras de Associação

> [!note] O que faz?
> **Regras de Associação** = encontrar relações frequentes entre itens. O clássico "quem compra X também compra Y".

> [!example] Exemplo: recomendação de produtos
>
> Cesta de compras dos clientes:
>
> | Cliente | Itens comprados |
> |---|---|
> | 1 | Camiseta, Calça, Boné, Óculos |
> | 2 | Calça, Boné, Óculos, Cinto |
> | 3 | Camiseta, Óculos, Cinto, Relógio |
> | 4 | Camiseta, Boné, Relógio, Tênis |
>
> O algoritmo descobre regras como: *"quem compra camiseta tende a comprar boné"*.

📖 Tópico completo em: [[10 - Regras de Associação]]

---

## 3.3. Tabela-Resumo das Tarefas

| Tarefa | O que faz | Exemplo |
|---|---|---|
| **Classificação** | Prevê uma **categoria** | E-mail é spam ou não? |
| **Regressão** | Prevê um **número** | Quanto custa essa casa? |
| **Agrupamento** | Descobre **grupos similares** | Que segmentos de clientes existem? |
| **Regras de Associação** | Encontra **itens que aparecem juntos** | Quem compra fralda compra cerveja? |

---

## 3.4. Aprendizado Supervisionado vs. Não Supervisionado

Esta é uma das **classificações mais importantes** em ML: o aprendizado é **supervisionado** ou **não supervisionado**?

### Aprendizado Supervisionado

> [!note] Definição
> Os dados de treino **já têm o rótulo** (a "resposta certa"). O algoritmo aprende olhando pares (entrada → resposta).

**Tarefas supervisionadas:**
- Classificação (rótulo = categoria)
- Regressão (rótulo = número)

> [!example] Analogia
> É como estudar com **gabarito**. Você vê o problema E a resposta certa, então aprende a relação entre eles.

### Aprendizado Não Supervisionado

> [!note] Definição
> Os dados **não têm rótulo**. O algoritmo tem que **descobrir sozinho** os padrões ou a estrutura.

**Tarefa principal não supervisionada:**
- Agrupamento

> [!example] Analogia
> É como receber uma pilha de fotos misturadas e ter que **organizar em álbuns** sem que ninguém tenha dito quantos álbuns nem o tema de cada um.

### Caso Híbrido: Regras de Associação

> [!warning] Atenção
> **Regras de Associação** pode ser **supervisionado ou não supervisionado** dependendo de como é aplicado. Normalmente é usada como **não supervisionada** (procurando padrões em transações), mas pode também ser direcionada por uma classe.

### Tabela-Resumo

| Tarefa | Descrição | Tipo de Aprendizado |
|---|---|---|
| **Classificação** | Atribui rótulos de classe a uma instância | Supervisionado |
| **Regressão** | Prevê um valor numérico/contínuo | Supervisionado |
| **Agrupamento** | Identifica grupos de instâncias similares | Não Supervisionado |
| **Regras de Associação** | Encontra relações frequentes entre itens | Supervisionado **ou** Não Supervisionado |

---

## 🔗 Próximos passos
- [[04 - Classificação]] — começamos a aprofundar nas tarefas, a partir de classificação.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
