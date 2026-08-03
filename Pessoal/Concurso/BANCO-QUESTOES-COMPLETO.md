# Banco de questões COMPLETO — Coren-SP / Quadrix
## Analista de Ciência de Dados e Inteligência Artificial

> Arquivo único e definitivo. **Substitui** `banco-questoes-coren-sp.md`, `banco-questoes-por-semana.md` e `banco-questoes-blocos-D-a-J.md`, que tinham letras de bloco conflitantes. Aqui os blocos vão de 01 a 11, na ordem exata do cronograma v2.

**Dois tipos de conteúdo:**

- 🟦 **SIMULADO** — itens escritos no padrão da banca, para tópicos **sem nenhum precedente** em prova Quadrix. Vêm com gabarito comentado pelo mecanismo do erro.
- 🟩 **REAL** — mapeamento de itens verdadeiros da banca, nas provas que você já tem em PDF. Gabarito oficial da própria prova.

Item real sempre vence simulação. Onde existe conjunto real, é ele que você resolve.

**Códigos das provas:** `CFBio` (Quadrix 2025) · `CFO` (Quadrix 2025) · `CRM` (Quadrix 2024) · `PRODAM` (Quadrix 2022, múltipla escolha) · `COREN-BD` e `COREN-SI` (VUNESP 2013, múltipla escolha).

---

## Índice

| Semana | Bloco / conjunto | Tipo | Itens |
|---|---|---|---|
| 1 | **Bloco 01** — Estatística descritiva e probabilidade | 🟦 | 20 |
| 2 | **Bloco 02** — Estatística inferencial | 🟦 | 20 |
| 2 | **Bloco 03** — Python, pandas e SQL analítico | 🟦 | 20 |
| 3 | Banco de dados | 🟩 | 20 |
| 4 | **Bloco 04** — DW e modelagem dimensional | 🟦 | 20 |
| 4 | **Bloco 05** — ETL, Pentaho, Apache Hop e pipelines | 🟦 | 20 |
| 5 | **Bloco 06** — Nuvem e Big Data | 🟦 | 20 |
| 5 | Arquitetura, SO e Linux | 🟩 | 20 |
| 5 | Redes e protocolos | 🟩 | 20 |
| 6 | Segurança da informação | 🟩 | 20 |
| 6 | Governança de TI | 🟩 | 18 |
| 7 | **Bloco 07** — Machine Learning | 🟦 | 20 |
| 7 | **Bloco 08** — Deep Learning, NLP, visão e MLOps | 🟦 | 20 |
| 7 | **Bloco 09** — Power BI | 🟦 | 20 |
| 7 | **Bloco 10** — Governança de dados e LGPD | 🟦 | 20 |
| 8 | Lógica proposicional | 🟩 | 16 |
| 9 | Contagem, probabilidade e aritmética | 🟩 | 20 |
| 10 | Português: leitura e semântica | 🟩 | 20 |
| 11 | Português: gramática e reescrita | 🟩 | 20 |
| 12 | Legislação administrativa | 🟩 | 20 |
| 13 | **Bloco 11** — Legislação Cofen/Coren | 🟦 | 20 |

**220 itens simulados + 194 itens reais mapeados.**

Apêndices ao final: mapa completo de itens reais por tópico, método de conversão de múltipla escolha em Certo/Errado, e lista de pares confundíveis.

---

## Como usar

1. **Resolva sem olhar o gabarito**, marcando C, E ou branco conforme a regra de convicção do cronograma — ≥70% se a penalidade for −1,0; ≥55% se for −0,5.
2. Ao conferir, para cada erro anote **o mecanismo**, não a resposta certa. É o mecanismo que se repete na prova.
3. Todo item errado vira **card de Anki no formato de par confundível**.
4. Refaça o bloco 7 dias depois. Se acertar 18 ou mais, arquive; abaixo disso, o tópico volta para a revisão da semana.

**Os seis mecanismos do item errado:** termo absoluto · definição trocada entre conceitos irmãos · inversão de causa e efeito · atributo de uma ferramenta colado em outra · número ou prazo trocado · "é vedado" × "é permitido".

---

# SEMANA 1 — Estatística descritiva e probabilidade

## 🟦 BLOCO 01 — Estatística descritiva e probabilidade

Julgue os itens a seguir.

1. A média aritmética é mais sensível à presença de valores extremos do que a mediana. C
2. Em uma distribuição com assimetria à direita (positiva), a média é menor que a mediana. C
3. O desvio padrão é expresso na mesma unidade de medida dos dados originais, ao contrário da variância. C
4. O coeficiente de variação, por ser adimensional, permite comparar a dispersão de conjuntos de dados expressos em unidades diferentes. C
5. No boxplot, a linha interna à caixa representa sempre a média dos dados. E
6. Dois eventos mutuamente exclusivos são, necessariamente, eventos independentes. E
7. O teorema de Bayes permite atualizar a probabilidade atribuída a uma hipótese à luz de nova evidência observada. E
8. Na distribuição binomial, o número de tentativas é fixo e a probabilidade de sucesso permanece constante entre elas. C
9. A distribuição de Poisson é adequada para modelar a contagem de ocorrências em um intervalo fixo, apresentando média igual à variância.
10. Pelo Teorema Central do Limite, a distribuição da média amostral aproxima-se da normal apenas se a população de origem for normalmente distribuída.
11. Um intervalo de confiança de 95% indica que há 95% de probabilidade de o parâmetro populacional estar contido naquele intervalo específico já calculado.
12. O erro do tipo I ocorre quando se rejeita a hipótese nula, sendo ela verdadeira.
13. Reduzir o nível de significância de 5% para 1%, mantidas as demais condições, aumenta a probabilidade de erro do tipo II.
14. Um p-valor de 0,03, adotado o nível de significância de 5%, conduz à não rejeição da hipótese nula.
15. O coeficiente de correlação de Pearson mede a associação linear entre duas variáveis e varia entre −1 e 1.
16. Coeficiente de correlação igual a zero implica ausência de qualquer relação entre as variáveis analisadas.
17. Na regressão linear múltipla, o R² ajustado penaliza a inclusão de variáveis explicativas que não contribuem para o poder explicativo do modelo.
18. A presença de multicolinearidade entre variáveis explicativas infla os erros-padrão dos coeficientes estimados.
19. A moda é a única medida de tendência central aplicável a variáveis qualitativas nominais.
20. A amostragem estratificada consiste em selecionar elementos em intervalos regulares, a partir de um ponto de partida escolhido aleatoriamente.

### Gabarito

