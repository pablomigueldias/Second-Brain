---
tags:
  - machine-learning
  - agrupamento
  - clustering
  - não-supervisionado
  - k-means
  - dbscan
---

# 9. Agrupamentos (Clustering)

> [!info] O que esta nota cobre
> A tarefa de **agrupamento** (clustering): o que é, suas aplicações, os **tipos** de agrupamento (completo, parcial, difuso, hierárquico), e os principais algoritmos: **K-means**, **K-medoid**, **DBSCAN** e **Agrupamento Hierárquico** (aglomerativo e divisivo).

---

## 9.1. Conceitos Fundamentais

> [!note] Definição
> **Agrupamento** é uma tarefa **não supervisionada** que **cria grupos a partir dos atributos** (características) das instâncias.

### Características principais

- ✅ É **não supervisionado** → **não existe classe** previamente definida.
- ✅ Objetivo: **encontrar grupos** de instâncias **similares**.
- ✅ O algoritmo descobre **sozinho** quantos grupos fazem sentido (alguns descobrem, em outros nós dizemos quantos).

### Exemplo: agrupamento de pessoas

| Age | Income | Gender | Education | **Cluster (descoberto)** |
|---|---|---|---|---|
| 32 | 50000 | Male | Bachelor's | 1 |
| 45 | 70000 | Female | Master's | 0 |
| 22 | 25000 | Male | High School | 2 |
| 38 | 80000 | Male | Doctorate | 0 |
| 28 | 40000 | Female | Bachelor's | 1 |
| 52 | 100000 | Female | Bachelor's | 0 |
| 26 | 35000 | Male | Associate's | 2 |
| 44 | 90000 | Female | Master's | 0 |
| 31 | 55000 | Male | Bachelor's | 1 |
| 39 | 75000 | Male | Master's | 0 |

> A coluna `Cluster` **não veio nos dados**. Foi descoberta pelo algoritmo, que percebeu padrões e juntou quem parecia parecido (ex.: cluster 0 parece reunir profissionais com renda maior e formação avançada).

---

## 9.2. Aplicações de Agrupamento

> [!example] Onde usamos clustering
> - **Segmentação de clientes** → dividir clientes em diferentes perfis de consumo/marketing.
> - **Análise de redes sociais** → reconhecer **comunidades** (grupos de usuários conectados entre si).
> - **Segmentação de imagens** → dividir uma imagem em regiões parecidas (separar objeto do fundo).
> - **Detecção de anomalias** → identificar pontos que não pertencem a nenhum grupo.
> - **Combate ao crime** → identificar **regiões com maior incidência** criminal.

---

## 9.3. Tipos de Agrupamento

### 9.3.1. Agrupamento Completo

> [!note] Definição
> **Cada elemento** é adicionado em **um único grupo** — todos pertencem, e cada um a apenas um lugar.

```
         Grupo A              Grupo B
       ┌────────────┐      ┌────────────┐
       │  • • • •   │      │  • • • •   │
       │   • • •    │      │    • •     │
       └────────────┘      └────────────┘
```

> [!example] Exemplo
> Dividir clientes em **exatamente um** segmento (não podem ser de dois ao mesmo tempo).

---

### 9.3.2. Agrupamento Parcial

> [!note] Definição
> **Cada instância pode pertencer a mais de um grupo** — os grupos podem se **sobrepor**.

```
       Grupo A           Grupo B
    ┌────────┐
    │        ├──┐    ┌──┐
    │   ● ●  │  │    │  │
    │       ●│●●│●●●●│  │
    │   ●    │  │    │  │
    └────────┘──┘    └──┘
        ↑ Sobreposição: elementos no meio
          pertencem aos dois grupos
```

> [!example] Exemplo
> Filmes podem pertencer a "Ação" e "Comédia" ao mesmo tempo.

---

### 9.3.3. Modelo Difuso (Fuzzy)

> [!note] Definição
> Cada elemento pertence a **cada grupo segundo uma probabilidade** (ou grau de pertinência). A soma das probabilidades para cada elemento deve dar 1.

| Elemento | Grupo A | Grupo B | Grupo C |
|---|---|---|---|
| **Elemento A** | 0,5 | 0,3 | 0,2 |
| **Elemento B** | 0,1 | 0,1 | 0,8 |
| **Elemento C** | 0,3 | 0,4 | 0,3 |

> [!example] Interpretação
> - **Elemento A** "pertence" 50% ao grupo A, 30% ao B e 20% ao C.
> - **Elemento B** pertence claramente ao grupo C (80%).
> - **Elemento C** é mais ambíguo, dividido entre os três.

