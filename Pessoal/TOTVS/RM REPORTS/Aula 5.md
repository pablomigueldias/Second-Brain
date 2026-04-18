---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - layout
aliases:
  - Configurações Básicas de Impressão
  - Aula 05 RM Reports
---

# Aula #005 - TOTVS RM - RM Reports: Configurações Básicas de Impressão

**Fonte:** [AULA #005 - TOTVS RM - RM Reports - Configurações básicas de impressão](https://youtu.be/E-_MYQDSp-c)
**Instrutor:** Renato Barbero

## Visão Geral
Nesta aula curta, o foco é a preparação do "Canvas" (área de desenho) **antes** de começar a arrastar os campos de banco de dados. O instrutor reforça a importância de definir o tamanho do papel e as margens logo no início para evitar o retrabalho de redimensionar todos os componentes do layout posteriormente.

---

##  Acessando as Propriedades Gerais do Relatório
Para modificar as configurações da página inteira, e não de uma faixa (band) específica, é necessário acessar a raiz do relatório.
- **Como acessar:** Basta clicar na área cinza fora do documento ou em uma área vazia para que a Grade de Propriedades mostre as opções gerais de `XtraReport` (RM Reports).

---

## Margens
A definição do espaço útil do relatório pode ser feita de duas formas:
1. **Manualmente (Visual):** Clicando e arrastando as linhas de margem diretamente na tela (o instrutor considera essa a forma mais fácil e intuitiva).
2. **Propriedades (Exato):** Digitando os valores exatos em centímetros na *Grade de Propriedades* na lateral da tela. O ajuste visual atualizará automaticamente esses números.

---

## Tamanho do Papel (Regra de Ouro)
O instrutor destaca que este é o passo que **deve ser feito antes de qualquer desenvolvimento de layout**.

- **O Problema:** Por padrão, o relatório pode vir configurado para o tamanho "Carta" (Letter). Se você construir o relatório inteiro nesse formato e depois o cliente for imprimir em folha "A4" (que é mais estreita), os campos que ficam mais à direita serão "comidos" (cortados) na impressão.
- **A Solução:** Logo ao criar o arquivo, altere a propriedade do papel para **A4** (ou o formato padrão utilizado pela empresa) e ajuste as margens. Isso garante que todo o design feito a partir daquele momento respeitará o limite físico da folha.
