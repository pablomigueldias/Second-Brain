---
titulo: "ITIL 4 — Detalhamento das Práticas de Gerenciamento de Serviços"
tags: [conceitos, estudo, governanca, gestao-de-projetos, sistema, organizacao, atendimento]
data: 2026-09-10
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 20
conceitos: [Análise de Negócio, Gerenciamento de Catálogo de Serviço, Portfólio de Serviços, Pipeline de Serviços, Gerenciamento de Disponibilidade, Gerenciamento de Desempenho e Capacidade, Gerenciamento de Incidentes, Habilitação de Mudanças]
---

# ITIL 4 — Detalhamento das Práticas de Gerenciamento de Serviços

> [!resumo] Do que se trata
> Esta aula detalha as práticas de gerenciamento de serviços da ITIL v4, explicando seus objetivos e como se encaixam nos níveis estratégico, tático e operacional. São abordadas práticas como Análise de Negócio, Gerenciamento de Catálogo de Serviço, Gerenciamento de Nível de Serviço, e a distinção entre Gerenciamento de Disponibilidade e Capacidade. A nota também explora o Gerenciamento de Incidentes e Requisições de Serviço, Habilitação de Mudanças e seus tipos, além de Gerenciamento de Configuração e Ativos de TI.

## Para lembrar

- **Análise de Negócio define as necessidades de um negócio e recomenda soluções para criar valor para as partes interessadas.**
- **Gerenciamento de Catálogo de Serviço propicia uma única fonte de informação consistente sobre todos os serviços e ofertas, disponível para o público-alvo pertinente.**
- **Gerenciamento de Disponibilidade foca em garantir os níveis de disponibilidade acordados, enquanto Gerenciamento de Desempenho e Capacidade visa garantir os níveis de desempenho e atender à demanda futura de forma eficaz em custo.**
- **Uma requisição de serviço não é obrigatoriamente um incidente; um incidente é uma interrupção ou redução da qualidade do serviço, enquanto uma requisição pode ser um pedido de informação.**
- **Habilitação de Mudanças garante que o serviço possa ser modificado, e os tipos de mudança são Padrão (pré-aprovada), Normal (fluxo de aprovação) e Emergencial (correção rápida de erro com impacto).**

## O que esta nota responde

- Quais são as principais práticas de gerenciamento de serviços detalhadas na ITIL v4?
- Qual a distinção entre Gerenciamento de Disponibilidade e Gerenciamento de Desempenho e Capacidade?
- Quais são os tipos de mudança abordados na prática de Habilitação de Mudanças?

## Conceitos

**Análise de Negócio** · **Gerenciamento de Catálogo de Serviço** · **Portfólio de Serviços** · **Pipeline de Serviços** · **Gerenciamento de Disponibilidade** · **Gerenciamento de Desempenho e Capacidade** · **Gerenciamento de Incidentes** · **Habilitação de Mudanças**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Práticas de gerenciamento de serviços ITIL 4 | ▪▪ |
| `04:40` | Catálogo, design e nível de serviço | ▪▪ |
| `09:20` | Disponibilidade, desempenho, capacidade e incidentes | ▪▪▪ |
| `13:20` | Continuidade, incidentes, problemas e mudanças | ▪▪▪ |
| `17:20` | Validação, configuração, ativos e técnico | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Análise de Negócio** | Tem como objetivo a prática analítica de um negócio ou de algum de seus elementos que define suas necessidades e recomenda soluções para atendê-las e/ou para resolver o problema de um negócio e criar valor para as partes interessadas. |
| **Gerenciamento de Catálogo de Serviço** | Além de propiciar uma única fonte de informação consistente sobre todos os serviços e as ofertas de serviços, garante que ele esteja disponível para o público-alvo pertinente. |
| **Design de Serviço** | Tem como objetivo projetar produtos e serviços que sejam adequados ao propósito e ao uso e possam ser fornecidos pela organização e seu ecossistema. |
| **Gerenciamento de Disponibilidade** | Tem como objetivo garantir que os serviços entreguem os níveis de disponibilidade acordados para atender às necessidades de clientes ou usuários. |
| **Requisição de Serviço** | Uma solicitação proveniente de um usuário ou de um representante de um usuário ou de um representante autorizado do usuário que inicia uma ação de serviços conforme acordado, como parte normal da entrega do serviço. |
| **Gerenciamento de Incidentes** | É o processo preocupado em retornar o funcionamento normal de um respectivo serviço o mais rápido possível. |
| **Gerenciamento de Problemas** | É o processo preocupado em descobrir a causa, o que está causando aquele teu incidente ou diversos outros incidentes. Tem como objetivo reduzir a probabilidade e o impacto de incidentes por meio da identificação de suas causas reais e potenciais e do gerenciamento de soluções de contorno e erros conhecidos. |
| **Gerenciamento de Liberação** | Tem como objetivo disponibilizar serviços e características novos e modificados para uso. |
| **Gerenciamento de Mudanças Organizacionais** | Está relacionado ao negócio. É quando há uma parada rolando na organização, que estão mudando. |
| **Gerenciamento de Habilitação de Mudanças** | Tem como objetivo garantir que os riscos sejam devidamente avaliados, autoriza o prosseguimento das mudanças e gerencia o calendário de mudanças para maximizar o número de mudanças bem sucedidas. |

