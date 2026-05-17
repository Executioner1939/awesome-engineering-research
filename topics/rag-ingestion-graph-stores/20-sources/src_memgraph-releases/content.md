## GitHub Releases API

`https://api.github.com/repos/memgraph/memgraph/releases?per_page=3`

```
"tag_name": "v3.10.1", "prerelease": false, "published_at": "2026-05-15T09:42:30Z",
"tag_name": "v3.10.0", "prerelease": false, "published_at": "2026-05-13T10:45:27Z",
"tag_name": "v3.9.0",  "prerelease": false, "published_at": "2026-03-25T11:44:43Z"
```

## Container version

`docker run --rm memgraph/memgraph:latest --version`:

```
memgraph version 3.10.1
```

Also emitted at startup:

```
The instance_down_timeout_sec flag is deprecated ... Please set this setting by running 'SET COORDINATOR SETTING ...'
```

— confirming Raft-coordinator semantics in 3.10.x.
