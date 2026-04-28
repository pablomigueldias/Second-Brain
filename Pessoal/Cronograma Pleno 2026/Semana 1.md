# 🚀 CRONOGRAMA: Aprender + Dominar IA Como Ferramenta

**Versão:** Intermediário com Muita Teoria → Pleno Full Stack com Prática  
**Premissa:** Você vai aprender ENTENDENDO, depois usar IA pra acelerar  
**Tempo:** Abril - Dezembro 2026 (8 meses)  
**Dedicação:** 3-4h focadas/dia

---

## 🤖 FILOSOFIA: Como Usar IA Corretamente

### A Regra de Ouro: 70-30

```
Seu trabalho:    70%
IA ajuda:        30%

✅ Você escreve o código base
✅ Você entende cada linha
✅ Quando trava, IA ajuda
✅ Você valida/refatora
✅ Você explica o resultado
```

### Quando Pedir IA:

|Situação|❌ ERRADO|✅ CERTO|
|---|---|---|
|Trava em lógica|"Cria do zero"|"Estou tentando X, trava em Y, por quê?"|
|Type hints|"Me gera tudo"|"Me mostra exemplo de 3 type hints para listas"|
|Refatoração|"Refatora meu código"|"Esse código está ruim? Como melhorar?"|
|Testes|"Cria testes pra mim"|"Como testar isso? Qual abordagem?"|
|Debugging|"Arruma meu bug"|"Por que isso não funciona? O erro é..."|

---

## 📅 ABRIL 2026 - Semana 1: Fundação

## Segunda 27/04

### Bloco 1: Honestidade + Diagnóstico (14h-16h)

**TAREFA 1: Responda novamente (sem colar do arquivo anterior):**

Abra terminal e crie arquivo `~/estudo/semana1/respostas-honestas.txt`:

Escreva AGORA (sem pesquisar):

```
PERGUNTA 1: Context vs Zustand - qual usar em cada caso?

Minha resposta honesta (pode estar errada):
[escreva aqui o que você REALMENTE acha]

PERGUNTA 2: Se você fosse estruturar um projeto React GRANDE (tipo Trello), como faria?

Minha resposta honesta:
[escreva]

PERGUNTA 3: O que é "prop drilling"? Por que é problema?

Minha resposta honesta:
[escreva]

PERGUNTA 4: Como você otimizaria uma lista com 10k items em React?

Minha resposta honesta:
[escreva]

PERGUNTA 5: SSR vs SSG - qual diferença?

Minha resposta honesta:
[escreva]
```

**DEPOIS** que você escreveu, use IA:

```
Prompt para IA:

Eu respondi essas perguntas sobre React. Revise minha compreensão
e aponte onde estou errado. Não dê a resposta correta ainda,
apenas diga "você está no caminho" ou "aqui você está errado".

[Cole suas respostas]
```

**Meta:** IA aponta gaps, você descobre o que não sabe

---

### Bloco 2: Entender React Render (18h-19:30)

**TAREFA 1: Faça um projeto PEQUENO**

```bash
mkdir -p ~/estudo/semana1/render-test
cd ~/estudo/semana1/render-test
npm create vite@latest . -- --template react
npm install
```

**TAREFA 2: Crie arquivo `/src/RenderTest.jsx`:**

```jsx
import { useState } from 'react';

export function RenderTest() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  console.log('RENDER: Parent renderizou!');
  
  return (
    <div style={{ padding: '20px', border: '2px solid blue' }}>
      <h2>Parent</h2>
      <p>Count: {count}</p>
      <p>Name: {name}</p>
      <input 
        value={name} 
        onChange={(e) => setName(e.target.value)}
        placeholder="Digite seu nome"
      />
      <button onClick={() => setCount(count + 1)}>
        Count: {count}
      </button>
      
      <Child key={count} count={count} />
    </div>
  );
}

function Child({ count }) {
  console.log('RENDER: Child renderizou!');
  
  return (
    <div style={{ padding: '10px', border: '2px solid red', marginTop: '10px' }}>
      <h3>Child</h3>
      <p>Count recebido: {count}</p>
    </div>
  );
}
```

**TAREFA 3: Teste e entenda:**

