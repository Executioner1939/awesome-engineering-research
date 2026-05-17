[Skip to main content](https://moonrepo.dev/docs/how-it-works/languages#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Although moon is currently focusing on the JavaScript ecosystem, our long-term vision is to be a
multi-language task runner and monorepo management tool. To that end, our languages (known as
toolchains) are implemented as WASM plugins, where their functionality is implemented in isolation,
and is _opt-in_.

## Enabling a language [​](https://moonrepo.dev/docs/how-it-works/languages\#enabling-a-language "Direct link to Enabling a language")

moon [supported languages](https://moonrepo.dev/docs/#supported-languages) are opt-in, and _are not_ enabled by default. We
chose this pattern to avoid unnecessary overhead, especially for the future when we have 10 or more
built-in languages.

To enable a supported language, simply define a configuration block with the language's name in
[`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain). Even an empty block will enable the language.

.moon/toolchains.yml

```yaml
# Enable JavaScript
javascript: {}

# Enable JavaScript with custom settings
javascript:
  packageManager: 'pnpm'

# Enable TypeScript
typescript: {}
```

## System language and toolchain [​](https://moonrepo.dev/docs/how-it-works/languages\#system-language-and-toolchain "Direct link to System language and toolchain")

When working with moon, you'll most likely have tasks that run built-in system commands that do not
belong to any of the supported languages. For example, you may have a task that runs `git` or
`docker` commands, or common commands like `rm`, `cp`, `mv`, etc.

For these cases, moon provides a special language/toolchain called `system`, that is always enabled.
This toolchain is a catch-all, an escape-hatch, a fallback, and provides the following:

- Runs a system command or a binary found on `PATH`.
- Wraps the execution in a shell.

To run system commands, set a task's [`toolchain`](https://moonrepo.dev/docs/config/project#toolchain) setting to "system".

moon.yml

```yaml
tasks:
  example:
    command: 'git status'
    toolchain: 'system'
```

## Tier structure and responsibilities [​](https://moonrepo.dev/docs/how-it-works/languages\#tier-structure-and-responsibilities "Direct link to Tier structure and responsibilities")

As mentioned in our introduction,
[language support is divided up into tiers](https://moonrepo.dev/docs/#supported-languages), where each tier introduces
more internal integrations and automations, but requires more work to properly implement.

### Tier 0 = Unsupported [​](https://moonrepo.dev/docs/how-it-works/languages\#tier-0--unsupported "Direct link to Tier 0 = Unsupported")

The zero tier represents all languages _not directly_ supported by moon. This tier merely exists as
a mechanism for running non-supported language binaries via the
[system toolchain](https://moonrepo.dev/docs/how-it-works/languages#system-language-and-toolchain).

moon.yml

```yaml
tasks:
  example:
    command: 'ruby'
    toolchain: 'system'
```

### Tier 1 = Language [​](https://moonrepo.dev/docs/how-it-works/languages\#tier-1--language "Direct link to Tier 1 = Language")

The first tier is the language itself. This is the most basic level of support, and is the only tier
that is required to be implemented for a language to be considered minimally supported. This tier is
in charge of:

- Declaring metadata about the language. For example, the name of the binary, supported file
extensions, available dependency/package/version managers, names of config/manifest/lock files,
etc.
- Mechanisms for detecting the language of a project based on config files and other criteria.
- Maps to a project's [`language`](https://moonrepo.dev/docs/config/project#language) setting.
- Supports a configuration block by name in [`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain).

moon.yml

```yaml
language: 'javascript'
```

### Tier 2 = Ecosystem [​](https://moonrepo.dev/docs/how-it-works/languages\#tier-2--ecosystem "Direct link to Tier 2 = Ecosystem")

The second tier requires the language functionality from tier 1, and eventually the toolchain
functionality from tier 3, and provides interoperability with moon's internals. This is the most
complex of all tiers, and the tier is in charge of:

- Determining when, where, and how to install dependencies for a project or the workspace.
- Loading project aliases and inferring implicit relationships between projects.
- Syncing a project and ensuring a healthy project state.
- Hashing efficiently for dependency installs and target runs.
- Helpers for parsing lockfiles and manifest files, and interacting with the language's ecosystem
(for example, Node.js module resolution).
- Prepending `PATH` with appropriate lookups to execute a task.
- Running a target's command with proper arguments, environment variables, and flags.
- Maps to a project's [`toolchains.default`](https://moonrepo.dev/docs/config/project#toolchain-1) or task's
[`toolchains`](https://moonrepo.dev/docs/config/project#toolchain) setting.

moon.yml

```yaml
tasks:
  example:
    command: 'webpack'
    toolchain: 'node'
```

.moon/toolchains.yml

```yaml
javascript: {}
node: {}
```

### Tier 3 = Toolchain [​](https://moonrepo.dev/docs/how-it-works/languages\#tier-3--toolchain "Direct link to Tier 3 = Toolchain")

The third tier is toolchain support via [proto](https://moonrepo.dev/proto). This is the final tier, as the toolchain is
unusable unless the platform has been entirely integrated, and as such, the platform depends on this
tier. This tier handles:

- Downloading and installing a language into the toolchain.
- Installing and deduping project dependencies.
- Detecting appropriate versions of tools to use.
- Determining which binary to use and execute targets with.
- Supports a `version` field in the named configuration block in
[`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain).

.moon/toolchains.yml

```yaml
node:
  version: '18.0.0'
```

- [Enabling a language](https://moonrepo.dev/docs/how-it-works/languages#enabling-a-language)
- [System language and toolchain](https://moonrepo.dev/docs/how-it-works/languages#system-language-and-toolchain)
- [Tier structure and responsibilities](https://moonrepo.dev/docs/how-it-works/languages#tier-structure-and-responsibilities)
  - [Tier 0 = Unsupported](https://moonrepo.dev/docs/how-it-works/languages#tier-0--unsupported)
  - [Tier 1 = Language](https://moonrepo.dev/docs/how-it-works/languages#tier-1--language)
  - [Tier 2 = Ecosystem](https://moonrepo.dev/docs/how-it-works/languages#tier-2--ecosystem)
  - [Tier 3 = Toolchain](https://moonrepo.dev/docs/how-it-works/languages#tier-3--toolchain)