| # | Gab. | Comentário / mecanismo |
|---|---|---|
| 1 | C | Definicional. |
| 2 | **E** | Inversão: na assimetria à direita, média > mediana. |
| 3 | C | A variância está na unidade ao quadrado. |
| 4 | C | Definicional. |
| 5 | **E** | Definição trocada (é a mediana) + termo absoluto "sempre". |
| 6 | **E** | Definição trocada. Mutuamente exclusivos e independentes são conceitos distintos e, em geral, incompatíveis. |
| 7 | C | Definicional. |
| 8 | C | Duas das condições do modelo binomial. |
| 9 | C | Em Poisson, média = variância = λ. |
| 10 | **E** | Termo restritivo "apenas" + inversão: o TCL vale independentemente da distribuição da população, dado n suficiente. |
| 11 | **E** | Interpretação incorreta do IC na abordagem frequentista. A probabilidade refere-se ao procedimento, não ao intervalo já calculado. |
| 12 | C | Definicional. |
| 13 | C | Trade-off entre erro I e erro II. |
| 14 | **E** | p-valor (0,03) < α (0,05) → rejeita-se H₀. |
| 15 | C | Definicional. |
| 16 | **E** | Termo absoluto "qualquer". Pearson mede relação *linear*; pode haver relação não linear. |
| 17 | C | Definicional. |
| 18 | C | Definicional. |
| 19 | C | Média e mediana exigem, no mínimo, escala ordinal. |
| 20 | **E** | Definição trocada: o descrito é amostragem sistemática. |

---

---

# SEMANA 2 — Estatística inferencial · Python e SQL

## 🟦 BLOCO 02 — Estatística inferencial

1. O teorema central do limite assegura que, para amostras suficientemente grandes, a distribuição da média amostral aproxima-se da normal, independentemente da distribuição da população de origem.
2. O erro-padrão da média diminui à medida que o tamanho da amostra aumenta.
3. Mantido o mesmo nível de confiança, o aumento do tamanho da amostra amplia a largura do intervalo de confiança.
4. Para elevar o nível de confiança de 95% para 99%, mantido o tamanho da amostra, o intervalo de confiança torna-se mais largo.
5. A distribuição t de Student é empregada quando o desvio padrão populacional é desconhecido e estimado a partir da amostra.
6. A distribuição t apresenta caudas mais pesadas que a normal padrão, aproximando-se dela conforme aumentam os graus de liberdade.
7. O teste qui-quadrado de independência é aplicável a variáveis quantitativas contínuas.
8. A hipótese nula é aquela que o pesquisador pretende comprovar por meio do teste.
9. O p-valor expressa a probabilidade de a hipótese nula ser verdadeira.
10. Em teste bilateral com nível de significância de 5%, a região crítica distribui-se em 2,5% em cada cauda.
11. O poder de um teste corresponde à probabilidade de rejeitar a hipótese nula quando ela é efetivamente falsa.
12. O erro do tipo II consiste em não rejeitar hipótese nula falsa.
13. Reduzir o nível de significância de 5% para 1% aumenta o poder do teste.
14. Na regressão linear simples, o coeficiente angular indica a variação esperada na variável dependente para cada unidade de variação na independente.
15. Um R² igual a 0,80 indica que 80% das observações foram corretamente previstas pelo modelo.
16. Os resíduos de uma regressão linear devem apresentar, idealmente, média zero, variância constante e independência.
17. A heterocedasticidade caracteriza-se pela variância não constante dos resíduos ao longo dos valores ajustados.
18. A existência de correlação entre duas variáveis é suficiente para estabelecer relação de causalidade entre elas.
19. Na amostragem por conglomerados, a população é dividida em grupos e alguns grupos são selecionados integralmente.
20. Em amostragem aleatória simples com reposição, um mesmo elemento pode ser selecionado mais de uma vez.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Enunciado correto do TCL. |
| 2 | C | Erro-padrão = σ/√n. |
| 3 | **E** | Inversão: amostra maior → intervalo mais estreito. |
| 4 | C | Mais confiança exige mais amplitude. |
| 5 | C | Definicional. |
| 6 | C | Definicional. |
| 7 | **E** | Definição trocada: aplica-se a variáveis categóricas. |
| 8 | **E** | Inversão: H₀ é a hipótese que se busca rejeitar; a alternativa é a do pesquisador. |
| 9 | **E** | Definição trocada. É a probabilidade de observar resultado tão ou mais extremo, **dado** que H₀ é verdadeira. |
| 10 | C | Definicional. |
| 11 | C | Poder = 1 − β. |
| 12 | C | Definicional. |
| 13 | **E** | Inversão: reduzir α aumenta β e portanto **reduz** o poder. |
| 14 | C | Definicional. |
| 15 | **E** | Definição trocada: R² é proporção da **variância** explicada, não de observações acertadas. |
| 16 | C | Pressupostos clássicos. |
| 17 | C | Definicional. |
| 18 | **E** | Absoluto "suficiente" + falácia clássica. |
| 19 | C | Definicional. |
| 20 | C | Definicional. |

---

## 🟦 BLOCO 03 — Python, pandas e SQL analítico

Julgue os itens a seguir.

1. Em pandas, o método `groupby()` seguido de função de agregação retorna objeto cujo índice é formado pelas chaves de agrupamento.
2. O método `merge()` do pandas realiza junção entre DataFrames, admitindo os tipos inner, outer, left e right.
3. Em pandas, Series é a estrutura bidimensional composta por linhas e colunas rotuladas.
4. Em pandas, `loc` realiza seleção baseada em rótulo, enquanto `iloc` realiza seleção baseada em posição inteira.
5. Por padrão, o método `dropna()` remove todas as colunas que contenham ao menos um valor ausente.
6. O método `pivot_table()` admite função de agregação definida pelo usuário, diferentemente de `pivot()`.
7. O método `apply()` permite aplicar função ao longo de um eixo do DataFrame.
8. A biblioteca NumPy fornece o objeto ndarray, cujas operações vetorizadas são mais eficientes que laços nativos do Python.
9. A biblioteca scikit-learn é voltada exclusivamente à construção de redes neurais profundas.
10. Em pandas, a concatenação de DataFrames ao longo do eixo das linhas é realizada por `concat()`.
11. Em SQL, a cláusula WHERE filtra registros antes da agregação, enquanto HAVING atua sobre o resultado agregado.
12. Em SQL, o comando `TRUNCATE TABLE` remove todos os registros da tabela, preservando sua estrutura.
13. Em SQL, o comando `DROP TABLE` remove somente os dados da tabela, mantendo sua definição no catálogo.
14. Funções de janela (window functions) permitem cálculo agregado sem colapsar as linhas do conjunto de resultados.
15. As funções `ROW_NUMBER()`, `RANK()` e `DENSE_RANK()` produzem resultados idênticos na presença de empates.
16. Uma Common Table Expression (CTE), definida pela cláusula WITH, pode ser recursiva.
17. O INNER JOIN retorna apenas as linhas que possuem correspondência em ambas as tabelas envolvidas.
18. O LEFT JOIN retorna todas as linhas da tabela à direita e apenas as correspondentes da tabela à esquerda.
19. GRANT e REVOKE pertencem à categoria DCL da linguagem SQL.
20. Em SQL, `COUNT(*)` e `COUNT(coluna)` retornam sempre o mesmo valor para uma dada tabela.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Definicional. |
| 2 | C | Definicional. |
| 3 | **E** | Definição trocada: Series é unidimensional; a bidimensional é o DataFrame. |
| 4 | C | Definicional. |
| 5 | **E** | Absoluto + eixo trocado: o padrão é `axis=0`, removendo **linhas**. |
| 6 | C | `pivot()` apenas reorganiza; não agrega. |
| 7 | C | Definicional. |
| 8 | C | Definicional. |
| 9 | **E** | Absoluto "exclusivamente" + troca: scikit-learn é de ML clássico; DL é TensorFlow/PyTorch. |
| 10 | C | Definicional. |
| 11 | C | Distinção clássica, cobrada com frequência. |
| 12 | C | Definicional. |
| 13 | **E** | Definição trocada: DROP remove dados **e** estrutura. |
| 14 | C | É a característica que as distingue de GROUP BY. |
| 15 | **E** | Definição trocada: `RANK()` salta posições após empate; `DENSE_RANK()` não; `ROW_NUMBER()` ignora empates. |
| 16 | C | Definicional. |
| 17 | C | Definicional. |
| 18 | **E** | Inversão: LEFT JOIN preserva todas as linhas da tabela à **esquerda**. |
| 19 | C | DCL = controle de acesso. |
| 20 | **E** | Absoluto "sempre": `COUNT(coluna)` desconsidera valores nulos. |

