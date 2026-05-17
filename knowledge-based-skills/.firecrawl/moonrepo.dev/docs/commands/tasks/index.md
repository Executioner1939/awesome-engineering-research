[Skip to main content](https://moonrepo.dev/docs/commands/tasks#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.0.0

The `moon tasks` command will list all tasks available in the workspace as a table of information.

```shell
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│Task                          Command          Type        Preset      Toolchains                                Description                                                           │
│───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────│
│website:build                 docusaurus       build                   typescript, javascript, node, yarn        Builds the Docusaurus app.                                            │
│website:format                prettier         test                    javascript, node, yarn                                                                                          │
│website:format-write          prettier         test                    javascript, node, yarn                                                                                          │
│website:lint                  eslint           test                    javascript, node, yarn                                                                                          │
│website:lint-fix              eslint           test                    javascript, node, yarn                                                                                          │
│website:start                 docusaurus       run         server      typescript, javascript, node, yarn                                                                              │
│website:test                  jest             test                    javascript, node, yarn                                                                                          │
│website:typecheck             tsc              test                    typescript, javascript, node, yarn                                                                              │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

info

Use [`moon query tasks`](https://moonrepo.dev/docs/commands/query/tasks) for advanced querying and filtering of tasks.

### Arguments [​](https://moonrepo.dev/docs/commands/tasks\#arguments "Direct link to Arguments")

- `[id]` \- Filter tasks to a specific project ID.

### Options [​](https://moonrepo.dev/docs/commands/tasks\#options "Direct link to Options")

- `--json` \- Print the projects as JSON.

- [Arguments](https://moonrepo.dev/docs/commands/tasks#arguments)
- [Options](https://moonrepo.dev/docs/commands/tasks#options)