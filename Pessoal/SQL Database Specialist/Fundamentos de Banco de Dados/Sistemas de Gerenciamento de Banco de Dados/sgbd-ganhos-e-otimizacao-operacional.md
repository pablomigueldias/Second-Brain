---
titulo: "SGBD: Ganhos e Otimização Operacional"
tags: [sgbd, banco-de-dados, otimizacao, sistema, conceitos, estudo, governanca]
data: 2026-09-26
fonte: "gravação (sistema)"
tipo: transcricao
duracao_min: 12
conceitos: [SGBD, Padronização de dados, Modelo relacional, Redução do tempo de desenvolvimento, Flexibilidade na manutenção, Abstração de dados, Economia de escala, DBA]
---

# SGBD: Ganhos e Otimização Operacional

> [!resumo] Do que se trata
> Esta aula detalha os ganhos ao utilizar um Sistema de Gerenciamento de Banco de Dados (SGBD), abordando a padronização da estrutura e inserção de dados para facilitar o acesso e a manutenção. Ela explica como o SGBD reduz o tempo de desenvolvimento ao assumir funções de gerenciamento e oferece flexibilidade na manutenção do esquema sem interromper a aplicação. Além disso, a aula discute a economia de escala resultante da automação e otimização do gerenciamento de dados.

## Para lembrar

- **A padronização da utilização do modelo relacional por um SGBD facilita o acesso, a manutenção e a leitura da estrutura dos dados, além de otimizar a geração de relatórios.**
- **SGBDs reduzem o tempo de desenvolvimento ao gerenciar funções de dados, permitindo que a aplicação utilize métodos mais simples como `query` para acesso a informações.**
- **A abstração de dados em um SGBD garante que modificações no esquema do banco de dados não interfiram na execução do programa, proporcionando flexibilidade na manutenção.**
- **A padronização de um SGBD torna as modificações no esquema mais flexíveis e otimizadas, muitas vezes sem a necessidade de derrubar a aplicação.**
- **A economia de escala é um ganho do SGBD, pois ele automatiza e otimiza o gerenciamento de dados, reduzindo custos operacionais e facilitando o controle de acessos.**

## O que esta nota responde

- Quais são os principais ganhos ao utilizar um SGBD?
- Como a padronização de dados em um SGBD contribui para a eficiência e manutenção?
- De que forma um SGBD impacta o tempo de desenvolvimento e a flexibilidade na manutenção de aplicações?

## Conceitos

**SGBD** · **Padronização de dados** · **Modelo relacional** · **Redução do tempo de desenvolvimento** · **Flexibilidade na manutenção** · **Abstração de dados** · **Economia de escala** · **DBA**

## Mapa da aula

| ⏱ | Assunto | Prova |
|---|---|---|
| `00:00` | SGBD: Ganhos e Padronização | ▪▪ |
| `04:20` | Padronização, Desenvolvimento, Manutenção | ▪▪ |
| `08:40` | Disponibilidade de Info Update | ▪▪ |

> [!nota] `▪▪▪` a aula disse que cai · `▪▪` dá para cobrar · `▪` contexto

## Quadro de definições

| Termo | Como a aula definiu |
|---|---|
| **Padronização de Dados** | Definir um padrão e uma estrutura específica para cada objeto, além de um tipo de dado associado a cada atributo ou propriedade característica deste objeto. |
| **Disponibilidade de Info Update** | Uma nova inserção ou atualização dentro do SGBD é refletida quase que automaticamente, de maneira imediata. O que se observa é um delay relacionado ao clock do sistema, ao tempo de puxar a informação da memória e persistir em HD, no disco. O sistema precisa processar essa informação, acessar o esquema, depois os dados, e então persistir a modificação através de consultas SQL. |

## Pegadinhas

- Embora o SGBD ofereça alta confiabilidade e segurança, acidentes ou falhas que corrompam dados ainda podem ocorrer, apenas é mais difícil que aconteçam.

## Teste-se

<details><summary>Qual o principal ganho da padronização de dados em um SGBD?</summary>

A padronização facilita o acesso e a manutenção dos dados, tornando-os mais fáceis de consumir e de manter, além de criar uma estrutura sólida e consistente para relatórios.

</details>

<details><summary>Como um SGBD contribui para a redução do tempo de desenvolvimento de uma aplicação?</summary>

O SGBD assume a função de gerenciamento dos dados, eliminando a necessidade de certas funções na aplicação e permitindo o uso de métodos mais abstratos para acesso às informações.

</details>

<details><summary>O que significa a flexibilidade na manutenção proporcionada por um SGBD?</summary>

Significa que modificações na base de dados ou no esquema não interferem na execução do programa, permitindo consultas independentes e aprimoramentos sem derrubar a aplicação.

</details>

<details><summary>Explique o conceito de 'Economia de Escala' ao usar um SGBD.</summary>

Refere-se à redução do custo operacional de gerenciamento, pois o SGBD automatiza e otimiza o gerenciamento de dados e acessos, resultando em baixa manutenção após o trabalho inicial de definição.

</details>

<details><summary>Segundo o texto, qual a relação entre SGBD e segurança dos dados?</summary>

