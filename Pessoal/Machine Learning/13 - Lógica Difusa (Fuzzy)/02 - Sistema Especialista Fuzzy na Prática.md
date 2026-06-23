---
tags:
  - machine-learning
  - lógica-difusa
  - fuzzy
  - sistemas-especialistas
  - prática
  - scikit-fuzzy
---

# 2. Sistema Especialista Fuzzy na Prática

> [!info] O que esta nota cobre
> A construção passo a passo de um sistema especialista fuzzy usando o exemplo de um **classificador de gravidade da asma**, incluindo funções de pertinência, regras e o código com `scikit-fuzzy`.

> [!warning] Aviso
> O exemplo a seguir é **totalmente fictício** e criado apenas para fins **didáticos** — não use para decisões médicas reais.

---

## 1. O problema: classificar a gravidade da asma

Queremos um sistema que receba métricas do paciente e infira a **gravidade** da asma.

> [!abstract] Variáveis linguísticas
> **Antecedentes** (entradas):
> 1. **Frequência de Crises**
> 2. **Uso de SABA** — agonista adrenérgico beta-2, medicamento de tratamento
> 3. **Débito Expiratório** — métrica da capacidade de expiração
>
> **Consequente** (saída — o objetivo do sistema):
> 4. **Classificação / Gravidade**

---

## 2. Os conjuntos difusos

| Crises | SABA | Débito Expiratório | Gravidade |
|---|---|---|---|
| Semanal | Semanal | 50–80% | Moderada |
| Diário | Diário | 33–55% | Aguda Grave |
| Contínuo | Contínuo | < 33% | Risco de Vida |
| **Antecedentes** | | | **Consequente** |

---

## 3. As etapas

```
① Criar variáveis linguísticas
② Definir funções de pertinência
③ Criar as regras
④ Criar o sistema Fuzzy
⑤ Inferir e avaliar os resultados
```

---

## 4. Funções de pertinência

> [!note] Definição
> Uma **função de pertinência** é uma função matemática que define o **grau de pertinência** de um elemento a um conjunto fuzzy — ou seja, o quão bem ele se encaixa em uma categoria linguística.

> [!example] Principais formatos
> - **Triangular (`trimf`)** — forma de triângulo, definida por **3 pontos** (início, máximo, fim). Pertinência varia linearmente.
> - **Trapezoidal (`trapmf`)** — forma de trapézio, definida por **4 pontos** (dois de subida, dois de descida). Topo "plano" de pertinência máxima.
> - **Gaussiana (`gaussmf`)** — curva suave em forma de sino.
> - **Sino generalizado (`gbellmf`)**.
> - **Sigmoidal (`sigmf`)** — transição em "S".

---

## 5. Implementação com `scikit-fuzzy`

> [!tip] Biblioteca
> Usaremos a `scikit-fuzzy`, que traz `Antecedent`, `Consequent`, `Rule` e o `ControlSystem`.

```python
!pip install -U scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
```

### Passo 1 — Variáveis (universo de 0 a 100)

```python
crises              = ctrl.Antecedent(np.arange(0, 101, 1), 'crises')
saba                = ctrl.Antecedent(np.arange(0, 101, 1), 'saba')
debito_expiratorio  = ctrl.Antecedent(np.arange(0, 101, 1), 'debito_expiratorio')
gravidade           = ctrl.Consequent(np.arange(0, 101, 1), 'gravidade')
```

### Passo 2 — Funções de pertinência

```python
# Antecedentes: trapézios (faixas com "platô")
crises['semanal']  = fuzz.trapmf(crises.universe, [0, 0, 30, 50])
crises['diario']   = fuzz.trapmf(crises.universe, [30, 50, 70, 90])
crises['continuo'] = fuzz.trapmf(crises.universe, [80, 90, 100, 100])

saba['semanal']  = fuzz.trapmf(saba.universe, [0, 0, 20, 40])
saba['diario']   = fuzz.trapmf(saba.universe, [20, 40, 60, 80])
saba['continuo'] = fuzz.trapmf(saba.universe, [80, 90, 100, 100])

debito_expiratorio['50-80']    = fuzz.trapmf(debito_expiratorio.universe, [0, 0, 20, 40])
debito_expiratorio['33-55']    = fuzz.trapmf(debito_expiratorio.universe, [20, 40, 60, 80])
debito_expiratorio['menos_33'] = fuzz.trapmf(debito_expiratorio.universe, [80, 90, 100, 100])

# Consequente: triângulos
gravidade['moderada']    = fuzz.trimf(gravidade.universe, [0, 30, 60])
gravidade['aguda_grave'] = fuzz.trimf(gravidade.universe, [30, 60, 85])
gravidade['risco_vida']  = fuzz.trimf(gravidade.universe, [90, 100, 100])
```

> [!tip] Visualizar os conjuntos
> `crises.view()` desenha as funções de pertinência — ótimo para conferir as sobreposições antes de rodar.

### Passo 3 — As regras difusas

```python
rule1 = ctrl.Rule(crises['semanal']  | saba['semanal']  | debito_expiratorio['50-80'],    gravidade['moderada'])
rule2 = ctrl.Rule(crises['diario']   | saba['diario']   | debito_expiratorio['33-55'],    gravidade['aguda_grave'])
rule3 = ctrl.Rule(crises['continuo'] | saba['continuo'] | debito_expiratorio['menos_33'], gravidade['risco_vida'])
```

> [!note] O operador `|`
> Aqui o `|` (OU difuso) significa que **qualquer** antecedente naquele nível ativa a regra — o sistema pega o **máximo** dos graus.

### Passo 4 — Montar o sistema

```python
asthma_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
asthma = ctrl.ControlSystemSimulation(asthma_ctrl)
```

### Passo 5 — Inferir e avaliar

```python
asthma.input['crises'] = 95
asthma.input['saba'] = 95
asthma.input['debito_expiratorio'] = 100

asthma.compute()

resultado = asthma.output['gravidade']
print("Gravidade da Asma:", resultado)

if   0  <= resultado < 60:  print("Gravidade é Moderada")
elif 60 <= resultado < 90:  print("Gravidade Aguda Grave")
else:                       print("Gravidade Risco de Vida")
```

> [!success] O que aconteceu
> Entradas **precisas** (95, 95, 100) foram **fuzzificadas**, passaram pelas **regras**, e o `compute()` fez a **defuzzificação** devolvendo um número **crisp** — que o `if/elif` traduz de volta para a categoria de gravidade.

---

## 6. Resumo mental

> [!summary] O ciclo completo na prática
> 1. **Variáveis** (`Antecedent`/`Consequent`) sobre um **universo** (`np.arange`).
> 2. **Funções de pertinência** (`trapmf`, `trimf`) definem os conjuntos.
> 3. **Regras** (`ctrl.Rule`) ligam antecedentes → consequente.
> 4. **`ControlSystem`** + **`Simulation`** montam o motor.
> 5. **`input` → `compute()` → `output`**: entra crisp, sai crisp.

---

## 🏷️ Tags Relacionadas
#machine-learning #lógica-difusa #fuzzy #scikit-fuzzy #prática #estudos

---
[[01 - Introdução à Lógica Difusa|⬅️ Nota anterior]] · [[00 - Índice|⬆️ Voltar ao Índice do Módulo]]
