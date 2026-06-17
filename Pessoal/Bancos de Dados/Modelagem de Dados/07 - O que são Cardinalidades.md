
Link do conteúdo: [O que são Cardinalidades](https://www.youtube.com/watch?v=OVBFFe4-jSM&list=PLucm8g_ezqNoNHU8tjVeHmRGBFnjDIlxD&index=10)

## Cardinalidade

A cardinalidade diz respeito ao número de itens que se relacionam nas entidades.
A cardinalidade pode ser máxima ou mínima, significando respectivamente os números mínimos e máximo de instâncias de cada entidade associadas no relacionamento.

`Cardinalidade Máxima`: Trata-se do número máximo de instâncias de entidade que podem participar em um relacionamento. Pode ser 1 ou N (muitos).

`Cardinalidade Mínima`: Número mínimo de instâncias de entidade que devem obrigatoriamente participar em um relacionamento; zero é participação opcional e um é obrigatória.


---
## Simbologia para Cardinalidades

Usando a notação de Peter Chen:

![](../IMG/Pasted%20image%2020260109145835.png)
## Simbologia para Cardinalidades

![](../IMG/Pasted%20image%2020260109145953.png)

---
## Exemplo de Cardinalidade

![](../IMG/Pasted%20image%2020260109150214.png)

Cardinalidade Mínima: Um cliente para uma encomenda

Cardinalidade Máxima: Um cliente para muitas encomendas

---
## Cardinalidade: Notação Peter Chen

![](../IMG/Pasted%20image%2020260109150550.png)

---
## Relacionamento Binário um-para-um

`1:1`

Uma instância de entidade única em uma entidade relacionada com uma instância de entidade única em outra entidade.

![](../IMG/Pasted%20image%2020260109150738.png)

Usando a notação de Peter Chen:

![](../IMG/Pasted%20image%2020260109151007.png)
## Relacionamento Binário um-para-muitos

`1:N`

Uma instância de entidade única em uma classe de entidade está relacionada a muitas instâncias de entidade em outra classe de entidade.

![](../IMG/Pasted%20image%2020260109151212.png)

Usando a notação de Peter Chen:

![](../IMG/Pasted%20image%2020260109151436.png)
## Relacionamento Binário muitos-para-muitos

`N:M`

Muitas instâncias em uma entidade estão relacionadas a muitas instâncias de entidade em outra entidade.

![](../IMG/Pasted%20image%2020260109151634.png)

Usando a notação Peter Chen

![](../IMG/Pasted%20image%2020260109151823.png)

---
## Desmembrando Relacionamento Muitos-para-muitos

![](../IMG/Pasted%20image%2020260109151914.png)
