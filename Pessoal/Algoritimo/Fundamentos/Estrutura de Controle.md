
# `if` 

Talvez o tipo de declaração mais conhecido seja o `if`. Por exemplo:

```
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>> if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

More
```

pode haver zero ou mais `elif` e o `else` é opcional. A palavra-chave `elif` é uma abreviação de 'else if' para evitar endentação excessiva. uma sequência de if... elif...elif... é um substituído para as instruções `switch` ou `case` encontradas em outras linguagens.

# `for` 

o `for` em python difere um pouco do que você pode estar acostumado em vez de sempre iterar sobre uma progressão aritmética de números, ou dar ao usuário a capacidade de definir tanto o passo de iteração quanto a condição de parada, o for em python itera sobre os itens de qualquer sequência(uma lista ou uma string), na ordem em que aparecem na sequência.

```
# Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
    print(w, len(w))

cat 3
window 6
defenestrate 12
```

Códigos que modificam uma coleção enquanto iteram sobre ela podem ser complicados de implementar corretamente. em vez disso, geralmente é mais simples iterar sobre uma cópia de coleção ou criar uma nova coleção.

```
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

## Função range()

Se você precisa iterar sobre uma sequência de números, a função integrar range( ) é muito útil. ela gera progressões aritméticas:

```
for i in range(5):
    print(i)
0
1
2
3
4
```

O ponto final fornecido nunca faz parte da sequência gerada; `range(10)`gera 10 valores, os índices válidos para itens de uma sequência de comprimento 10. É possível definir o início do intervalo em outro número ou especificar um incremento diferente (inclusive negativo; às vezes chamado de "passo"):

```
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```

Para iterar sobre os índices de uma sequência, você pode combinar [`range()`](https://docs.python.org/3/library/stdtypes.html#range "faixa")`e` [`len()`](https://docs.python.org/3/library/functions.html#len "len")da seguinte forma:

```
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

0 Mary
1 had
2 a
3 little
4 lamb
```

Na maioria desses casos, porém, é conveniente usar a [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "enumerar") função, veja [Técnicas de Repetição](https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms) .

Algo estranho acontece se você simplesmente imprimir um intervalo:

```
range(10)
range(0, 10)
```

Em muitos aspectos, o objeto retornado [`range()`](https://docs.python.org/3/library/stdtypes.html#range "faixa")se comporta como se fosse uma lista, mas na verdade não é. Trata-se de um objeto que retorna os itens sucessivos da sequência desejada quando você itera sobre ele, mas ele não compõe a lista de fato, economizando espaço.

Dizemos que tal objeto é [iterável](https://docs.python.org/3/glossary.html#term-iterable) , isto é, adequado como alvo para funções e construções que esperam algo do qual possam obter itens sucessivos até que o suprimento se esgote. Vimos que a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)instrução é uma construção desse tipo, enquanto um exemplo de função que recebe um iterável é [`sum()`](https://docs.python.org/3/library/functions.html#sum "soma"):

```
sum(range(4))  # 0 + 1 + 2 + 3
6
```

Mais adiante, veremos mais funções que retornam iteráveis ​​e recebem iteráveis ​​como argumentos. No capítulo [Estruturas de Dados](https://docs.python.org/3/tutorial/datastructures.html#tut-structures) , discutiremos isso com mais detalhes [`list()`](https://docs.python.org/3/library/stdtypes.html#list "lista").

# `break` e `continue`

O break rompe com o envolvimento `for` ou `while` mais interno

```
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
```

O continue continue com a próxima iteração do loop:

```
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## `esle` sobre loops

Em um laço `for``or`, a instrução pode ser combinada com uma cláusula `if`. Se o laço terminar sem executar o `if` , a cláusula `if` será executada.`while``break``else``break``else`

Em um [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)loop, a `else`cláusula é executada após o término da última iteração do loop, ou seja, se nenhuma interrupção ocorreu.

Em um [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)loop, ele é executado depois que a condição do loop se torna falsa.

