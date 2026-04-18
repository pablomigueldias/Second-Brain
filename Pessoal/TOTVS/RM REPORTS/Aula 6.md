
---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - layout
  - formatacao
aliases:
  - Texto, Totalizador, Imagem, Linhas e Formas
  - Aula 06 RM Reports
---

# Aula #006 - TOTVS RM - RM Reports: Texto, Totalizador, Imagem, Linhas e Formas

**Fonte:** [AULA #006 - TOTVS RM - RM Reports - Texto, Totalizador, Imagem, Linhas e Formas.](https://youtu.be/71oJo7B48Rw)
**Instrutor:** Renato Barbero

## 📌 Visão Geral (Início do Módulo 2)
Esta aula inicia o segundo módulo do curso de RM Reports. O foco principal é enriquecer visualmente o layout do relatório e começar a utilizar dados do **módulo de Folha de Pagamento (RM Labore)**. O instrutor demonstra a inserção de logotipos, formatação de textos em massa, aplicação de máscaras de moeda, além de explorar elementos gráficos como linhas e formas geométricas.

---
## Trocando de Módulo: Banco de Dados do RM Labore
Nesta etapa, o curso deixa de olhar para a listagem de produtos e passa a listar funcionários.
- **Tabela Utilizada:** `PFUNC` (Folha de Pagamento - Funcionários).
- **Dica de Ouro (Descobrir o nome da tabela):** Se você não souber qual tabela puxar, abra o cadastro que você deseja listar diretamente no sistema TOTVS. Clique com o botão direito numa área vazia da tela e vá em **Visualizar Nome dos Campos**. O sistema mostrará o formato `Tabela.Campo` (ex: `PFUNC.CHAPA`), facilitando a busca no RM Reports.

---

## Otimização de Layout e Formatação
Após adicionar os campos (Chapa, Nome, Salário) à faixa de detalhe, o instrutor demonstra técnicas para formatar os rótulos de forma mais eficiente.

### Formatação em Lote (Herança de Propriedades)
- Em vez de clicar em cada caixa de texto (cabeçalho) para colocar em **Negrito**, você pode clicar diretamente na faixa (Band) chamada *Cabeçalho do Detalhe*.
- Ao colocar a propriedade dessa Band como Negrito, **todos** os textos que forem criados dentro dela herdarão automaticamente a formatação. Isso poupa muito tempo.

### Alinhamento e Bordas
- **Atalhos Visuais:** Para garantir que todos os campos fiquem com a mesma estética, você pode selecionar múltiplos campos segurando a tecla `CTRL`. Depois, na aba Layout, utilize recursos como *Mesma Largura* e *Alinhar Margem à Direita*.
- **Bordas (Grid):** Selecionando todos os campos, é possível ativar a visualização de bordas, o que cria um aspecto de tabela/grade no relatório.

---
## Elementos Visuais Adicionais
### 1. Imagem (Logotipo)
- Pode ser arrastada da caixa de ferramentas para o *Cabeçalho da Página*.
- **Configuração:** O arquivo deve estar salvo no computador. É recomendável mudar a propriedade de tamanho para **"Estender Imagem" (Stretch/Zoom)** para que ela se adapte perfeitamente ao quadrado desenhado sem ser cortada.

### 2. Formas (Shapes)
- O controle de formas pode ser utilizado para chamar a atenção para informações importantes (ex: Totais).
- **Opções:** Retângulos, elipses, triângulos ou setas.
- O instrutor exemplifica colocando uma seta apontando para o resultado da folha de pagamento e alterando a sua cor para destacá-la.

### 3. Linhas
- Elemento simples, mas crucial para a leitura. Servem para separar visualmente quebras ou encerramentos de listagens.
- **Opções:** Pode ser uma linha sólida, tracejada (dash), pontilhada, e sua espessura pode ser aumentada nas propriedades. Podem ser ancoradas no topo ou no fundo da faixa.

---

## Totalizador e Máscara de Moeda
O instrutor cria um filtro (`SITUACAO <> 'D'`) para trazer apenas os funcionários ativos e soma os salários.

- **Totalizador:** Adicionado ao *Rodapé do Detalhe*, configurado para apontar para a coleção do campo `SALARIO`.
- **Format String (Formato de Moeda):**
  - Para que os números brutos do banco de dados fiquem legíveis (ex: `1500.00` para `R$ 1.500,00`), deve-se aplicar uma formatação.
  - Nas propriedades do campo e do totalizador, vá em "Formato do Texto", selecione a categoria **Moeda (Currency - "C")** e garanta que tenha duas casas decimais.