```bash
npm run dev
# Abra http://localhost:5173
# Abra DevTools (F12) → Console
```

**Agora OBSERVE:**

1. Digite no input "Pablo"
    
    - Quantas vezes "RENDER: Parent renderizou!" aparece?
    - Quantas vezes "RENDER: Child renderizou!" aparece?
2. Clique no botão Count
    
    - Qual diferença?

**TAREFA 4: Responda por escrito**

Arquivo: `~/estudo/semana1/entendimento-render.md`

```markdown
# Meu Entendimento de React Render

## Teste 1: Digitar no Input
- Parent renderizou X vezes porque:
  [sua explicação]

- Child renderizou X vezes porque:
  [sua explicação]

## Teste 2: Clicar no Botão
- Qual a diferença e por quê?
  [sua explicação]

## Minha Conclusão:
React renderiza quando:
[sua explicação em palavras suas]
```

**TAREFA 5: Use IA para validar**

```
Prompt:

Fiz um teste em React e observei esse comportamento:
[descreva o que viu]

Meu entendimento é:
[escreva seu entendimento]

Estou certo? Se errado, qual é a verdade?
NÃO QUERO que você corrija meu código.
SÓ QUERO que você valide meu entendimento.
```

**Meta:** Você entendeu ANTES de IA validar

---

## Terça 28/04

### Bloco 1: React Props Profundo (14h-16h)

**TAREFA 1: Escreva código SEM COPIAR**

Você tem 30 minutos para fazer isto do zero:

Crie `/src/PropTest.jsx`:

Requisitos:

- [ ] Um componente pai que tem um state `users` (array de objetos)
- [ ] Um componente filho que recebe `users` como prop
- [ ] Um botão que adiciona novo user
- [ ] Filho renderiza lista de users

**Sem copiar código anterior.** **Sem pedir IA pra gerar.** **Você faz do zero.**

Se travar:

```
Prompt para IA (NOT para gerar código):

Estou tentando fazer um componente que:
[descreva o que quer]

Estou travado em:
[descreva onde trava]

Como posso resolver? Não quero código, quero dica.
```

**DEPOIS que fez:**

Commit:

```bash
git add .
git commit -m "feat: aprender props - versão 1 feita do zero"
```

---

### Bloco 2: Python Type Hints (18h-19:30)

**TAREFA 1: Encontre 3 funções suas antigas**

Pegue código que você escreveu antes:

```python
# Seu código antigo (provavelmente sem type hints)
def processar_dados(dados):
    resultado = []
    for item in dados:
        resultado.append(item * 2)
    return resultado
```

**TAREFA 2: Melhore VOCÊ MESMO**

Tente adicionar type hints:

```python
# Sua melhoria (sem IA)
def processar_dados(dados):  # Meu tipo aqui
    resultado = []
    for item in dados:
        resultado.append(item * 2)
    return resultado
```

Se não tem certeza:

```
Prompt para IA:

Estou tentando adicionar type hints. Minha função é:
[sua função]

Os tipos que achei apropriados são:
[escreva o que você acha]

Estou certo? Se não, qual seria a abordagem?
```

**Meta:** Você pensa ANTES de IA validar

---

## Quarta 29/04

### Bloco 1: React + Python Integrados (14h-16h)

**TAREFA 1: Crie uma API FastAPI muito simples**

Pasta: `~/estudo/semana1/simple-api/`

```bash
mkdir -p ~/estudo/semana1/simple-api
cd ~/estudo/semana1/simple-api
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install fastapi uvicorn
```

Crie `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

# Sua tarefa: crie 3 endpoints
# GET /tarefas - retorna lista de tarefas
# POST /tarefas - cria nova tarefa
# DELETE /tarefas/{id} - deleta tarefa

# Dica: dados ficam em lista python mesmo (sem banco por enquanto)

tarefas = [
    {"id": 1, "titulo": "Estudar React"},
    {"id": 2, "titulo": "Estudar Python"},
]

# VOCÊ ESCREVE OS ENDPOINTS ABAIXO
# Tente do zero
```

Se travar:

