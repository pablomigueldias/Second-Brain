
# Comentário

Os comentário em Python começam com o caractere de cerquilha (#) e se estendem até o final da linha. Um comentário pode aparecer no início de uma linha ou após um espaço em branco ou código, mas não dentro de uma string literal. Um caractere de cerquilha dentro de uma string literal é apenas um caractere de cerquilha. como os comentários servem para esclarecer o código e não são interpretados pelo Python, eles podem ser omitidos ao digitar exemplos.

```
# este é o primeiro comentário
spam = 1  # e este é o segundo comentário
          # ... e agora é a terceira!
text = "# este não é um comentário porque esta dentro de uma citação"
```


# Números

O seu interpretador funciona como uma calculadora simpels: você pode digitar uma expressão nele e escreverá o valor. A sintaxe da expressão é direta: os operadores  `+`, `-` `*` e  `/`  podem ser usados para realizar operações aritméticas; parênteses (`)`) podem ser usados para agrupar.

```
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # Divisões sempre retorna um ponto flutuante
1.6
```

Os números inteiros (por exemplo , `1` , `2`, `3`) têm o tipo inteiro **int** , enquanto os números com parte fracionárias (por exemplo: `5.0`,`1.6`) tem o tipo decimal **float**.
Veremos mais sobre tipos numéricos posteriormente.

A divisão `/` sempre retorna um número de ponto flutante (float). para realizar a divisão inteira e obter o resultado inteiro, você pode usar o `//` operador  para calcular o resto, você pode usar `%`

```
>>> 17 / 3  # divisão classica que retorna um float
5.666666666666667
>>> 17 // 3  # divisão inteira que descarta a parte fracionaria
5
>>> 17 % 3  # O operador % que retorna o resto da divisão
2
>>> 5 * 3 + 2
17
```

Com python, é possível usar o `**` operador que calcula potência:

```
>>> 5 ** 2  # 5 Potencia de 2
25
>>> 2 ** 7  # 2 Potencia de 7
128
```

O sinal de igual  **=** é usado para atribuir um valor a uma variável. Depois disso, nenhum resultado é exibido antes do próximo prompt interativo:

```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

se uma variável não estiver "definida" (não tiver um valor atribuido), tentar usá-la resultará em um erro:

```
n 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

Há suporte completo para ponto flutuante; operadores com operados de tipos mistos convertem o operando inteiro em ponto flutuante: 

```
>>> 4 * 3.75 - 1
14.0
```

No modo interativo, a última expressão impressa é atribuída à variável `_`. Isso significa que, ao usar o Python como uma calculadora de mesa, é um pouco mais fácil continuar os cálculos, por exemplo:

```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

Essa variável dever ser tratada como somente leitura pelo usuário. Não atribua um valor a ela explicitamente -- você criaria uma variável local independente com os mesmo nome, mascarando a variável interna com seus comportamento específico.

Além de `int` e `float`, o Python suporta outros tipos de números, como `Decimal` e `Fraction`. O Python também possui suporte integrado para números complexos e usa o sufixo `j` ou `J` para indicar a parte imaginária (por exemplo, 1/2 `3+5j`)

# Texto

Python pode manipular texto (representado pelo tipo **str**, as chamadas "strings") bem como números. isso inclui caracteres "`!`", palavras "`Coelho`" , nomes "`Paris`", frases "", etc. "". Eles podem ser colocados entre aspas simples ('') ou aspas duplas ("") com o mesmo resultado. '`. . .`', "`. . .`"

```
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!"  # double quotes
Paris rabbit got your back :)! Yay!'
>>> '1975'  # digits and numerals enclosed in quotes are also strings
'1975'
```

para citar um citação, precisamos "escapar" as aspas, precedendo-as com `\`. Alternativamente, podemos usar o outro tipo de aspas:

```
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

No Shell do Python, a definição da string e a string de saída podem ter aparências diferentes. A **print()** função produz uma saída mais legível, omitindo as aspas e imprimindo caracteres especiais e de escape:

```
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s)  # with print(), special characters are interpreted, so \n produces new line
First line.
Second line.
```

se você não quiser que os caracteres precedidos por aspas `\` sejam interpretados como caracteres especiais, você pode usar strings brutas adicionando umas `r`aspa antes da primeira aspa:

```
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

Literais de string podem abranger várias linhas. Uma maneira de fazer isso é usando aspas triplas: `"` `"""..."""`ou `"\ `'''...'''`"`. Os caracteres de fim de linha são incluídos automaticamente na string, mas é possível evitar isso adicionando uma `\`quebra de linha no final da linha. No exemplo a seguir, a quebra de linha inicial não é incluída:

```
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

