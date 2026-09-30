---
titulo: "SGBD: Controle de Concorrência e OLTP"
tags: [sgbd, banco-de-dados, transacoes, otimizacao, sistemas, conceitos, sql]
data: 2026-09-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 11
conceitos: [Controle de Concorrência, Transações multiusuários, OLTP (Online Transaction Processing), Atomicidade, Action-Driven, OLAP (Online Analytical Processing), Arquitetura Híbrida, ETL (Extract, Transform, Load)]
---

# SGBD: Controle de Concorrência e OLTP

> [!resumo] Do que se trata
> A aula aborda o controle de concorrência em SGBDs, explicando como gerenciar múltiplos acessos para manter a coerência e acurácia dos dados. Detalha o OLTP (Online Transaction Processing), suas características, a importância da atomicidade nas transações e seu contexto action-driven. Por fim, compara OLTP com OLAP, introduzindo a arquitetura híbrida e o pipeline de dados ETL.

## Para lembrar

- **O controle de concorrência é o mecanismo utilizado para permitir o acesso concorrente de diversos usuários, mantendo os dados coerentes e a acurácia do sistema.**
- **OLTP (Online Transaction Processing) é uma abordagem de acesso simultâneo onde uma sucessão de operações é agregada em uma transação para completar uma ação, focando na performance.**
- **A atomicidade garante que uma transação seja executada completamente ou que nenhuma de suas operações seja efetivada, retornando o banco de dados ao seu estado original e consistente.**
- **Sistemas OLTP são aplicações multiusuário que gerenciam transações concorrentes, exigindo isolamento considerável e alta performance, e estão atrelados ao contexto operacional do negócio (action-driven).**
- **OLTP (ambiente operacional, propósito de processar dados) e OLAP (ambiente informativo, propósito de analisar dados) são abordagens totalmente distintas, mas complementares.**

## O que esta nota responde

- Como um SGBD gerencia o acesso concorrente de múltiplos usuários?
- O que é OLTP e qual a importância da atomicidade em suas transações?
- Quais as principais diferenças entre OLTP e OLAP?

## Conceitos

**Controle de Concorrência** · **Transações multiusuários** · **OLTP (Online Transaction Processing)** · **Atomicidade** · **Action-Driven** · **OLAP (Online Analytical Processing)** · **Arquitetura Híbrida** · **ETL (Extract, Transform, Load)**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Controle de Concorrência e OLTP | ▪▪ |
| `05:00` | OLTP: Características, Atomicidade e Contexto | ▪▪ |
| `09:20` | OLTP: Action-Driven, OLAP e Arquitetura | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Controle de Concorrência** | O mecanismo utilizado para permitir o acesso concorrente de diversos usuários. Seu objetivo é manter os dados coerentes e a acurácia do sistema, garantindo que os dados permaneçam com alto nível de corretude e não se modifiquem, a não ser por uma ação específica de atualização. Um acesso concorrente não deve resultar em inconsistência de estado do SGBD. |
| **OLTP** | OLTP (Online Transaction Processing) é uma abordagem de acesso simultâneo onde uma sucessão de operações é agregada em uma transação para completar uma ação. Sistemas OLTP são encarregados de registrar todas as transações de uma determinada operação organizacional. O OLTP foca na performance. |
| **Sistema OLTP** | Um sistema orientado a processamento de transações online em tempo real. Ele requer suporte para transações em rede e utiliza processamento cliente-servidor, com comunicação via API ou HTTP, e softwares intermediários que permitem que as transações rodem em diferentes plataformas e computadores distribuídos pela rede. |
| **Atomicidade** | Garante que uma transação seja executada completamente ou que nenhuma de suas operações seja efetivada, retornando o banco de dados ao seu estado original e consistente. Se uma operação falha durante a execução de uma transação, o SGBD deve ser capaz de retroceder e desfazer todas as ações anteriores daquela transação. |

## Pegadinhas

- OLTP e OLAP são abordagens distintas: OLTP foca em processar dados em ambiente operacional, enquanto OLAP foca em analisar dados em ambiente informativo.
- O OLTP é um ambiente action-driven, voltado para decisões que utilizam transações, diferente do data-driven, onde a tomada de decisão é baseada em dados.

## Teste-se

<details><summary>Qual o principal mecanismo utilizado para permitir o acesso concorrente de diversos usuários em um SGBD?</summary>

O principal mecanismo é o controle de concorrência. Ele visa manter os dados coerentes e a acurácia do sistema, garantindo que os dados não se modifiquem sem uma ação específica de atualização.