---

---

# SEMANA 3 — Banco de dados

## 🟩 Set de 20 itens REAIS — banco de dados

| # | Prova | Item | Assunto |
|---|---|---|---|
| 1–10 | CFO | 81–90 | conceito de BD e SGBD, modelo ER, restrições de integridade, chave primária, desnormalização, ACID, índices, relacional × NoSQL |
| 11 | CFBio | 86 | entidade associativa |
| 12 | CFBio | 87 | ALTER TABLE / restrição UNIQUE |
| 13 | CFBio | 88 | integridade referencial |
| 14 | PRODAM | 31 | operações em fila |
| 15 | PRODAM | 36 | relacionamento N:N e entidade associativa |
| 16 | PRODAM | 51 | forma normal e dependência de junção |
| 17 | PRODAM | 52 | administração de dados × administração de BD |
| 18 | PRODAM | 53 | remoção de tabela em SQL |
| 19 | COREN-BD | 35 | maior forma normal a partir de dependências funcionais |
| 20 | COREN-BD | 42 | deadlock no controle de concorrência |

**Reserva (faça se sobrar tempo):** COREN-BD 31–34, 36–41 · PRODAM 55.
**Ignore:** COREN-BD 43–45, 58–60 (versões de SGBD datadas).

> Os itens 16 e 19 são de normalização com dependência funcional. Faça no papel. É o formato que mais derruba dev.

---

---

# SEMANA 4 — DW, modelagem dimensional, ETL e pipelines

## 🟦 BLOCO 04 — DW e modelagem dimensional

Julgue os itens a seguir.

1. Sistemas OLTP são otimizados para transações curtas e frequentes, enquanto sistemas OLAP são voltados a consultas analíticas sobre grandes volumes.
2. No esquema estrela (star schema), as tabelas de dimensão são normalizadas em múltiplos níveis hierárquicos.
3. A tabela fato armazena as métricas do processo de negócio e as chaves estrangeiras que a ligam às dimensões.
4. A granularidade da tabela fato corresponde ao nível de detalhe do evento registrado em cada uma de suas linhas.
5. A Slowly Changing Dimension do tipo 1 sobrescreve o valor anterior do atributo, não preservando histórico.
6. A Slowly Changing Dimension do tipo 2 sobrescreve o atributo alterado, mantendo apenas o valor corrente.
7. A Slowly Changing Dimension do tipo 3 preserva histórico limitado por meio de colunas adicionais destinadas a valores anteriores.
8. Na abordagem de Kimball, o data warehouse é construído de forma incremental, a partir de data marts integrados por dimensões conformadas.
9. Na abordagem de Inmon, os data marts são construídos primeiro e o data warehouse corporativo é derivado deles.
10. Dimensão degenerada é o atributo de natureza dimensional armazenado na própria tabela fato, como o número do pedido.
11. Um data lake armazena dados em formato bruto, com aplicação de esquema no momento da leitura.
12. O data lakehouse combina o armazenamento de baixo custo do data lake com recursos transacionais e de governança característicos do data warehouse.
13. O Data Mesh propõe a centralização total da propriedade dos dados em uma única equipe de plataforma.
14. Tabela fato destinada a registrar a ocorrência de um evento, sem métricas numéricas associadas, é denominada factless fact table.
15. Um data warehouse caracteriza-se por ser orientado a assunto, integrado, não volátil e variante no tempo.
16. Por ser não volátil, o data warehouse não admite atualização por meio de cargas incrementais.
17. Dimensão conformada é aquela compartilhada de forma consistente entre múltiplas tabelas fato.
18. O cubo OLAP admite as operações de drill-down, roll-up, slice e dice.
19. O MOLAP armazena os dados em estruturas multidimensionais próprias, enquanto o ROLAP consulta diretamente o banco de dados relacional.
20. A surrogate key de uma dimensão deve, obrigatoriamente, coincidir com a chave natural do sistema de origem.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Definicional. |
| 2 | **E** | Definição trocada: normalização das dimensões caracteriza o **snowflake**. |
| 3 | C | Definicional. |
| 4 | C | Definicional. |
| 5 | C | Definicional. |
| 6 | **E** | Definição trocada com o tipo 1: o tipo 2 cria nova linha versionada, preservando histórico. |
| 7 | C | Definicional. |
| 8 | C | Bottom-up. |
| 9 | **E** | Inversão: Inmon é top-down — DW corporativo primeiro, data marts derivados. |
| 10 | C | Definicional. |
| 11 | C | *Schema on read*. |
| 12 | C | Definicional. |
| 13 | **E** | Inversão: o Data Mesh propõe descentralização por domínio, com dados tratados como produto. |
| 14 | C | Definicional. |
| 15 | C | As quatro características de Inmon. |
| 16 | **E** | Confusão de conceito: não volatilidade se refere a não sofrer alteração/exclusão transacional, e não impede carga incremental. |
| 17 | C | Definicional. |
| 18 | C | Definicional. |
| 19 | C | Definicional. |
| 20 | **E** | Inversão + absoluto: a surrogate key é justamente artificial, independente da chave natural. |

---

---

## 🟦 BLOCO 05 — ETL, Pentaho, Apache Hop e pipelines

Julgue os itens a seguir.

