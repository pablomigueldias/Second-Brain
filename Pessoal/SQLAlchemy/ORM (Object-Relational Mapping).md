
## O que é esse tal de ORM?

Imagine que você tem um **Dicionário de Tradução.**

-  No mundo **Python**, você gosta de lidar com **Objeto e Classes**(ex:`usuario.nome`)
-  No mundo do Banco de Dados, tudo são **Tabelas e Linhas**(SQL)

O ORM é o tradutor que permite que você crie uma classe em Python e, magicamente, o SQL Alchemy entenda que aquilo deve ser uma tabela no banco de dados.

---

## Mapeamento Declarativo (A Planta da Casa)


```Python
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
```

### A Fundação(`DeclarativeBase`)

```Python
class Base(DeclarativeBase):
	pass
```

Aqui você está criando a "raiz" de tudo. Todas as suas tabelas precisam herdar dessa classe `Base` para que o SQLAlchemy saiba: "Opa, essa classe aqui não é uma classe comum, ela representa uma tabela!".

### Definindo a Tabela(`User` e `Address`)

- `__tablename__`: É o nome real da tabela lá no banco de dados(ex: no Python a classe chama `User`, mas no SQL a tabela chama `user_account`).
- `Mapped[str]`: isso é uma novidade do SQLAlchemy 2.0. Eele usa as "Dicas de Tipo"(Type Hints) do Pyhton para dizer. "Essa coluna vai guardar texto(string)".
- mapped_column(): Aqui você dá os detalhes específicos da coluna.
	- `primary_key=True`: Diz que esse é o ID único da linha(como o CPF de um registro);
	- `ForeignKey`: Cria um vínculo. O `Address` diz: "Eu Pertenço ao ID tal da tabela `user_account`".

### O Relacionamento(`relationship`)

Imagine um fio de telefone ligando duas casas.

- O `User` tem uma lista de `addresses`(endereços).
- O `Address` tem um dono (`user`).
- O `relationship` não cria uma coluna física no banco, mas cria uma "atalho" no Python para você acessar os dados vinculados facilmente.

---
## Dica

Ao estudar ORM, **tente visualizar a tabela enquanto escreve a classe**. Sempre que vir `Mapped[int]`, pense: "isso vai virar uma coluna do tipo INTEGER no meu banco". A conexão mental entra a estrutura do objeto e a estrutura da tabela é o que faz dominar qualquer ORM (Django,SQLAlchemy ou Hibernate).

