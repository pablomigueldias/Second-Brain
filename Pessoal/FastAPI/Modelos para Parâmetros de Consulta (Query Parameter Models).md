
## A Analogia da Sacola

Imagine que você foi ao mercado

- **Jeito Antigo**: Você tenta carregar 10 laranjas equilibrando-as nos braços(parâmetros soltos). É difícil de segurar.
- **Jeito Novo**: Você coloca todas as laranjas dentro de uma sacola(o Modelo Pydantic) e carrega apenas a sacola.

## Como criar o Modelo

Usamos o `BaseModel` do Pydantic, igualzinho fizemos para o `Body`. A diferença é que usamos `Field` para definir as regras (maior que, menor que,padrão).

```Python
from typing import Annotated,Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

class FiltrosBusca(BaseModel):
	limit: int = Field(100, gt=0,le=100) #Padrão 100, entre 1 e 100
	offset: int = Field(0,ge=0) # Padrão 0, positivo
	order_by: Lietal["data","preco"] = "data" # Escolha restrita
	tags: list[str] = []  # Lista de texto
```


## Usando na Rota (O Segredo)

Aqui está. Como o FastAPI sabe se esse modelo é um **JSON(Body)** ou um **Parâmetros de URL(Query)**?

Nós dizemos explicitamente quando `Query()` dentro do `Annotated`

```Python
@app.get("/items/")
async def buscar_itens(
	filtros: Annotated[FiltrosBusca, Query()]
):
	return filtros
```

Ao fazer isso, o FastAPI **não** vai esperar um JSON. Ele vai olhar para a URL: `http://localhost:8000/items/?limit=50&order_by=preco`

---
## Proibindo Parâmetros Extras

por padrão, se o usuário enviar `?limit=10&coisa_aleatoria=xyz`, o FastAPI ignora o "coisa_aleatoria". Mas se você quiser ser rigoroso e dar erro caso enviem algo que não existe, adicione uma configuração no modelo:

```Python
class FiltrosRigorosos(BaseModel):
	Model_config = {"extra":"forbid"} # Proìbe extras!
	limit: int = Field(10)
```

Se o usuário tentar inventar parâmetros, ele recebe um erro `extra_forbidden`