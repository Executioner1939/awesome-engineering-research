[Skip to main content](https://moonrepo.dev/docs/commands/sync/projects#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.8.0

The `moon sync projects` command will force sync _all_ projects in the workspace to help achieve a
healthy repository state. This applies the following:

- Ensures cross-project dependencies are linked based on
[`dependsOn`](https://moonrepo.dev/docs/config/project#dependson).
- Ensures language specific configuration files are present and accurate.
- Ensures root configuration and project configuration are in sync.
- Any additional language specific semantics that may be required.

```shell
$ moon sync projects
```

> This command should rarely be ran, as [`moon run`](https://moonrepo.dev/docs/commands/run) will sync affected projects
> automatically! However, when migrating or refactoring, manual syncing may be necessary.

### Configuration [​](https://moonrepo.dev/docs/commands/sync/projects\#configuration "Direct link to Configuration")

- [`projects`](https://moonrepo.dev/docs/config/workspace#projects) in `.moon/workspace.*`

- [Configuration](https://moonrepo.dev/docs/commands/sync/projects#configuration)