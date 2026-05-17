Excerpt from docs.falkordb.com/cypher/indexing/vector-index.html:

> Creating vector indexes.
>
> Querying vector indexes using `CALL db.idx.vector.queryNodes()`.
>
> Returning node results from vector searches.

Observation: the docs page demonstrates the procedure call and its return shape, but does not include an example combining the vector procedure with subsequent graph traversal (`MATCH ... -[*]->`) in a single Cypher statement. Integration is procedure-call-and-stitch, not language-level fusion.

Source: https://docs.falkordb.com/cypher/indexing/vector-index.html
