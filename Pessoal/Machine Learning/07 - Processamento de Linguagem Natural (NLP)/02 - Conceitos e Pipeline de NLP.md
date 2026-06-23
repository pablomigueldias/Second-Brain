---
tags:
  - machine-learning
  - nlp
  - tokenização
  - pos-tagging
  - lematização
---

# 2. Conceitos e Pipeline de NLP

> [!info] O que esta nota cobre
> O **pipeline** clássico de pré-processamento em NLP: **corpus**, **annotations**, **tokenização**, **POS tagging**, **lematização** e **dependency parsing**. E o que é um **modelo** linguístico.

---

## 2.1. Corpus

> [!note] Definição
> **Corpus** = um **conjunto de dados em linguagem natural** (texto **não estruturado**). É a matéria-prima do NLP — os textos com os quais o modelo trabalha ou é treinado.

---

## 2.2. Annotations (o processo mais importante)

> [!important] Anotações são o coração do NLP
> **Annotations** = o processo de **colocar anotações no texto**: flexões, classes gramaticais, dependências entre palavras, etc. É a etapa que transforma texto cru em informação estruturada.

> [!example] Frase de exemplo do curso
> *"Nossa vida é controlada por algoritmos, disse artista e professor de artes digitais…"*
> Cada palavra recebe anotações como classe gramatical e relações de dependência (no formato CoNLL-U).

---

## 2.3. O Pipeline, passo a passo

Usando a frase **"Nossa vida é controlada por algoritmos,"**:

### Passo 1 — Tokenization
> [!note] Tokenização
> **Separar a sentença em suas partes**: palavras, pontos, símbolos.
> ```
> "Nossa vida é controlada por algoritmos,"
>    →  [Nossa] [vida] [é] [controlada] [por] [algoritmos] [,]
> ```
> Cada pedaço é um **token**.

### Passo 2 — Parts-of-Speech Tagging (POS)
> [!note] POS Tagging
> Adiciona a **classe gramatical** (tag) a cada token: se é verbo, substantivo, adjetivo, etc.
> ```
> Nossa     vida    é      controlada  por    algoritmos  ,
> PRON      NOUN    AUX    VERB        ADP    NOUN        PUNCT
> ```

> [!example] Tabela de tags POS (universais)
> | Tag | Significado | Exemplo |
> |---|---|---|
> | **PROPN** | Nome próprio | José, Maria |
> | **VERB** | Verbo | andar, dirigir |
> | **ADP** | Adposição (preposição) | de, em, durante |
> | **DET** | Determinante | a, aquela, muitas |
> | **NOUN** | Substantivo | casa, carro |
> | **PUNCT** | Pontuação | , . ; |
> | **ADJ** | Adjetivo | infeliz, brasileiro |
> | **CCONJ** | Conjunção coordenativa | e, mas, nem |
> | **SCONJ** | Conjunção subordinativa | embora, uma vez que |
> | **AUX** | Verbo auxiliar | ser, estar, ter |
> | **PRON** | Pronome | meu, minha, os quais |
> | **NUM** | Número | 10, vinte |
> | **ADV** | Advérbio | tarde, aqui, mal |
> | **INTJ** | Interjeição | ah, psiu, hum |

### Passo 3 — Lemmatizing (Lemma)
> [!note] Lematização
> Reduz a palavra à sua **forma de dicionário** (lema), para que variações possam ser analisadas juntas.
> ```
> Nossa → meu      controlada → controlar      algoritmos → algoritmo
> ```
> Assim "controlada", "controlando" e "controlar" são tratadas como **a mesma** palavra.

> [!tip] Lematização ≠ Stemming
> Lematização traz a forma **correta** do dicionário (controlar). O *stemming* só corta o final da palavra de forma bruta (control-), podendo gerar não-palavras. Lematização é mais precisa.

### Passo 4 — Dependency Parsing
> [!note] Análise de Dependências
> Encontra a **relação entre palavras "pais" e "filhos"** — quem depende de quem na estrutura da frase.
> ```
>              controlada (raiz)
>             /     |      \
>          vida     é    algoritmos
>           |               |
>         Nossa            por
> ```
> Mostra que "vida" é o sujeito de "controlada", "algoritmos" é o complemento via "por", etc.

---

## 2.4. O que é um "Modelo" em NLP

> [!important] Modelo = banco de dados linguístico
> Em NLP, o **modelo** que faz toda essa análise (verbo? substantivo? quais flexões? quais dependências?) é, na prática, um **banco de dados linguístico**:
> - É **específico de cada idioma** (um modelo para português, outro para inglês).
> - A maioria das plataformas de NLP **tem seus próprios modelos** (ou usam de terceiros).
> - **Você pode criar o seu!**

> [!example] Ferramentas do curso
> O curso usou **NLTK** e **spaCy** (bibliotecas de NLP em Python) para tokenizar, etiquetar POS e lematizar textos.

---

## 2.5. Resumo

> [!summary] O essencial do pipeline
> - **Corpus** = textos crus (não estruturados).
> - **Annotations** = anotar o texto (a etapa mais importante).
> - Pipeline: **Tokenização → POS Tagging → Lematização → Dependency Parsing**.
> - **POS** = classe gramatical; **Lema** = forma de dicionário; **Parsing** = relações entre palavras.
> - **Modelo** = banco de dados linguístico, **específico por idioma**.

---

## 🔗 Próximos passos
- [[03 - Word Embeddings e Transformers]] — depois de preparar o texto, como transformá-lo em **números** que capturam significado.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