1. No ETL, a transformação ocorre antes da carga no destino; no ELT, após a carga.
2. O ELT é adequado quando o repositório de destino dispõe de capacidade de processamento suficiente para executar as transformações.
3. No Pentaho Data Integration, a transformation manipula o fluxo de dados, enquanto o job orquestra a execução de tarefas.
4. No Pentaho Data Integration, os steps são conectados por hops, que definem o fluxo entre eles.
5. No Pentaho Data Integration, o job é o artefato utilizado para transformar registro a registro dentro do fluxo de dados.
6. O Apache Hop originou-se como um fork do Pentaho Data Integration.
7. No Apache Hop, os artefatos equivalentes a transformation e job denominam-se, respectivamente, pipeline e workflow.
8. O Apache Airflow organiza tarefas em grafos acíclicos dirigidos (DAG), com dependências declaradas explicitamente.
9. Em orquestração de dados, idempotência significa que a reexecução da mesma carga produz o mesmo estado final, sem duplicação de registros.
10. Processamento em batch e em streaming diferem quanto à latência e ao modo de delimitação do conjunto de dados processado.
11. A arquitetura Lambda mantém, em paralelo, uma camada batch e uma camada de velocidade; a arquitetura Kappa unifica o tratamento em fluxo único.
12. Na arquitetura Kappa, é obrigatória a manutenção de uma camada batch separada da camada de streaming.
13. Parquet e ORC são formatos colunares, adequados a consultas analíticas que acessam subconjunto de colunas.
14. O Avro é formato colunar otimizado para leitura analítica de poucas colunas.
15. O particionamento de tabelas por data reduz o volume de dados varridos em consultas filtradas por período.
16. Delta Lake e Apache Iceberg acrescentam controle transacional e versionamento sobre arquivos armazenados em data lake.
17. A carga incremental processa apenas os registros novos ou alterados desde a última execução do pipeline.
18. O Change Data Capture (CDC) identifica alterações ocorridas na origem para propagá-las ao destino.
19. Em um pipeline de dados, a staging area constitui a camada final, destinada ao consumo pelos usuários de negócio.
20. A verificação de qualidade dos dados em um pipeline deve ser realizada exclusivamente ao final da carga, após a disponibilização ao usuário.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Definicional. |
| 2 | C | É a premissa que viabiliza o ELT. |
| 3 | C | Definicional. |
| 4 | C | Vocabulário do PDI: steps + hops. |
| 5 | **E** | Definição trocada: quem manipula o fluxo registro a registro é a **transformation**. |
| 6 | C | Fato histórico do projeto. |
| 7 | C | Vocabulário do Hop. |
| 8 | C | Definicional. |
| 9 | C | Definicional. |
| 10 | C | Definicional. |
| 11 | C | Definicional. |
| 12 | **E** | Inversão + absoluto: a Kappa dispensa a camada batch — é exatamente sua proposta. |
| 13 | C | Definicional. |
| 14 | **E** | Definição trocada: o Avro é orientado a linha, voltado a serialização e escrita. |
| 15 | C | *Partition pruning*. |
| 16 | C | Definicional. |
| 17 | C | Definicional. |
| 18 | C | Definicional. |
| 19 | **E** | Definição trocada: a staging é área intermediária de preparação, não camada de consumo. |
| 20 | **E** | Absoluto + inversão: a verificação deve ocorrer ao longo do pipeline, antes da disponibilização. |

---

---

# SEMANA 5 — Nuvem, Big Data e núcleo genérico de TI

## 🟦 BLOCO 06 — Nuvem e Big Data

Julgue os itens a seguir.

1. No modelo IaaS, o provedor gerencia a infraestrutura física e o cliente responde pelo sistema operacional e pelas aplicações.
2. No modelo SaaS, o cliente é responsável pela manutenção do sistema operacional e do middleware.
3. A elasticidade permite o ajuste automático dos recursos computacionais conforme a variação da demanda.
4. A computação em nuvem é, por definição, menos segura que qualquer ambiente local, independentemente dos controles adotados.
5. Hypervisores como VMware ESXi, Microsoft Hyper-V e KVM permitem a criação e o gerenciamento de máquinas virtuais.
6. O modelo de responsabilidade compartilhada estabelece que a segurança em ambiente de nuvem é dividida entre provedor e cliente.
7. Amazon S3, Azure Blob Storage e Google Cloud Storage são serviços de armazenamento de objetos.
8. Amazon Redshift, Azure Synapse Analytics e Google BigQuery são serviços de data warehouse.
9. Amazon SageMaker, Azure Machine Learning e Google Vertex AI são serviços de armazenamento de objetos.
10. No HDFS, os arquivos são divididos em blocos replicados entre os nós do cluster.
11. No ecossistema Hadoop, o YARN é responsável pelo gerenciamento de recursos e pelo escalonamento de aplicações.
12. O MapReduce grava resultados intermediários em disco, o que o torna menos eficiente que o Spark em processamento iterativo.
13. O Spark utiliza o MapReduce como seu motor de execução padrão.
14. O RDD é a abstração de coleção distribuída e imutável do Spark.
15. O Spark adota avaliação preguiçosa (lazy evaluation): as transformações só são executadas quando acionadas por uma ação.
16. O Apache Kafka é plataforma de streaming organizada em tópicos, partições e grupos de consumidores.
17. No Kafka, a mensagem é removida do tópico imediatamente após ser consumida pelo primeiro consumidor.
18. O processamento distribuído pressupõe a divisão da carga de trabalho entre múltiplos nós que operam em paralelo.
19. A escalabilidade horizontal consiste em ampliar a capacidade de um único nó, mediante acréscimo de CPU e memória.
20. Arquiteturas de data warehouse em nuvem com separação entre armazenamento e computação permitem escalar cada camada de forma independente.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Definicional. |
| 2 | **E** | Inversão: no SaaS o provedor gerencia toda a pilha. |
| 3 | C | Definicional. |
| 4 | **E** | Absoluto "qualquer" + "independentemente de". Compare com o item real CRM-RR 118, idêntico em mecanismo. |
| 5 | C | Item real equivalente: CRM-RR 116. |
| 6 | C | Definicional. |
| 7 | C | Tabela de equivalência entre nuvens. |
| 8 | C | Tabela de equivalência entre nuvens. |
| 9 | **E** | Categoria trocada: são serviços de machine learning. |
| 10 | C | Definicional. |
| 11 | C | Definicional. |
| 12 | C | Motivo central da adoção do Spark. |
| 13 | **E** | Atributo colado em ferramenta errada: o Spark tem motor próprio baseado em DAG. |
| 14 | C | Definicional. |
| 15 | C | Definicional. |
| 16 | C | Definicional. |
| 17 | **E** | A retenção no Kafka é por tempo ou tamanho; a mensagem permanece disponível a outros grupos de consumidores. |
| 18 | C | Definicional. |
| 19 | **E** | Definição trocada: o descrito é escalabilidade **vertical**. |
| 20 | C | Definicional. |

---

---

## 🟩 Set de 20 itens REAIS — arquitetura, SO e Linux

| # | Prova | Item |
|---|---|---|
| 1–11 | CRM | 71–81 (cache, memória virtual, barramento, SO monolítico × modular, journaling, gerenciamento de processos) |
| 12–16 | CFBio | 71–75 (cache L1/L2, barramento de E/S, escalonador de curto prazo, swap, comando `find` com `-exec`) |
| 17–19 | PRODAM | 26, 27, 28 (compactação de memória, overlapped seeks, journaling) |
| 20 | COREN-BD | 46 (RAID nível 0) |

**Reserva:** COREN-BD 47, 53–57 · COREN-SI 48–52 *(pule os itens de Windows Server 2008)*.


## 🟩 Set de 20 itens REAIS — redes e protocolos

| # | Prova | Item |
|---|---|---|
| 1–10 | CRM | 82–91 (IPv4/IPv6, TCP/IP, switch, DNS, VPN, FTP ativo × passivo, FTPS/SFTP, portas 20 e 21) |
| 11–13 | CFBio | 76, 77, 78 (sub-rede /26, 802.1Q e VLAN trunk, `scp -r`) |
| 14–20 | COREN-SI | 38, 39, 40, 41, 42, 43, 46 (camadas OSI, subcamada MAC, SNMP, classes de IP, TTL, DHCP com reserva, IEEE 802.15) |

**Ignore:** COREN-SI 58 (e-PING 2013).

