[Skip to main content](https://moonrepo.dev/docs/commands/check#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon check [...projects]` (or `moon c`) command will run _all_ [build and test tasks](https://moonrepo.dev/docs/concepts/task#types) for one or many projects. This is a convenience
command for verifying the current state of a project, instead of running multiple
[`moon run`](https://moonrepo.dev/docs/commands/run) commands.

```shell
# Check project by name
$ moon check app

# Check multiple projects by name
$ moon check client server

# Check closest project from current working directory
$ moon check --closest

# Check ALL projects (may be costly)
$ moon check --all
```

### Arguments [​](https://moonrepo.dev/docs/commands/check\#arguments "Direct link to Arguments")

- `[...id]` \- List of project IDs or aliases to explicitly check, as defined in
[`projects`](https://moonrepo.dev/docs/config/workspace#projects).

### Options [​](https://moonrepo.dev/docs/commands/check\#options "Direct link to Options")

Inherits all options from [`moon exec`](https://moonrepo.dev/docs/commands/exec), and pre-fills with: `--on-failure=bail`,
`--upstream=deep`.

- `--all` \- Run check for all projects in the workspace.
- `--closest` \- Run check for the closest project starting from the current working directory.

### Configuration [​](https://moonrepo.dev/docs/commands/check\#configuration "Direct link to Configuration")

- [`projects`](https://moonrepo.dev/docs/config/workspace#projects) in `.moon/workspace.*`
- [`tasks`](https://moonrepo.dev/docs/config/tasks#tasks) in `.moon/tasks/*`
- [`tasks`](https://moonrepo.dev/docs/config/project#tasks) in `moon.*`

- [Arguments](https://moonrepo.dev/docs/commands/check#arguments)
- [Options](https://moonrepo.dev/docs/commands/check#options)
- [Configuration](https://moonrepo.dev/docs/commands/check#configuration)