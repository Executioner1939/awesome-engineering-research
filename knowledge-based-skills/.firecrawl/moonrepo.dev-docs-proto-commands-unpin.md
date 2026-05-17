[Skip to main content](https://moonrepo.dev/docs/proto/commands/unpin#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.36.0

The `proto unpin <tool>` command will unpin a version of a tool.

```shell
$ proto unpin go
$ proto unpin node --tool-native
```

By default this will update the local [`./.prototools`](https://moonrepo.dev/docs/proto/config) file. Pass `--from` to customize
the location.

### Arguments [​](https://moonrepo.dev/docs/proto/commands/unpin\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.

### Options [​](https://moonrepo.dev/docs/proto/commands/unpin\#options "Direct link to Options")

- `--from` \- [Location of `.prototools`](https://moonrepo.dev/docs/proto/config#locations) to update. Supports `global`, `local`,
and `user`.v0.41.0
- `--tool-native` \- Use a tool specific location, like the `devEngines` field in the `package.json`
for JavaScript tools.v0.55.0

- [Arguments](https://moonrepo.dev/docs/proto/commands/unpin#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/unpin#options)