## Pegadinhas

- Não confunda Gerenciamento de Disponibilidade com Gerenciamento de Desempenho e Capacidade.
- Não confunda Gerenciamento de Incidentes com Gerenciamento de Problemas.
- Uma requisição de serviço não é obrigatoriamente um incidente.
- Não confunda Gerenciamento de Mudanças Organizacionais com Habilitação de Mudanças.

## Teste-se

<details><summary>Qual o objetivo principal do Gerenciamento de Nível de Serviço?</summary>

Definir metas claras e baseadas no negócio para o desempenho dos serviços, permitindo que a entrega de um serviço seja avaliada, monitorada e gerenciada com relação a essas metas.

</details>

<details><summary>Qual a diferença entre Acordo de Nível de Serviço (SLA) e Acordo de Nível Operacional (OLA) quanto à emissão?</summary>

O SLA é emitido entre um provedor externo e um cliente externo. O OLA é emitido entre um provedor de serviço interno e um cliente interno.

</details>

<details><summary>Um administrador de rede não avaliou a capacidade necessária para um concurso público, causando a queda do servidor de inscrições. Isso é um problema de qual gerenciamento?</summary>

É um problema de Gerenciamento de Desempenho e Capacidade. O administrador não avaliou previamente a demanda atual e futura do serviço.

</details>

<details><summary>Qual a principal diferença entre Gerenciamento de Incidentes e Gerenciamento de Problemas?</summary>

O Gerenciamento de Incidentes foca em restaurar a operação normal do serviço o mais rápido possível. O Gerenciamento de Problemas busca identificar a causa raiz dos incidentes para reduzir sua probabilidade e impacto.

</details>

<details><summary>Quais são os três tipos de mudança abordados na Habilitação de Mudanças?</summary>

Os três tipos são: Mudança Padrão (baixo risco, pré-aprovada), Mudança Normal (segue fluxo de registro, avaliação e aprovação) e Mudança Emergencial (reparar erro com impacto negativo rapidamente).

</details>

<details><summary>Qual o objetivo do Gerenciamento de Ativos de TI?</summary>

O objetivo é o planejamento e gerenciamento do ciclo de vida completo de todos os ativos de serviços de tecnologia da informação.

</details>

## Conteúdo

`⏱ 00:00`

Olá, concurseiros de plantão! Quem vos fala é o professor Gabriel Pacheco. Vamos retornar ao nosso conteúdo e ver as práticas de gerenciamento de serviços.

Fica muito mais fácil compreender que as coisas acontecem na sua organização em um nível estratégico negocial, depois no nível tático e gerencial, e por fim no nível operacional. Assim, você consegue entender claramente como essas práticas se encaixam.

Você precisa decorar as práticas de gerenciamento de serviços que temos na `ITIL V4`. Vou apresentar uma por uma, e depois expandiremos o estudo de cada uma delas para que fiquem bem assimiladas.

