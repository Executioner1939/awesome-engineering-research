[Skip to main content](https://moonrepo.dev/docs/config/toolchain#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `.moon/toolchains.*` file configures the toolchain and the workspace development environment.
This file is _optional_.

Managing tool version's within the toolchain ensures a deterministic environment across any machine
(whether a developer, CI, or production machine).

## `extends` [​](https://moonrepo.dev/docs/config/toolchain\#extends "Direct link to extends")

Defines one or many external `.moon/toolchains.*`'s to extend and inherit settings from. Perfect for
reusability and sharing configuration across repositories and projects. When defined, this setting
must be an HTTPS URL _or_ relative file system path that points to a valid YAML document!

.moon/toolchains.yml

```yaml
extends: 'https://raw.githubusercontent.com/organization/repository/master/.moon/toolchains.yml'
```

caution

Settings will be merged recursively for blocks, with values defined in the local configuration
taking precedence over those defined in the extended configuration.

## `moon`v1.29.0 [​](https://moonrepo.dev/docs/config/toolchain\#moon "Direct link to moon")

Configures how moon will receive information about latest releases and download locations.

### `manifestUrl` [​](https://moonrepo.dev/docs/config/toolchain\#manifesturl "Direct link to manifesturl")

Defines an HTTPS URL in which to fetch the current version information from.

.moon/toolchains.yml

```yaml
moon:
  manifestUrl: 'https://proxy.corp.net/moon/version'
```

### `downloadUrl` [​](https://moonrepo.dev/docs/config/toolchain\#downloadurl "Direct link to downloadurl")

Defines an HTTPS URL in which the moon binary can be downloaded from. The download file name is
hard-coded and will be appended to the provided URL.

Defaults to downloading from GitHub: [https://github.com/moonrepo/moon/releases](https://github.com/moonrepo/moon/releases)

.moon/toolchains.yml

```yaml
moon:
  downloadUrl: 'https://github.com/moonrepo/moon/releases/latest/download'
```

## `proto`v1.39.0 [​](https://moonrepo.dev/docs/config/toolchain\#proto "Direct link to proto")

Configures how moon integrates with and utilizes [proto](https://moonrepo.dev/proto).

### `version` [​](https://moonrepo.dev/docs/config/toolchain\#version "Direct link to version")

The version of proto to install and run toolchains with. If proto or this version of proto has not
been installed yet, it will be installed automatically when running a task.

.moon/toolchains.yml

```yaml
proto:
  version: '0.51.0'
```

## Shared [​](https://moonrepo.dev/docs/config/toolchain\#shared "Direct link to Shared")

The following settings are available and shared across all toolchains. Run
`moon toolchain info <toolchain>` for all available settings for a specific toolchain.

### `inheritAliases`v2.1.0 [​](https://moonrepo.dev/docs/config/toolchain\#inheritaliases "Direct link to inheritaliases")

When enabled, will inherit [aliases for projects](https://moonrepo.dev/docs/concepts/project#aliases) while the toolchain
is extending the project graph. An alias is typically derived from a `name` field in a toolchain
manifest file (`package.json`, `Cargo.toml`, etc). Defaults to `true`.

.moon/toolchains.yml

```yaml
javascript:
  inheritAliases: false
```

### `installDependencies`v2.1.0 [​](https://moonrepo.dev/docs/config/toolchain\#installdependencies "Direct link to installdependencies")

When enabled and running a task, will automatically install toolchain dependencies if the lockfile,
manifest, or environment has changed changed since the last run. This is achieved through the
[`InstallDependencies` action](https://moonrepo.dev/docs/how-it-works/action-graph). Defaults to `true`.

.moon/toolchains.yml

```yaml
javascript:
  installDependencies: false
```

### `plugin` [​](https://moonrepo.dev/docs/config/toolchain\#plugin "Direct link to plugin")

Configures the location of the `.wasm` plugin file that moon will use to run this toolchain.
Supports `file://` (relative from `.moon`), `https://`, and `github://` protocols.
[Learn more about plugin locators](https://moonrepo.dev/docs/guides/wasm-plugins#configuring-plugin-locations).

.moon/toolchains.yml

```yaml
custom-toolchain:
  plugin: 'file://../path/to/plugin.wasm'
```

> This field is not required for built-in toolchains. However, it can be configured to override the
> built-in plugin if you want to use your own implementation.

### `versionFromPrototools`v2.0.0 [​](https://moonrepo.dev/docs/config/toolchain\#versionfromprototools "Direct link to versionfromprototools")

When a toolchain supports the `version` setting, this setting controls whether the version will be
inherited from the root `.prototools` configuration file. This is useful for sharing a single
version across multiple toolchains, and only having to update it in one place.

When `false`, doesn't inherit a version. When `true`, matches the version specified in `.prototools`
using the same toolchain identifier. Otherwise a string can be provided to specify a proto-specific
identifier. Defaults to `true`.

.moon/toolchains.yml

```yaml
node:
  versionFromPrototools: 'nodejs'
```

.prototools

```toml
nodejs = "~24"
```

## Go [​](https://moonrepo.dev/docs/config/toolchain\#go "Direct link to Go")

## `go` [​](https://moonrepo.dev/docs/config/toolchain\#go-1 "Direct link to go-1")

Run `moon toolchain info go` for all available settings.

## JavaScript [​](https://moonrepo.dev/docs/config/toolchain\#javascript "Direct link to JavaScript")

## `javascript` [​](https://moonrepo.dev/docs/config/toolchain\#javascript-1 "Direct link to javascript-1")

Run `moon toolchain info javascript` for all available settings.

## `bun` [​](https://moonrepo.dev/docs/config/toolchain\#bun "Direct link to bun")

Run `moon toolchain info bun` for all available settings.

info

This toolchain requires the [`javascript`](https://moonrepo.dev/docs/config/toolchain#javascript) toolchain to also be enabled.

## `deno` [​](https://moonrepo.dev/docs/config/toolchain\#deno "Direct link to deno")

Run `moon toolchain info deno` for all available settings.

info

This toolchain requires the [`javascript`](https://moonrepo.dev/docs/config/toolchain#javascript) toolchain to also be enabled.

## `node` [​](https://moonrepo.dev/docs/config/toolchain\#node "Direct link to node")

Run `moon toolchain info node` for all available settings.

info

This toolchain requires the [`javascript`](https://moonrepo.dev/docs/config/toolchain#javascript) toolchain to also be enabled.

## `npm` [​](https://moonrepo.dev/docs/config/toolchain\#npm "Direct link to npm")

Run `moon toolchain info npm` for all available settings.

info

This toolchain requires the [`node`](https://moonrepo.dev/docs/config/toolchain#node) toolchain to also be enabled.

## `pnpm` [​](https://moonrepo.dev/docs/config/toolchain\#pnpm "Direct link to pnpm")

Run `moon toolchain info pnpm` for all available settings.

info

This toolchain requires the [`node`](https://moonrepo.dev/docs/config/toolchain#node) toolchain to also be enabled.

## `yarn` [​](https://moonrepo.dev/docs/config/toolchain\#yarn "Direct link to yarn")

Run `moon toolchain info yarn` for all available settings.

info

This toolchain requires the [`node`](https://moonrepo.dev/docs/config/toolchain#node) toolchain to also be enabled.

## `typescript` [​](https://moonrepo.dev/docs/config/toolchain\#typescript "Direct link to typescript")

Run `moon toolchain info typescript` for all available settings.

## Python [​](https://moonrepo.dev/docs/config/toolchain\#python "Direct link to Python")

## `unstable_python` [​](https://moonrepo.dev/docs/config/toolchain\#unstable_python "Direct link to unstable_python")

Run `moon toolchain info unstable_python` for all available settings.

## `unstable_pip` [​](https://moonrepo.dev/docs/config/toolchain\#unstable_pip "Direct link to unstable_pip")

Run `moon toolchain info unstable_pip` for all available settings.

info

This toolchain requires the [`unstable_python`](https://moonrepo.dev/docs/config/toolchain#unstable_python) toolchain to also be enabled.

## `unstable_uv` [​](https://moonrepo.dev/docs/config/toolchain\#unstable_uv "Direct link to unstable_uv")

Run `moon toolchain info unstable_uv` for all available settings.

info

This toolchain requires the [`unstable_python`](https://moonrepo.dev/docs/config/toolchain#unstable_python) toolchain to also be enabled.

## Rust [​](https://moonrepo.dev/docs/config/toolchain\#rust "Direct link to Rust")

## `rust` [​](https://moonrepo.dev/docs/config/toolchain\#rust-1 "Direct link to rust-1")

Run `moon toolchain info rust` for all available settings.

- [`extends`](https://moonrepo.dev/docs/config/toolchain#extends)
- [`moon`](https://moonrepo.dev/docs/config/toolchain#moon)
  - [`manifestUrl`](https://moonrepo.dev/docs/config/toolchain#manifesturl)
  - [`downloadUrl`](https://moonrepo.dev/docs/config/toolchain#downloadurl)
- [`proto`](https://moonrepo.dev/docs/config/toolchain#proto)
  - [`version`](https://moonrepo.dev/docs/config/toolchain#version)
- [Shared](https://moonrepo.dev/docs/config/toolchain#shared)
  - [`inheritAliases`](https://moonrepo.dev/docs/config/toolchain#inheritaliases)
  - [`installDependencies`](https://moonrepo.dev/docs/config/toolchain#installdependencies)
  - [`plugin`](https://moonrepo.dev/docs/config/toolchain#plugin)
  - [`versionFromPrototools`](https://moonrepo.dev/docs/config/toolchain#versionfromprototools)
- [Go](https://moonrepo.dev/docs/config/toolchain#go)
- [`go`](https://moonrepo.dev/docs/config/toolchain#go-1)
- [JavaScript](https://moonrepo.dev/docs/config/toolchain#javascript)
- [`javascript`](https://moonrepo.dev/docs/config/toolchain#javascript-1)
- [`bun`](https://moonrepo.dev/docs/config/toolchain#bun)
- [`deno`](https://moonrepo.dev/docs/config/toolchain#deno)
- [`node`](https://moonrepo.dev/docs/config/toolchain#node)
- [`npm`](https://moonrepo.dev/docs/config/toolchain#npm)
- [`pnpm`](https://moonrepo.dev/docs/config/toolchain#pnpm)
- [`yarn`](https://moonrepo.dev/docs/config/toolchain#yarn)
- [`typescript`](https://moonrepo.dev/docs/config/toolchain#typescript)
- [Python](https://moonrepo.dev/docs/config/toolchain#python)
- [`unstable_python`](https://moonrepo.dev/docs/config/toolchain#unstable_python)
- [`unstable_pip`](https://moonrepo.dev/docs/config/toolchain#unstable_pip)
- [`unstable_uv`](https://moonrepo.dev/docs/config/toolchain#unstable_uv)
- [Rust](https://moonrepo.dev/docs/config/toolchain#rust)
- [`rust`](https://moonrepo.dev/docs/config/toolchain#rust-1)