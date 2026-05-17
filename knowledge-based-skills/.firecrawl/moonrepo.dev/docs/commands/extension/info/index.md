[Skip to main content](https://moonrepo.dev/docs/commands/extension/info#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.0.0

The `moon extension info <id> [plugin]` command will display detailed information about a extension.
To do this, the command will download the WASM plugin, extract information, and call specific
functions.

For built-in extensions, the \[plugin locator\]\[locator\] argument is optional, and will be derived
from the identifier.

```shell
$ moon extension info download
```

For third-party extensions, the \[plugin locator\]\[locator\] argument is required, and must point to
the WASM plugin.

```shell
$ moon extension info custom https://example.com/path/to/plugin.wasm
```

### Arguments [​](https://moonrepo.dev/docs/commands/extension/info\#arguments "Direct link to Arguments")

- `<id>` \- ID of the extension to view.
- `[plugin]` \- Optional \[plugin locator\]\[locator\] for third-party extensions.

## Example output [​](https://moonrepo.dev/docs/commands/extension/info\#example-output "Direct link to Example output")

```text
Extension ─────────────────────────────────────────────────────────────────

  Download a file from a URL into the current working directory.

  ID: download
  Title: Download
  Version: 1.0.0

APIs ──────────────────────────────────────────────────────────────────────

  ⚫️ define_extension_config
  🟢 execute_extension
  ⚫️ extend_command
  ⚫️ extend_project_graph
  ⚫️ extend_task_command
  ⚫️ extend_task_script
  ⚫️ initialize_extension
  🟢 register_extension (required)
  ⚫️ sync_project
  ⚫️ sync_workspace
```

- [Arguments](https://moonrepo.dev/docs/commands/extension/info#arguments)
- [Example output](https://moonrepo.dev/docs/commands/extension/info#example-output)