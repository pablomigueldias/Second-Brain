# Cronograma 90 dias — v2 (ordem: Específicos → Matemática → Português → Lei)
## Coren-SP / Quadrix — Analista de Ciência de Dados e IA

> Substitui a v1. Mesma estrutura de prova, mesmas regras de marcação, ordem das fases invertida conforme sua escolha.

---

## Estrutura das fases

| Fase | Semanas | Dias | Conteúdo | Itens na prova |
|---|---|---|---|---|
| **1** | 1–7 | 1–49 | Conhecimentos Específicos | ~50 |
| **2** | 8–9 | 50–63 | Matemática e Raciocínio Lógico | ~9 |
| **3** | 10–11 | 64–77 | Português | ~15 |
| **4** | 12–13 | 78–90 | Legislação + simulados | ~30 |

**Trilhas de fundo, contínuas:**
- 30 itens C/E por dia a partir do dia 4, misturando tópicos já vistos
- 20–30 min de Português por dia desde o dia 1 — **só questões, sem teoria**
- Carro: áudio conforme tabela na seção final
- Anki todos os dias

---

## Rotina diária (3h de mesa)

| Tempo | Atividade |
|---|---|
| 25 min | Português — só questões, dos itens reais mapeados |
| 105 min | Bloco da fase atual |
| 30 min | 30 itens C/E do bloco + tópicos anteriores |
| 20 min | Anki |

**Domingo (1h30):** só erros da semana + Anki completo. Sem conteúdo novo.

---

## Regra de marcação

| Penalidade | Break-even | Regra prática |
|---|---|---|
| −1,0 | 50% | marque só com **≥70%** de convicção |
| −0,5 | 33% | marque com **≥55%** |

Item em branco = 0, sem penalização. Confirmar o valor no edital.

**Os seis mecanismos do item errado:** termo absoluto · definição trocada entre conceitos irmãos · inversão de causa e efeito · atributo de uma ferramenta colado em outra · número ou prazo trocado · "é vedado" × "é permitido".

---

# FASE 1 — Conhecimentos Específicos (dias 1–49)

### Semana 1 (dias 1–7) — Diagnóstico + Estatística e Probabilidade

- **Dias 1–2:** prova CFBio 2025 completa, cronometrada, 120 itens. Anote acertos por bloco — é a linha de base.
- Montar deck de Anki e uma nota por tópico no Obsidian.
- **Estatística descritiva:** medidas de posição e dispersão, boxplot, assimetria, curtose, coeficiente de variação.
- **Probabilidade:** axiomas, condicional, independência, **Bayes**.
- **Distribuições:** binomial, Poisson, normal, t, qui-quadrado.
- Questões: **Bloco A** do banco (20 itens).

> Atenção à divisão: estatística aplicada a dados é **específico**. Combinatória, lógica proposicional e aritmética são **RLM**, e ficam na Fase 2.

### Semana 2 (dias 8–14) — Estatística inferencial + Python + SQL

- **Inferência:** TCL, intervalo de confiança, teste de hipótese, erro tipo I e II, p-valor, correlação de Pearson, regressão linear simples e múltipla, R² e R² ajustado, multicolinearidade.
- **Python em modo prova:** pandas (groupby, merge, pivot, apply), numpy, e o "quem faz o quê" das bibliotecas — scikit-learn, matplotlib, seaborn, TensorFlow, PyTorch.
- **SQL analítico:** joins, subqueries, window functions, CTE, agregações, `HAVING` vs `WHERE`, `DELETE`/`TRUNCATE`/`DROP`, DDL/DML/DCL.
- Questões reais: CFO 91–100 · CFBio 91–93 · PRODAM 37, 39, 53.

### Semana 3 (dias 15–21) — Banco de dados

Terreno seu, mas a prova cobra no papel o que você faz na prática.

- **Relacional:** modelo ER, entidade fraca e associativa, normalização 1FN–BCNF (**treine no papel**), ACID, integridade referencial e de domínio, índices, plano de execução, desnormalização, catálogo do sistema, deadlock, triggers, stored procedures.
- **NoSQL:** os quatro tipos, teorema CAP, BASE, quando usar cada um.
- **Recuperação de dados:** tipos de backup, WAL, PITR, RTO/RPO, replicação, hot/warm/cold-site.
- Questões reais: CFO 81–90 · CFBio 86–88 · PRODAM 31, 36–39, 51–55, 60 · COREN-BD 31–45 *(só os conceituais — pule tudo com versão de produto)*.

