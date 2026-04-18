---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - banco_de_dados
  - sql
  - stored_procedure
aliases:
  - Stored Procedures no RM Reports
  - Aula 11 RM Reports
---

#  Aula #011 - TOTVS RM - RM Reports: Stored Procedure

**Fonte:** [AULA #011 - TOTVS RM - RM Reports - Stored Procedure](https://www.youtube.com/watch?v=yTTzyiu2u2Q)
**Instrutor:** Renato Barbero

## Visão Geral
Nesta aula avançada, o instrutor demonstra como integrar o RM Reports com o banco de dados (SQL Server) executando uma **Stored Procedure**. O cenário prático é a simulação de um reajuste salarial: a SP recebe a porcentagem de aumento, faz os cálculos, salva em uma tabela customizada (auxiliar), e o RM Reports consome e exibe esse resultado.

---
### O que é uma Stored Procedure (SP)?

Em bancos de dados relacionais (como SQL Server, PostgreSQL, Oracle), uma **Stored Procedure** (ou Procedimento Armazenado) é essencialmente um script ou um lote de códigos SQL que fica salvo e pré-compilado dentro do próprio servidor de banco de dados.

**Pense nela como uma "Função" no Back-end:** Em vez de você enviar um comando SQL gigante e complexo a partir da sua aplicação (ou do RM Reports) toda vez que precisar de um dado, você cria essa rotina lá no banco e dá um nome a ela. Depois, você apenas "chama" essa rotina.

**Vantagens de usar Stored Procedures:**

1. **Lógica Complexa:** Diferente de uma simples consulta (`SELECT`), uma SP permite usar lógica de programação dentro do banco de dados (`IF/ELSE`, `WHILE`, variáveis, criar e apagar tabelas temporárias, fazer cálculos avançados linha a linha).
    
2. **Performance:** Como ela fica armazenada no servidor, o plano de execução dela já fica otimizado ("cacheado"). O banco já sabe a melhor rota para executar aquele código.
    
3. **Segurança:** Você pode dar permissão para o usuário do sistema apenas _executar_ a SP, sem dar a ele permissão de _ver_ ou alterar as tabelas reais do banco.
    
4. **Tráfego de Rede:** Em vez de trafegar centenas de linhas de código pela rede, a aplicação só envia o comando de execução (ex: `EXEC SP_Calcula_Folha @Indice = 0.2`).


## Passo 1: Criação da Stored Procedure no Banco de Dados
Antes de ir para o TOTVS RM, o instrutor vai direto no gerenciador do banco de dados para criar o procedimento.

1. **Parâmetro de Entrada:** A SP é criada para receber uma variável externa chamada `@INDICE` (um valor decimal que representará a porcentagem de aumento, ex: `0.2` para 20%).
2. **Uso de Tabela "Z":** No ecossistema TOTVS, tabelas nativas começam com suas letras padrão (ex: `PFUNC`). Tabelas criadas pelo usuário/cliente costumam começar com a letra `Z` (ex: `ZPFUNC`).
3. **Lógica de Execução da SP:**
   - **Limpeza:** A primeira instrução é apagar os dados antigos da tabela `ZPFUNC` (`DELETE ZPFUNC`), garantindo que o relatório sempre traga dados novos ao ser rodado.
   - **Inserção e Cálculo:** Ele faz um `INSERT INTO` pegando a Chapa, Nome e Salário da tabela original de funcionários. 
   - O segredo está no cálculo matemático dentro do SQL para a coluna "Novo Salário": `Salario + (Salario * @Indice)`.
   - **Filtro:** Traz apenas funcionários não demitidos (`SITUACAO <> 'D'`).
1. **Compilação:** A procedure é salva com o nome `SP_FUNCIONARIOS_AJUSTE`.

---

## Passo 2: Configurando o RM Reports
Com o banco de dados pronto, o trabalho passa para dentro da interface do RM.

### 1. Fonte de Dados (A Leitura)
- No RM Reports, adiciona-se uma nova fonte de dados do tipo **Consulta SQL**.
- A consulta será muito simples: `SELECT * FROM ZPFUNC` (Ela apenas lê a tabela auxiliar que foi preenchida pela SP).
- Os campos (Chapa, Nome, Salário, Novo Salário) são arrastados para o *Detalhe* do relatório e recebem máscaras financeiras.

### 2. Vinculando a Stored Procedure (A Execução)
Para que a tabela `ZPFUNC` tenha dados atualizados antes do `SELECT` rodar, o RM Reports precisa acionar a SP.
- Nas propriedades do relatório, existe um local específico para vincular Stored Procedures.
- O instrutor seleciona a `SP_FUNCIONARIOS_AJUSTE` que havia sido criada no banco de dados.

### 3. Configuração de Parâmetros (Ligação Tela -> Banco)
Como a SP exige um parâmetro (o `@INDICE`), o RM Reports precisa de um campo para o usuário digitar esse valor na tela.
- Clica-se com o botão direito na área de *Parâmetros* no RM e seleciona-se "Adicionar Parâmetro".
- **Atenção ao Nome:** O nome do parâmetro no RM **deve ser idêntico** ao nome esperado pela SP (ex: `INDICE`).
- O tipo de dado é definido como "Decimais".

---

## Passo 3: Execução e Resultado
- Ao clicar em gerar o relatório, o sistema TOTVS exibe uma tela pedindo para o usuário preencher o parâmetro "Índice".
- O instrutor digita `0.2` (simulando 20% de aumento).
- **O fluxo que ocorre em milissegundos:** O RM passa o valor 0.2 para a SP > A SP limpa a tabela ZPFUNC > A SP calcula os salários + 20% e preenche a tabela > A Consulta SQL do RM lê a tabela > O relatório é desenhado na tela.


