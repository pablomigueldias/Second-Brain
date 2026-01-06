
Link do conteúdo: [Casos de uso](https://www.youtube.com/watch?v=ePX-S4Leq7Y&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=4)

## O que são Casos de Uso

Sistemas não existem de forma isolada. Há a interação com humos ou máquinas.

De acordo com o Booch, Rumbaugh e Jacobson:

"Um Caso de Uso especifica o comportamento de um sistema (ou parte), e é uma descrição de um conjunto de sequência de ações para produzir um resultado observável do valo de um ator"

Usamos casos de uso para captar o comportamento pretendido de um sistema, sem especificar como esses comportamento é implementado.

---

Um caso de uso executa uma quantidade específica de trabalho, realizando algo que seja de valor para um ator, como o cálculo de um resultado, por exemplo.

Casos de uso pode ter variantes - casos de uso que são versões especializadas de outros casos, incluídos como parte de outro caso de uso ou ainda que estendam o comportamento de um caso base.

Representam aspectos do comportamento de uma classe e modelam Requisitos.

## Aplicações dos Casos de Uso

No geral, empregamos casos de uso com duas finalidades:

1) Definir Escopo - Visualizar e entender as funcionalidades presentes no sistema
2) Identificar Papéis - Identificar quem interage com o sistema e com quais funcionalidades essa interação ocorre
3) Os casos de uso NÃO são empregados para:
	- Detalhar a implementação de funcionalidades

## A Importância dos Casos de Uso

- Permite que os especialistas do domínio especifiquem sua visão externa de modo que desenvolvedores possam construir a visão interna.
- Permitem que os desenvolvedores abordem um elemento e o compreendam - como ele deve ser utilizado
- Servem como base para testar cada elemento.
--- 
## Casos de Uso: Assunto

Um Assunto é uma classe descrita por um conjunto de casos de uso.

No geral, representa um sistema ou um subsistema

Cada caso de uso modela um comportamento dessa classe, e em conjunto, eles descrevem o comportamento completo do assunto.

---
## Casos de Uso: Nomes

Todo caso de uso possui um nome que o identifica e diferencia dos demais casos de uso do sistema.

O nome é uma sequência de caracteres de texto, e deve ser único no pacote que o contém.

No geral, os nomes são expressões verbais ativas, que nomeiam um comportamento específico do sistema.

Exemplos de nomes de caso de uso:

- Fazer pedido
- Pagar Fatura
- Ler Sensor

---
## O que são Atores

Um caso de uso representa um requisito funcional do sistema, como um todo.

Envolve a interação de atores com o sistema. Um Ator representa um conjunto de papéis que os usuários dos casos de uso desempenham ao interagir com eles.

Atores podem ser humanos, organizações ou ainda sistemas automatizados(equipamentos, outros sistemas, etc.) e são elementos externos ao sistema.

![[Pasted image 20260102101032.png]]

## Atores e Casos de Uso

Atores se conectam a casos de uso por relação de associação, indicando que o ator e o caso de uso se comunicam entre si, com a possibilidade de enviarem e receberem mensagens.

Por exemplo, para um caso de uso "Fazer um Pedido" pode haver um ator "Cliente" que se comunica com o caso de uso por uma associação

O nome de um ator deve sempre informar seu papel, e não quem é representado.

![[Pasted image 20260102101437.png]]

---
## Como identificar atores

Podemos identificar os atores que farão parte de um caso de uso fazendo perguntas com:

- Que organizações, pessoas ou entidades vão usar o sistema ou são importantes para realização de funções?
- Quais sistemas se comunicam com o sistema desenvolvido?
- Quem pode se interessar por algum requisito funcional do sistema?
- Quem deve receber informações sobre ocorrências do sistema? 

Atores semelhantes devem ser organizados em uma hierarquia de generalização / especialização

---
# Como identificar os Casos de Uso

Para identificar casos de uso, podemos fazer perguntas como:
- Quais as funcionalidades pretendidas para o sistema?
- Elencar as necessidades e os objetivos de cada ator em relação ao sistema
- Quais informações o sistema precisa retornar?
- O sistema precisa realizar ações que se repetem no tempo?
- Considerando os requisitos funcionais, determinar um ou mais casos de uso que os implementem.

---
## Relacionamentos

Entre casos de uso e atores: Associação.

Entre casos de uso:
- Generalização
- Extensão / Estendido (extends)
- Inclusão (includes)

Já entre os atores podemos ter o relacionamento de Generalização

![[Pasted image 20260102103835.png]]

---
### Fluxo de Eventos

Especificamos o comportamento de um caso de uso com um Fluxo de Eventos. Nele incluiremos:

- Quando e como o caso de uso se inicia e termina
- Quando ele interage com os atores
- Os objetos transferidos
- Fluxo básico e fluxos alternativos do comportamento.

Obs.: Os fluxos de eventos podem ser especificados de vária maneiras, como:

- Texto informal(nosso exemplo)
- Tabela com pré-e pós condições
- Maquinas de estados
- Diagramas de atividades
- Pseudocódigo.
---

## Exemplo de Fluxo de Eventos: Validar Usuário

Fluxo Principal:

- Sistema solicita ao cliente seu numero de identificação (ID) e uma senha de acesso.
- Cliente digita seu ID e senha em um teclado numérico
- Cliente confirma as entradas, pressionando Enter.
- Sistema verifica ID e senhas fornecidos.
- Se ID for válido e senha corresponder, sistema reconhece usuário, permitindo sua entrada, finalizando caso de uso.

Fluxo Alternativo:

- Cliente fornece um ID ou senha inválidos.
- Neste caso, sistema reinicia o caso de uso.
- Se cliente fornecer credenciais erradas três vezes em sequência, sistema cancela transação, e bloqueia acesso do usuário por uma hora
- Sistema registra tentativa de acesso em log.

Outro fluxo alternativo:

- Cliente cancela a transação a qualquer momento, pressionando um botão Cancelar, exibido na tela.
- Não são realizadas alterações na conta do cliente
- Caso de uso é finalizado

Também existe o Fluxo de Exceção, empregado pra descrever possíveis restrições do sistema, como por exemplo não aceitar cartão com validade vencida.

---