</details>

<details><summary>Quais são os três objetivos do controle de concorrência?</summary>

Os objetivos são: manter os dados coerentes, manter a acurácia do sistema garantindo a corretude dos dados, e assegurar que os dados não se modifiquem a não ser por uma ação específica de atualização.

</details>

<details><summary>O que significa a sigla OLTP e qual seu foco principal?</summary>

OLTP significa Online Transaction Processing. Seu foco principal é a performance na execução de uma sucessão de operações agregadas em uma transação para completar uma ação.

</details>

<details><summary>Explique o conceito de Atomicidade em sistemas OLTP.</summary>

Atomicidade garante que uma transação seja executada completamente ou que nenhuma de suas operações seja efetivada. Se uma operação falha, o SGBD deve retroceder e desfazer todas as ações anteriores daquela transação, retornando o banco de dados ao estado original e consistente.

</details>

<details><summary>Qual a principal diferença entre OLTP e OLAP em termos de propósito e ambiente?</summary>

OLTP tem como propósito processar dados em um ambiente operacional, enquanto OLAP tem como propósito analisar dados em um ambiente informativo.

</details>

<details><summary>Em que contexto o OLTP está relacionado, e como ele se diferencia do conceito de data-driven?</summary>

O OLTP está relacionado ao contexto de action-driven, onde o ambiente operacional é voltado para decisões que utilizam transações. Ele se diferencia do data-driven, onde a tomada de decisão é baseada em dados.

</details>

## Conteúdo

`⏱ 00:00`

Já falamos sobre natureza autodescritiva, isolamento do programa de dados e a parte das views que fornecem uma nova perspectiva dos dados para cada usuário ou grupo de usuários distinto. Agora, falaremos sobre compartilhamento de dados e processamento de transações multiusuários.

Dificilmente você terá um sistema acessado por apenas um usuário. Na maioria dos casos, múltiplos acessos virão de setores, pessoas e grupos distintos, cada um com necessidades diferentes do SGBD. A maior dificuldade nisso tudo está relacionada à integração do sistema para prover o acesso concomitante dessas informações para essas diferentes pessoas, e a manutenção também é um fator crucial.

O mecanismo utilizado para permitir o acesso concorrente de diversos usuários é o **controle de concorrência**. Um SGBD precisa prover mecanismos de controle de concorrência para:
- Manter os dados coerentes.
- Manter a acurácia do sistema, garantindo que os dados continuem com alto nível de corretude.
- Assegurar que os dados não se modifiquem, a não ser por uma ação específica de atualização.

Um acesso concorrente não pode resultar em inconsistência de estado do SGBD.

> [!definicao] Controle de Concorrência
> O mecanismo utilizado para permitir o acesso concorrente de diversos usuários.
> >
> Seu objetivo é manter os dados coerentes e a acurácia do sistema, garantindo que os dados permaneçam com alto nível de corretude e não se modifiquem, a não ser por uma ação específica de atualização. Um acesso concorrente não deve resultar em inconsistência de estado do SGBD.

> [!exemplo] Reserva de assentos em voos
> Imagine diferentes atendentes realizando a reserva de um assento para uma viagem em um voo específico. Todas essas pessoas precisam acessar a lista de assentos. Cada uma escolherá um assento, mas pode acontecer de, por acaso, duas ou mais atendentes escolherem o mesmo assento simultaneamente.
> >
> Para evitar inconsistências — como duas pessoas diferentes chegarem no dia do voo com passagens para o mesmo assento — é essencial que o sistema tenha um controle de concorrência. Se a atendente A está fazendo a reserva e já está efetivamente modificando o status de um assento, o sistema deve bloquear (dar um `lock`) pelo menos aquele atributo para que a outra pessoa não consiga acessá-lo. A visão dela deve ser que o assento está "ocupado" ou "reservado", pelo menos até o momento em que a atendente A conclua ou desista do processo.
> >
> O foco é permitir a concorrência no acesso às informações, mas garantindo que os dados continuem com corretude.

Existe também o **OLTP**.

> [!definicao] OLTP
> **OLTP** (Online Transaction Processing) é uma abordagem de acesso simultâneo onde uma sucessão de operações é agregada em uma transação para completar uma ação.
> >
> Sistemas OLTP são encarregados de registrar todas as transações de uma determinada operação organizacional. Por exemplo, uma transação pode conter uma série de operações que o sistema deve efetuar de ponta a ponta, garantindo sua execução.
> >
> O OLTP foca na performance. Um exemplo seria um sistema de transações bancárias.

