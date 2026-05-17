Excerpt from docs.falkordb.com/operations/cluster.html:

> A FalkorDB cluster shards the keyspace across multiple master nodes using Redis Cluster's hash-slot mechanism (16,384 slots distributed across the masters).
>
> Each graph exists as a single Redis key residing on the shard whose hash-slot range matches the graph's name hash.
>
> FalkorDB is distributed through Docker containers running the integrated Redis-FalkorDB stack, enabling users to orchestrate multi-node clusters using standard Redis clustering tools like `redis-cli --cluster`.

Source: https://docs.falkordb.com/operations/cluster.html
