[Skip to main content](https://moonrepo.dev/docs/proto/commands/bin#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto bin <tool> [version]` command will return an absolute path to a tool's binary within the
toolchain. When a tool has not been installed, or a version cannot be resolved, the command will
exit with a failure.

```shell
$ proto bin node 16.10.0
/Users/example/.proto/tools/node/16.10.0/bin/node
```

This command can also return directories using the `--dir` option.

```shell
$ proto bin node 16.10.0 --dir exes
/Users/example/.proto/tools/node/16.10.0/bin

$ proto bin node 16.10.0 --dir globals
/Users/example/.proto/tools/node/globals/bin
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/bin\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.
- `[version]` \- Version of tool. If not provided, will attempt to
[detect the version](https://moonrepo.dev/docs/proto/detection).

### Options [​](https://moonrepo.dev/docs/proto/commands/bin\#options "Direct link to Options")

- `--all` \- Return multiple paths, separated by newlines, instead of the first path.v0.50.0
- `--dir <dir>` \- Return a directory instead of of the main file. v0.50.0
  - `exes` \- Returns the executable's directory.
  - `globals` \- Returns the globals/packages directory.
- `--bin` \- When applicable, return the `~/.proto/bin` path.
- `--shim` \- When applicable, return the `~/.proto/shims` path.

- [Arguments](https://moonrepo.dev/docs/proto/commands/bin#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/bin#options)