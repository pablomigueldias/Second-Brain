
[[Sistemas de Arquivos - Sistema de Banco de Dados.canvas|Sistemas de Arquivos - Sistema de Banco de Dados]]

## NATUREZA AUTODESCRITIVA

-  Uma definição e descrição completa de sua estrutura e restrições.
- Armazenada no catálogo do SGBD
	-  Estrutura de cada arquivo, o tipo e formato dos itens de dados e as restrições sobre os dados
	-  METADADOS

## RELAÇOES

| Nome_relacao      | Numero_de_colunas |
| ----------------- | :---------------: |
| ALUNO             |         4         |
| DISCIPLINA        |         4         |
| TURMA             |         5         |
| HISTORICO ESCOLAR |         3         |
| PRE_REQUISITO     |         2         |
## COLUNAS

| Nome_coluna          | Tipo_de_dado  | Pertence_a_relacao |
| -------------------- | ------------- | ------------------ |
| Nome                 | Caractere(30) | ALUNO              |
| Numero_aluno         | Caractere(4)  | ALUNO              |
| Tipo_aluno           | Inteiro(1)    | ALUNO              |
| Curso                | Tipo_curso    | ALUNO              |
| Nome_disciplina      | Caractere(10) | DISCIPLINA         |
| Numero_disciplina    | ZZZZNNN       | DISCIPLINA         |
| ...                  | ...           | ...                |
| ...                  | ...           | ...                |
| ...                  | ...           | ...                |
| Numero_pre_requisito | ZZZZNNN       | PRE_REQUISITO      |

## ISOLAMENTO ENTRE PROGRAMAS E DADOS

-  independência de dados do programa
- Exemplo:
	-  Acrescentar data de nascimento a ralação aluno.
- SGBDOO
	-  Operação -> Interface ou assinatura + implementação ou método
	-  A implementação pode ser alterada sem mudança na interface
	-  Independência de operação do programa

## ABSTRAÇÃO DE DADOS

- Característica que permite a independência de dados do programa e a independência da operação dos programas.
- SGBD
	- Representação conceitual
		- Usa um `Modelo de dados`
	- Conceito Lógicos

## SUPORTE A MÚLPLAS VISÕES DOS DADOS

- Visão:
	-  Um subconjunto do banco de dados ou
	-  pode conter dados que são derivados dos arquivos do banco de dados(dados virtual).
- Um SGBD multiusuário precisa oferecer facilidades para definir múltiplas visões.

## COMPARTILHAMENTO DE DADOS

- Processamento de transação multiusuário
	- On-line Transaction Processing (OLTP)
- Controle de concorrência (SGBD)
	-  Garantir que vários usuários tentando atualizar o mesmo dado façam isso de maneira controlada.
	-  Transações concorrente
		- Operam de forma correta e eficiente
		- Que tal +5 centavos a respeito de transação

## CONCEITO DE TRANSAÇÃO

- É um programa em execução ou processo que inclui um ou mais acessos ao banco de dados, que efetuam leitura ou atualização de seus registros.

1.  Atomicidade
2.  Consistência
3.  Isolamento
4.  Durablilidade



