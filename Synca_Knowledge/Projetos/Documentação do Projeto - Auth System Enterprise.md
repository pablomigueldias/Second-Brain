
**Resumo (O que é?):** O projeto Auth System Enterprise é uma solução de nível de produção (_production-grade_) para Autenticação e Gerenciamento de Usuários. O Auth System Enterprise foi construído com foco estrito em arquitetura moderna, melhores práticas de segurança de dados e alta escalabilidade.

**Acesso (Live Demo) e Credenciais:**

- **Frontend:** Hospedado na plataforma Vercel ([Acessar Frontend](https://user-authentication-roan.vercel.app/)).
    
- **Backend:** Hospedado na plataforma Render ([Acessar Backend](https://user-authentication-5ebj.onrender.com)).
    
- **Credenciais de Teste:** O sistema possui uma conta de administrador pré-configurada para testes rápidos, utilizando o email `admin@example.com` e a senha `admin123`.
    

_Aviso sobre Hospedagem (Render Free Tier):_ O backend do Auth System Enterprise está hospedado no plano gratuito do Render, o qual suspende o servidor após 15 minutos de inatividade. O usuário deve acessar a URL do Backend primeiro para "acordar" o servidor (um processo que pode levar até 50 segundos) antes de tentar realizar o login na interface do Frontend.

## Stack Tecnológico do Auth System Enterprise

A infraestrutura tecnológica do Auth System Enterprise divide-se em componentes avançados para operações de Backend e de Frontend:

### Backend (Python)

- **Framework Web:** FastAPI (escolhido pela sua alta performance na construção de APIs).
    
- **ODM (Object-Document Mapper):** Beanie (utilizado para o mapeamento assíncrono de documentos no MongoDB).
    
- **Gerenciador de Dependências:** Poetry.
    
- **Segurança e Autenticação:** A segurança do sistema baseia-se na implementação do protocolo OAuth2, utilizando JWT (JSON Web Tokens) para as sessões e a biblioteca Bcrypt para o _hashing_ de senhas.
    

### Frontend (TypeScript)

- **Framework Web:** Next.js 16 (configurado com a arquitetura moderna de App Router e Server Components).
    
- **Estilização:** Tailwind CSS v4 (framework CSS utilitário).
    
- **Cliente HTTP:** Axios (configurado com _interceptors_ para realizar a injeção automática dos tokens de acesso).
    
- **Validação de Formulários:** React Hook Form (para garantir validações de alta performance).
    

## Arquitetura do Auth System Enterprise

O desenvolvimento do Auth System Enterprise segue estritamente os princípios de _Clean Architecture_ (Arquitetura Limpa) e _Separation of Concerns_ (Separação de Preocupações).

### Fluxo de Componentes e Integração Sistêmica

O ecossistema principal do Auth System Enterprise opera com o seguinte fluxo de dados: O Usuário interage com o Frontend em Next.js através de uma conexão HTTPS. Este Frontend comunica-se com a API Backend em FastAPI realizando requisições HTTP seguras combinando Axios e JWT. Dentro do servidor, a API FastAPI delega responsabilidades para três camadas distintas: valida a entrada de dados utilizando os schemas do Pydantic, processa a autenticação através de um Serviço OAuth2 interno, e finalmente gerencia a persistência lendo e gravando informações no banco de dados MongoDB Atlas.

### Modelagem de Dados (Entidade USER no MongoDB)

A estrutura do banco de dados do Auth System Enterprise concentra-se na coleção `USER`. Cada documento de usuário no MongoDB contém obrigatoriamente:

- `_id`: Identificador principal (ObjectId / PK).
    
- `username`: O nome do usuário em formato string.
    
- `email`: O endereço de email estruturado como uma string e protegido por um Índice Único (_Unique Index_).
    
- `password_hash`: A senha criptografada do usuário.
    
- `role`: O nível de acesso do usuário (padronizado inicialmente como 'user').
    
- `created_at` e `updated_at`: Carimbos de data/hora (datetime) para rastreabilidade.
    
- `is_active`: Um campo booleano para gerenciar a habilitação da conta.
    

### Fluxo de Autenticação (Sequência de Login)

O processo de autenticação e emissão de tokens no Auth System Enterprise segue uma sequência de validação estrita:

1. O Usuário insere seu Email e Senha na interface e o Frontend envia uma requisição `POST` para a rota `/api/v1/auth/login`.
    
2. A API (FastAPI) consulta o banco de dados (MongoDB) buscando exclusivamente pelo Email fornecido e recupera os dados do usuário.
    
3. A API utiliza o Bcrypt para verificar se o Hash da senha salva no banco corresponde à senha digitada.
    
4. **Cenário de Falha (Senha Inválida):** A API retorna um status `401 Unauthorized` e o Frontend processa e exibe a mensagem de erro para o Usuário.
    
5. **Cenário de Sucesso (Senha Válida):** A API gera um _Access Token_ JWT e devolve ao Frontend um status `200 OK` contendo o token e o tipo do token. O Frontend armazena esse token no navegador (Cookie ou Storage) e redireciona o Usuário para a área protegida do Dashboard.
    

## Como Inicializar o Auth System Enterprise Localmente

Para rodar os serviços do Auth System Enterprise no computador local, o ambiente exige as instalações prévias do Python 3.11+, Node.js 20+ e do gerenciador Poetry.

### 1. Configuração do Backend


```Bash
cd backend

# Instalar as dependências do ecossistema Python
poetry install

# Ativar o ambiente virtual do projeto
poetry shell

# Iniciar o servidor FastAPI com suporte a recarregamento automático
uvicorn app.main:app --reload
```

### 2. Configuração do Frontend


```Bash
cd frontend

# Instalar as dependências do ecossistema Node
npm install

# Iniciar o servidor de desenvolvimento do Next.js
npm run dev
```

### 3. Configuração das Variáveis de Ambiente (.env)

O funcionamento pleno do Auth System Enterprise depende da criação de arquivos `.env` na raiz das pastas de frontend e backend, contendo chaves operacionais e _connection strings_.

**Declarações exigidas no Backend (`/backend/.env`):**


```Bash
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
MONGO_URI=mongodb+srv://<user>:<pass>@cluster.mongodb.net/auth_db
```

**Declarações exigidas no Frontend (`/frontend/.env.local`):**


```Bash
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api/v1
```