---
tags:
  - totvs
  - rm_reports
  - erp
  - relatorios
  - paginacao
  - front_end
aliases:
  - Informações da Página no RM Reports
  - Aula 10 RM Reports
---

#  Aula #010 - TOTVS RM - RM Reports: Informações da Página

**Fonte:** [AULA #010 - TOTVS RM - Informações da Página](https://youtu.be/oyeZ-rvNCns)
**Instrutor:** Renato Barbero

## Visão Geral
Esta é uma aula rápida e direta ao ponto, focada no componente **Informações da Página** (Page Info). Este controle é utilizado principalmente em cabeçalhos e rodapés para fornecer contexto de paginação, data de extração e autoria do documento impresso.

---

## O Componente "Informações da Página"
Ao arrastar a ferramenta "Informações da Página" da *Caixa de Ferramentas* para o layout, você ganha acesso a macros de formatação prontas, dispensando a necessidade de criar expressões complexas de concatenação.

As opções disponíveis incluem:
- **Número Total de Páginas:** Exibe a contagem de páginas.
- **Romano / Romano em Minúsculas:** Permite que a paginação seja impressa em numeração romana (ex: I, II, III).
- **Data e Hora Atual:** Carimba o momento exato da geração do relatório.
- **Nome do Usuário:** Traz o *nome* completo de quem gerou o documento.
- **Contagem de Páginas (Padrão "1 de X"):** Macro pronta para exibir o formato clássico de paginação.

---

## Exemplos Práticos no Relatório
O instrutor demonstra a aplicação configurando o rodapé do relatório:
1. **Identificação Visual:** Insere a opção "Nome do Usuário" para registrar na folha impressa quem foi o colaborador (ex: "Mestre") que executou a extração.
2. **Paginação Customizada:** Insere o "Contador da Página" e, em seguida, altera suas propriedades para numeração Romana. Ao gerar o relatório completo, as páginas passam a ser exibidas como "Página I de I", "Página II", etc.

---

## Análise Estratégica: Variável (Aula 09) vs. Informações da Página (Aula 10)
A partir do que foi apresentado nas duas últimas aulas, é importante fazer uma distinção técnica clara sobre qual componente escolher para arquitetar seus relatórios:

- **Componente Variável (Aula 09):** É focado em **Metadados de Sistema e Suporte**. Ele traz o *Código do Usuário* (o login do banco/sistema) e o *Código do Relatório* (ex: `gap.curso.02`). **Uso ideal:** Rastreiabilidade técnica, debugging e auditoria de TI.
- **Componente Informações da Página (Aula 10):** É focado na **Camada de Apresentação (Front-end do Relatório)**. Ele traz o *Nome do Usuário* formatado e paginações amigáveis (como numeração romana). **Uso ideal:** Entregáveis formais, documentos para a diretoria, contratos e espelhos de ponto onde a leitura deve ser fluida e amigável para o cliente final.