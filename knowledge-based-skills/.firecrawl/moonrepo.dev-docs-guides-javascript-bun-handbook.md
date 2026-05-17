[Skip to main content](https://moonrepo.dev/docs/guides/javascript/bun-handbook#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Utilizing JavaScript (and TypeScript) in a monorepo can be a daunting task, especially when using
Bun (or Node.js), as there are many ways to structure your code and to configure your tools. With
this handbook, we'll help guide you through this process.

info

This guide is a living document and will continue to be updated over time!

## moon setup [​](https://moonrepo.dev/docs/guides/javascript/bun-handbook\#moon-setup "Direct link to moon setup")

For this part of the handbook, we'll be focusing on [moon](https://moonrepo.dev/moon), our task runner. To start,
languages in moon act like plugins, where their functionality and support _is not_ enabled unless
explicitly configured. We follow this approach to avoid unnecessary overhead.

### Enabling the language [​](https://moonrepo.dev/docs/guides/javascript/bun-handbook\#enabling-the-language "Direct link to Enabling the language")

To enable JavaScript support via Bun, define the [`bun`](https://moonrepo.dev/docs/config/toolchain#bun) setting in
[`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain), even if an empty object. The
[`javascript`](https://moonrepo.dev/docs/config/toolchain#javascript) toolchain must also be enabled, and configured to
use Bun as the package manager.

.moon/toolchains.yml

```yaml
# Enable JavaScript
javascript:
  packageManager: 'bun'

# Enable Bun
bun: {}
```

Or by pinning a `bun` version in [`.prototools`](https://moonrepo.dev/docs/proto/config) in the workspace root.

.prototools

```toml
bun = "1.0.0"
```

This will enable the JavaScript and Bun toolchains and provide the following automations around its
ecosystem:

- Node modules will automatically be installed if dependencies in `package.json` have changed, or
the lockfile has changed, since the last time a task has ran.
  - We'll also take `package.json` workspaces into account and install modules in the correct
    location; either the workspace root, in a project, or both.
- Relationships between projects will automatically be discovered based on `dependencies`,
`devDependencies`, and `peerDependencies` in `package.json`.

### Utilizing the toolchain [​](https://moonrepo.dev/docs/guides/javascript/bun-handbook\#utilizing-the-toolchain "Direct link to Utilizing the toolchain")

When a language is enabled, moon by default will assume that the language's binary is available
within the current environment (typically on `PATH`). This has the downside of requiring all
developers and machines to manually install the correct version of the language, _and to stay in_
_sync_.

Instead, you can utilize [moon's toolchain](https://moonrepo.dev/docs/concepts/toolchain), which will download and
install the language in the background, and ensure every task is executed using the exact version
across all machines.

Enabling the toolchain is as simple as defining the [`bun.version`](https://moonrepo.dev/docs/config/toolchain#version)
setting.

.moon/toolchains.yml

```yaml
# Enable Bun toolchain with an explicit version
bun:
  version: '1.0.0'
```

> Versions can also be defined with [`.prototools`](https://moonrepo.dev/docs/proto/config).

### Configuring the toolchain [​](https://moonrepo.dev/docs/guides/javascript/bun-handbook\#configuring-the-toolchain "Direct link to Configuring the toolchain")

Since the JavaScript ecosystem supports multiple runtimes, moon is unable to automatically detect
the correct runtime for all scenarios. Does the existence of a `package.json` mean Node.js or Bun?
We don't know, and default to Node.js because of its popularity.

To work around this, you can set `toolchain` to "bun" at the task-level or project-level.

moon.yml

```yaml
# For all tasks in the project
toolchains:
  default: ['javascript', 'bun']

tasks:
  build:
    command: 'webpack'
    # For this specific task
    toolchains: ['javascript', 'bun']
```

> The task-level `toolchains.default` only needs to be set if executing a `node_modules` binary! The
> `bun` binary automatically sets the toolchain to Bun.

### Using `package.json` scripts [​](https://moonrepo.dev/docs/guides/javascript/bun-handbook\#using-packagejson-scripts "Direct link to using-packagejson-scripts")

If you're looking to prototype moon, or reduce the migration effort to moon tasks, you can configure
moon to inherit `package.json` scripts, and internally convert them to moon tasks. This can be
achieved with the [`javascript.inferTasksFromScripts`](https://moonrepo.dev/docs/config/toolchain#infertasksfromscripts)
setting.

.moon/toolchains.yml

```yaml
javascript:
  inferTasksFromScripts: true
```

Or you can run scripts through `bun run` calls.

moon.yml

```yaml
tasks:
  build:
    command: 'bun run build'
```

## Handbook [​](https://moonrepo.dev/docs/guides/javascript/bun-handbook\#handbook "Direct link to Handbook")

info

Refer to the [Node.js handbook](https://moonrepo.dev/docs/guides/javascript/node-handbook) for more information on repository structure,
dependency management, and more. Since both runtimes are extremely similar, the information in that
handbook also applies to Bun!

- [moon setup](https://moonrepo.dev/docs/guides/javascript/bun-handbook#moon-setup)
  - [Enabling the language](https://moonrepo.dev/docs/guides/javascript/bun-handbook#enabling-the-language)
  - [Utilizing the toolchain](https://moonrepo.dev/docs/guides/javascript/bun-handbook#utilizing-the-toolchain)
  - [Configuring the toolchain](https://moonrepo.dev/docs/guides/javascript/bun-handbook#configuring-the-toolchain)
  - [Using `package.json` scripts](https://moonrepo.dev/docs/guides/javascript/bun-handbook#using-packagejson-scripts)
- [Handbook](https://moonrepo.dev/docs/guides/javascript/bun-handbook#handbook)