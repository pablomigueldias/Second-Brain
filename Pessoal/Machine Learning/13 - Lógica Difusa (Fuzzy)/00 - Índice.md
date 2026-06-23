---
tags:
  - machine-learning
  - moc
  - índice
  - lógica-difusa
  - fuzzy
aliases:
  - Lógica Difusa
  - Fuzzy
---

# Lógica Difusa (Fuzzy)

> [!info] Sobre este módulo
> Este é o **mapa de conteúdo (MOC)** do módulo **13 — Lógica Difusa (Fuzzy)**. Em vez do mundo preto-no-branco da lógica booleana (0 ou 1), a lógica difusa trabalha com **graus** (meio cheio, quase quente), simulando o **raciocínio humano** para tomar decisões.

---

## Roteiro de Estudo

- [[01 - Introdução à Lógica Difusa]] — Booleana vs. difusa, graus de pertinência, variáveis linguísticas e o sistema de inferência.
- [[02 - Sistema Especialista Fuzzy na Prática]] — Construir um sistema fuzzy passo a passo (exemplo do classificador de asma).

---

## Visão Geral em uma Imagem Mental

```
   Entrada precisa (crisp)
        │  Fuzzificação
        ▼
   Conjuntos difusos (graus 0 a 1)
        │  Regras "Se... Então..."
        ▼
   Sistema de Inferência (Mamdani / Takagi-Sugeno)
        │  Defuzzificação
        ▼
   Saída precisa (crisp)
```

---

## Conceito-Chave Rápido (cola)

> [!summary] Para não esquecer
> - **Booleana** = 0 ou 1. **Difusa** = qualquer valor **entre 0 e 1** (pertinência parcial).
> - **Variáveis linguísticas** = "baixo, médio, alto" em vez de números exatos.
> - **Fuzzificação** (entrada → graus) → **regras** → **inferência** → **defuzzificação** (→ valor preciso).
> - Simula o **raciocínio humano**; usada em eletrodomésticos, controle, diagnóstico.

---

## 🏷️ Tags Relacionadas
#machine-learning #lógica-difusa #fuzzy #sistemas-especialistas #estudos

---
[[_Índice Machine Learning|⬅️ Voltar ao Índice do Curso]]
