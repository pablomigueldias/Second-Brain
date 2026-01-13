
Link do conteúdo: [Normalização - Segunda Forma normal](https://www.youtube.com/watch?v=6ER9lWOk-cY&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=17)

- Baseada no conceito de Dependência Funcional Total.
- Um esquema de Relação R está 2FN se cada atributo não-chave de R for total e funcionalmente dependente da PK de R.
- para testar a 2FN, testamos as dependências funcionais cujos atributos fazem parte da chave primária.
- Caso a PK tenha um único atributo, esse teste não precisa ser aplicado.

Uma tabela está na 2ª FN se:
- Está na 1ª FN
- Todos os atributos não-chave são funcionalmente dependentes de todas as partes da chave primária.
- Não existem dependências parciais.
- Caso contrário, deve-se gerar uma nova tabela com os dados.

Um atributo-chave é um que é uma PK ou parte de uma PK composta.

---

Deve-se criar uma nova relação para cada chave PK ou combinação de atributos que forem **determinantes em uma dependência funcional**.
Esse atributo será a PK na nova tabela.
Mova os atributos não-chave dependentes desta PK para a nova tabela.

## Normalizando tabela até 2FN

![](../IMG/Pasted%20image%2020260113171539.png)

![](../IMG/Pasted%20image%2020260113172020.png)