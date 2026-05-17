[Skip to main content](https://moonrepo.dev/docs/proto/plugins#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

proto supports a pluggable architecture as a means for consumers to integrate and manage custom
tools (languages, CLIs, etc) within proto's toolchain. It's not possible for proto to support
_everything_ in core directly, so plugins are a way for the community to extend the toolchain to
their needs.

## Enabling plugins [​](https://moonrepo.dev/docs/proto/plugins\#enabling-plugins "Direct link to Enabling plugins")

Plugins can be enabled by configuring them in [`.prototools`](https://moonrepo.dev/docs/proto/config#plugins) files, within the
`[plugins]` section. The map key is the plugin name _in kebab-case_, which is used as the
binary/tool name in proto, and also the name for configuration and cache purposes. The map value is
a [plugin locator string](https://moonrepo.dev/docs/guides/wasm-plugins#configuring-plugin-locations) that defines a
protocol and source location.

.prototools

```toml
[plugins.tools]
<id> = "<protocol>://<location>"
```

## Creating plugins [​](https://moonrepo.dev/docs/proto/plugins\#creating-plugins "Direct link to Creating plugins")

To ease the plugin development process, proto supports 2 types of plugins, a
[non-WASM configuration based plugin](https://moonrepo.dev/docs/proto/non-wasm-plugin) for basic use cases, and a
[WASM based plugin](https://moonrepo.dev/docs/proto/wasm-plugin) for advanced use cases.

## Publish a plugin [​](https://moonrepo.dev/docs/proto/plugins\#publish-a-plugin "Direct link to Publish a plugin")

proto's registry is currently powered by static JSON files located in our official
[proto repository](https://github.com/moonrepo/proto/tree/master/registry). View that link for
information on how to publish a plugin.

- [Enabling plugins](https://moonrepo.dev/docs/proto/plugins#enabling-plugins)
- [Creating plugins](https://moonrepo.dev/docs/proto/plugins#creating-plugins)
- [Publish a plugin](https://moonrepo.dev/docs/proto/plugins#publish-a-plugin)