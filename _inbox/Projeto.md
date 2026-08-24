# Projeto Faculdade — Sistema de Barbearia

### 4 entregas em fatias verticais · agosto a novembro/2026

|Entrega|Funcionalidade|Janela|
|---|---|---|
|**E1**|Cadastro de Clientes|25/08 → 14/09|
|**E2**|Cadastro de Barbeiro|15/09 → 05/10|
|**E3**|Agendamento de Corte e Opção de Serviço|06/10 → 26/10|
|**E4**|Histórico de Atendimento e Serviço Prestado|27/10 → 16/11|
|—|Buffer, ajustes e apresentação|17/11 → 30/11|

---

## 1. Regra de ouro

Cada entrega é uma **fatia vertical**: banco + backend + frontend da mesma funcionalidade, funcionando ponta a ponta. Se não dá para abrir no navegador e usar, não está entregue.

**Definition of Done (vale para todas as entregas):**

- [ ] Migration aplicada e versionada no repositório
- [ ] Endpoints testados no Swagger
- [ ] Tela consumindo a API real, sem mock
- [ ] Erros tratados no front (validação, 401, 403, 409, 500)
- [ ] README atualizado
- [ ] `docker compose up` funcionando em pasta limpa

---

## 2. Stack

|Camada|Tecnologia|
|---|---|
|Banco|PostgreSQL 16|
|Backend|FastAPI + SQLAlchemy + Alembic|
|Frontend|Next.js (App Router) + Tailwind + shadcn/ui|
|Auth|JWT com papéis (CLIENTE / BARBEIRO / ADMIN)|
|Infra|Docker Compose|

Timezone `America/Sao_Paulo` padronizado em banco, API e front desde a E1.

---

## 3. Evolução do schema

Cada entrega adiciona uma migration nova. Nunca reescreva as anteriores.

### E1 — Cadastro de Clientes

```sql
cliente
  id            UUID PK
  nome          VARCHAR(120) NOT NULL
  email         VARCHAR(160) UNIQUE NOT NULL
  telefone      VARCHAR(20)
  data_nascimento DATE
  senha_hash    TEXT NOT NULL
  ativo         BOOLEAN DEFAULT TRUE
  criado_em     TIMESTAMPTZ DEFAULT NOW()
  atualizado_em TIMESTAMPTZ
```

### E2 — Cadastro de Barbeiro

```sql
barbeiro
  id          UUID PK
  nome        VARCHAR(120) NOT NULL
  email       VARCHAR(160) UNIQUE NOT NULL
  telefone    VARCHAR(20)
  cpf         VARCHAR(14) UNIQUE
  bio         TEXT
  foto_url    TEXT
  senha_hash  TEXT NOT NULL
  ativo       BOOLEAN DEFAULT TRUE
  criado_em   TIMESTAMPTZ DEFAULT NOW()

horario_trabalho                    -- expediente semanal padrão
  id, barbeiro_id FK,
  dia_semana  SMALLINT CHECK (dia_semana BETWEEN 0 AND 6),
  hora_inicio TIME, hora_fim TIME
  CHECK (hora_fim > hora_inicio)
  UNIQUE (barbeiro_id, dia_semana, hora_inicio)
```

### E3 — Agendamento e Serviços

```sql
servico
  id, nome VARCHAR(120), descricao TEXT,
  duracao_min INT NOT NULL, preco NUMERIC(10,2) NOT NULL, ativo BOOLEAN

barbeiro_servico                    -- N:N
  barbeiro_id FK, servico_id FK, PK (barbeiro_id, servico_id)

bloqueio_agenda                     -- almoço, folga, feriado
  id, barbeiro_id FK, inicio TIMESTAMPTZ, fim TIMESTAMPTZ, motivo VARCHAR(120)

agendamento
  id, cliente_id FK, barbeiro_id FK, servico_id FK,
  inicio TIMESTAMPTZ NOT NULL,
  fim    TIMESTAMPTZ NOT NULL,
  preco_cobrado NUMERIC(10,2),      -- congela o preço do momento do agendamento
  status VARCHAR(20) DEFAULT 'AGENDADO',
  observacao TEXT, criado_em TIMESTAMPTZ DEFAULT NOW()

-- trava anti-conflito no próprio banco
CREATE EXTENSION IF NOT EXISTS btree_gist;
ALTER TABLE agendamento ADD CONSTRAINT sem_conflito_barbeiro
  EXCLUDE USING gist (
    barbeiro_id WITH =,
    tstzrange(inicio, fim) WITH &&
  ) WHERE (status = 'AGENDADO');
```

