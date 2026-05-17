[Skip to main content](https://moonrepo.dev/docs/commands/daemon/start#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

v2.2.0

The `moon daemon start` command will start the daemon background process if it's not already
running. If a daemon is already running for this workspace, the existing process is reused.

```shell
$ moon daemon start
```

info

You typically don't need to run this command manually. When the daemon is
[enabled](https://moonrepo.dev/docs/guides/daemon#enabling-the-daemon), it starts automatically with any `moon` command.

caution

The daemon must be enabled in your [workspace configuration](https://moonrepo.dev/docs/config/workspace) before it can
be started. If the `daemon` setting is not enabled, this command will display a warning and exit.