
`pipx` É utilizado para instalar aplicações CLI do Python globalmente, mantendo-as isoladas em ambientes virtuais.
`pipx` Gerenciará atualizações e desinstalações quando usado para instalar o Poetry.
## 1 - **Instale o pipx**

Caso `pipx`ainda não esteja instalado, você pode seguir qualquer uma das opções nas [instruções oficiais de instalação do pipx](https://pipx.pypa.io/stable/installation/) . Qualquer versão atualizada do pipx `pipx`funcionará.

---

## 2 - Instalar o Poetry

```
pipx install poetry
```


---

## 3 - Instalar o Poetry (avançado)

> [!NOTE] Alerta
>
> Você pode pular esta etapa se simplesmente quiser a versão mais recente e já tiver instalado o Poetry conforme descrito na etapa anterior. Esta etapa detalha usos avançados deste método de instalação. Por exemplo, instalar o Poetry a partir do código-fonte, ter várias versões instaladas simultaneamente etc.

`pipx`É possível instalar diferentes versões do Poetry, usando a mesma sintaxe do pip:

```
pipx install poetry==1.8.4
```

`pipx`Também é possível instalar versões do Poetry em paralelo, o que facilita o teste de versões alternativas ou de pré-lançamento. Cada versão recebe um sufixo exclusivo, especificado pelo usuário, que será usado para criar um nome binário exclusivo:

```
pipx install --suffix=@1.8.4 poetry==1.8.4
poetry@1.8.4 --version
```

```
pipx install --suffix=@preview --pip-args=--pre poetry
poetry@preview --version
```

Por fim, `pipx`é possível instalar qualquer [especificação de requisito pip](https://pip.pypa.io/en/stable/cli/pip_install/) válida , o que permite a instalação da versão de desenvolvimento a partir de `git`, ou mesmo o teste local de solicitações de pull:
``
```
pipx install --suffix @main git+https://github.com/python-poetry/poetry.git@main
pipx install --suffix @pr1234 git+https://github.com/python-poetry/poetry.git@refs/pull/1234/head
```


---

## 4 - Atualização de Poetry

```
pipx upgrade poetry
```


---

## 5 - Desinstalar o Poetry

```
pipx uninstall poetry
```