### E4 — Histórico de Atendimento

```sql
atendimento                         -- registro do que de fato aconteceu
  id, agendamento_id FK UNIQUE,
  iniciado_em TIMESTAMPTZ, finalizado_em TIMESTAMPTZ,
  valor_final NUMERIC(10,2),
  forma_pagamento VARCHAR(20),      -- DINHEIRO | PIX | CARTAO
  observacao_barbeiro TEXT,
  criado_em TIMESTAMPTZ DEFAULT NOW()

atendimento_servico                 -- serviços extras feitos na cadeira
  id, atendimento_id FK, servico_id FK,
  quantidade INT DEFAULT 1, preco_unitario NUMERIC(10,2)

avaliacao                           -- opcional, se sobrar tempo
  id, atendimento_id FK UNIQUE, nota SMALLINT CHECK (nota BETWEEN 1 AND 5),
  comentario TEXT, criado_em

-- status finais do agendamento passam a ser: CONCLUIDO | CANCELADO | NAO_COMPARECEU

CREATE INDEX idx_agend_cliente_inicio  ON agendamento (cliente_id, inicio DESC);
CREATE INDEX idx_agend_barbeiro_inicio ON agendamento (barbeiro_id, inicio);
CREATE INDEX idx_atend_finalizado      ON atendimento (finalizado_em DESC);
```

---

# ENTREGA 1 — Cadastro de Clientes

**25/08 → 14/09** · _O cliente cria conta, faz login e gerencia o próprio cadastro._

### Banco de dados

|ID|Card|
|---|---|
|E1-BD-01|Subir Postgres no `docker-compose.yml` com volume persistente|
|E1-BD-02|Configurar Alembic e gerar migration inicial|
|E1-BD-03|Criar tabela `cliente` com UNIQUE em email|
|E1-BD-04|Script de seed com 3 clientes de teste|

### Backend

|ID|Card|
|---|---|
|E1-BE-01|Esqueleto FastAPI: estrutura de pastas, settings via `.env`, `/health`|
|E1-BE-02|Model SQLAlchemy + schemas Pydantic (create, update, response sem senha)|
|E1-BE-03|Hash de senha com Argon2id|
|E1-BE-04|`POST /clientes` — cadastro com validação de email duplicado|
|E1-BE-05|`POST /auth/login` — emissão de JWT|
|E1-BE-06|Dependency `get_current_user` protegendo rotas|
|E1-BE-07|`GET /clientes/me` e `PATCH /clientes/me`|
|E1-BE-08|`GET /clientes` — listagem paginada e busca por nome/email|
|E1-BE-09|`DELETE /clientes/{id}` — desativação lógica (`ativo = false`)|
|E1-BE-10|Handler global de erros em formato padronizado|
|E1-BE-11|Testes pytest: cadastro, login, email duplicado, token inválido|

### Frontend

|ID|Card|
|---|---|
|E1-FE-01|Projeto Next.js + Tailwind + layout base (header, container, tema)|
|E1-FE-02|Client HTTP central com injeção de token e tratamento de 401|
|E1-FE-03|Tela de cadastro com validação (React Hook Form + Zod)|
|E1-FE-04|Tela de login e persistência de sessão|
|E1-FE-05|Guard de rota protegida com redirect|
|E1-FE-06|Tela "Meu perfil" com edição de dados|
|E1-FE-07|Listagem de clientes com busca e paginação|
|E1-FE-08|Feedback visual: loading, toast de sucesso, erro vindo da API|

