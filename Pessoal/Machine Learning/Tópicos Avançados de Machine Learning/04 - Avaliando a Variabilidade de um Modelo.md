---
tags:
  - machine-learning
  - tópicos-avançados
  - avaliação
  - intervalo-de-confiança
  - estatística
---

# 4. Avaliando a Variabilidade de um Modelo

> [!info] O que esta nota cobre
> Por que o acerto de um modelo **não é um número fixo**, e sim uma **faixa de valores**. Vamos aprender a calcular **intervalos de confiança** — para a média e para a proporção — e entender por que isso é vital antes de prometer resultados a um cliente.

---

## 4.1. Cenário: O Projeto de Detecção de Fraude

> [!example] A situação
> Seu cliente vende um produto online por **R$ 50,00**:
> - **30 mil transações** por mês.
> - **15%** das transações são **fraudulentas** (4.500 fraudes).
> - **Faturamento mensal**: R$ 1.275.000,00.
> - **Perdas com fraude**: R$ 225.000,00.
> - **Margem de lucro** (5%): R$ 63.750,00.
>
> **Pergunta do cliente:** *posso reduzir minha perda com fraudes?*

### Sua proposta

Você coleta dados, faz testes, e cria um modelo com **90% de acerto**. Com base nisso, propõe:

> [!note] A proposta de negócio
> - Reduzir fraude de **15% para 10%**.
> - Faturamento: de R$ 1.275.000 para **R$ 1.350.000**.
> - Perdas com fraude: de R$ 225.000 para **R$ 150.000**.
> - **Custo do projeto**: R$ 300.000,00.
> - **ROI (retorno) em apenas 4 meses!** 🎉

Parece ótimo. Mas...

---

## 4.2. A Questão Crítica

> [!question] A pergunta que muda tudo
> **É seguro afirmar um acerto de 90%?**

> [!danger] A resposta: NÃO
> **Não**, porque estamos trabalhando com **amostras**, e amostras estão sujeitas a **variabilidade**.
>
> **Agravante:** modelos de negócio mudam rapidamente, e isso pode influenciar o resultado — às vezes mais rápido do que você consegue atualizar o modelo.

> [!important] A lição central desta nota
> Quando você diz "o modelo tem 90% de acerto", esse **90% veio de uma amostra específica**. Com outra amostra, daria 88%, ou 91%, ou 89,5%... O número "90%" **não é uma verdade absoluta** — é uma estimativa que **varia**.

---

## 4.3. A Solução: Intervalos de Confiança

> [!note] A ideia
> Em vez de prometer **um número**, prevemos uma **faixa de variabilidade** do resultado. Essa faixa é o **intervalo de confiança**.

Há **duas formas** de calcular, dependendo de como você roda o modelo:

> [!info] Duas abordagens
> 1. **Intervalo de Confiança para a Média** → quando você roda o modelo **várias vezes** e usa a média dos resultados.
> 2. **Intervalo de Confiança para a Proporção** → quando você roda o modelo **uma única vez**.

---

## 4.4. Intervalo de Confiança para a Média

> [!note] Quando usar
> Quando você cria **vários modelos** (ex: 100 modelos) e quer saber a faixa em que a **média de acerto** realmente está.

### Os ingredientes (exemplo do curso)

> [!example] Dados do exemplo
> - **100 modelos** criados (tamanho da amostra, n = 100).
> - **Intervalo de confiança desejado**: 95%.
> - **Valor de Z** (para 95%): **1,96**.
> - **Desvio padrão** dos acertos: 12,61.
> - **Média** dos acertos: 88,2.

### A fórmula (margem de erro)

$$
\text{Margem} = Z \times \frac{\sigma}{\sqrt{n}}
$$

### O cálculo

$$
\text{Margem} = 1{,}96 \times \frac{12{,}61}{\sqrt{100}} = 1{,}96 \times \frac{12{,}61}{10} \approx 2{,}47
$$

### O resultado

O intervalo é a **média ± a margem**:
$$
88{,}2 - 2{,}47 = 85{,}7 \qquad\qquad 88{,}2 + 2{,}47 = 90{,}67
$$