`⏱ 05:00`

Um sistema de transações bancárias registra as operações que vão ser efetuadas em um banco, seja um caixa, seja uma reserva de viagem, enfim. É preciso que todas as operações contidas nessa transação sejam efetuadas. Cenários como banco, caixa, reserva de viagem, hotel e cartão de crédito estão associados a esse tipo de operação.

> [!definicao] OLTP (Online Transaction Processing)
> Um **sistema OLTP** é um sistema orientado a processamento de transações online em tempo real. Ele requer suporte para transações em rede e utiliza processamento cliente-servidor, com comunicação via `API` ou `HTTP`, e softwares intermediários que permitem que as transações rodem em diferentes plataformas e computadores distribuídos pela rede.

Em grandes aplicações, a eficiência do OLTP dependerá muito da sofisticação do software de gerenciamento de transações, como o `CICS`. É necessário um ambiente otimizado para que ele consiga, de fato, executar todas as operações dentro de uma transação.

A ideia do OLTP é justamente prover performance para executar uma transação fim a fim sem problemas. Os cenários em que se encaixa esse tipo de situação são bem específicos e precisam de bastante performance. Venda, banco e reserva, por exemplo, exigem constância na execução, e o sistema precisa ser destinado para este fim.

### Características do OLTP

Um sistema OLTP é uma aplicação multiusuário que gerencia transações concorrentes. É essencial que essas transações ocorram de maneira satisfatória e com um isolamento considerável, sem interferências.

> [!exemplo] A importância do isolamento
> Ao realizar um depósito em um caixa eletrônico, o sistema não pode travar e reter o dinheiro. Se a transação não fosse efetuada, isso causaria um problema grave. Por isso, é necessário um isolamento considerável para que as transações ocorram de maneira satisfatória, sem interferências.

A modalidade de trabalho para sistemas OLTP é toda voltada para um SGBD com configuração de alta performance. O sistema é concebido e pensado desde o design inicial do projeto de banco de dados.

### Atomicidade

> [!definicao] Atomicidade
> A **atomicidade** garante que uma transação seja executada completamente ou que nenhuma de suas operações seja efetivada, retornando o banco de dados ao seu estado original e consistente. Se uma operação falha durante a execução de uma transação, o SGBD deve ser capaz de retroceder e desfazer todas as ações anteriores daquela transação.

### Contexto: Action-Driven

O OLTP está muito relacionado ao contexto de **action-driven**. Anteriormente, foi discutido o conceito de *data-driven*, onde a tomada de decisão é baseada em dados. No OLTP, o ambiente operacional é voltado para decisões que utilizam transações.

`⏱ 09:20`

Por que decisão que eu estou comentando? Porque, a partir do momento que eu vou reservar um hotel, uma passagem, consultar meu extrato bancário, eu estou tomando uma decisão.

Esses sistemas são orientados à transação, possibilitando que possuam um alto desempenho. Eles estão atrelados ao contexto operacional do negócio.

### OLTP vs. OLAP

Para contrapor e perceber onde o **OLTP** (Online Transaction Processing) está inserido, nós temos um cenário que geralmente é comparado com o **OLAP** (Online Analytical Processing).

| Característica | OLTP (Online Transaction Processing) | OLAP (Online Analytical Processing) |
|---|---|---|
| Ambiente | Operacional | Informativo |
| Propósito | Processar dados | Analisar dados |

São abordagens totalmente distintas, mas uma, na verdade, complementa a outra.

### Arquitetura Híbrida e Pipeline de Dados

Ainda surgiu, depois disso, uma outra arquitetura, que seria uma arquitetura híbrida, que mescla o bom dos dois mundos.

Nesse processo, nós teríamos um pipeline de dados chamado **ETL** (Extract, Transform, Load).

Isso possibilita realizar uma abordagem mais analítica, e depois, através de *data mining*, análises e tomadas de decisão, as informações são devolvidas para o ambiente operacional.

O cenário do OLTP está associado a um ambiente de banco de dados (ambiente de SGBD), enquanto o OLAP está mais associado a um ambiente de *data warehouses*.

## Relacionado

- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[../Introdução a Banco de Dados/sgbd-etapas-estrutura-e-fases]]
- [[../Introdução a Banco de Dados/modelo-relacional-usuarios-e-integracao-de-sgbds]]
- [[sgbd-natureza-autodescritiva-esquema-e-catalogo]]
