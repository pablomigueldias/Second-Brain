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

# 📊 Aula #011 - TOTVS RM - RM Reports: Stored Procedure

**Fonte:** [AULA #011 - TOTVS RM - RM Reports - Stored Procedure](https://www.youtube.com/watch?v=yTTzyiu2u2Q)
**Instrutor:** Renato Barbero

## 📌 Visão Geral
Nesta aula avançada, o instrutor demonstra como integrar o RM Reports com o banco de dados (SQL Server) executando uma **Stored Procedure**. O cenário prático é a simulação de um reajuste salarial: a SP recebe a porcentagem de aumento, faz os cálculos, salva em uma tabela customizada (auxiliar), e o RM Reports consome e exibe esse resultado.

---

## 💻 Passo 1: Criação da Stored Procedure no Banco de Dados
Antes de ir para o TOTVS RM, o instrutor vai direto no gerenciador do banco de dados para criar o procedimento [00:00:35].

1. **Parâmetro de Entrada:** A SP é criada para receber uma variável externa chamada `@INDICE` (um valor decimal que representará a porcentagem de aumento, ex: `0.2` para 20%) [00:00:48].
2. **Uso de Tabela "Z":** No ecossistema TOTVS, tabelas nativas começam com suas letras padrão (ex: `PFUNC`). Tabelas criadas pelo usuário/cliente costumam começar com a letra `Z` (ex: `ZPFUNC`).
3. **Lógica de Execução da SP:**
   - **Limpeza:** A primeira instrução é apagar os dados antigos da tabela `ZPFUNC` (`DELETE ZPFUNC`), garantindo que o relatório sempre traga dados novos ao ser rodado [00:01:20].
   - **Inserção e Cálculo:** Ele faz um `INSERT INTO` pegando a Chapa, Nome e Salário da tabela original de funcionários. 
   - O segredo está no cálculo matemático dentro do SQL para a coluna "Novo Salário": `Salario + (Salario * @Indice)` [00:02:47].
   - **Filtro:** Traz apenas funcionários não demitidos (`SITUACAO <> 'D'`).
4. **Compilação:** A procedure é salva com o nome `SP_FUNCIONARIOS_AJUSTE` [00:03:40].

---

## ⚙️ Passo 2: Configurando o RM Reports
Com o banco de dados pronto, o trabalho passa para dentro da interface do RM.

### 1. Fonte de Dados (A Leitura)
- No RM Reports, adiciona-se uma nova fonte de dados do tipo **Consulta SQL** [00:05:09].
- A consulta será muito simples: `SELECT * FROM ZPFUNC` (Ela apenas lê a tabela auxiliar que foi preenchida pela SP) [00:05:41].
- Os campos (Chapa, Nome, Salário, Novo Salário) são arrastados para o *Detalhe* do relatório e recebem máscaras financeiras.

### 2. Vinculando a Stored Procedure (A Execução)
Para que a tabela `ZPFUNC` tenha dados atualizados antes do `SELECT` rodar, o RM Reports precisa acionar a SP [00:08:31].
- Nas propriedades do relatório, existe um local específico para vincular Stored Procedures.
- O instrutor seleciona a `SP_FUNCIONARIOS_AJUSTE` que havia sido criada no banco de dados [00:08:48].

### 3. Configuração de Parâmetros (Ligação Tela -> Banco)
Como a SP exige um parâmetro (o `@INDICE`), o RM Reports precisa de um campo para o usuário digitar esse valor na tela.
- Clica-se com o botão direito na área de *Parâmetros* no RM e seleciona-se "Adicionar Parâmetro" [00:09:15].
- **Atenção ao Nome:** O nome do parâmetro no RM **deve ser idêntico** ao nome esperado pela SP (ex: `INDICE`).
- O tipo de dado é definido como "Decimais" [00:09:51].

---

## 🚀 Passo 3: Execução e Resultado
- Ao clicar em gerar o relatório, o sistema TOTVS exibe uma tela pedindo para o usuário preencher o parâmetro "Índice" [00:10:09].
- O instrutor digita `0.2` (simulando 20% de aumento).
- **O fluxo que ocorre em milissegundos:** O RM passa o valor 0.2 para a SP > A SP limpa a tabela ZPFUNC > A SP calcula os salários + 20% e preenche a tabela > A Consulta SQL do RM lê a tabela > O relatório é desenhado na tela [00:10:24].