---

---

# SEMANA 6 — Segurança da informação e Governança de TI

## 🟩 Set de 20 itens REAIS — segurança da informação

| # | Prova | Item |
|---|---|---|
| 1–5 | CFO | 71–75 (CID, antivírus como suficiente, políticas de segurança, phishing) |
| 6–7 | CFBio | 81, 82 (phishing, keylogger descrito como DDoS) |
| 8–15 | CRM | 92–99 (backup, senhas fracas, phishing e engenharia social, IoT e superfície de ataque, criptografia, sistemas novos e vulnerabilidades) |
| 16–17 | PRODAM | 32, 35 (RBAC, sniffer) |
| 18 | COREN-SI | 34 (rootkit) |
| 19 | COREN-SI | 55 (honeypot) |
| 20 | COREN-SI | 59 (injeção de SQL por concatenação) |

**Reserva:** COREN-SI 31–33, 36, 37 (ISO 27001/27002), 53, 54, 57, 60.


## 🟩 Set de 18 itens REAIS — governança de TI

| # | Prova | Item |
|---|---|---|
| 1–10 | CRM | 100–109 (COBIT, alinhamento estratégico, transparência, as 5 fases do ciclo de vida ITIL, os 5 grupos do PMBOK) |
| 11–15 | CFO | 76–80 (ITIL e PMBOK como garantia automática, responsabilidade da governança, tratamento de riscos, alinhamento, compliance com LGPD e GDPR) |
| 16–18 | CFBio | 83, 84, 85 (objetivo do ITIL, grupos de processos do PMBOK, termo de abertura) |

> São 18, não 20 — é tudo que existe nas provas que você tem. É também o bloco com maior certeza de cair: apareceu nas três provas de conselho, em três cargos diferentes.

---

---

# SEMANA 7 — ML, DL, NLP, Power BI e governança de dados

## 🟦 BLOCO 07 — Machine Learning

Julgue os itens a seguir.

1. O aprendizado supervisionado requer um conjunto de dados previamente rotulado.
2. O algoritmo k-means é um método supervisionado de classificação.
3. A análise de componentes principais (PCA) reduz a dimensionalidade projetando os dados em componentes que maximizam a variância explicada.
4. O random forest é um método ensemble que combina árvores de decisão por meio de bagging, reduzindo a variância do modelo.
5. No gradient boosting, as árvores são treinadas sequencialmente, cada uma corrigindo os erros residuais das anteriores.
6. O sobreajuste (overfitting) caracteriza-se por erro elevado tanto no conjunto de treino quanto no de validação.
7. Aumentar a complexidade do modelo reduz simultaneamente o viés e a variância.
8. A regularização L1 (Lasso) pode reduzir coeficientes a exatamente zero, atuando como mecanismo de seleção de atributos.
9. A regularização L2 (Ridge) elimina completamente do modelo as variáveis irrelevantes.
10. A precisão corresponde à proporção de verdadeiros positivos entre todas as predições classificadas como positivas.
11. O recall mede a proporção de predições positivas que se mostraram corretas.
12. O F1-score é a média harmônica entre precisão e recall.
13. Em base fortemente desbalanceada, a acurácia pode apresentar valor elevado ainda que o modelo seja incapaz de identificar a classe minoritária.
14. Área sob a curva ROC (AUC) igual a 0,5 indica desempenho equivalente ao de uma classificação aleatória.
15. Na validação cruzada k-fold, todo o conjunto de dados é utilizado tanto para treino quanto para validação, em rodadas alternadas.
16. O conjunto de teste deve ser empregado para o ajuste dos hiperparâmetros do modelo.
17. A regressão logística, apesar da denominação, é empregada em problemas de classificação.
18. O RMSE penaliza erros de maior magnitude mais fortemente que o MAE, por elevar os resíduos ao quadrado.
19. No CRISP-DM, a etapa de entendimento do negócio antecede a de entendimento dos dados.
20. O aprendizado por reforço dispensa qualquer sinal de retorno do ambiente, aprendendo exclusivamente por observação passiva.

### Gabarito

| # | Gab. | Comentário / mecanismo |
|---|---|---|
| 1 | C | Definicional. |
| 2 | **E** | Definição trocada: k-means é não supervisionado, de agrupamento. |
| 3 | C | Definicional. |
| 4 | C | Definicional. |
| 5 | C | Diferença central entre boosting e bagging. |
| 6 | **E** | Definição trocada: overfitting = erro baixo no treino e alto na validação. O descrito é underfitting. |
| 7 | **E** | Inversão do trade-off viés-variância: reduz viés e *aumenta* variância. |
| 8 | C | Propriedade do L1. |
| 9 | **E** | Atributo do L1 colado no L2 + absoluto "completamente". L2 encolhe, não zera. |
| 10 | C | Definicional. |
| 11 | **E** | Definição trocada: o descrito é precisão. Recall = VP / (VP + FN). |
| 12 | C | Definicional. |
| 13 | C | Justamente por isso a acurácia é insuficiente em bases desbalanceadas. |
| 14 | C | Definicional. |
| 15 | C | Definicional. |
| 16 | **E** | Confusão entre validação e teste. Hiperparâmetro se ajusta na validação; o teste é usado uma vez, ao final. |
| 17 | C | Definicional. |
| 18 | C | Definicional. |
| 19 | C | Ordem do CRISP-DM: negócio → dados → preparação → modelagem → avaliação → implantação. |
| 20 | **E** | Absoluto "qualquer"/"exclusivamente" + inversão: o reforço depende justamente do sinal de recompensa. |

---

---

## 🟦 BLOCO 08 — Deep Learning, NLP, visão e MLOps

Julgue os itens a seguir.

