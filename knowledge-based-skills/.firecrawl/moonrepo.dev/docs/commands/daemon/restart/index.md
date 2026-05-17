[Skip to main content](https://moonrepo.dev/docs/commands/daemon/restart#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

v2.2.0

The `moon daemon restart` command will stop the currently running daemon process and start a new
one. This is useful after manual configuration changes, when the cached state seems stale, or after
upgrading moon to a new version.

```shell
$ moon daemon restart
```

caution

The daemon must be enabled in your [workspace configuration](https://moonrepo.dev/docs/config/workspace) before it can
be restarted. If the `daemon` setting is not enabled, this command will display a warning and exit.

info

View the official [daemon guide](https://moonrepo.dev/docs/guides/daemon) for more information on how the daemon works.