As práticas são:
- Análise de negócio
- Gerenciamento de catálogo de serviços
- Design de serviço
- Gerenciamento de nível de serviço
- Gerenciamento de disponibilidade
- Gerenciamento de capacidade
- Gerenciamento de continuidade de serviços
- Monitoramento e gerenciamento de eventos
- Central de serviços
- Gerenciamento de incidentes
- Gerenciamento de requisição de serviço
- Gerenciamento de problemas
- Gerenciamento de liberação
- Habilitação de mudança
- Validação e teste de serviço
- Gerenciamento de configuração de serviço
- Gerenciamento de ativos de serviço

> [!atenção]
> Adoram misturar Gerenciamento de Disponibilidade e Gerenciamento de Capacidade, principalmente na `ITIL V3`. Tome nota disso!

> [!atenção]
> Adoram misturar Gerenciamento de Incidentes e Gerenciamento de Problemas. Principalmente esses dois.

> [!atenção]
> A prática de Habilitação de Mudança já foi bem cobrada em provas.

Agora, vamos detalhar cada uma, assim como fizemos previamente com as práticas gerais de gerenciamento de serviços.

### Análise de Negócio

> [!definicao] Análise de Negócio
> Tem como objetivo a prática analítica de um negócio ou de algum de seus elementos que define suas necessidades e recomenda soluções para atendê-las e/ou para resolver o problema de um negócio e criar valor para as partes interessadas.
>
> Basicamente, você está aplicando ferramentas de análise para entender qual é o problema do seu negócio e, com a entrega daquele serviço, conseguir agregar valor ao seu cliente.

### Gerenciamento de Catálogo de Serviço

> [!definicao] Gerenciamento de Catálogo de Serviço
> Além de propiciar uma única fonte de informação consistente sobre todos os serviços e as ofertas de serviços, garante que ele esteja disponível para o público-alvo pertinente.

Aqui temos uma relação muito forte entre o **Gerenciamento de Catálogo de Serviços** e o **Gerenciamento de Portfólio de Serviços**.

> [!exemplo] A analogia do funil de serviços
> Imagine um tonel que está filtrando os serviços. Todo esse tonel representa o seu **Portfólio de Serviços** na organização.
>
> Dentro desse portfólio, você tem um funil. Os serviços que estão sendo desenvolvidos, ainda na visão do seu portfólio, podem passar por esse funil.
>
> Em um certo momento, quando eles passam por esse funil, estarão disponíveis para que um cliente ou uma organização consiga utilizá-los.
>
> O que você tem no seu portfólio de serviços, que está acima do funil, é chamado de **Pipeline de Serviços**.

`⏱ 04:40`

Pipeline de serviços. O que está no seu catálogo de serviços é o que você tem no seu portfólio de serviços.

O **catálogo de serviços** é definido como a especificação de todos os serviços que estão efetivamente disponíveis para a utilização de uma organização do seu cliente.

Algumas coisas podem ser retiradas desse catálogo de serviço e colocadas em um outro balde, que são serviços que você não utiliza mais, mas que você em algum momento pode retomar a utilização. Isso também compõe o teu portfólio de serviços e é chamado de **serviços descontinuados** ou **serviços aposentados**.

#### Serviços Descontinuados
Eles servem para que, se você tiver um outro serviço que esteja centralizado e trabalhado com aquela mesma característica, você possa buscar ele lá no seu serviço descontinuado.

### Design de Serviço
Seguindo para a nossa aula, você tem o seu **design de serviço**. A palavra *design* deve ser interpretada como projeto.

> [!definicao] Design de Serviço
> Tem como objetivo projetar produtos e serviços que sejam adequados ao propósito e ao uso e possam ser fornecidos pela organização e seu ecossistema.

### Gerenciamento de Nível de Serviço
O **Gerenciamento de nível de serviço** tem como objetivo definir metas claras e baseadas no negócio para o desempenho dos serviços, permitindo que a entrega de um serviço seja devidamente avaliada, monitorada e gerenciada com relação a essas metas.

É importante lembrar de alguns termos do gerenciamento de serviço:

*   Acordo de nível de serviço
*   Acordo de nível operacional
*   Contrato