---

### 9.3.4. Modelo Hierárquico

> [!note] Definição
> Permite que **um grupo tenha subgrupos**. Os grupos formam uma **árvore**.

```
                  Todos
                /   |   \
           Grupo1 Grupo2 Grupo3
            / \           |
         Sub Sub        Sub  ...
```

> [!example] Exemplo
> Em uma loja: o grupo "Eletrônicos" pode ter subgrupos "Celulares", "Notebooks" e "Acessórios"; "Celulares" pode ter subgrupos "Android" e "iPhone"; etc.

---

### 9.3.5. Agrupamento com ou sem Ruído

#### Agrupa todos os elementos (sem ruído)
```
         Grupo A    Grupo B    Grupo C
        [● ● ●]    [● ● ●]    [● ● ●]
```

#### Pode deixar elementos sem agrupar (com ruído)
```
         Grupo A    Grupo B    Grupo C
        [● ● ●]    [● ● ●]    [● ● ●]

         ● ←─── ponto isolado, classificado como RUÍDO
```

> [!tip] Por que isso é útil?
> Em dados reais, há pontos **estranhos**, **anomalias**, ou simplesmente que **não se encaixam em nenhum grupo natural**. Forçar todos a entrarem em algum grupo distorce a análise. Métodos como **DBSCAN** (veja abaixo) permitem deixar ruído de fora.

---

## 9.4. Algoritmos Principais

### 9.4.1. K-means e K-medoid

> [!note] Características gerais
> - **Simples** e amplamente usados.
> - **Baseados em protótipo** — cada grupo é representado por um "ponto central".
> - **Encontram um número de grupos definido pelo usuário** (você diz: "quero 3 grupos").
> - **Agrupam todos os objetos** (não há ruído).
> - **Definir os centróides** (pontos centrais) é a etapa fundamental.
> - Usam **Distância Euclidiana** para medir similaridade.

#### Diferença entre K-means e K-medoid

| Aspecto | **K-means** | **K-medoid** |
|---|---|---|
| Protótipo | **Centróide**: média de um grupo de pontos | **Medóide**: ponto mais representativo |
| O protótipo é um ponto real? | ❌ Quase nunca (é um valor calculado) | ✅ Sim (é um dos próprios pontos dos dados) |
| Sensibilidade a outliers | Mais sensível (média é puxada por extremos) | Menos sensível |

> [!example] Analogia
> Imagine medir o "típico" de um grupo de pessoas:
> - **K-means**: tira a média da altura, peso, idade — você obtém uma "pessoa imaginária".
> - **K-medoid**: escolhe **a pessoa mais representativa** do grupo — uma pessoa real.

#### Limitações do K-means e K-medoid

> [!warning] Onde falham
> - Têm dificuldade para detectar **grupos naturais não esféricos**.
> - Têm dificuldade com grupos de **tamanho** ou **densidades muito diferentes**.
> - Restritos a dados onde existe uma **noção de centro** (não funciona bem com dados categóricos puros).
> - O resultado depende muito da **escolha inicial dos centros** — pode ser melhorado escolhendo bem (ex.: K-means++).

---

### 9.4.2. DBSCAN

> [!note] Definição
> **DBSCAN** = *Density-Based Spatial Clustering of Applications with Noise*. Como o nome diz, é **baseado em densidade** — agrupa pontos que estão **próximos uns dos outros**.

#### Características do DBSCAN

- ✅ **Baseado em densidade** (não em centróides).
- ✅ **Menos afetado por ruído** que K-means.
- ✅ **Número de grupos definido automaticamente** — você não precisa dizer quantos!
- ✅ **Pontos de baixa densidade** são definidos como **ruído** e **não agrupados**.
- ✅ A densidade é baseada num **raio especificado**. Um ponto pode estar:
  - **No interior** do grupo (muitos vizinhos próximos),
  - **No limite** (poucos vizinhos),
  - **Sem classificação (ruído)** (vizinhos insuficientes).
- ⚠️ **Não é bom** quando os grupos têm **densidades muito diferentes**.

#### Conceito visual

```
   Cluster 1            Cluster 2          Ruído
   ●●●●●●●              ●●●●●               ●
   ●●●●●●●●●●           ●●●●●●●●
   ●●●●●●●●             ●●●●●●
   ●●●●●●               ●●●

                                     ●  ←── ponto isolado:
                                          DBSCAN marca como ruído
```

