[Skip to main content](https://moonrepo.dev/docs/proto/commands/list#__docusaurus_skipToContent_fallback)

On this page

danger

This command was removed in v0.44, use [`proto versions`](https://moonrepo.dev/docs/proto/commands/versions) instead!

The `proto list <tool>` (or `proto ls`) command will list installed versions by scanning the
manifest at `~/.proto/tools/<tool>/manifest.json` for possible versions.

```shell
$ proto list node
16.16.0
18.2.0
19.4.0
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/list\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.

### Options [​](https://moonrepo.dev/docs/proto/commands/list\#options "Direct link to Options")

- `--aliases` \- Include aliases in the list.

- [Arguments](https://moonrepo.dev/docs/proto/commands/list#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/list#options)