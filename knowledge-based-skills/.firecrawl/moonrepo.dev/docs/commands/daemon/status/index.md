[Skip to main content](https://moonrepo.dev/docs/commands/daemon/status#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

v2.2.0

The `moon daemon status` command displays information about the running daemon process.

```shell
$ moon daemon status
```

When the daemon is running, the following information is displayed:

- **PID** — The process ID of the daemon.
- **Socket** (macOS/Linux) or **Named pipe** (Windows) — The IPC endpoint used for communication.
- **Uptime** — How long the daemon has been running.
- **PID file** — Path to the PID file (`.moon/cache/daemon/moond.pid`).
- **Log file** — Path to the log file (`.moon/cache/daemon/server.log`).

If the daemon is not running, a warning is displayed instead.

info

View the official [daemon guide](https://moonrepo.dev/docs/guides/daemon) for more information on how the daemon works.