
imagine que você tem dois projetos de culinária: um precisa de **muito açucar**(FastAPI versão antiga) e outro é **diet** (FastAPI versão nova). se você usar a mesma despensa (o Python global do seu PC) para os dois, você vai acabar estragando uma das receitas.

O **Ambiente Virtual** é como se fosse uma "cozinha privativa" para cada projeto.

### 1. Porque usar?

- **Isolamento**: Cada projeto tem sua próprias bibliotecas e versões.
- **Organizações**: Você não "suja" o Python principal do seu computador.
- **Segurança**: Evita que uma atualização em um projeto quebre todos os outros.

### 2. Como criar e usar

#### Passo 1: Criar o ambiente
Dentro da pasta do seu projeto, digite no terminal:

```Bash
python -m venv .venv
```

isso cria uma pasta chamada `.venv` que contém uma cópia "limpa" do Python.

#### Passo 2: Ativar o ambiente
Você precisa dizer ao seu terminal: "Ei, a partir de agora, use o Python dessa pasta!".

- **No Windowns(PowerShell)**:`.venv\Scripts\activate`
- **No Linux ou Mac**: `source .venv/bin/activate`

### Passo 3: Instalar as coisas
Agora, tudo o que você instalar com o `pip install` ficará guardado **apenas** dentro desse projeto.

```Bash
pip install "fastapi[standard]"
```

---
## 3. O arquivo `requirements.txt`

É a "lista de compras" do seu projeto. Com ele, se você passar seu código para um amigo, ele saberá exatamente o que instalar.

- **Para criar a lista**: `pip freeze > requirements.txt`
- **Para instalar a lista**:`pip install -r requirements.txt`
---
## 4. O que acontece "por baico do capô?"

Lembra da `PATH` ? quando você **ativa** o ambiente virtual, o Python apenas "trapaceia" o sistema e coloca a pasta `.venv/bin` no topo do seu `PATH`. Assim, o computador encontra o Python do seu projeto antes de encontrar o Python Global.