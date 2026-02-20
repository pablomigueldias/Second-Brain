
**Resumo (O que é?):** Os Modelos Aninhados (ou _Nested Models_) representam a capacidade da biblioteca Pydantic de criar e validar estruturas de dados complexas, profundas e hierárquicas. Em vez de receber apenas tipos primitivos simples (como textos ou números soltos), o framework FastAPI utiliza os Modelos Aninhados do Pydantic para processar objetos JSON que contêm listas, dicionários e até mesmo outros objetos JSON embutidos internamente. A arquitetura de Modelos Aninhados permite que a API valide requisições robustas e espelhe exatamente os relacionamentos do banco de dados (como um "Produto" que contém múltiplas "Imagens" e "Categorias").

## Validação de Listas e Conjuntos (Sets) no Pydantic

A definição de tipos para coleções de dados evoluiu no Pydantic para garantir previsibilidade e segurança no FastAPI. A tipagem explícita dita o nível de rigor que a API aplicará aos dados recebidos.

- **Tipagem Genérica (`list`):** Declarar um campo apenas como `tags: list = []` funciona, mas é perigoso. O FastAPI não saberá o conteúdo da lista, permitindo uma mistura insegura de textos, números ou booleanos.
    
- **Tipagem Estrita (`list[str]`):** Declarar o campo como `tags: list[str] = []` informa ao Pydantic que a lista deve conter exclusivamente strings (textos). O FastAPI converterá ou rejeitará elementos que fujam dessa regra.
    
- **O Poder dos Conjuntos (`set[str]`):** O uso da tipagem `set` é ideal para eliminar duplicatas automaticamente. Se o cliente da API enviar um JSON contendo `["rock", "metal", "rock"]`, o Pydantic, através da tipagem `tags: set[str] = set()`, processará os dados e entregará ao FastAPI apenas os valores únicos: `{"rock", "metal"}`.
    

## Modelos dentro de Modelos (Submodelos Pydantic)

A melhor prática para dados complexos é separar as responsabilidades através da criação de Submodelos. Se um modelo principal (`Item`) possui propriedades que formam um subconjunto lógico (como uma `Image` que tem uma URL e um nome), o desenvolvedor deve criar uma classe `BaseModel` isolada para a imagem e injetá-la como atributo no modelo pai.

### Exemplo Prático de Submodelos

```Python
from pydantic import BaseModel, HttpUrl

# 1. Definição do Submodelo Pydantic (Modelo Filho)
class Image(BaseModel):
    url: HttpUrl # O HttpUrl do Pydantic valida se a string é uma URL válida
    name: str

# 2. Definição do Modelo Principal Pydantic (Modelo Pai)
class Item(BaseModel):
    name: str
    price: float
    # O Pydantic aninha o modelo Image aqui. O campo é opcional (None).
    image: Image | None = None 
```

O código acima instrui o FastAPI a validar e esperar a seguinte estrutura JSON aninhada:

```JSON
{
    "name": "TV",
    "price": 5000,
    "image": {
        "url": "http://loja.com/tv.jpg",
        "name": "Foto da TV"
    }
}
```

## Listas de Submodelos Pydantic

Para situações de relacionamento de "Um para Muitos" (como um `Item` que possui uma galeria com várias fotos), o desenvolvedor combina a tipagem de listas nativa do Python com a classe do Submodelo Pydantic.

### Exemplo de Lista de Submodelos


```Python
class Item(BaseModel):
    name: str
    # O Pydantic agora valida uma lista onde cada elemento OBRIGATORIAMENTE é um modelo Image
    images: list[Image] | None = None 
```

Estrutura JSON esperada pelo FastAPI:


```JSON
{
  "name": "TV",
  "images": [
    {"url": "http://loja.com/frente.jpg", "name": "Frente"},
    {"url": "http://loja.com/verso.jpg", "name": "Verso"}
  ]
}
```

## Validação de Dicionários com Chaves Arbitrárias (Dict)

Quando a API FastAPI precisa receber um corpo de requisição onde as chaves (keys) são dinâmicas, desconhecidas previamente ou geradas de forma variável (como IDs de banco de dados vinculados a pesos de produtos), o desenvolvedor não deve criar um `BaseModel` engessado. A solução nativa é utilizar o tipo `dict` (Dicionário) do Python, especificando rigorosamente o tipo esperado para as chaves e para os valores: `dict[tipo_da_chave, tipo_do_valor]`.

### Exemplo Prático de Dicionário Arbitrário


```Python
from fastapi import FastAPI

app = FastAPI()

# O FastAPI garante que as chaves serão inteiros (IDs) e os valores serão decimais (pesos)
@app.post("/pesos/")
async def criar_pesos(pesos: dict[int, float]):
    return pesos
```

Estrutura JSON válida para esta rota:

```JSON
{
    "102": 3.5,
    "550": 10.2
}
```