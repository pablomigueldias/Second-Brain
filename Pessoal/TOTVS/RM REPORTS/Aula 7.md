---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - logica_de_programacao
aliases:
  - Expressões e Cálculos no RM Reports
  - Aula 07 RM Reports
---

# Aula #007 - TOTVS RM - RM Reports: Expressões

**Fonte:** [AULA #007 - TOTVS RM - RM Reports - Expressão](https://youtu.be/X89UtsVTGsk)
**Instrutor:** Renato Barbero

## Visão Geral
Dando continuidade ao Módulo 2 e utilizando o relatório de folha de pagamento (RM Labore) criado na aula anterior, o instrutor demonstra o uso avançado da ferramenta **Expressão**. As expressões permitem a criação de campos calculados dinamicamente no relatório, sem a necessidade de alterar a consulta SQL original ou a estrutura do banco de dados.

---

## Criando Campos Calculados com Expressões
O cenário prático da aula simula uma necessidade do setor de RH: projetar como ficaria a folha de pagamento caso houvesse um reajuste salarial de 15% para todos os funcionários.

1. **Estruturando o Layout:** O instrutor cria espaço no relatório, copiando o cabeçalho "Salário" e renomeando o novo campo para **"Novo Salário"**.
2. **Adicionando a Expressão:** Em seguida, arrasta a ferramenta "Expressão" da Caixa de Ferramentas para o *Detalhe*, alinhando-a com a nova coluna.
3. **Construindo a Fórmula Matemática:**
   - Nas propriedades do campo Expressão, acessa-se o menu de parâmetros.
   - O RM Reports permite usar os campos já embutidos no relatório ou ir direto na base de dados.
   - A fórmula utilizada foi baseada no salário atual multiplicado pelo fator de reajuste: `[Salario] * 1.15`.
   - **⚠️ Atenção à Sintaxe (Ponto vs. Vírgula):** O instrutor inicialmente digita `1,15` e o relatório retorna um erro ao compilar. No RM Reports (herdando regras comuns ao SQL/C#), o separador decimal obrigatório em expressões matemáticas é o **ponto (.)**, devendo ser corrigido para `1.15`.

---

##  Formatação e Totalização da Expressão
Após calcular a linha individual, é necessário manter o rigor visual e financeiro do relatório.

- **Máscara de Moeda:** A expressão criada recebe o Formato de Texto **Moeda (C2)** nas propriedades, garantindo as duas casas decimais e o separador de milhar visuais.
- **Totalizador de Expressão:** - Um novo "Totalizador" é inserido no *Rodapé do Detalhe* para somar a projeção.
  - Na propriedade de *Collection* (Campos Totalizados), em vez de apontar para um campo do banco, o instrutor aponta para o campo dinâmico que acabou de ser criado: `Expressão`.
- **Resultado:** O relatório apresenta o Salário Atual do funcionário, o Novo Salário (+15%), o Total da Folha Antiga (ex: R$ 140.000) e o Total da Folha Projetada (ex: R$ 161.000).

---

## Navegação pelas Funções de Expressões Avançadas
Além de cálculos matemáticos básicos, a ferramenta "Expressões" possui uma biblioteca vasta de funções embutidas:

- **Funções Matemáticas:** `Round` (arredondar), `Power` (potência), `Exp` (exponencial), entre outras.
- **Funções de Texto (String):**
  - `Upper`: Transforma a string em MAIÚSCULAS.
  - `Len`: Conta a quantidade de caracteres de um texto.
  - `Substring`: Extrai um pedaço específico de um texto.
  - `Remove` e `Replace`: Apagam ou substituem caracteres dentro da string.
- **Funções de Data e Hora:**
  - O sistema possui funções para retornar o dia exato da consulta, extrair apenas o ano (`Year`), mês, dia, hora ou minuto de uma data informada pelo banco.
  - **Prática:** O instrutor adiciona o comando `Today()` em um campo vermelho no layout, que ao renderizar o relatório, devolve dinamicamente a data atual em que a impressão foi gerada (ex: `01/09/2022`).