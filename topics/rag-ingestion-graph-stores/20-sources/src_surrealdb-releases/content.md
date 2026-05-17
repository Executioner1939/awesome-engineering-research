## GitHub Releases API

`https://api.github.com/repos/surrealdb/surrealdb/releases?per_page=5`

```
"tag_name": "v3.0.5", "name": "Release 3.0.5", "prerelease": false, "published_at": "2026-03-27T16:07:56Z",
"tag_name": "v2.6.5", "prerelease": false, "published_at": "2026-03-24T13:34:44Z",
"tag_name": "v2.6.4", "prerelease": false, "published_at": "2026-03-17T17:04:20Z",
"tag_name": "v3.0.4", "prerelease": false, "published_at": "2026-03-13...",
"tag_name": "v3.0.3", "prerelease": false, "published_at": "2026-03-10..."
```

Two parallel maintenance lines: 3.x (current, head at 3.0.5) and 2.6.x (LTS, head at 2.6.5).

## Container version

`docker run --rm surrealdb/surrealdb:latest version`:

```
3.0.5 for linux on aarch64
```
