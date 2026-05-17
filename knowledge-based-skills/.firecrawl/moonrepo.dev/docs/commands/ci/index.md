[Skip to main content](https://moonrepo.dev/docs/commands/ci#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon ci` command is a special command that should be ran in a continuous integration (CI)
environment, as it does all the heavy lifting necessary for effectively running tasks.

By default this will run all tasks that are affected by changed files and have the
[`runInCI`](https://moonrepo.dev/docs/config/project#runinci) task option enabled.

```shell
$ moon ci
```

However, you can also provide a list of targets to explicitly run, which will still be filtered down
by `runInCI`.

```shell
$ moon ci :build :lint
```

info

View the official [continuous integration guide](https://moonrepo.dev/docs/guides/ci) for a more in-depth example of how to
utilize this command.

### Arguments [​](https://moonrepo.dev/docs/commands/ci\#arguments "Direct link to Arguments")

- `...[target]` \- [Task targets](https://moonrepo.dev/docs/concepts/target) to run.

### Options [​](https://moonrepo.dev/docs/commands/ci\#options "Direct link to Options")

Inherits most options from [`moon exec`](https://moonrepo.dev/docs/commands/exec) and pre-fills with: `--affected`, `--ci`,
`--on-failure=continue`, `--summary=detailed`, `--upstream=deep`, `--downstream=direct`.

### Configuration [​](https://moonrepo.dev/docs/commands/ci\#configuration "Direct link to Configuration")

- [`tasks`](https://moonrepo.dev/docs/config/tasks#tasks) in `.moon/tasks/*`
- [`tasks`](https://moonrepo.dev/docs/config/project#tasks) in `moon.*`
- [`tasks.*.options.runInCI`](https://moonrepo.dev/docs/config/project#runinci) in `moon.*`

- [Arguments](https://moonrepo.dev/docs/commands/ci#arguments)
- [Options](https://moonrepo.dev/docs/commands/ci#options)
- [Configuration](https://moonrepo.dev/docs/commands/ci#configuration)