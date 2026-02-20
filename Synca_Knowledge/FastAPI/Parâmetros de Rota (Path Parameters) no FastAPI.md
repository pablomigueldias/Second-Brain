
**Resumo (O que é?):** Os Parâmetros de Rota (ou _Path Parameters_) no framework FastAPI permitem a criação de endpoints dinâmicos e flexíveis na API. Em vez de o desenvolvedor registrar uma URL estática e individual para cada recurso do sistema (como criar uma rota separada para cada produto do banco de dados), o desenvolvedor define um Parâmetro de Rota na URL utilizando chaves `{}`. Este Parâmetro de Rota atua como um espaço reservado (_placeholder_) que captura o valor dinâmico inserido na URL pelo cliente e o repassa diretamente para a função Python processar a requisição.

## Declaração Básica de Parâmetros de Rota

A declaração de um Parâmetro de Rota ocorre diretamente no decorador da rota do FastAPI. O nome da variável definida entre as chaves `{}` na URL deve corresponder exatamente ao nome do parâmetro exigido na assinatura da função assíncrona.

### Exemplo de Rota Dinâmica Simples

```Python
from fastapi import FastAPI

app = FastAPI()

# O FastAPI captura qualquer valor após /itens/ e o injeta na variável item_id
@app.get("/itens/{item_id}")
async def ler_item(item_id: str):
    # Se a URL for /itens/celular, a função retorna {"item_id": "celular"}
    return {"item_id": item_id}
```

## A Tipagem no FastAPI (Conversão e Validação Automática)

O framework FastAPI utiliza os _Type Hints_ nativos do Python para automatizar tarefas complexas nos Parâmetros de Rota. Quando o desenvolvedor define a tipagem da variável (exemplo: `item_id: int`), o FastAPI executa duas operações de segurança simultâneas:

1. **Conversão Automática de Dados (_Type Casting_):** Mesmo que os dados trafeguem pela URL HTTP em formato de texto (string), o FastAPI converte automaticamente o valor extraído do Parâmetro de Rota para o tipo Python exigido (como transformar a string `"3"` no número inteiro `3`).
    
2. **Validação Rigorosa de Dados:** Se o cliente da API enviar um Parâmetro de Rota que não pode ser convertido (por exemplo, acessar a URL `/itens/abacaxi` em uma rota que exige um `int`), o FastAPI bloqueia a execução da função e devolve automaticamente um erro HTTP **422 Unprocessable Entity**, detalhando que o valor fornecido não é um número inteiro válido.
    

## A Ordem de Declaração das Rotas Importa

O motor de roteamento do FastAPI processa e avalia as rotas de cima para baixo na leitura do arquivo. Devido a este comportamento sequencial, uma falha arquitetural comum é permitir que um Parâmetro de Rota dinâmico "engula" (faça _shadowing_) uma rota estática. A regra de ouro no FastAPI é: **Rotas fixas e estáticas devem sempre ser declaradas antes das rotas dinâmicas que possuem os mesmos prefixos.**

### Exemplo de Conflito de Rotas no FastAPI

```Python
# ARQUITETURA INCORRETA: A rota dinâmica está acima da rota estática
@app.get("/usuarios/{user_id}") 
async def ler_usuario(user_id: str):
    # Se o cliente acessar /usuarios/eu, o FastAPI vai parar AQUI.
    # O FastAPI assumirá que "eu" é apenas mais um user_id dinâmico.
    return {"id": user_id}
	
@app.get("/usuarios/eu") 
async def ler_meu_usuario():
    # ESTA ROTA É INALCANÇÁVEL (Unreachable Code) devido à ordem.
    return {"id": "usuario_logado"}
```

## Valores Predefinidos em Parâmetros de Rota com Enum

Quando um Parâmetro de Rota deve aceitar apenas um conjunto estrito e limitado de opções (como selecionar um modelo de Machine Learning específico), o desenvolvedor deve utilizar a classe `Enum` nativa do Python. Ao tipar o Parâmetro de Rota com uma classe `Enum`, o FastAPI garante que apenas os valores enumerados sejam aceitos. Além disso, o FastAPI renderiza automaticamente um menu de seleção (_dropdown_) na documentação interativa do Swagger UI (`/docs`), facilitando os testes do Front-end.

### Exemplo de Parâmetro de Rota com Enum


```Python
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# A classe herda de str e Enum para garantir a tipagem correta no FastAPI
class NomeModelo(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
	
@app.get("/modelos/{nome_modelo}")
async def obter_modelo(nome_modelo: NomeModelo):
    # O FastAPI já validou que nome_modelo é estritamente uma das três opções
    return {"modelo": nome_modelo}
```

## Parâmetros de Rota que Contêm Caminhos de Arquivo (Path)

Em situações específicas onde o valor do Parâmetro de Rota precisa conter barras de diretório `/` (por exemplo, um caminho de arquivo como `fotos/viagem/rio.jpg`), o roteador padrão do FastAPI se confundirá, achando que as barras indicam novas sub-rotas. Para solucionar isso, o desenvolvedor deve utilizar o conversor especial `:path` diretamente dentro das chaves do Parâmetro de Rota.

### Exemplo de Parâmetro de Rota com Caminhos Internos


```Python
# O sufixo :path instrui o FastAPI a não quebrar a string ao encontrar barras '/'
@app.get("/arquivos/{file_path:path}")
async def ler_arquivo(file_path: str):
    # Se a URL for /arquivos/fotos/viagem/rio.jpg, file_path será "fotos/viagem/rio.jpg"
    return {"caminho_do_arquivo": file_path}
```