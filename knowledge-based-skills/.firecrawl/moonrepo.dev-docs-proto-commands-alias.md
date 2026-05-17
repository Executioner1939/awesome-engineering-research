[Skip to main content](https://moonrepo.dev/docs/proto/commands/alias#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto alias <tool> <alias> <version>` (or `proto a`) command will define a custom alias that
maps to a specific version for the provided tool. Aliases can be used anywhere a version is
accepted.

```shell
$ proto alias node work 16.16
```

By default this will update the local [`./.prototools`](https://moonrepo.dev/docs/proto/config) file. Pass `--to` to customize
the location.

### Arguments [​](https://moonrepo.dev/docs/proto/commands/alias\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.
- `<alias>` \- Name of the alias. Supports alphanumeric chars.
- `<version>` \- Version to map to the alias.

## Options [​](https://moonrepo.dev/docs/proto/commands/alias\#options "Direct link to Options")

- `--to` \- [Location of `.prototools`](https://moonrepo.dev/docs/proto/config#locations) to update. Supports `global`, `local`,
and `user`.v0.41.0

- [Arguments](https://moonrepo.dev/docs/proto/commands/alias#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/alias#options)