## GitHub Releases API

`https://api.github.com/repos/FalkorDB/FalkorDB/releases?per_page=3`

```
"tag_name": "v4.18.7", "prerelease": false, "published_at": "2026-05-14T12:04:33Z",
"tag_name": "v4.18.6", "prerelease": false, "published_at": "2026-05-11T20:42:05Z",
"tag_name": "v4.18.5", "prerelease": false, "published_at": "2026-05-11T11:00:52Z",
```

## Container inspection

`docker run --rm falkordb/falkordb:latest` then `redis-cli MODULE LIST` and `INFO server`:

```
name graph
ver 41807
path /var/lib/falkordb/bin/falkordb.so
args MAX_QUEUED_QUERIES 25 TIMEOUT 1000 RESULTSET_SIZE 10000
name vectorset
ver 1
--- INFO server ---
redis_version:8.6.3
redis_mode:standalone
os:Linux 6.12.76-linuxkit aarch64
```

Module wire-version `41807` corresponds to release tag `v4.18.7`; the FalkorDB container ships the module loaded into Redis 8.6.3.
