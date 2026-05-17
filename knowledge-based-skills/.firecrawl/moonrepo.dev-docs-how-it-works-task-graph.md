[Skip to main content](https://moonrepo.dev/docs/how-it-works/task-graph#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The task graph is a representation of all configured
[tasks in the workspace](https://moonrepo.dev/docs/config/workspace#projects) and their relationships between each other,
and is represented internally as a directed acyclic graph (DAG). This graph is derived from
information in the [project graph](https://moonrepo.dev/docs/how-it-works/project-graph). Below is a visual representation of a task
graph.

info

The [`moon task-graph`](https://moonrepo.dev/docs/commands/task-graph) command can be used to view the structure of your
workspace.

## Relationships [​](https://moonrepo.dev/docs/how-it-works/task-graph\#relationships "Direct link to Relationships")

A relationship is between a dependent (downstream task) and a dependency/requirement (upstream
task). Relationships are derived explicitly with the task [`deps`](https://moonrepo.dev/docs/config/project#deps) setting,
and fall into 1 of 2 categories:

### Required [​](https://moonrepo.dev/docs/how-it-works/task-graph\#required "Direct link to Required")

These are dependencies that are required to run and complete with a success, before the owning task
can run. If a required dependency fails, then the owning task will abort.

### Optional [​](https://moonrepo.dev/docs/how-it-works/task-graph\#optional "Direct link to Optional")

The opposite of [required](https://moonrepo.dev/docs/how-it-works/task-graph#required), these are dependencies that can either a) not exist during
task inheritance, or b) run and fail without aborting the owning task.

## What is the graph used for? [​](https://moonrepo.dev/docs/how-it-works/task-graph\#what-is-the-graph-used-for "Direct link to What is the graph used for?")

Great question, the task graph is extremely important for running tasks (duh), and it also:

- Is fed into the [action graph](https://moonrepo.dev/docs/how-it-works/action-graph) that can be executed in topological order.
- Determines affected tasks in [continuous integration](https://moonrepo.dev/docs/guides/ci) workflows.

- [Relationships](https://moonrepo.dev/docs/how-it-works/task-graph#relationships)
  - [Required](https://moonrepo.dev/docs/how-it-works/task-graph#required)
  - [Optional](https://moonrepo.dev/docs/how-it-works/task-graph#optional)
- [What is the graph used for?](https://moonrepo.dev/docs/how-it-works/task-graph#what-is-the-graph-used-for)