1. O perceptron de camada única não é capaz de resolver o problema do XOR.
2. O algoritmo de retropropagação (backpropagation) calcula os gradientes da função de perda em relação aos pesos, propagando o erro da saída para as camadas anteriores.
3. A função de ativação ReLU retorna zero para entradas negativas e o próprio valor para entradas positivas.
4. Funções de ativação são dispensáveis em redes profundas, pois a composição de camadas lineares já produz fronteiras de decisão não lineares.
5. A função softmax é empregada na camada de saída de problemas de classificação multiclasse, produzindo distribuição de probabilidade.
6. Uma época corresponde a uma passagem completa do algoritmo por todo o conjunto de treinamento.
7. O tamanho do lote (batch size) e a taxa de aprendizado são parâmetros aprendidos automaticamente durante o treinamento.
8. O dropout desativa aleatoriamente neurônios durante o treinamento, atuando como técnica de regularização.
9. O problema do desaparecimento do gradiente afeta redes profundas e motivou a adoção de arquiteturas como a LSTM no tratamento de sequências longas.
10. Redes neurais convolucionais aplicam filtros que exploram a localidade espacial, sendo adequadas ao processamento de imagens.
11. As camadas de pooling têm por função aumentar a dimensionalidade dos mapas de características.
12. Os Transformers dispensam a recorrência, utilizando mecanismo de autoatenção para modelar dependências entre elementos da sequência.
13. Embeddings representam palavras como vetores densos em um espaço no qual a proximidade reflete similaridade semântica.
14. Stemming e lematização são procedimentos equivalentes, pois ambos retornam a forma canônica registrada no dicionário.
15. O TF-IDF atribui peso maior a termos frequentes em um documento e raros na coleção.
16. A abordagem RAG combina a recuperação de documentos em base externa com a geração de texto por modelo de linguagem.
17. A segmentação semântica atribui uma classe a cada pixel da imagem, diferentemente da detecção de objetos, que delimita regiões.
18. Data drift consiste na alteração da relação entre as variáveis de entrada e a variável-alvo ao longo do tempo.
19. A feature store centraliza atributos versionados, promovendo consistência entre as etapas de treinamento e de inferência.
20. Após o deploy, o modelo em produção dispensa monitoramento contínuo, desde que tenha apresentado boas métricas na validação.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Limitação clássica; motivou as camadas ocultas. |
| 2 | C | Definicional. |
| 3 | C | Definicional. |
| 4 | **E** | Inversão: sem ativação não linear, a rede colapsa em transformação linear única. |
| 5 | C | Definicional. |
| 6 | C | Definicional. |
| 7 | **E** | Troca parâmetro × hiperparâmetro: ambos são definidos pelo projetista. |
| 8 | C | Definicional. |
| 9 | C | Definicional. |
| 10 | C | Definicional. |
| 11 | **E** | Inversão: o pooling **reduz** a dimensionalidade. |
| 12 | C | Definicional. |
| 13 | C | Definicional. |
| 14 | **E** | Definições trocadas + absoluto: stemming corta radicais e pode gerar forma inexistente; só a lematização retorna o lema. |
| 15 | C | Definicional. |
| 16 | C | Definicional. |
| 17 | C | Definicional. |
| 18 | **E** | Definição trocada: o descrito é **concept drift**. Data drift é mudança na distribuição das entradas. |
| 19 | C | Definicional. |
| 20 | **E** | Absoluto: monitoramento contínuo é necessário justamente por causa do drift. |

---

---

## 🟦 BLOCO 09 — Power BI

Julgue os itens a seguir.

1. O Power Query utiliza a linguagem M nas etapas de extração e transformação de dados.
2. A linguagem DAX é utilizada na criação de medidas e de colunas calculadas do modelo.
3. O DAX é a linguagem empregada nas etapas de extração e transformação executadas pelo Power Query.
4. No modo Import, os dados são carregados e compactados no modelo, o que favorece o desempenho das consultas.
5. No modo DirectQuery, as consultas são enviadas à fonte no momento da interação do usuário, sem que os dados sejam armazenados no modelo.
6. O modo DirectQuery permite a utilização de todas as funções DAX, sem qualquer restrição.
7. A medida é calculada no momento da consulta, conforme o contexto de filtro, enquanto a coluna calculada é materializada no modelo durante a atualização.
8. A coluna calculada é avaliada dinamicamente conforme o contexto de filtro aplicado no visual.
9. O contexto de linha é o contexto de avaliação linha a linha, característico de colunas calculadas e de funções iteradoras.
10. A função CALCULATE permite modificar o contexto de filtro no qual uma expressão é avaliada.
11. A função ALL remove os filtros aplicados a uma tabela ou coluna no contexto de avaliação.
12. SUMX é função iteradora que percorre uma tabela avaliando a expressão linha a linha.
13. A função RELATED recupera valor de tabela relacionada situada no lado "um" do relacionamento.
14. Os relacionamentos no Power BI admitem cardinalidade um-para-um, um-para-muitos e muitos-para-muitos.
15. Um modelo do Power BI pode conter mais de um relacionamento ativo simultaneamente entre as mesmas duas tabelas.
16. O esquema estrela é a modelagem recomendada para modelos do Power BI, por favorecer desempenho e simplicidade.
17. O gateway de dados local é necessário para a atualização agendada de conjuntos de dados conectados a fontes locais.
18. A segurança em nível de linha (RLS) restringe o acesso a linhas do modelo conforme o usuário autenticado.
19. A publicação de um relatório no Power BI Service dispensa qualquer configuração adicional para que a atualização dos dados passe a ocorrer automaticamente.
20. Workspace é o ambiente de colaboração do Power BI Service, no qual relatórios, dashboards e conjuntos de dados são organizados.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Definicional. |
| 2 | C | Definicional. |
| 3 | **E** | Linguagens trocadas: a etapa de ETL do Power Query usa **M**. |
| 4 | C | Definicional. |
| 5 | C | Definicional. |
| 6 | **E** | Absoluto "todas / sem qualquer restrição": o DirectQuery impõe limitações a funções DAX. |
| 7 | C | Distinção central; cobrada com frequência. |
| 8 | **E** | Definição trocada com medida: a coluna calculada é materializada na atualização. |
| 9 | C | Definicional. |
| 10 | C | Definicional. |
| 11 | C | Definicional. |
| 12 | C | Definicional. |
| 13 | C | Definicional. |
| 14 | C | Definicional. |
| 15 | **E** | Só um relacionamento pode estar ativo entre o mesmo par de tabelas; os demais ficam inativos. |
| 16 | C | Recomendação oficial de modelagem. |
| 17 | C | Definicional. |
| 18 | C | Definicional. |
| 19 | **E** | Absoluto: é preciso configurar credenciais, gateway e agendamento. |
| 20 | C | Definicional. |

---

---

## 🟦 BLOCO 10 — Governança de dados e LGPD

Julgue os itens a seguir.

1. Conforme a LGPD, o dado anonimizado não é considerado dado pessoal, salvo quando o processo de anonimização for revertido.
2. De acordo com a LGPD, o princípio da finalidade estabelece que o tratamento deve limitar-se ao mínimo necessário para a realização de suas finalidades.
3. Controlador é a pessoa natural ou jurídica, de direito público ou privado, a quem competem as decisões referentes ao tratamento de dados pessoais.
4. O consentimento do titular é a única base legal admitida pela LGPD para o tratamento de dados pessoais.
5. Dados referentes à saúde e dados biométricos são classificados pela LGPD como dados pessoais sensíveis.
6. O encarregado pelo tratamento de dados pessoais atua como canal de comunicação entre o controlador, os titulares e a autoridade nacional.
7. O titular tem direito à portabilidade de seus dados a outro fornecedor de serviço ou produto, mediante requisição expressa.
8. A LGPD não se aplica ao tratamento de dados realizado por pessoa natural para fins exclusivamente particulares e não econômicos.
9. Anonimização e pseudonimização são termos sinônimos, uma vez que ambas as técnicas impedem definitivamente a reidentificação do titular.
10. A autoridade nacional poderá determinar ao controlador que elabore relatório de impacto à proteção de dados pessoais.
11. O tratamento de dados pessoais para a tutela da saúde, em procedimento realizado por profissionais de saúde ou por entidades sanitárias, constitui hipótese legal prevista na LGPD.
12. Segundo o DAMA-DMBOK, a governança de dados ocupa posição central em relação às demais áreas de conhecimento da gestão de dados.
13. O data steward é o responsável final pela infraestrutura física de armazenamento dos dados.
14. A linhagem de dados descreve a origem do dado e as transformações por ele sofridas ao longo do pipeline.
15. O catálogo de dados é um repositório de metadados que facilita a descoberta e o entendimento dos ativos de dados da organização.
16. Completude, acurácia, consistência, tempestividade e unicidade estão entre as dimensões usualmente adotadas para avaliar qualidade de dados.
17. O gerenciamento de dados mestres (MDM) visa estabelecer versão única e confiável dos dados mestres da organização.
18. O conceito de privacy by design exige que os requisitos de proteção de dados sejam incorporados apenas após a homologação do sistema.
19. O mascaramento de dados em ambiente de homologação elimina a necessidade de controle de acesso nesse ambiente.
20. A governança de dados independe do patrocínio da alta gestão, por constituir atribuição exclusivamente técnica das equipes de tecnologia.

