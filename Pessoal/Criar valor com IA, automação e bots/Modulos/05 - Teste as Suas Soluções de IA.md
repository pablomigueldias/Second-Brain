---
tema: "Teste as Suas Soluções de IA"
curso: "Criar valor com IA, automação e bots"
fonte: "gravacao"
origem: "sistema:alsa_output (gravação de aula)"
data: 2026-06-21
tags: [estudo, testes, ia, qualidade, alucinacoes]
---

# Teste as Suas Soluções de IA — por que (e como) testar antes de publicar

> Em uma frase: construir é só metade do trabalho; sem **testar**, sua solução de IA pode dar respostas erradas com cara de certas — e isso custa caro.

## 👋 Vamos começar
Oi, Pablo! Deixa eu te contar uma história real: em 2024 o Google lançou os "AI Overviews" no topo da busca. Boa ideia — mas o recurso às vezes inventava coisas, tipo recomendar que a pessoa **comesse uma pedrinha por dia** para ficar saudável. Engraçado quando é óbvio. Mas e quando o erro **não** é óbvio? Imagine alguém com alergia perguntando *"esta receita leva nozes?"* e recebendo um "não" errado. Por isso este módulo é sobre **testar**. Vem comigo.

---

## 📖 Entendendo passo a passo

### Alucinações: o erro com cara de verdade
Quando um modelo de IA retorna algo **falso como se fosse verdadeiro**, chamamos isso de **[[Alucinação (IA)]]**. É um problema sério porque a IA é **vendida como confiável** — então as pessoas tendem a **acreditar** na resposta.

> 💡 **Guarde isto:** o perigo da alucinação não é a IA errar, é ela errar **com confiança**, num contexto em que o usuário foi levado a confiar. É isso que trava empresas de adotarem IA sem cuidado.

Pode-se dizer "ah, a pessoa deveria checar por conta". Mas a realidade é que esses recursos são **projetados e vendidos para serem confiáveis** — logo, as pessoas vão tomar como verdade. A responsabilidade de testar é **sua**, de quem constrói.

### Quanto mais variáveis, mais teste
A quantidade de teste necessária cresce com a **complexidade** da solução.

Exemplo simples: um site que coleta e-mails para uma newsletter. Você precisa testar basicamente duas coisas:
1. O campo aceita **apenas e-mails válidos**.
2. O e-mail realmente **vai parar na lista**.

Testou isso, pode publicar. Mas conforme você adiciona variáveis, **mais coisas podem dar errado** — e mais tempo de teste é necessário.

> [!TIP] Na prática
> Teste também a **dependência de terceiros**: se a sua automação usa um serviço externo e ele muda, a sua solução **não pode quebrar**. Pense no que acontece se a API de fora se comportar diferente.

Sim, testar é chato. Mas é **muito menos chato** do que descobrir o erro depois, em produção, e ter que voltar para juntar os cacos — ainda mais se a solução é **pública** e o erro arranha a sua **reputação**.

### Como testar um **modelo de IA**
Volte ao modelo que reconhece dígitos (módulo 1). O dataset dos 50 mil exemplos de treino vinha com **mais 10 mil imagens separadas para teste**. Como **já sabemos** qual número está em cada uma, podemos perguntar ao modelo e **conferir se ele acerta**.

> 💡 **Guarde isto:** a regra de ouro de testar IA é **separar dados de teste** dos dados de treino e usá-los como um gabarito. É "fazer uma pergunta cuja resposta você já sabe, só para ver se o modelo está mentindo".

Mesmo assim — como o caso do Google mostra — **alguns erros escapam**. Teste reduz risco, não o zera.

### Como testar **automações e chatbots**
Em programação existe o **[[Teste de Unidade]]** (*unit test*): código que testa automaticamente cada parte contra uma lista de requisitos. Ótimo — mas em ferramentas **no-code/low-code** isso nem sempre está disponível.

Nesse caso, o conselho do curso é **manual e direto**:
1. Faça uma **lista de requisitos** da sua solução (o que ela *deve* fazer).
2. **Use a solução como se você fosse o cliente** — e tente **"furar"** (achar o jeito de quebrar).