### Semana 4 (dias 22–28) — DW, modelagem dimensional e ETL

Seu maior ponto cego. Nada disso existia na prova de 2013 e não existe em prova Quadrix.

- **DW:** OLTP × OLAP, ETL × ELT, fato e dimensão, star × snowflake, granularidade, SCD tipos 1/2/3, Kimball × Inmon, Data Lake / Lakehouse / Data Mesh.
- **Ferramentas do edital:** Pentaho PDI (transformation × job, steps, hops) e Apache Hop (fork do Pentaho; pipelines × workflows).
- **Engenharia de dados:** orquestração e DAGs (Airflow), batch × streaming, arquiteturas Lambda e Kappa, particionamento, formatos colunares (Parquet, ORC, Avro), idempotência e reprocessamento, Delta Lake / Iceberg.
- **Integração via API:** REST, paginação, autenticação, códigos de status. Questões: CFBio 101–105.
- 📝 **Discursiva 1** (manuscrita, 20–30 linhas, cronometrada): *"Arquitetura de pipeline de dados para processamento de grandes volumes"*.
- Questões: **Bloco D** — me pede que eu escrevo.

### Semana 5 (dias 29–35) — Nuvem, Big Data e núcleo genérico de TI

Pontos baratos: apareceram nas três provas de conselho da Quadrix, em todos os cargos.

- **Nuvem:** IaaS/PaaS/SaaS, elasticidade, hypervisores, snapshots. Tabela comparativa AWS × Azure × GCP para armazenamento, DW, ML e processamento → decoreba, vai para o Anki e para o carro.
- **Big Data:** Hadoop (HDFS, MapReduce, YARN), Spark (RDD, DataFrame, lazy evaluation), Kafka.
- **Núcleo genérico:** arquitetura e hierarquia de cache, gerenciamento de processos e memória, Linux (comandos e `/etc`), redes e protocolos, journaling.
- Questões reais: CRM 71–91 e 116–120 · CFBio 71–80 · COREN-BD 46–47, 53–57 · COREN-SI 38–52.

### Semana 6 (dias 36–42) — Segurança da informação e Governança de TI

53 itens reais disponíveis. É o bloco com maior densidade de questão real por hora de estudo.

- **Segurança:** CID, phishing, engenharia social, malware por tipo (rootkit, trojan, hijacker, keylogger, spyware), criptografia, certificados, ISO 27001/27002, controle de acesso (RBAC, MAC, DAC), honeypot, IDS/IPS, SQL injection.
- **Governança de TI:** ITIL (as 5 fases do ciclo de vida de serviço), COBIT, PMBOK (os 5 grupos de processos).
- Questões reais: CFO 71–80 · CFBio 81–85 · CRM 92–109 · PRODAM 32–35 · COREN-SI 31–37, 53–60.
- 📝 **Discursiva 2:** *"Segurança da informação e proteção de dados em sistemas de conselho profissional"*.

### Semana 7 (dias 43–49) — ML, DL, NLP, Power BI e Governança de dados

Semana densa, mas é seu território mais forte. Se atrasar, o corte aceitável é aqui.

**Dias 43–45 — Machine Learning e Deep Learning**
- Supervisionado × não supervisionado × por reforço
- Algoritmos: regressão linear e logística, árvores, random forest, gradient boosting, SVM, KNN, Naive Bayes, k-means, PCA
- Métricas: matriz de confusão, acurácia, precisão, recall, F1, ROC/AUC, RMSE, MAE
- Overfitting, bias-variance, regularização L1/L2, validação cruzada, desbalanceamento, CRISP-DM
- DL: perceptron, backpropagation, ativações, época/batch/learning rate, dropout, CNN, RNN/LSTM, Transformers, embeddings
- NLP: tokenização, stemming × lematização, TF-IDF, word2vec, BERT, LLMs, RAG
- MLOps: deploy batch × online, API de inferência, **data drift × concept drift**, retreinamento, feature store, MLflow
- Questões: **Bloco B** do banco (20 itens)

**Dias 46–47 — Power BI**
- Power Query (M) × DAX · modelagem e cardinalidade · Import × DirectQuery × Live Connection · medida × coluna calculada · contexto de linha × contexto de filtro · CALCULATE, FILTER, SUMX, ALL, RELATED · Power BI Service (workspace, dataset, gateway, RLS, atualização agendada)
- **Instale e faça 3 dashboards.** Conceito sem prática não gruda.

