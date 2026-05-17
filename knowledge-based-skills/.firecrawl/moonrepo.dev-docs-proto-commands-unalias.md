[Skip to main content](https://moonrepo.dev/docs/proto/commands/unalias#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto unalias <tool> <alias>` (or `proto ua`) command will remove a custom alias for the
provided tool.

```shell
$ proto unalias node work
```

By default this will update the local [`./.prototools`](https://moonrepo.dev/docs/proto/config) file. Pass `--from` to customize
the location.

### Arguments [​](https://moonrepo.dev/docs/proto/commands/unalias\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.
- `<alias>` \- Name of the alias. Supports alphanumeric chars.

## Options [​](https://moonrepo.dev/docs/proto/commands/unalias\#options "Direct link to Options")

- `--from` \- [Location of `.prototools`](https://moonrepo.dev/docs/proto/config#locations) to update. Supports `global`, `local`,
and `user`.v0.41.0

- [Arguments](https://moonrepo.dev/docs/proto/commands/unalias#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/unalias#options)