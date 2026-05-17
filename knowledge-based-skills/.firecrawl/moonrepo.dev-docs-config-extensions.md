[Skip to main content](https://moonrepo.dev/docs/config/extensions#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.0.0

The `.moon/extensions.*` file configures extensions that can hook into pipeline events, or be
executed directly. This file is _optional_.

## `extends` [​](https://moonrepo.dev/docs/config/extensions\#extends "Direct link to extends")

Defines one or many external `.moon/extensions.*`'s to extend and inherit settings from. Perfect for
reusability and sharing configuration across repositories and projects. When defined, this setting
must be an HTTPS URL _or_ relative file system path that points to a valid YAML document!

.moon/extensions.yml

```yaml
extends: 'https://raw.githubusercontent.com/organization/repository/master/.moon/extensions.yml'
```

caution

Settings will be merged recursively for blocks, with values defined in the local configuration
taking precedence over those defined in the extended configuration.

## How it works [​](https://moonrepo.dev/docs/config/extensions\#how-it-works "Direct link to How it works")

A mapping of extensions that can be downloaded and executed with the [`moon ext`](https://moonrepo.dev/docs/commands/ext)
command. An extension is a WASM plugin, and the location of the WASM file must be defined with the
`plugin` field, which requires a
[plugin locator string](https://moonrepo.dev/docs/guides/wasm-plugins#configuring-plugin-locations).

.moon/extensions.yml

```yaml
example:
  plugin: 'file://./path/to/example.wasm'
  # or
  plugin: 'https://example.com/path/to/example.wasm'
```

Additionally, extensions support custom configuration that is passed to the WASM runtime when the
plugin is instantiated. This configuration is defined by inserting additional fields under the
extension name, relative to the `plugin` field. Each extension may have its own settings, so refer
to their documentation for more information.

.moon/extensions.yml

```yaml
example:
  plugin: 'file://./path/to/example.wasm'
  setting1: true
  setting2: 'abc'
```

## Supported extensions [​](https://moonrepo.dev/docs/config/extensions\#supported-extensions "Direct link to Supported extensions")

View the [official guide](https://moonrepo.dev/docs/guides/extensions) for all built-in extensions.

- [`extends`](https://moonrepo.dev/docs/config/extensions#extends)
- [How it works](https://moonrepo.dev/docs/config/extensions#how-it-works)
- [Supported extensions](https://moonrepo.dev/docs/config/extensions#supported-extensions)