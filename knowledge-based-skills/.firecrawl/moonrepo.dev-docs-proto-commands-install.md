[Skip to main content](https://moonrepo.dev/docs/proto/commands/install#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto install` (or `proto i`) command can be used to install one or many tools.

### Installing all toolsv0.39.0 [​](https://moonrepo.dev/docs/proto/commands/install\#installing-all-tools "Direct link to installing-all-tools")

The `proto install` command (without arguments) will download and install _all_ tools and plugins
from all parent [`.prototools`](https://moonrepo.dev/docs/proto/config) configuration files, and any
[versions detected](https://moonrepo.dev/docs/proto/detection) in the current working directory (if not defined in
`.prototools`).

```shell
$ proto install
```

> By default, this command _does not_ install tools for versions pinned in the global
> `~/.proto/.prototools` file. Pass `--config-mode all` to include them.

### Installing one tool [​](https://moonrepo.dev/docs/proto/commands/install\#installing-one-tool "Direct link to Installing one tool")

The `proto install <tool> [version]` command will download and install a single tool by unpacking
their archive to `~/.proto/tools/<tool>`. If the tool has already been installed, the command will
exit early.

The command is also smart enough to resolve partial versions, so 1, 1.2, and 1.2.3 are all
acceptable. It even supports aliases when applicable, like `latest`, `next`, `beta`, etc. To install
a canary release, use `canary`.

```shell
$ proto install deno
$ proto install deno 1.31
$ proto install deno canary
```

#### Pinning the version [​](https://moonrepo.dev/docs/proto/commands/install\#pinning-the-version "Direct link to Pinning the version")

By default this command will only install the tool into `~/.proto/tools` but will not make the
binary available. If you would like to also pin the resolved version to a `.prototools` file, use
the `--pin` option.

```shell
# ./.prototools
$ proto install bun --pin
$ proto install bun --pin local

# ~/.proto/.prototools
$ proto install bun --pin global

# ~/.prototools
$ proto install bun --pin user
```

### Handling plugin hooks [​](https://moonrepo.dev/docs/proto/commands/install\#handling-plugin-hooks "Direct link to Handling plugin hooks")

Some tools run [post-install hooks](https://moonrepo.dev/docs/proto/tools) that support arbitrary arguments that can be passed
after `--`.

```shell
$ proto install go -- --no-gobin
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/install\#arguments "Direct link to Arguments")

- One tool
  - `[tool]` \- Type of tool.
  - `[version]` \- Version of tool. Defaults to a pinned version in `.prototools` or "latest".
  - `[-- <args>]` \- Additional arguments to pass to post-install hooks.

### Options [​](https://moonrepo.dev/docs/proto/commands/install\#options "Direct link to Options")

- `--force` \- Force install, even if already installed.
- `--update-lockfile` \- Don't inherit a version from the lockfile and update the existing record.v0.51.0
- One tool
  - `--build` \- Build from source if available. v0.45.0
  - `--no-build` \- Download a pre-built if available. v0.45.0
  - `--pin` \- Pin the resolved version and create a symlink in `~/.proto/bin`. Accepts a boolean
    (pins locally by default), or the string "global", or the string "local".

- [Installing all tools](https://moonrepo.dev/docs/proto/commands/install#installing-all-tools)
- [Installing one tool](https://moonrepo.dev/docs/proto/commands/install#installing-one-tool)
  - [Pinning the version](https://moonrepo.dev/docs/proto/commands/install#pinning-the-version)
- [Handling plugin hooks](https://moonrepo.dev/docs/proto/commands/install#handling-plugin-hooks)
- [Arguments](https://moonrepo.dev/docs/proto/commands/install#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/install#options)