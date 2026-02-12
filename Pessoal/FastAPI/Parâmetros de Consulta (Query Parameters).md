
Diferente dos parâmetros de rota, o parâmetros de consulta não ficam fixo no caminho. Eles aparecem após um ponto de interrogação `?`na URL.

## Como identificar na URL?

Imagina a URL : `http://127.0.0.1:8000/items/?skip=0&limit=10`

- `?`: Indica que o caminho acabou e começa as consultas
- `skip=0`: É um par de **chave**(`skip`) e o **valor**(`0`)
- `&`: Serve para separar vários parâmetros.

---
## Como o FastAPI reconhece?

Se você colocar um parâmetro na sua função que **não está** no caminho (`@app.get("/items/")`), o FastAPI automaticamente entende que ele é um **Query Parameter**.

```Python
fake_items_db = [{"name": "Item 1"}, {"name": "Item 2"}, {"name": "Item 3"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

---

## Tipos de Parâmetros: Obrigatórios vc Opcionais

O FastAPI decide se um parâmetro é obrigatório ou não com base em como você o escreve:

|**Tipo**|**Como escrever no código**|**Exemplo na URL**|
|---|---|---|
|**Obrigatório**|`needy: str` (sem valor padrão)|`?needy=quero_isso`|
|**Com Padrão**|`skip: int = 0` (usa 0 se não for enviado)|`?skip=5`|
|**Opcional**|`q: str \| None = None` (pode ser vazio)|`?q=busca` ou nada|

**Atenção**: Se você definir um parâmetro sem valor  padrão (como `needy:str`) e o usuário não enviar na URL, o FastAPI retornará um erro automático de "campo obrigatório".

---

## A "Mágica" dos Boleanos (Verdadeiro/Falso)

O FastAPI é muito inteligente com tipos de `bool`. se você definir um parâmetro como `short:bool = False`, ele aceitará varias formas de dizer  "sim" ou "não":

- **Verdadeiro(True)**: `?short=1`, `?short=True`, `?short=true`, `?short=on`, `?short=yes`
- **Falso(False)**: O Padrão ou qualquer variação de "false","no", "0"

---
## Misturando tudo

Você pode ter parâmetros de rota e de consultas na mesma função. O FastAPI sabe quem é quem pelo nome:

```Python
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,      # Path Parameter (está na URL)
    item_id: str,      # Path Parameter (está na URL)
    q: str | None = None, # Query Parameter (opcional)
    short: bool = False   # Query Parameter (com padrão)
):
    ...
```