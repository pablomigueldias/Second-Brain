
- **Tabelas Globais**: `GUSUARIO`(Usuários), `GCAMPOS`(Dicionário de campos), `GLINKSREL`(Relacionamento entre tabelas)
- **Pessoas e RH(P e V)**: `PPESSOAS`(Cadastro único de pessoas físicas - CPF, Nome,Data de Nasc), `PFUNC`(Funcionários - Chapa, Salário, Cargo).
- **Educacional(S - Classis)**: `SALUNO`(Alunos), `SMATRICULA`(Matrículas).
- **Backoffice / Financeiro(F e T)**: (Lançamentos Financeiros), `TMOV`(Movimentos de estoque/compras/vendas).

Regra: A tabela `PPESSOA` é o centro do universo. Um funcionário, um aluno e um professor são antes de tudo, uma `PPESSOA`. A ligação entre `PFUNC`(Funcionário) e `PPESSOA` se dá pelo campo `CODPESSOA`.

