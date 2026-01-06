
## Configuração do projeto

Primeiro, vamos criar nosso novo projeto, vamos chamá-lo de `poetry-demo`,

```
poetry new poetry-demo
```

isso criará o `poetry-demo `diretório com o seguinte conteúdo:

```
poetry-demo
├── pyproject.toml
├── README.md
├── src
│   └── poetry_demo
│       └── __init__.py
└── tests
    └── __init__.py
```

O `pyproject.toml` é o arquivo mais importante aqui. Ele irá orquestrar seu projeto e suas dependências. Por enquanto, ele se parece com isto:

```
[project]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = [
    {name = "Sébastien Eustace", email = "sebastien@eustace.io"}
]
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

O Poetry pressupõe que seu pacote contenha um pacote com o mesmo nome `project.name` localizado na raiz do seu projeto. Caso contrário, preencha o campo `tool.poetry.packages` especificando seus pacotes e seus respectivos locais.

Da mesma forma, o arquivo tradicional `MANIFEST.in`é substituído pelas seções `project.readme``<project>` `tool.poetry.include`, `<project>` e ` <project>`. A seção `<project> ` também é preenchida implicitamente pelo seu arquivo `<project>`. Para obter a documentação completa sobre o formato do projeto, consulte a [seção `pyproject`](https://python-poetry.org/docs/pyproject/) da documentação.`tool.poetry.exclude``tool.poetry.exclude``.gitignore`

# Definindo uma versão do Python


> [!NOTE] Alerta
> Diferentemente de outros pacotes, o Poetry não instala automaticamente um interpretador Python. Se você deseja executar arquivos Python em seu pacote, como um script ou aplicativo, você precisa fornecer seu próprio interpretador Python para executá-los

O Poetry Exigirá que você especifique explicitamente quais versões do Python pretende suportar, e seu bloqueio universal garantirá que seu projeto seja instalável (e que todas as dependência declarem suporte para) todas as versões do Python suportadas. Novamente, é importante lembrar que -- diferentemente de outras dependências -- definir uma versão do Python significa apenas especificar quais versões do Python você pretende suportar.

por exemplo, neste `pyproject.toml`:

```
[project]
requires-python = ">=3.9"
```

Estamos permitindo qualquer versão do Python 3 que seja igual ou superior a `3.9.0`.

Ao executar o comendo `poetry install`, você precisa ter acesso a alguma versão de um interpretador Python que atenda a essa restrição e que esteja disponível em seu sistema. O Poetry não instará um interpretador Python para você.

## Inicializando um projeto pré-exixtente

Em vez de criar um novo projeto, o Poetry pode ser usado para 'inicializar' um diretório já existente. para criar um `pyproject.toml` arquivo interativamente no diretório `pre-existing-project`:

```
cd pre-existing-project
poetry init
```

## Modos de operação

O Poetry pode ser operado em dois modos diferentes. O modo padrão é o modo de pacote, que é o modo correto se você quiser empacotar projeto em um sdist ou um wheel e talvez publicá-lo em um índice de pacotes. Nesse modo, alguns metadados, como `<nome_do_projeto>` e `name` e `version` `<nome_do_projeto>`, que são necessários para o empacotamento, são obrigatórios. Além disso, o próprio projeto será instalado em modo editável ao executar o comento `poetry install` 

se você deseja usar o Poetry apenas para gerenciamento de dependências, mas não para empacotamento, pode usar o modo não empacotado:

```
[tool.poetry]
package-mode = false
```

Neste modo, metadados como `<nome_do_projeto>` `name` e `version` `<nome_do_projeto>` são opcionais. Portando não é possivel criar uma distribuição ou publicar o projeto em um índice de pacotes. Além disso, ao executar `poetry install`, o Poetry não tenta instalar o projeto em si, mas apenas suas dependências (assom como `poetry install`  `poetry install --no-root).

## Especificando dependências

Se você deseja adicionar dependências ao seu projeto, pode especificá-las na `project`secão.

```
[project]
# ...
dependencies = [
    "pendulum (>=2.1,<3.0)"
]
```

como você pode ver, ele utiliza um mapeamento de nomes de pacotes e restrições de versão.

O Poetry usa essas informações para buscar o conjunto correto de arquivos nos "repositórios" de pacotes que você registra na `tool.poetry.source` seção, ou no PyPi por padrão.

Além disso, em vez de modificar o `pyproject.toml` arquivo manualmente, você pode usar o `add` comando.

```
$ poetry add pendulum
```

