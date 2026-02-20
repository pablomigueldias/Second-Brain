
**Resumo (O que é?):** O Python é uma linguagem de programação dinamicamente tipada, o que significa que o interpretador não exige a declaração explícita de tipos (como texto, inteiro ou booleano) durante a criação de uma variável. No entanto, a partir da versão 3.6, o Python moderno introduziu o suporte aos _Type Hints_ (Dicas de Tipagem). Os _Type Hints_ permitem que o desenvolvedor declare explicitamente o tipo esperado de uma variável, parâmetro ou retorno de função. Embora os _Type Hints_ não alterem a execução em tempo real (runtime) do Python puro, eles são fundamentais para ferramentas de análise estática, autocompletar em IDEs modernas e, principalmente, formam a base de validação estrutural em frameworks modernos como o FastAPI e o Pydantic.

## Por que usar Type Hints no Python?

A adoção de _Type Hints_ no ecossistema Python resolve problemas críticos de desenvolvimento e manutenção de código, transformando IDEs (como VS Code ou PyCharm) em assistentes proativos. Sem a tipagem, a IDE desconhece a natureza da variável e não consegue oferecer suporte.

- **Autocompletar Inteligente (Intellisense):** Quando o desenvolvedor utiliza _Type Hints_, a IDE compreende o objeto e sugere instantaneamente os métodos corretos assim que o ponto (`.`) é digitado (ex: sugerir `.title()`, `.capitalize()` ou `.upper()` exclusivamente para strings).
    
- **Prevenção Estática de Erros:** O uso de _Type Hints_ permite que a IDE alerte o desenvolvedor sobre operações inválidas (como tentar somar um número inteiro com um texto) antes mesmo de o código Python ser executado.
    

### Exemplo Prático com e sem Type Hints


```Python
# Sem Type Hints: A IDE não sabe o que são first_name e last_name.
# O desenvolvedor fica sem ajuda para lembrar os métodos de string.
def get_full_name_antigo(first_name, last_name):
    return first_name.title() + ' ' + last_name.title()

# Com Type Hints: A IDE sabe exatamente que os parâmetros são strings (str).
def get_full_name_moderno(first_name: str, last_name: str) -> str:
    return first_name.title() + ' ' + last_name.title()
```

## Tipos Simples e Tipos Genéricos no Python

Além das tipagens básicas e primitivas (`str`, `int`, `float`, `bool`), o Python permite a tipagem de estruturas de dados que atuam como contêineres de outros valores, conhecidas como Tipos Genéricos. A partir do Python 3.9, o desenvolvedor pode declarar a tipagem interna dessas coleções utilizando colchetes `[]`.

- **Lista Tipada (`list`):** A declaração `list[str]` informa que a variável é uma lista onde cada elemento interno é obrigatoriamente uma string.
    
- **Dicionário Tipado (`dict`):** A declaração `dict[str, float]` informa que a variável é um dicionário onde a chave (key) é obrigatoriamente uma string e o valor (value) é um número decimal.
    
- **Tupla Tipada (`tuple`):** A declaração `tuple[int, int, str]` informa que a variável é uma tupla imutável contendo exatamente três elementos, obrigatoriamente nesta ordem: um inteiro, outro inteiro e um texto.
    

## Tipos Avançados no Python (Union e Optional)

Em cenários arquiteturais flexíveis, uma mesma variável Python pode assumir múltiplas naturezas diferentes. O Python lida com essas incertezas através de operadores de União e Opcionalidade.

### Union (União de Tipos)

A União ocorre quando um parâmetro de função ou variável pode aceitar validamente mais de um tipo de dado específico.

- **Sintaxe Moderna (Python 3.10+):** O desenvolvedor utiliza a barra vertical `|` como o operador lógico "OU" (ex: `item: int | str`).
    
- **Sintaxe Legada (Versões anteriores):** Exigia a importação da biblioteca `typing` (ex: `item: Union[int, str]`).
    

### Optional (Tipagem Possivelmente Nula)

A Opcionalidade ocorre quando um valor pode conter um tipo específico (como um texto) ou simplesmente estar ausente/vazio (representado pelo valor `None` no Python). O framework FastAPI utiliza largamente esta sintaxe para identificar se um campo de requisição é obrigatório ou opcional.

- **Sintaxe Moderna (Python 3.10+):** `name: str | None = None`
    
- **Sintaxe Legada (Versões anteriores):** `name: Optional[str] = None`
    

## Classes e Modelos Pydantic baseados em Type Hints

O poder real dos _Type Hints_ no ecossistema web moderno é destravado quando aliado a bibliotecas de validação de dados como o Pydantic. O desenvolvedor pode utilizar suas próprias classes como declarações de tipo. O framework FastAPI depende integralmente desta arquitetura.

### Exemplo de Type Hints com Pydantic BaseModel

```Python
from pydantic import BaseModel

# O BaseModel do Pydantic lê os Type Hints e cria um contrato de dados rígido
class User(BaseModel):
    id: int
    name: str = 'Pablo'
	
# O parâmetro 'user' exige estritamente um objeto que respeite o modelo User
def save_user(user: User):
    print(user.name)
```

Neste cenário de injeção de dependência, a biblioteca Pydantic utiliza os _Type Hints_ para garantir o _Type Casting_ (conversão automática). Se o cliente da API enviar o campo `id` como uma string `"123"`, o Pydantic converterá o dado automaticamente para o número inteiro `123`. Se a conversão for matematicamente impossível (ex: `"abacaxi"`), o Pydantic e o FastAPI gerarão um erro automático de validação para o usuário.