
## SELECT: Buscando Informações

para ler dados, o SQLAlchemy usa função `select()`

- **A Analogia**: Imagine que o banco de dados é uma **Grande Biblioteca**
	- O `select(User)` diz: "Vá até a seção do Usuário".
	- O `.where()` é o seu **filtro**: "Traga apenas quem tem o nome 'Sandy' ".
	- O `session.scalars()`: é o **carrinho do bibliotecário**: ele pega os livros(objetos Python) e te entrega pronto pra ler.

```Python
stmt = select(User).where(User.name == "spongebob")

for user in session.scalars(stmt): 
	print(user)
```

* **Nota técnica:** O `scalars()` é usado quando queremos os objetos direto (o objeto `User`), e não uma linha bruta do banco.

---
## JOIN: Cruzando Dados

Às vezes você quer informações de dudas tabelas ao mesmo tempo

-  É como cruzar duas listas: uma lista de **Clientes** e uma lista de **Pedidos**. O `join` encontra onde eles se conectam (ex: o ID do cliente no pedido).

```Python
smt = select(Address).join(Address.user).where(User.name = "sandy")
```

Aqui estamos buscando endereços mais "espiando" a tabela de usuário para filtrar apenas os que pertencem à "sandy"

---
## Updates: A "Planilha Inteligente"

O SQLAlchemy tem um recurso incrível chamado **Unit of Work**. Ele monitora seus objetivos.

- Imagine uma planilha do Google Sheets. se você mudar o texto de uma célula, ele fica com uma marcação de "salvando..."
- No SQLAlchemy, se você alterar um atributo do objeto, a `session` percebe a mudança automaticamente. Você só precisa dar o `commit()` no final.

```Python
patrick.addresses.append(Address(email_address="patrickstar@sqla.org"))
sandy_address.email_address = "novo_email@sandy.com"
session.commit() # O SQLAlchemy gera o UPDATE e o INSERT sozinho aqui
```

---
## Deletes: Limpando a Casa

Existem duas formas principais:

1. `session.delete(objeto)`: Marca o objeto para ser excluído.
2. **Remover de uma lista**: Se você configurou o "cascade"(cascata), remover um endereço da lista do usuário pode apagá-lo do banco

**Importante**: O **Lazy Loading**(carregamento preguiçoso) acontece quando você acessa, por exemplo, `user.addresses`. O SQLAlchemy só vai ao banco buscar esse endereço exato no momento em que você toca naquela propriedade.

---
## Dica

Observe que o SQLAlchemy tenta ser **eficiente**. Ele não sai gritando com o banco de dados a cada linha de código que você escreve. Ele vai anotando tudo que você mudou e, no momento do `flush()` ou `commit()`, ele envia um "pacote" de instruções SQL de uma vez só.

Sempre que for alterar algo, pense:"Estou alterando o objeto Python primeiro, o banco só saberá disso quando eu assinar o contrato (commit)"