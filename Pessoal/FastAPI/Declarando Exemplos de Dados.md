
O FastAPI permite que você coloque dados "fake" que aparecerão automaticamente na documentação (`/docs`). Assim, o usuário só precisa clicar em um botão para testar, sem precisar digitar tudo à mão.

Existem 3 formas principais de fazer isso:

## 1. No Modelo Pydantic (Recomendado 🏆)

Esta é a forma mais organizada. Você coloca o exemplo dentro da classe do modelo. Assim, em qualquer lugar que esse modelo for usado, o exemplo vai junto.

Usamos o `model_config` com a chave `json_schema_extra`:

```Python
class Item(BaseModel):
    name: str
    price: float

    # Configuração extra do modelo
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

## 2. Direto no Campo (`Field`)

Se você quiser dar exemplo apenas de um campo específico (ex: mostrar que o preço deve ter casas decimais), use o parâmetro `examples` dentro do `Field`.

```Python
class Item(BaseModel):
    name: str = Field(examples=["PlayStation 5"])
    price: float = Field(examples=[4500.50])
```

## 3. Na Rota (`Body`)

Às vezes, o mesmo modelo `Item` é usado em lugares diferentes e você quer dar exemplos diferentes para cada rota. Nesse caso, colocamos o exemplo dentro da função da rota, usando `Body`.

```Python
@app.put("/items/{id}")
async def update_item(
    item: Annotated[Item, Body(examples=[{"name": "Xbox", "price": 3000}])]
):
    ...
```

## 4. Múltiplos Exemplos

E se você quiser mostrar para o usuário vários cenários? Tipo: "Exemplo Normal", "Exemplo Inválido" ou "Exemplo Mínimo"?

Você usa o `openapi_examples` dentro do `Body`. Isso cria um menu de seleção na documentação!

```Python
@app.post("/items/")
async def create_item(
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
    ...
```