[Skip to main content](https://moonrepo.dev/docs/proto/commands/pin#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.19.0

The `proto pin <tool> <version>` command will pin a version (or alias) of a tool. This version will
be used when attempting to [detect a version](https://moonrepo.dev/docs/proto/detection).

```shell
$ proto pin go 1.20
$ proto pin python 3.14 --to=global
$ proto pin node lts --resolve
$ proto pin npm latest --resolve --tool-native
```

By default this will update the local [`./.prototools`](https://moonrepo.dev/docs/proto/config) file. Pass `--to` to customize
the location, or use the `--tool-native` option to use a location unique to the tool.

### Arguments [​](https://moonrepo.dev/docs/proto/commands/pin\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.
- `<version>` \- Version of tool.

### Options [​](https://moonrepo.dev/docs/proto/commands/pin\#options "Direct link to Options")

- `--resolve` \- Resolve the version to a fully-qualified semantic version before pinning.
- `--to` \- [Location of `.prototools`](https://moonrepo.dev/docs/proto/config#locations) to update. Supports `global`, `local`,
and `user`.v0.41.0
- `--tool-native` \- Pins the version in a tool specific location. Examples:v0.55.0
  - JavaScript tooling (Node, Bun, Deno, npm, pnpm, Yarn, etc)
    - Pins version in the `devEngines` field in the `package.json` file.

- [Arguments](https://moonrepo.dev/docs/proto/commands/pin#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/pin#options)