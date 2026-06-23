---
tags:
  - machine-learning
  - nlp
  - word-embedding
  - transformers
  - vetores
---

# 3. Word Embeddings e Transformers

> [!info] O que esta nota cobre
> Como transformar **palavras em vetores de números** (word embeddings) que capturam significado, as propriedades de **similaridade** e **analogia**, e a arquitetura **Transformer** que revolucionou o NLP.

---

## 3.1. O que é Word Embedding

> [!note] Definição
> **Word Embedding** = palavras ou frases do vocabulário são **mapeadas para vetores de números reais**. Cada palavra vira uma lista de números (dimensões).

> [!example] Palavras viram coordenadas
> | Word | Dim 1 | Dim 2 | Dim 3 |
> |---|---|---|---|
> | Cat | 0.10 | 0.30 | 0.70 |
> | Dog | 0.15 | 0.35 | 0.68 |
> | Mouse | 0.90 | 0.05 | 0.20 |
> | Cheese | 0.85 | 0.05 | 0.22 |
> | Jump | 0.45 | 0.80 | 0.30 |
> | Run | 0.47 | 0.82 | 0.33 |
>
> Repare: "Cat" e "Dog" têm vetores **parecidos** (são animais de estimação). "Mouse" e "Cheese" também (associação rato-queijo). O embedding **aprende** essas relações a partir de muito texto.

---

## 3.2. Independentes vs. Dependentes de contexto

> [!important] Uma evolução importante
> | Tipo | A palavra tem... | Exemplos |
> |---|---|---|
> | **Independentes de contexto** | **um vetor fixo**, não importa a frase | **Word2Vec**, **GloVe** |
> | **Dependentes de contexto** | **vetores diferentes** conforme o uso | **ELMo**, **BERT**, **GPT** |

> [!example] Por que contexto muda tudo
> A palavra "**banco**" em "sentei no banco" e "fui ao banco" tem o **mesmo** vetor no Word2Vec, mas **vetores diferentes** no BERT — que entende pelo contexto se é assento ou instituição. Por isso os modelos contextuais são muito mais poderosos.

---

## 3.3. Propriedades dos embeddings

### Similaridade
> [!note]
> Palavras de significado próximo têm vetores próximos. Mede-se isso com a **similaridade de cosseno**:
>
> | | Gato | Cachorro | Muro |
> |---|---|---|---|
> | **Gato** | 1,0 | 0,9 | 0,5 |
> | **Cachorro** | 0,9 | 1,0 | 0,7 |
> | **Muro** | 0,5 | 0,7 | 1,0 |
>
> Gato↔Cachorro = 0,9 (muito similar); Gato↔Muro = 0,5 (pouco).

### Analogia
> [!example] A mágica do "rei − homem + mulher = rainha"
> Os embeddings capturam relações que funcionam como **aritmética vetorial**:
> | Word | Dim1 | Dim2 | Dim3 |
> |---|---|---|---|
> | King | 0.6 | 0.8 | 0.4 |
> | Queen | 0.4 | 0.8 | 0.4 |
> | Man | 0.6 | 0.7 | 0.5 |
> | Woman | 0.4 | 0.7 | 0.5 |
>
> A diferença King→Queen é a mesma de Man→Woman. Isso permite resolver analogias por vetores.

### Três tipos de propriedade capturada
> [!summary]
> - **Semânticas:** o vetor de "Gato" é parecido com o de "Cachorro" (significado).
> - **Sintáticas:** função gramatical (substantivo vs. verbo).
> - **Distributivas:** palavras que aparecem em **contextos semelhantes** ficam próximas.

---

## 3.4. Transformers

> [!note] Definição
> **Transformers** são uma **arquitetura de rede neural** desenvolvida para NLP, baseada em mecanismos de **self-attention** (auto-atenção).

> [!important] O segredo: self-attention
> O mecanismo de **atenção** permite ao modelo **pesar a importância de cada palavra em relação às outras** da frase, ao mesmo tempo. É isso que o torna **ótimo em tarefas de contexto** — ele "presta atenção" nas palavras relevantes, mesmo distantes.

> [!example] Como se conecta com embeddings
> Os Transformers **podem usar word embeddings como entrada**. O fluxo: texto → embeddings (vetores) → Transformer (com self-attention) → saída (tradução, classificação, geração…).

> [!tip] Por que isso é um divisor de águas
> A arquitetura Transformer (do paper "Attention Is All You Need", 2017) é a base de **todos** os grandes modelos modernos — GPT, BERT, T5. Sem ela, não existiriam os LLMs da próxima nota.

---

## 3.5. Resumo

> [!summary] O essencial
> - **Word Embedding** = palavra → **vetor de números** que captura significado.
> - **Independentes de contexto** (Word2Vec, GloVe) = vetor fixo; **dependentes** (BERT, GPT) = vetor muda com a frase.
> - Embeddings capturam **similaridade** (cosseno) e **analogia** (aritmética vetorial).
> - **Transformers** usam **self-attention** para pesar a importância das palavras; base dos LLMs.

---

## 🔗 Próximos passos
- [[04 - LLMs (Large Language Models)]] — os gigantes construídos sobre Transformers.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
