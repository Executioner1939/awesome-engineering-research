[Skip to main content](https://moonrepo.dev/docs/commands/daemon/logs#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

v2.2.0

The `moon daemon logs` command tails the daemon's log file in real time, streaming new entries as
they are written. The daemon must be running for this command to work.

```shell
$ moon daemon logs
```

The log file is located at `.moon/cache/daemon/server.log` and contains detailed trace-level output,
including file watcher events, graph rebuilds, and RPC requests.

info

On macOS/Linux this command uses `tail -f` under the hood. On Windows it uses PowerShell's
`Get-Content -Wait`.

If the daemon is not running or the log file does not exist, a warning is displayed and no action is
taken.