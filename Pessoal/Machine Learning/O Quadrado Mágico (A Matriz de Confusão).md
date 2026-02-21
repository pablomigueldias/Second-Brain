
Quando uma IA faz um teste de classificação, não basta sabermos apenas "quantas elas acertou". Nós precisamos saber **que tipo de erro** ela está cometendo. Para isso, os cientistas de dados usam a **Matriz de Confusão**

>[!tip] A Regra do Nome 
>O nome de cada quadrante é formado por duas partes
> 	1. **Verdadeiro ou Falso**: A IA acertou (Verdadeiro) ou errou (Falso)?
> 	2. **Positivo ou Negativo**: O que a IA respondeu? Ela disse "Sim"(Positivo) ou "Não"(Negativo)?

Esta tabela cruza o que aconteceu na **Realidade** com o que a **IA Previu**:

| **O que a IA Previu      | **Era Positivo (Real)**                                                                 | **Era Negativo (Real)**                                                                      |
| ------------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **A IA previu Positivo** | ✅ **VP (Verdadeiros Positivos):** Acertou! A IA disse que era Positivo e realmente era. | ❌ **FP (Falsos Positivos):** Errou! A IA deu um _alarme falso_ (disse que era, mas não era). |
| **A IA previu Negativo** | ❌ **FN (Falsos Negativos):** Errou! A IA _deixou passar_ (disse que não era, mas era).  | ✅ **VN (Verdadeiros Negativos):** Acertou! A IA disse que não era, e realmente não era.      |
