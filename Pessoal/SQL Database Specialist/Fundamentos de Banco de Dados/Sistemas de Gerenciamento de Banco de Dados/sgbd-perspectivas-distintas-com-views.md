---
titulo: "SGBD: Perspectivas Distintas com Views"
tags: [sgbd, banco-de-dados, conceitos, sql, organizacao, modelagem-de-dados]
data: 2026-09-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 6
conceitos: [SGBD, Views, Query, Read-only, Perspectivas de dados, Agregação de dados, Tabelas, Transcript acadêmico]
---

# SGBD: Perspectivas Distintas com Views

> [!resumo] Do que se trata
> Views são uma funcionalidade essencial dos SGBDs que permitem criar perspectivas personalizadas de dados para diferentes usuários. Elas são visões virtuais geradas por queries, combinando e agregando informações de múltiplas tabelas. Com views, é possível simplificar a visualização de dados, excluindo informações irrelevantes e apresentando apenas o que é necessário para cada setor ou perfil de usuário.

## Para lembrar

- **Views são uma das vantagens do SGBD, fornecendo perspectivas distintas de um mesmo conjunto de dados.**
- **Uma view é uma visão virtual de dados, criada a partir de um conjunto de duas ou mais tabelas.**
- **Views permitem selecionar, agregar ou combinar informações específicas de diferentes tabelas através de uma query, retornando uma visão personalizada.**
- **Uma view pode ser `read-only` (apenas leitura), garantindo que a estrutura original dos dados não seja alterada.**
- **Views facilitam o gerenciamento de informações entre grupos distintos, permitindo que cada setor visualize apenas os dados relevantes para suas necessidades.**

## O que esta nota responde

- O que são views em um SGBD e qual sua principal função?
- Como as views contribuem para a segurança e personalização do acesso aos dados?
- Uma view pode ser utilizada para modificar os dados originais?

## Conceitos

**SGBD** · **Views** · **Query** · **Read-only** · **Perspectivas de dados** · **Agregação de dados** · **Tabelas** · **Transcript acadêmico**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | SGBD views: conceito e exemplos | ▪▪ |
| `04:40` | Views: agregação e exclusão de dados | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **View** | Uma visão virtual de dados, criada a partir de um conjunto de tabelas (duas ou mais). Ela permite selecionar informações específicas, agregá-las ou combiná-las de diferentes tabelas, processando-as através de uma `query` para retornar uma visão personalizada. Essa visão pode ser `read-only` (apenas leitura). |
| **View** | Criada a partir de uma `query` (processamento de consulta) para agregar informações, refletindo a estrutura que o usuário está esperando, e excluindo dados que não são necessários ou que não precisam ser visualizados naquele momento. |

## Teste-se

<details><summary>Qual é uma das principais vantagens que o SGBD oferece com as views?</summary>

O SGBD oferece a capacidade de fornecer perspectivas distintas de um mesmo conjunto de dados através das views. Isso é útil em ambientes colaborativos onde diferentes áreas precisam de visões personalizadas dos dados.

</details>

<details><summary>O que é uma view, de acordo com a aula?</summary>

Uma view é uma visão virtual de dados, criada a partir de um conjunto de tabelas. Ela processa informações através de uma `query` para retornar uma visão personalizada, que pode ser apenas leitura (`read-only`).

</details>

<details><summary>Cite um exemplo de como as views podem simplificar a visualização de dados para um usuário.</summary>

Em um cenário de matrícula, um aluno pode não precisar de todas as informações detalhadas de um curso. Uma view pode exportar apenas o nome do curso, seu número e os pré-requisitos, simplificando a visualização para o que é relevante.

</details>

<details><summary>Qual a função de uma view em relação à agregação e exclusão de dados?</summary>

Uma view é criada para agregar informações e refletir a estrutura que o usuário espera. Ela também serve para excluir dados que não são necessários ou que não precisam ser visualizados em um determinado momento.

</details>

<details><summary>Em que tipo de ambiente a utilização de um SGBD com views se torna mais relevante?</summary>

A utilização de um SGBD com views é mais relevante em um ambiente colaborativo. Nele, diversas pessoas de áreas distintas estão interessadas nos dados e demandam perspectivas personalizadas.

</details>

## Conteúdo

`⏱ 00:00`

### Perspectivas Distintas com Views

Uma das vantagens mais interessantes que o `SGBD` possui é a capacidade de fornecer perspectivas distintas de um mesmo conjunto de dados, as chamadas **views**.