### Gabarito

| # | Gab. | Comentário / mecanismo |
|---|---|---|
| 1 | C | Art. 12 da LGPD. |
| 2 | **E** | Definição trocada: o descrito é o princípio da **necessidade**. Finalidade = propósitos legítimos, específicos e informados. Pegadinha recorrente (comparar com CFBio, item 89). |
| 3 | C | Literalidade do art. 5º, VI. |
| 4 | **E** | Absoluto "única". Há dez bases legais no art. 7º. |
| 5 | C | Art. 5º, II. |
| 6 | C | Art. 41, § 2º. |
| 7 | C | Art. 18, V. |
| 8 | C | Art. 4º, I. |
| 9 | **E** | Definições trocadas + absoluto "definitivamente". A pseudonimização é reversível pelo controlador. |
| 10 | C | Art. 38. |
| 11 | C | Art. 7º, VIII / art. 11, II, "f". Item de alta probabilidade em conselho de enfermagem. |
| 12 | C | A governança é o núcleo da roda do DMBOK. |
| 13 | **E** | Definição trocada: infraestrutura é do **data custodian**. O steward zela por definição, qualidade e uso do domínio de dados. |
| 14 | C | Definicional. |
| 15 | C | Definicional. |
| 16 | C | Definicional. |
| 17 | C | Definicional. |
| 18 | **E** | Inversão + "apenas": privacy by design exige incorporação desde a concepção. |
| 19 | **E** | Absoluto "elimina a necessidade". Controles são complementares, não substitutos. |
| 20 | **E** | Absoluto + inversão: patrocínio da alta gestão é condição reconhecida de sucesso, e governança não é atribuição exclusivamente técnica. |

---

---

# SEMANA 8 — Lógica proposicional

## 🟩 Set de 16 itens REAIS — lógica

| # | Prova | Item | Assunto |
|---|---|---|---|
| 1–3 | CRM | 25, 26, 27 | negação de disjunção, equivalência de condicional, bicondicional |
| 4–6 | CFO | 20, 21, 22 | encadeamento de condicionais e conclusão |
| 7–9 | COREN | 27, 28, 30 | negação de condicional, argumento válido, premissa faltante |
| 10–11 | PRODAM | 17, 18 | negação de p→q, equivalência de condicional |
| 12–15 | CFBio | 17, 18, 19, 20 | sequência definida por regra + conclusão sobre conjunto infinito |
| 16 | COREN | 29 | sequência numérica |

> 16 itens é o que existe. Lógica pura é o menor bloco de RLM na banca — a maior parte de RLM é contagem e probabilidade, que vem na semana 9.

---

---

# SEMANA 9 — Contagem, probabilidade e aritmética

## 🟩 Set de 20 itens REAIS — contagem e aritmética

| # | Prova | Item | Assunto |
|---|---|---|---|
| 1–4 | CFBio | 21, 22, 23, 24 | permutação, probabilidade, distribuição com restrição, permutação caótica |
| 5–10 | CFO | 14, 15, 16, 17, 18, 19 | combinação, princípio da inclusão-exclusão, probabilidade geométrica, máximo de tentativas |
| 11–14 | CRM | 21, 22, 23, 24 | combinação, "pelo menos um", probabilidade condicional |
| 15–17 | CRM | 28, 29, 30 | conjuntos com três elementos, complementar, condicional |
| 18 | COREN | 26 | conjuntos, três produtos |
| 19–20 | PRODAM | 12, 21 | "pelo menos uma vez" por complementar, combinação simples |

**Reserva (aritmética e proporção):** COREN 11–15, 18 · PRODAM 11, 13, 14, 19, 22, 23, 25.

---

---

# SEMANA 10 — Português: leitura e semântica

## 🟩 Set de 20 itens REAIS — leitura e semântica

| # | Prova | Item | Assunto |
|---|---|---|---|
| 1–6 | CRM | 1, 2, 3, 4, 5, 6 | tipologia textual, ideias do texto, inferência, extrapolação indevida |
| 7–10 | CFBio | 1, 2, 3, 4 | tipologia dissertativo-expositiva, deturpação de informação, inferência |
| 11–15 | CFO | 1, 2, 3, 4, 5 | ideias do texto, inferência plausível, tese defendida |
| 16–18 | CRM | 11, 12, 15 | gradação, sentido de vocábulo, referente de pronome |
| 19–20 | COREN | 1, 2 | ideia central, opinião categórica |

**Método obrigatório:** todo item de Português da Quadrix se resolve **voltando à linha citada** e confrontando palavra por palavra. Nunca julgue de memória do texto. O mecanismo de erro mais comum é a afirmação que "quase" reproduz o texto, mas insere uma relação causal, um superlativo ou uma generalização que não está lá — veja CFBio 1 e CRM 1 como modelos.

---

---

# SEMANA 11 — Português: gramática e reescrita

## 🟩 Set de 20 itens REAIS — gramática e reescrita

| # | Prova | Item | Assunto |
|---|---|---|---|
| 1–7 | CFBio | 5, 6, 7, 8, 9, 10, 11 | reescrita com conector, crase e regência, função do "que", indeterminação do sujeito, isolamento por vírgulas, concordância |
| 8–15 | CFO | 6, 7, 8, 9, 10, 11, 12, 13 | regência, pontuação, sinonímia, referente, "em que" × "onde", reescrita de voz passiva, crase facultativa |
| 16–20 | CRM | 7, 9, 13, 17, 18 | omissão de trecho e coesão, substituição de expressão, substituição de advérbio, omissão de vírgula, crase antes de verbo |

**Reserva:** CFBio 12–15 · CRM 8, 10, 14, 16, 19, 20 · COREN 7, 10.

> Os dois formatos que mais aparecem: **reescrita mantendo correção e sentido** e **crase**. Se o tempo apertar na semana 11, priorize esses dois.

---

---

# SEMANA 12 — Legislação administrativa

## 🟩 Set de 20 itens REAIS — legislação administrativa

| # | Prova | Item | Norma |
|---|---|---|---|
| 1–5 | CFBio | 41, 42, 43, 44, 45 | Lei 8.429/1992 |
| 6–10 | CFO | 41, 42, 43, 44, 45 | Lei 8.429/1992 (aplicada a caso concreto) |
| 11–15 | CFBio | 46, 47, 48, 49, 50 | LAI 12.527/2011 + Dec. 7.724/2012 |
| 16–20 | CRM | 41, 42, 43, 44, 45 | LAI 12.527/2011 |

