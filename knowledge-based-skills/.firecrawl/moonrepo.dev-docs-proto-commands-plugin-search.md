[Skip to main content](https://moonrepo.dev/docs/proto/commands/plugin/search#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.36.0

The `proto plugin search <query>` command will search for plugins provided by the community, based
on the provided query string. Built-in plugins _are not_ searchable.

```text
$ proto plugin search moon

Search results for: moon
Learn more about plugins: https://moonrepo.dev/docs/proto/plugins
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Plugin      Author    Format Description             Locator                                                             │
│──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────│
│ moon        moonrepo  TOML   moon is a multi-        https://raw.githubusercontent.com/moonrepo/moon/master/proto-       │
│                              language build system   plugin.toml                                                         │
│                              and codebase management                                                                     │
│                              tool.                                                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/plugin/search\#arguments "Direct link to Arguments")

- `<query>` \- Query string to match against.

### Options [​](https://moonrepo.dev/docs/proto/commands/plugin/search\#options "Direct link to Options")

- `--json` \- Print the results in JSON format.

- [Arguments](https://moonrepo.dev/docs/proto/commands/plugin/search#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/plugin/search#options)