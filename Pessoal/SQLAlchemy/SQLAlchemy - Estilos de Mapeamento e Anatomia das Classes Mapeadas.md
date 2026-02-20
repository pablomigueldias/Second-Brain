
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

**Por que?** Porque para o SQLAlchemy, buscar algo no banco não é um "nascimento"(construção), é apenas uma "ressureição"(desserialização). O objeto já existia, ele só está sendo remontando na memória com os dados que vieram do disco

---

## Introspecção: O Raio-X do Objeto

Você pode usar a função `inspect()` para ver as entranhas de qualquer classe ou objeto mapeado. É como pedir um relatório médico completo:

- Ele te diz quais colunas foram alteradas.
- O que ainda não foi carregado do banco(lazy load).
- A qual sessão o objeto está conectado.

---
### Dica

Ao estudar mapeamentos, tente separar mentalmente o **Objeto Python** da **Tabela SQL**. o SQLAlchemy usa um objeto chamado `Mapper` pra ficar no meio do caminho traduzindo as ordens de um lado para o outro. Se você entender que a classe Python é apenas uma "fantasia" que o dado veste para passear no seu código, a lógica ORM fica muito mais clara.


