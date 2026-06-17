
Link do conteúdo: [Normalização e Anomalias - Conceitos](https://www.youtube.com/watch?v=NpG1Xt8LB_c&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=15)

## Anomalias de Atualização

- Anomalias são problemas que ocorrem em bancos de dados mal planejados e não-normalizados, geralmente ocorrendo por excesso de dados armazenados em uma mesma tabela.
- São causadas pelas dependências parciais e transitivas.
- As anomalias de atualização são classificadas em anomalias de inserção, de exclusão e de modificação.

---
## Anomalia de inclusão

Anomalia de Inclusão: Não deve ser possível adicionar um dado a não ser que o outro dado esteja disponível. Por exemplo, não deve ser permitido cadastrar um novo livro sem que um autor já esteja cadastrado.

## Anomalia de Exclusão

Anomalia de Exclusão: ao excluirmos um registro, dados referentes em outra tabela são excluídos. Por exemplo, se excluirmos um autor, os livros desse autor devem ser excluídos também.

## Anomalia de Modificação

Anomalia de Modificação: ao alterar um dado em uma tabela, dados em outras tabelas precisam ser alterados.
Por exemplo, se o código de um autor for modificado, esse código deve ser modificado na tabela de autores e na de livros também, para manter o relacionamento entre livros e seus autores corretos.

## Eliminar anomalias

Projetar os esquemas de relações(tabelas) no banco de dados de modo que nenhuma anomalia de inserção, exclusão ou modificação esteja presente na relações. Para isso, usamos o processo de **Normalização**

---
## Normalização

Normalização consiste em um processo de análise de uma relação para assegurar que seja bem formada.
Decompor relações com **anomalias** para produzir relações menores e bem-estruturadas.
Ou seja, em uma relação normalizada podemos inserir, excluir ou modificar registros sem criar anomalias.

- O processo de normalização, proposto por Codd em 1972, aplica a um esquema de relação uma série de testes para certificar que ela satisfaça uma Forma Normal (FN)
- Codd propôs originalmente 3 formas normais: 1ª, 2ª e 3ª FNs.
- Posteriormente, a 3FN foi revisada e uma definição mais robusta foi proposta por Boyce e Codd, denominada Foma Normal de Boyce-Codd (FNBC)

## Objetivo da Normalização

Analisar esquemas de relação(tabelas) com base em suas dependências funcionais e chaves primárias para:

1. Minimizar redundâncias
2. Minimizar anomalias de inserção, exclusão e modificação

As relações são decompostas em esquemas de relação menores que atendem aos testes de forma normal.

O ideal é que o projeto do bando de dados relacional alcance a FNBC ou a 3FN para cada tabela.
Não é adequado normalizar apenas até a 1FN ou à 2FN, pois na verdade essas formas normais são usadas para se chegar à 3FN ou FNBC.