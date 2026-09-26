---
titulo: "SGBD: Atores Indiretos e Requisitos Operacionais"
tags: [sgbd, banco-de-dados, sistema, organizacao, ferramentas, conceitos, fundamentos]
data: 2026-09-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 5
conceitos: [Atores indiretos, Design de sistema, Implementação de sistema, Operação e manutenção, Desenvolvedores de ferramentas, Requisitos de operacionalização, Ambiente computacional propício, Disponibilidade do sistema]
---

# SGBD: Atores Indiretos e Requisitos Operacionais

> [!resumo] Do que se trata
> Esta aula aborda os atores indiretamente envolvidos no contexto de SGBDs, detalhando suas funções no suporte e operacionalização do sistema. Ela explora o papel do design e implementação do sistema, da operação e manutenção, e dos desenvolvedores de ferramentas. A nota enfatiza a importância de um ambiente computacional propício e de requisitos bem definidos para garantir a disponibilidade e o propósito do SGBD.

## Para lembrar

- **Atores indiretos no contexto de SGBDs incluem o design do sistema, a implementação do SGBD, a operação e manutenção, e os desenvolvedores de ferramentas.**
- **O propósito do SGBD é fornecer e disponibilizar dados, e os atores indiretos garantem o ambiente e suporte para essa disponibilidade.**
- **O designer e a implementação do sistema estão relacionados aos módulos e interfaces do SGBD como um pacote, incluindo requisitos de sistema operacional e pacotes necessários para seu funcionamento.**
- **O setor de operação e manutenção é responsável pelo hardware e software do SGBD, assegurando que o ambiente computacional opere bem para o sucesso do sistema.**
- **Desenvolvedores de ferramentas criam utilitários opcionais para diversos fins, como performance, modelagem e análise de dados, associados ao contexto do SGBD.**

## O que esta nota responde

- Quem são os atores indiretamente envolvidos na operação de um SGBD?
- Quais são as responsabilidades do design e da implementação de um sistema de suporte ao SGBD?
- Qual o papel da equipe de operação e manutenção e dos desenvolvedores de ferramentas no contexto de SGBDs?

## Conceitos

**Atores indiretos** · **Design de sistema** · **Implementação de sistema** · **Operação e manutenção** · **Desenvolvedores de ferramentas** · **Requisitos de operacionalização** · **Ambiente computacional propício** · **Disponibilidade do sistema**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | Atores Indiretos e Requisitos Operacionais | ▪▪ |
| `04:20` | Suporte ao Consumo de Dados | ▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Propósito do SGBD** | Fornecer e disponibilizar dados. |

## Pegadinhas

- Um SGBD online funcionando tranquilamente não garante o consumo de dados se o ambiente completo (API, front, back, servidor HTTP) não estiver operacional.

## Teste-se

<details><summary>Quais são os quatro tipos de atores indiretos relacionados a SGBDs mencionados na aula?</summary>

Os quatro tipos são: design do sistema, implementação do SGBD, operação e manutenção, e desenvolvedores de ferramentas.

</details>

<details><summary>Qual é o propósito fundamental de um SGBD, segundo a aula?</summary>

O propósito fundamental do SGBD é fornecer e disponibilizar dados.

</details>

<details><summary>Qual a principal responsabilidade do setor de Operação e Manutenção?</summary>

O setor de Operação e Manutenção é responsável pelo hardware e software do SGBD, garantindo que o sistema operacional e o hardware operem bem.

</details>

<details><summary>O que os desenvolvedores de ferramentas criam no contexto de SGBDs?</summary>

Eles criam ferramentas opcionais para diversos fins, como performance, modelagem e análise de dados, associadas ao contexto de SGBD.

</details>

<details><summary>Por que o ambiente computacional completo é importante para a operacionalização do SGBD?</summary>

Um SGBD funcionando não é suficiente se o ambiente completo, como a API, o front-end, o back-end e o servidor HTTP, não estiver operacional para permitir o acesso e consumo dos dados.

</details>

## Conteúdo

`⏱ 00:00`

### Atores Indiretos no Contexto de SGBDs

Falaremos agora de um outro cenário, de outros atores que estão relacionados a banco de dados, mas não estão diretamente ligados aos cenários de SGBD.

