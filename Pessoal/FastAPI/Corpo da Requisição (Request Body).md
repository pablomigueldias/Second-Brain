
Quando você precisa enviar dados do cliente(como um navegador ou app celular) para a API, você os envia como um **Request Body**


## O que é o Request Body?

É um "pacote" de dados (geralmente em formato JSON) que viaja escondido na requisição. Diferente dos parâmetros da URL, ele não tem limite de tamanho e é mais seguro enviar informações detaljadas.

- **POST**: Usado para criar dados.
- **PUT**: Usado para atualizar dados.
- **GET**: Não deve ser usado com corpo(é como tentar colocar uma melancia dentro de um envelope de carta).

---
## O Poder do Pydantic(BaseModel)

para definir como esse "pacote" deve ser, usamos o **Pydantic**. Você cria uma classe que herda de `BaseModel`. Isso define o "formato"(schema) dos dados.

```Python
from pydantic import BaseModel

class Item(BaseModel):
	name: str
	description: str | None = None #Opcional
	price: float
	tax: float | None = None #Opcional
```

---
## Declarando no FastAPI

para receber esse objeto, basta colocá-lo como parêmetro na sua função. O FastAPI vai ler o JSON que chegar, transformar em um objeto Python e validar tudo para você.

```Python
@app.post("/items/")
async def create_item(item: Item)
		return item
```

O que o FastAPI faz por você aqui:

1. Lê o JSON que veio na requisição
2. Converte os tipos(ex:se o preço veio como string "45.5", ele vira `float`)
3. Valida: se faltar o `nome`(que é obrigatório), ele já avisa o erro pro usuário.
4. Autocompletar: Dentro da função, se você digitar `item`, seu editor vai sugerir `name`,`price`, etc.
---
## O Grande Mix: Body + Path + Query

O FastAPI é inteligente o suficiente para saber de onde vem cada dado. Ele usa uma lógica simples

| **Se o parâmetro...**                        | **O FastAPI entende como...** |
| -------------------------------------------- | ----------------------------- |
| Está declarado na **rota** (ex: `{item_id}`) | **Path Parameter**            |
| É um **tipo simples** (int, str, bool)       | **Query Parameter**           |
| É um **modelo Pydantic** (BaseModel)         | **Request Body**              |

### Exemplo

```Python
app.put("/items/{item_id})
async def update_item(item_id:int, item: Item, q: str | None = None):
	# item_id -> vem do caminho (path)
	# item -> vem do corpo (Body/JSON)
	# q -> vem da interrogação (Query)
	return {"item_id:"item_id,**item.model_dump(), "q":q}
```


```Python
from pydantic import BaseModel

class Aluno(BaseModel):
	nome: str
	idade: int
	plano: str | None = None
```
