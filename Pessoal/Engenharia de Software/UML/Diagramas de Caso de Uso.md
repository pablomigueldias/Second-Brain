
Link do Conteúdo: [Diagramas Caso de Uso](https://www.youtube.com/watch?v=K-BaRfFx0mA&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=5)

 A UML fornece representação gráfica para casos de uso e atores com a sua notação padrão:

![[Pasted image 20260102111716.png]]

## Relacionamento entre Atores e Casos de Uso

Um Ator se relaciona com um Caso de Uso por meio de um relacionamento de Associação:

![[Pasted image 20260102111900.png]]

## Relacionamento entre Casos de Uso

Abaixo temos as representações de relacionamentos entre caos de uso:

![[Pasted image 20260102112035.png]]

# Relacionamento de Inclusão

Um caso de uso inclui de forma incondicional outro caso de uso

![[Pasted image 20260102112352.png]]

Relacionamento de Extensão

Um caso de uso pode estender a funcionalidade de um outro caso de uso. Comportamental opcional.

![[Pasted image 20260102112523.png]]

Podemos também usar Pontos de Extensão e Notas Explicativas:

![[Pasted image 20260102112646.png]]

## Relacionamento de Generalização

A generalização ocorre quando um ator ou caso de uso possui as mesmas características de um elemento base, porém com características específicas.

![[Pasted image 20260102112942.png]]

## Relacionamentos entre Atores

Atores podem se relacionar entre si por meio de Generalização.

![[Pasted image 20260102113226.png]]

## Boas práticas ao criar diagramas de casos de uso

- Nomes: Use nomes únicos, identificáveis e capazes de identificar seu propósito
- Fatore variantes, aplicando comportamentos  a outros casos que estendem um caso de uso
- Sempre descreve o fluxo de eventos da maneira mais clara possível, de modo que observadores externos possam compreendê-lo.
- Exiba somente os casos de uso importantes para a compreensão do comportamento do sistema (ou parte dele)
- Idem com relação aos atores.

- Distribua os elementos no diagrama de forma a minimizar o cruzamento de linhas, que interfere na compreensão.
- Organize os elementos que têm comportamentos e papéis relacionados próximos entre si.
- Faça uso de notas e cores diferentes como indicação visuais para ressaltar características importantes
- Caso relacionamentos de inclusão e extensão fiquem muito complicados, os exiba em outro diagrama complementar.