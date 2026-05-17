[Skip to main content](https://moonrepo.dev/docs/commands/ext#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.20.0

The `moon ext <id>` command will execute an extension (a WASM plugin) that has been configured in
[`.moon/extensions.*`](https://moonrepo.dev/docs/config). View our official [extensions guide](https://moonrepo.dev/docs/guides/extensions) for
more information.

```shell
$ moon ext download -- --url https://github.com/moonrepo/moon/archive/refs/tags/v1.19.3.zip
```

Extensions typically support command line arguments, which _must_ be passed after a `--` separator
(as seen above). Any arguments before the separator will be passed to the `moon ext` command itself.

caution

This command requires an internet connection if the extension's `.wasm` file must be downloaded from
a URL, and it hasn't been cached locally.

### Arguments [​](https://moonrepo.dev/docs/commands/ext\#arguments "Direct link to Arguments")

- `<id>` \- Name of the extension to execute.
- `[-- <args>]` \- Arguments to pass to the extension.

### Configuration [​](https://moonrepo.dev/docs/commands/ext\#configuration "Direct link to Configuration")

- [`*`](https://moonrepo.dev/docs/config/workspace#extensions) in `.moon/extensions.*`

- [Arguments](https://moonrepo.dev/docs/commands/ext#arguments)
- [Configuration](https://moonrepo.dev/docs/commands/ext#configuration)