### Critérios de aceite

- Email duplicado retorna 409 e o front exibe a mensagem correta
- Senha nunca aparece em nenhuma resposta da API
- Token expirado derruba o usuário para a tela de login
- Refresh da página mantém a sessão ativa

---

# ENTREGA 2 — Cadastro de Barbeiro

**15/09 → 05/10** · _A barbearia cadastra profissionais e define o expediente de cada um._

### Banco de dados

|ID|Card|
|---|---|
|E2-BD-01|Migration: tabela `barbeiro`|
|E2-BD-02|Migration: tabela `horario_trabalho` com CHECKs|
|E2-BD-03|Adicionar coluna de papel na autenticação (CLIENTE / BARBEIRO / ADMIN)|
|E2-BD-04|Seed: 3 barbeiros com expediente seg–sáb|

### Backend

|ID|Card|
|---|---|
|E2-BE-01|Model + schemas de `Barbeiro`|
|E2-BE-02|`POST /barbeiros` — cadastro com validação de CPF e email únicos|
|E2-BE-03|`GET /barbeiros` (público) e `GET /barbeiros/{id}`|
|E2-BE-04|`PATCH /barbeiros/{id}` e desativação lógica|
|E2-BE-05|Login de barbeiro reaproveitando o fluxo de auth da E1|
|E2-BE-06|Dependency `require_role` para proteger rotas administrativas|
|E2-BE-07|`PUT /barbeiros/{id}/horarios` — definir expediente semanal em lote|
|E2-BE-08|`GET /barbeiros/{id}/horarios`|
|E2-BE-09|Upload de foto (ou campo de URL, se o tempo apertar)|
|E2-BE-10|Testes: papéis, CPF duplicado, horário com fim antes do início|

### Frontend

|ID|Card|
|---|---|
|E2-FE-01|Layout do painel administrativo com menu lateral|
|E2-FE-02|Login de barbeiro e redirecionamento por papel|
|E2-FE-03|Listagem de barbeiros com filtro por ativo/inativo|
|E2-FE-04|Formulário de cadastro/edição de barbeiro com máscaras (CPF, telefone)|
|E2-FE-05|Grade de expediente semanal (7 dias, com intervalos)|
|E2-FE-06|Página pública "Nossa equipe" com foto e bio|
|E2-FE-07|Bloqueio visual de rotas admin para cliente logado|

### Critérios de aceite

- Cliente logado recebe 403 em qualquer rota administrativa
- Expediente com hora final menor que a inicial é barrado no front e no back
- Barbeiro desativado some da listagem pública mas continua no banco
- Máscara de CPF valida antes de enviar

---

# ENTREGA 3 — Agendamento de Corte e Opção de Serviço

**06/10 → 26/10** · _Núcleo do sistema. É a entrega mais pesada das quatro._

> **Atenção:** esta fatia carrega duas coisas ao mesmo tempo (catálogo de serviços + motor de agendamento). Faça o CRUD de serviços nos primeiros 4 dias e reserve o resto do prazo para a disponibilidade. Se a E2 terminar adiantada, puxe o `servico` para lá.

### Banco de dados

|ID|Card|
|---|---|
|E3-BD-01|Migration: tabela `servico` (nome, duração, preço)|
|E3-BD-02|Migration: N:N `barbeiro_servico`|
|E3-BD-03|Migration: tabela `bloqueio_agenda`|
|E3-BD-04|Migration: tabela `agendamento` com FKs e status|
|E3-BD-05|Habilitar `btree_gist` e criar constraint `EXCLUDE` anti-conflito|
|E3-BD-06|Índice composto `(barbeiro_id, inicio)`|
|E3-BD-07|Seed: 6 serviços, vínculos e agendamentos de teste|

### Backend

