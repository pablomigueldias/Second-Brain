**Resumo (O que é?):**

Da mesma forma que o framework FastAPI utiliza a classe `Query` para impor regras de validação em parâmetros de busca (Parâmetros de Consulta), o FastAPI utiliza a classe `Path` para validar parâmetros estruturais que fazem parte integrante da URL (Parâmetros de Rota). A sintaxe de implementação entre `Query` e `Path` é virtualmente idêntica, compartilhando as mesmas regras matemáticas de limite. A distinção fundamental de arquitetura é que um Parâmetro de Rota (Path Parameter) é **sempre obrigatório**. A obrigatoriedade ocorre porque o Parâmetro de Rota constrói o endereço do recurso; se o Parâmetro de Rota estiver ausente, a URL alvo simplesmente não existe no servidor.

## Regras Matemáticas de Validação Numérica no FastAPI

Para estabelecer limites de validação numérica, o FastAPI adota uma nomenclatura baseada em siglas da língua inglesa ("sopa de letrinhas"). Estas siglas são inseridas como argumentos dentro das classes `Path` ou `Query` para definir fronteiras matemáticas estritas.

|**Sigla no FastAPI**|**Significado Original (Inglês)**|**Tradução do Comportamento**|**Símbolo Matemático Equivalente**|
|---|---|---|---|
|`gt`|Greater Than|Estritamente Maior que|`>`|
|`ge`|Greater Than or Equal|Maior ou Igual a|`>=`|
|`lt`|Less Than|Estritamente Menor que|`<`|
|`le`|Less Than or Equal|Menor ou Igual a|`<=`|

### Casos de Uso Comuns das Regras Matemáticas

- **Validação de Idade (Maior ou igual a 18 anos):** O desenvolvedor utiliza `Path(ge=18)`.
    
- **Validação de Paginação (Página estritamente maior que zero):** O desenvolvedor utiliza `Query(gt=0)`.
    
- **Validação de Porcentagem (Intervalo fechado entre 0 e 100):** O desenvolvedor combina restrições utilizando `Path(ge=0, le=100)`.
    

## Implementação da Validação de Rota com Annotated e Path

Para aplicar as regras matemáticas, o desenvolvedor deve importar a classe `Path` do pacote do FastAPI e combiná-la com a tipagem estrita do recurso `Annotated`.

### Exemplo Prático de Validação de ID


```Python
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

# O FastAPI exige que item_id seja um inteiro maior ou igual a 1
@app.get("/itens/{item_id}")
async def ler_item(
    item_id: Annotated[int, Path(title="O ID do item", ge=1)]
):
    return {"item_id": item_id}
```

Com a arquitetura de validação acima, se o cliente da API tentar acessar rotas inválidas como `/itens/0` ou `/itens/-5`, o FastAPI intercepta a requisição e retorna um erro HTTP de validação (Unprocessable Entity) antes mesmo de executar o bloco de código da função Python.

## Validação de Números Decimais (Float) no FastAPI

O motor de injeção de dependências do FastAPI aplica exatamente as mesmas regras e siglas (`gt`, `lt`, `ge`, `le`) para variáveis de ponto flutuante. O framework realiza a conversão automática para a tipagem `float` nativa do Python e valida os limites estabelecidos.

### Exemplo de Validação de Ponto Flutuante


```Python
from typing import Annotated
from fastapi import Query

# O tamanho exigido deve estar estritamente no intervalo entre 0.0 e 10.5
size: Annotated[float, Query(gt=0, lt=10.5)]
```

## A Resolução de Conflitos de Ordem de Parâmetros com Annotated

Na linguagem Python pura, existe uma restrição sintática rígida: na assinatura de uma função, parâmetros obrigatórios (parâmetros sem valor padrão) nunca podem ser declarados depois de parâmetros opcionais (parâmetros com valor padrão associado). Historicamente, isso gerava atritos arquiteturais no FastAPI ao tentar misturar um `Path Parameter` (que é sempre obrigatório e não tem valor padrão) após um `Query Parameter` (que frequentemente é opcional).

A adoção do `Annotated` resolve este conflito de ordem de forma definitiva. Ao utilizar o `Annotated`, o interpretador Python avalia a sintaxe como válida, delegando ao motor do FastAPI a responsabilidade de gerenciar os valores obrigatórios e padrões por debaixo dos panos. O uso universal do `Annotated` garante que o desenvolvedor nunca enfrente erros de compilação relacionados à ordem posicional dos parâmetros da API.