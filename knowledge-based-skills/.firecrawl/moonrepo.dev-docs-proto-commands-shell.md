[Skip to main content](https://moonrepo.dev/docs/proto/commands/shell#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.54.0

The `proto shell <tools...>` (or `proto sh`, `proto session`) command will initialize a list of
tools into the environment and start an interactive shell session with that environment active.

```shell
$ proto shell node@20 npm@10
```

Tools will automatically detect a version to launch with based on loaded `.prototools`, but the
version can be provided inline by suffixing the tool with `@<version>`. If no tools are provided,
the list will be inherited from the current `.prototools` configuration.

```shell
$ proto shell node pnpm
```

This is effectively a convenience wrapper around [`proto exec`](https://moonrepo.dev/docs/proto/commands/exec) that launches an interactive
shell instead of an arbitrary command. Inside the session, all configured environment variables and
`PATH` modifications for the provided tools are active.

### Choosing a shell [​](https://moonrepo.dev/docs/proto/commands/shell\#choosing-a-shell "Direct link to Choosing a shell")

By default, the current shell is detected and reused. To start a different shell, pass `--shell`
with the shell name.

```shell
$ proto shell node@20 --shell fish
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/shell\#arguments "Direct link to Arguments")

- `[tools...]` \- List of tool identifiers with optional version. If omitted, tools are inherited
from `.prototools` configs.

### Options [​](https://moonrepo.dev/docs/proto/commands/shell\#options "Direct link to Options")

- `--shell` \- Shell to start an interactive session for (e.g. `bash`, `pwsh`).

- [Choosing a shell](https://moonrepo.dev/docs/proto/commands/shell#choosing-a-shell)
- [Arguments](https://moonrepo.dev/docs/proto/commands/shell#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/shell#options)