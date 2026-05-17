[Skip to main content](https://moonrepo.dev/docs/proto/commands/exec#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.53.0

The `proto exec <tools...> -- <command>` (or `proto x`) command will activate a temporary
environment by loading and initializing any number of tools, and then execute an arbitrary command
within that environment.

```shell
$ proto exec node pnpm -- pnpm run dev
```

Tools will automatically detect a version to execute with based on loaded `.prototools`, but the
version can be provided inline by suffixing the tool with `@<version>`.

```shell
$ proto exec node@24.2 pnpm@10 -- pnpm run dev
```

### Shell support [​](https://moonrepo.dev/docs/proto/commands/exec\#shell-support "Direct link to Shell support")

By default, the command will not be executed in a shell, and will be excuted in the context of the
parent process. If you want to execute the command within a shell (using `-c`), you can use the
`--shell` option.

```shell
$ proto exec node pnpm --shell bash -- <command>
```

If your command contains special characters, complex expressions, or shell specific syntax, you may
need to pass `--raw` to avoid quoting/escaping issues.

```shell
$ proto exec node pnpm --shell bash --raw -- <command>
```

Furthermore, if you want to launch an interactive shell session with the activated environment, you
can pass the shell command itself as the exec command.

```shell
$ proto exec node pnpm -- bash
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/exec\#arguments "Direct link to Arguments")

- `<tools...>` \- List of tool identifiers with optional version.
- `<command>` \- Command to execute within the environment. Must be passed after a `--` separator.

### Options [​](https://moonrepo.dev/docs/proto/commands/exec\#options "Direct link to Options")

- `--tools-from-config` \- Inherit tools to initialize from `.prototools` configs, instead of passing
an explicit list.
- `--raw` \- Execute the command as-is without quoting or escaping when using `--shell`.
- `--shell` \- Shell to execute the command with (e.g. `bash` or `pwsh`).

- [Shell support](https://moonrepo.dev/docs/proto/commands/exec#shell-support)
- [Arguments](https://moonrepo.dev/docs/proto/commands/exec#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/exec#options)