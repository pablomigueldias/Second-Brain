**Resumo (O que é?):**

A Validação de Strings e Parâmetros de Consulta no framework FastAPI expande as capacidades de tipagem primitivas da linguagem Python. Em vez de aceitar qualquer texto genérico, o FastAPI permite que o desenvolvedor imponha regras de negócio estritas diretamente na assinatura da função (como exigir que uma busca tenha um tamanho mínimo ou respeite uma formatação específica). Para orquestrar essas validações avançadas de forma limpa, o FastAPI e o ecossistema Pydantic utilizam a classe estrutural `Annotated` em conjunto com a função `Query`.

## O Papel da Classe Annotated no FastAPI

A estrutura `Annotated` é a abordagem padrão e oficialmente recomendada pelo FastAPI (a partir da versão 0.95) para injetar metadados e regras de validação nos tipos nativos do Python. Em uma analogia com o sistema de correios, o tipo base (como `str`) representa o conteúdo físico de um pacote (um par de meias), enquanto os metadados adicionados pelo `Annotated` representam as etiquetas de restrição coladas do lado de fora da caixa (como "Frágil" ou "Peso Máximo: 1kg").

### Exemplo Prático com Annotated e Query


```Python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# O Annotated preserva o tipo opcional 'str | None' e injeta a regra do Query limitando o tamanho
@app.get("/search/")
async def search_items(
    q: Annotated[str | None, Query(max_length=50)] = None
):
    return {"q": q}
```

## Validações Comuns de String com a Função Query

A função `Query()` do FastAPI atua como um validador de fronteira que bloqueia requisições malformadas. O desenvolvedor pode combinar múltiplos parâmetros de restrição simultaneamente dentro da instância do `Query()`:

|**Parâmetro de Validação**|**Comportamento Estrutural no FastAPI**|**Exemplo de Implementação**|
|---|---|---|
|`min_length`|Define a quantidade mínima obrigatória de caracteres para a string.|`Query(min_length=3)`|
|`max_length`|Define a quantidade máxima permitida de caracteres para a string.|`Query(max_length=50)`|
|`pattern`|Exige que a string inserida corresponda a uma Expressão Regular (Regex) específica.|`Query(pattern="^fixedquery$")`|

## Injeção de Metadados para Documentação (Swagger UI)

Além de aplicar segurança via validações, a função `Query()` aceita parâmetros de metadados puramente descritivos. O FastAPI processa esses metadados para enriquecer a documentação interativa OpenAPI gerada automaticamente (Swagger UI disponível na rota `/docs`).

- **`title`:** Estabelece um título curto e de fácil leitura para o parâmetro na interface.
    
- **`description`:** Renderiza uma explicação detalhada sobre a funcionalidade do Parâmetro de Consulta.
    
- **`alias`:** Configura um "apelido" público para o parâmetro na URL da API. O `alias` é vital quando a URL precisa receber um nome de chave inválido para o Python (como variáveis contendo hífens, ex: `item-query`).
    
- **`deprecated=True`:** Sinaliza visualmente na documentação oficial que este Parâmetro de Consulta está obsoleto e será descontinuado em atualizações futuras.
    

## Recebimento de Múltiplos Valores (Listas) em Parâmetros de Consulta

Em arquiteturas de busca complexas, o cliente HTTP pode enviar a mesma chave de consulta na URL contendo valores distintos simultaneamente (por exemplo: `?q=foo&q=bar`). Para instruir o FastAPI a não sobrescrever o valor, mas sim agrupá-los, o desenvolvedor deve tipar o Parâmetro de Consulta explicitamente como uma lista (`list`).

### Exemplo de Captura de Lista na URL


```Python
# A tipagem list[str] instrui o FastAPI a acumular todas as chaves 'q' da URL
@app.get("/items/")
async def read_item(
    q: Annotated[list[str] | None, Query()] = None
):
    # Resultado extraído da URL '?q=foo&q=bar': {"q": ["foo", "bar"]}
    return {"q": q}
```

## Validação Personalizada com AfterValidator (Pydantic V2)

Quando as regras embutidas no FastAPI (como `min_length` e `pattern`) não são suficientes para cobrir as regras de negócio, a arquitetura do Pydantic (a partir da versão 2) fornece a classe `AfterValidator`. O `AfterValidator` permite que o desenvolvedor conecte funções Python customizadas diretamente no `Annotated`.

### Exemplo de Regra Customizada para Prefixos


```Python
from typing import Annotated
from pydantic import AfterValidator
from fastapi import FastAPI

app = FastAPI()

# 1. Definição da função puramente Python para validação
def validar_prefixo(v: str) -> str:
    # Se a string não começar com o prefixo correto, levanta um erro formal
    if not v.startswith("user-"):
        raise ValueError("O identificador deve começar obrigatoriamente com 'user-'")
    return v

# 2. Injeção da validação na rota através do Annotated e AfterValidator
@app.get("/users/{user_id}")
async def get_user(
    user_id: Annotated[str, AfterValidator(validar_prefixo)]
):
    return {"user_id": user_id}
```