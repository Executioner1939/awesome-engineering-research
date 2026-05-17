[Skip to main content](https://moonrepo.dev/docs/commands/extension/add#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.0.0

The `moon extension add <id> [plugin]` command will add a extension to the workspace by injecting a
configuration block into `.moon/extensions.*`. To do this, the command will download the WASM
plugin, extract information, and call initialize functions.

For built-in extensions, the [plugin locator](https://moonrepo.dev/docs/guides/wasm-plugins#configuring-plugin-locations) argument is optional, and will be derived
from the identifier.

```shell
$ moon extension add download
```

For third-party extensions, the [plugin locator](https://moonrepo.dev/docs/guides/wasm-plugins#configuring-plugin-locations) argument is required, and must point to
the WASM plugin.

```shell
$ moon extension add custom https://example.com/path/to/plugin.wasm
```

### Arguments [​](https://moonrepo.dev/docs/commands/extension/add\#arguments "Direct link to Arguments")

- `<id>` \- ID of the extension to use.
- `[plugin]` \- Optional [plugin locator](https://moonrepo.dev/docs/guides/wasm-plugins#configuring-plugin-locations) for third-party extensions.

### Options [​](https://moonrepo.dev/docs/commands/extension/add\#options "Direct link to Options")

- `--minimal` \- Generate minimal configurations and sane defaults.
- `--yes` \- Skip all prompts and enables tools based on file detection.

- [Arguments](https://moonrepo.dev/docs/commands/extension/add#arguments)
- [Options](https://moonrepo.dev/docs/commands/extension/add#options)