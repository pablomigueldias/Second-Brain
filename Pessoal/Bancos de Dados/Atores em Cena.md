
# DBA ou AD?


- Administrador de Dados (AD)
	-  É a pessoa que toma as decisões estratégicas e de normas com relação aos dados da empresa.
- Administrador do Bando de dados (DBA)
	- É as pessoa que fornece o suporte técnico necessário para implementar essas decisões. Assim, o DBA é responsável pelo controle geral do sistema em um nível técnico.

## ADMIN. DE BANCO DE DADOS (DBA)

- Banco de dados
	- Recurso principal
- SGBD e os software relacionados
	- Recurso secundário
- DBA é o responsável
	-  Por autorizar o acesso ao banco de dados, coordenar e monitorar seu uso e adquirir recurso de software e hardware conforme a necessidade
	-  por resolver problemas como falha na segurança e demora no tempo de resposta do sistema.

## ATRIBUIÇÕES DO DBA

- Definir o esquema conceitual
- Definir o esquema interno
- Contato com os usuários
- Definir restrições de segurança e integridade
- Monitorar o desempenho e responder a requisitos de mudanças
- Definir normal de descarga e recarga

## DEFINIR NORMAS DE DESGARGA E RECARGA

- O DBA tem de definir e implementar um esquema apropriado de controle de danos, em geral envolvendo:

1. Descarga ou `dumping` periódico do banco de dados para o meio de armazenamento de backup e
2.  Recarga ou `restauração` do banco de dados quando necessário, a partir do `dump` mais recente.

## POJETISTA DE BANCO DE DADOS (ADS)

- Responsáveis:
	- Identificar os `dados` a serem armazenados
	- Escolher `estruturas` apropriadas para representar esses dados.

- Para isso...
	- Precisa se comunicar com todos os potenciais usuários a fim de entender suas necessidades e criar um projeto que as atenda.
	-  Definem visões!

## ATRIBUIÇÕES DO DA

- Decidir quais informações devem ser mantidas no banco de dados;
	-  identificar as entidades de interesse para a empresa e identificar as informações a serem registradas sobre essas entidades(Projeto Lógico ou conceitual)
- Padronizam os nomes dos objetos criados no BD;
- Gerencia  e auxiliam na definição das regras de integridade;
- Controlam a existência de informações redundantes;
- Trabalham de forma corporativa nos modelos de dados da organização;

## Usuários Finais

- Pessoas cujas funções exigem acesso ao BD para consulta, atualizações e geração de relatórios.
- São divididos em:
	-  Casuais -  Ocasionalmente acessam o banco de dados
	-  Iniciantes ou paramétricos - Sua função principal gira em tordo de consultar e atualizar o banco de dados constantemente, usando tipos padrão de consultas e atualizações - denominadas transações programadas.
	- Sofisticados - estão profundamente familiarizados com a facilidades do SGBD a ponto de implementar as próprias aplicações
	- Isolados - mantêm banco de dados pessoais usando pacotes de programas prontos, que oferecem interfaces de fácil utilização, baseadas em menus ou gráficos

## ANALISTA DE SISTEMAS E PROGRAMADORES

- Analista de sistemas -> Identificam as necessidades dos usuários finais, especialmente os iniciantes e paramétricos, e definem as especificações das transações padrão que atendam as elas.
- Programadores -> Implementam essas especificações como programas; depois testam, depuram, documentam e mantêm essas transações programadas.

## TRABALHADORES DOS BASTIDORES

- Trabalham para manter o ambiente do Sistema do Banco de Dados.
-  Projetista e implementadores de Sistemas de SGBDs
-  Desenvolvedores de ferramentas
- Operadores e pessoal de manutenção(suporte)

[[Atores em cena - Mapa.canvas|Atores em cena - Mapa]]



