[Skip to main content](https://moonrepo.dev/docs/commands/query/tasks#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Use the `moon query tasks` sub-command to query task information for all projects in the project
graph. The tasks list can be filtered by passing a [query statement](https://moonrepo.dev/docs/concepts/query-lang) as
an argument, or by using [options](https://moonrepo.dev/docs/commands/query/tasks#options) arguments.

```shell
# Find all tasks grouped by project
$ moon query tasks

# Find all tasks from projects with an id that matches "react"
$ moon query tasks --id react
$ moon query tasks "task~react"
```

This will output a list of projects as JSON. The output has the following structure:

```ts
{
	tasks: Record<string, Record<string, Task>>,
	options: QueryOptions,
}
```

### Arguments [​](https://moonrepo.dev/docs/commands/query/tasks\#arguments "Direct link to Arguments")

- `[query]` \- An optional [query statement](https://moonrepo.dev/docs/concepts/query-lang) to filter projects with. When
provided, all [filter options](https://moonrepo.dev/docs/commands/query/tasks#filters) are ignored. v1.4.0

### Options [​](https://moonrepo.dev/docs/commands/query/tasks\#options "Direct link to Options")

#### Affected [​](https://moonrepo.dev/docs/commands/query/tasks\#affected "Direct link to Affected")

- `--affected` \- Filter tasks that have been affected by changed files.
- `--downstream` \- Include downstream dependents of queried tasks. Supports "none" (default),
"direct", "deep".v1.30.0
- `--upstream` \- Include upstream dependencies of queried tasks. Supports "none", "direct", "deep"
(default).v1.30.0

#### Filtersv1.30.0 [​](https://moonrepo.dev/docs/commands/query/tasks\#filters "Direct link to filters")

All option values are case-insensitive regex patterns.

- `--command <regex>` \- Filter tasks that match this command.
- `--id <regex>` \- Filter tasks that match this ID.
- `--project <regex>` \- Filter tasks that belong to this project.
- `--script <regex>` \- Filter tasks that match this script.
- `--toolchain <regex>` \- Filter tasks of this toolchain. v1.31.0
- `--type <regex>` \- Filter tasks of this type.

### Configuration [​](https://moonrepo.dev/docs/commands/query/tasks\#configuration "Direct link to Configuration")

- [`projects`](https://moonrepo.dev/docs/config/workspace#projects) in `.moon/workspace.*`
- [`tasks`](https://moonrepo.dev/docs/config/project#tasks) in `moon.*`

- [Arguments](https://moonrepo.dev/docs/commands/query/tasks#arguments)
- [Options](https://moonrepo.dev/docs/commands/query/tasks#options)
  - [Affected](https://moonrepo.dev/docs/commands/query/tasks#affected)
  - [Filters](https://moonrepo.dev/docs/commands/query/tasks#filters)
- [Configuration](https://moonrepo.dev/docs/commands/query/tasks#configuration)