> [!summary] Interpretação
> *"O acerto médio do modelo deve variar entre **85,7% e 90,67%**, com um nível de confiança de **95%**."*
>
> Ou seja: não é "90%" — é uma **faixa**. E o limite inferior (85,7%) pode ser bem diferente do que você prometeu!

> [!warning] Cuidado na geração dos modelos
> Os **dados de treino** dos vários modelos devem ser escolhidos por funções que deem a todas as instâncias **as mesmas chances de serem selecionadas** (amostragem aleatória justa). Senão, a variabilidade medida fica enviesada.

---

## 4.5. Intervalo de Confiança para a Proporção

> [!note] Quando usar
> Quando você roda o modelo **uma única vez** e quer estimar a faixa da **proporção de acertos**.

### Os ingredientes (exemplo do curso)

> [!example] Dados do exemplo
> - **1.000 registros** de teste (n = 1000).
> - **Intervalo de confiança**: 95%.
> - **Valor de Z**: 1,96.
> - **P(a)** = proporção de acertos = 0,9 (90%).
> - **P(e)** = proporção de erros = 0,1 (10%).

### A fórmula (margem de erro)

$$
\text{Margem} = Z \times \sqrt{\frac{\hat{p}\,(1 - \hat{p})}{n}}
$$

### O cálculo

$$
\text{Margem} = 1{,}96 \times \sqrt{\frac{0{,}9 \times (1 - 0{,}9)}{1000}} = 1{,}96 \times \sqrt{\frac{0{,}09}{1000}} \approx 0{,}02
$$

### O resultado

$$
0{,}90 - 0{,}02 = 0{,}88 \qquad\qquad 0{,}90 + 0{,}02 = 0{,}92
$$

> [!summary] Interpretação
> *"A proporção de acertos esperada da aplicação na detecção de fraudes é entre **88% e 92%**, com um nível de confiança de **95%**."*

---

## 4.6. Entendendo os Conceitos Estatísticos

> [!info] O que é "nível de confiança de 95%"?
> Significa: se você repetisse o experimento muitas vezes, em **95% das vezes** o valor real cairia dentro do intervalo calculado. Não é certeza absoluta — é confiança alta.

> [!info] O que é o "valor de Z"?
> É um número da distribuição normal que corresponde ao nível de confiança escolhido:
> - 90% de confiança → Z = 1,645
> - **95% de confiança → Z = 1,96** (o mais usado)
> - 99% de confiança → Z = 2,576
>
> Quanto **maior** o nível de confiança, **maior** o Z, e **mais larga** a faixa.

---

## 4.7. Comparação das Duas Abordagens

| | **Intervalo para a Média** | **Intervalo para a Proporção** |
|---|---|---|
| Quando usar | Rodou o modelo **várias vezes** | Rodou o modelo **uma vez** |
| Precisa de | Média + desvio padrão dos resultados | Proporção de acerto/erro |
| Fórmula da margem | $Z \cdot \dfrac{\sigma}{\sqrt{n}}$ | $Z \cdot \sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$ |

---

## 4.8. Por que Isso Importa na Prática

> [!important] A grande lição
> Apresentar um modelo como "**90% de acerto**" é **arriscado** e até **antiético** num projeto sério. O correto é:
>
> *"O modelo tem acerto **entre 85,7% e 90,67%** com 95% de confiança."*
>
> Isso protege você (não promete o que não pode garantir) e dá ao cliente uma **visão realista** para decidir o investimento.

---

## 4.9. Resumo

> [!summary] O essencial da Variabilidade
> - O acerto de um modelo **não é fixo** — é uma **faixa**, porque vem de amostras.
> - Em vez de um número, reporte um **intervalo de confiança**.
> - **Para a Média** → rodou várias vezes: usa média + desvio padrão.
> - **Para a Proporção** → rodou uma vez: usa a proporção de acertos.
> - **Z = 1,96** para 95% de confiança (o mais comum).
> - Sempre comunique resultados como faixa, não como número absoluto.

---

## 🔗 Próximos passos
- [[05 - Avaliando o Desempenho de Modelos]] — e quando você quer comparar **dois** modelos? Como saber se um é mesmo melhor?

---
[[00 - Índice|⬅️ Voltar ao Índice]]
