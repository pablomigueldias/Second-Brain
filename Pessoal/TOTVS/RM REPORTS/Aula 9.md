---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - variaveis
  - boas_praticas
aliases:
  - Variáveis no RM Reports
  - Aula 09 RM Reports
---

# Aula #009 - TOTVS RM - RM Reports: Variável

**Fonte:** [AULA #009 - TOTVS RM - RM Reports - Variável](https://youtu.be/ccpZxX0oa7M)
**Instrutor:** Renato Barbero

## Visão Geral
Nesta aula, é apresentado o componente **Variável**. Diferente das expressões (que fazem cálculos matemáticos) e das tabelas de banco de dados, as Variáveis capturam **metadados do sistema ou do próprio relatório** no momento em que ele é gerado, inserindo-os dinamicamente no layout.

---

## Tipos de Variáveis Disponíveis
Ao arrastar o controle "Variável" da *Caixa de Ferramentas* para o canvas e acessar suas propriedades na aba "Dados", você tem acesso aos seguintes metadados:

1. **Código do Relatório**
2. **Descrição do Relatório**
3. **Versão**
4. **Nome da Coligada**
5. **Código do Usuário**
6. **Identificador do Relatório**

*(Nota: Cada componente "Variável" arrastado para a tela permite selecionar apenas uma dessas informações por vez)*.

---

## Casos de Uso e Exemplos Práticos

### 1. Auditoria e Rastreio no Cabeçalho
- **Código do Usuário:** O instrutor insere essa variável no *Cabeçalho da Página*.
- **Motivo:** Quando um departamento imprime o relatório e o envia para outro setor, o documento já sai com o registro de qual usuário estava logado ("Mestre", por exemplo) e gerou a listagem, o que é excelente para controle interno e auditoria.

### 2. Título Dinâmico
- **Descrição do Relatório:** Em vez de digitar um rótulo de texto estático ("Listagem de Funcionários"), usa-se a variável da descrição. 
- Dessa forma, se o nome do relatório for alterado nos parâmetros do sistema, o título do documento impresso é atualizado automaticamente.

---

## Dica de Ouro (Boas Práticas de Suporte e Manutenção)
A dica mais importante da aula é voltada para a **manutenção de sistemas e chamados de suporte**.

- **A Estratégia:** Adicione sempre o **Código do Relatório** (ex: `gap.curso.02`) de forma discreta no *Rodapé da Página*.
- **O Problema:** Empresas que utilizam o TOTVS RM costumam ter centenas ou milhares de relatórios customizados com nomes muito parecidos.
- **A Solução:** Quando um usuário final abrir um chamado relatando um bug ou erro de cálculo em um relatório impresso, você não precisará investigar ou tentar adivinhar qual arquivo ele usou. Basta pedir que ele olhe no rodapé da folha ou envie um print e informar o código exato. Com o código em mãos, você o joga no filtro do RM Reports e edita o arquivo correto em segundos.