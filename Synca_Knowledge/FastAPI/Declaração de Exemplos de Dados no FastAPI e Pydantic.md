
**Resumo (O que é?):** A Declaração de Exemplos de Dados no framework FastAPI é uma técnica utilizada para injetar dados simulados (fake data) diretamente na documentação interativa gerada automaticamente (Swagger UI em `/docs`). A Declaração de Exemplos de Dados preenche previamente os campos de requisição JSON na interface da documentação, permitindo que os usuários e desenvolvedores front-end testem a API com um único clique, sem a necessidade de digitar estruturas complexas de dados manualmente. O ecossistema FastAPI e Pydantic oferece quatro abordagens distintas para configurar estes exemplos, dependendo do escopo e da granularidade necessários para a arquitetura do projeto.

## 1. Configuração de Exemplos no Modelo Pydantic (Abordagem Recomendada)

A definição de exemplos diretamente na classe do Modelo Pydantic (que herda de `BaseModel`) é a prática mais organizada e recomendada. O Modelo Pydantic atua como a fonte única da verdade; portanto, qualquer rota da API que utilizar este Modelo Pydantic herdará automaticamente o exemplo configurado. Para implementar esta abordagem, o desenvolvedor deve utilizar o dicionário de configuração interna `model_config` em conjunto com a chave `json_schema_extra`.

### Exemplo de Código no Modelo Pydantic


```Python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

    # O model_config injeta o exemplo no esquema JSON gerado pelo Pydantic
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "PlayStation 5",
                    "price": 4500.00
                }
            ]
        }
    }
```

## 2. Configuração de Exemplos Direto no Pydantic Field

Quando o desenvolvedor necessita fornecer exemplos para propriedades individuais em vez do objeto inteiro, a configuração deve ser feita através do Pydantic `Field`. O Pydantic `Field` aceita o parâmetro `examples` (recebendo uma lista), o que é ideal para demonstrar restrições específicas de formatação, como a exigência de casas decimais em um campo numérico.

### Exemplo de Código no Pydantic Field


```Python
from pydantic import BaseModel, Field

class Item(BaseModel):
    # O Pydantic Field documenta exemplos individuais para cada atributo
    name: str = Field(examples=["PlayStation 5"])
    price: float = Field(examples=[4500.50])
```

## 3. Configuração de Exemplos na Rota com FastAPI Body

Em arquiteturas mais complexas, um mesmo Modelo Pydantic pode ser reaproveitado em múltiplas rotas diferentes (por exemplo, uma rota de criação e uma rota de atualização). Se o desenvolvedor desejar exibir exemplos distintos para cada contexto de rota, a declaração de exemplos deve ocorrer na assinatura da função da rota, utilizando a classe `Body` do FastAPI em conjunto com a tipagem `Annotated`.

### Exemplo de Código com FastAPI Body


```Python
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.put("/items/{id}")
async def update_item(
    # O FastAPI Body injeta um exemplo exclusivo para esta rota de atualização (PUT)
    item: Annotated[Item, Body(examples=[{"name": "Xbox", "price": 3000.00}])]
):
    return item
```

## 4. Múltiplos Exemplos com OpenAPI no FastAPI Body

Para documentações avançadas que exigem a demonstração de vários cenários de uso (como um "Cenário de Sucesso", um "Cenário com Dados Faltando" ou um "Cenário Limite"), o desenvolvedor deve utilizar o parâmetro `openapi_examples` dentro da função `Body` do FastAPI. O parâmetro `openapi_examples` instrui o Swagger UI a renderizar um menu de seleção (dropdown) interativo na documentação, permitindo que o usuário alterne entre os diferentes _payloads_ de teste.

### Exemplo de Código com Múltiplos Cenários OpenAPI


```Python
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(
    # O openapi_examples cria um menu interativo com cenários nomeados na documentação
    item: Annotated[Item, Body(
        openapi_examples={
            "Normal": {
                "summary": "Um item padrão",
                "value": {"name": "Mouse", "price": 50.0}
            },
            "Caro": {
                "summary": "Um item de luxo",
                "value": {"name": "Mouse de Ouro", "price": 5000.0}
            }
        }
    )]
):
    return item
```