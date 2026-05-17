Excerpt from memgraph.com/docs/fundamentals/storage-memory-usage:

> IN_MEMORY_TRANSACTIONAL — the default database storage mode that favors strongly-consistent ACID transactions.
>
> IN_MEMORY_ANALYTICAL — speeds up import and data analysis but offers no ACID guarantees besides manually created snapshots.
>
> ON_DISK_TRANSACTIONAL — supports ACID properties in the same way as IN_MEMORY_TRANSACTIONAL with the additional ability to store data on disk.

`ON_DISK_TRANSACTIONAL` uses RocksDB as the on-disk store; the transactional working set still fits in RAM.

Source: https://memgraph.com/docs/fundamentals/storage-memory-usage
