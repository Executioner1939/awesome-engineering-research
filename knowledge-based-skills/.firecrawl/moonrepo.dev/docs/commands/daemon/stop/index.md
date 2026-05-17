[Skip to main content](https://moonrepo.dev/docs/commands/daemon/stop#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

v2.2.0

The `moon daemon stop` command will stop the running daemon process. It first attempts a graceful
shutdown, and if the daemon does not exit within a few seconds, it will be forcefully killed. Daemon
files (PID, socket) are cleaned up automatically.

```shell
$ moon daemon stop
```

If the daemon is not running, a warning is displayed and no action is taken.

info

View the official [daemon guide](https://moonrepo.dev/docs/guides/daemon) for more information on how the daemon works.