```
Prompt:

Estou fazendo endpoints REST. Tenho isto:
[seu código]

Preciso fazer:
- GET /tarefas (retornar lista)
- POST /tarefas (adicionar)
- DELETE /tarefas/{id} (deletar)

Estou travado em: [aonde?]

Como resolver? Não quero código pronto, quero entender a abordagem.
```

---

**TAREFA 2: Conecte seu React na API**

React Component que faz fetch:

```jsx
// Você escreve isto do zero
import { useState, useEffect } from 'react';

export function TarefasList() {
  const [tarefas, setTarefas] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    // Você escreve: fetch de http://localhost:8000/tarefas
    // Atualiza state
    // Trata erro
  }, []);
  
  // Você renderiza lista
  return (
    // seu JSX
  );
}
```

**Meta:** React + Python conectados, feito POR VOCÊ

---

## Quinta 30/04

### Bloco 1: Teste Sua Compreensão (14h-16h)

**TAREFA 1: Refatore seu PropTest.jsx**

Pegue o código que fez na terça. Agora MELHORE:

Requisitos de refatoração:

- [ ] Extrair componente Child
- [ ] Passar dados via props corretamente
- [ ] Adicionar prop validation (proptypes ou TypeScript JSDoc)
- [ ] Adicione um estilo Tailwind simples

Não é "fazer novo". É **pegar o que tem e melhorar.**

Se tiver dúvida em refatoração:

```
Prompt:

Meu código está assim:
[seu código]

Quero refatorar porque:
[sua razão]

Qual é a melhor abordagem? Não me reescreva, só guie.
```

---

### Bloco 2: Entender Erros Python (18h-19:30)

**TAREFA 1: Quebra propositalmente seus endpoints**

Seu `main.py` da API:

```python
# Seu código atual (do quarta)
# AGORA faça propositalmente dar ERRO
# Exemplo: tente acessar campo que não existe
# Tente fazer operação inválida
```

**TAREFA 2: Entenda o erro**

Quando erro aparecer, NÃO corrija logo. Leia:

```
O que diz o erro?
Qual linha?
Por quê deu erro?
Qual foi minha intenção?
Como deveria ser?
```

**TAREFA 3: Corrija**

Agora sim, conserte. Teste novamente.

**Se não entender:**

```
Prompt:

Meu código:
[seu código]

Erro:
[mensagem de erro]

Entendo que o erro significa:
[sua interpretação]

Estou certo?
```

**Meta:** Você entende erros, não só "arruma"

---

## Sexta 1/05 - Python Intensive

### Bloco A (14h-15:30): Type Hints Profundo

Pegue funções suas. Adicione CORRETOS type hints.

Se dúvida:

```
Prompt:

Minha função:
[seu código]

Meus type hints:
[o que você colocou]

Isso está correto para este caso de uso?
Se não, qual seria?
```

---

### Bloco B (16h-17:30): Testes em Python

**TAREFA 1: Teste seus endpoints**

```python
# Teste 1: GET /tarefas retorna lista
# Teste 2: POST /tarefas cria
# Teste 3: DELETE /tarefas/{id} deleta

# Você escreve testes para cada um
# Use pytest
```

Se não sabe testar:

```
Prompt:

Quero testar meus endpoints FastAPI.
Minha função GET é:
[seu código]

Como faço teste para isto?
Qual é a estrutura?
```

IA ensina, você implementa.

---

## Sábado 2/05 - Integração Total

**TAREFA: Seu React faz CRUD na sua API**

Requisitos:

- [ ] GET /tarefas e mostra na tela
- [ ] POST /tarefas cria nova
- [ ] DELETE /tarefas/{id} deleta
- [ ] Tudo funciona

Tudo feito POR VOCÊ. IA só valida/ajuda quando trava.

---

## Domingo 3/05 - Review

**TAREFA 1: Documenta o que aprendeu**

Arquivo: `~/estudo/semana1/resumo.md`

