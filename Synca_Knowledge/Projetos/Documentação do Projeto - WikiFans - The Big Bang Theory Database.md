
**Resumo (O que é?):**

O projeto WikiFans é uma aplicação Full Stack moderna, responsiva e internacionalizada (i18n). O objetivo do WikiFans é atuar como uma base de dados interativa para consultar informações detalhadas sobre os personagens da série de televisão _The Big Bang Theory_. O projeto foi arquitetado para demonstrar competências avançadas em desenvolvimento web, com foco estrito em Arquitetura Limpa, criação de um Design System Escalável e otimização da Experiência do Usuário (UX).

**Acesso (Live Demo) e Documentação:**

- **Frontend (Vercel):** [Acessar Projeto WikiFans](https://wiki-fans.vercel.app/).
    
- **Backend API (Render):** [Acessar Swagger UI do WikiFans](https://wikifans.onrender.com/docs).
    

## Stack Tecnológico do WikiFans

A arquitetura do projeto WikiFans é baseada na separação de responsabilidades (Frontend e Backend), utilizando as seguintes tecnologias:

### Frontend (Interface do Usuário)

- **Framework Principal:** React.js operando dentro do ecossistema Vite para otimização de performance.
    
- **Estilização:** Tailwind CSS v4, adotando a versão mais recente para criação de um Design System customizado.
    
- **Animações:** Framer Motion, responsável pelas animações de entrada e transições de layout fluidas.
    
- **Roteamento e Requisições:** React Router Dom para navegação em SPA (Single Page Application) e Axios para comunicação HTTP segura.
    
- **Iconografia:** Lucide React.
    

### Backend (API RESTful)

- **Linguagem e Framework:** Python 3.12 em conjunto com o framework ASGI FastAPI, garantindo execução assíncrona de altíssima performance.
    
- **Banco de Dados e ORM:** SQLite atua como o banco de dados relacional primário, enquanto o SQLAlchemy realiza a manipulação e mapeamento objeto-relacional (ORM) dos dados.
    
- **Validação:** Pydantic é utilizado para a validação estrita dos _schemas_ de dados recebidos e enviados pela API.
    
- **Servidor Web:** Uvicorn.
    

### Infraestrutura e DevOps

- **Deploy Frontend:** Hospedado na nuvem da Vercel.
    
- **Deploy Backend:** Hospedado na nuvem do provedor Render.
    
- **Versionamento:** Git e GitHub.
    

## Funcionalidades Principais do WikiFans

- **Suporte Multi-idioma (i18n):** O Frontend do WikiFans possui suporte nativo aos idiomas Inglês e Português, permitindo a troca instantânea de linguagem arquitetada através da Context API do React.
    
- **Design System Personalizado e Temas:** A interface do WikiFans utiliza variáveis nativas de tema CSS mapeadas pelo Tailwind CSS v4 para estabelecer cores semânticas padronizadas (como `primary`, `secondary` e `surface`).
    
- **Responsividade Mobile-First:** O layout do WikiFans é perfeitamente fluido e adaptável a telas de celulares, tablets e desktops, fazendo uso intensivo das tecnologias CSS Grid e Flexbox.
    
- **Mecanismo de Busca Híbrida:** A API Backend do WikiFans foi projetada para resolver buscas de personagens aceitando tanto o identificador numérico (`ID`) quanto o identificador textual (`Slug`) na mesma rota.
    

## Endpoints da API do WikiFans

O Backend do WikiFans segue estritamente os padrões RESTful de desenvolvimento de software. Abaixo estão as rotas públicas disponíveis no sistema:

|**Método HTTP**|**Endpoint do WikiFans**|**Descrição e Comportamento**|**Exemplo de Requisição**|
|---|---|---|---|
|`GET`|`/`|**Health Check:** Rota raiz utilizada para verificar se o servidor da API do WikiFans está online e processando requisições adequadamente.|`https://wikifans.onrender.com/`|
|`GET`|`/personagens`|**Listagem Global:** Rota que retorna um _array_ JSON contendo um resumo descritivo de todos os personagens da série cadastrados no banco de dados.|`https://wikifans.onrender.com/personagens`|
|`GET`|`/personagens/{personagem_id}`|**Consulta Detalhada:** Rota híbrida que busca os dados completos de um personagem específico. O mecanismo de busca do WikiFans aceita como parâmetro dinâmico tanto o ID numérico quanto o Slug textual.|`/personagens/1`|

## Como Inicializar o WikiFans Localmente

Para o desenvolvimento local, o sistema exige a instalação prévia do Node.js, npm e Python 3.10 ou superior.

### 1. Configuração e Execução do Backend


```Bash
# Navegar para o diretório da API do WikiFans
cd back-end

# (Opcional) Criar e isolar as dependências em um ambiente virtual
python -m venv venv
source venv/bin/activate  # Para sistemas Linux/Mac
venv\Scripts\activate     # Para sistemas Windows

# Instalar os pacotes e bibliotecas Python necessárias
pip install -r requirements.txt

# Iniciar o servidor web Uvicorn do FastAPI em modo de recarregamento
uvicorn main:app --reload
```

### 2. Configuração e Execução do Frontend


```Bash
# Navegar para o diretório da interface web do WikiFans
cd front-end

# Instalar as dependências do ecossistema Node.js
npm install

# Criar o arquivo de Variáveis de Ambiente (.env) apontando para a API local
echo "VITE_API_URL=http://127.0.0.1:8000" > .env

# Inicializar o servidor de desenvolvimento super rápido do Vite
npm run dev
```