
Link do conteúdo: [Exemplo Diagrama Sequencial](https://www.youtube.com/watch?v=LeV6RO-6Tn4&list=PLucm8g_ezqNqCRGHGHoacCo6N1bfN7hXZ&index=9)

## Como criar um Diagrama de Sequência 

Passos recomendados para a criação de um diagrama de sequência:

1) Selecionar um Caso de Uso no Diagrama de casos de uso
2) Escrever uma descrição detalhada do que o caso de uso faz(sua narrativa).
3) Identificar os atores e objetos que interagem
4) Identificar as mensagens que os objetos trocam entre si
5) Determinar a sequência das mensagens
6) Determinar condições especiais(loops, fluxos, alternativos, etc.)
7) Desenhar o diagrama

## Sistema de Biblioteca

Exemplo de Diagrama de Casos de Uso: `Sistema de Biblioteca`

- Sistema permite cadastrar novos usuários(público geral e operadores do sistema)
- Sistema permite realizar empréstimo de livros
- Calcula multa por atraso na devolução dos livros
- Permite cadastrar novos títulos no acervo

Representado pelo diagrama de casos de uso a seguir.

Diagrama de Casos de Uso(fragmento)

![[Pasted image 20260105162324.png]]

## Identificar objetos e atores envolvidos

- Operador do sistema (bibliotecário)
- Sistema de Gerenciamento da Biblioteca
- Banco de dados do sistema

![[Pasted image 20260105162555.png]]
## Descrição detalhada do caso de uso

1) Operador requisita ao sistema a criação de um novo usuário
2) Operador seleciona o tipo de conta de usuário
3) Operador fornece os dados do usuário
4) Sistema verifica os dados no banco de dados
5) Nova conta de usuário é criada e gravada no BD
6) Sistema confirma a criação da conta

![[EXEMPLO2.png]]