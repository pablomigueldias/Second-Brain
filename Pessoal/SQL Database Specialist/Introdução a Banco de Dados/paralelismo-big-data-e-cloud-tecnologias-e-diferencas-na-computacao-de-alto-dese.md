---
titulo: "Paralelismo, Big Data e Cloud: Tecnologias e Diferenças na Computação de Alto Desempenho"
tags: [conceitos, dados, banco-de-dados, sgbd, ferramentas, sistema, fundamentos]
data: 2026-09-16
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 4
conceitos: [Paralelismo, Big Data, Cloud Computing, High Performance Computing (HPC), AWS RDS, Processamento paralelo, Persistência de dados, SGBD distribuído]
---

# Paralelismo, Big Data e Cloud: Tecnologias e Diferenças na Computação de Alto Desempenho

> [!resumo] Do que se trata
> A nota explora o paralelismo, Big Data e Cloud como tecnologias cruciais para experimentos de larga escala. Ela define paralelismo como o processamento concorrente de dados sem dependências e Big Data como o processamento paralelo de dados persistentes e particionados. Além disso, a nota diferencia High Performance Computing (HPC) do Big Data, enfatizando a persistência dos dados como o principal fator distintivo.

## Para lembrar

- **Paralelismo é a capacidade de processar uma aplicação ou dados de maneira concorrente, sem sequência ou dependência entre as ações.**
- **Big Data está associado ao processamento paralelo de dados persistentes e particionados, diferente do paralelismo geral que é volátil.**
- **A Cloud disponibiliza recursos de terceiros, provendo tecnologias como serviço, como o AWS RDS para SGBDs.**
- **High Performance Computing (HPC) envolve nós de processamento paralelo onde as informações não são persistidas, apenas processadas.**
- **A principal diferença entre HPC e Big Data reside na persistência dos dados, além das ferramentas e modelos distintos que cada um utiliza.**

## O que esta nota responde

- Quais tecnologias são essenciais para experimentos de larga escala?
- Qual a diferença fundamental entre High Performance Computing (HPC) e Big Data?
- Como a Cloud Computing facilita o uso de SGBDs em larga escala?

## Conceitos

**Paralelismo** · **Big Data** · **Cloud Computing** · **High Performance Computing (HPC)** · **AWS RDS** · **Processamento paralelo** · **Persistência de dados** · **SGBD distribuído**

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Paralelismo** | É a capacidade de processar uma aplicação ou dados de maneira paralela. Não há uma sequência ou dependência entre as ações a serem executadas em diferentes momentos; um conjunto de operações pode ser executado em paralelo em diferentes clusters. Múltiplos processadores operam concorrentemente, de maneira concomitante, para atingir o mesmo objetivo. |
| **Big Data** | Está associado ao processamento paralelo de dados persistentes e particionados. |
| **Cloud** | Disponibiliza recursos de terceiros, provendo tecnologias como serviço. |
| **HPC (High Performance Computing)** | Ou computação de alto desempenho, envolve nós de processamento. |

## Pegadinhas

- Diferente do paralelismo geral, que é volátil (processa, mas não armazena), o Big Data persiste os dados.
- A grande diferença entre HPC e Big Data reside na persistência dos dados, além das ferramentas e modelos distintos que cada um utiliza.

## Teste-se

<details><summary>Qual a principal característica que distingue o Big Data do paralelismo geral?</summary>

A principal característica é que o Big Data persiste os dados, enquanto o paralelismo geral é volátil, processando mas não armazenando.

</details>

<details><summary>O que a Cloud provê como serviço?</summary>

A Cloud provê tecnologias como serviço, disponibilizando recursos de terceiros.

</details>

<details><summary>Quais são as duas plataformas de Cloud mais utilizadas mencionadas no texto?</summary>

As plataformas de Cloud mais utilizadas mencionadas são Azure e AWS.

</details>

<details><summary>Qual a principal diferença entre HPC e Big Data, além das ferramentas?</summary>

A principal diferença entre HPC e Big Data reside na persistência dos dados. HPC não persiste, apenas processa, enquanto Big Data persiste e armazena.

</details>

<details><summary>Cite dois modelos de processamento paralelo utilizados em HPC.</summary>

Em HPC, o processamento paralelo ocorre através de modelos específicos como MPI, PMP ou PCL.

</details>

## Conteúdo

Quando pensamos em experimentos de larga escala, consideramos algumas tecnologias: Paralelismo, Big Data e Cloud.

> [!definicao] Paralelismo
> É a capacidade de processar uma aplicação ou dados de maneira paralela. Não há uma sequência ou dependência entre as ações a serem executadas em diferentes momentos; um conjunto de operações pode ser executado em paralelo em diferentes *clusters*. Múltiplos processadores operam concorrentemente, de maneira concomitante, para atingir o mesmo objetivo.

**Big Data** está associado ao processamento paralelo de dados persistentes e particionados. Diferente do paralelismo geral, que é volátil (processa, mas não armazena), o Big Data persiste os dados. Ele é tratado de uma outra forma pela aplicação.

A **Cloud** disponibiliza recursos de terceiros, provendo tecnologias como serviço.

> [!exemplo] Cloud como Serviço: `AWS RDS`
> Ao utilizar um SGBD na `AWS`, como o `RDS`, você está usando um banco de dados como serviço. Isso elimina a necessidade de se preocupar com diversas questões, como falhas ou a atuação de um DBA, que pode se ater apenas ao desenvolvimento e persistência dos dados. A própria `AWS` gerencia esses aspectos dentro do serviço, mas para isso, é preciso pelo menos definir as suas réplicas ou utilizar um serviço que possua redundância.

Essas tecnologias vieram para facilitar a execução do quarto paradigma de análises.

### Tecnologias e `HPC`

O Big Data e o Paralelismo estão relacionados ao `HPC` (High Performance Computing), enquanto a Cloud é exemplificada por `Azure` e `AWS`, que são as mais utilizadas.

### High Performance Computing (`HPC`)

**High Performance Computing (HPC)**, ou computação de alto desempenho, envolve nós de processamento. O `lustre` é um sistema de `HPC` que possui arquivos paralelos e sem persistência. Na `HPC`, o processamento paralelo ocorre através de modelos específicos, como `MPI`, `PMP` ou `PCL`, e as informações não são persistidas; elas são apenas processadas.

### `HPC` vs. `Big Data`

A grande diferença entre `HPC` e `Big Data` reside na persistência dos dados, além das ferramentas e modelos distintos que cada um utiliza.

| Característica | `HPC` (High Performance Computing) | `Big Data` |
| :------------- | :--------------------------------- | :--------- |
| Processamento  | Paralelo                           | Paralelo   |
| Persistência   | Não persiste (apenas processa)     | Persiste e armazena |
| Modelos/Ferramentas | `MPI`, `PMP`, `PCL` (outros modelos associados) | `MapReduce`, `Spark`, SGBDs paralelos |

## Relacionado

- [[modelagem-de-dados-do-contexto-relacional-a-era-do-big-data-e-paradigmas-cientif]]
- [[decomposicao-conceitos-estrategias-e-aplicacoes]]
- [[bancos-de-dados-definicao-acesso-e-escala]]
- [[BANCO-QUESTOES-COMPLETO (2)]]
