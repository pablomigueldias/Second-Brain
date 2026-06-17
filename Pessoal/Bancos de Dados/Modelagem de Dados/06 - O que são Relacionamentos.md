
Link do conteúdo: [O que são Relacionamentos](https://www.youtube.com/watch?v=KSw0rTGEwPI&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=8)

## Relacionamentos

- A entidades podem ser conectadas entre si por meio de Relacionamentos. Trata-se de uma estrutura que indica a associação de elementos de uma ou mais entidades.

---
## Porque precisamos de relacionamentos?

- Como os dados de diferentes entidades são armazenados em tabelas distintas, geralmente precisamos combinar duas ou mais tabelas para responder às perguntas específicas dos usuários.
- Por exemplo, podemos querer saber quais produtos, em qual quantidade, foram adquiridos por um cliente em particular. Precisaremos então de dados das tabelas de clientes, de pedido e produtos para obter essa informação.

## Representando relacionamentos

- Representamos um Relacionamento em um DER por meio de um losango que conecta uma ou mais Entidades:

![](../IMG/Pasted%20image%2020260109095230.png)

## Grau de um Relacionamento 

O grau de um relacionamento define o número de entidades que participam do relacionamento. Assim, um relacionamento pode ser:

- Unário
- Binário
- Ternário

Os relacionamentos mais comuns são os de grau (binário) 

## Relacionamento Unário (Recursivo)

![](../IMG/Pasted%20image%2020260109095838.png)
## Relacionamento Binário

![](../IMG/Pasted%20image%2020260109100022.png)
## Relacionamento Ternário

![](../IMG/Pasted%20image%2020260109100206.png)

---
## Relacionamento entre Tabelas

Uma tabela é relacionada com outras tabelas. Por exemplo, um produto é vendido em uma loja.

![](../IMG/Pasted%20image%2020260109100509.png)

O grau de um Relacionamento indica o número de entidades envolvidas no relacionamento, como por exemplo unário, binário, ternário.

## Efetuando relacionamento entre múltiplas tabelas

-  Cada linha de dados em uma tabela deve ser identificada de uma forma única usando-se uma Chave Primária (identificador exclusivo).
- Usamos uma Chave Estrangeira para relacionar os dados entre múltiplas tabelas.
- Usamos para isso o relacionamento entre chave primária de uma tabela com a chave estrangeira em outra tabela.