|ID|Card|
|---|---|
|E3-BE-01|CRUD de `servico` — leitura pública, escrita protegida|
|E3-BE-02|`PUT /barbeiros/{id}/servicos` — vincular serviços ao profissional|
|E3-BE-03|`GET /barbeiros?servico_id=` — quem atende determinado serviço|
|E3-BE-04|CRUD de `bloqueio_agenda`|
|E3-BE-05|**Serviço de disponibilidade**: expediente − bloqueios − agendamentos, respeitando `duracao_min`|
|E3-BE-06|`GET /disponibilidade?barbeiro_id=&servico_id=&data=`|
|E3-BE-07|`POST /agendamentos` com verificação transacional e captura do `IntegrityError` da constraint|
|E3-BE-08|Regras de negócio: antecedência mínima, janela máxima de dias futuros, nada no passado|
|E3-BE-09|Congelar `preco_cobrado` no momento do agendamento|
|E3-BE-10|`GET /agendamentos/meus` — próximos do cliente logado|
|E3-BE-11|`PATCH /agendamentos/{id}/cancelar` com janela mínima|
|E3-BE-12|Testes: dois agendamentos no mesmo slot, serviço longo no fim do expediente, slot sobre bloqueio|

### Frontend

|ID|Card|
|---|---|
|E3-FE-01|Tela admin: CRUD de serviços|
|E3-FE-02|Tela admin: vincular serviços a cada barbeiro|
|E3-FE-03|Página pública de serviços (cards com duração e preço)|
|E3-FE-04|Fluxo de agendamento em passos: serviço → barbeiro → data → horário → confirmação|
|E3-FE-05|Calendário com dias sem expediente desabilitados|
|E3-FE-06|Grade de horários consumindo `/disponibilidade`|
|E3-FE-07|Tela de resumo antes de confirmar (serviço, profissional, data, valor)|
|E3-FE-08|"Meus agendamentos" com os próximos horários|
|E3-FE-09|Modal de cancelamento com confirmação|
|E3-FE-10|Tratar slot ocupado por terceiro: recarregar a grade e avisar|

### Critérios de aceite

- Dois navegadores tentando o mesmo horário: um agenda, o outro recebe erro claro
- Serviço de 60 min não aparece disponível 30 min antes do fim do expediente
- Cancelamento libera o slot imediatamente
- Alterar o preço de um serviço não muda o valor de agendamentos já feitos
- Nenhum horário exibido cai dentro de um bloqueio

---

# ENTREGA 4 — Histórico de Atendimento e Serviço Prestado

**27/10 → 16/11** · _Fecha o ciclo: o agendamento vira atendimento registrado e consultável._

### Banco de dados

|ID|Card|
|---|---|
|E4-BD-01|Migration: tabela `atendimento`|
|E4-BD-02|Migration: tabela `atendimento_servico` (serviços extras na cadeira)|
|E4-BD-03|Migration: tabela `avaliacao` (opcional)|
|E4-BD-04|Índices para consultas de histórico e relatório|
|E4-BD-05|Query agregada de faturamento e volume por período|

### Backend

|ID|Card|
|---|---|
|E4-BE-01|`POST /agendamentos/{id}/iniciar` — abre o atendimento|
|E4-BE-02|`POST /atendimentos/{id}/finalizar` — grava valor final, pagamento e fecha o agendamento como CONCLUIDO|
|E4-BE-03|`PATCH /agendamentos/{id}/nao-compareceu`|
|E4-BE-04|`POST /atendimentos/{id}/servicos` — adicionar serviço extra e recalcular o total|
|E4-BE-05|`GET /clientes/{id}/historico` — atendimentos passados com serviços e valores|
|E4-BE-06|`GET /barbeiros/{id}/historico` com filtro de período|
|E4-BE-07|`GET /atendimentos/{id}` — comprovante detalhado|
|E4-BE-08|`GET /relatorios/resumo` — faturamento, ticket médio, taxa de cancelamento e não comparecimento|
|E4-BE-09|`GET /relatorios/servicos-mais-prestados`|
|E4-BE-10|`POST /atendimentos/{id}/avaliacao` (opcional)|
|E4-BE-11|Testes: finalizar duas vezes, recálculo com serviço extra, histórico só do próprio usuário|

