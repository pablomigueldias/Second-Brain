
Até agora, apenas dizíamos que um parâmetro era `str` ou `int`. Mas e se você quiser que uma busca tenha no mínimo 3 letras e no máximo 50? Usamos `Annotated` e a classe `Query`.

## O que é o `Annotated`?

O `Annotated` é a forma recomendada pelo FastiAPI(desde a versão 0.95) para adicionar metadados aos tipos.

**Analogia**: Imagine um pacote de correio.

- O **Tipo**(`str`) é o conteúdo (ex: um par de meias).
- O **Metadados**(`Query`) são as entiquetas coladas na caixa(ex: "Frágil,"Peso Máximo: 1kg").

```Python
from typing import Annotated
from fastapi import Query
# q é uma string opcional, mas se existir, deve ter no máximo 50 caracteres
q: Annotated [str | None, Query(max_length=50)] = None
```

## Validação Comuns de String

Dentro do `Query()`, você pode passar vários "guardas" para vigiar seu dados:

| Validação    | O que faz?               | Exemplo                       |
| ------------ | ------------------------ | ----------------------------- |
| `min_length` | Tamanho mínimo da string | Query(min_length=3)           |
| `max_length` | Tamanho máximo da string | Query(max_length=50)          |
| `pattern`    | Segue um padrão (Regex)  | Query(pattern="^fixedquery$") |

---

### Metadados para a Documentação

Você também pode usar o `Query` para deixar sua documentação (`/docs`) mais bonita e explicativa para outros programadores:

- `title`: Um título curto para o parâmetro.
- `description`: Uma explicação detalhada do que esse parâmetro faz
- `alias`: Um "apelido". Útil quando você que rum nome que o Python não aceita (ex: `item-query`  com hífen).
- `deprecated=True`:Avisa que esse parâmetro vai deixar de existir em breve.
---
## Recebendo Listas de Valores

se você quiser que o usuário envie vários valores para a mesma chave (ex:`q=foo&q=bar`),basta usar o tipo list:

```Python
@app.get("/items/")
async def read_item(q:Annotated[list[str] | None , Query()] = None)
		return {"q":q}
# Resultado: {"q":["foo"],["bar"]}
```

---
## Validação Personalizada (`AfterValidator`) 

se as regras básicas não forem suficientes, você pode criar uma função e usá-las com o `AfterValidator` do Pydantic (versão 2+)

**Exemplo**: Verificar se um ID começa sempre com "user-".

```Python
def validar_prefixo(v:str):
	if not v.startswith("user-")
		raise ValueError("Deve começar com user-")
	return v
#No parâmetro:
user_id: Annotated[str,AfterValidator(validar_prefixo)]
```