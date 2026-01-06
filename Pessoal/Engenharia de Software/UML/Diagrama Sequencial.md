
Link do conteúdo: [Diagrama Sequencial](https://www.youtube.com/watch?v=UVkj3ed0ZuM&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=9)


Diagrama que enfatiza a ordenação temporal das mensagens. No geral, se baseia em um caso de uso definido pelo diagrama de mesmo nome, e usa o diagrama de classes para definir os objetos envolvidos no processo.

As interações são mostradas na ordem em que elas ocorrem - ou seja, esse tipo de diagrama mostra uma sequência de eventos.

Os Casos de Uso são refinados em um ou mais Diagramas de Sequência.

## Aplicações dos Diagramas de Sequência

- Ajudar a identificar como os objetos no sistemas interagem uns com o outros para implementar as funcionalidades definidas.
- Visualizar como mensagens são trocadas entre os componentes.
- Entender os Requisitos de um sistema ou parte dele
- Realizar a documentação de processos em um sistema em desenvolvimento
- Mostrar detalhes em diagramas de Casos de uso

## Componentes de um Diagrama de Sequência

Um Diagrama de Sequência costuma conter os seguintes elementos:

- Atores
- Objetos que participam da interação
- Mensagens trocadas (e seus parâmetros)
- Linhas de vida e Caixa de Ativação
- Operadores de Controle Estruturado
- Foco de Controle
- Gate

## Diagramas de Sequência: Atores

- Representam papéis que interagem com o sistema e seus objetos.
- Um ator está sempre fora do escopo do sistema modelado.
- Os atores são empregados para representar usuários humanos e outros elementos externos

## Diagrama de Sequência: Objetos

São os elementos que participam das interações no diagrama. Representam uma classe ou um objeto.

- Interagem por meio de mensagens
- Colocados no nível superior do diagrama, ao longo do eixo x
- Objetos que inicia a interação é colocado à esquerda
- Objetos subordinados à direita

Um objeto é representado por um retângulo com seu nome.

![[Pasted image 20260105145117.png]]

## Diagrama de Sequência: Linha de Vida

Elemento nomeado que representa um participante interno individual na interação.
A Linha de Vida de um objeto é uma linha tracejada vertical que representa o período de tempo no qual um objeto existe.

![[Pasted image 20260105145335.png]]

## Diagrama de Sequência: Foco de Controle

Período no qual um objeto está participando ativamente de um processo, ou seja, o tempo necessário para que um objeto complete uma tarefa.
Também é chamado de `Caixa de Ativação`.

Representado dentro da linha de vida de um objeto, como um retângulo na vertical.

Obs.: Como atores são elementos externos, eles não precisam de caixa de ativação.

![[Pasted image 20260105145721.png]]

## Diagrama de Sequência: Mensagens

Demonstram a ocorrência de eventos(chamadas de métodos) ou comunicação entre objetos, sem chamar métodos.

Mostram as informações que são enviadas entrem os objetos

As Mensagens são representadas por uma seta horizontal que vai de uma linha de vida a outra, apontando para o destinatário da mensagem.

![[Pasted image 20260105150047.png]]

---

## Tipo de Mensagens

Existem vários tipos de mensagens empregadas em diagramas de sequência, sendo as mais comuns as seguintes:

- Mensagem Síncrona
- Mensagem Assíncrona
- Auto - mensagem
- Mensagem Resposta
- Mensagem de Criação de Participante
- Mensagem de Exclusão de Participante
- Mensagem de Guarda

## Mensagem Síncrona

Mensagem que espera por uma resposta antes que a interação possa prosseguir. Remetente espera até que o receptor tenha terminado o processamento de mensagem. Grande parte das mensagens é síncrona.

Usamos uma seta de ponta sólida para representar a mensagem síncrona.

![[Pasted image 20260105150550.png]]

## Mensagem Assíncrona

Mensagem que não espera por uma resposta do destinatário antes que a interação possa prosseguir. A interação prossegue independente do destinatário processar a mensagem ou não.

Usamos uma seta de ponta linear para representar a mensagem síncrona

![[Pasted image 20260105151917.png]]

## Mensagem de Criação de Participantes

Uma mensagem de criação permite instanciar um novo objeto no diagrama. às vezes, é necessário que uma mensagem crie um novo objeto

Representada por uma seta tracejada com o rótulo `<<create>>`  em uma tag.

![[Pasted image 20260105152153.png]]

## Mensagem de Exclusão de Participoante

A Mensagem de exclusão é empregada para eliminar um objeto. Assim, a memória é desalocada pela destruição da ocorrência do objeto no sistema.

Representada por uma seta que termina com um X.

![[Pasted image 20260105152418.png]]

## Auto-Mensagem

Uma auto-mensagem é empregada quando um objeto necessita realizar uma chamada a si mesmo.

Representada com uma seta que sai e volta ao mesmo objeto.

Pode ser síncrona ou assíncrona.

![[Pasted image 20260105152557.png]]

## Mensagem de Resposta

Uma mensagem de resposta (ou de retorno) identifica a resposta a uma mensagem enviada para o objeto.

Pode retornar informações específicas ou apenas uma mensagem de êxito ou falha na execução de um método.

Representadas por uma linha fina tracejada que aponta para o objeto que recebe o resultado de retorno.

![[Pasted image 20260105152837.png]]

## Mensagens de Guarda

As Mensagens de Guarda são usada para modelar condições.

Úteis quando é necessário restringir o fluxo de uma mensagem de acordo com uma condição.

Representadas por uma elipse ao redor da seta de mensagem, indicando a condição.

![[Pasted image 20260105153057.png]]

## Exemplos de Mensagens

![[Pasted image 20260105153221.png]]

## Diagrama de Sequência: Gate

Um Gate(Portão) é o final de uma mensagem, ou seja, um ponto de conexão entre uma mensagem que esteja dentro de um fragmento de interação com outra que esteja fora.

São representados como pontos de conexão de mensagem no quadro em si.

![[Pasted image 20260105153508.png]]

## Tempo de Vida de um Objeto

O Tempo de Vida de um Objeto se refere ao tempo em que ele existe, independente de estar realizando algum processo ou não. Quando um objeto não é mais necessário no sistema, seu tempo de vida pode expirar, e o objeto pode ser removido com uma mensagem de exclusão (Destroy()).

![[Pasted image 20260105153828.png]]

## Fragmentos Combinados e Controle Estruturado

Muitas vezes precisamos mostrar condicionais e loops, ou ainda a execução concorrente de várias sequências.

Para isso usamos `Operadores de Controle Estruturado`(Ou `Operadores de Interação`).

Um Fragmento combinado define uma combinação de fragmentos de interação. Definido por um operador de interação e operando de interação

Região retangular no diagrama, com uma tag que informa o tipo de operador. Aplica-se às linhas de vida que atravessam seu corpo.


## Alguns Tipos de Operadores de Interação

- Execução opcional(um ou nada): `opt`
- Execução condicional(um ou outro): `alt`
- Execução paralela: `par`
- Execução de loop(iteração): `loop`
- Ordem sequencial estrita: `strict`
- Interação Inválida: `neg`
- Interação com outro diagrama: `ref`
- Quebra de execução(exceção): `break`
- Negação: `neg`

![[Pasted image 20260105154639.png]]