**Reserva:** CRM 46–55 (LAI e Decreto 7.724) · CFBio 51, 52 e CFO 48–51 (Lei 9.784/1999) · CFO 52, 53 (Decreto 9.830/2019) · CFO 46, 47 (ética no setor público).

**Treino de formato em lei de conselho:** resolva CFBio 56–70 e CFO 56–70. O conteúdo é de Biologia e Odontologia e não serve; o padrão de pegadinha em lei de conselho é idêntico ao que você enfrentará com Cofen/Coren. São 30 itens.

---

---

# SEMANA 13 — Legislação Cofen/Coren

## 🟦 BLOCO 11 — Legislação Cofen/Coren

> ⚠️ **Leia antes de usar.** Deixei **de fora deliberadamente** todos os itens que dependem de número exato — quantidade de membros do Cofen e dos Corens, duração e reeleição de mandato, prazos recursais, percentuais de repasse de anuidades entre Cofen e Corens, e o número da Resolução Cofen que aprova o Código de Ética vigente. São exatamente os pontos que a Quadrix troca para criar item errado, e eu não vou arriscar te fazer memorizar número errado. **Extraia esses números você mesmo do texto das leis e monte sua própria tabela no Anki.** Os itens abaixo cobrem a camada conceitual e de atribuições, e as normas exatas devem ser confirmadas no edital.

Julgue os itens a seguir.

1. O Conselho Federal e os Conselhos Regionais de Enfermagem constituem autarquias federais, dotadas de personalidade jurídica de direito público.
2. O Conselho Federal e os Conselhos Regionais de Enfermagem constituem, em conjunto, o órgão disciplinador do exercício da profissão de enfermeiro e das demais profissões de enfermagem.
3. A jurisdição dos Conselhos Regionais de Enfermagem restringe-se ao município em que se localiza a respectiva sede.
4. O exercício das atividades de enfermagem exige a inscrição do profissional no Conselho Regional da respectiva jurisdição.
5. Entre as rendas dos Conselhos Regionais de Enfermagem figuram anuidades, taxas, multas e doações.
6. A Lei nº 7.498/1986 dispõe sobre a regulamentação do exercício da enfermagem, sendo regulamentada pelo Decreto nº 94.406/1987.
7. São considerados profissionais de enfermagem o enfermeiro, o técnico de enfermagem, o auxiliar de enfermagem e a parteira.
8. A direção do órgão de enfermagem integrante da estrutura básica da instituição de saúde constitui atividade privativa do enfermeiro.
9. A consulta de enfermagem e a prescrição da assistência de enfermagem constituem atividades privativas do enfermeiro.
10. Os cuidados diretos de enfermagem a pacientes graves, com risco de morte, podem ser delegados ao auxiliar de enfermagem, desde que sob supervisão à distância do enfermeiro.
11. O técnico de enfermagem exerce atividades de nível médio, atuando sob a supervisão do enfermeiro.
12. O auxiliar de enfermagem executa atividades de nível médio, de natureza repetitiva, sob supervisão.
13. O Código de Ética dos Profissionais de Enfermagem é aprovado por lei federal específica.
14. Entre as penalidades aplicáveis por infração ética estão a advertência verbal, a multa, a censura, a suspensão do exercício profissional e a cassação do direito ao exercício profissional.
15. A pena de cassação do direito ao exercício profissional pode ser aplicada e tornada definitiva pelo Conselho Regional, sem participação do Conselho Federal.
16. Das decisões dos Conselhos Regionais de Enfermagem cabe recurso ao Conselho Federal de Enfermagem.
17. Compete ao Conselho Federal de Enfermagem normatizar e expedir instruções destinadas à uniformidade de procedimento e ao bom funcionamento dos Conselhos Regionais.
18. A fiscalização do exercício profissional da enfermagem é atribuição dos Conselhos Regionais, em suas respectivas jurisdições.
19. A inscrição no Conselho Regional é dispensada quando o profissional de enfermagem atua exclusivamente em atividade de docência.
20. O profissional que passa a exercer atividade em jurisdição distinta daquela de sua inscrição principal deve observar as regras de inscrição secundária previstas na regulamentação.

### Gabarito

| # | Gab. | Mecanismo / comentário |
|---|---|---|
| 1 | C | Natureza jurídica dos conselhos de fiscalização profissional. |
| 2 | C | Finalidade institucional do sistema Cofen/Coren. |
| 3 | **E** | A jurisdição é regional/estadual, não municipal. |
| 4 | C | Requisito para o exercício legal. |
| 5 | C | Composição típica das receitas de conselho. |
| 6 | C | Par lei + decreto regulamentador. |
| 7 | C | Categorias previstas na Lei nº 7.498/1986. |
| 8 | C | Atividade privativa do enfermeiro. |
| 9 | C | Atividades privativas do enfermeiro. |
| 10 | **E** | Atividade privativa do enfermeiro + atributo inventado ("supervisão à distância"). Mecanismo típico da banca. |
| 11 | C | Definicional. |
| 12 | C | Definicional. |
| 13 | **E** | Instrumento normativo trocado: o Código de Ética é aprovado por **Resolução do Cofen**. |
| 14 | C | Rol de penalidades éticas. |
| 15 | **E** | Absoluto "sem participação do Conselho Federal": a cassação depende de manifestação do Cofen. |
| 16 | C | Estrutura recursal do sistema. |
| 17 | C | Competência normativa do Cofen. |
| 18 | C | Competência fiscalizatória dos Regionais. |
| 19 | **E** | Absoluto + inversão: o exercício profissional exige inscrição. |
| 20 | C | Inscrição secundária. |

---

---

# APÊNDICE 1 — Mapa completo dos itens reais por tópico

Você já tem esse material. São as quatro provas que você me mandou + as duas do Coren 2013.

**Códigos:**
- `CFBio` = Conselho Federal de Biologia, Quadrix 2025, Analista de Desenvolvimento (C/E, 120 itens)
- `CFO` = Conselho Federal de Odontologia, Quadrix 2025, Analista de Desenvolvimento (C/E, 120 itens)
- `CRM` = CRM-RR, Quadrix 2024, Administrador de Redes (C/E, 120 itens)
- `PRODAM` = Prodam-AM, Quadrix 2022, Analista de TI (múltipla escolha — converter, ver Parte 3)
- `COREN-BD` = Coren-SP, VUNESP 2013, Administrador de Banco de Dados (múltipla escolha)
- `COREN-SI` = Coren-SP, VUNESP 2013, Analista de Segurança da Informação (múltipla escolha)

---

# APÊNDICE 2 — Como fabricar seus próprios itens

---

# APÊNDICE 3 — Pares confundíveis

**Pares confundíveis que estes blocos exercitam:**
ETL × ELT · star × snowflake · SCD tipo 1 × tipo 2 × tipo 3 · Kimball × Inmon · transformation × job · pipeline × workflow · Lambda × Kappa · Parquet/ORC × Avro · staging × camada de consumo · IaaS × SaaS · horizontal × vertical · MapReduce × Spark · data drift × concept drift · stemming × lematização · pooling (reduz × aumenta) · parâmetro × hiperparâmetro · M × DAX · medida × coluna calculada · Import × DirectQuery · RANK × DENSE_RANK × ROW_NUMBER · LEFT × RIGHT JOIN · lei × resolução · Regional × Federal.