> [!tip] Quando usar DBSCAN
> - Quando você **não sabe** quantos grupos existem.
> - Quando os grupos podem ter **formas estranhas** (não-esféricas).
> - Quando há **muitas anomalias/outliers** que precisam ser identificadas.

---

### 9.4.3. Agrupamento Hierárquico

> [!note] Definição
> Constrói uma **hierarquia de grupos** — uma árvore que mostra como os pontos se agrupam progressivamente.

Há duas abordagens opostas:

#### Aglomerativa (bottom-up) — **mais comum**

> Começa com **cada ponto sendo seu próprio grupo**. A cada etapa, **funde os pares mais próximos**. Requer uma **noção de proximidade** (distância). Continua até sobrar um único grupo grande contendo todos.

```
   Início: cada ponto é um grupo
   ●  ●  ●  ●  ●  ●  ●  ●
   │  │  │  │  │  │  │  │
   └─ ┘  └─ ┘  └─ ┘  └─ ┘     ← pares mais próximos se fundem
   │     │     │     │
   └─────┘     └─────┘        ← grupos se fundem
   │           │
   └───────────┘              ← último merge
         │
         ●                    ← tudo num grupo só
```

#### Divisiva (top-down)

> Começa com **todos os pontos em um único grupo**. A cada etapa, **divide** até que reste apenas grupos únicos (cada ponto sozinho).

```
   Início: tudo junto
         ●
         │
   ┌─────┴─────┐              ← divide
   │           │
   ┌─────┐     ┌─────┐        ← divide cada metade
   │     │     │     │
   ┌─ ┐  ┌─ ┐  ┌─ ┐  ┌─ ┐     ← continua...
   │  │  │  │  │  │  │  │
   ●  ●  ●  ●  ●  ●  ●  ●     ← cada ponto sozinho
```

#### Dendograma

> [!note] O que é um dendograma
> É o **gráfico em forma de árvore** que mostra como os grupos foram formados (na aglomerativa) ou divididos (na divisiva). A **altura** dos ramos indica **quão similares** os grupos eram quando se uniram.

```
   Altura
   │     ┌─────────────┐
   │     │             │
   │   ┌─┴─┐         ┌─┴─┐
   │  ┌┴┐  │        ┌┴┐  │
   │  │ │  │        │ │  │
   │  A B  C        D E  F
   │
   └─────────────────────────▶
            Pontos
```

> [!tip] Vantagens do hierárquico
> - **Não exige número de clusters** definido a priori — você decide olhando o dendograma.
> - Mostra a **relação entre os grupos** (quais são mais parecidos entre si).
> - Bom para **explorar** os dados.

---

## 9.5. Tabela-Resumo dos Algoritmos

| Algoritmo | Você diz quantos grupos? | Lida com ruído? | Formas não-esféricas? | Densidades variadas? |
|---|---|---|---|---|
| **K-means** | ✅ Sim (k) | ❌ Não | ❌ Difícil | ❌ Difícil |
| **K-medoid** | ✅ Sim (k) | ❌ Não | ❌ Difícil | ❌ Difícil |
| **DBSCAN** | ❌ Não (descobre) | ✅ Sim | ✅ Sim | ❌ Difícil |
| **Hierárquico** | ❌ Não (você escolhe no dendograma) | Depende | Depende | Depende |

---

## 9.6. Como Escolher?

```
   Você sabe quantos grupos quer?
                │
            ┌───┴───┐
           SIM     NÃO
            │       │
            ▼       ▼
       K-means    Há muito ruído ou grupos
       (ou K-     com formas estranhas?
        medoid)        │
                  ┌────┴────┐
                 SIM       NÃO
                  │         │
                  ▼         ▼
                DBSCAN   Hierárquico
                         (Aglomerativo)
```

---

## 9.7. Resumo

> [!summary] O essencial sobre agrupamento
> - **Aprendizado não supervisionado** (sem rótulos).
> - **Tipos**: completo, parcial, difuso, hierárquico.
> - **Pode** ou **não** ter ruído (depende do método).
> - **K-means** = simples, rápido, mas rígido (precisa de k, esférico, sem ruído).
> - **DBSCAN** = baseado em densidade, lida com ruído, formas livres.
> - **Hierárquico** = constrói uma árvore (dendograma).

---

## 🔗 Próximos passos
- [[10 - Regras de Associação]] — o último tópico: descobrir relações como "quem compra X também compra Y".

---
[[00 - Índice|⬅️ Voltar ao Índice]]
