---
tags:
  - machine-learning
  - algoritmos-genéticos
  - crossover
  - mutação
  - elitismo
---

# 2. Como Funciona

> [!info] O que esta nota cobre
> A mecânica de um algoritmo genético: **cromossomo, gene e população**, **codificação**, **recombinação (crossover)**, métodos de **seleção** (roleta e classificação), **mutação**, **elitismo** e **fitness**.

---

## 2.1. Cromossomo, Gene e População

> [!note] Os blocos básicos
> - **Cromossomo:** uma **solução proposta** para o problema.
> - **População:** o **conjunto de cromossomos** (várias propostas de solução).
> - **Gene:** cada cromossomo é composto por **genes** — que podem ser valores **binários, numéricos, texto…**, dependendo do problema.

```
              Genes
          ┌───┬───┬───┬───┬───┐
   Crom.1 │ A │ B │ C │ D │ E │
   Crom.2 │ C │ B │ D │ E │ A │   ← População
   Crom.3 │ B │ A │ D │ C │ E │
          └───┴───┴───┴───┴───┘
```

> [!warning] Tamanho da população importa
> A população **não deve ser nem muito pequena** (pouca diversidade, fica presa) **nem muito grande** (aumenta o processamento sem melhorar a solução). É um equilíbrio.

---

## 2.2. Codificação

> [!note] Como representar os genes
> A **codificação** define a estrutura dos genes do cromossomo, conforme o problema:
> | Tipo | Quando usar | Exemplo |
> |---|---|---|
> | **Binária** | escolhas sim/não | o que levar na **mochila** (1 = leva, 0 = não) |
> | **Permutação** | ordenar coisas | **caixeiro viajante** (ordem das cidades) |
> | **Valores** | parâmetros numéricos | resolver uma **equação matemática** |

---

## 2.3. Recombinação (Crossover)

> [!note] O que é
> **Crossover** = combinar genes de **dois cromossomos** (pais) para produzir **descendentes** (nova geração). O objetivo é gerar filhos **melhores** misturando boas características.

> [!important] Como acontece
> - A combinação ocorre segundo uma **probabilidade** (ex.: 0,5 ou 0,7).
> - Os pais são selecionados **com reposição** (podem ser escolhidos várias vezes).
> - Os **pontos de cruzamento** são escolhidos **aleatoriamente**.

### Tipos de crossover
> [!example]
> - **Ponto único:** corta os pais em **um** ponto e troca as metades.
>   ```
>   Pai 1:  A B | C D E        Filho 1: A B | c d e
>   Pai 2:  a b | c d e   →    Filho 2: a b | C D E
>   ```
> - **Dois pontos:** corta em **dois** pontos e troca o miolo.

---

## 2.4. Seleção: quem se reproduz?

> [!note] Dois métodos principais

### Seleção por Roleta (Roulette Wheel)
> [!note]
> Cromossomos **mais bem adaptados** (maior fitness) têm **mais chance** de seleção, e são escolhidos mais vezes.
> - **Desvantagem:** cromossomos de **baixa** adaptação têm chances **quase nulas** → perde-se diversidade.
> ```
>   Roleta (área ∝ fitness):
>   ┌─────────┬───┬──┐
>   │  Crom B │ A │C │   ← B (fitness alto) ocupa mais espaço
>   └─────────┴───┴──┘
> ```

### Seleção por Classificação (Rank)
> [!note]
> Ordena os cromossomos: o **pior** recebe rank 1, o segundo pior rank 2, e assim por diante. A chance de seleção depende do **rank**, não do valor bruto do fitness.
> - **Vantagem:** **balanceia** as chances — mesmo os de fitness baixo têm uma chance razoável, preservando diversidade.

---

## 2.5. Mutação

> [!note] O que é
> Cada **gene** pode ser **modificado aleatoriamente** segundo uma probabilidade. Normalmente essa probabilidade é **muito baixa** (ex.: **0,01** ou **0,001**).

> [!important] Por que existe
> A mutação injeta **diversidade nova** na população — características que não estavam em nenhum pai. Sem ela, a população poderia **estagnar** e ficar presa numa solução mediana. É a "fagulha" da inovação.

---

## 2.6. Elitismo

> [!note] O que é
> Para **não perder os melhores cromossomos**, uma **cópia deles** é mantida **sem alterações** (sem crossover nem mutação) e passada direto para a próxima geração.

> [!tip] Por que importa
> Garante que a qualidade **nunca regrida**: a melhor solução de uma geração está garantida na próxima. Protege o progresso já conquistado.

---

## 2.7. Fitness, Espaço de Soluções e Descendentes

> [!note] Adaptação (Fitness) — como medir
> - Na natureza, a adaptação é medida pelo **ambiente**.
> - No GA, cada indivíduo recebe uma **"nota"** (fitness). Quanto **maior**, mais chance de permanecer e reproduzir. Notas baixas → mais chance de descarte.
> - Calcula-se via uma **função objetivo** (ex.: `F = Σ genes`).

> [!important] Espaço de Soluções
> - É o conjunto de **todas as soluções possíveis**.
> - Uma solução é medida pela sua **adaptação**.
> - ⚠️ **A melhor solução encontrada nem sempre é a solução ótima global** — GA é uma **heurística**.

> [!note] Descendentes (a nova geração)
> Através de **crossover + mutação + elitismo**, gera-se uma nova geração. A geração anterior é **completamente substituída**, e a nova mantém o **mesmo tamanho** de população.

---

## 2.8. Resumo

> [!summary] O essencial
> - **Cromossomo** = solução; **gene** = parte da solução; **população** = conjunto de soluções.
> - **Codificação:** binária, permutação ou valores.
> - **Crossover** combina pais; **mutação** (prob. baixa) traz diversidade; **elitismo** preserva os melhores.
> - **Seleção:** roleta (proporcional ao fitness) ou classificação (por rank, mais balanceada).
> - GA é **heurística**: a melhor solução achada **pode não ser a ótima global**.

---

## 🔗 Próximos passos
- [[03 - Exemplos Práticos]] — vendo tudo isso rodar num exemplo numérico completo.

---
[[00 - Índice|⬅️ Voltar ao Índice]]
