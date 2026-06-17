
Link do conteúdo: [Primeira Forma Normal](https://www.youtube.com/watch?v=eRaAMNjCFYw&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=16)

Definida historicamente para reprovar atributos multivalorados, compostos e suas combinações.
O domínio de um atributos deve incluir apenas valores atômicos(indivisíveis), e o valor de qualquer atributo em uma tupla deve ser único valor do domínio desses atributos.

Uma tabela está na 1ª forma normal quando:
- Somente possui valores atômicos
- Não há grupos de atributos repetidos(há apenas um dado por coluna nas linhas)
- Existe uma chave primária
- Relação não possui atributos multivalorados ou relações aninhadas

- Uma tabela está na 1ª forma normal se somente houverem valores atômicos no domínio de seus atributos.
- Um valor atômico é um valor indivisível.
- Como exemplo, um campo de Endereço possui subdomínios Rua,Número e CEP. Esses itens devem ser separados no processo e normalização.
- Cada informação deve ser colocada em um campo diferente.
---
## Dados Atômicos

- Elementos de dados que representam o nível mais baixo de detalhamento.
- Então, campos não-atômicos são aqueles que podem ser subdivididos em mais de um campo, pois eles escondem detalhes, como por exemplo o nome de uma pessoa, que contém o primeiro nome e o sobrenome.

---
## Normalizando tabela até 1FN

![](../IMG/Pasted%20image%2020260113162057.png)
![](../IMG/Pasted%20image%2020260113162453.png)