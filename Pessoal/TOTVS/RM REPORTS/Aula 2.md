---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - banco_de_dados
aliases:
  - Criando Relatório Básico no RM Reports
  - Aula 02 RM Reports
---

# Aula #002 - TOTVS RM - RM Reports: Criando um relatório básico

**Fonte:** [AULA #002 - TOTVS RM - RM Reports - Criando um relatório básico, muito fácil!](https://www.youtube.com/watch?v=rj_JgQ3x2pc)
**Instrutor:** Renato Barbero

## Visão Geral
Nesta aula, a parte teórica da primeira aula é colocada em prática através da criação de um relatório básico de **Listagem de Produtos**. O foco é entender o painel de propriedades, a inserção de banco de dados (tabelas do sistema), a geração do relatório e a manipulação das faixas (Bands) de cabeçalho.

---

## Margens e Propriedades Gerais do Relatório
As margens definem o espaço de impressão e a área útil do Canvas.
- **Ajuste Visual:** Clicando e arrastando as linhas demarcadas no canvas, as margens diminuem ou aumentam visualmente.
- **Grade de Propriedades (Property Grid):** - Ao clicar na área geral do relatório, a grade mostra propriedades do tipo `XtraReport` (o relatório como um todo), permitindo digitar os valores exatos das margens.
  - O painel de propriedades é dinâmico: se você clica no *Cabeçalho*, ele exibe as propriedades apenas do cabeçalho; se clica no *Relatório*, exibe as gerais.

---

## Inserindo a Fonte de Dados e Tabelas
Para popular o relatório, é preciso conectar o *dataset*.
1. **Adicionar Tabela:** Clique com o botão direito em "Campos" ou no ícone da aba Início e selecione "Adicionar Fonte de Dados".
2. **Seleção da Tabela:** Neste exemplo prático, utilizou-se a tabela de produtos (`TPRUDUTO` ou correlata no sistema).
3. **Análise Preliminar:** Ao selecionar a tabela, o TOTVS RM mostra uma prévia útil:
   - Quantidade de registros na tabela.
   - Lista de todos os campos disponíveis.
   - Tabelas relacionadas (joins nativos).
1. **Mapeamento (Drag and Drop):** Com a tabela adicionada, os campos aparecem na lateral. Basta pesquisar o campo desejado (ex: `CODIGOPRD` e `DESCRICAO`) e arrastar para dentro da faixa de **Detalhe 1**.

---

## Propriedades Essenciais dos Campos de Texto
Ao selecionar um campo arrastado para o detalhe, a *Grade de Propriedades* oferece configurações fundamentais de layout e comportamento:

- **Pode Crescer (Can Grow):** Muito importante para campos de descrição longa. Se desmarcado, o texto será "cortado" no limite do tamanho do campo desenhado na tela. Se ativado (marcado), o campo expande dinamicamente para baixo (quebrando a linha) para imprimir o conteúdo inteiro.
- **Múltiplas Linhas:** Permite que o texto faça quebra de linha se o espaço lateral acabar.
- **Visível (Visible):** Determina se o campo aparece na impressão. É comum trazer campos "invisíveis" apenas para usá-los como parâmetro matemático ou de ordenação oculta no background.

---

## Geração, Filtros e Exportação
Existem diferentes maneiras de visualizar o resultado e exportá-lo:

### 1. Pré-visualização (Aba Exibição)
- Faz uma consulta rápida e leve, trazendo apenas os **primeiros registros**, ideal para verificar se o layout (tamanhos, alinhamentos) está correto sem onerar o servidor.

### 2. Geração Completa e Agendamento (Job)
- Ao gerar o relatório "por fora" (pela tela principal do RM Reports), a ferramenta processa todas as linhas do banco (ex: 15 páginas de produtos).
- Em ambientes robustos (3 camadas), é possível **Agendar a Geração**: O processamento rodará no servidor (Job) em dias e horários recorrentes (ex: toda segunda e quarta).

### 3. Filtros na Geração
- Ao pedir para gerar, o sistema permite incluir filtros (ex: campo `TIPO = 'S'`).
- Isso transforma as 15 páginas originais em apenas 3 páginas, imprimindo apenas Serviços em vez de todos os Produtos.
- Filtros digitados por fora podem ficar gravados na janela de geração; para trazer tudo de novo, basta excluir o filtro salvo.

### 4. Exportação
- Na tela de visualização da impressão, há suporte nativo para exportar o relatório para diversos formatos: **PDF, HTML, RTF, DOCX, XLS (Excel), CSV e Texto**.

---

## Trabalhando com Cabeçalhos (Página vs. Detalhe)
A aula demonstra a diferença crucial entre inserir rótulos (nomes das colunas) no cabeçalho da página ou do detalhe:

- **Cabeçalho do Detalhe:**
  - Precisa ser adicionado manualmente clicando com o botão direito `> Inserir Band > Cabeçalho do Detalhe`.
  - Funciona como um índice ou agrupador do lote de dados. Se o relatório quebrar em 15 páginas, o título da coluna (ex: "CÓDIGO" e "DESCRIÇÃO") aparecerá **apenas na primeira página**, antes de iniciar a listagem dos dados.
- **Cabeçalho da Página:**
  - É a faixa (Band) padrão que fica no topo.
  - Se os rótulos de texto (nomes das colunas) forem colocados nesta área, eles se repetirão no topo de **todas as páginas impressas**, o que é o padrão mais comum para tabelas e listagens longas.

### Dica Prática de Alinhamento
Para alinhar os "Rótulos de Cabeçalho" com os "Campos de Banco de Dados" do detalhe perfeitamente, o instrutor utiliza a barra de ferramentas superior: seleciona os dois itens e usa recursos como *Mesma Largura*, *Mesma Altura* e *Alinhar Margem à Esquerda*, garantindo um relatório simétrico e profissional.