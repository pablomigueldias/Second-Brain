
## Os Dois Estilos de Mapeamento

O SQLAlchemy é flexivel e permite que você escolha como quer "casar" suas classes Python com as tabelas do banco. Existem dois estilos principais:

**Mapeamento Declarativo(O Moderno)**

É o que vimos até agora. você define a classe e a tabela **tudo no mesmo lugar**
- é como comprar um **móvel planejado**. você ja desenha o armário sabendo exatamente onde ele vai ficar na parede.
- É mais rápido, legível e funciona muito bem como ferramentas de checagem de tipo (como o Mypy).

**Mapeamento Imperativo**

Aqui, você cria uma classe Python pura de um lado e um objeto `Table` do outro, e depois "força" a união deles usando um método chamado `map_imperatively`.

- é como comprar uma **casa antiga**. Você tem a estrutura(o banco) e seus móveis(as classes), e precisa dar um jeito de encaixar um no outro manualmente.
- Útil se você tem classes prontas que não podem "saber" nada sobre banco de dados (desacoplamento total).

---
## Registro(The Registry)

Independente do estilo, desde a versão 1.4, todos os mapeamentos passam por um "Livro de Registro" central chamado `registry`. Ele é o cérebro que mantém a lista de todas as classes que o SQLAlchemy está vigiando.

---

## O Mistério do Construtor(__init__)

aqui está algo que confunde muita gente:

-  Quando você faz `user = User(name="Sponge")`, o SQLAlchemy cria automaticamente um `__init__` para você que aceita esse nomes como argumentos.
- Quando o SQLAlchemy busca um usuário no banco (`session.get`), ele **NÃO** chama o `__init__`!

**Por que?** Porque para o SQLAlchemy, buscar algo no banco não é um "nascimento"(construção), é apenas uma "ressureição"