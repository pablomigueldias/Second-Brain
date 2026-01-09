
Link do conteúdo: [Comparando Entidades e Relações](https://www.youtube.com/watch?v=CdbYZGEClLg&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=7)

## Entidade x Relação

- Uma Entidade é um conceito do mundo real, como por exemplo um Cliente ou um Produto
- Uma Relação é um conjunto de registros(tuplas) que representam um modelo de uma entidade.
- Cada registro representa uma instância de entidade, e o conjunto de todas as instâncias, com seus atributos, é chamado de Relação.

---
## Relação

Tabela bidimensional com características específicas, composta por linhas e colunas, criada a partir de uma entidade.

Características de uma relação:
- Linhas contém dados sobre instâncias de uma entidade(registros)
- Colunas contém dados sobre atributos da entidade(campos)

---
## Relação - características - cont.

- Cada célula da tabela armazena um único valor
- Todos os valores em uma coluna são do mesmo tipo(domínio)
- Cada coluna possui um nome único
- Não há duas linhas idênticas.
- As relações geralmente geram tabelas no banco.

---
## Exemplo de uma Relação

| ID_Produto | Nome_Produto | Preco_Produto |
| ---------- | ------------ | ------------- |
| 1000       | Mouse        | 15,00         |
| 1001       | Teclado      | 20,00         |
| 1002       | Webcam       | 65,00         |

> [!NOTE] Relação
> Toda Relação é uma tabela, mas nem toda tabela é uma relação.

| Cód | Mercadoria      | Qtde_Estoque | Fornecedor | Validade   |
| --- | --------------- | ------------ | ---------- | ---------- |
| 189 | Azeitona Pretas | 50           | 05         | 02/08/2026 |
| 222 | Peixe Congelado | 26           | 08         | 22/09/2026 |
| 236 | Enlatado        | 48           | 12         | 30/10/2026 |

`Cód`: Chave primária (PK)
`Fornecedor`: Chave estrangeira