Em qualquer tipo de loop, a `else`cláusula **não** é executada se o loop for encerrado por um `if` [`break`](https://docs.python.org/3/reference/simple_stmts.html#break). Obviamente, outras maneiras de encerrar o loop antecipadamente, como um `if` [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)ou uma exceção lançada, também evitarão a execução da [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)cláusula.

Isso é exemplificado no seguinte `for`loop, que busca por números primos:


```
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

(Sim, este é o código correto. Observe atentamente: a `else`cláusula pertence ao `for`laço, **não** à `if`instrução.)

Uma maneira de pensar na cláusula `else` é imaginá-la emparelhada com o `if` `if` dentro do loop. Conforme o loop é executado, ele percorrerá uma sequência como `if/if/if/else`. O `if` `if`está dentro do loop e é encontrado várias vezes. Se a condição for verdadeira em algum momento, um `if` `break`ocorrerá. Se a condição nunca for verdadeira, a `else`cláusula fora do loop será executada.

Quando usada com um laço, a `else`cláusula tem mais em comum com a `else` cláusula de uma [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)instrução do que com a de `if` outras instruções: a cláusula `try`de uma instrução `else`é executada quando nenhuma exceção ocorre, e a `else`cláusula de um laço é executada quando nenhuma `break`exceção ocorre.

## `pass`

A [`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass)instrução não faz nada. Ela pode ser usada quando uma instrução é sintaticamente necessária, mas o programa não requer nenhuma ação

```
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
```

Isso é comumente usado para criar classes mínimas:

```
class MyEmptyClass:
    pass
```

