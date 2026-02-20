
**Resumo (O que é?):**

Os Parâmetros de Consulta (ou _Query Parameters_) no framework FastAPI são variáveis dinâmicas enviadas pelo cliente através da URL da requisição HTTP. Diferente dos Parâmetros de Rota (Path Parameters) que ficam fixos e definem o caminho estrito do recurso, os Parâmetros de Consulta são anexados ao final da URL. Os Parâmetros de Consulta são amplamente utilizados no desenvolvimento de APIs para aplicar filtros, paginação ou opções de ordenação em listagens de dados, sem a necessidade de alterar a estrutura principal e hierárquica da rota.

## Como Identificar Parâmetros de Consulta na URL

A sintaxe dos Parâmetros de Consulta segue um padrão universal na arquitetura web. O navegador ou cliente HTTP constrói a URL utilizando caracteres especiais padronizados para separar o caminho principal dos dados de consulta dinâmicos.

- **O Separador Inicial (`?`):** O símbolo de interrogação indica que o caminho estático da URL terminou e que a declaração dos Parâmetros de Consulta começará a partir daquele ponto.
    
- **Chave e Valor (`chave=valor`):** Os Parâmetros de Consulta são sempre compostos por um par que conecta o nome da variável e o seu respectivo valor recebido (ex: `skip=0`).
    
- **O Conector (`&`):** O símbolo do "E comercial" (ampersand) serve para concatenar e separar múltiplos Parâmetros de Consulta independentes enviados na mesma URL (ex: `http://127.0.0.1:8000/items/?skip=0&limit=10`).
    

## Como o FastAPI Reconhece os Parâmetros de Consulta

O motor de injeção de dependências do FastAPI possui uma regra de inferência implícita simples e poderosa. Se o desenvolvedor declarar um parâmetro de tipagem primitiva na função da rota em Python, mas esse parâmetro **não estiver** mapeado na string da rota (dentro das chaves `{}` no decorador `@app.get()`), o FastAPI assumirá automaticamente que esta variável é um Parâmetro de Consulta.

### Exemplo de Reconhecimento Automático do FastAPI

```Python
from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"name": "Item 1"}, {"name": "Item 2"}, {"name": "Item 3"}]

# A string da rota NÃO possui variáveis mapeadas entre chaves {}
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # O FastAPI buscará automaticamente os valores 'skip' e 'limit' na URL após o sinal de interrogação '?'
    return fake_items_db[skip : skip + limit]
```

## Tipos de Parâmetros de Consulta: Obrigatórios vs Opcionais

O framework FastAPI define a obrigatoriedade de um Parâmetro de Consulta baseando-se estritamente em como o desenvolvedor define as dicas de tipagem (type hints) e os valores padrões na assinatura da função Python.

|**Categoria do Parâmetro de Consulta**|**Como declarar no código Python**|**Exemplo de captura na URL**|**Comportamento do FastAPI**|
|---|---|---|---|
|**Obrigatório**|`needy: str` (Sem valor padrão)|`?needy=quero_isso`|Se o cliente não enviar este Parâmetro de Consulta específico, o FastAPI recusa a requisição HTTP e retorna um erro automático de validação (campo obrigatório ausente).|
|**Com Valor Padrão**|`skip: int = 0` (Recebe `0` diretamente)|`?skip=5`|Se o cliente não enviar o Parâmetro de Consulta na URL, o FastAPI utilizará o valor `0` para a execução interna da função, sem gerar erros.|
|**Opcional**|`q: str \| None = None` (Tipado com `None`)|`?q=busca` ou nada enviado|O Parâmetro de Consulta pode estar completamente ausente. O FastAPI tratará a variável interna atribuindo o valor nulo `None`.|

## A Conversão Automática de Booleanos no FastAPI

O framework FastAPI executa um _type casting_ (conversão de tipo de dado) altamente inteligente para Parâmetros de Consulta definidos com a tipagem estrita `bool`. Se o desenvolvedor definir um parâmetro na rota como `short: bool = False`, o FastAPI será capaz de interceptar diversas strings comuns enviadas na URL e convertê-las adequadamente para o tipo booleano nativo do Python.

- **Valores interpretados pelo FastAPI como Verdadeiro (True):** O framework aceita `1`, `True`, `true`, `on` e `yes` (ex: `?short=on`).
    
- **Valores interpretados pelo FastAPI como Falso (False):** O framework aceita o valor padrão (ausência da variável na URL), `0`, `False`, `false` e `no` (ex: `?short=no`).
    

## Misturando Parâmetros de Rota e de Consulta

Em arquiteturas de API completas e estruturadas, é padrão que uma mesma requisição HTTP possua tanto Parâmetros de Rota quanto Parâmetros de Consulta atuando em conjunto. O FastAPI é inteligente o suficiente para distinguir e separar a origem de cada variável, mapeando os nomes dos parâmetros da função Python contra a string declarada no decorador da rota.

### Exemplo de Mistura de Parâmetros na Mesma Rota

```Python
from fastapi import FastAPI

app = FastAPI()

# O FastAPI identifica explicitamente 'user_id' e 'item_id' declarados no caminho
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,           # Classificado como Path Parameter (está textualmente na URL)
    item_id: str,           # Classificado como Path Parameter (está textualmente na URL)
    q: str | None = None,   # Classificado como Query Parameter (é opcional e NÃO está na string da URL)
    short: bool = False     # Classificado como Query Parameter (possui valor padrão e NÃO está na string da URL)
):
    # O FastAPI entrega as variáveis corretamente inferidas e já convertidas (int, str, bool)
    return {"user_id": user_id, "item_id": item_id, "q": q, "short": short}
```