Estes termos possuem características fundamentais:

| Característica | Acordo de Nível de Serviço (SLA) | Acordo de Nível Operacional | Contrato |
| :--- | :--- | :--- | :--- |
| **Emissão entre** | Provedor externo e cliente externo | Provedor de serviço interno e cliente interno | Trabalhado sempre com vias legais |
| **Composição** | Pode compor o contrato | Não se aplica | Pode incorporar o SLA |
| **Características legais** | Não tem características legais | Não se aplica | Possui características legais |

### Práticas de Gerenciamento de Serviços
Nós teremos o **Gerenciamento de disponibilidade**.

> [!definicao] Gerenciamento de Disponibilidade
> Tem como objetivo garantir que os serviços entreguem os níveis de disponibilidade acordados para atender às necessidades de clientes ou usuários.

Por exemplo, se você precisa que o serviço esteja disponível em 99,9% do tempo, isso é gerenciamento de disponibilidade.

#### Diferença entre Gerenciamento de Disponibilidade e Gerenciamento de Desempenho e Capacidade

> [!atenção] Não confundam nunca Gerenciamento de Disponibilidade com Gerenciamento de Desempenho e Capacidade.

O **Gerenciamento de desempenho e capacidade** tem como objetivo garantir que os serviços alcancem os níveis de desempenho acordados e previstos, atendendo à demanda atual e futura de maneira eficaz em custo.

Para nunca mais errar questões de prova, é fundamental fazer uma comparação entre os dois gerenciamentos:

| Gerenciamento | Objetivo Principal | Exemplo Prático |
| :--- | :--- | :--- |
| **Gerenciamento de Disponibilidade** | Garantir que o serviço entregue os níveis de disponibilidade acordados. | Quero que o serviço de telefonia da minha organização esteja disponível 99,9% do tempo necessário. |
| **Gerenciamento de Desempenho e Capacidade** | Garantir que os serviços alcancem os níveis de desempenho acordados e previstos, atendendo à demanda atual e futura de maneira eficaz em custo. | (Não foi fornecido um exemplo específico, mas o foco é a capacidade de atender a demanda.) |

`⏱ 09:20`

Para o gerenciamento da disponibilidade, eu quero que o serviço de telefonia da minha organização esteja disponível 99,9% do tempo necessário. Um exemplo é o serviço de conectividade à internet; isso também é um serviço de disponibilidade.

Para **desempenho e capacidade**, eu quero que o meu serviço de conexão à internet suporte até mil conexões simultâneas com comunicação de dados de 500 megabits por segundo. A diferença é que um é avaliação da capacidade e outro é disponibilidade.

> [!atenção]
> Nas provas, eles gostam de misturar disponibilidade com desempenho e capacidade. Você não pode errar esse tipo de questão.

Outra característica interessante, que aparece em algumas questões como um `cheque-mate` de conteúdo, é a relação entre desempenho e capacidade e incidentes.

### Desempenho e Capacidade vs. Gerenciamento de Incidentes

> [!exemplo] Problema de Desempenho e Capacidade em Concurso Público
> Um administrador de sistema operacional ou administrador de rede está diante de um problema. Ele não conversou adequadamente com a área de negócio para saber quantos usuários teriam simultaneamente nas inscrições de um concurso público específico que ele está trabalhando, por exemplo, o concurso público da Receita Federal do Brasil.
> >
> Por conta desse problema, a conexão caiu e o servidor onde as pessoas estavam fazendo suas inscrições parou de funcionar.
> >
> **Nesse momento, eu tenho um problema de gerenciamento de incidentes ou de desempenho e capacidade?**
> >
> É um problema de desempenho e capacidade.
> >
> **Motivo:** O administrador não avaliou previamente com o cliente o quanto era preciso atender inicialmente daquele serviço. E mais do que isso, ele também não avaliou para o futuro, fazendo uma projeção do que seria necessário atender naquele serviço.

Essas variáveis são frequentemente abordadas em questões de prova.

### Outros Gerenciamentos

**Gerenciamento de Continuidade de Serviço** tem como objetivo garantir que os níveis de disponibilidade e de desempenho do serviço sejam suficientes em caso de desastre.

