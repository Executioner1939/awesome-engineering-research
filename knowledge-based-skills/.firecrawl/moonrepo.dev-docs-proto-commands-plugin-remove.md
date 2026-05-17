[Skip to main content](https://moonrepo.dev/docs/proto/commands/plugin/remove#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.23.0

The `proto plugin remove <id>` command will remove the provided tool ID from the `[plugins]` section
of the chosen (`.prototools`).

```shell
$ proto plugin remove node
```

> Built-in plugins _cannot_ be removed!

### Arguments [​](https://moonrepo.dev/docs/proto/commands/plugin/remove\#arguments "Direct link to Arguments")

- `<id>` \- ID of the tool.

### Options [​](https://moonrepo.dev/docs/proto/commands/plugin/remove\#options "Direct link to Options")

- `--from` \- [Location of `.prototools`](https://moonrepo.dev/docs/proto/config#locations) to update.v0.41.0
- `--type` \- Type of plugin to remove, either `tool` (default) or `backend`.v0.52.0

- [Arguments](https://moonrepo.dev/docs/proto/commands/plugin/remove#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/plugin/remove#options)