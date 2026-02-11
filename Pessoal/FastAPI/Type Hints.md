
O Python é um linguagem dinamicamente tipada, o que significa que você normalmente não precisa dizer se uma variável é um texto ou um número. no entanto, o Python moderno (3.6+) suporta `type hints`(dicas de tipos), que permitem declarar explicitamente o tipo de uma variável

## 1. Porque usar Type Hints?

Imagina o que você esta escrevendo uma função para formatar nomes:

```Python
def get_full_name(first_name, last_name):
	full_name = fist_name.title() + '' + lasta_name.tile()
	return full_name
```

se você esquecer como se escreve o método que deixa a primeira letra maiúscula(`title()`,`capitaliza()`,`upper()`) o seu editor de código(como VS Code ou PyCharm) **não conseguirá te ajudar** porque ele não sabe se `first_name` é uma string, um número ou uma lista.

### A Solução: Adicionando Tipos

Ao mudar a definição para: `first_name: str, last_name:str`

Você esta dizendo: "Ei, editor, esses dois parâmetros serão sempre strings(`str`)".

### Benefícios imediatos:

- **Autocompletar**: O editor sugere métodos de strings assim que você digita um ponto(`.`).
-  **Prevenção de Erros**: O editor te avisa se você tentar somar um número com um texto antes mesmo de você rodar o código.

## 2. Tipos Simples e Tipos Genéricos

Além do básico (`str`, `int`, `float`, `bool`), temos estruturas que guardam outros valores, chamadas de `Genéricos`.

A partir do Python 3.9, você pode declarar o tipo que está dentro da lista usando colchetes []:

- **Lista**: `list[str]`(Uma lista onde cada item é uma string).
- **Dicionário**: `dict[str,float]`(Um dicionário onde a **chave** é string e o valor é um número decimal).
- **Tupla**:`tuple[int,int,str]`(Uma tupla com exatamente dois números e um texto nessa ordem).

## 3. Tipos Avançados: Union e Optional

Às vezes, uma variável pode ser mais de uma coisa.

**Union**(União)
se um parâmetro puder ser um número inteiro ou um texto:

- Python 3.10+ : `item: int | str`(Usa-se a barra vertical como 'ou').
- Versões anteriores: `Union[int,str]`

**Optional**(Possivelmente Nulo)
se um valor puder ser um texto ou simplesmente não existir (`None`):

- Python 3.10+:  `name:str | None = None`
- Ver