SGBDs oferecem alta segurança e confiabilidade, tornando acidentes ou falhas que corrompam dados muito mais difíceis de ocorrer, embora não impossíveis.

</details>

<details><summary>Qual a definição de 'Disponibilidade de Info Update' no contexto de um SGBD?</summary>

É a reflexão quase imediata de novas inserções ou atualizações no SGBD, com um pequeno delay relacionado ao processamento do sistema para acessar e persistir a informação.

</details>

## Conteúdo

`⏱ 00:00`

Eu sei que já falei com vocês sobre as vantagens de se utilizar um SGBD, mas agora quero pontuar especificamente alguns ganhos que temos ao utilizar um sistema voltado para o gerenciamento de banco de dados.

### Ganhos ao Utilizar um SGBD

#### Padronização

A primeira questão é a **padronização**. Se cada um define a estrutura em sua aplicação e o gerenciamento dos dados dentro da sua aplicação de usuário, não há padronização quanto à estrutura. Cada um pode utilizar e modelar os dados da maneira que achar melhor, mais conveniente.

Quando utilizamos um SGBD, padronizamos a utilização do modelo relacional para persistir os dados que representam o seu contexto. Ganhamos em termos de acesso e manutenção desses dados, pela padronização. Quando definimos padronização para os dados, fica mais fácil de consumir e de manter.

Temos diversas vantagens atreladas a SGBDs. Quando conseguimos definir o tipo de dado para cada atributo, quando conseguimos definir dentro de uma organização como será a estrutura dentro daquele banco de dados, e às vezes, indo além, não só um SGBD, mas as boas práticas de como inserir os dados dentro do SGBD... Se em uma organização é definido que a inserção dos dados deve ser de uma forma específica.

> [!exemplo] Padronização na inserção de dados
> Em uma organização, pode ser definido que a inserção dos dados deve seguir um padrão específico. Por exemplo, o nome deve ter a primeira letra maiúscula e o restante minúsculo, ou então tudo maiúsculo.
> >
> Isso, embora pareça simples, facilita a vida ao consultar o banco.
> >
> Outro exemplo é o que acontece em determinados sites de compra: ao digitar o e-mail, o sistema mantém tudo em caixa alta. Isso é feito para evitar erros de digitação e a perda do e-mail, forçando um padrão de inserção de dados para prevenir inconsistências. Essa é outra maneira de utilizar as informações que serão persistidas nos bancos de dados.

A partir dessa padronização fornecida por um SGBD, conseguimos dispor essas informações de uma maneira visual e que todos entendam, porque o modelo já está bem definido e padronizado. Assim, os interessados saberão ler aquela estrutura. Além disso, facilita a geração e criação de relatórios.

Vamos pensar na padronização de estrutura de um SGBD, das informações que estão sendo persistidas ali, dentro de um banco de dados. Vamos olhar para as tabelas.

> [!exemplo] Estrutura padronizada de uma sessão
> Em um SGBD, a estrutura de uma sessão (a oferta de uma disciplina em um determinado período) é bem definida. Ela é caracterizada por:
> - identificador
> - número
> - semestre
> - ano
> - estrutura
> >
> Defino que para meu objeto de sessão, essa é a estrutura. Ela não vai variar, a menos que, em uma fase posterior, seja identificada a necessidade de acrescentar um novo atributo. Nesse caso, você entrará em contato com o DBA (Database Administrator), com as pessoas responsáveis pela manutenção do banco de dados, e verificará a possibilidade de modificação do esquema.
> >
> Mas, via de regra, você tem um padrão. Aquela é a estrutura definida, e você não tem como criar uma variante dela. Se você deixa isso a cargo da aplicação, a cargo da subjetividade do ser humano, cada um entende de uma maneira. E dessa forma, como cada um entende de uma maneira, você não tem dois algoritmos...

`⏱ 04:20`

você não tem dois algoritmos escritos de maneira idêntica. Quando se pega duas provas diferentes de duas pessoas com um algoritmo idêntico, até nas variáveis, isso é considerado cola.

Nesse sentido, o que se consegue é tirar essa subjetividade e definir um padrão, uma estrutura específica para cada objeto. Além disso, definimos também um tipo de dado associado a cada atributo, associado a cada propriedade característica deste objeto.

> [!definicao] Padronização de Dados
> Definir um padrão e uma estrutura específica para cada objeto, além de um tipo de dado associado a cada atributo ou propriedade característica deste objeto.

Por exemplo, se eu defino que o nome do curso é alfanumérico, vai ser dessa forma. Uma pessoa pode entender que o número do curso deve ser apenas numérico. Parece coisa simples, mas que, dentro de um dia a dia de persistência de dados, dificultaria demais se você tem dados que acabam sendo incompatíveis, mas que querem dizer a mesma coisa, aliás, querem representar o mesmo contexto. Isso dificulta a utilização e o consumo desses dados.

Assim, consegue-se criar uma estrutura sólida e consistente para a geração de relatórios a partir do SGBD.

### Redução do Tempo de Desenvolvimento

