
Para obter ajuda na linha de comando, basta executar o comando `poetry`para ver a lista completa de comandos e, em seguida, `--help`combinar qualquer um deles com outros comandos pode fornecer mais informações.

- `--verbose (-v|vv|vvv)`Aumentar o nível de detalhamento das mensagens: “-v” para saída normal, “-vv” para saída mais detalhada e “-vvv” para depuração.
- `--help (-h)`Exibir informações de ajuda.
- `--quiet (-q)`Não exibir nenhuma mensagem.
- `--ansi`Forçar saída ANSI.
- `--no-ansi`Desativar saída ANSI.
- `--version (-V)`Exibir a versão deste aplicativo.
- `--no-interaction (-n)`Não faça perguntas interativas.
- `--no-plugins`: Desativa os plugins.
- `--no-cache`: Desativa os caches de origem do Poetry.
- `--directory=DIRECTORY (-C)`: O diretório de trabalho para o comando Poetry (o padrão é o diretório de trabalho atual). Todos os argumentos da linha de comando serão resolvidos em relação ao diretório especificado.
- `--project=PROJECT (-P)`Especifique outro caminho como raiz do projeto. Todos os argumentos da linha de comando serão resolvidos em relação ao diretório de trabalho atual ou ao diretório especificado usando `--directory`a opção, se utilizada.

## sobre

O `about`comando exibe informações globais sobre o Poetry, incluindo a versão atual e a versão do `poetry-core`.

```
poetry about
```

## adicionar

O `add`comando adiciona os pacotes necessários ao seu sistema `pyproject.toml`e os instala.

Se você não especificar uma restrição de versão, o Poetry tentará usar a versão mais recente.

```
poetry add requests pendulum
```

Por padrão, um pacote é buscado apenas no [PyPI](https://pypi.org/) . Você pode modificar a fonte padrão (PyPI) ou adicionar e usar [Fontes de Pacotes Suplementares](https://python-poetry.org/docs/repositories/#supplemental-package-sources) ou [Fontes de Pacotes Explícitas](https://python-poetry.org/docs/repositories/#explicit-package-sources) .

Para obter mais informações, consulte a documentação [de fontes de pacotes](https://python-poetry.org/docs/repositories/#package-sources) .


Você também pode especificar uma restrição ao adicionar um pacote:

```
# Allow >=2.0.5, <3.0.0 versions
poetry add pendulum@^2.0.5

# Allow >=2.0.5, <2.1.0 versions
poetry add pendulum@~2.0.5

# Allow >=2.0.5 versions, without upper bound
poetry add "pendulum>=2.0.5"

# Allow only 2.0.5 version
poetry add pendulum==2.0.5
```

Se você tentar adicionar um pacote que já está presente, receberá um erro. No entanto, se você especificar uma restrição, como acima, a dependência será atualizada usando a restrição especificada.

Se você deseja obter a versão mais recente de uma dependência já presente, pode usar a `latest`restrição especial:

```
poetry add pendulum@latest
```

Você também pode adicionar `git`dependências:

```
poetry add git+https://github.com/sdispater/pendulum.git
```