Ele encontrará automaticamente um restrição de versão adequada e instalará o pacote e sua subdependências.

O Poetry oferece suporte a uma sintaxe rica para especificação de dependências, incluindo requisitos com acento circunflexo, til, curinga, desigualdade, e múltiplas restrições.

## Utilizando seu ambiente virtual

por padrão, o Poetry cria um ambiente virtual em `{cache-dir}/virtualenvs`. você pode alterar esse `cache-dir` editando a configuração do Poetry. Além disso, pode pode usar o `virtualenvs.in-project` variavel de configuração para criar ambiente virtuais dentro do diretório do seu projeto.

Existem diversas maneiras de executar comandos dentro desse ambiente virtual.


> [!NOTE] Gestão de ambiente virtual externo
> O Poetry detectará e respeitará um ambiente virtual existente que tenha sido ativado externamente. Este é um mecanismo poderoso que se visa ser uma alternativa ao gerenciamento de ambiente simplificado integrado ao Poetry
> 
> Para tirar proveito disso, basta ativar um ambiente virtual usando seu método ou ferramenta preferida, antes de executar quaisquer comendo do Poetry que esperam manipular um ambiente

## Usando poetry run

para executar seu script, basta usar `poetry run python your_script.py`. Da mesma forma, se você tiver ferramentas de linha de comandos como `pytest` ou `black` poderá executá-las usando `poetry run pytest`



> [!NOTE] Title
>Se você estiver gerenciando seu próprio ambiente virtual externamente, não precisa usar o comando `python` `poetry run`, pois presumivelmente já terá ativado esse ambiente virtual e disponibilizado a instância correta do Python. Por exemplo, estes comandos devem retornar o mesmo caminho do Python:
>
```
>conda activate your_env_name
which python
poetry run which python
poetry env activate
which python
```


## Ativar o ambiente virtual

