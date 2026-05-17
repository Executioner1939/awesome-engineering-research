[Skip to main content](https://moonrepo.dev/docs/proto/commands/uninstall#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto uninstall <tool> [version]` (or `proto ui`) command will uninstall and remove a tool from
`~/.proto/tools/<tool>`. If the tool has not been installed, the command will exit early.

```shell
# Remove a specific version
$ proto uninstall deno 1.31

# Remove all versions
$ proto uninstall deno
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/uninstall\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.
- `[version]` \- Version of tool.

- [Arguments](https://moonrepo.dev/docs/proto/commands/uninstall#arguments)