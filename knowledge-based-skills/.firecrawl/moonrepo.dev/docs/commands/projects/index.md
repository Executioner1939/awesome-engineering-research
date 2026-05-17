[Skip to main content](https://moonrepo.dev/docs/commands/projects#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.0.0

The `moon projects` command will list all projects configured in the workspace as a table of
information.

```shell
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│Project          Source                    Stack             Layer             Toolchains                                Description                                                   │
│───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────│
│types            packages/types            frontend          library           javascript, node, typescript, yarn                                                                      │
│website          website                   frontend          application       javascript, node, typescript, yarn        A static website powered by Docusaurus.                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

info

Use [`moon query projects`](https://moonrepo.dev/docs/commands/query/projects) for advanced querying and filtering of projects.

### Options [​](https://moonrepo.dev/docs/commands/projects\#options "Direct link to Options")

- `--json` \- Print the projects as JSON.

- [Options](https://moonrepo.dev/docs/commands/projects#options)