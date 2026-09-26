---
titulo: "SGBD: Cenários de Não Utilização e Alternativas"
tags: [sgbd, banco-de-dados, sistema, otimizacao, conceitos, ferramentas, estudo]
data: 2026-09-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 5
conceitos: [SGBD, Overhead do sistema, Custo-benefício, Controle de concorrência, Sistemas embarcados (Embedded Systems), Real time, SQLite, Persistência em arquivo]
---

# SGBD: Cenários de Não Utilização e Alternativas

> [!resumo] Do que se trata
> A aula explora os cenários em que a utilização de um Sistema Gerenciador de Banco de Dados (SGBD) pode não ser a melhor opção, considerando o custo-benefício e o *overhead* do sistema. Ela detalha exemplos práticos de dispositivos e softwares que operam sem SGBDs, como sistemas embarcados e aplicações de *real time*. Por fim, a nota apresenta o SQLite como uma alternativa simplificada e enfatiza a importância de analisar os requisitos do projeto para a decisão de uso.

## Para lembrar

- **A utilização de um SGBD é justificada por múltiplos acessos, necessidade de transações e um alto nível de confiabilidade.**
- **O custo de um SGBD inclui investimento inicial, generalidade da definição e processamento, além de *overhead* para segurança, controle de concorrência, recuperação e funções de integridade.**
- **Cenários como projetos de análise de dados com equipes reduzidas, sistemas embarcados e aplicações rigorosas de *real time* podem não necessitar de um SGBD.**
- **Dispositivos de rede, sistemas GIS de geolocalização e AutoCAD são exemplos práticos de sistemas que não utilizam um SGBD.**
- **SQLite é uma alternativa simplificada para gerenciamento e persistência de informações em cenários como celulares, sendo uma biblioteca para C.**

## O que esta nota responde

- Em que situações não é recomendado utilizar um SGBD?
- Quais são os custos e o *overhead* associados ao uso de um SGBD?
- Quais são as alternativas simplificadas para persistência de dados quando um SGBD completo não é necessário?

## Conceitos

**SGBD** · **Overhead do sistema** · **Custo-benefício** · **Controle de concorrência** · **Sistemas embarcados (Embedded Systems)** · **Real time** · **SQLite** · **Persistência em arquivo**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Custo-benefício e cenários de não uso SGBD | ▪▪ |
| `04:20` | Decisão de uso SGBD: requisitos e contexto | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **SGBD** | Sistema Gerenciador de Banco de Dados |
| **SQLite** | Uma biblioteca para C, utilizada para gerenciamento e persistência das informações. |

## Teste-se

<details><summary>Quais são as características que acrescem no custo de um SGBD?</summary>

O custo de um SGBD está associado ao investimento inicial e à generalidade da definição e processamento. O overhead do sistema inclui segurança, controle de concorrência, recuperação e funções de integridade.

</details>

<details><summary>Em que tipo de cenário a utilização de um SGBD é justificada?</summary>

A utilização de um SGBD é justificada quando há múltiplos acessos, necessidade de transações e um nível de confiabilidade mais alto.

</details>

<details><summary>Cite três exemplos práticos de dispositivos ou softwares que não utilizam um SGBD.</summary>

Dispositivos de rede voltados para a acomodação de pacotes, sistemas GIS de geolocalização e o AutoCAD são exemplos de sistemas que não utilizam um SGBD.

</details>

<details><summary>Qual alternativa simplificada de gerenciamento de dados pode ser usada em cenários como celulares?</summary>

Em cenários que utilizam um modelo simplificado, como em celulares, pode-se usar o SQLite. É uma biblioteca para C, utilizada para gerenciamento e persistência das informações.

</details>

<details><summary>Qual é a principal consideração ao decidir se deve ou não usar um SGBD?</summary>

É crucial entender os requisitos do seu projeto e do seu contexto. Deve-se questionar se realmente se precisa de todas as características e vantagens que um SGBD oferece.

</details>

## Conteúdo

`⏱ 00:00`

### Quando não utilizar um SGBD

