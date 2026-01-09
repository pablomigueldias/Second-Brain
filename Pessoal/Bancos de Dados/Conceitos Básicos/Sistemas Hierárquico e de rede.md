
- Registros com estruturas semelhantes
- Muitos tipos de registros e muitos relacionamentos entre eles
- Não ofereciam capacidades suficientes para:
	- Abstração de dados
	- Independência de dados e programas
- Mainframes: Grandes e caros!
- 3 paradigmas principais: Hierárquico , Rede e Arquivos invertidos

[[Modelo Paradigmas.canvas|Modelo Paradigmas]]

## OFERECENDO ABSTRAÇÃO E FLEXIBILIDADE

- Banco de Dados Relacionais
	- Separa o armazenamento físico dos dados de sua representação conceitual
	- fornece uma base matemática para representação e consulta de dados.
- 1970 - Sistemas Relacionais Experimentais
- 1980 - SGBDs relacionais
- Melhoria no processamento e otimização de consulta.

## BD MAIS COMPLEXOS (O-O)

- Final da década de 80 - Linguagens orientadas a objetos
- Necessidade de armazenar e compartilhar objetos complexos e estruturados
	- BDOOs
	- Complexidade do modelo e falta de um padrão
- Conceitos de OO -> Relacionais
	- SGBDORs

## INTERCÂMBIO DE DADOS NA WEB (XML)

- Web + HMTL
	-  Dados extraídos dinamicamente de diversos SGBDs
- XML combina conceitos dos modelos usados nos sistemas de documentos com os conceitos de modelagem de banco de dados

## NOVAS APLICAÇÕES DE BANCO DE DADOS

- Aplicações tinham sua própria estrutura de arquivos e dados
- SGBDs possuem extensões que dão suporte às necessidades especializadas de algumas aplicações
	- Aplicações cientificas
	- Armazenamento e recuperação de imagens
	- Armazenamento e recuperação de vídeos
	- Mineração de dados
	- Aplicações espaciais(clima, mapas ...)
	- Aplicações de séries temporais

## PROBLEMAS DE APLICAÇÕES NO MODELO RELACIONAL

- Estruturas de dados mais complexas eram necessárias para modelar a aplicação do que a representação relacional simples
- Novos tipos de dados eram necessários além dos tipos numéricos e alphanuméricos.
- Novas operações e construtores de consulta eram necessários para manipular os novos tipos de dados
- Novas estruturas de armazenamento eram necessárias para pesquisa eficiente sobre os novos tipos de dados

## NOVAS FUNCIONALIDADES DO SGBDS

- Incorporação de conceitos de BDOO aos sistemas relçacionais
- Novos módulos!
-  Banco de dados de Back-ends.
-  ERP = Enterprise Resource Planning
	- Consolida diversas áreas funcionais dentro de uma organização
- CRM = Customer RelationShip Managment
	- Funções de processamento de pedido, bem como marketing e suporte ao cliente

## NOSQL OU BIGDATA

- Atual geração de banco de dados
- aborda alguns dos pontos: ser não-relacional, distribuído, de código aberto e escalável horizontalmente.
- A Intenção original tem sido banco de dados modernos escaláveis na / para web.
- O movimento começou no inicio de 2009 e está crescendo rapidamente.

Características:

- Livre de esquema(schema-free),
- Suporte a replicação, API simples, consistência eventual / BASE (não ACID),
- Quantidade enorme de dados
- Definição por produto e linguagem de interface "Obter uma resposta rápida é mais importante do que obter uma resposta correta"










