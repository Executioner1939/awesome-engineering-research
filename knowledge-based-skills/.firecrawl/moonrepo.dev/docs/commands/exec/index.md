[Skip to main content](https://moonrepo.dev/docs/commands/exec#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.0.0

The `moon exec` (or `moon x`, or `moonx`) command is a low-level command for executing tasks in the
action pipeline. It provides fine-grained control over how tasks are selected and executed, through
command line options, making it ideal for custom workflows and advanced use cases.

The [`moon check`](https://moonrepo.dev/docs/commands/check), [`moon ci`](https://moonrepo.dev/docs/commands/ci), and [`moon run`](https://moonrepo.dev/docs/commands/run) commands are all built on
top of `moon exec`, so be sure to check those out for more user-friendly abstractions!

```shell
# Run `lint` in project `app`
$ moon exec app:lint
$ moonx app:lint

# Run `dev` in project `client` and `server`
$ moon exec client:dev server:dev
$ moonx client:dev server:dev

# Run `test` in all projects
$ moon exec :test
$ moonx :test

# Run `test` in the closest project, relative to the current working directory
$ moon exec '~:test'
$ moonx '~:test'

# Run `test` in all projects with tag `frontend`
$ moon exec '#frontend:test'
$ moonx '#frontend:test'

# Run `format` in the default project
$ moon exec format
$ moonx format

# Run `build` in projects matching the query
$ moon exec :build --query "language=javascript && projectLayer=library"
```

info

For a declarative alternative to CLI options, see the [execution plan guide](https://moonrepo.dev/docs/guides/exec-plan).

## Arguments [​](https://moonrepo.dev/docs/commands/exec\#arguments "Direct link to Arguments")

- `...<target>` \- [Task targets](https://moonrepo.dev/docs/concepts/target) or project relative tasks to run.
- `[-- <args>]` \- Additional arguments to
[pass to the underlying command](https://moonrepo.dev/docs/run-task#passing-arguments-to-the-underlying-command).

## Options [​](https://moonrepo.dev/docs/commands/exec\#options "Direct link to Options")

- `--ci` \- Force enable CI mode.
- `-f`, `--force` \- Force run and bypass cache, ignore changed files, and skip affected checks.
- `-i`, `--interactive` \- Run the pipeline and tasks interactively.
- `-p`, `--plan <PATH>` \- Path to an execution plan JSON file. See the
[execution plan guide](https://moonrepo.dev/docs/guides/exec-plan) for more details. v2.1.0
- `-s`, `--summary [LEVEL]` \- Print a summary of all actions that were ran in the pipeline.

### Workflow [​](https://moonrepo.dev/docs/commands/exec\#workflow "Direct link to Workflow")

- `--ignore-ci-checks` \- Ignore "run in CI" task checks.
- `--on-failure <ON>` \- When a task fails, either bail the pipeline, or continue executing.
- `--query <QUERY>` \- Filter tasks based on the result of a query.
- `--no-actions` \- Run the pipeline without sync and setup related actions.

### Affected [​](https://moonrepo.dev/docs/commands/exec\#affected "Direct link to Affected")

- `--affected [BY]` \- Only run tasks if affected by changed files. Optionally accepts "local" or
"remote".
- `--base <BASE>` \- Base branch, commit, or revision to compare against.
- `--head <HEAD>` \- Current branch, commit, or revision to compare with.
- `-g`, `--include-relations` \- Include graph relations for affected checks, instead of just changed
files.
- `--status <STATUS>` \- Filter changed files based on a changed status.
- `--stdin` \- Accept changed files from stdin for affected checks.

### Graph [​](https://moonrepo.dev/docs/commands/exec\#graph "Direct link to Graph")

- `--downstream <DEPTH>`, `--dependents <DEPTH>` \- Control the depth of downstream dependents.
Supports "none" (default), "direct", "deep".
- `--upstream <DEPTH>`, `--dependencies <DEPTH>` \- Control the depth of upstream dependencies.
Supports "none", "direct", "deep" (default).

### Parallelism [​](https://moonrepo.dev/docs/commands/exec\#parallelism "Direct link to Parallelism")

- `--job <INDEX>` \- Index of the current job (0 based).
- `--job-total <TOTAL>` \- Total amount of jobs to run.

- [Arguments](https://moonrepo.dev/docs/commands/exec#arguments)
- [Options](https://moonrepo.dev/docs/commands/exec#options)
  - [Workflow](https://moonrepo.dev/docs/commands/exec#workflow)
  - [Affected](https://moonrepo.dev/docs/commands/exec#affected)
  - [Graph](https://moonrepo.dev/docs/commands/exec#graph)
  - [Parallelism](https://moonrepo.dev/docs/commands/exec#parallelism)