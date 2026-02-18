
Assim como usamos `Query` para validar parâmetros de busca, usamos `Path` para validar parâmetros que fazem parte da URL. A sintaxe é muito parecida, mas com regras matemáticas.

## Importando o `Path`

Primeiro, precisamos importar o `Path` do FastAPI.

```Python
from fastapi import FastAPI, Path
```

A grande diferença entre `Query` e `Path` é : **Um `Path Parameter` é  SEMPRE obrigatório.** Não faz sentido ele ser opcional, porque se ele não estiver lá, a URL não existe.

## A "Sopa de Letrinhas" da Matemática

O FastAPI usa siglas em Inglês para definir as regras maior e menor. Aqui está o seu "dicionário de bolso":

| Sigla | Significado em Inglês | Tradução         | Símbolo Matematico |
| ----- | --------------------- | ---------------- | ------------------ |
| gt    | Greater Than          | Maior que        | `>`                |
| ge    | Greater Than or Equal | Maior ou Igual a | `>=`               |
| lt    | Less Than             | Menor que        | `<`                |
| le    | Less than or Equal    | Menor ou igual a | `<=`               |
**Exemplos Práticos**
- Idade(Maior ou igual a 18): `Path(ge=18)`
- Página do Livro(Maior que 0):`Path(gt=0)`
- Porcentagem(Entre 0 e 100): `Path(ge=0, le=100)`
## Como usar o código (com `Annotated`)

Vamos ver como fica uma rota que busca um item pelo ID, onde o ID precisa ser maior ou igual a 1:

```Python
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/itens/{item_id}")
async def ler_item(item_id: Annotated[int,Path(title="O ID do item",ge=1)]
):
	return {"item_id": item_id}
```

se o usuário tentar acessar `/itens/0` ou `/itens/-5`, o FastAPI barra a entrada e retorna um erro, antes mesmo de rodar sua função

## O Problema da Ordem(e como o `Annotated` resolve)

No Python, existe uma regras chata: em um função, parâmetros obrigatórios(sem valor padrão) não podem vir depois do parâmetros opcionais(com o valor padrão).

Antigamente, isso causava uma dor de cabeça para misturar Path(obrigatório) e Query (opcional), mas usando o `Annotated`, O Python não reclama, pois ele  entende que o valor padrão é gerenciado pelo FastAPI.

**Resumo**: Use sempre `Annotated` e você nunca terá problemas com a ordem dos parâmetros!

## Números Decimais(`float`)

As mesmas regras (`gt`,`lt`,etc). valem para números quebrados (`float`).

```Python
# O tamanho deve ser maior que 0 e menor que 10.5
size: Annotated[float, Query(gt=0, lt=10.5)]
```