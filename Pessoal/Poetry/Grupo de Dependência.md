
```
[dependency-groups]
test = [
    "pytest (>=8.0.0,<9.0.0)",
]
lint = [
    "ruff (>=0.11.0,<0.12.0)",
]
dev = [
    { include-group = "test" },
    { include-group = "lint" },
    "tox",
]
```

Neste exemplo, o `dev`grupo inclui todas as dependências dos grupos `test`e .`lint`

O [`add`](https://python-poetry.org/docs/cli/#add)comando é a maneira preferida de adicionar dependências a um grupo. Isso é feito usando a `--group (-G)`opção.

```
poetry add pytest --group test
```

Se o grupo ainda não existir, ele será criado automaticamente.

### Instalando dependências de grupo

**Por padrão** , as dependências de **todos os grupos não opcionais** serão instaladas ao executar o comando `poetry install`.


> [!NOTE] Alerta
> O conjunto padrão de dependências para um projeto inclui o `main`grupo implícito, bem como todos os grupos que não estão explicitamente marcados como um [grupo opcional](https://python-poetry.org/docs/managing-dependencies/#optional-groups) .


Você pode **excluir** um ou mais grupos com a `--without`opção:

```
poetry install --without test,docs
```

Você também pode optar por participar de [grupos opcionais](https://python-poetry.org/docs/managing-dependencies/#optional-groups) usando a `--with`opção:


```
poetry install --with docs
```



Quando usados ​​em conjunto, o grupo opcional `--dependencies` `--without`tem precedência sobre o grupo `--with``--dependencies`. Por exemplo, o comando a seguir instalará apenas as dependências especificadas no `test`grupo opcional.

```
poetry install --with test,docs --without docs
```

[[Gerenciando dependências]]