Temos também a questão da redução do tempo no desenvolvimento. Por exemplo, se a função de gerenciamento dos dados está agora a cargo do SGBD, existem funções que não são mais necessárias dentro da minha aplicação. Isso vai desde a estrutura de gerenciamento até, por exemplo, *features* da BP descontinuadas, como uma recuperação das informações.

> [!exemplo] Otimização com SGBD
> Ao invés de ter uma função mais complexa para acessar um arquivo e puxar as informações, utiliza-se um método que realiza uma `query`.
> >
> Se estiver utilizando `Spring Boot` em `Java`, por exemplo, é possível "abusar" disso, fazendo um `get` utilizando o `JPA Repository`. Assim, consegue-se abstrair e retirar *features* que seriam utilizadas na aplicação, reduzindo o tempo e otimizando recursos.

### Flexibilidade na Manutenção

A flexibilidade permite tornar o processo um pouco mais ágil. Pensemos assim: eu tenho a definição de requisitos, eu desenvolvo, eu testo e vou aprimorar aquela minha aplicação. Uma vez que ela entra em produção, qualquer tipo de aprimoramento se torna mais complexo, principalmente se for para modificação da estrutura de dados.

Quando o dado está isolado no programa, há uma flexibilidade bem maior. É possível realizar as consultas na base de dados de forma independente. Se houver alguma modificação na base de dados, no esquema ou no BD, isso não vai interferir na execução do programa. Obtém-se uma flexibilidade em termos de modificação nesse cenário.

> [!atenção] Modificações no Esquema
> Não é trivial fazer modificações no esquema do banco de dados, mas a padronização torna o processo mais flexível, mais fácil e mais otimizado.

Visto que não é necessário derrubar a aplicação para depois subi-la novamente, há um ganho bem grande. Com relação a um novo requisito ou alguma modificação no esquema, há uma grande flexibilidade.

> [!exemplo] Adição de Atributo
> Verificou-se que na tabela de estudante, na entidade `estudante`, deseja-se adicionar o ano em que o aluno cursou a matéria.
> >
> (Nota: Não se está levando em consideração redundância de informação ou a melhor maneira de modelar; é apenas uma simulação de caso em que se queira realizar a modificação e adicionar um novo atributo na tabela.)
> >
> Adicionar um novo atributo na tabela `estudante` fica muito mais fácil, pois, ao fazer a consulta via `SQL`, o sistema, baseado na teoria de conjuntos, não se preocupa com quantos atributos o estudante tem. Ele vai fazer um `select from` e puxar os dados.

`⏱ 08:40`

O `SQL` vai puxar aquelas informações, independentemente da quantidade de elementos que aquela entidade ou conjunto possui. Da mesma maneira, para curso, se eu quero adicionar a informação de coordenador, eu consigo adicionar sem interferir na minha aplicação.

> [!definicao] Disponibilidade de Info Update
> Uma nova inserção ou atualização dentro do SGBD é refletida quase que automaticamente, de maneira imediata.
> O que se observa é um delay relacionado ao clock do sistema, ao tempo de puxar a informação da memória e persistir em HD, no disco.
> O sistema precisa processar essa informação, acessar o esquema, depois os dados, e então persistir a modificação através de consultas `SQL`.

### Economia de Escala

Um outro ganho está relacionado à economia de escala, onde nós estamos baixando o custo operacional de gerenciamento. Se eu estou passando essa função para um sistema, esse sistema acaba sendo automatizado. Ele consegue definir o gerenciamento de maneira mais otimizada. Eu consigo definir os acessos àquele conteúdo, àqueles dados de uma maneira otimizada, definindo índices ou então uma busca mais específica.

Eu vou ter um trabalho inicial, com certeza, de definição de todos os requisitos e toda essa estrutura. Mas, uma vez feito, eu não preciso mais mexer teoricamente. A manutenção em cima daquele SGBD vai ser relativamente baixa porque, se não houver nenhum tipo de modificação no esquema e acesso aos dados (por exemplo, a não mudar os dados que eu preciso acessar mais rapidamente), eu não preciso modificar. Então, eu tenho uma economia, tanto em termos de recursos financeiros quanto de tempo, na parte de gerenciamento de todas as informações.

### Segurança e Confiabilidade

Além disso, como o SGBD é bem consolidado, eu tenho uma maior segurança. Os dados que estão persistidos ali vão ter um nível de confiabilidade muito alto. Dificilmente vai haver um acidente, uma falha que vai corromper seus dados.

> [!atenção] Confiabilidade do SGBD
> Embora o SGBD ofereça alta confiabilidade e segurança, não significa que acidentes ou falhas que corrompam dados não possam ocorrer. Apenas é mais difícil que aconteçam.

Nós temos uma série de vantagens e ganhos associados à utilização do SGBD.

## Relacionado

- [[sgbd-natureza-autodescritiva-esquema-e-catalogo]]
- [[sgbd-abordagens-e-caracteristicas-essenciais]]
- [[sgbd-vantagens-otimizacao-e-integridade-dos-dados]]
- [[../Introdução a Banco de Dados/bancos-de-dados-da-evolucao-ao-big-data]]
