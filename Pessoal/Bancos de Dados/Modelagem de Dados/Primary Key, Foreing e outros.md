
Link do conteúdo: [Primary Key, Foreing e outros](https://www.youtube.com/watch?v=sbIT5UXTEg8&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=9)

## Chaves

uma chave consiste em uma ou mais colunas de uma relação cujos valores são usados para identificar de forma exclusiva uma linha ou conjunto de linha. Poder ser única(identifica única linha) ou não-única(identifica um conjunto de linhas).

Única(Unique): Candidata, Composta, Primária, Surrogada
Não-Única(Non-Unique): Estrangeira

---
## Chave Candidata

- Atributo ou grupo de atributos com o potencial para se tornarem uma chave primária.
- Uma chave candidata que não seja usada como chave primária será conhecida como **Chave Alternativa**

Ex.: Campos Num_Matrícula e CPF em um tabela de registro de alunos.

___
## Chave Primária

- Chave candidata escolhida para ser a chave **principal** na relação
- identifica de forma **exclusiva** os registros em uma tabela, não podendo ter repetição de valores nem tampouco valor nulo.
- Primary Key / PK

___
## Chave Estrangeira

- Coluna de uma tabela que estabelece um **Relacionamento com a Chave Primária**(PK) de outra tabela.
- É a partir da chave estrangeira(Foreign Key / FK) que sabemos com qual registro em outra tabela um registro está relacionado

___
## Chave Composta

- Chave que é composta de dois ou mais atributos(colunas)
- Geralmente empregada quando não é possível utilizar uma única coluna de uma tabela para identificar de forma exclusiva seus registros.

---
## Chave Surrogada / Substituta

- Valo numérico, único, adicionado a uma relação para servir como chave primária.
- Não possui significado para os usuários e geralmente fica escondida nas aplicações.
- As chaves substitutas são frequentemente usadas no lugar de uma chave primária composta

---
## Instruções para criação de chaves primárias e estrangeiras

- Não é possível haver valores duplicados em uma chave primária
- No geral, não é possível alterar o valor de uma chave primária
- Chaves estrangeiras são baseadas em valores de dados, classificadas como ponteiros lógicos
- Um valor de uma chave estrangeira deve corresponder a um valor existente em uma chave primária associada(ou valor de chave única). Caso contrário, deve ser nulo (NULL).
- Uma chave estrangeira deve referenciar uma chave primária ou uma coluna de chave única.

## Exemplo de chave primária e chave estrangeira

![](../IMG/Pasted%20image%2020260109105151.png)

## O conceito de Domínio

- Definir tipos de dados
- Especificar calores válidos em um campo

![](../IMG/Pasted%20image%2020260109105723.png)

