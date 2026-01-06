
O Poetry permite especificar as dependências principais na [`project.dependencies`](https://python-poetry.org/docs/pyproject/#dependencies)seção `<main>` do seu arquivo `pyproject.toml` `poetry.json`, conforme a PEP 621. Por razões de compatibilidade com versões anteriores e para definir informações adicionais que são usadas apenas pelo Poetry, as [`tool.poetry.dependencies`](https://python-poetry.org/docs/pyproject/#dependencies-and-dependency-groups)seções `<main>` podem ser utilizadas.

Consulte [a especificação de dependências](https://python-poetry.org/docs/dependency-specification/) para obter mais informações.

## Grupos de dependência

O Poetry oferece uma maneira de **organizar** suas dependências em **grupos** .

As dependências declaradas `project.dependencies`respectivamente `tool.poetry.dependencies` fazem parte de um `main`grupo implícito. Essas dependências são necessárias para o seu projeto durante a execução.

Além das `main`dependências principais, você pode ter dependências que são necessárias apenas para testar seu projeto ou para gerar a documentação.

Para declarar um novo grupo de dependências, use uma `dependency-groups`seção de acordo com a PEP 735 ou uma `tool.poetry.group.<group>`seção onde < `<group>`nome_do_grupo_de_dependências> é o nome do seu grupo de dependências (por exemplo, <nome_do_grupo_de_dependências `test`>):

