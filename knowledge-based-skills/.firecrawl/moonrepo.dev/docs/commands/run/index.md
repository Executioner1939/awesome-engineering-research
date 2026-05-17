[Skip to main content](https://moonrepo.dev/docs/commands/run#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon run` (or `moon r`) command will run one or many [targets](https://moonrepo.dev/docs/concepts/target) and all of
its dependencies in topological order. Each run will incrementally cache each task, improving speed
and development times... over time. View the official [Run a task](https://moonrepo.dev/docs/run-task) and
[Cheat sheet](https://moonrepo.dev/docs/cheat-sheet#tasks) articles for more information!

```shell
# Run `lint` in project `app`
$ moon run app:lint

# Run `dev` in project `client` and `server`
$ moon run client:dev server:dev

# Run `test` in all projects
$ moon run :test

# Run `test` in the closest project, relative to the current working directory
$ moon run '~:test'

# Run `test` in all projects with tag `frontend`
$ moon run '#frontend:test'

# Run `format` in default project
$ moon run format

# Run `build` in projects matching the query
$ moon run :build --query "language=javascript && projectLayer=library"
```

info

The default behavior for `moon run` is to "fail fast", meaning that any failed task will immediately
abort execution of the entire action graph. Use `moon exec --on-failure continue` for alternative
behavior.

### Arguments [​](https://moonrepo.dev/docs/commands/run\#arguments "Direct link to Arguments")

- `...<target>` \- [Targets](https://moonrepo.dev/docs/concepts/target) or project relative tasks to run.
- `[-- <args>]` \- Additional arguments to
[pass to the underlying command](https://moonrepo.dev/docs/run-task#passing-arguments-to-the-underlying-command).

### Options [​](https://moonrepo.dev/docs/commands/run\#options "Direct link to Options")

Inherits all options from [`moon exec`](https://moonrepo.dev/docs/commands/exec) and pre-fills with: `--on-failure=bail`,
`--upstream=deep`.

- `query` \- Filter tasks based on the result of a query.

### Configuration [​](https://moonrepo.dev/docs/commands/run\#configuration "Direct link to Configuration")

- [`projects`](https://moonrepo.dev/docs/config/workspace#projects) in `.moon/workspace.*`
- [`tasks`](https://moonrepo.dev/docs/config/tasks#tasks) in `.moon/tasks/*`
- [`tasks`](https://moonrepo.dev/docs/config/project#tasks) in `moon.*`

- [Arguments](https://moonrepo.dev/docs/commands/run#arguments)
- [Options](https://moonrepo.dev/docs/commands/run#options)
- [Configuration](https://moonrepo.dev/docs/commands/run#configuration)