
Link do conteúdo: [Dependências (Funcional, Multivalorada, Transitiva)](https://www.youtube.com/watch?v=koe4GVN_83M&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=14)

## Dependência Funcional 

Seja E uma entidade, e X e Y dois atributos quaisquer de E. Dizemos que Y é funcionalmente dependente de X se e somente se cada valor de X tiver associado a ele exatamente de Y.

Simbolicamente:

![](../IMG/Pasted%20image%2020260113145122.png)

Que lemos com "X determina funcionalmente Y".

## Exemplo

Ex.: O prazo de entrega de um pedido depende do número do pedido considerado:

![](../IMG/Pasted%20image%2020260113145352.png)

O atributo que determina o valor é chamado de **Determinante**.
O outro atributo é chamado de **Dependente**.

Um chave primária em uma relação determina funcionalmente todos os outros atributos não-chave na linha.

---
## Dependência Funcional Total

Em uma relação com uma PK composta, um atributo não-chave que depende dessa PK como um todo, e não somente de parte dela, é dito como possuindo Dependência Funcional Total.

## Exemplo

![](../IMG/Pasted%20image%2020260113150014.png)

Aqui, Quant_produto depende tanto de Num_Pedido quanto Cod_Produto, ao mesmo tempo.

---
## Dependência Funcional Parcial

Uma dependência Funcional Parcial

Uma dependência funcional é parcial quando os atributos não-chave não dependem funcionalmente de toda a PK quando esta for composta.
Ou seja existe uma dependência funcional, mas somente de uma parte da chave primária.

## Exemplo

![](../IMG/Pasted%20image%2020260113150412.png)

Campo Nome_Disciplina é dependente de Cod_Disciplina, mas não do ID_Aluno

---
## Dependência Funcional Transitiva

Ocorre quando um campo não depende diretamente da chave primária da tabela(nem mesmo parcialmente), mas depende de um outro campo não-chave.

## Exemplo

![](../IMG/Pasted%20image%2020260113150851.png)

No exemplo, o atributo Nome_Vendedor depende funcionalmente do Cód_vendedor, que não é chave primária na tabela. ja o campo Prazo_Entrega depende da PK, Num_Pedido

---
## Dependência Multivalorada

Ocorre quando, para cada valor de um atributo A, existe um conjunto de valores para outro atributos B e C que estão associados a ele, mas são independentes entre si.
Representamos a dependência multivalorada assim:

![](../IMG/Pasted%20image%2020260113151347.png)

Onde B é a coluna que depende de A.

## Exemplo

![](../../../Pasted%20image%2020260113151505.png)

Ano e Cor são independente entre si e dependem do modelo do carro. Essas duas colunas são dependentes multivaloradas do modelo