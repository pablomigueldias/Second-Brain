
Uma variável de ambiente é uma variável que vive **fora** do seu código Python. Ele mora no Sistema Operacional(Windows,Linux ou MacOS).

## 1. Por que usar isso?

Imagine que você tem uma senha para o seu banco de dados. Se você escrever a senha direto no código(`senha = "12345"`), e depois enviar esse código para o GitHub, todo mundo verá sua senha. com as **env vars**, você deixa a senha guardada no computador onde o servidor roda, e o código Python apenas a "pergunta" ao sistema.

#### Exemplo de Uso no Terminal

No Linux/MacOS(ou Git Bash)

```bash
export MEU_NOME="Pablo"
echo $MEU_NOME
```

No Windows (PowerShell):

```PowerShell
$Env:MEU_NOME = "Wade Wilson"
echo $Env:MEU_NOME
```
 ---
## 2. Lendo Variáveis de Ambiente no Python

para ler esses valores no seu código, usamos o módulo padrão `os`.

```Python
import os
# O segundo argumento ("Mundo") é o valor padrão caso a variável não exista
nome = os.getenv("MY_NAME","Mundo")
print(f'Olá {nome} do Python')
```

---
## 3. A Importante Varável `PATH`

O seu sistema operacional tem uma variável especial chamada `PATH`. Ela é uma lista de endereços(pastas) onde o sistema procura programas.

Quando você digita `python` ou `fastapi` no terminal:

1. O sistema olha para o `PATH`.
2. Ele percorre cada pasta listada lá procurando um arquivo chamado "python"
3. Ele executa o primeiro que encontrar.

**Dica**: Se você tentar rodar um comando e receber "Comando não encontrado", 99% das vezes é porque a pasta onde o programa está instalado não foi adicionado ao `PATH`

---
## 4. Pontos Importantes para o FastAPI

- **Tudo é texto**: Variáveis de ambiente são sempre strings. se você guardar `PORTA=8000`, o Python vai ler como `"8000"`. Você precisará converter para `int(8000)` se precisar de um número.
- **Segurança**: Nunca coloque senha ou chave de API no seu arquivo `.py`. Use variáveis de ambiente!