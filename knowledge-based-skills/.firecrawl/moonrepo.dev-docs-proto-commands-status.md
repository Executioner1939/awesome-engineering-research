[Skip to main content](https://moonrepo.dev/docs/proto/commands/status#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.34.0

The `proto status` command will list all tools that are currently active for a target directory,
what versions of those tools are resolved to, and the configuration file in which they are defined.

```text
$ proto status
╭───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Tool      Configured Resolved  Installed                           Config                             │
│───────────────────────────────────────────────────────────────────────────────────────────────────────│
│ bun       1.1.42     1.1.42    /Users/name/.proto/tools/          /Users/name/.proto/.prototools      │
│                                bun/1.1.42                                                             │
│ deno      1.43.1     1.43.1    /Users/name/.proto/tools/          /Users/name/.proto/.prototools      │
│                                deno/1.43.1                                                            │
│ node      23.5.0     23.5.0    /Users/name/.proto/tools/          /Users/name/.proto/.prototools      │
│                                node/23.5.0                                                            │
│ npm       ~10.7      10.7.0    /Users/name/.proto/tools/          /Users/name/.proto/.prototools      │
│                                npm/10.7.0                                                             │
│ python    3.12.0     3.12.0    /Users/name/.proto/tools/          /Users/name/.proto/.prototools      │
│                                python/3.12.0                                                          │
│ yarn      3.6.3      3.6.3     /Users/name/.proto/tools/          /Users/name/.proto/.prototools      │
│                                yarn/3.6.3                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

> By default, this command _does not_ check tools for versions pinned in the global
> `~/.proto/.prototools` file. Pass `--config-mode all` to include them.

### Options [​](https://moonrepo.dev/docs/proto/commands/status\#options "Direct link to Options")

- `--json` \- Print the list in JSON format.

- [Options](https://moonrepo.dev/docs/proto/commands/status#options)