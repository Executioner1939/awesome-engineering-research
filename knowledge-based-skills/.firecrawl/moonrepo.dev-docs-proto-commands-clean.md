[Skip to main content](https://moonrepo.dev/docs/proto/commands/clean#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto clean` command can be used to uninstall stale and unused tools, plugins, and more. By
default, it will remove items that haven't been used in the last 30 days.

```shell
$ proto clean
```

Furthermore, the command can be used to target a specific artifact type.

```shell
$ proto clean plugins
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/clean\#arguments "Direct link to Arguments")

- `[target]` \- Type of target. Accepts `cache`, `plugins`, `temp`, or `tools`.v0.44.0

### Options [​](https://moonrepo.dev/docs/proto/commands/clean\#options "Direct link to Options")

- `--days` \- Number of days before a tool is considered stale.
- `--json` \- Print the clean result in JSON format. v0.44.0
- `--yes` \- Avoid and confirm all prompts.

- [Arguments](https://moonrepo.dev/docs/proto/commands/clean#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/clean#options)