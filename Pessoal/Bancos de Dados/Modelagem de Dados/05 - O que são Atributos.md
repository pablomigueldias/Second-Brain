
Link do conteúdo: [O que são Atributos](https://www.youtube.com/watch?v=59TZc_vRpcQ&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=6)

## Atributos

- Os atributos descrevem características da entidade, como por exemplo: fabricante, modelo, cor, placa, etc.
- Os atributos possuem um tipo de dados(domínio) nome e valor específico.

## Representando Atributos

- Os atributos podem ser representados por uma elipse contendo o seu nome, ligada à entidade que qualifica
- Opcionalmente, podemos representar um atributo apenas pelo seu nome ligado à entidade, sem utilizar a elipse.

![](../IMG/Pasted%20image%2020260108143545.png)

---
## Tipos de Atributos

Os atributos podem ser de vários tipos, tais como:

- Simples
- Composto
- Multivalorado
- Determinante
- Identificador

entre outros.

---
## Atributo Simples / Atômico

Não possui características especiais, e são indivisíveis.

Ex.: Nome da empresa, CPF, CNPJ

![](../IMG/Pasted%20image%2020260108144001.png)

---
## Atributo Composto

É formado por itens menores; pode ser subdividido em outros atributos.

Ex.: Endereço da empresa

![](../IMG/Pasted%20image%2020260108144210.png)

---
## Atributo Multivalorado

Pode conter mais de um valor para um mesmo registro(informação).

Ex.: Telefone da empresa

![](../IMG/Pasted%20image%2020260108144443.png)

---
## Atributo Determinante 

Define de forma única as instâncias de uma entidade. Não podem existir duas instâncias com o mesmo valor desse atributo.

Ex.: CNPJ da empresa, Código do Produto

![](../IMG/Pasted%20image%2020260108144737.png)

---
## Atributos Identificadores ("Chaves")

Uma **Chave** identifica uma instância específica na classe de entidade
Ex.: CPF, CódigoProduto, Matrícula, ID_Setor

As chaves podem ser únicas ou não-únicas:

- Únicas: o valor dos dados da chave é único na entidade
- Não-única: Usada para agrupar instâncias de classe em categorias.

As chaves podem ser compostas, consistindo de dois ou mais atributos combinados.

---
## Exemplos de Representação de Entidades e Atributos

![](../IMG/Pasted%20image%2020260108145550.png)
![](../IMG/Pasted%20image%2020260108145601.png)

Podemos também representar uma entidade de forma textual:

**Produto(Cod_Produto,Nome_Produto,Preço,Qtde_Estoque)**
