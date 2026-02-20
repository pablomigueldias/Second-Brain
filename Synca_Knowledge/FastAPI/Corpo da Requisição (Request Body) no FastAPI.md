**Resumo (O que é?):**

O Corpo da Requisição (ou _Request Body_) é o pacote de dados enviado pelo cliente (como um navegador web ou aplicativo móvel) diretamente para a API. Diferente dos parâmetros passados pela URL (que são visualmente expostos e limitados pelo navegador), o Corpo da Requisição trafega de forma encapsulada na chamada HTTP (frequentemente no formato JSON). O Corpo da Requisição não possui restrições rígidas de tamanho de caracteres, sendo o mecanismo mais seguro e robusto para transmitir informações complexas, sigilosas ou extensas. O Corpo da Requisição é utilizado primordialmente nos métodos HTTP `POST` (para criação de dados) e `PUT` (para atualização de dados). O método HTTP `GET` não deve transportar um Corpo da Requisição (tentar enviar um pacote de dados em um `GET` é conceitualmente equivalente a tentar colocar uma melancia inteira dentro de um envelope de carta).

## Definição de Esquemas com Pydantic (BaseModel)

Para estabelecer o formato exato que a API deve esperar receber no Corpo da Requisição, o desenvolvimento em FastAPI utiliza a biblioteca de validação Pydantic. A modelagem de um Corpo da Requisição exige a criação de uma classe em Python que herde obrigatoriamente da classe `BaseModel` do Pydantic. Esta classe `BaseModel` atua como um contrato estrutural, definindo a tipagem obrigatória ou opcional de cada dado.

### Exemplo de Modelagem com BaseModel

```Python
from pydantic import BaseModel

# A classe Item dita a estrutura exata do Corpo da Requisição
class Item(BaseModel):
    name: str
    description: str | None = None # Campo opcional
    price: float
    tax: float | None = None # Campo opcional

# A classe Aluno dita a estrutura exata para um escopo educacional
class Aluno(BaseModel):
    nome: str
    idade: int
    plano: str | None = None
```

## O Processamento Automático do FastAPI

Para interceptar o Corpo da Requisição, o desenvolvedor declara a classe Pydantic como um parâmetro diretamente na assinatura da função da rota. Ao receber o envio do cliente, o FastAPI executa quatro rotinas subjacentes automaticamente:

1. **Leitura de Carga Útil (Payload):** O FastAPI lê e extrai o JSON bruto contido no Corpo da Requisição.
    
2. **Conversão de Tipos (Type Casting):** O FastAPI converte dados incompatíveis para a tipagem exigida pela classe (por exemplo, se o cliente enviar o preço como uma string `"45.5"`, o FastAPI converte o dado nativamente para um `float`).
    
3. **Validação de Estrutura:** O FastAPI valida as regras estipuladas no `BaseModel`. Se o cliente não enviar um campo obrigatório (como o atributo `name`), o FastAPI recusa o processamento e devolve um erro detalhado automaticamente para o cliente.
    
4. **Intellisense (Autocompletar na IDE):** O FastAPI, em conjunto com o Pydantic, permite que o editor de código (como o VS Code) sugira automaticamente os atributos mapeados (`name`, `price`) ao manipular a variável dentro do bloco da função.
    

### Exemplo de Captura do Corpo da Requisição

```Python

@app.post("/items/")
async def create_item(item: Item):
    # A variável 'item' agora é um objeto Python seguro e completamente validado
    return item
```

## Integração: Body Parameter, Path Parameter e Query Parameter

O framework FastAPI possui um mecanismo interno de inferência altamente capaz de distinguir a origem de múltiplos dados em uma única requisição HTTP. O FastAPI classifica e extrai os parâmetros baseando-se em sua posição na rota e em sua tipagem Python:

|**Característica do Parâmetro na Função**|**Classificação Automática do FastAPI**|**Como o FastAPI extrai a informação**|
|---|---|---|
|O parâmetro está declarado explicitamente dentro da string da rota (ex: `/items/{item_id}`).|**Path Parameter** (Parâmetro de Caminho)|O FastAPI retira o valor da própria barra de endereço da URL.|
|O parâmetro está declarado com um tipo primitivo simples (ex: `int`, `str`, `bool`).|**Query Parameter** (Parâmetro de Consulta)|O FastAPI busca o valor na URL após o símbolo de interrogação `?`.|
|O parâmetro está declarado com uma tipagem de classe Pydantic (`BaseModel`).|**Request Body** (Corpo da Requisição)|O FastAPI extrai o conteúdo do JSON enviado no pacote da requisição HTTP.|

### Exemplo Prático com Múltiplas Entradas (Mix de Parâmetros)


```Python
# A rota sinaliza a espera de um identificador na própria URL
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    # Lógica de extração do FastAPI:
    # item_id -> Vem do caminho da URL (Path Parameter)
    # item -> Vem do payload JSON validado (Request Body)
    # q -> Vem da interrogação na URL (Query Parameter)
    
    return {"item_id": item_id, **item.model_dump(), "q": q}
```