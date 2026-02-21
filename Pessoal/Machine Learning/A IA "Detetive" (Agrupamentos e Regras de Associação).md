
Diferente da Classificação e da Regressão, onde nós dizemos para a máquina exatamente o que queremos que ele adivinhe (o preço ou a categoria), nesta duas tarefas a IA trabalha como uma detetive procurando **padrões ocultos**.

### Agrupamentos (Clusterings)

A tarefa de Agrupamento serve para **identificar grupos de instâncias de dados que são similares**. A IA olha para um multidão de dados misturados e os separa em "tribos com características parecidas."

- **Exemplo Prático(Segmentação de Clientes)**: Uma loja tem vários clientes e quer fazer campanhas de marketing diferentes. A IA analisa a idade, renda e preferências e os divide em "Segmentos"(grupos). A loja não sabia quais eram os grupos antes da IA fazer o cálculo!

Observe como a IA criou a última coluna ("Segmento") agrupando pessoas com perfis parecidos:

|**Cliente**|**Idade**|**Gênero**|**Renda**|**Compras Online**|**Compras em Loja**|**Preferência de Produto**|**Segmento (Criado pela IA)**|
|---|---|---|---|---|---|---|---|
|1|32|F|3500|Sim|Não|Eletrônicos|Segmento 2|
|2|45|M|4500|Não|Sim|Roupas|Segmento 1|
|3|28|M|2500|Sim|Não|Esportes|Segmento 2|
|4|60|F|6500|Não|Sim|Casa e Decoração|Segmento 3|
|5|50|M|5000|Sim|Sim|Eletrônicos|Segmento 1|
|6|40|F|4000|Sim|Não|Beleza|Segmento 2|
|7|35|M|3000|Não|Sim|Esportes|Segmento 2|
|8|55|F|5500|Não|Sim|Casa e Decoração|Segmento 3|
|9|42|M|4800|Sim|Sim|Roupas|Segmento 1|
|10|29|F|3200|Sim|Não|Bebidas|Segmento 2|

---

## Regras de Associação

A tarefa de Regras de Associação serve para **identificar relações frequentes entre itens de um conjunto de dados**. Em vez de agrupas pessoas, ela encontra coisas que costumam acontecer juntas.

- **Exemplo Prático(Recomendação de Produtos)**: É o famoso "Quem comprou X, também comproy Y". Se a IA perceber que muitas pessoas que compram "camiseta" e "Calça" também compra "Boné", ela cria uma regra de associação para recomendar boné para o próximo cliente que levar a camiseta e a calça.

E olhando para essas combinações que a IA crias as recomendações:

|**Cliente**|**Item 1**|**Item 2**|**Item 3**|**Item 4**|
|---|---|---|---|---|
|1|Camiseta|Calça|Boné|Óculos|
|2|Calça|Boné|Óculos|Cinto|
|3|Camiseta|Óculos|Cinto|Relógio|
|4|Camiseta|Boné|Relógio|Tênis|
|5|Calça|Relógio|Tênis|Óculos|
|6|Camiseta|Tênis|Boné|Cinto|
|7|Calça|Tênis|Cinto|Óculos|
|8|Camiseta|Boné|Tênis|Relógio|
|9|Camiseta|Calça|Relógio|Cinto|
|10|Camiseta|Óculos|Tênis|Cinto|