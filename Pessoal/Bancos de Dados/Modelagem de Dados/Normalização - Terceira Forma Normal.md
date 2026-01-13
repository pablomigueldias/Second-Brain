
Link do conteúdo: [Terceira Forma Normal](https://www.youtube.com/watch?v=usA8QKvEHWw&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=18)

- Baseada no conceito de Dependência Transitivas. 
- A relação não deve ter um atributo não-chave determinado funcionalmente por outro atributo não-chave sobre a PK
- Deve-se decompor e montar uma nova relação que inclua os atributos não-chave que determinam funcionalmente outros atributos não-chave

Uma tabela está na 3FN se:

- Estiver na 2FN
- Não existirem **dependências transitivas**
- Uma tabela está na Terceira Forma normal se ela estiver na segunda forma normal e se nenhuma coluna não-chave depender de outra coluna não-chave.

uma dependência transitiva em uma tabela é uma dependência funcional entre dois ou mais atributos não-chave.

---

Para cada atributo (ou grupo) não-chave que for um determinante na relação, crie uma nova tabela.
Esse atributo será a PK na nova relação.
Mova então todos os atributos que são dependentes funcionalmente do atributo chave para a nova tabela.
O atributo (PK na nova relação) fica também na tabela original, e servirá como uma chave estrangeira para associar as duas relações.

## Normalizando tabela até 3FN

![](../IMG/Pasted%20image%2020260113174353.png)

![](../IMG/Pasted%20image%2020260113174607.png)

---

## Passos da Normalização - Resumido

![](../IMG/Pasted%20image%2020260113175049.png)

