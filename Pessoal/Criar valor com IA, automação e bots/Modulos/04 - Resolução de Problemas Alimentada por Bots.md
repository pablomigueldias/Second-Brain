---
tema: "Resolução de Problemas Alimentada por Bots"
curso: "Criar valor com IA, automação e bots"
fonte: "gravacao"
origem: "sistema:alsa_output (gravação de aula)"
data: 2026-06-21
tags: [estudo, chatbots, amazon-lex, automacao, atendimento]
---

# Resolução de Problemas Alimentada por Bots — como criar um chatbot

> Em uma frase: chatbots automatizam conversas que não precisam de um humano — e você vai aprender como eles funcionam e a montar um do zero no Amazon Lex.

## 👋 Vamos começar
Oi, Pablo! Soa estranho dizer "conversa que não precisa de humano", né? Mas pensa: quando você liga para perguntar o horário de funcionamento de um lugar, você não precisa de uma *pessoa* — precisa da *resposta*. Se um computador já tem essa resposta, ele resolve. Neste módulo vou te mostrar **como chatbots funcionam por dentro** (intenções e jornadas), **quando** eles valem a pena e a gente vai **construir um** no Amazon Lex. Vem comigo.

---

## 📖 Entendendo passo a passo

### O que um chatbot resolve (e por quê)
Quando você liga para um atendimento e ouve *"pressione 1 para conta nova, 2 se já tem conta"*, aquilo é um chatbot básico **filtrando a sua intenção** para te mandar ao lugar certo. Sem ele, uma pessoa teria que atender só para descobrir o que você quer e te transferir — mais lento e mais caro.

E para um negócio **pequeno**, de uma pessoa só? Aqui está o pulo do gato: a **mesma lógica das automações** (módulo 2) vale para chatbots. Se você se pega **respondendo a mesma pergunta toda hora**, ou quer **limitar o tempo no telefone**, um chatbot assume essa parte e **libera seu tempo** para o que importa.

> 💡 **Guarde isto:** chatbot é automação aplicada a **conversas**. Vale quando a interação é **repetitiva** e a resposta é **previsível**.

### Como funcionam: intenção + jornada do usuário
O mecanismo central:
1. O bot identifica a **intenção** do usuário a partir do que ele escreve/fala.
2. Encaminha o usuário pela **jornada** (*user journey*) correta — uma sequência de passos.

Exemplo: reservar uma mesa. A jornada linear seria:
- Usuário: *"quero reservar uma mesa"* → intenção **reconhecida**.
- Bot: *"para qual dia?"* → se a resposta não for reconhecida, **pergunta de novo**; se for, **avança**.
- Bot: *"para que horário?"* → e assim por diante, até ter **todas as informações**.

> [!TIP] Na prática
> Uma jornada **linear** (uma pergunta após a outra) é simples. A complexidade aparece quando há **ramificações**: opções que dependem das respostas anteriores ("se for grupo grande, perguntar sobre área reservada").

Os bots **modernos** vão além do menu de múltipla escolha: o usuário descreve em **linguagem natural** o que quer, e o bot entende a intenção — isso é **IA / machine learning** rodando por baixo. Muito melhor do que ficar clicando em listas.

### Quando vale a pena: o eletricista autônomo
Caso do curso: você é **eletricista autônomo**, dia corrido. Cada ligação dura ~10 min; com **6 ligações/dia**, lá se vai **1 hora**. Um chatbot pode:
- **Responder perguntas frequentes** (horário, preço de visita técnica, se atende emergência).
- **Aceitar agendamentos** (pede data, horário, tipo de serviço, contato e confirma).
- **Escalar para humano** quando o assunto for complexo demais ("vou te transferir para o eletricista").
- **Melhorar com o tempo:** conforme você vê que perguntas surgem, refina as respostas.

> 💡 **Guarde isto:** um bom chatbot tem três "modos": **responder FAQ**, **executar tarefas** (agendar) e **escalar** o que não dá conta. Comece simples e evolua.

### Mãos à obra: construindo no Amazon Lex
Vamos construir o chatbot do **restaurante** usando o **[[Amazon Lex]]** — o serviço da AWS que, aliás, **alimenta a Alexa**. Bom para iniciantes e com um **nível gratuito** generoso. (Como sempre: há outras ferramentas ótimas; não fique preso a uma.)

Dois conceitos centrais do Lex:
- **Intent (intenção)** — uma funcionalidade do bot (ex.: "Reservar Mesa").
- **Slot** — cada informação que o bot precisa coletar para cumprir a intenção (data, horário, nº de pessoas…). Cada slot tem um **tipo de dado** (ex.: `AMAZON.Date`).

