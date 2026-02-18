
O Pydantic permite criar estruturas de dados tão profundos quanto você precisar.

## Listas e Conjuntos

Se você tem um campo que pode receber vários valores(como "tags" de um produto), você usa `list`.

A evolução da tipagem:
-  `tags: list = []`: Funciona, mas o FastAPI não sabe o que tem dentro da lista. Pode ser texto, números ou abacaxi
-  `tags:list[str] = []`: Agora sim! O FastAPI sabe que é uma **lista de textos.**

**O Poder do `Set` (Conjunto)**

E se o usuário enviar `["rock","metal","rock"]`? A tag "rock" ficou repetida se você usar `set`:

```Python
tags: set[str] = set()
```

O Python remove duplicatas automaticamente! O resultado será apenas `{"rock","metal"}`

---
## Modelos dentro de Modelos(Submodelos)

Imagine que um **Item** tem uma **Imagem**. A imagem tem URL e Nome. Em vez de colocar tudo solto no item, criamos um modelo só pra ela.

```Python
from pydantic import BaseModel, HttpUrl

# 1. Definimos o modelo menor (Filho)
class Image(BaseModel):
    url: HttpUrl # Valida se é uma URL real (http://...)
    name: str

# 2. Usamos ele dentro do modelo maior (Pai)
class Item(BaseModel):
    name: str
    price: float
    image: Image | None = None # Aqui está o aninhamento!
```

O JSON esperado seria:

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

---
## Listas de Modelos

E se o item tiver **várias** fotos? Basta usar `list` com o seu modelo

```Python
class Item(BaseModel):
    name: str
    images: list[Image] | None = None # Uma galeria de fotos!
```

O FastAPI vai esperar:

```JSON
{
  "name": "TV",
  "images": [
    {"url": "...", "name": "Frente"},
    {"url": "...", "name": "Verso"}
  ]
}
```

---
## Corpos de Dicionários Arbitrários

Às vezes, você não sabe os nomes dos campos(chaves) que vão chegar. imagine um sistema onde você guarda o peso de itens por ID, mas os IDs mudam sempre.

Você pode usar `dict[key_type, value_type]`

```Python
@app.post("/pesos/")
async def criar_pesos(pesos: dict[int, float]):
    return pesos
```

Isso aceita um JSON onde as chaves são números inteiros e os valores são números decimais:

```JSON
{
    "102": 3.5,
    "550": 10.2
}
```
```