Alguns atores estão fora desse contexto. São eles:
- O design do sistema (não do SGBD em si, mas o sistema que dá suporte ao SGBD).
- A implementação do SGBD (ou seja, quem vai realizar a instalação e os requisitos de todo o processo relacionado ao sistema).
- A operação e manutenção.
- Os desenvolvedores de ferramentas.

Esses são os que estão ligados de maneira indireta ao contexto de SGBDs. São as pessoas que mantêm o SGBD disponível para que os usuários possam consumir as informações.

> [!definicao] Propósito do SGBD
> O propósito do SGBD é fornecer e disponibilizar dados.

Por sua vez, essas pessoas fornecem todo um ambiente, todo um suporte para que haja uma disponibilidade desse sistema, para que ele cumpra seu propósito.

### Design e Implementação do Sistema

Tanto o **designer de sistema** quanto a **implementação de sistema** estão relacionados aos módulos e interfaces do SGBD como um pacote.

O que eu preciso de requisito para o meu SGBD rodar? Qual é o sistema operacional? O que falta na minha máquina?

> [!exemplo] Requisitos para instalação do MySQL
> Por exemplo, se a gente vai instalar o `MySQL`, eu preciso de um `VS Code` instalado na máquina. Eu preciso de uma série de pacotes instalados ali. Durante o processo de instalação, a gente vai estar identificando esses pacotes e conversando um pouquinho sobre eles.

Há todo um aparato, na verdade, uma série de requisitos que fornecem um ambiente propício, o ambiente computacional propício para o SGBD operar. Nesse sentido, nós temos segurança, recuperação, ou a partir em camadas, diversos módulos são necessários para que haja um processamento também adequado, ou seja, que as *queries* sejam processadas e que haja o poder computacional para poder suportar alguma demanda, a demanda necessária. Enfim, uma série de aspectos relacionados ao ambiente que vai manter um SGBD.

### Operação e Manutenção

O setor de **operação e manutenção** já é responsável pelo hardware e software do SGBD.

Anteriormente, eu falei do que vai dar suporte com relação ao SGBD em si. E aqui, como que eu vou manter o meu sistema operacional e o meu hardware operando bem, para que tudo isso daqui seja bem-sucedido?

### Desenvolvedores de Ferramentas

Já o **desenvolvedor de ferramentas**, são os *devs*, são os desenvolvedores. Eles criam ferramentas opcionais para diversos fins, como, por exemplo, a parte de performance, modelagem, análise dos dados.

Associados ao contexto de SGBD, que está atrelado a dados, nós temos muitas vezes o cara da modelagem sendo um cientista, a análise vai ser uma pessoa, um analista de Power BI, ou uma análise de dados, e performance também. Nós temos aí, na verdade, um outro cenário: eu vou trabalhar o meu sistema para que ele seja performático, utilizando, por exemplo, sistemas `OLTP`.

### Requisitos para Operacionalização

Temos uma série de informações, uma série de requisitos que precisam de atenção para que o nosso sistema, para que o nosso ambiente, ele possa ser operacionalizado. Não é somente modelar; a parte de segurança, a parte de performance, identificação de, às vezes, uma chamada mais direcionada ao conteúdo, realizando como se fosse um *cache* daquela informação, para que ela possa ser recuperada mais rápido. Às vezes é uma informação sensível, ou então uma informação que é muito demandada.

`⏱ 04:20`

Às vezes é uma informação sensível, ou então uma informação que é muito demandada. Diversos aspectos relacionados ao SGBD, mas que não estão diretamente ligados a ele, precisam ser pontuados. Essas pessoas são as responsáveis por eles, de maneira que o nosso ambiente seja bem configurado e tudo corra bem.

> [!exemplo] A importância do ambiente completo
> Não adianta ter um SGBD online funcionando tranquilamente se:
> - A API via front não acessa o back, e o back não consegue fazer a integração com o banco.
> - Há algum problema no servidor HTTP, que não está processando as chamadas e as requisições HTTP.

Existe todo um cenário mais complexo que precisa dar suporte para que esses dados possam ser consumidos.

## Relacionado

- [[sgbd-atores-tipos-de-usuarios-e-finalidade]]
- [[sgbd-etapas-estrutura-e-fases]]
- [[bancos-de-dados-definicao-acesso-e-escala]]
- [[sgbd-abordagens-e-caracteristicas-essenciais]]

---

## Revisão da transcrição

<details><summary>1 frase(s) descartadas como ruído de vídeo (inscrição, saudação, despedida)</summary>

- Olá, !

</details>
