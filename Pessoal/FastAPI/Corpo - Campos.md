
Da mesma forma que usamos `Query` para validar a URL e `Path` para validar o caminho, usamos o `Field` para validar atributos dentro de um Modelo Pydantic.

## A Diferença Crucial de Importação 

Até agora, importávamos tudo de `fastapi`. Mas o `Field` mora na casa do vizinho o **Pydantic**.

```Python
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field 
```

## Para que server o `Field`?

Imagine que você tem um modelo `Item`

-  `nome: str` é muito genérico. Aceita qualquer texto
-  `preco: float` aceita qualquer número, inclusive `-50.00`(o que seria um prejuízo)

com o `Field`, você dita as regras do jogo:

```Python
class Item(BaseModel):
	name: str
	description: str | None = Field(
		default = None
		title = "Descrição do Item"
		max_length = 300
	)
	price: float = Field(
		gt=0 # Greater Than 0 (Maior que zero)
		description = "O preço deve ser positivo"
	)
```

## A Mesma "Sopa de Letrinhas"

A Boa notícia é que o `Field` funciona exatamente igual ao `Query` e `Path`. Você usa os mesmo códigos que já aprendeu:

- **Números** `gt`(maior que), `ge`(maior ou igual), `lt`(menor que), `le`(menor ou igual).
- **Texto**: `min_length`,`max_length`,`pattern`(Regex)
- **Documentação**: `title`, `description`

## Por que usar isso?

**Segurança**: Impede que dados inválidos (como preço negativo) entrem no seu banco de dados
**Documentação**: O FastAPI lê os  `description` dentro do `Field` e coloca automaticamente na página `/docs`. Seu front-end vai agradecer!