> [!TIP] Na prática — passo a passo no Lex
> 1. **Criar bot** → "Create a blank bot", preencher nome/descrição.
> 2. Criar uma **função (role)** com permissões básicas do Lex; responder à pergunta sobre **COPPA** (lei de privacidade de crianças) conforme o público; escolher o **idioma**.
> 3. Criar a **intent** "Reservar Mesa" com uma descrição.
> 4. Adicionar **sample utterances** (exemplos de frases): "quero reservar uma mesa", "tem mesa para amanhã?", etc. São exemplos que ensinam o bot a reconhecer a intenção.
> 5. Adicionar **slots**: `data` (tipo `AMAZON.Date`), com um **prompt** ("Para que data você gostaria de visitar?"). Repetir para **horário**, **nº de pessoas**, **alergias**, **nome** e **e-mail/contato**.
> 6. **Confirmação:** definir o prompt de confirmação ("Confirma a reserva desta mesa?") e a resposta de recusa ("Ok, sua solicitação não será enviada").
> 7. **Fulfillment** (atendimento): o que o bot diz se der certo ou errado.
> 8. **Closing response:** "Obrigado por reservar conosco."
> 9. **Build** → **Test**: o bot abre num painel, você diz "quero reservar uma mesa" e ele conduz a coleta dos slots e confirma.

### O elo final: APIs deixam o bot *agir*
"Mas o bot realmente faz a reserva?" Aqui voltam as **[[API]]s** (lembra do garçom, módulo 1). Se o seu restaurante usa um **sistema de reservas com API**, você **conecta o chatbot a esse sistema**: ao terminar a coleta, o bot **cria a reserva de verdade** no calendário do restaurante — processo automatizado **de ponta a ponta**.

> 💡 **Guarde isto:** sem API, o bot apenas **informa**. Com API, o bot **executa tarefas** — esse é o salto de qualidade. Vale para o Lex e para a maioria das ferramentas de chatbot.

Para o restaurante, o resultado é claro: menos tempo da equipe ao telefone, atendendo só os casos **incomuns**, enquanto o bot cuida do **comum**.

---

## 🧠 Por que isso importa pra você
Chatbot fecha o trio do curso: **automação** + **IA** + **conversa automatizada**. Entender **intenção → jornada → slots** te dá um molde mental que serve para qualquer ferramenta (Lex, Dialogflow, etc.). E perceber que **APIs transformam um bot que fala num bot que faz** é o que separa uma demo bonitinha de uma solução que realmente economiza horas de trabalho.

## 📌 Resumo pra fixar
- Chatbot = automação de **conversas repetitivas e previsíveis**.
- Funciona por **intenção** (o que o usuário quer) + **jornada do usuário** (a sequência de passos).
- Bots modernos entendem **linguagem natural** (IA/ML por baixo), não só menus.
- Um bom bot **responde FAQ**, **executa tarefas** e **escala** o que não resolve.
- No **Amazon Lex**: **intents** (funcionalidades) e **slots** (dados a coletar, cada um com seu tipo).
- Fluxo: utterances → slots → confirmação → fulfillment → closing → build → test.
- **APIs** elevam o bot de "informar" para "executar" (fazer a reserva de verdade).

## 🗝️ Palavras novas (do jeito simples)
- **[[Chatbot]]** — software que automatiza conversas com usuários.
- **[[Amazon Lex]]** — serviço da AWS para criar chatbots; é o que move a Alexa.
- **Intent (intenção)** — uma funcionalidade do bot, ligada ao que o usuário quer fazer.
- **Slot** — um dado que o bot precisa coletar (data, horário, nome), com um tipo definido.
- **Utterance** — exemplo de frase que o usuário diria; ensina o bot a reconhecer a intenção.
- **Jornada do usuário** — a sequência de passos que o bot conduz até concluir a tarefa.
- **Fulfillment** — a etapa em que o bot "cumpre" a tarefa (e o que ele responde ao dar certo/errado).
- **[[API]]** — permite o bot **agir** (ex.: gravar a reserva num sistema externo).

## ✅ Teste-se (pra enraizar)
1. **P:** Que tipo de conversa um chatbot resolve bem? → **R:** As **repetitivas e previsíveis**, em que a resposta não exige um humano.
2. **P:** Quais os dois conceitos centrais do funcionamento de um bot? → **R:** **Intenção** (o que o usuário quer) e **jornada do usuário** (a sequência de passos).
3. **P:** O que diferencia um bot moderno de um menu "digite 1, digite 2"? → **R:** Ele entende **linguagem natural** via IA/ML, em vez de só oferecer opções fixas.
4. **P:** No Amazon Lex, o que é uma **intent** e o que é um **slot**? → **R:** Intent é uma funcionalidade (ex.: Reservar Mesa); slot é cada dado a coletar (data, horário…).
5. **P:** Para que servem as **utterances**? → **R:** São frases de exemplo que ensinam o bot a reconhecer aquela intenção.
6. **P:** Quais os três "modos" de um bom chatbot? → **R:** Responder FAQ, executar tarefas (agendar) e escalar para humano quando preciso.
7. **P:** O que muda quando você conecta o bot a uma **API**? → **R:** Ele deixa de só informar e passa a **executar tarefas de verdade** (criar a reserva, por exemplo).
8. **P:** No caso do eletricista, quanto tempo o bot pode poupar? → **R:** Cerca de 1 hora/dia (6 ligações de ~10 min) que iriam para o telefone.

## 🔗 Para continuar
- [[03 - Desbloquear Soluções com IA Generativa]]
- [[05 - Teste as Suas Soluções de IA]]
- [[_Índice Criar valor com IA, automação e bots]]
