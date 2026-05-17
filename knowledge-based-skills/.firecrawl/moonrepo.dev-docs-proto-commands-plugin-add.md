[Skip to main content](https://moonrepo.dev/docs/proto/commands/plugin/add#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.23.0

The `proto plugin add <id> <plugin>` command will add the provided ID and plugin locator string to
the `[plugins]` section of a chosen `.prototools`.

```shell
$ proto plugin add node "https://github.com/moonrepo/node-plugin/releases/latest/download/node_plugin.wasm"
```

> Learn more about [plugin locator strings](https://moonrepo.dev/docs/proto/plugins#enabling-plugins).

### Arguments [​](https://moonrepo.dev/docs/proto/commands/plugin/add\#arguments "Direct link to Arguments")

- `<id>` \- ID of the tool.
- `<plugin>` \- How to locate the plugin.

### Options [​](https://moonrepo.dev/docs/proto/commands/plugin/add\#options "Direct link to Options")

- `--to` \- [Location of `.prototools`](https://moonrepo.dev/docs/proto/config#locations) to update.v0.41.0
- `--type` \- Type of plugin to add, either `tool` (default) or `backend`.v0.52.0

- [Arguments](https://moonrepo.dev/docs/proto/commands/plugin/add#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/plugin/add#options)