Fase 1

|**Passo**|**Detalhe da Ação**|**Ferramentas/Conceito**|**Objetivo**|
|---|---|---|---|
|**1. Projeto**|Inicie o projeto e o repositório Git.|`mkdir` / `git init`|Estruturar o diretório principal.|
|**2. Dependências**|Configure o ambiente virtual e gerencie as dependências.|**Poetry** (Recomendado) ou `pipenv`|Isolamento e reprodutibilidade do projeto.|
|**3. FastAPI**|Instale o framework e as dependências essenciais (servidor).|`poetry add fastapi uvicorn`|Preparar o _core_ da API.|
|**4. Estrutura**|Crie a estrutura de diretórios inicial.|`app/`, `app/main.py`, `app/game_logic.py`, `app/models.py`, `tests/`|Organização do código (Modularidade).|
Fase 2

|**Passo**|**Detalhe da Ação**|**Arquivo Principal**|**Habilidade Demonstrada**|
|---|---|---|---|
|**5. Modelos**|Defina os modelos de dados para a requisição (input do jogador) e resposta (resultado do jogo).|`app/models.py` (Usando Pydantic)|Validação de dados e tipagem.|
|**6. Lógica da Máquina**|Implemente a função que escolhe a jogada da máquina (randômica)1.|`app/game_logic.py`|Uso do módulo `random` e encapsulamento de lógica.|
|**7. Lógica do Jogo**|Crie a função principal que compara as jogadas e determina o resultado (`"win"`, `"lose"`, `"draw"`).|`app/game_logic.py` (Usando `if/else` ou _mapping_)|Resolução de problemas complexos (regras: Pedra > Tesoura, Tesoura > Papel, Papel > Pedra)2222.|
|**8. Endpoint**|Crie o _endpoint_ `POST /api/v1/play` para receber a jogada e retornar o resultado.|`app/main.py`|Criação de API RESTful.|
Fase 3

| **Passo**                                | **Detalhe da Ação**                                                                                                                                | **Ferramentas/Conceito**                     | **Valor para o Recrutador**                                                                          |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **9. Testes Unitários**                  | Instale o Pytest e escreva testes para a função de lógica do jogo (`game_logic.py`). **Teste todas as 9 combinações possíveis** (3x3).             | `poetry add --dev pytest` / Pasta `tests/`   | Compromisso com a qualidade (TDD/Testes Automatizados).                                              |
| **10. Linting & Formatação**             | Configure ferramentas de qualidade para manter o código limpo.                                                                                     | **Black** (Formatador) e **Flake8** (Linter) | Código legível, padronizado e livre de erros simples.                                                |
| **11. Versionamento Semântico (SemVer)** | Use _tags_ no Git para marcar os _releases_ do seu projeto (Ex: `v1.0.0`).                                                                         | `git tag v1.0.0` / `git push --tags`         | Profissionalismo no ciclo de vida do software.                                                       |
| **12. Regra Extra**                      | Implemente a regra extra (não permitir pedra duas vezes seguidas) usando um banco de dados simples (ex: SQLite) ou um sistema de estado de sessão. | `app/game_logic.py`                          | Abordagem de persistência de estado (Conceito de `useState` do React, mas aplicado ao Back-End)3333. |

Fase 4

| **Passo**                             | **Detalhe da Ação**                                                                                     | **Arquivo**                  | **Resultado Final**                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------- | --------------------------------------------- |
| **13. README**                        | Crie um README detalhado com: visão geral, Tech Stack, como instalar e rodar, e como usar o _endpoint_. | `README.md`                  | O cartão de visitas do seu projeto.           |
| **14. Licença**                       | Adicione um arquivo de licença (ex: MIT).                                                               | `LICENSE`                    | Profissionalismo e clareza sobre permissões.  |
| **15. Containerização (Nível Extra)** | Adicione um `Dockerfile` para empacotar a aplicação.                                                    | `Dockerfile`                 | Conhecimento em orquestração/DevOps.          |
| **16. CI/CD (Nível Extra)**           | Configure o GitHub Actions para rodar testes e linting automaticamente em cada _push_.                  | `.github/workflows/main.yml` | Experiência em integração e entrega contínua. |