Consulte [Ativando o ambiente virtual](https://python-poetry.org/docs/managing-environments/#activating-the-environment) .

## Restrição de Versão

Em nosso exemplo, estamos solicitando o `pendulum` pacote com a restrição de versão `>=2.1.0 <3.0.0`. isso significa qualquer versão maior ou igual a 2.1.0 e menor que 3.0.0 

Leia [a especificação de dependências](https://python-poetry.org/docs/dependency-specification/ "Documentação de especificação de dependências") para obter informações mais detalhadas sobre versões, como as versões se relacionam entre si e as diferentes maneiras de especificar dependências.


> [!NOTE] Como o Poetry baixa os arquivos corretos?
> 
> Ao especificar uma dependência em `pyproject.toml` poetry.properties, o Poetry primeiro pega o nome do pacote que você solicitou e o procura em qualquer repositório que você tenha registrado usando  a repositories chave `poetry.properties`. se você não tiver registrado nenhum repositório adicional, ou se o Poetry não encontrar um pacote com esse nome nos repositório especificados, ele recorrerá ao PyPI
> 
> Quando o Poetry encontra o pacote correto, ele tenta encontrar a melhor correspondência para a restrição de versão que você especificou.

## Instalando dependências

Para instalar as dependências definidas para o seu projeto, basta executar o [`install`](https://python-poetry.org/docs/cli/#install)comando.

```
poetry install
```

Ao executar este comando, uma de duas coisas pode acontecer:


### Instalação sem`poetry.lock`

Se você nunca executou o comando antes e também não há nenhum `poetry.lock`arquivo presente, o Poetry simplesmente resolve todas as dependências listadas no seu `pyproject.toml`arquivo e baixa a versão mais recente dos arquivos correspondentes.

Quando o Poetry terminar a instalação, ele gravará todos os pacotes e suas versões exatas baixadas em um `poetry.lock`arquivo, vinculando o projeto a essas versões específicas. Você deve adicionar esse `poetry.lock`arquivo ao repositório do seu projeto para que todos que trabalham nele usem as mesmas versões das dependências (mais detalhes abaixo).

### Instalando com`poetry.lock`

Isso nos leva ao segundo cenário. Se já existir um `poetry.lock`arquivo `.gitignore` e outro `pyproject.toml`arquivo `.gitignore` quando você executar `poetry install`o comando, significa que você já o executou `install`antes ou que outra pessoa no projeto o executou `install`e adicionou o `poetry.lock`arquivo ao projeto (o que é bom).

De qualquer forma, executar o comando `install`quando um `poetry.lock`arquivo está presente resolve e instala todas as dependências listadas nele `pyproject.toml`, mas o Poetry usa as versões exatas listadas `poetry.lock`para garantir que as versões dos pacotes sejam consistentes para todos que trabalham no seu projeto. Como resultado, você terá todas as dependências solicitadas pelo seu `pyproject.toml`arquivo, mas elas podem não estar nas versões mais recentes disponíveis (algumas dependências listadas no `poetry.lock`arquivo podem ter versões mais recentes lançadas desde a criação do arquivo). Isso é intencional e garante que seu projeto não seja interrompido devido a mudanças inesperadas nas dependências.

### Ao adicionar seu `poetry.lock`arquivo ao controle de versão


#### Como desenvolvedor de aplicativos

Os desenvolvedores de aplicativos se comprometem `poetry.lock`a obter versões mais reproduzíveis.

Fazer o commit deste arquivo no Visual C++ é importante porque fará com que qualquer pessoa que configure o projeto use exatamente as mesmas versões das dependências que você está usando. Seu servidor de CI, máquinas de produção, outros desenvolvedores da sua equipe, tudo e todos usarão as mesmas dependências, o que mitiga o potencial de bugs que afetam apenas algumas partes das implantações. Mesmo que você desenvolva sozinho, daqui a seis meses, ao reinstalar o projeto, você poderá ter certeza de que as dependências instaladas ainda estarão funcionando, mesmo que muitas novas versões tenham sido lançadas desde então. (Veja a nota abaixo sobre o uso do comando de atualização.)


>
> Se você adicionou a [`[build-system]`](https://python-poetry.org/docs/pyproject/#poetry-and-pep-517)seção recomendada ao arquivo pyproject.toml do seu projeto, poderá _instalar_ com sucesso o projeto e suas dependências em um ambiente virtual usando um comando como `pip `pip install -e .`install poet-core`. No entanto, o pip não usará o arquivo de bloqueio para determinar as versões das dependências, pois o sistema de compilação do poetry-core destina-se a desenvolvedores de bibliotecas (consulte a próxima seção).


#### Como desenvolvedor de bibliotecas[](https://python-poetry.org/docs/basic-usage/#as-a-library-developer)

Os desenvolvedores de bibliotecas têm mais coisas a considerar. Seus usuários são desenvolvedores de aplicativos, e sua biblioteca será executada em um ambiente Python que você não controla.

O aplicativo ignora o arquivo de bloqueio da sua biblioteca. Ele pode usar qualquer versão de dependência que atenda às restrições do seu arquivo de configuração `pyproject.toml`. O aplicativo provavelmente usará a versão de dependência compatível mais recente. Se a versão da sua biblioteca `poetry.lock`ficar desatualizada em relação a alguma nova versão de dependência que cause problemas para seus usuários, você provavelmente será o último a descobrir.

Uma maneira simples de evitar esse cenário é omitir o `poetry.lock`arquivo. No entanto, ao fazer isso, você sacrifica a reprodutibilidade e o desempenho até certo ponto. Sem um arquivo de bloqueio, pode ser difícil encontrar o motivo da falha nos testes, pois, além de alterações óbvias no código, uma atualização de biblioteca não detectada pode ser a culpada. Além disso, o Poetry precisará realizar o bloqueio antes de instalar uma dependência se o arquivo de bloqueio `poetry.lock`tiver sido omitido. Dependendo do número de dependências, esse processo pode levar um tempo considerável.

Se você não quiser abrir mão dos benefícios de reprodutibilidade e desempenho, considere uma atualização regular para `poetry.lock`manter o software atualizado e reduzir o risco de interrupções repentinas para os usuários.

### Instalando apenas as dependências

Se você deseja instalar apenas as dependências, execute o `install`comando com a `--no-root`flag:

```
poetry install --no-root
```

## Atualizando as dependências para as versões mais recentes.[](https://python-poetry.org/docs/basic-usage/#updating-dependencies-to-their-latest-versions)

Como mencionado acima, o `poetry.lock`arquivo impede que você obtenha automaticamente as versões mais recentes de suas dependências. Para atualizar para as versões mais recentes, use o `update`comando. Isso buscará as versões correspondentes mais recentes (de acordo com o seu `pyproject.toml`arquivo) e atualizará o arquivo de bloqueio com as novas versões. (Isso é equivalente a excluir o `poetry.lock`arquivo e executar o comando `install`novamente.)


> O Poetry exibirá um **aviso** ao executar um comando de instalação se `poetry.lock`os parâmetros `pyproject.toml` não estiverem sincronizados.
> 



