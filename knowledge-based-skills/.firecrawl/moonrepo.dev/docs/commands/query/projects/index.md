[Skip to main content](https://moonrepo.dev/docs/commands/query/projects#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Use the `moon query projects` sub-command to query information about all projects in the project
graph. The project list can be filtered by passing a [query statement](https://moonrepo.dev/docs/concepts/query-lang) as
an argument, or by using [options](https://moonrepo.dev/docs/commands/query/projects#options) arguments.

```shell
# Find all projects
$ moon query projects

# Find all projects with an id that matches "react"
$ moon query projects --id react
$ moon query projects "project~react"

# Find all projects with a `lint` or `build` task
$ moon query projects --tasks "lint|build"
$ moon query projects "task=[lint,build]"
```

This will output a list of projects as JSON. The output has the following structure:

```ts
{
	projects: Project[],
	options: QueryOptions,
}
```

### Affected projects [​](https://moonrepo.dev/docs/commands/query/projects\#affected-projects "Direct link to Affected projects")

This command can also be used to query for affected projects, based on the state of the VCS working
tree. For advanced control, you can also pass the results of `moon query changed-files` to stdin.

```shell
# Find all affected projects
$ moon query projects --affected

# Find all affected projects using the results of another query
$ moon query changed-files | moon query projects --affected
```

### Arguments [​](https://moonrepo.dev/docs/commands/query/projects\#arguments "Direct link to Arguments")

- `[query]` \- An optional [query statement](https://moonrepo.dev/docs/concepts/query-lang) to filter projects with. When
provided, all [filter options](https://moonrepo.dev/docs/commands/query/projects#filters) are ignored. v1.4.0

### Options [​](https://moonrepo.dev/docs/commands/query/projects\#options "Direct link to Options")

#### Affected [​](https://moonrepo.dev/docs/commands/query/projects\#affected "Direct link to Affected")

- `--affected` \- Filter projects that have been affected by changed files.
- `--downstream` \- Include downstream dependents of queried projects. Supports "none" (default),
"direct", "deep".v1.29.0
- `--upstream` \- Include upstream dependencies of queried projects. Supports "none" (default),
"direct", "deep".v1.29.0

#### Filters [​](https://moonrepo.dev/docs/commands/query/projects\#filters "Direct link to Filters")

All option values are case-insensitive regex patterns.

- `--alias <regex>` \- Filter projects that match this alias.
- `--id <regex>` \- Filter projects that match this ID/name.
- `--language <regex>` \- Filter projects of this programming language.
- `--layer <regex>` \- Filter project of this layer.
- `--source <regex>` \- Filter projects that match this source path.
- `--stack <regex>` \- Filter projects of the tech stack.
- `--tags <regex>` \- Filter projects that have the following tags.
- `--tasks <regex>` \- Filter projects that have the following tasks.

### Configuration [​](https://moonrepo.dev/docs/commands/query/projects\#configuration "Direct link to Configuration")

- [`projects`](https://moonrepo.dev/docs/config/workspace#projects) in `.moon/workspace.*`

- [Affected projects](https://moonrepo.dev/docs/commands/query/projects#affected-projects)
- [Arguments](https://moonrepo.dev/docs/commands/query/projects#arguments)
- [Options](https://moonrepo.dev/docs/commands/query/projects#options)
  - [Affected](https://moonrepo.dev/docs/commands/query/projects#affected)
  - [Filters](https://moonrepo.dev/docs/commands/query/projects#filters)
- [Configuration](https://moonrepo.dev/docs/commands/query/projects#configuration)