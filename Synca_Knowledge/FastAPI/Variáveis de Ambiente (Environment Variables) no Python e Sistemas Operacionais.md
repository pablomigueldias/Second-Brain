
**Resumo (O que é?):** Uma Variável de Ambiente (frequentemente abreviada como _env var_) é uma variável de configuração que vive estritamente fora do código-fonte da aplicação (como um script Python). A Variável de Ambiente reside e é gerenciada diretamente pelo Sistema Operacional subjacente, seja ele Windows, Linux ou macOS.

## Por que utilizar Variáveis de Ambiente?

A utilização de Variáveis de Ambiente resolve problemas críticos de segurança e portabilidade no desenvolvimento de software. Se um desenvolvedor escrever senhas de banco de dados ou chaves de API diretamente no código-fonte (em formato _hardcoded_, como `senha = "12345"`) e enviar esse código para um repositório público como o GitHub, as credenciais ficarão expostas a terceiros. Com as Variáveis de Ambiente, a credencial sensível fica guardada com segurança no computador ou servidor onde a aplicação roda, e o código Python apenas "pergunta" o valor ao Sistema Operacional no momento da execução.

### Como Declarar Variáveis de Ambiente no Terminal

- **No Linux/MacOS (ou terminais Git Bash):** O desenvolvedor utiliza o comando `export` para definir a Variável de Ambiente e `echo` com o prefixo `$` para visualizá-la.
    
    
    ```Bash
    export MEU_NOME="Pablo"
    echo $MEU_NOME
    ```
    
- **No Windows (PowerShell):** O desenvolvedor utiliza o prefixo `$Env:` para atribuir e ler a Variável de Ambiente.
    
    
    ```PowerShell
    $Env:MEU_NOME = "Wade Wilson"
    echo $Env:MEU_NOME
    ```
    

## Lendo Variáveis de Ambiente no Python

Para que uma aplicação Python consiga acessar e ler os valores armazenados no Sistema Operacional, o desenvolvedor deve utilizar a biblioteca padrão `os`. A função `os.getenv()` é o método mais seguro para extrair e processar esses dados no código.

### Exemplo Prático de os.getenv()


```Python
import os

# O os.getenv busca a Variável de Ambiente "MY_NAME". 
# O segundo argumento ("Mundo") atua como um valor de fallback (padrão) caso a variável não exista no SO.
nome = os.getenv("MY_NAME", "Mundo")
print(f'Olá {nome} do Python')
```

## A Importância da Variável de Sistema PATH

Todo Sistema Operacional possui uma Variável de Ambiente nativa e especial chamada `PATH`. A variável `PATH` funciona como uma lista global de endereços (diretórios) onde o Sistema Operacional procura sistematicamente por programas e arquivos executáveis.

Quando o desenvolvedor digita um comando abstrato como `python` ou `fastapi` no terminal, o sistema segue um fluxo estrito:

1. O Sistema Operacional consulta imediatamente o conteúdo da variável `PATH`.
    
2. O sistema percorre cada pasta listada no `PATH` em ordem estrutural, procurando por um arquivo executável com o nome exato do comando solicitado (ex: "python").
    
3. O sistema interrompe a busca e executa o primeiro arquivo correspondente que encontrar.
    

_Nota de Troubleshooting:_ Se o terminal retornar um erro clássico de "Comando não encontrado", a causa principal (em 99% das ocorrências) é que a pasta onde o programa foi fisicamente instalado não foi adicionada adequadamente à variável `PATH` do Sistema Operacional.

## Variáveis de Ambiente no Contexto do FastAPI

Ao integrar Variáveis de Ambiente em projetos web (como APIs em FastAPI), o desenvolvedor deve observar duas regras arquiteturais:

- **Conversão de Tipos (Type Casting):** O Sistema Operacional armazena Variáveis de Ambiente estritamente como formatos de texto (strings). Se o desenvolvedor configurar a porta do servidor na máquina como `PORTA=8000`, o interpretador Python extrairá o valor como a string `"8000"`. É obrigatório converter o dado explicitamente (ex: `int(8000)`) para utilizá-lo em operações numéricas de rede.
    
- **Garantia de Segurança:** O desenvolvedor nunca deve inserir chaves de API, _tokens_ ou senhas em texto claro dentro de arquivos `.py` sob nenhuma circunstância. Estes dados operacionais sensíveis devem ser sempre injetados e resolvidos através de Variáveis de Ambiente.