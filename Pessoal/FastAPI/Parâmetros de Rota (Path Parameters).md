
Às vezes você não quer uma rota estática(fixa), mais sim uma que mude dependendo do dado que você quer buscar. Por exemplo, em vez de criar uma rota para cada produto, você cria uma rota que aceita o **ID do produto**.

## O que são Parâmetros de Rota?

No FastAPI, você defina uma variável na URL usando chaves `{}`

```Python
@app.get("/itens/{item_id}")
async def (ler_item):
return {"item_id":item_id}
```

se você acessar `http://localhost:8000/itens/celular`, a função vai receber `"celular"` na variável `item_id`.

## A Mágica da Tipagem (Conversão e Validação)

Lembra do **Type Hints**? Aqui é onde eles trabalham pra você.

Se você declarar o tipo de parâmetro com `int`:

```Python
@app.get("/itens/{item_id}")
async def ler_item(item_id: int) # Declaramos como inteiro
	return {"item_id":item_id}
```

O FastAPI faz duas coisas automáticas:

1. **Conversão de Dados**: Mesmo que a URL envie o número como texto (`"3"`), o FastAPI converte para um `int` real do Pyhton.
2. **Validação de Dados**: Se alguém digitar `itens/abacaxi`, o FastAPI responde automaticamente com um erro **422 Unprocessable Entity**, explicando que "abacaxi" não é um número inteiro.
---
## A Ordem Importa

O FastAPI lê as rotas de **cima para baixo**. Se você tiver uma rota dinâmica e uma fica que se pareçam, a fixa dever vir **primeiro**.

```Python
# JEITO ERRADO
@app.get("/usuarios/{user_id}") # Esta rota 'engole' tudo
async def ler_usuario(user_id:str)
	return {"id":user_id}
	
@app.get("usuario/eu") # Esta rota nunca será alcançada!
async def ler_meu_usuario():
	return {"id":"usuario_logado"}
```

No exemplo acima, de você acessar `usuarios/eu`, o FastAPI vai achar que o seu `user_id` é a string `eu`. **Sempre coloque as rotas fixas antes das dinâmicas!**

---
## Valores Predefinidos com Enum

E se você quiser que o usuário escolha apenas entre opções específicas? Usamos o `Enum` do Python.

```Python
from enum import Enum

class NomeModelo(str,Enum)
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"
	
@app.get("/modelos/{nome_modelo}")
async def obter_modelo(nome_modelo: NomeModelo)
	return {"modelo": nome_modelo}
```

**Vantagem**: Na documentação interativa `/docs`, o FastAPI vai criar um menu de seleção (dropdown) com apenas essas 3 opções para o usuário escolher!

---

## Parâmetros que contêm "Caminhos"

Se você precisar que o parâmetro seja um caminho do arquivo (ex: `fotos/viagem/rio.jpg`), o FastAPI permite usar o formato `:path`.

```Python
@app.get("/arquivos/{file_path:path}")
async def ler_arquivo(file_path:str):
	return {"caminho_do_arquivo": file_path}
```
