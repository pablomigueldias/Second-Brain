---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - banco_de_dados
aliases:
  - Introdução ao RM Reports
  - Aula 01 RM Reports
---

# Aula #001 - TOTVS RM - RM Reports

**Fonte:** [AULA #001 - TOTVS RM - RM Reports - Desvendando o RM Reports- Apresentação](https://www.youtube.com/watch?v=5awNMmu5Cac)
**Instrutor:** Renato Barbero

## Visão Geral e Acesso Inicial
O RM Reports é a ferramenta nativa do ecossistema TOTVS para a criação e extração de relatórios, indo desde listagens simples até fluxos financeiros complexos.

- **Caminho de Acesso:** O recurso pode ser encontrado em qualquer módulo do sistema acessando o menu **Gestão > RM Reports** 
- **Filtros de Busca:** É possível criar filtros personalizados (usando sintaxe semelhante a SQL, como `LIKE`) para buscar relatórios específicos no sistema de forma rápida.

---
## Parâmetros de Criação de um Novo Relatório
Ao criar um novo relatório, o sistema exige o preenchimento de diversos metadados essenciais para sua organização e segurança.
### 1. Identificação
- **Código:** Deve ser sugestivo e seguir um padrão de nomenclatura da empresa (ex: para boletos, usar `Boleto_p001` ou `Bol_p01`)
- **Descrição / Observações:** Campos dedicados para detalhar o propósito do relatório, facilitando manutenções futuras.

### 2. Comportamento e Execução
- **Visível a todas coligadas:** Se marcado, o relatório fica disponível em todo o grupo empresarial (todas as filiais/coligadas).
- **Filtro obrigatório ao executar:** Obriga o usuário final a preencher parâmetros antes da geração. Se ignorado, a geração do relatório apresentará erro.
- **Usar diretório padrão:** Permite definir um caminho específico (pasta no computador/servidor) para onde as exportações serão salvas automaticamente.

### 3. Segurança e Permissões
- **Grupo:** Define qual departamento ou grupo de usuários pode enxergar o relatório (ex: criar um grupo "Financeiro" e atrelar aos perfis correspondentes).
- **Nível de Acesso:** Dentro do grupo escolhido, define as permissões individuais (quem tem apenas leitura, quem pode gerar ou quem pode modificar o layout)

### 4. Classificação e Módulos
- **Tipo:** Varia de acordo com a aplicação. Pode ser tipificado como *Nota Fiscal, Fatura, Pedido, Recibo*, etc. Relatórios de listagem de dados normais que não se encaixam nessas categorias devem usar o tipo **Genérico**.
- **Módulo de Origem:** Define de onde a informação será extraída.
  - *Nota Histórica da TOTVS:* O instrutor cita as nomenclaturas antigas da linha RM que ainda aparecem no sistema:
    - **Fluxus:** Gestão Financeira.
    - **Nucleus:** Gestão de Estoque, Compras e Faturamento.
- **Disponível no Menu:** Cria um atalho prático. O relatório aparece em uma "setinha" de acesso rápido na interface principal, dispensando a necessidade de buscá-lo via filtros.

### 5. Fontes de Dados Padrão e Auditoria
- **Fonte de Dados (Aba Metadados):** O RM possui algumas fontes pré-definidas para acelerar o desenvolvimento de cotações ou orçamentos, embora a maioria dos relatórios gerenciais exija criação do zero.
- **Modificado por/em:** Log automático de auditoria gerado sempre que alguém altera e executa o relatório.

---

##  Estrutura do Editor (Layout)
Ao clicar duas vezes no relatório recém-criado, a interface de desenvolvimento ("Canvas") é aberta.

### Estrutura Visual Básica
O documento é dividido em "Bands" (faixas) clássicas de relatórios:
1. **Cabeçalho de Página 1**
2. **Detalhe 1** (Onde os dados de fato iteram/repetem)
3. **Rodapé da Página 1**

### Abas de Ferramentas
O sistema habilita três abas principais no menu superior:

- **1. Início (Home):**
  - Controles padrões do Office (Copiar, Colar, Desfazer).
  - **Grupos e Quebras:** Configurações estruturais do relatório.
  - **Filtros Internos:** Filtros hardcoded no relatório (ex: trazer apenas clientes Pessoa Física).
  - **Adicionar Fonte de Dados (O Principal):** É aqui que você informa se os dados virão de uma **Tabela do Sistema** ou de uma **Consulta SQL** customizada.
- **2. Layout:**
  - Ferramentas de estilização visual (Fonte, Negrito, Alinhamento de campos, Margens superiores e inferiores).
- **3. Exibição:**
  - Controles de Zoom da tela e a ferramenta de **Pré-visualizar**, permitindo testar o layout renderizado rapidamente.

### Integração dos Dados no Canvas
- No painel lateral existe a **Caixa de Ferramentas** (controles de texto, imagens, etc.) e a **Lista de Campos**.
- Após adicionar a Fonte de Dados (seja via tabela ou consulta SQL), as colunas aparecem na Lista de Campos. O desenvolvimento baseia-se em clicar nesses campos e **arrastá-los** para dentro das faixas (bands) do relatório.