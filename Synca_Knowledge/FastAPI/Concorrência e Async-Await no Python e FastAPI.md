
**Resumo (O que é?):**

A Concorrência e o uso de Async/Await em Python representam um modelo de execução de software onde o sistema gerencia múltiplas tarefas ao mesmo tempo, sem que a aplicação fique travada esperando uma finalização. Uma analogia prática para a programação assíncrona é o atendimento em uma lanchonete moderna: na abordagem Assíncrona (Concorrente), o sistema registra um pedido e, enquanto aguarda o preparo (uma operação de Entrada/Saída lenta), libera o sistema para processar outros pedidos. Em contraste, na abordagem Síncrona (Sequencial), o sistema fica totalmente bloqueado em uma fila, aguardando a finalização da primeira tarefa antes de poder atender a próxima.

## Diferença entre Concorrência e Paralelismo

Embora os termos sejam frequentemente confundidos no desenvolvimento de software, Concorrência e Paralelismo resolvem problemas diferentes de maneiras distintas:

- **Concorrência (Asynchronous / Async):** A Concorrência trata da habilidade do sistema de alternar e lidar com muitas coisas ao mesmo tempo dentro de um único processo. A Concorrência é ideal para tarefas do tipo I/O Bound (Entrada e Saída), como aguardar a resposta de um banco de dados, a leitura de um arquivo ou o carregamento de uma API externa. O sistema pausa a espera de uma tarefa para adiantar o processamento de outra.
    
- **Paralelismo:** O Paralelismo trata da execução literal e simultânea de muitas coisas ao mesmo exato tempo. O Paralelismo exige múltiplos processadores (ou múltiplos núcleos de CPU) trabalhando fisicamente juntos de forma independente. O Paralelismo é utilizado para tarefas do tipo CPU Bound (que exigem alto poder computacional e cálculos matemáticos pesados), como processamento de vídeos ou treinamentos complexos de Machine Learning.
    

## Quando usar async def ou def no FastAPI

O framework FastAPI possui um gerenciamento inteligente e suporta nativamente tanto funções assíncronas quanto síncronas. A regra para escolher entre `async def` e `def` no FastAPI depende das bibliotecas utilizadas dentro da rota:

|**Situação da Biblioteca no Código**|**Declaração a Usar**|**Motivo da Escolha Arquitetural no FastAPI**|
|---|---|---|
|A biblioteca suporta e exige o uso de `await`.|`async def`|O FastAPI permite que o servidor atenda outras requisições de usuários simultaneamente enquanto aguarda a resposta assíncrona.|
|A biblioteca é antiga e não suporta operações assíncronas.|`def`|O FastAPI executará automaticamente esta função síncrona em uma _thread_ separada para garantir que o servidor principal não trave.|
|O desenvolvedor não tem certeza da compatibilidade.|`def`|Utilizar `def` padrão é o caminho mais seguro no FastAPI para iniciantes evitarem gargalos de bloqueio acidental do servidor.|

### Exemplo Prático de Código no FastAPI


```Python
# Abordagem Assíncrona (Concorrente / Rápida)
@app.get('/async-route')
async def ler_resultados_assincronos():
    # A palavra-chave 'await' pausa a execução apenas desta função específica.
    # Isso permite que o FastAPI atenda outros usuários enquanto aguarda a resposta.
    resultados = await biblioteca_lenta_assincrona() 
    return resultados
	
# Abordagem Síncrona (Sequencial / Padrão)
@app.get('/sync-route')
def ler_resultados_sincronos():
    # O FastAPI identifica a falta do 'async' e joga a execução para uma thread separada.
    # A função aguarda de forma bloqueante até o processamento terminar.
    resultados = biblioteca_comum_sincrona() 
    return resultados
```

## O Conceito de Corrotina (Coroutine)

Uma **Corrotina** (ou _Coroutine_) é o termo técnico que descreve o objeto gerado e retornado quando o Python executa uma função declarada com `async def`. A Corrotina funciona como um "número de chamada" ou um "ticket" de espera do sistema. O interpretador Python compreende que uma Corrotina é uma rotina especial que pode ter sua execução pausada (no momento em que encontra um `await`) e posteriormente retomada de onde parou, viabilizando assim a alternância de contexto da Concorrência.