**Monitoração e gerenciamento de eventos** tem como objetivo a observação sistemática de serviços e componentes de serviço, e o registro e relato de determinadas mudanças de estado identificadas como eventos.

**Central de serviço** tem como objetivo capturar a demanda: demanda de resolução de incidentes e requisições de serviço.

**Gerenciamento de incidentes** tem como objetivo minimizar o impacto negativo de incidentes, restaurando a operação normal do serviço o mais rápido possível. O aspecto é tipo: a luz apagou, acende; a luz apagou, acende, sem se preocupar com a motivação pela qual a luz está sendo apagada. A preocupação é retornar o funcionamento do serviço o mais rápido possível ao nível normal.

### Requisições de Serviço vs. Incidentes

> [!atenção]
> É muito comum a afirmação de que uma requisição de serviço obrigatoriamente sempre será um incidente. Isso não é verdade.

Um incidente pode gerar uma requisição de serviço? Sim, pode. Mas uma **requisição de serviço** pode ser simplesmente você ligando para a sua central de atendimento e pedindo informações sobre como mudar a sua senha, porque você não sabe como mudar.

Isso é um incidente? Você está pedindo para informar como muda a senha. Isso foi um incidente? Você está com alguma incapacidade de uso de algum serviço? Você não está.

Então, a requisição de serviço tem como objetivo...

`⏱ 13:20`

a requisição de serviço tem como objetivo suportar a qualidade acordada de um serviço por meio do tratamento de todas as requisições de serviço pré-definidas e iniciadas pelos usuários de maneira eficaz e fácil de usar.

> [!definicao] Requisição de Serviço
> Uma solicitação proveniente de um usuário ou de um representante de um usuário ou de um representante autorizado do usuário que inicia uma ação de serviços conforme acordado, como parte normal da entrega do serviço.

Ou seja, eu tenho ali a área de suporte que vai me apoiar a modificação da minha senha. Eu ligo e peço informações sobre como modificar a senha. Isso é uma requisição de serviço.

### Gerenciamento de Serviços

Além disso, há o gerenciamento de incidentes e o gerenciamento de problemas.

> [!definicao] Gerenciamento de Incidentes
> É o processo preocupado em retornar o funcionamento normal de um respectivo serviço o mais rápido possível.

> [!definicao] Gerenciamento de Problemas
> É o processo preocupado em descobrir a causa, o que está causando aquele teu incidente ou diversos outros incidentes. Tem como objetivo reduzir a probabilidade e o impacto de incidentes por meio da identificação de suas causas reais e potenciais e do gerenciamento de soluções de contorno e erros conhecidos.

> [!definicao] Gerenciamento de Liberação
> Tem como objetivo disponibilizar serviços e características novos e modificados para uso.

É o gerenciamento de como você vai colocar um respectivo serviço que, ora, tenha sido desenvolvido em produção.

### Comparação de Conceitos

É fundamental não confundir os conceitos de gerenciamento de incidentes e gerenciamento de problemas.

| Conceito | Foco Principal | Objetivo |
| :--- | :--- | :--- |
| **Gerenciamento de Incidentes** | Restabelecer o serviço. | Retornar o funcionamento normal o mais rápido possível. |
| **Gerenciamento de Problemas** | Encontrar a causa raiz. | Reduzir a probabilidade e o impacto de incidentes identificando causas reais e potenciais. |

### Habilitação de Mudanças

O **Gerenciamento de Liberação** é o seu gerenciamento de colocar um serviço em produção.

O **Gerenciamento de Mudanças Organizacionais** está relacionado ao negócio. É quando há uma parada rolando na organização, que estão mudando. O que eu tenho que saber é ter habilidades específicas para garantir que aquilo mude e fique perfeito.

> [!definicao] Gerenciamento de Mudanças Organizacionais
> Está relacionado ao negócio. É quando há uma parada rolando na organização, que estão mudando.

Por outro lado, o **Gerenciamento de Habilitação de Mudanças** tem como objetivo garantir que os riscos sejam devidamente avaliados, autoriza o prosseguimento das mudanças e gerencia o calendário de mudanças para maximizar o número de mudanças bem sucedidas.

