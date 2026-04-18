---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - logica_de_programacao
  - formulas
aliases:
  - Fórmulas no RM Reports
  - Aula 08 RM Reports
---

# Aula #008 - TOTVS RM - RM Reports: Fórmula

**Fonte:** [AULA #008 - TOTVS RM - RM Reports - Fórmula](https://youtu.be/-6V_HJJYBC0)
**Instrutor:** Renato Barbero

##  Visão Geral
Nesta aula, o instrutor apresenta a ferramenta **Fórmula**. Diferente das "Expressões" (vistas na aula anterior), que são cálculos matemáticos e manipulações de strings feitas diretamente no relatório, as Fórmulas são **procedimentos nativos do sistema TOTVS** criados para resolver regras de negócio complexas sem a necessidade de escrever consultas SQL avançadas.

---

## O Conceito de Fórmulas no TOTVS RM
As fórmulas servem como atalhos lógicos. Cada módulo do TOTVS possui funções pré-definidas para abstrair cálculos complexos.

- **Exemplo Financeiro:** Calcular o valor líquido de um lançamento financeiro. Via SQL, seria necessário cruzar diversas tabelas para abater impostos, retenções e taxas. Com o uso de uma fórmula nativa, o sistema já entrega esse valor mastigado.
- **Exemplo no Labore (Folha de Pagamento):** O instrutor utiliza uma fórmula para buscar o **Salário Mínimo do Sindicato** de cada colaborador. Fazer isso via banco de dados exigiria um `JOIN` entre a tabela do funcionário, a tabela de sindicatos e suas respectivas vigências. A fórmula resolve isso com um único comando.

---

##  Implementação Prática (Passo a Passo)

1. **Inserindo o Componente:**
   - Na Caixa de Ferramentas, seleciona-se o componente "Fórmula" e arrasta-se para dentro da faixa de *Detalhe* do relatório.
1. **Criando a Fórmula no Editor:**
   - Ao acessar as propriedades do campo, o instrutor opta por criar uma nova fórmula apontada para o módulo de "RH / Folha de Pagamento".
   - Na biblioteca de funções do RM, existe uma documentação interna que explica o que cada fórmula faz. Ele localiza e seleciona a função relacionada ao "Salário mínimo do sindicato".
1. **Validação Automática (Testar Fórmula):**
   - O editor de fórmulas possui uma funcionalidade muito útil: o botão **"Testar fórmula automaticamente"**. Quando marcado, o sistema compila o código na hora, pega o primeiro registro do banco (o primeiro funcionário da folha) e exibe o resultado simulado (no exemplo da aula, retornou o valor de R$ 380,00), validando se a lógica está correta antes de gerar todo o relatório.

---

## Formatação e Integração Visual
Após validar a fórmula, é necessário tratá-la visualmente para manter a consistência do documento.

- O instrutor cria um novo rótulo no *Cabeçalho do Detalhe* chamado "Salário Mínimo do Sindicato".
- **Máscara Financeira:** Assim como na aula anterior, o campo numérico retornado pela fórmula recebe a máscara de formato de texto **"C2" (Moeda)**. Isso garante a exibição com R$, ponto como separador de milhar e duas casas decimais.
- **Bordas:** O controle de bordas é aplicado para seguir o estilo de "grade" das outras colunas.
- **Visualização:** Ao rodar a pré-visualização, o sistema mostra o salário base do sindicato de cada funcionário corretamente alinhado ao seu registro. *(Nota: Na base de testes do instrutor, todos retornaram 380,00 porque estavam atrelados ao mesmo sindicato).*