Existe um cenário em que se opta por não utilizar um **SGBD** (Sistema Gerenciador de Banco de Dados). Esse cenário está atrelado ao custo-benefício de usar um SGBD em relação ao que se precisa persistir e ao custo de *overhead* do sistema.

Se você tem um cenário muito específico e curto, que não tem muitas modificações, para que usar um SGBD? É preciso entender que a utilização de um SGBD é justificada quando há múltiplos acessos, necessidade de transações, e um nível de confiabilidade mais alto. Há um *trade-off* a ser considerado.

O custo de um SGBD está associado a certas características, como:
- Investimento inicial.
- Generalidade da definição e processamento.

Isso acresce no custo, porque o SGBD, no modelo relacional, traz uma representação geral, consegue abstrair o conjunto de dados e processá-los de maneira mais otimizada. No entanto, existe o custo e o *overhead* do sistema, que incluem:
- Segurança.
- Controle de concorrência.
- Recuperação.
- Funções de integridade.

Há uma série de mecanismos que vão acrescendo no custo. É preciso considerar: eu preciso de tudo isso para minha base de dados? Se sim, você utilizará um SGBD. Se não, por exemplo, se apenas você manipula os dados e não precisa de controle de concorrência, você pode ponderar o que realmente é necessário.

### Cenários de não utilização de SGBD

Existem alguns cenários em que não se utiliza um SGBD.

> [!exemplo] Projeto de análise de dados (freelancer)
> Eu, Juliana, como freelancer, estou fazendo um projeto de análise de dados para uma empresa. Eles querem aumentar a performance de negócios em um contexto específico. Eu não preciso utilizar um SGBD para isso. A linguagem `Python` me oferece uma série de recursos onde não há necessidade de usar um SGBD. Eu não preciso jogar os dados em um sistema, processá-los lá dentro e depois puxar de novo. Eu simplesmente puxo as informações do arquivo e as processo via programação.

Outro exemplo são os **Embedded Systems** (sistemas embarcados). Quando você tem sistemas de dados embarcados, como em um robô, você não vai usar um SGBD completo.

Se o seu banco de dados é simples e nunca vai mudar, pode ser mais interessante utilizar uma persistência em arquivo e tratar isso na aplicação.

Aplicações rigorosas de *real time* que demandam uma parte mais performática também podem ser prejudicadas quando se utiliza um SGBD relacional.

#### Exemplos práticos de dispositivos e softwares que não utilizam SGBD

São exemplos de *real world*:
- Dispositivos de rede voltados para a acomodação de pacotes.
- Sistemas GIS de geolocalização.
- O `AutoCAD`, uma ferramenta voltada para arquitetura e urbanismo.

Todos esses sistemas mencionados não utilizam um SGBD.

#### Alternativa simplificada: SQLite

Em cenários que utilizam um modelo simplificado, como em celulares, você pode usar o `SQLite`. É uma biblioteca para `C`, utilizada para gerenciamento e persistência das informações.

Pense bem: se o cenário precisa, leve em consideração todas as características do SGBD e as vantagens que ele oferece. Mas questione se você realmente precisa de tudo aquilo, pois, às vezes, pode gerar um trabalho desnecessário.

`⏱ 04:20`

vai te dar um trabalho e criar a história, como utilizar um canhão para matar uma formiga. Você terá um trabalho enorme para persistir dados no banco, quando poderia tratá-los facilmente utilizando uma linguagem de programação.

### Decisão sobre o Uso de STBD

> [!exemplo] Cenários de Equipe Reduzida
> Principalmente se você trabalha como `job solo`, `freelancer` ou como analista interno. Por exemplo, em sua dissertação ou projeto, se a equipe for composta por você e mais uma pessoa, ou apenas uma pessoa, ou somente você.

É crucial entender os requisitos do seu projeto e do seu contexto para definir se você utilizará ou não um STBD.

## Relacionado

- [[sgbd-natureza-autodescritiva-esquema-e-catalogo]]
- [[sgbd-atores-tipos-de-usuarios-e-finalidade]]
- [[sgbds-os-mais-utilizados-no-mercado]]
- [[sgbd-atores-indiretos-e-requisitos-operacionais]]