As sequências de caracteres podem ser concatenadas (coladas umas às outras) com o `+`operador e repetidas com `*`:

```
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

Duas ou mais _strings literais_ (ou seja, aquelas entre aspas) lado a lado são concatenadas automaticamente.

```
'Py' 'thon'
'Python'
```

Essa funcionalidade é particularmente útil quando você deseja quebrar sequências longas:

```
>>> text = ('Put several strings within parentheses '
        'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

Isso só funciona com dois valores literais, não com variáveis ​​ou expressões:

```
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```

Se você deseja concatenar variáveis ​​ou uma variável e um literal, use `+`:

```
>>> prefix + 'thon'
'Python'
```

As cadeias de caracteres podem ser _indexadas_ (subscritas), com o primeiro caractere tendo índice 0. Não existe um tipo de caractere separado; um caractere é simplesmente uma cadeia de caracteres de tamanho um:

```
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```

Os índices também podem ser números negativos, para começar a contagem da direita:

```
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
```

Além da indexação, _o fatiamento_ também é suportado. Enquanto a indexação é usada para obter caracteres individuais, _o fatiamento_ permite obter uma substring:

```
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

Os índices de fatiamento possuem valores padrão úteis; um primeiro índice omitido assume o valor zero por padrão, e um segundo índice omitido assume o tamanho da string que está sendo fatiada por padrão.

```
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>> word[-2:]  # characters from the second-last (included) to the end
'on'
```

Observe como o início está sempre incluído e o fim sempre excluído. Isso garante que seja sempre igual a :`s[:i] + s[i:]s`

```
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

Uma maneira de lembrar como funcionam os slices é pensar nos índices como apontando _entre_ caracteres, com a borda esquerda do primeiro caractere numerada como 0. Então, a borda direita do último caractere de uma string de _n_ caracteres tem índice _n_ , por exemplo:

```
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

A primeira linha de números indica a posição dos índices 0…6 na string; a segunda linha indica os índices negativos correspondentes. O trecho de _i_ a _j_ consiste em todos os caracteres entre as arestas rotuladas como _i_ e _j_ , respectivamente.

Para índices não negativos, o comprimento de uma fatia é a diferença entre os índices, se ambos estiverem dentro dos limites. Por exemplo, o comprimento de `word[1:3]`é 2.

Tentar usar um índice muito grande resultará em um erro:

```
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

No entanto, índices de fatiamento fora do intervalo são tratados de forma adequada quando usados ​​para fatiamento:

```
>>> word[4:42]
'on'
>>> word[42:]
''
```

As strings em Python não podem ser alteradas — elas são imutáveis . Portanto, atribuir um valor a uma posição indexada na string resulta em um erro:

```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Se você precisar de uma string diferente, crie uma nova:

```
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

A função integrada **len()** retorna o comprimento de uma string:

```
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

## Listas

Python reconhece diversos tipos de dados _compostos_ , usados ​​para agrupar outros valores. O mais versátil é a _lista_ , que pode ser escrita como uma lista de valores (itens) separados por vírgulas entre colchetes. Listas podem conter itens de tipos diferentes, mas geralmente todos os itens são do mesmo tipo.

```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

Assim como as strings (e todos os outros tipos de sequência predefinidos ), as listas podem ser indexadas e fatiadas:

```
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

As listas também suportam operações como concatenação:

```
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Ao contrário das strings, que são [imutáveis](https://docs.python.org/3/glossary.html#term-immutable) , as listas são um tipo [mutável](https://docs.python.org/3/glossary.html#term-mutable) , ou seja, é possível alterar seu conteúdo:

```
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

Você também pode adicionar novos itens ao final da lista, usando o _método_.

```
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

Em Python, a atribuição simples nunca copia dados. Quando você atribui uma lista a uma variável, a variável passa a se referir à _lista existente_ . Quaisquer alterações feitas na lista por meio de uma variável serão refletidas em todas as outras variáveis ​​que a referenciam.

```
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]
```

Todas as operações de fatiamento retornam uma nova lista contendo os elementos solicitados. Isso significa que o seguinte fatiamento retorna uma cópia superficial da lista:

```
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
["Red", "Green", "Blue", "Alpha"]
>>> rgba
["Red", "Green", "Blue", "Alph"]
```

A atribuição a fatias também é possível, podendo inclusive alterar o tamanho da lista ou limpá-la completamente:

```
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

A função integrada `len()`também se aplica a listas:

```
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

É possível aninhar listas (criar listas que contenham outras listas), por exemplo:

```
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

