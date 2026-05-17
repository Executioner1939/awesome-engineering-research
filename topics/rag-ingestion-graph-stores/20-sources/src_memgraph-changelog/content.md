Excerpt from memgraph.com/docs/release-notes:

## v3.10.0 (2026-05-13)

> Vector edge indexes now use the single-store pattern (storing only a `VectorIndexId`).
>
> Coordinators ignore periodic storage snapshots (no user data to snapshot).
>
> HA coordinator cluster operations ... now follow a Raft-first pattern with majority acknowledgment before success.
>
> Fine-grained label and edge-type permissions now support explicit `DENY` semantics.
>
> Per-database memory tracking via Tenant Profiles.

Built-in roles (admin, readonly, readwrite) auto-created.

## v3.9.0 (2026-03-25)

> Concurrent operations on vector indexes ... are now less contention-prone: internal locking allows multiple writers in parallel.
>
> Parallel vector index recovery.
>
> Server-side global parameters persisting across sessions and replicated cluster-wide.

Kerberos SSO module added.

Source: https://memgraph.com/docs/release-notes
