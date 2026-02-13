Muitos devs focam apenas em aprender a sintaxe do SQL ou os métodos do ORM, mas esquecem que a performance de uma aplicação começa muito antes de escrever a primeira linha de código: ela começa no **Design do Schema**.

Hoje vamos mergulhar na teoria das **Dependências**, o conceito fundamental por trás da Normalização. Entender isso é a diferença entre um banco escalável e um sistema lento e redundante.

### O que é Dependência Funcional?

No contexto de banco de dados, "dependência" não é sobre pacotes `pip` ou `npm`. É sobre a relação lógica entre atributos (colunas) de uma tabela.

Seja $E$ uma entidade. Dizemos que $Y$ é funcionalmente dependente de $X$ se, para cada valor de $X$, existe **exatamente um** valor de $Y$ associado.

> **Matematicamente:** $X \to Y$ (Lê-se: "X determina funcionalmente Y").

* **Determinante:** O atributo lado esquerdo ($X$).
* **Dependente:** O atributo lado direito ($Y$).

#### Exemplo Prático

Imagine uma tabela de Pedidos. O `Prazo_Entrega` não é aleatório; ele é determinado pelo `Numero_Pedido`.

| Numero_Pedido (PK) | Data_Pedido | Prazo_Entrega |
| :--- | :--- | :--- |
| 1001 | 2023-10-01 | 2023-10-15 |

Aqui, `Numero_Pedido` **determina** `Prazo_Entrega`.
Em uma tabela bem normalizada, a **Primary Key (PK)** deve determinar funcionalmente *todos* os outros atributos não-chave.

---

### Dependência Funcional Total vs. Parcial

Isso aqui é a chave para entender a **2ª Forma Normal (2NF)**. Esses conceitos só aparecem quando temos uma **Chave Primária Composta** (uma PK formada por duas ou mais colunas).

#### 1. Dependência Funcional Total
Ocorre quando um atributo não-chave depende da **PK inteira** (todos os campos que compõem a chave). É o cenário ideal.

**Cenário:** Tabela `Itens_Pedido`.
* **PK Composta:** `Num_Pedido` + `Cod_Produto`.
* **Atributo:** `Quantidade`.

A quantidade comprada depende *exclusivamente* da combinação daquele pedido específico com aquele produto específico. Ela tem **Dependência Total** da chave.

#### 2. Dependência Funcional Parcial (O Perigo)
Ocorre quando um atributo depende apenas de **uma parte** da chave composta. Isso gera redundância.

**Cenário Ruim:** Tabela `Notas_Alunos`.
* **PK Composta:** `ID_Aluno` + `Cod_Disciplina`.
* **Atributo:** `Nome_Disciplina`.

O `Nome_Disciplina` depende apenas do `Cod_Disciplina`. Ele não se importa com quem é o aluno.
Isso viola a integridade e desperdiça espaço. Se a disciplina mudar de nome, você teria que atualizar todas as linhas de alunos matriculados nela.

> 💡 **Dica Pro:** Se você identificou uma Dependência Parcial, é um sinal claro de que essa informação deve ser extraída para uma nova tabela (ex: criar uma tabela só para `Disciplinas`).

---

### Dependência Funcional Transitiva

Essa é a vilã que a **3ª Forma Normal (3NF)** combate.
Ela ocorre quando um campo não depende diretamente da PK, mas sim de outro campo que também não é chave.

**Estrutura:** $A \to B \to C$
(A PK determina B, e B determina C).

#### Exemplo Real

Tabela: `Entregas`

| Num_Pedido (PK) | Cod_Vendedor | Nome_Vendedor |
| :--- | :--- | :--- |
| 500 | V01 | Carlos |

Analise a cadeia:
1.  `Num_Pedido` determina quem é o `Cod_Vendedor`.
2.  `Cod_Vendedor` determina o `Nome_Vendedor`.

O `Nome_Vendedor` está ali de "penetra". Ele depende transitivamente da PK através do código do vendedor.
**Solução:** Mova os dados do vendedor para uma tabela `Vendedores` e mantenha apenas a FK `Cod_Vendedor` na tabela de entregas.

---

### Dependência Multivalorada

Aqui entramos no território da **4ª Forma Normal (4NF)**.
Ocorre quando um atributo $A$ determina um **conjunto** de valores para $B$ e um **conjunto** de valores para $C$, mas $B$ e $C$ são independentes entre si.

Símbolo: $A \twoheadrightarrow B$

#### O Caso do Carro
Imagine uma tabela que tenta armazenar todas as variações de um carro.

* Modelo: Honda Civic
* Ano: 2020, 2021, 2022
* Cor: Preto, Prata, Branco

As cores disponíveis independem dos anos de fabricação (neste exemplo teórico). Se tentarmos colocar tudo na mesma tabela, teremos que fazer o produto cartesiano de Anos x Cores para cada Modelo, gerando linhas repetidas absurdamente.

> **Insight:** Dependências multivaloradas sugerem que você está tentando misturar dois assuntos independentes na mesma entidade. Separe-os.

---

### Conclusão

Entender dependências não é preciosismo acadêmico. É sobre criar bancos de dados onde:
1.  **A escrita é rápida** (menos linhas para atualizar).
2.  **A consistência é garantida** (dados não se contradizem).
3.  **O armazenamento é otimizado**.

No próximo post, vamos aplicar esses conceitos para normalizar uma tabela "Frankenstein" até a 3NF usando Python e Pandas para validar os dados.

Ficou com dúvida? Manda no [LinkedIn/Twitter]!