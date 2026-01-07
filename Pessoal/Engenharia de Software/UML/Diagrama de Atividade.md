
Link do conteúdo: [Diagrama de Atividades](https://www.youtube.com/watch?v=_1vHj_j3zDY&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=10)

## Diagrama de Atividade

- Tipo de diagrama comportamental que representa graficamente o fluxo de controle de uma atividade para outra, com descrição de ações passo-a-passo em um sistema.
- Especifica a transformação de entradas em saídas por meio de uma sequência controlada temporal de ações.
- Semelhante a um fluxograma, porém com suporte a concorrência(paralelismo) e sincronismo de atividades.
- Variação do diagrama de estados, que permite modelar comportamento baseado em fluxo.

### Conceito-Chave

`Atividade` é um processo de negócio, como por exemplo a venda de um produto online. Muitas vezes descreve a implementação de um caso de uso.

Uma `ação` é um passo individual(atômico) dentro de uma atividade, como por exemplo a adição de um produto a um carrinho de compras.

## Para que serve um diagrama de atividade?

- Mostrar interações entre objetos
- Expressar como as ações são executadas
- O que cada ação faz- mudança nos estados dos objetos
- Quando as ações são executadas(sequência)
- Onde e que realiza as ações.

Seu emprego mais comum é na captura de trabalhos que vão ser executados quando uma operação específica do sistema é disparada(ação).

Muito úteis para modelagem de fluxos de trabalho e de processos.

## Elementos de um diagrama de atividade

- `Nó inicial`: Ponto de início da atividade modelada.
- `Fluxo/Aresta`: Ou ainda transição. Descreve a sequência na qual as atividades se realizam. Conexão entre duas ações. Representada por uma seta.
- `Decisão`: Um único fluxo de entrada e vários fluxo de saída. Cada fluxo de saída possui uma sentinela ou `guarda`, que é condição booleana, entre colchetes. Sentinelas são mutualmente exclusivas.
- `Intercalação`: Vários fluxos de entrada e uma única saída. Marca o final de um condicional iniciado por uma decisão.
- `Divergência`:(fork) ponto no qual suas ou mais tarefas podem se iniciar em paralelo
- `Convergência`: (join) Ponto no qual duas ou mais tarefas paralelas se unem para dar início a uma nova tarefa única
- `Nó Final de Atividades`: Ponto onde termina a atividade modelada
- `Partições`: Mostra quem faz o que(quem realiza cada ações ou conjunto de ações). Na UML 1.1 eram chamadas de "raias"("swimlanes").
- `Sinais` ou `Mensagens`: Envio ou recebimento de sinais ou mensagens por um ação.

![[Pasted image 20260105185837.png]]![](foto.png)

## Exemplo de Diagramas de atividades

![[Pasted image 20260105190120.png]]