Outro [`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass)uso possível é como um marcador para uma função ou corpo condicional ao trabalhar em um novo código, permitindo que você continue pensando em um nível mais abstrato. O `is` `pass`é ignorado silenciosamente.

```
def initlog(*args):
    pass   # Remember to implement this!
```

Para este último caso, muitas pessoas usam o literal de reticências `...`em vez de `& `pass``. Esse uso não tem nenhum significado especial para Python e não faz parte da definição da linguagem (você poderia usar qualquer expressão constante aqui), mas `...`também é usado convencionalmente como um corpo de texto de exemplo.

## `match`

Uma [`match`](https://docs.python.org/3/reference/compound_stmts.html#match)instrução `switch` recebe uma expressão e compara seu valor a padrões sucessivos fornecidos como um ou mais blocos `case`. Isso é superficialmente semelhante a uma instrução `switch` em C, Java ou JavaScript (e muitas outras linguagens), mas é mais parecido com o casamento de padrões em linguagens como Rust ou Haskell. Apenas o primeiro padrão que corresponde é executado, e a instrução também pode extrair componentes (elementos de sequência ou atributos de objeto) do valor para variáveis. Se nenhum caso corresponder, nenhum dos ramos é executado.

```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

Observe o último bloco: o “nome da variável” `_`funciona como um _caractere curinga_ e sempre encontra correspondência.

Você pode combinar vários literais em um único padrão usando `|`(“ou”):

```
case 401 | 403 | 404:
    return "Not allowed"
```

Os padrões podem se assemelhar a atribuições de desempacotamento e podem ser usados ​​para vincular variáveis:

```
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

Estude isso com atenção! O primeiro padrão tem dois literais e pode ser considerado uma extensão do padrão literal mostrado acima. Mas os dois padrões seguintes combinam um literal e uma variável, e a variável _associa_ um valor do sujeito ( `point`). O quarto padrão captura dois valores, o que o torna conceitualmente semelhante à atribuição de desempacotamento .`(x, y) = point`

Se você estiver usando classes para estruturar seus dados, poderá usar o nome da classe seguido por uma lista de argumentos semelhante a um construtor, mas com a capacidade de capturar atributos em variáveis:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

Você pode usar parâmetros posicionais com algumas classes internas que fornecem uma ordem para seus atributos (por exemplo, dataclasses). Você também pode definir uma posição específica para atributos em padrões, configurando o `__match_args__`atributo especial em suas classes. Se estiver definido como (“x”, “y”), os seguintes padrões são todos equivalentes (e todos vinculam o `y`atributo à `var`variável):

```
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
```

Uma maneira recomendada de ler padrões é observá-los como uma extensão do que você colocaria à esquerda de uma atribuição, para entender quais variáveis ​​seriam definidas com quais valores. Somente os nomes independentes (como `var`acima) são atribuídos por uma instrução `match`. Nomes com pontos (como ` `foo.bar`_`), nomes de atributos (como `_` `x=`e `y=``_` acima) ou nomes de classes (reconhecidos pelos “(…)” ao lado deles, como `Point`acima) nunca são atribuídos.

Os padrões podem ser aninhados arbitrariamente. Por exemplo, se tivermos uma lista curta de Pontos, com `__match_args__`valores adicionados, poderíamos fazer a correspondência assim:

```
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```

Podemos adicionar uma `if`cláusula a um padrão, conhecida como "guarda". Se a guarda for falsa, `match`o programa tenta o próximo bloco `case`. Observe que a captura de valor ocorre antes da avaliação da guarda:

```
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

Diversas outras características importantes desta declaração:

- Assim como na desempacotamento de atribuições, os padrões de tupla e lista têm exatamente o mesmo significado e, de fato, correspondem a sequências arbitrárias. Uma exceção importante é que eles não correspondem a iteradores ou strings.
    
- Os padrões de sequência suportam desempacotamento estendido e funcionam de forma semelhante às atribuições de desempacotamento. O nome após também pode ser , portanto, corresponde a uma sequência de pelo menos dois itens sem vincular os itens restantes.`[x, y, *rest]``(x, y, *rest)``*``_``(x, y, *_)`
    
- Padrões de mapeamento: captura os valores de um dicionário. Ao contrário dos padrões de sequência, chaves extras são ignoradas. Um desempacotamento como também é suportado (mas seria redundante, portanto não é permitido).`{"bandwidth": b, "latency": l}``"bandwidth"``"latency"``**rest``**_`
    
- Os subpadrões podem ser capturados usando a `as`palavra-chave:

```
case (Point(x1, y1), Point(x2, y2) as p2): ...
```

- irá capturar o segundo elemento da entrada como `p2`(desde que a entrada seja uma sequência de dois pontos)
    
- A maioria dos literais são comparados por igualdade, porém os singletons `True`, `False`e `None`são comparados por identidade.
    
- Os padrões podem usar constantes nomeadas. Esses nomes devem ser precedidos por pontos para evitar que sejam interpretados como variáveis ​​de captura:

```
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
```

## Definição de Função

Podemos criar uma função que escreva a série de Fibonacci em um limite arbitrário:

```
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

A palavra-chave `function` [`def`](https://docs.python.org/3/reference/compound_stmts.html#def)introduz a _definição_ de uma função . Ela deve ser seguida pelo nome da função e pela lista de parâmetros formais entre parênteses. As instruções que formam o corpo da função começam na linha seguinte e devem ser indentadas.

É simples escrever uma função que retorne uma lista dos números da sequência de Fibonacci, em vez de imprimi-la:

```
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

Este exemplo, como de costume, demonstra alguns novos recursos do Python:

- A [`return`](https://docs.python.org/3/reference/simple_stmts.html#return)instrução retorna um valor de uma função. `return`Sem um argumento de expressão, retorna `None`. Sair do final de uma função também retorna `None`.
    
- A instrução `result.append(a)`chama um _método_ do objeto lista `result`. Um método é uma função que "pertence" a um objeto e é nomeado como `obj.methodname`, onde `obj`é algum objeto (que pode ser uma expressão) e `methodname`é o nome de um método definido pelo tipo do objeto. Tipos diferentes definem métodos diferentes. Métodos de tipos diferentes podem ter o mesmo nome sem causar ambiguidade. (É possível definir seus próprios tipos de objeto e métodos, usando _classes_ , veja [Classes](https://docs.python.org/3/tutorial/classes.html#tut-classes) ). O método [`append()`](https://docs.python.org/3/library/stdtypes.html#list.append "lista.adicionar")mostrado no exemplo é definido para objetos lista; ele adiciona um novo elemento ao final da lista. Neste exemplo, ele é equivalente a , mas mais eficiente.`result = result + [a]`


## Mais sobre funções

Também é possível definir funções com um número variável de argumentos. Existem três formas, que podem ser combinadas.

### valores de argumentos padrão

A forma mais útil é especificar um valor padrão para um ou mais argumentos. Isso cria uma função que pode ser chamada com menos argumentos do que o permitido por sua definição. Por exemplo:

```
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

Essa função pode ser chamada de diversas maneiras:

- Apresentando apenas o argumento obrigatório: `ask_ok('Do you really want to quit?')`
    
- Indicando um dos argumentos opcionais: `ask_ok('OK to overwrite the file?', 2)`
    
- ou até mesmo apresentando todos os argumentos: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`
    

Este exemplo também introduz a [`in`](https://docs.python.org/3/reference/expressions.html#in)palavra-chave. Ela testa se uma sequência contém ou não um determinado valor.

Os valores padrão são avaliados no ponto de definição da função, no escopo _de definição_ , de modo que

```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```

irá imprimir `5`.

**Aviso importante:** O valor padrão é avaliado apenas uma vez. Isso faz diferença quando o valor padrão é um objeto mutável, como uma lista, um dicionário ou instâncias da maioria das classes. Por exemplo, a função a seguir acumula os argumentos passados ​​a ela em chamadas subsequentes:

```
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

Isso será impresso.

```
[1]
[1, 2]
[1, 2, 3]
```

Se você não quiser que o valor padrão seja compartilhado entre chamadas subsequentes, você pode escrever a função assim:

```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

### palavra-chave no argumento

As funções também podem ser chamadas usando [argumentos nomeados](https://docs.python.org/3/glossary.html#term-keyword-argument) no formato `kwarg=value`. Por exemplo, a seguinte função:

```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

Aceita um argumento obrigatório ( `voltage`) e três argumentos opcionais ( `state`, `action`, e `type`). Esta função pode ser chamada de qualquer uma das seguintes maneiras:

```
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

mas todas as chamadas seguintes seriam inválidas:

```
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```

Em uma chamada de função, os argumentos nomeados devem seguir os argumentos posicionais. Todos os argumentos nomeados passados ​​devem corresponder a um dos argumentos aceitos pela função (por exemplo, `a` `actor`não é um argumento válido para a `parrot`função), e a ordem deles não importa. Isso também inclui argumentos não opcionais (por exemplo, `b` `parrot(voltage=1000)`também é válido). Nenhum argumento pode receber um valor mais de uma vez. Aqui está um exemplo que falha devido a essa restrição:

```
def function(a):
    pass

function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
```

Quando um parâmetro formal final da forma `<parameter>` `**name`está presente, ele recebe um dicionário (consulte [Tipos de Mapeamento — dict](https://docs.python.org/3/library/stdtypes.html#typesmapping) ) contendo todos os argumentos nomeados, exceto aqueles correspondentes a um parâmetro formal. Isso pode ser combinado com um parâmetro formal da forma `<parameter> `*name`` (descrito na próxima subseção), que recebe uma [tupla](https://docs.python.org/3/tutorial/datastructures.html#tut-tuples) contendo os argumentos posicionais além da lista de parâmetros formais. (`<parameter> ` `*name`deve ocorrer antes de `<parameter> `**name``.) Por exemplo, se definirmos uma função como esta:

```
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

Poderia ser chamado assim:

```
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

e, claro, seria impresso:

```
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```


### parâmetros especiais

Por padrão, os argumentos podem ser passados ​​para uma função Python por posição ou explicitamente por palavra-chave. Para maior legibilidade e melhor desempenho, faz sentido restringir a forma como os argumentos podem ser passados, de modo que um desenvolvedor precise apenas consultar a definição da função para determinar se os itens são passados ​​por posição, por posição e palavra-chave, ou apenas por palavra-chave.

A definição de uma função pode ter a seguinte aparência:

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

onde `positional` `/`e `*``keyword` são opcionais. Se usados, esses símbolos indicam o tipo de parâmetro pela forma como os argumentos podem ser passados ​​para a função: somente posicional, posicional ou por palavra-chave e somente por palavra-chave. Parâmetros por palavra-chave também são chamados de parâmetros nomeados.