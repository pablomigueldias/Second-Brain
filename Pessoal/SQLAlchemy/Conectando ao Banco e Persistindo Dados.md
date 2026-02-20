
## O Engine:  A Ponte de Comunicação

O primeiro passo é criar o **Engine**(o motor). Ele é o objeto que sabe como se conectar ao seu banco de dados especificos(seja SQLite, PostgreSQL ou MySQL).

```Python
from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True)
```

-  `sqlite://`: Isso dia ao SQLAlchemy: "Crie um vando de dados SQLite que existe apenas na memória RAM(volátil)".
- `echo=True`: É o modo "fofoqueiro". Sempre que o SQLAchemy enviar um comando para o banco, ele vai imprimir esse comendo no seu terminal. É excelente para aprender!

---
## MetaData: Construindo as Tabelas

O comando abaixo é o que realmente "abre o terreno" e constrói as tabelas.

```Python
Base.metadata.create_all(engine)
```

- `Base.metadata`: É o catálogo onde todas as suas classes (User,Address) ficaram registradas;
- `.create_all(engine)`: Ele envia a ordem: "Ei, Engine, pegue esse catálogo e crie todas essas tabelas lá no banco de dados para mim!".

---
## Session

Para salver os dados, usamos a **Session**. Ela funciona como um "espaço de rascunho" ou um carrinho de compras.

```Python
from sqlalchemy.orm import Session

with Session(engine) as session: # 1. Criando o objeto (ainda apenas na memória do Python) patrick = User(name="patrick", fullname="Patrick Star")

# 2. Colocando no "carrinho" (ainda não salvou no disco!) session.add(patrick)
session.add()

# 3. O fechamento do negócio (agora sim, vai para o banco!)
session.commit()
```

- `with Session(engine) as session`: Usamos o `with`(Context Manager) para garantir que a conexão seja fechada automaticamente quando terminarmos. É como desligar a luz ao sair do quarto
- `session.add()`: Você avisa à sessão: "Fique de olho nesse objeto aqui, eu pretendo salvar ele".
- `session.commit()`: É o martelo do juiz. Ele diz: "Pode gravar permanentemente no banco de dados agora!".

---
### Dica

Tente pensar na **Session** como um **balcão de aeroporto**. Você chega, entrega a mala, mostra o passaporte e confere a passagem. Se você desistir da viagem antes de receber o bilhete final(`commit`), nada acontece e você volta para a casa com tudo. O `commit()` é o momento em que você entra no avião: a partir daí, a viagem é oficial e o banco de dados mudou de estado.

