
**Resumo (O que é?):** Os Modelos para Parâmetros de Consulta (ou _Query Parameter Models_) no framework FastAPI representam um padrão arquitetural para agrupar múltiplos parâmetros de URL dentro de uma única classe de validação Pydantic. Em vez de declarar dezenas de variáveis soltas na assinatura da função da rota (uma abordagem análoga a tentar carregar dez laranjas equilibrando-as nos braços), o desenvolvedor encapsula todos os filtros em um único objeto estruturado (a "sacola"). O Modelo de Parâmetros de Consulta centraliza as regras de validação, melhora a legibilidade do código e simplifica a manutenção da API.

## Criação do Modelo de Parâmetros de Consulta com Pydantic

A criação de um Modelo de Parâmetros de Consulta utiliza a mesma classe `BaseModel` do ecossistema Pydantic que é utilizada para validar o Corpo da Requisição (Request Body JSON). Para definir regras de negócio estritas (como limites numéricos ou valores padrões), o desenvolvedor utiliza a ferramenta `Field` do Pydantic.

### Exemplo de Configuração de Filtros de Busca


```Python
from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

# O BaseModel define o contrato exato dos parâmetros de URL esperados
class FiltrosBusca(BaseModel):
    # O Pydantic Field restringe o limite para estar entre 1 e 100, com padrão 100
    limit: int = Field(100, gt=0, le=100) 
    
    # O Pydantic Field garante que o offset (paginação) seja positivo, com padrão 0
    offset: int = Field(0, ge=0) 
    
    # O tipo Literal do Python restringe a escolha apenas a valores específicos previstos
    order_by: Literal["data", "preco"] = "data" 
    
    # O tipo list permite capturar o mesmo parâmetro de URL múltiplas vezes (ex: ?tags=a&tags=b)
    tags: list[str] = []  
```

## Injeção do Modelo na Rota do FastAPI (O Segredo)

A grande diferença técnica reside em como o desenvolvedor instrui o framework FastAPI a ler os dados. Se o modelo Pydantic for injetado de forma pura na rota, o FastAPI assumirá por padrão que os dados virão do Corpo da Requisição (JSON Body). Para forçar a leitura diretamente da URL (Query String), é obrigatório o uso explícito da classe `Query()` dentro da tipagem `Annotated`.

### Exemplo Prático de Declaração na Rota

```Python
app = FastAPI()

@app.get("/items/")
async def buscar_itens(
    # O Annotated em conjunto com Query() altera o comportamento do FastAPI.
    # O FastAPI não buscará um JSON, mas sim uma URL como: 
    # http://localhost:8000/items/?limit=50&order_by=preco
    filtros: Annotated[FiltrosBusca, Query()]
):
    # A variável 'filtros' agora é um objeto validado pelo Pydantic com todos os dados da URL
    return filtros
```

## Restrição Rigorosa de Parâmetros de Consulta Extras (Forbid Extra)

O comportamento padrão do framework FastAPI e do Pydantic é ser tolerante a dados não mapeados: se o cliente enviar um parâmetro de URL inexistente no modelo (por exemplo, `?limit=10&coisa_aleatoria=xyz`), o FastAPI processa os dados conhecidos e ignora silenciosamente a chave `"coisa_aleatoria"`. Para cenários corporativos rigorosos, o desenvolvedor pode proibir completamente campos adicionais utilizando o dicionário interno `model_config` do Pydantic.

### Exemplo de Configuração de Proibição

```Python
from pydantic import BaseModel, Field

class FiltrosRigorosos(BaseModel):
    # A configuração extra="forbid" torna o Modelo Pydantic intolerante a parâmetros não declarados
    model_config = {"extra": "forbid"} 
    
    limit: int = Field(10)
```

Com a configuração `"extra": "forbid"`, se o cliente tentar enviar um parâmetro inventado na URL, o FastAPI e o Pydantic interrompem imediatamente o processamento e retornam ao usuário um erro HTTP detalhado do tipo `extra_forbidden`.