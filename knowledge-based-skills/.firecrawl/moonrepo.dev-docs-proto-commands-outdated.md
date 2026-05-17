[Skip to main content](https://moonrepo.dev/docs/proto/commands/outdated#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.19.0

The `proto outdated` command will load all [`.prototools`](https://moonrepo.dev/docs/proto/config) files and check for newer
(matching configured range) and latest versions of each configured tool. Will also include the
configuration file in which the version has been configured.

```text
$ proto outdated

╭───────────────────────────────────────────────────────────────────────╮
│ Tool      Current Newest  Latest  Config                              │
│───────────────────────────────────────────────────────────────────────│
│ bun       1.1.42  1.1.42  1.1.42  /Users/name/.proto/.prototools      │
│ node      23.5.0  23.5.0  23.5.0  /Users/name/.proto/.prototools      │
│ npm       10.7.0  10.7.0  11.0.0  /Users/name/.proto/.prototools      │
│ rust      1.83.0  1.83.0  1.83.0  /Users/name/.proto/.prototools      │
│ yarn      3.6.3   3.8.7   4.5.1   /Users/name/.proto/.prototools      │
╰───────────────────────────────────────────────────────────────────────╯
```

> By default, this command _does not_ check tools for versions pinned in the global
> `~/.proto/.prototools` file. Pass `--config-mode all` to include them.

### Options [​](https://moonrepo.dev/docs/proto/commands/outdated\#options "Direct link to Options")

- `--json` \- Print the list in JSON format.
- `--latest` \- When updating versions with `--update`, use the latest version instead of newest.
- `--update` \- Update and write newest/latest versions to their respective configuration.
- `--yes` \- Avoid and confirm all prompts. v0.44.0

- [Options](https://moonrepo.dev/docs/proto/commands/outdated#options)