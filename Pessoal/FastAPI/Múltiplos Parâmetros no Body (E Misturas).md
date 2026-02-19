- **Tem `{}` na rota?  $\to$ É Path Parameter**.
- **É um Modelo Pydantic? $\to$ É Body(JSON).**
- **É um tipo simples (int,str) e não está na rota? $\to$ É Query Parameter**

```Python
@app.put("/itens/{item_id}")
async def update_item(
	item_id: int, # Path (vem da URL)
	item: Item, # Body (vem do JSON)
	q: str | None = None # Query(vem do ?q=...)
):
	...
```

---
## Múltiplos Modelos no Body(A Mudança na Estrutura)

Aqui a coisa muda de figura.

Se você pedir apenas um modelo (`item: Item`), o FastAPI espera que o JSON seja os dados do item direto:

```JSON
{ "nome": "Martelo", "preco": 50 }
```

Mas, se você pedir dois ou mais modelos (`item: Item, user: User`), o FastAPI muda a estrutura do JSON. Ele cria um objeto "pai" e usa os nomes dos parâmetros como chaves

```Python
async def update_item(item: Item, user: User): ...
```

**O JSON esperado será**:

```JSON
{
    "item": { "nome": "Martelo", "preco": 50 },
    "user": { "username": "joao" }
}
```

## Valores Singulares no Body

E se você quiser enviar um `Item`, um `User` e também um número simples, tipo `importancia:int`?

Se você só declarar `importancia: int`, o FastAPI vai achar que é um **Query(na URL)**. para forçar que esse número venha dentro do JSON, usamos o `Body()`:

```Python
from fastapi import Body

async def update_item(
    item: Item, 
    user: User, 
    importancia: Annotated[int, Body()] # Força a ser Body!
): ...
```

**JSON Esperado:**

```JSON
{
    "item": {...},
    "user": {...},
    "importancia": 5
}
```

---

## O Truque do `embed=True`

Às vezes, você tem apenas um modelo(Item), mas quer que o JSON venhas co a chave `item`, só para manter o padrão organizado.

Você usa o `embed=True`

```Python
async def update_item(item: Annotated[Item, Body(embed=True)]): ...
```

Em vez de enviar `{ "nome": "Martelo" }`, o cliente terá que enviar `{ "item": { "nome": "Martelo" } }`