```markdown
# Resumo Semana 1

## O Que Aprendi:

### React
- Renderização: Quando re-render?
  [sua explicação em 3 frases]
- Props: Como passar dados?
  [sua explicação]
- State: Como funciona?
  [sua explicação]

### Python
- Type Hints: Quando usar?
  [sua explicação]
- FastAPI: Como fazer endpoint?
  [sua explicação]
- Testes: Como testar função?
  [sua explicação]

### Integração
- Como React e Python se conectam?
  [sua explicação]

## Minha Maior Dificuldade:
[Aonde você mais travou?]

## Como Resolvi:
[Como conseguiu resolver?]

## Próxima Semana:
[O que quer melhorar?]
```

**TAREFA 2: GitHub**

```bash
cd ~/estudo/semana1
git init
git add .
git commit -m "chore: semana 1 - fundações React + Python"
git remote add origin https://github.com/seu-user/estudo-2026
git push -u origin main
```

---

## 📊 Resumo Semana 1

**Você fez:**

- ✅ Diagnosticou seus gaps
- ✅ Entendeu render cycle
- ✅ Aprendeu props
- ✅ Type hints
- ✅ React + Python conectados
- ✅ Testes básicos

**Você NÃO fez:**

- ❌ Copiar código
- ❌ Deixar IA fazer
- ❌ Avançar sem entender

**Você sabe agora:**

- ✅ O que é render
- ✅ Como props funcionam
- ✅ Como conectar React + Python
- ✅ Type hints corretos

**Se alguém perguntar na entrevista "Por que seu componente renderiza 3 vezes?" você RESPONDE.**

---

# 📅 MAIO 2026 - Projeto 1: Landing Page RIG

## Estrutura Geral

Você vai fazer do zero. SEM COPIAR.

### Semana 1 (4-10 Maio)

**Dia 1: Planejamento**

- Você esboça a estrutura
- Você desenha no papel
- Você lista componentes necessários

**Dia 2-3: Componentes base**

- Você escreve Button.jsx DO ZERO
- Você escreve Card.jsx DO ZERO
- IA valida

**Dia 4-5: Seções**

- Você escreve Hero DO ZERO
- Você escreve Features DO ZERO
- Progressivamente mais seções

**Dia 6-7: Polish**

- Tailwind
- Responsividade
- Testes

### Processo para cada componente:

```
1. Você escreve 70% do código
2. Testa no browser
3. Se der erro: DEBUG você mesmo
4. Se não conseguir: IA ajuda a debugar (NÃO reescreve)
5. Você entende o erro
6. Você corrige
7. Commit
```

---

# 🎯 RESUMINDO: Como Você Vai Usar IA

### ✅ PARA ISTO: (Use IA)

- "Por que meu código não funciona?" (IA ajuda debugar)
- "Qual é a melhor prática aqui?" (IA explica)
- "Como testar isto?" (IA mostra abordagem)
- "Que biblioteca usar?" (IA recomenda)
- "Como funciona isto?" (IA explica)

### ❌ NÃO PARA ISTO: (Não use IA)

- "Me cria um componente" (NÃO)
- "Refatora meu código" (NÃO)
- "Me gera testes" (NÃO)
- "Cria um endpoint" (NÃO)

---

# 📋 COMO COMEÇAR SEGUNDA 27/04

## 14h-16h: Bloco 1

```bash
# Crie pasta de estudos
mkdir -p ~/estudo/semana1
cd ~/estudo/semana1

# Crie arquivo de respostas
touch respostas-honestas.txt

# Abra e responda as 5 questões (SEM IA, SEM PESQUISAR)
```

Depois:

```
Use IA para validar respostas
```

---

## 18h-19:30: Bloco 2

```bash
mkdir -p render-test
cd render-test
npm create vite@latest . -- --template react
npm install

# Crie o arquivo RenderTest.jsx
# Faça os testes
# Documente o aprendizado
```

---

# 🚀 REGRA MAIS IMPORTANTE

```
SE VOCÊ CONSEGUE EXPLICAR EM 3 FRASES = APRENDEU
SE NÃO CONSEGUE = PRECISA ENTENDER MAIS
```

Isso é verdade pra tudo. Sempre teste a si mesmo.

---

**Pronto para começar? Você tem um cronograma real, prático, e que te torna COMPETENTE.** 🚀

**Próximo passo: Segunda 14h, Bloco 1. Responder as questões honestamente.**

**Te vejo lá!**