> [!TIP] Na prática
> A aula recomenda o livro **[[The Mom Test]]** — sobre conversar com usuários e construir produtos melhores. Vale para entender de verdade o que sua solução precisa entregar.

E uma palavra de leveza: **erros acontecem**. Se algo passou, você **não falhou** — conserte rápido e siga em frente.

### O processo de 5 passos para corrigir um problema
Quando um teste revela que algo não funciona:

1. **Identificar o impacto** do problema (faça isso **primeiro** — ajuda a achar a raiz mais rápido).
2. **Identificar a causa-raiz.**
3. **Resolver** o problema.
4. **Testar de novo**, várias vezes, com exemplos diferentes.
5. **Documentar a correção** — registre qual era o problema e como você resolveu.

> 💡 **Guarde isto:** **documentar a correção** é o passo que as pessoas pulam — e é o que te salva quando o mesmo problema voltar daqui a três meses. Escreva o que era e como consertou.

---

## 🧠 Por que isso importa pra você
Você vai construir automações e bots que **outras pessoas** vão usar. Testar é o que separa um protótipo divertido de uma solução **confiável**. E entender **alucinações** te deixa cético na medida certa: você passa a usar IA sabendo que ela pode errar com confiança, e a **desenhar verificações** em vez de confiar cegamente. O processo de 5 passos, por fim, é um hábito que serve para depurar qualquer coisa — não só IA.

## 📌 Resumo pra fixar
- **Alucinação** = IA retorna algo falso como se fosse verdade; perigoso porque parece confiável.
- A quantidade de teste cresce com o **número de variáveis** da solução.
- Teste também o que depende de **terceiros** (se o serviço externo muda, não pode quebrar).
- Testar **modelo de IA**: use um **conjunto de teste separado** (gabarito conhecido).
- Testar **automação/chatbot**: faça uma **lista de requisitos** e **use como cliente**, tentando furar.
- **Unit tests** automatizam isso em código, mas nem sempre cabem em no-code.
- Bug encontrado → siga os **5 passos**: impacto → causa-raiz → resolver → re-testar → **documentar**.

## 🗝️ Palavras novas (do jeito simples)
- **[[Alucinação (IA)]]** — quando o modelo gera informação falsa com aparência de verdadeira.
- **Falso positivo** — uma resposta apresentada como correta que, na verdade, está errada.
- **Conjunto de teste** — dados separados, com resposta conhecida, usados para avaliar o modelo.
- **[[Teste de Unidade]]** — código que testa automaticamente partes de uma solução contra requisitos.
- **Causa-raiz** — a origem real de um problema (não só o sintoma).
- **[[The Mom Test]]** — livro sobre conversar com usuários e construir produtos melhores.

## ✅ Teste-se (pra enraizar)
1. **P:** O que é uma alucinação de IA? → **R:** Quando o modelo retorna algo falso como se fosse verdadeiro.
2. **P:** Por que alucinações são tão perigosas? → **R:** Porque a IA é vendida como confiável, então as pessoas acreditam na resposta errada.
3. **P:** Do que depende a quantidade de teste necessária? → **R:** Da **complexidade**/número de variáveis da solução — mais variáveis, mais teste.
4. **P:** Como se testa um modelo de IA de classificação? → **R:** Usando um conjunto de **teste separado**, com respostas conhecidas, e conferindo os acertos.
5. **P:** Como testar uma automação no-code, se não dá para usar unit test? → **R:** Listando os requisitos e usando a solução como cliente, tentando quebrá-la.
6. **P:** Qual o primeiro passo ao encontrar um bug, e por quê? → **R:** Identificar o **impacto** — ajuda a chegar à causa-raiz mais rápido.
7. **P:** Qual passo do processo as pessoas mais pulam? → **R:** **Documentar a correção** — registrar o problema e a solução para não sofrer de novo.
8. **P:** Por que testar a dependência de terceiros? → **R:** Porque se o serviço externo mudar, sua solução não pode falhar junto.

## 🔗 Para continuar
- [[04 - Resolução de Problemas Alimentada por Bots]]
- [[06 - Guardar Dados na Era da IA]]
- [[_Índice Criar valor com IA, automação e bots]]
