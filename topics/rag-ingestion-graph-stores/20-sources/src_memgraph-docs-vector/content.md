Excerpt from memgraph.com/docs/querying/vector-search:

> Vector search, also known as vector similarity search or nearest neighbor search, is a technique used to find the most similar items in a collection of data based on their vector representations.
>
> Vector search is commonly used as a retrieval technique in RAG systems to find entities based on semantic similarity rather than exact matches.

Limitation called out by the docs:

> Unlike other index types, the query planner currently does not utilize vector indices.

The vector index is accessed via `vector_search.search()` / `vector_search.search_edges()` procedure calls returning nodes/edges with distances, which can then feed graph traversal in a follow-on `MATCH`.

Source: https://memgraph.com/docs/querying/vector-search
