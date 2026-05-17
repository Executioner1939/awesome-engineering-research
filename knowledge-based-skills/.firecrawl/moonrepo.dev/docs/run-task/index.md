[Skip to main content](https://moonrepo.dev/docs/run-task#__docusaurus_skipToContent_fallback)

BunDenoGoNode.jsPHPPythonRubyRust

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

2 min

Even though we've [created a task](https://moonrepo.dev/docs/create-task), it's not useful unless we _run it_, which is done
with the [`moon run <target>`](https://moonrepo.dev/docs/commands/run) command. This command requires a single argument, a
[primary target](https://moonrepo.dev/docs/concepts/target), which is the pairing of a scope and task name. In the example
below, our project is `app`, the task is `build`, and the target is `app:build`.

```shell
$ moon run app:build
```

When this command is ran, it will do the following:

- Generate a directed acyclic graph, known as the action (dependency) graph.
- Insert [`deps`](https://moonrepo.dev/docs/config/project#deps) as targets into the graph.
- Insert the primary target into the graph.
- Run all tasks in the graph in parallel and in topological order (the dependency chain).
- For each task, calculate [hashes](https://moonrepo.dev/docs/concepts/cache) and either:
  - On cache hit, exit early and return the last run.
  - On cache miss, run the task and generate a new cache.

## Running dependents [​](https://moonrepo.dev/docs/run-task\#running-dependents "Direct link to Running dependents")

moon will _always_ run upstream dependencies ( [`deps`](https://moonrepo.dev/docs/config/project#deps)) before running the
primary target, as their outputs may be required for the primary target to function correctly.

However, if you're working on a project that is shared and consumed by other projects, you may want
to verify that downstream dependents have not been indirectly broken by any changes. This can be
achieved by passing the `--downstream` option (aliased as `--dependents`), which will run dependent
targets _after_ the primary target.

```shell
$ moon run app:build --downstream direct
```

## Running based on affected files only [​](https://moonrepo.dev/docs/run-task\#running-based-on-affected-files-only "Direct link to Running based on affected files only")

By default [`moon run`](https://moonrepo.dev/docs/commands/run) will _always_ run the target, regardless if files have
actually changed. However, this is typically fine because of our
[smart hashing & cache layer](https://moonrepo.dev/docs/concepts/cache). With that being said, if you'd like to _only_ run a
target if files have changed, pass the `--affected` flag.

```shell
$ moon run app:build --affected
```

Under the hood, we extract locally changed (created, modified, staged, etc) files from your
configured [VCS](https://moonrepo.dev/docs/config/workspace#vcs), and exit early if no files intersect with the task's
[inputs](https://moonrepo.dev/docs/config/project#inputs).

### Using remote changes [​](https://moonrepo.dev/docs/run-task\#using-remote-changes "Direct link to Using remote changes")

If you'd like to determine affected files based on remote changes instead of local changes, pass the
`remote` value. This will extract changed files by comparing the current `HEAD` against the
[`vcs.defaultBranch`](https://moonrepo.dev/docs/config/workspace#defaultbranch).

```shell
$ moon run app:build --affected remote
```

### Filtering based on change status [​](https://moonrepo.dev/docs/run-task\#filtering-based-on-change-status "Direct link to Filtering based on change status")

We can take this a step further by filtering down affected files based on a change status, using the
`--status` option. This option accepts the following values: `added`, `deleted`, `modified`,
`staged`, `unstaged`, `untracked`. If not provided, the option defaults to all.

```shell
$ moon run app:build --affected --status deleted
```

Multiple status can be provided by passing the `--status` option multiple times.

```shell
$ moon run app:build --affected --status deleted --status modified
```

## Passing arguments to the underlying command [​](https://moonrepo.dev/docs/run-task\#passing-arguments-to-the-underlying-command "Direct link to Passing arguments to the underlying command")

If you'd like to pass arbitrary arguments to the underlying task command, in addition to the already
defined [`args`](https://moonrepo.dev/docs/config/project#args), you can pass them after `--`. These arguments are _appended_
_as-is_.

```shell
$ moon run app:build -- --force
```

> The `--` delimiter and any arguments _must_ be defined last on the command line.

## Advanced run targeting [​](https://moonrepo.dev/docs/run-task\#advanced-run-targeting "Direct link to Advanced run targeting")

By this point you should have a basic understanding of how to run tasks, but with moon, we want to
provide support for advanced workflows and development scenarios. For example, running a target in
all projects:

```shell
$ moon run :build
```

Or perhaps running a target based on a query:

```shell
$ moon run :build --query "language=[javascript, typescript]"
```

Jump to the official [`moon run` documentation](https://moonrepo.dev/docs/commands/run) for more examples!

## Next steps [​](https://moonrepo.dev/docs/run-task\#next-steps "Direct link to Next steps")

[Learn about tasks](https://moonrepo.dev/docs/concepts/task) [Learn about `moon run`](https://moonrepo.dev/docs/commands/run)

- [Running dependents](https://moonrepo.dev/docs/run-task#running-dependents)
- [Running based on affected files only](https://moonrepo.dev/docs/run-task#running-based-on-affected-files-only)
  - [Using remote changes](https://moonrepo.dev/docs/run-task#using-remote-changes)
  - [Filtering based on change status](https://moonrepo.dev/docs/run-task#filtering-based-on-change-status)
- [Passing arguments to the underlying command](https://moonrepo.dev/docs/run-task#passing-arguments-to-the-underlying-command)
- [Advanced run targeting](https://moonrepo.dev/docs/run-task#advanced-run-targeting)
- [Next steps](https://moonrepo.dev/docs/run-task#next-steps)