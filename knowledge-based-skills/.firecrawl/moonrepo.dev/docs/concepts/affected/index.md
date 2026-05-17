[Skip to main content](https://moonrepo.dev/docs/concepts/affected#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Affected is a term to describe when a project or task is _affected by a change_ in the environment
(workspace). This is a core concept in moon, and is the basis for many of our features, such as task
running, incremental builds, and more.

## Change types [​](https://moonrepo.dev/docs/concepts/affected\#change-types "Direct link to Change types")

To start, there are 3 types of "sources" that can trigger an affected state: files, environment
variables, and graph relations.

### Files [​](https://moonrepo.dev/docs/concepts/affected\#files "Direct link to Files")

A file is considered changed if it has been added, modified, deleted, renamed, moved, copied, so on
and so forth. This state is determined by the version control system (VCS) in use, such as Git,
Mercurial, or Subversion. For Git, this is determined by the `git status` command.

For a project, any changed file that is within the project folder (starts with the project source),
triggers affected.

For a task, any changed file that is configured within the task's
[`inputs`](https://moonrepo.dev/docs/config/project#inputs) triggers affected.

### Environment variables [​](https://moonrepo.dev/docs/concepts/affected\#environment-variables "Direct link to Environment variables")

An environment variable is considered changed if it exists and is non-empty. This is determined by
the presence of the variable in the environment, and its value.

For projects, they are _not_ affected by environment variables.

For a task, any changed environment variable that is configured within the task's
[`inputs`](https://moonrepo.dev/docs/config/project#inputs) triggers affected.

### Graph relations [​](https://moonrepo.dev/docs/concepts/affected\#graph-relations "Direct link to Graph relations")

A relation is considered changed if a project or task that is depended on, or depends on, is
affected by a changed file or environment variable. This is determined by the project and task
graph, which is built from the workspace configuration.

For a project, affected dependency/dependent projects of the project (via
[`dependsOn`](https://moonrepo.dev/docs/config/project#dependson)), or affected tasks within the project, triggers
affected.

For a task, affected dependency/dependent tasks of the task (via [`deps`](https://moonrepo.dev/docs/config/project#deps))
triggers affected.

info

This check is conditionally enabled. For [`moon query`](https://moonrepo.dev/docs/commands/query), it is always enabled.
For exec-based commands, it is not enabled by default and the `--include-relations` flag must be
passed.

## Graph depth [​](https://moonrepo.dev/docs/concepts/affected\#graph-depth "Direct link to Graph depth")

When determining affected state based on graph relations, the depth of traversal can be configured
with the `--upstream` (`--dependencies`) and `--downstream` (`--dependents`) options. These options
can be set to one of the following values:

- `none` \- Do not include any relations.
- `direct` \- Include only direct relations.
- `deep` \- Include all relations.

For exec-based commands, the default is `--upstream=deep` and `--downstream=none`, meaning all
dependencies are included, but no dependents are included. For query and other commands, the default
is `none` for both.

- [Change types](https://moonrepo.dev/docs/concepts/affected#change-types)
  - [Files](https://moonrepo.dev/docs/concepts/affected#files)
  - [Environment variables](https://moonrepo.dev/docs/concepts/affected#environment-variables)
  - [Graph relations](https://moonrepo.dev/docs/concepts/affected#graph-relations)
- [Graph depth](https://moonrepo.dev/docs/concepts/affected#graph-depth)