**Dias 48–49 — Governança de dados + LGPD**
- DAMA-DMBOK, data owner / steward / custodian, dimensões de qualidade, catálogo, linhagem, MDM, mascaramento, privacy by design
- **LGPD:** princípios (atenção a finalidade × necessidade), bases legais, dados sensíveis, direitos do titular, controlador / operador / encarregado, ANPD, anonimização × pseudonimização, RIPD, tutela da saúde
- Questões: **Bloco C** do banco (20 itens)

> A LGPD é a única lei antecipada, e por um motivo objetivo: ela cai nos Complementares **e** dentro dos Específicos. Mesma hora de estudo, retorno dobrado.

🎯 **Domingo, dia 49 — Simulado 1:** prova CFO 2025 completa, cronometrada, com penalização aplicada. Compare com o diagnóstico do dia 1.

---

# FASE 2 — Matemática e Raciocínio Lógico (dias 50–63)

### Semana 8 (dias 50–56) — Lógica

- Lógica proposicional: conectivos, tabela-verdade, negação de condicional e de disjunção, equivalências, contrapositiva
- Argumento válido, premissas, conclusão
- Diagramas lógicos e quantificadores
- Sequências e padrões numéricos
- Questões reais: CRM 25–30 · CFO 20–22 · COREN 26–30 · PRODAM 17–18, 29

🎧 **A partir de hoje começa o áudio de legislação no carro.** Passivo, sem estudo sentado. Ver tabela na seção final.

### Semana 9 (dias 57–63) — Contagem, probabilidade e aritmética

- Combinatória: princípio fundamental, permutação, arranjo, combinação, permutação com repetição, anagramas
- Probabilidade em problemas de contagem, "pelo menos um", complementar
- Conjuntos: união, interseção, diagrama de Venn, problemas com três conjuntos
- Razão e proporção, porcentagem, juros simples, regra de três, média ponderada
- Geometria básica: áreas, volumes, escala
- Questões reais: CFBio 17–24 · CFO 14–19 · CRM 21–24, 28–30 · PRODAM 11–16, 19–25 · COREN 11–20
- 📝 **Discursiva 3:** *"Métricas de avaliação de modelos de classificação e a escolha da métrica adequada ao problema"*

---

# FASE 3 — Português (dias 64–77)

Você já vem fazendo 25 min/dia desde o dia 1. Aqui vira o bloco principal.

### Semana 10 (dias 64–70) — Leitura e semântica

- Tipologia e gênero textual, ideias do texto, inferência × informação explícita, opinião × fato
- Referenciação e coesão: pronomes, elipse, retomada
- Semântica: sinonímia em contexto, ambiguidade, sentido conotativo
- Relações lógico-discursivas: conclusão, explicação, concessão, condição, finalidade, contraste
- Questões reais: CRM 1–20 · CFBio 1–4, 12–16
- **Método:** todo item de Português da Quadrix se resolve confrontando a afirmação com o trecho exato do texto. Nunca julgue de memória — volte à linha citada.

### Semana 11 (dias 71–77) — Gramática e reescrita

- Crase (foco: casos facultativos e antes de verbo)
- Regência nominal e verbal
- Concordância verbal e nominal
- Emprego do "que" e do "se" (partícula apassivadora × índice de indeterminação)
- Pontuação: vírgula em adjunto adverbial deslocado, aposto, oração adjetiva restritiva × explicativa
- **Reescrita mantendo sentido e correção** — o formato mais frequente da banca
- Questões reais: CFBio 5–11 · CFO 6–13 · COREN 7–10
- 📝 **Discursiva 4:** *"Governança de dados e conformidade com a LGPD em conselho profissional"*

🎯 **Domingo, dia 77 — Simulado 2:** prova CRM-RR 2024 completa.

---

# FASE 4 — Legislação (dias 78–90)

Duas semanas, com o vocabulário já familiar por causa do áudio das semanas 8 a 11. O objetivo agora é **fixar números, prazos e literalidade** — não conhecer o assunto.

### Semana 12 (dias 78–84) — Legislação administrativa

| Dias | Norma | Foco | Questões reais |
|---|---|---|---|
| 78–79 | **Lei 8.429/1992** (Improbidade) | sujeitos, modalidades, sanções, prazo prescricional, acordo de não persecução civil | CFBio 41–45 · CFO 41–45 |
| 80–81 | **LAI 12.527/2011 + Dec. 7.724/2012** | prazos, sigilo, requerimento, transparência ativa × passiva, definições | CFBio 46–50 · CRM 41–55 |
| 82–83 | **Lei 9.784/1999 + Dec. 9.830/2019** | prazo recursal, instâncias, impedimento × suspeição, motivação, erro grosseiro | CFBio 51–52 · CFO 48–53 |
| 84 | Revisão de LGPD (já vista na semana 7) + ética no setor público | — | CFO 46–47 |

