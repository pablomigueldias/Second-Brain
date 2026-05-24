
## 🔍 Etapa 2 — Análise Exploratória (Dias 3-4)

**O que fazer:** abra `notebooks/01_eda.ipynb` no VS Code e rode célula por célula. O notebook já está todo comentado e guiado.

Sua tarefa ativa:

- Rodar tudo e entender cada saída.
- Na seção 5, criar gráficos extras para outras colunas (o notebook te orienta).
- Preencher a célula final de **conclusões** com o que você descobriu.

**Revise:** suas notas _03 - Definições e Conceitos_ e _09 - Datasets Desbalanceados_.

**Commit:** `"Adiciona análise exploratória dos dados"`

---

## 🔧 Etapa 3 — Engenharia de Atributos (Dia 5)

**O que fazer:** o código de limpeza já está pronto em `src/preprocessing.py` — todo comentado. Sua tarefa:

- Ler o arquivo inteiro e **entender cada função** (os comentários explicam tudo).
- Testá-lo: com o `venv` ativo, rode `python src/preprocessing.py` e veja se funciona.
- Se a EDA revelou algum problema extra nos dados, adicionar o tratamento aqui.

**Revise:** suas notas _01 - Engenharia de Atributos_ e _07 - Codificação de Categorias_.

**Commit:** `"Adiciona módulo de pré-processamento dos dados"`

---

## 🤖 Etapa 4 — Treinar e Comparar Modelos (Dias 6-7)

**O que fazer:** criar o `notebooks/02_modelagem.ipynb`. Quando chegar aqui, me peça ("estou na Etapa 4") e eu te entrego o notebook comentado.

Você vai:

- Treinar Naive Bayes, Árvore de Decisão e Random Forest.
- Comparar com validação cruzada.
- Avaliar por **recall e F1**, não acurácia.

**Revise:** suas notas _04 - Classificação_, _05 - Matriz de Confusão_, e do módulo Algoritmos: _04 - Naive Bayes_, _06 - Árvores de Decisão_, _08 - Random Forest_.

**Commit:** `"Treina e compara modelos de classificação"`

---

## ⚖️ Etapa 5 — SMOTE + Avaliação por Custo (Dias 8-9)

**O que fazer:** aplicar SMOTE no conjunto de treino e refazer a avaliação. Depois, traduzir a matriz de confusão em **dinheiro**, usando os custos da Etapa 1.

> Esta é a etapa que mais diferencia seu projeto. Quase nenhum portfólio júnior faz análise de custo. Capriche.

**Revise:** suas notas _09 - Datasets Desbalanceados_ e _06 - Custo de um Modelo_.

**Commit:** `"Aplica SMOTE e avaliação por custo de negócio"`

---

## 📝 Etapa 6 — Script de Treino + Conclusão (Dia 10)

**O que fazer:**

- Criar `src/train.py`: um script que roda o pipeline inteiro e **salva o modelo** num arquivo `.pkl` (me peça quando chegar aqui).
- Preencher a seção **"Conclusão"** do README.

**Commit:** `"Adiciona script de treino e salva o modelo"`

---

## 🌐 Etapa 7 — API com FastAPI (Dia 11)

**O que fazer:** criar `api/main.py` — uma API que carrega o modelo salvo e responde previsões. Me peça quando chegar aqui que eu te entrego o código comentado.

Ao final, a API roda com `uvicorn api.main:app --reload` e você testa no navegador.

**Revise:** nada de ML — aqui é seu lado web. Vai ser tranquilo para você.

**Commit:** `"Adiciona API para servir o modelo"`

---

## ✨ Etapa 8 — Polimento Final (Dia 12)

**O que fazer:**

- Revisar o README inteiro: preencher tudo que falta, apagar os comentários 🖊️.
- Conferir que os notebooks rodam do início ao fim sem erro.
- Adicionar a tabela de resultados e a matriz de confusão (como imagem) no README.
- Conferir que o `.gitignore` está funcionando (sem `venv/` no GitHub).
- Commit final caprichado.

**Commit:** `"Finaliza documentação e resultados do projeto"`

---

## 📌 Quando me pedir ajuda

Nos pontos marcados, volte aqui no chat e diga em qual etapa está. Vou te entregar:

- **Etapa 4:** o notebook `02_modelagem.ipynb` comentado.
- **Etapa 5:** o código de SMOTE + função de cálculo de custo.
- **Etapa 6:** o script `src/train.py`.
- **Etapa 7:** o código `api/main.py`.

Entreguei assim, em pedaços, de propósito: se eu te desse tudo pronto agora, você ia só copiar e colar sem aprender. Fazendo etapa por etapa, cada parte do código chega quando você já tem contexto para entendê-la. **O objetivo é você aprender, não só ter um repositório.**

---

## ⏱️ Resumo do cronograma (1-2 semanas)

|Dias|Etapa|Entregável|
|---|---|---|
|1|Setup|Ambiente + repositório no ar|
|2|Problema|Seção do README escrita|
|3-4|EDA|Notebook 01 completo|
|5|Eng. Atributos|preprocessing.py entendido|
|6-7|Modelagem|Notebook 02 completo|
|8-9|SMOTE + Custo|Avaliação financeira|
|10|Treino + Conclusão|train.py + README|
|11|API|API funcionando|
|12|Polimento|Projeto finalizado|

Sobram 2 dias de folga numa janela de 2 semanas — use para imprevistos (vão acontecer) ou para aprofundar uma etapa que você curtiu.