Raramente você será a única pessoa a utilizar um `SGBD`. Exceto se for um cientista de dados solo ou freelancer, e mesmo nesse cenário a utilização de um `SGBD` pode ser questionável. No entanto, em um ambiente colaborativo, diversas pessoas estarão interessadas nos dados, mas essas pessoas são de áreas distintas. Muitas vezes, um dado é irrelevante para uma área específica, ou até mesmo restrito à sua visualização.

Pense em um cenário onde você tem pessoas da educação, do marketing, de vendas, do planejamento e do financeiro. São áreas e setores distintos, interessados no contexto da companhia, por exemplo, no e-commerce ou na venda de produtos. Cada um tem seu cenário, suas metas e seus relatórios a serem feitos, o que demanda perspectivas distintas do mesmo contexto.

Vamos citar um exemplo simplificado para elucidar essa necessidade:

| Setor      | Dados de Interesse                               |
| :--------- | :----------------------------------------------- |
| Educação   | Nome, Matrícula, Matéria, Sala                   |
| Financeiro | Mensalidade, Situação de atraso                  |
| Vendas     | Data de Início, Curso Extra                      |

A área de Vendas, por exemplo, pode se interessar por "Curso Extra" porque talvez haja algum tipo de formação que seja interessante para o perfil do aluno. Baseado nos cursos extras que o aluno faz, a universidade pode oferecer formações de sua autoria ou da própria instituição.

#### O que são Views?

> [!definicao] View
> Uma **view** é uma visão virtual de dados, criada a partir de um conjunto de tabelas (duas ou mais). Ela permite selecionar informações específicas, agregá-las ou combiná-las de diferentes tabelas, processando-as através de uma `query` para retornar uma visão personalizada. Essa visão pode ser `read-only` (apenas leitura).

Através de uma `view`, é possível excluir determinadas informações ou agregar dados de diferentes fontes. Isso facilita o gerenciamento de informações entre grupos distintos, permitindo que cada setor visualize apenas os dados relevantes para suas necessidades. Por exemplo, uma coluna pode pertencer a duas tabelas, outra a apenas uma, e outra a uma terceira, e a `view` as combina de forma lógica.

> [!exemplo] Simplificando dados de curso para o usuário
> Imagine que você tem uma tabela com informações detalhadas sobre cursos, incluindo:
> - Nome do curso
> - Número do curso
> - Quantidade de créditos
> - Departamento associado
> - Pré-requisitos
>
> No entanto, um usuário, como um aluno fazendo a matrícula, não está interessado em todas essas informações. À primeira vista, ele só quer saber o nome do curso, sua identificação e os pré-requisitos associados.
>
> A partir de uma `query`, é possível processar as informações e gerar uma `view` que exporta para o usuário apenas o curso, o número e os pré-requisitos, simplificando a visualização e focando no que é relevante para ele.

> [!exemplo] O `transcript` acadêmico
> Um `transcript` (histórico escolar) é um exemplo de agregação de informações de três entidades distintas:
> - Estudante
> - Grade (curricular)
> - Sessão (quando a disciplina foi ofertada)
>
> O estudante, por si só, já possui suas informações...

`⏱ 04:40`

O estudante, por si só, já fala... E aqui, o `grade report` está associado ao número do estudante, à sessão em que ele está sendo identificado e à grade.

O que estamos puxando aqui? O número do estudante, o nome do estudante, o número do curso, a grade, o semestre, o ano e a sessão.

O ID da sessão está relacionado ao `grade report`. O ano está relacionado à sessão, e o semestre também está dentro da coluna `sessão` na entidade `sessão grade`. O número do curso está presente nessa [entidade].

Nós temos, na verdade, um agregado de informações, algumas das quais não são necessárias ou que eu não preciso visualizar naquele momento.

> [!definicao] View
> Uma **view** é criada a partir de uma `query` (processamento de consulta) para agregar informações, refletindo a estrutura que o usuário está esperando, e excluindo dados que não são necessários ou que não precisam ser visualizados naquele momento.

## Relacionado

- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[../Introdução a Banco de Dados/bancos-de-dados-da-evolucao-ao-big-data]]
- [[../Introdução a Banco de Dados/bancos-de-dados-definicao-acesso-e-escala]]
- [[sgbd-natureza-autodescritiva-esquema-e-catalogo]]
