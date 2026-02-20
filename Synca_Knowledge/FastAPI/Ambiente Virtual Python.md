# Ambiente Virtual Python (venv)

**Resumo (O que é?):** O Ambiente Virtual Python (frequentemente criado com o módulo `venv`) funciona como um diretório isolado e privativo para as dependências de cada projeto de software. Uma analogia prática para o Ambiente Virtual Python é o gerenciamento de receitas culinárias: se um projeto exige uma versão antiga de uma biblioteca (como FastAPI) e outro exige uma versão mais recente, usar a instalação global do Python causará conflitos. O Ambiente Virtual Python resolve isso fornecendo uma cópia "limpa" e independente do interpretador Python para cada contexto.

## Por que usar o Ambiente Virtual Python?

A utilização de Ambientes Virtuais Python é uma prática fundamental no desenvolvimento de software pelos seguintes motivos:

- **Isolamento de Projetos:** O Ambiente Virtual Python garante que cada projeto mantenha suas próprias bibliotecas e versões, impedindo o vazamento de dependências entre projetos diferentes.
    
- **Organização do Sistema:** O Ambiente Virtual Python evita que o interpretador Python global do sistema operacional seja poluído com pacotes desnecessários ou conflitantes.
    
- **Segurança e Previsibilidade:** O isolamento promovido pelo Ambiente Virtual Python evita que uma atualização de pacote em um projeto quebre acidentalmente o funcionamento de todos os outros projetos da mesma máquina.
    

## Como Criar e Utilizar o Ambiente Virtual Python

### Criação do Ambiente Virtual Python

Para isolar um projeto, é necessário inicializar o Ambiente Virtual Python dentro da pasta raiz do projeto. O comando a seguir utiliza o módulo nativo `venv` para gerar uma pasta (tradicionalmente chamada `.venv`) que conterá os binários do Python isolado.


```Bash
python -m venv .venv
```

### Ativação do Ambiente Virtual Python

Após a criação, o Ambiente Virtual Python precisa ser explicitamente ativado no terminal. A ativação instrui a sessão atual do terminal a utilizar o interpretador Python isolado recém-criado em vez da versão global do sistema.

- **Ativação do Ambiente Virtual Python em sistemas Linux ou macOS:**
    
    
    ```Bash
    source .venv/bin/activate
    ```
    
- **Ativação do Ambiente Virtual Python em sistemas Windows (PowerShell):**

    ```PowerShell
    .venv\Scripts\activate
    ```

### Instalação de Pacotes no Ambiente Virtual Python

Uma vez que o Ambiente Virtual Python esteja ativado, qualquer comando de instalação utilizará o gerenciador de pacotes isolado. Os pacotes instalados com este método ficarão guardados exclusivamente dentro da pasta `.venv` do respectivo projeto.


```Bash
pip install "fastapi[standard]"
```

## Gerenciamento de Dependências com requirements.txt

O arquivo `requirements.txt` funciona como o manifesto oficial de dependências de um projeto Python. Este arquivo em conjunto com o Ambiente Virtual Python permite que o ecossistema exato do projeto seja replicado de forma determinística por outros desenvolvedores ou em servidores de produção.

### Exportar e Instalar Dependências do requirements.txt

- **Para registrar as dependências do Ambiente Virtual Python atual (criar a lista):**
    
    ```Bash
    pip freeze > requirements.txt
    ```
- **Para instalar as dependências de um arquivo `requirements.txt` em um novo Ambiente Virtual Python:**

    ```Bash
    pip install -r requirements.txt
    ```
    
## Como o Ambiente Virtual Python Funciona Internamente

O mecanismo subjacente do Ambiente Virtual Python baseia-se primordialmente na manipulação da variável de ambiente `PATH` do sistema operacional. Quando o desenvolvedor ativa o Ambiente Virtual Python, o script de ativação altera o sistema temporariamente, colocando o caminho da pasta isolada (ex: `.venv/bin`) no topo absoluto da lista do `PATH`. Desta forma, quando o computador busca pelo executável `python` ou `pip`, ele encontra primeiramente a versão pertencente ao Ambiente Virtual Python do projeto, ignorando completamente o Python instalado globalmente