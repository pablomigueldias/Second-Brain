
**Resumo (O que é?):** O Pydantic Field (ou apenas `Field`) é uma ferramenta da biblioteca Pydantic utilizada para validar, restringir e documentar os atributos internos de um modelo de dados (geralmente herdado de `BaseModel`). Da mesma forma que o framework FastAPI utiliza `Query` para validar parâmetros de URL e `Path` para validar caminhos de rota, o FastAPI exige o uso do Pydantic Field para ditar as regras do corpo (Body) da requisição JSON. O Pydantic Field evita que tipos genéricos aceitem dados logicamente incorretos, como um preço negativo ou um texto excessivamente longo.

## A Importação do Pydantic Field

A diferença crucial na arquitetura ao utilizar o Pydantic Field é a sua origem de importação. Diferente das ferramentas de validação de rotas que pertencem ao pacote principal do FastAPI, o Pydantic Field pertence ao ecossistema do Pydantic.


```Python
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field 
```

## Casos de Uso e Parâmetros do Pydantic Field

A grande vantagem do Pydantic Field é que ele compartilha exatamente a mesma "sopa de letrinhas" (nomenclatura de parâmetros) utilizada pelas funções `Query` e `Path` do FastAPI. O desenvolvedor utiliza os mesmos códigos para definir regras:

- **Validação de Números no Pydantic Field:** * `gt` (Greater Than / Maior que)
    
    - `ge` (Greater or Equal / Maior ou igual)
        
    - `lt` (Less Than / Menor que)
        
    - `le` (Less or Equal / Menor ou igual)
        
- **Validação de Texto no Pydantic Field:**
    
    - `min_length` (Tamanho mínimo de caracteres)
        
    - `max_length` (Tamanho máximo de caracteres)
        
    - `pattern` (Validação via Expressão Regular / Regex)
        
- **Documentação Embutida no Pydantic Field:**
    
    - `title` (Título amigável do campo)
        
    - `description` (Descrição detalhada do campo)
        

## Benefícios de Utilizar o Pydantic Field

A implementação do Pydantic Field em aplicações FastAPI garante duas vantagens fundamentais para a arquitetura do sistema:

1. **Segurança de Dados:** O Pydantic Field atua como um escudo, impedindo que dados inválidos, maliciosos ou logicamente impossíveis (como um prejuízo de `-50.00` em um campo de preço) cheguem à camada de banco de dados.
    
2. **Documentação Automática:** O FastAPI lê os parâmetros `title` e `description` configurados dentro do Pydantic Field e os injeta automaticamente na página interativa de documentação (`/docs` gerada pelo Swagger UI). Isso facilita enormemente a integração para a equipe de Front-end.
    

### Exemplo Prático de Código com Pydantic Field


```Python
# Definição do Modelo utilizando Pydantic Field para validação estrita
class Item(BaseModel):
    name: str
    
    # O Pydantic Field restringe o tamanho e documenta o campo
    description: str | None = Field(
        default=None,
        title="Descrição do Item",
        max_length=300
    )
    
    # O Pydantic Field garante que o preço nunca seja zero ou negativo
    price: float = Field(
        gt=0, 
        description="O preço deve ser estritamente positivo e maior que zero"
    )
```