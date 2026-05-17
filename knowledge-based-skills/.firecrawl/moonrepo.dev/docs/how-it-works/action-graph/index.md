[Skip to main content](https://moonrepo.dev/docs/how-it-works/action-graph#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

When you run a [task](https://moonrepo.dev/docs/config/project#tasks-1) on the command line, we generate an action graph to
ensure [dependencies](https://moonrepo.dev/docs/config/project#deps) of tasks have ran before running run the primary task.

The action graph is a representation of all [tasks](https://moonrepo.dev/docs/concepts/task), derived from the
[project graph](https://moonrepo.dev/docs/how-it-works/project-graph) and [task graph](https://moonrepo.dev/docs/how-it-works/task-graph), and is also represented internally
as a directed acyclic graph (DAG).

## Actions [​](https://moonrepo.dev/docs/how-it-works/action-graph\#actions "Direct link to Actions")

Unlike other task runners in the industry that represent each node in the graph as a task to run, we
represent each node in the graph as an action to perform. This allows us to be more flexible and
efficient with how we run tasks, and allows us to provide more functionality and automation than
other runners.

The following actions compose our action graph:

### Sync workspace [​](https://moonrepo.dev/docs/how-it-works/action-graph\#sync-workspace "Direct link to Sync workspace")

This is a common action that always runs and give's moon a chance to perform operations and health
checks across the entire workspace.

info

This action can be skipped by disabling the
[`pipeline.syncWorkspace`](https://moonrepo.dev/docs/config/workspace#syncworkspace) setting.

### Setup toolchain [​](https://moonrepo.dev/docs/how-it-works/action-graph\#setup-toolchain "Direct link to Setup toolchain")

The most important action in the graph is the setup toolchain action, which downloads and installs a
tier 3 language into the toolchain. For other tiers, this is basically a no-operation.

- When the tool has already been installed, this action will be skipped.
- Actions will be scoped by toolchain and version (or none if using global `PATH`).

info

This action can be skipped by setting the `MOON_SKIP_SETUP_TOOLCHAIN=true` environment variable. The
skip can be scoped per tool by setting the value to the tool name (`node`), and also by version
(`node:20.0.0`). Supports a comma-separated list.

### Setup environmentv1.35.0 [​](https://moonrepo.dev/docs/how-it-works/action-graph\#setup-environment "Direct link to setup-environment")

This action runs after the toolchain has been setup, but before dependencies are installed, so that
the development environment can be setup and configured. This includes operations such as modifying
a manifest (`package.json`, etc), updating configuration files, initializing venv's (Python), so on
and so forth.

### Setup protov1.39.0 [​](https://moonrepo.dev/docs/how-it-works/action-graph\#setup-proto "Direct link to setup-proto")

This action runs before all toolchain related actions and ensures that [proto](https://moonrepo.dev/proto) has been
installed and is available for use. This is required for toolchains that will be downloaded and
installed.

### Install dependencies [​](https://moonrepo.dev/docs/how-it-works/action-graph\#install-dependencies "Direct link to Install dependencies")

Before we run a task, we ensure that all language/toolchain dependencies (`node_modules` for
example) have been installed, by automatically installing them if we detect changes since the last
run. We achieve this by comparing lockfile modified timestamps, parsing manifest files, and hashing
resolved dependency versions.

- When dependencies do _not_ need to be installed, this action will be skipped.
- Depending on the language and configuration, we may install dependencies in a project, or in the
workspace root for all projects.
- Actions will be scoped by toolchain and dependencies root.

info

This action can be skipped by disabling the
[`pipeline.installDependencies`](https://moonrepo.dev/docs/config/workspace#installdependencies) setting.

### Sync project [​](https://moonrepo.dev/docs/how-it-works/action-graph\#sync-project "Direct link to Sync project")

To ensure a consistently healthy project and repository, we run a process known as syncing
_everytime_ a task is ran. This action will run sync operations for all toolchains associated with
the project.

info

This action can be skipped by disabling the
[`pipeline.syncProject`](https://moonrepo.dev/docs/config/workspace#syncproject) setting.

### Run task [​](https://moonrepo.dev/docs/how-it-works/action-graph\#run-task "Direct link to Run task")

The primary action in the graph is the run [task](https://moonrepo.dev/docs/concepts/task) action, which runs a project's
task as a child process, derived from a [target](https://moonrepo.dev/docs/concepts/target). Tasks can depend on other
tasks, and they'll be effectively orchestrated and executed by running in topological order using a
thread pool.

### Run interactive task [​](https://moonrepo.dev/docs/how-it-works/action-graph\#run-interactive-task "Direct link to Run interactive task")

Like the base run task, but runs the [task interactively](https://moonrepo.dev/docs/concepts/task#interactive) with stdin
capabilities. All interactive tasks are run in isolation in the graph.

### Run persistent task [​](https://moonrepo.dev/docs/how-it-works/action-graph\#run-persistent-task "Direct link to Run persistent task")

Like the base run task, but runs the [task in a persistent process](https://moonrepo.dev/docs/concepts/task#persistent)
that never exits. All persistent tasks are run in parallel as the last batch in the graph.

## What is the graph used for? [​](https://moonrepo.dev/docs/how-it-works/action-graph\#what-is-the-graph-used-for "Direct link to What is the graph used for?")

Without the action graph, tasks would not efficiently run, or possibly at all! The graph helps to
run tasks in parallel, in the correct order, and to ensure a reliable outcome.

- [Actions](https://moonrepo.dev/docs/how-it-works/action-graph#actions)
  - [Sync workspace](https://moonrepo.dev/docs/how-it-works/action-graph#sync-workspace)
  - [Setup toolchain](https://moonrepo.dev/docs/how-it-works/action-graph#setup-toolchain)
  - [Setup environment](https://moonrepo.dev/docs/how-it-works/action-graph#setup-environment)
  - [Setup proto](https://moonrepo.dev/docs/how-it-works/action-graph#setup-proto)
  - [Install dependencies](https://moonrepo.dev/docs/how-it-works/action-graph#install-dependencies)
  - [Sync project](https://moonrepo.dev/docs/how-it-works/action-graph#sync-project)
  - [Run task](https://moonrepo.dev/docs/how-it-works/action-graph#run-task)
  - [Run interactive task](https://moonrepo.dev/docs/how-it-works/action-graph#run-interactive-task)
  - [Run persistent task](https://moonrepo.dev/docs/how-it-works/action-graph#run-persistent-task)
- [What is the graph used for?](https://moonrepo.dev/docs/how-it-works/action-graph#what-is-the-graph-used-for)