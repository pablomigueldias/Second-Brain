
Assim como usamos `Query` para validar parâmetros de busca, usamos `Path` para validar parâmetros que fazem parte da URL. A sintaxe é muito parecida, mas com regras matemáticas.

## Importando o `Path`

Primeiro, precisamos importar o `Path` do FastAPI.

```Python
from fastapi import FastAPI, Path
```

A grande diferença entre `Query` e `Path` é : 