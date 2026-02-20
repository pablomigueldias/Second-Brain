
**Resumo (O que é?):** O gerenciamento de Múltiplos Parâmetros no framework FastAPI permite que uma única rota HTTP receba e processe dados provenientes de fontes distintas simultaneamente (URL, Query String e Payload JSON). Além de misturar essas fontes, o FastAPI possui uma arquitetura flexível que permite agrupar múltiplos Modelos Pydantic independentes dentro de um mesmo Corpo da Requisição (JSON Body). Quando múltiplos modelos ou tipos primitivos são declarados para o Corpo da Requisição, o FastAPI reestrutura automaticamente o formato esperado do JSON para evitar conflitos de chaves, criando objetos aninhados.

## Regras de Inferência de Parâmetros no FastAPI

O motor de injeção de dependências do FastAPI utiliza regras de inferência estritas para determinar automaticamente a origem de cada variável declarada na função da rota:

- **É um Parâmetro de Rota (Path Parameter):** Se a variável declarada na função estiver envolvida por chaves `{}` na string da rota (ex: `/itens/{item_id}`).
    
- **É o Corpo da Requisição (Body/JSON):** Se a variável declarada for tipada com uma classe Pydantic (que herda de `BaseModel`).
    
- **É um Parâmetro de Consulta (Query Parameter):** Se a variável for tipada com um tipo primitivo do Python (`int`, `str`, `bool`) e não estiver mapeada na string da rota.
    

### Exemplo de Mistura Básica de Parâmetros

```Python

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float

@app.put("/itens/{item_id}")
async def update_item(
    item_id: int,          # O FastAPI infere como Path Parameter (vem da URL)
    item: Item,            # O FastAPI infere como Request Body (vem do Payload JSON)
    q: str | None = None   # O FastAPI infere como Query Parameter (vem de ?q=...)
):
    return {"item_id": item_id, "item": item, "query": q}
```

## Múltiplos Modelos Pydantic no Corpo da Requisição (Body)

Quando o desenvolvedor declara apenas um único Modelo Pydantic na rota (ex: `item: Item`), o FastAPI espera que as chaves do JSON correspondam diretamente aos atributos desse modelo (ex: `{"nome": "Martelo", "preco": 50}`). No entanto, se o desenvolvedor declarar **dois ou mais** Modelos Pydantic na mesma rota, o FastAPI altera o contrato do JSON. O framework cria um objeto raiz e utiliza o nome exato dos parâmetros da função como chaves para aninhar os dados.

### Exemplo Prático com Múltiplos Modelos Pydantic


```Python
class User(BaseModel):
    username: str

# A rota exige dois modelos distintos simultaneamente
@app.put("/itens-e-usuarios/")
async def update_item_and_user(item: Item, user: User): 
    return {"item": item, "user": user}
```

A declaração acima obriga o cliente da API a enviar o seguinte JSON reestruturado:


```JSON
{
    "item": { 
        "nome": "Martelo", 
        "preco": 50 
    },
    "user": { 
        "username": "joao" 
    }
}
```

## Injeção de Valores Singulares no Corpo da Requisição com FastAPI Body

Em cenários arquiteturais específicos, o desenvolvedor pode precisar receber um Modelo Pydantic junto com um valor primitivo simples (como um identificador ou um nível de importância) dentro do mesmo JSON. Se o desenvolvedor declarar apenas `importancia: int`, a regra de inferência do FastAPI tentará buscar esse valor na URL como um Query Parameter. Para forçar o FastAPI a ler esse valor primitivo de dentro do Corpo da Requisição JSON, é obrigatório utilizar a classe `Body()` em conjunto com `Annotated`.

### Exemplo Prático com Valores Singulares

```Python
from fastapi import Body
from typing import Annotated

@app.put("/itens-avancados/")
async def update_item_advanced(
    item: Item, 
    user: User, 
    # O Annotated em conjunto com Body() anula a regra do Query Parameter
    # forçando o inteiro 'importancia' a ser lido do payload JSON
    importancia: Annotated[int, Body()] 
): 
    return {"item": item, "user": user, "importancia": importancia}
```

JSON esperado pelo FastAPI após a injeção com `Body()`:


```JSON
{
    "item": {"nome": "Martelo", "preco": 50},
    "user": {"username": "joao"},
    "importancia": 5
}
```

## O Truque Estrutural do embed=True no FastAPI Body

Em situações onde o sistema exige apenas um único Modelo Pydantic (ex: `Item`), mas a padronização do Front-end ou do contrato de API exige que os dados venham encapsulados sob uma chave específica (para padronizar com outras rotas de múltiplos modelos), o desenvolvedor utiliza o parâmetro `embed=True` dentro da configuração do `Body()`.

### Exemplo Prático de Envelopamento com embed=True


```Python
@app.put("/itens-encapsulados/")
async def update_item_embedded(
    # O embed=True força o empacotamento do modelo sob a chave 'item'
    item: Annotated[Item, Body(embed=True)]
): 
    return item
```

Em vez de enviar um JSON plano `{"nome": "Martelo", "preco": 50}`, o parâmetro `embed=True` força o cliente a enviar o JSON em formato aninhado:


```JSON
{ 
    "item": { 
        "nome": "Martelo", 
        "preco": 50 
    } 
}
```