> [!atenção] Não confunda Gerenciamento de Mudanças Organizacionais com Habilitação de Mudanças.
>
> *   **Mudança Organizacional:** É uma mudança negocial ou legislativa.
> *   **Habilitação de Mudanças:** É a prática que garante que o serviço possa ser modificado, seja por uma necessidade negocial ou legislativa.

### Tipos de Mudança

Existem três tipos de mudança:

1.  **Mudança Padrão:** É uma mudança de baixo risco, pré-aprovada, com procedimentos aceitos e documentados. O fato de ser padrão é que ela já está autorizada.
2.  **Mudança Normal:** É uma mudança que segue o fluxo normal de registro, avaliação e aprovação para execução.
3.  **Mudança Emergencial:** É uma mudança que pretende reparar um erro em um serviço de tecnologia da informação que está causando impacto negativo para o cliente e precisa ser corrigido rapidamente.

`⏱ 17:20`

Esses são os três tipos de mudança que podemos ter.

### Validação e Teste de Serviço

> [!definicao] Validação e Teste de Serviço
> Tem como objetivo garantir que produtos e serviços novos ou modificados atendam aos requisitos definidos.

É um conceito bem intuitivo. Não precisamos de muitas explicações sobre o assunto, pois é bem direcionado. A prática consiste em validar e confirmar que o serviço está cumprindo o que deve fazer.

### Gerenciamento de Configuração de Serviço

> [!definicao] Gerenciamento de Configuração de Serviço
> Tem como objetivo garantir que informações precisas e confiáveis sobre a configuração dos serviços e sobre os **itens de configuração** que suportam os serviços estejam disponíveis quando e onde necessários. Isso serve para sabermos quais configurações estão sendo utilizadas, principalmente nos produtos e recursos empregados para disponibilizar um serviço.

### Gerenciamento de Ativos de TI

> [!definicao] Gerenciamento de Ativos de TI
> Tem como objetivo o planejamento e gerenciamento do ciclo de vida completo de todos os **ativos de serviços de tecnologia da informação**.

### Práticas de Gerenciamento Técnico

Por fim, temos as práticas de gerenciamento técnico. A única que já vi cair em prova foi a segunda, mas isso não descarta a possibilidade das outras duas:

-   **Gerenciamento de Implantação**: Tem como objetivo gerenciar a implantação de hardware, software, documentação, processos ou qualquer outro componente de serviço novo ou alterado em ambientes de produção.
-   **Gerenciamento de Infraestrutura e Plataforma**: Tem como objetivo supervisionar a infraestrutura e as plataformas usadas por uma organização. Permite a monitoração das soluções de tecnologia disponíveis, incluindo as de terceiros.
-   **Desenvolvimento e Gerenciamento de Software**: Tem como objetivo garantir que os aplicativos atendam às necessidades das partes interessadas em termos de funcionalidade, confiabilidade, capacidade de manutenção, conformidade e auditabilidade.

### Considerações Finais

Espero que tenham acompanhado com bastante atenção as aulas de ITIL 4. É justamente isso que tem sido cobrado historicamente, desde as versões anteriores da ITIL, como ITIL v3 e ITIL v3 2011, que acompanho há muito tempo. Agora, o importante é sentar e resolver as questões.

Acompanhem nossos comentários para complementar o conhecimento e sanar possíveis falhas. Bons estudos a todos! Depois, tragam-nos o feedback e o depoimento sobre a importância deste curso para vocês. Muito obrigado, até o nosso próximo curso.

## Relacionado

- [[introducao-a-itil-4-e-gestao-de-servicos-de-ti]]
- [[itil-4-praticas-de-gerenciamento-e-suas-categorias]]
- [[itil-4-conceitos-fundamentais-e-definicoes]]
- [[itil-4-as-quatro-dimensoes-do-gerenciamento-de-servicos]]

---

## Revisão da transcrição

Termos que o Whisper errou e o glossário corrigiu — confira se algum ficou errado e ajuste `data/glossario.json`:

- `Aitio → ITIL`
