---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - banco_de_dados
  - logica_de_programacao
aliases:
  - Estrutura Básica e Quebras no RM Reports
  - Aula 03 RM Reports
---

# Aula #003 - TOTVS RM - RM Reports: Estrutura Básica de um Relatório (Quebras e Totalizadores)

**Fonte:** [AULA #003 - TOTVS RM - RM Reports - Estrutura Básica de um Relatório](https://youtu.be/t7Ap0YxkFlk)
**Instrutor:** Renato Barbero

## Visão Geral
Nesta terceira aula, o foco avança da listagem simples para a **organização lógica dos dados**. O instrutor ensina como criar *Quebras* (agrupamentos semelhantes à cláusula `GROUP BY` no SQL), implementar contadores invisíveis e configurar totalizadores que se reiniciam automaticamente a cada grupo.

---

## Criando Quebras e Ordenação (Agrupamento de Dados)
A "Quebra" serve para agrupar as informações do relatório com base em um critério específico, separando os dados em blocos organizados.

- **Configurando a Quebra:** Na faixa (band) de "Cabeçalho do Detalhe", acessando a setinha de opções ("Ordenação / Quebra"), é possível adicionar o campo pelo qual o relatório deve ser dividido.
- **Exemplo Prático:** O instrutor utiliza o campo `TIPO` (Produto ou Serviço). Ao inserir esse campo na regra de quebra e arrastá-lo para o layout, o relatório passa a imprimir primeiro todos os produtos (`P`) e, em um bloco separado, todos os serviços (`S`).
- **Ordenação dos Registros:** Dentro da mesma aba de configurações, define-se a ordem em que as linhas aparecerão. No exemplo, ele ordenou os itens internamente pelo `Código do Produto`.

---

## Contadores e Expressões Ocultas
Para contar quantos itens existem dentro de cada grupo (quantos produtos e quantos serviços), é necessária uma lógica envolvendo campos invisíveis.

1. **Campo Expressão:** Em vez de usar um campo do banco de dados, arrasta-se um controle de "Expressão" para o *Rodapé do Detalhe*.
2. **Valor Fixo:** Dentro da expressão, insere-se apenas o número `1`. Isso significa que, para cada linha lida do banco, o sistema gerará o valor 1.
3. **Invisibilidade (Visible = False):** Para não poluir o layout imprimindo o número 1 em todas as linhas, acessa-se as propriedades do campo e desmarca-se a opção "Visível". Ele continuará existindo e calculando no *background*, mas não será impresso.

---

## Totalizadores (Sumarização)
Com o contador invisível criado, o próximo passo é somá-lo ao final de cada bloco para exibir o total real.

- **Inserindo o Totalizador:** Arrasta-se a ferramenta de "Totalizador" para o *Rodapé do Detalhe*.
- **Configuração do Cálculo (Collection):** Clicando nas propriedades do totalizador, indica-se qual campo deve ser somado. Neste caso, seleciona-se o "Campo Expressão" criado no passo anterior.
- **Zerar na Quebra (Crucial):** Essa é a configuração mais importante. Deve-se marcar a opção para que o totalizador **zere na quebra** do campo `TIPO`.
  - *Por que isso é necessário?* Se o sistema contar 402 produtos, e você não zerar, ao começar a contar os 73 serviços, ele continuará a soma a partir do 402 (imprimindo 475 no final dos serviços). Ao "zerar na quebra", ele entrega o total correto de 402 produtos e, logo abaixo, o total independente de 73 serviços.

---
## Filtros Avançados (Último Nível)
Para evitar que o relatório imprima categorias/grupos pai junto com os itens finais, utiliza-se a estrutura hierárquica do RM.

- A máscara de produtos funciona em níveis (ex: `01` é Grupo Canetas; `01.01` é Caneta Azul).
- Para listar apenas os produtos reais e não as "pastas" agrupadoras, cria-se um filtro estrutural na fonte de dados: **`ÚLTIMO NÍVEL = 1`**. Isso exclui as categorias genéricas da listagem final.

---

##  Comportamento das Faixas (Revisão Prática)
Ao gerar o relatório completo (14 páginas), o instrutor demonstra visualmente a diferença do comportamento das faixas:
- **Cabeçalho/Rodapé de Página:** Imprimem em absolutamente **todas** as páginas (ex: data da impressão no topo, número da página `1/14` no rodapé).
- **Cabeçalho/Rodapé do Detalhe:** Só são impressos no momento exato em que a "Quebra" acontece. O cabeçalho aparece antes do bloco de "Produtos", e o rodapé aparece no final desse bloco para mostrar a contagem (402 itens). Depois, eles voltam a aparecer apenas quando inicia o bloco de "Serviços" (73 itens).