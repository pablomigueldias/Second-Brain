

## Passo 6 — Baixar o dataset

1. Procure por **"Telco Customer Churn dataset"** — é um dataset público muito conhecido (originalmente disponibilizado pela IBM, hospedado no Kaggle e em vários mirrors).
2. Baixe o arquivo CSV (nome típico: `WA_Fn-UseC_-Telco-Customer-Churn.csv`).
3. Renomeie para `telco_churn.csv` para simplificar.
4. Coloque dentro de `data/raw/`.

> O arquivo final: `data/raw/telco_churn.csv`

---

## Passo 7 — Primeiro commit

Conecte o projeto local ao GitHub e faça o primeiro envio:

```bash
git init
git add .
git commit -m "Estrutura inicial do projeto de previsão de churn"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/churn-prediction.git
git push -u origin main
```

> Troque `SEU-USUARIO` pela sua conta. Esse é o seu **primeiro commit** — o projeto já está no ar.

---

## ✅ Checklist final do Dia 1

- [ ] Repositório criado no GitHub
- [ ] Estrutura de pastas no lugar
- [ ] `venv` criado e ativado (aparece `(venv)` no terminal)
- [ ] `pip install -r requirements.txt` rodou sem erro
- [ ] Interpretador selecionado no VS Code
- [ ] Dataset em `data/raw/telco_churn.csv`
- [ ] Primeiro commit enviado para o GitHub

Se todos os itens estão marcados: **Dia 1 concluído.** Pode partir para o notebook `01_eda.ipynb`.

---

## 📌 Lembrete importante sobre o `venv`

Toda vez que você abrir o projeto de novo, precisa **ativar o venv** antes de trabalhar:

```bash
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

Se esquecer, o Python não vai achar as bibliotecas. Se aparecer "ModuleNotFoundError", quase sempre é o venv desativado.