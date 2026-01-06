
Link do conteúdo: [Classes](https://www.youtube.com/watch?v=JQSsqMCVi1k&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=2)

## Diagramas de Classes UML

Um diagrama de classes é usado para descrever a estrutura estática de classes no sistema, permitindo os atributos, operações(métodos) e os relacionamentos entre as classes.

Apresenta uma visão estática da organização das classes, definindo sua estrutura lógica.

É um dos diagramas mais populares, e serve como base para a construção de outros diagramas UML.

Basicamente, descrevem o que deve estar presente no sistema modelado.

## Classes, Atributos e Métodos

uma classe é uma representação de um item do mundo real, físico ou abstrato, na forma de um tipo de dados personalizado.

As classes possuem estruturas internas chamadas de Atributos e de Métodos

`Atributos` são usados para armazenar os dados dos objetos de uma classe

`Métodos` são operações, ou funções que a instância de classe pode executar

Uma instância de classe é chamada de Objeto.

## Classes, Atributos e Métodos - Exemplo

Classe:  Pessoa

Atributos: Altura, Nome, Idade, Peso

Métodos: Andar, Comer, Falar, Estudar, Dormir, Trabalhar

---
Objeto da Classe (Instância)

Atributos:

- Nome: Pablo
- Altura: 1,82
- Idade: 28
- Peso: 86 kg

## Representação de uma Classe

Representamos uma classe usando um diagrama dividido em três compartimentos:

- Nome: Inclui o nome e o estereótipo da classe (informação sobre a classe)
- Atributos: Lista de atributos da classe no formato nome:tipo ou nome:tipo=valor
- Operações: Lista de métodos da classe no formato método(parâmetro):tipo_retorno

## Visibilidade dos Membros (Atributos/Métodos)

Representamos a visibilidade dos atributos e das operações usando os modificadores de acesso a seguir:

- + Público
-  # Protegido
-  -  Privado
-  ~ Pacote
-  /  Derivado

## Representação de uma Classe

Exemplo: Representando uma classe Pessoa, que contém os atributos nome, sobrenome e dataNasc, além do método calculaIdade: 

![[Pasted image 20260101210047.png]]

## Relacionamento entre Classes

Um Relacionamento é uma conexão entre itens. Existem vários tipos de relacionamento possíveis entre classes:

- Dependência
- Associação
- Agregação
- Composição
- Generalização

Cada uma desses relacionamentos possui uma representação gráfica específica.


