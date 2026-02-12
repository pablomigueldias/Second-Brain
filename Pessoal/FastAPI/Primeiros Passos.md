
Para criar uma API com FastAPI, você só precisa de um arquivo ( vamos chamar de main.py) e cinco passos básicos.

## 1. O Código Mínimo

```Python
from fastapi import FastAPI # 1. importa a "ferramenta"

app = FastAPI() # 2. Cria o "chefe" do projeto (instância)

@app.get("/") # 3. Define o "onde" (rota) e o "como" (método)
async def root(): # 4. Define o que acontece (função)
	return {"message": "Hello World"} # 5. Entrega a resposta
```

---
## 2. Anatomia de um Rota(Path Operation)

Imagine que sua API é um **Restaurante**:

- **O Caminho (Path)**: é o endereço ou "mesa". no código acima, o caminho é `/`. se fosse `https://meusite.com/cardapio`, o caminho seria `/cardapio`.
- **A Operação (HTTP Method)**: É o tipo de pedido que o cliente faz.
	- `GET`: "Me dê informações"(ler o cardápio).
	- `POST`:"Crie alho novo"(fazer um pedido na cozinha).
	- `PUT`: "Atualize algo"(mudar o pedido).
	- `DELETe`: "Remova algo"(cancelar o pedido
- **O Decorador(`@app.get('/')`)**: Em Python, o `@` é como um chapéu decorativo. Ele diz ao FastAPI: "Ei, toda vez que alguém for ao endereço '/' usando o método 'GET', execute a função que está logo abaixo de mim."
---
## 3. Rodando o Servidor

para colocar o restaurante para funcionar, usamos o comando no terminal:

```Bash
fastapi dev main.py
```

isso vai abrir um servidor em `http://127.0.0.1:8000`.

-  **Dev Mode**: O FastAPI fica vigiando seu código. se você mudar uma vírgula e salvar, o servidor reinicia sozinho!

---
## 4. Documentação Automática

O FastAPI já vem com um "menu digital" pronto. Sem escrever uma linha a mais de código, você ganha:

1. **Swagger UI (`docs`)**: Uma página interativa onde você pode testar sua API clicando em botões.
2. **ReDoc(`/redoc`)**: Uma documentação mais limpa e organizada para leitura.
3. **OpenAPI(o"Mapa")**: O FastAPI gera um arquivo JSON (`openapi.json`) que descreve tudo o que sua API faz. É o "projeto arquitetônico" do seu sistema.
---
## 5. Porque usar `async def`?

Usamos o `async def` para que o servidor não fique parado esperando. Se a sua função for apenas devolver um texto simples. o FastAPI lida com isso na velocidade da luz!