**Método para lei seca:** tabela de números (prazos, quóruns, percentuais, quantidade de membros) + Anki de par confundível. A Quadrix erra o item trocando o número.

### Semana 13 (dias 85–90) — Legislação Coren + fechamento

⚠️ **Bloco de maior retorno por hora de todo o cronograma.** Conteúdo curto, cobrado na literalidade, ninguém de TI estuda, e vale ~15 itens em 120.

| Dia | Atividade |
|---|---|
| 85 | **Lei 5.905/1973** (cria Cofen e Corens): composição, competências, receitas, mandatos |
| 86 | **Lei 7.498/1986 + Decreto 94.406/1987** (exercício da enfermagem): atribuições privativas por categoria |
| 87 | **Código de Ética dos Profissionais de Enfermagem** + Regimento Interno do Coren-SP |
| 88 | 🎯 **Simulado 3** completo + correção |
| 89 | Só erros do simulado + 📝 **Discursiva 5** + Anki total |
| 90 | Leitura passiva das notas do Obsidian. Sem conteúdo novo. Dormir cedo. |

**Treino de formato, faça na semana 12:** resolva CFBio 56–70 e CFO 56–70 — legislação de conselho de Biologia e Odontologia. O conteúdo não serve, o padrão de pegadinha em lei de conselho é idêntico.

> Confirmar as normas exatas quando o edital sair. Estas são as candidatas prováveis pelo padrão Quadrix em conselho profissional, não fato consumado.

---

## Trilha do carro

| Semanas | Áudio |
|---|---|
| 1–4 | Definições de estatística, vocabulário de ETL e DW, suas notas do Obsidian |
| 5–7 | Tabela de serviços cloud, ITIL/COBIT/PMBOK, métricas de ML, LGPD |
| **8–11** | **Legislação: texto de 8.429, LAI, 9.784, Lei 5.905/1973, Código de Ética** ← começa aqui |
| 12–13 | Legislação em revisão + suas notas, tudo |
| Sempre | Podcast de atualidades e geopolítica, 2 a 3× por semana |

Grave TTS das notas ou sua própria voz — a própria voz gruda mais.

> **Teto de ferramenta:** você vai querer construir o pipeline TTS + gerador de itens. Vale, mas **um domingo, versão feia, 2 horas**. Passou disso, vai para o backlog.

## Inglês e Atualidades

Fora da mesa. Inglês: 20 min, 2× por semana, some ao que você já faz (série com legenda, Duolingo, podcast). Itens reais: CFO 32–40 · CRM 31–40 · COREN-SI 21–25. Atualidades: só podcast e manchetes. Padrão da banca: geopolítica (China/EUA, Oriente Médio, América Latina) + tecnologia.

## Discursiva

Estrutura literal do que a banca pede: introdução curta → **um parágrafo por aspecto obrigatório, na ordem a) b) c)** → conclusão curta. 20 a 30 linhas, manuscrita, caneta preta ou azul, sem identificação. Não abordar um dos três aspectos = perder aquele terço da nota.

---

## Riscos desta ordem, para você monitorar

1. **Português concentrado no fim.** É habilidade, não decoreba — se os 25 min/dia caírem, esse bloco fica descoberto. É o ponto frágil.
2. **Legislação em 2 semanas.** Funciona *se* o áudio das semanas 8–11 acontecer. Sem o áudio, 30 itens em 14 dias é apertado.
3. **Semana 7 sobrecarregada.** ML + DL + NLP + Power BI + governança em 7 dias. Se atrasar, corte Power BI para a semana 12 — é o mais autocontido.

## Checkpoints

- [ ] **Dia 2:** diagnóstico por bloco. Se Português vier abaixo de 40%, suba os 25 min para 45 min desde já.
- [ ] **Publicação do edital:** parar 1 dia, comparar o programático, ajustar.
- [ ] **Dia 49 (Simulado 1):** se os específicos não passarem de 70%, adie a Fase 2 por uma semana e reforce os blocos fracos.
- [ ] **Dia 77 (Simulado 2):** calibragem da regra de chute + decidir se legislação precisa invadir a semana 11.
