[Skip to main content](https://moonrepo.dev/docs/concepts/task-inheritance#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Unlike other task runners that require the same tasks to be repeatedly defined for _every_ project,
moon uses an inheritance model where tasks can be defined once at the workspace-level, and are then
inherited by _many or all_ projects.

Workspace-level tasks (also known as global tasks) are defined in [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks), and
are inherited by based on conditions. However, projects are able to include, exclude, or rename
inherited tasks using the [`workspace.inheritedTasks`](https://moonrepo.dev/docs/config/project#inheritedtasks) in
[`moon.*`](https://moonrepo.dev/docs/config/project).

## Conditional inheritance [​](https://moonrepo.dev/docs/concepts/task-inheritance\#conditional-inheritance "Direct link to Conditional inheritance")

Task inheritance is powered by the [`inheritedBy`](https://moonrepo.dev/docs/config/tasks#inheritedby) setting in global
task configurations (those in [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks)). This setting defines conditions that a
project must meet in order for inheritance to occur. If the setting is not defined, or no conditions
are defined, the configuration is inherited by _all_ projects.

The following conditions are supported:

- `file`, `files` \- Inherit for projects that contain specific files (does not support globs).
- `language`, `languages` \- Inherit for projects that belong to specific
[`language`](https://moonrepo.dev/docs/config/project#language) s.
- `layer`, `layers` \- Inherit for projects that belong to specific
[`layer`](https://moonrepo.dev/docs/config/project#layer) s.
- `stack`, `stacks` \- Inherit for projects that belong to specific
[`stack`](https://moonrepo.dev/docs/config/project#stack) s.
- `tag`, `tags` \- Inherit for projects that have specific [`tags`](https://moonrepo.dev/docs/config/project#tags).
- `toolchain`, `toolchains` \- Inherit for projects that belong to specific
[`toolchains`](https://moonrepo.dev/docs/config/project#toolchains).

One or many conditions can be defined, and all conditions must be met for inheritance to occur. For
example, the following configuration will only be inherited by Node.js frontend libraries.

.moon/tasks/node-frontend-library.yml

```yaml
inheritedBy:
  toolchain: 'node'
  stack: 'frontend'
  layer: 'library'
```

Each condition supports a single value or an array of values. For example, the previous example
could be rewritten to inherit for both Node.js or Deno frontend libraries.

.moon/tasks/js-frontend-library.yml

```yaml
inheritedBy:
  toolchains: ['node', 'deno']
  stack: 'frontend'
  layer: 'library'
```

### Clauses [​](https://moonrepo.dev/docs/concepts/task-inheritance\#clauses "Direct link to Clauses")

The `tags` and `toolchains` conditions support special clauses `and`, `or` (the default), and `not`
for matching more complex scenarios.

```yaml
inheritedBy:
  toolchains:
    or: ['javascript', 'typescript']
    not: ['ruby']
  layer: 'library'
```

## Merge strategies [​](https://moonrepo.dev/docs/concepts/task-inheritance\#merge-strategies "Direct link to Merge strategies")

When a [global task](https://moonrepo.dev/docs/config/tasks#tasks) and [local task](https://moonrepo.dev/docs/config/project#tasks) of the same
name exist, they are merged into a single task. To accomplish this, one of many
[merge strategies](https://moonrepo.dev/docs/config/project#options) can be used.

Merging is applied to the parameters [`args`](https://moonrepo.dev/docs/config/project#args),
[`deps`](https://moonrepo.dev/docs/config/project#deps), [`env`](https://moonrepo.dev/docs/config/project#env-1),
[`inputs`](https://moonrepo.dev/docs/config/project#inputs), [`outputs`](https://moonrepo.dev/docs/config/project#outputs), and
[`toolchains`](https://moonrepo.dev/docs/config/project#toolchains), using the [`merge`](https://moonrepo.dev/docs/config/project#merge),
[`mergeArgs`](https://moonrepo.dev/docs/config/project#mergeargs), [`mergeDeps`](https://moonrepo.dev/docs/config/project#mergedeps),
[`mergeEnv`](https://moonrepo.dev/docs/config/project#mergeenv), [`mergeInputs`](https://moonrepo.dev/docs/config/project#mergeinputs),
[`mergeOutputs`](https://moonrepo.dev/docs/config/project#mergeoutputs) and
[`mergeToolchains`](https://moonrepo.dev/docs/config/project#mergetoolchains) options respectively. Each of these options
support one of the following strategy values.

- `append` (default) - Values found in the local task are merged _after_ the values found in the
global task. For example, this strategy is useful for toggling flag arguments.
- `prepend` \- Values found in the local task are merged _before_ the values found in the global
task. For example, this strategy is useful for applying option arguments that must come before
positional arguments.
- `preserve` \- Preserve the original global task values. This should rarely be used, but exists for
situations where an inheritance chain is super long and complex, but we simply want to the base
values. v1.29.0
- `replace` \- Values found in the local task entirely _replaces_ the values in the global task. This
strategy is useful when you need full control.

All 3 of these strategies are demonstrated below, with a somewhat contrived example, but you get the
point.

```yaml
# Global
tasks:
  build:
    command:
      - 'webpack'
      - '--mode'
      - 'production'
      - '--color'
    deps:
      - 'designSystem:build'
    inputs:
      - '/webpack.config.js'
    outputs:
      - 'build/'

# Local
tasks:
  build:
    args: '--no-color --no-stats'
    deps:
      - 'reactHooks:build'
    inputs:
      - 'webpack.config.js'
    options:
      mergeArgs: 'append'
      mergeDeps: 'prepend'
      mergeInputs: 'replace'

# Merged result
tasks:
  build:
    command:
      - 'webpack'
      - '--mode'
      - 'production'
      - '--color'
      - '--no-color'
      - '--no-stats'
    deps:
      - 'reactHooks:build'
      - 'designSystem:build'
    inputs:
      - 'webpack.config.js'
    outputs:
      - 'build/'
    options:
      mergeArgs: 'append'
      mergeDeps: 'prepend'
      mergeInputs: 'replace'
```

- [Conditional inheritance](https://moonrepo.dev/docs/concepts/task-inheritance#conditional-inheritance)
  - [Clauses](https://moonrepo.dev/docs/concepts/task-inheritance#clauses)
- [Merge strategies](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies)