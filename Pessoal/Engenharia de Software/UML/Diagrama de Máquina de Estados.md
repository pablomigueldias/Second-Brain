
Link do conteúdo: [Diagrama de Máquina de Estados](https://www.youtube.com/watch?v=N0wc9sHp5yo&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=11)

Também conhecido como Diagrama de Transição de Estados ou simplesmente `Diagrama de Estados`

- Diagrama comportamental empregado para descrever como um sistema se comporta quando um evento ocorro, considerando todos os estados, transições e ações possíveis de um objeto.
- Representa o estado ou situação na qual um objeto pode se encontrar ao longo da execução dos processos em um sistema.
- Mostra como um elemento se comporta por meio de um conjunto de transições de estado - a chamada `máquina de estados`.

## Para que serve?

Os diagramas de máquina de estados são muito usados para modelar o comportamento de:

- Interfaces
- Casos de uso
- Instâncias de classes

e na modelagem de sistemas reativos.

--- 

## Elementos de um diagrama de estados

- `Estado(simples)`: condição ou situação na vida de um objeto que satisfaz alguma condição, realiza alguma atividade ou espera um evento.
- `Estado inicial`: Determina o início da modelagem dos estados de um elemento.
- `Estado final`: indica o final dos estados modelados para o elemento.
- `Estado composto`: Estado que possui sub-estados.

![[Pasted image 20260105194608.png]]


## Elementos de um diagrama de estados

- `Transição:`Movimento de um estado para o outro estado. Representa um evento que causa uma mudança no estado de um objeto, levando a um novo estado.

Ocorre da seguinte forma:

1) Um elemento está em um estado inicial
2) Um evento ocorre
3) Uma ação realizada
4) O elemento muda para um estado distinto

![[Pasted image 20260105194949.png]]

## Elementos de um diagrama de estados

- `Evento` incidente que leva os objetos a transicionar de um estado para o outro. Ocorrência de um estímulo que pode disparar uma transição de estado. pode ser interno ou externo.
	- Tipos de eventos: Sinal, Chamada, Temporizado, Mudança
- `Ação`: Execução atômica que se completa sem interrupção, Resultando em uma alteração de estado.
- `Atividade`: Execução atual não atômica em uma maquina de estados.

## Condicionais: Pseudoestado de escolha

- `Pseudoestado de escolha`: Ponto na transição de estados de um objeto no qual uma decisão será tomada, baseada em uma condição. É um nó de decisão, condicionado por condições de `guarda` para decidir qual o próximo estado a ser gerado para o objeto.
- `Condição de Guarda`: Condição avaliada após o disparo de um evento, e que determina como ocorrerá a transição - pode haver múltiplas transições possíveis do mesmo estado com o mesmo disparo- mas só uma ocorrerá

![[Pasted image 20260105200217.png]]

---

- `Barras de Bifurcação`: Ocorre quando duas ou mais transições partem de um mesmo estado. Assim, haverá mais de um processo ocorrendo de forma paralela.
- `Barra de União/Junção`: Quando duas ou mais transições levam a um mesmo estado. Determina o momento em que dois ou maios processos paralelos se unem em um único processo.

![[Pasted image 20260105200649.png]]

## Operações realizadas em um estado

`Atividades internas`: Um objeto pode realizar atividades enquanto está em um estado. Essas atividades podem ser detalhadas por meio das seguintes cláusulas:

- `entry/` Atividade executada quando o objeto entra em um estado
- `do/` Executada enquanto o objeto está em um estado
- `exit/` Quando o objeto sai de um estado (antes da transição)
- `on event/` Realizada em resposta a um evento(estímulo)

![[Pasted image 20260105201007.png]]

## Como criar um diagrama de estados

- Determine o estado inicial e o estado final
- Identifique todos os estados possíveis para o processo modelado.
- Use setas ou linhas para destacar as transições de controle de um estado para outro, conectando origem e destino.
- Rotule os eventos que disparam essas transições
- Estabeleça condições de guarda para assegurar que as transições são apropriadas e relevantes. Uma condição de guarda força e verificação da transição contra uma condição antes do prosseguir

## Exemplo de Diagrama de estados

![[Pasted image 20260105201622.png]]
