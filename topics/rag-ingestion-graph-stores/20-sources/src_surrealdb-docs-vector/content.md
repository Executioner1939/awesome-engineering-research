Excerpt from surrealdb.com/docs/surrealql/datamodel/vector:

```surql
SELECT
  ->purchased->product AS history,
  ->reviewed->product[WHERE vector::similarity::cosine(embedding, $vec) > 0.8] AS relevant
```

> Graph traversals, vector search, and temporal filtering in a single statement.
>
> One query, every model.
>
> SurrealQL composes graph traversal, vector search, and temporal filtering in a single statement. No multi-system orchestration.

Source: https://surrealdb.com/docs/surrealql/datamodel/vector
