
Link do conteúdo: [Relacionamento Classes](https://www.youtube.com/watch?v=IJtQWLnHvcQ&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=3)


## Relacionamento de Dependência

Dependência Fraca, usualmente transiente, que ilustra que uma classe usa informações e serviços de outra classe em algum momento, dependendo dela.

Do tipo "Classe A depende da Classe B"

![[Pasted image 20260101214612.png]]

## Multiplicidade 

A multiplicidade é usada para determinar o número mínimo e o número máximo de objetos envolvidos na associação, de cada lado, e também pode especificar o nível de dependência entre os objetos.

| Multiplicidade | Siginificado                                                                                             |
| -------------- | -------------------------------------------------------------------------------------------------------- |
| 0...1          | No mínimo zero e no máximo um. Indica não obrigatoriedade do relacionamento                              |
| 1...1          | Um e somente um. Um objeto da classe se relaciona com um objeto de outra                                 |
| 0...*          | Mínimo nenhum e no máximo muitos.                                                                        |
| 1...*          | Mínimo um e no máximo muitos.                                                                            |
| *              | Muitos                                                                                                   |
| 2...7          | Mínimo 2 e no máximo 7. Ou seja, no mínimo duas e no máximo sete instâncias envolvidas no relacionamento |

## Relacionamento de Associação

Relacionamento mais forte do que a dependência, indica que a classe mantém uma referência a outra classe ao longo do tempo. As associações podem conectar mais de duas classes

Do tipo "Classe A tem uma Classe B"

![[Pasted image 20260101215618.png]]

A Associação pode ter um nome e possui multiplicidade

> [!NOTE] Navegabilidade
> A seta representa a Navegabilidade, que identifica o sentido em que as informações são transmitidas entre os objetos das classes relacionadas ( relacionamento unidirecional).
> Navegabilidade não é obrigatória no diagrama(relacionamento bidirecional)

## Associação Ternária

Associação que conecta objetos de três classes. um losango indica o ponto de convergência(conexão) das classes envolvidas.

![[Pasted image 20260101220238.png]]

Na prática, podemos ter associações n-árias, conectando quaisquer número de objetos de classes.

## Relacionamento de Agregação

Relacionamento mais específico do que a associação, indica que uma classe é um contêiner ou uma coleção de outras classes. As classes contidas não dependem do contêiner - assim , quando o contêiner é destruído, as classes continuam existindo.

Do tipo "Classe A possui uma Classe B"

![[Pasted image 20260101220848.png]]
## Relacionamento de Composição

Variação mais específico da agregação, este relacionamento indica uma dependência de ciclo de vida forte entre as classes, de modo que quando um contêiner é destruído, seu conteúdo também o é.

Do tipo "Classe A é parte da classe B"

![[Pasted image 20260101221046.png]]

## Relacionamento de Generalização / Especialização

Relacionamento entre itens gerais (superclasses/classes - mãe) e tipos mais específicos desses itens (subclasses / classes - filha). Representa a Herança entre as classes.

Do tipo "Classe A é um tipo de Classe B"

![[Pasted image 20260101221410.png]]

A classe filha herda propriedades da classe mãe, principalmente atributos e operações, e pode possuir seus próprios.

## Classe Associativa

São produzidas quando ocorrem associações com multiplicidades muitos (*) em todas as extremidades, no geral, existem atributos da associação que não podem ser armazenados em nenhuma das classes envolvidas.


![[Pasted image 20260101221828.png]]


## Resumo da notação de Relacionamentos

![[Pasted image 20260101222132.png]]

## Boas práticas ao criar diagramas de classe

- O nome da classe deve ser significativo, descrevendo um aspecto real do sistema
- Os relacionamentos entre os elementos devem ser identificados antes de criar o diagrama
- Devem ser especificados os atributos e operações de cada classe
- Sempre que necessário, acrescente anotações para ajudar a definir aspectos das classes ou seus relacionamentos.