
-  Processo de Software é um conjunto de atividades que leva á produção de um produto de software. (Sommerville)
- Um pouco de história.
- Os modelos encontrados no mercado não são mutuamente excludentes e são na verdade usados em conjunto.
- Quebrando mitos: São escolhidos conforme a natureza do projeto.

Modelo Sequencial linear - Cascata

- Sugere uma abordagem sistemática sequencial
- Inicia no nível do sistema e progride até a manutenção

	[[Cascata.canvas|Cascata]]

- Engenharia de sistemas/informação: estabelecimento de todos os requisitos para o sistema e alocação de algum sobconjunto desses requisitos para o software.
- A engenharia de sistema trata de um conjunto de necessidades a nível de sistema em alto nível, a engenharia da informação inclui um conjunto de necessidades a nível estratégico e das áreas de negócio.

## Etapas

- `Analise de requisitos de software`: Intensificação da análise de requisitos no que o software precisa ter, conhecimento do domínio da informação do software, função, comportamento, desempenho e interface.
- `Projeto`: enfoca a estrutura de dados, arquitetura do software, representações da interface e detalhes procedimentais. Traduz os requisitos de forma que a representação do software possa ser avaliada da codificação.
- `Codificação (teste de unidade)`: Tradução do projeto para linguagem de máquina.
- `Teste(integração)`: condução de testes para descobrir erros e garantir que entradas definidas produzirão resultados reais, que concordam com os resultados exigidos.
- `Manutenção(operação)`: se torna necessária quando se tem tem uma modificação. Reaplica cada uma das fases precedentes a um programa existente.

## Vantagem/Desvantagem

- `Vantagem`: maior capacidade de organização do projeto, visto que uma etapa só inicia após a anterior.
- `Desvantagem`:
	- Modificações poderão causar confusões.
	- Dificilmente o cliente expõe todos os requisitos de uma só vez.
	- Só teremos uma versão executável após o termino do projeto.

## Modelos Evolucionários

- Modelos de processo que foram projetados para acomodar um produto que evolui com o tempo.

- ***Modelo Incremental:***
	- Combina modelo sequencial linear com a filosofia interativa da prototipagem
	- o primeiro incremento é chamado de núcleo do produto
	- Desenvolve-se um plano para cada incremento de forma que o núcleo do produto seja modificado para melhor satisfazer às necessidades do cliente e à elaboração de características e funcionalidades adicionais.
	- Objetiva elaboração de um produto funcional.
	- Útil quando não há mão de obra disponível para uma implementação completa, dentro do prazo comercial de entrega

	[[Incremento.canvas|Incremento]]
