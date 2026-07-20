---
type: dashboard
tags: [moc, ingles]
---

# 🇺🇸 Inglês — Dashboard

## 📺 Episódios estudados

```dataview
TABLE serie AS "Série", temporada AS "T", episodio AS "Ep", data AS "Data", dificuldade AS "Nível"
FROM #series
WHERE type = "estudo-ingles"
SORT data DESC
```

## 🕐 Últimos 7 dias

```dataview
LIST FROM #series WHERE data >= date(today) - dur(7 days) SORT data DESC
```
