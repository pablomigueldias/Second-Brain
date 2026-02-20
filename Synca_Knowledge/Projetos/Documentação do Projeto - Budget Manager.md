
**Resumo (O que é?):** O projeto **Budget Manager** é uma aplicação Full-Stack de controle financeiro pessoal. O objetivo do Budget Manager é simplificar o rastreamento e o gerenciamento de despesas através de uma interface de usuário (UI) limpa e de uma API RESTful robusta.

**Acessos (Live Demo):**

- **Frontend:** Hospedado na Vercel ([Acessar Aplicação](https://budget-manager-puce.vercel.app)).
    
- **Backend:** Documentação Swagger UI hospedada no Render ([Acessar API Docs](https://budgetmanager-jzu5.onrender.com/docs)).
    

## Stack Tecnológico do Budget Manager

A arquitetura do Budget Manager é dividida entre tecnologias modernas de Backend, Frontend e esteira de Deploy:

### Backend (API)

- **Linguagem:** Python 3.11+.
    
- **Framework:** FastAPI (Escolhido por sua alta performance, facilidade de aprendizado e prontidão para produção).
    
- **Banco de Dados:** PostgreSQL (Ambiente de Produção no Render) e SQLite (Ambiente de Desenvolvimento Local).
    
- **ORM:** SQLAlchemy (Gerenciamento e interações com o banco de dados).
    
- **Gerenciador de Dependências:** Poetry.
    
- **Validação de Dados:** Pydantic.
    

### Frontend (Interface)

- **Biblioteca Principal:** React.js (Versão 18).
    
- **Build Tool:** Vite (Para tempos de build super rápidos).
    
- **Estilização:** Tailwind CSS (Framework CSS utilitário).
    
- **Cliente HTTP:** Axios.
    

### DevOps e Infraestrutura

- **Hospedagem Backend:** Render.
    
- **Hospedagem Frontend:** Vercel.
    
- **CI/CD:** Pipeline de implantação automática acionada via Git push.
    
- **Versionamento:** Git e GitHub (utilizando a padronização Conventional Commits).
    

## Recursos Principais (Key Features)

- **API RESTful Documentada:** O backend do Budget Manager fornece _endpoints_ totalmente documentados utilizando OpenAPI (Swagger UI).
    
- **Sistema de Banco de Dados Híbrido:** O ecossistema do Budget Manager alterna de forma inteligente entre o banco SQLite para desenvolvimento local e o PostgreSQL para produção, utilizando Variáveis de Ambiente.
    
- **Operações CRUD Completas:** O sistema permite a criação, leitura, atualização e exclusão (CRUD) de transações financeiras.
    
- **Sistema de Filtros:** A interface do Budget Manager permite filtrar transações por intervalos de datas e por categorias específicas.
    
- **Design Responsivo:** O frontend do Budget Manager funciona de forma fluida tanto em dispositivos desktop quanto em dispositivos móveis.
    

## Decisões de Engenharia da Arquitetura

### A Escolha do Framework FastAPI

O framework FastAPI foi selecionado para o backend do Budget Manager devido à sua velocidade de execução (baseada no Starlette) e à sua validação automática de dados (baseada no Pydantic). A adoção do FastAPI permitiu o desenvolvimento ágil de uma API robusta, acompanhada de documentação gerada automaticamente.

### Estratégia de Banco de Dados (Paridade de Ambiente)

Para garantir uma excelente experiência de desenvolvimento (DX) sem sacrificar a estabilidade do sistema em produção, o Budget Manager utiliza uma _connection string_ de banco de dados dinâmica. A aplicação utiliza por padrão um arquivo leve SQLite localmente. No entanto, o sistema se conecta automaticamente a um banco de dados relacional PostgreSQL assim que detecta a presença da Variável de Ambiente `DATABASE_URL` no ambiente de nuvem do provedor Render.

## Como Executar o Budget Manager Localmente

**Pré-requisitos do Sistema:**

- Python 3.10+ instalado.
    
- Node.js e npm instalados.
    
- Poetry (Gerenciador de pacotes Python) instalado.
    

### 1. Configuração e Execução do Backend

```Bash
# Clonar o repositório oficial do Budget Manager
git clone https://github.com/pablomigueldias/BudgetManager
cd budget-manager/backend

# Instalar as dependências do Python utilizando o Poetry
poetry install

# Ativar o ambiente virtual isolado
poetry shell

# Iniciar o servidor FastAPI com hot-reload ativo
uvicorn app.main:app --reload
```

### 2. Configuração e Execução do Frontend


```Bash
# Em um novo terminal, navegar até o diretório do frontend
cd ../frontend

# Instalar as dependências do ecossistema Node
npm install

# Iniciar o servidor de desenvolvimento do Vite
npm run dev
```

---

**Contato do Desenvolvedor:** Pablo Miguel Dias Ortiz - Fullstack Developer & Data Science.