[Skip to main content](https://moonrepo.dev/docs/config/tasks#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `.moon/tasks/**/*` files configures file groups and tasks that are inherited by _every matching_
project in the workspace based on inheritance conditions.
[Learn more about task inheritance!](https://moonrepo.dev/docs/concepts/task-inheritance)

Projects can override or merge with these settings within their respective [`moon.*`](https://moonrepo.dev/docs/config/project).

## `extends` [​](https://moonrepo.dev/docs/config/tasks\#extends "Direct link to extends")

Defines one or many external `.moon/tasks/**/*`'s to extend and inherit settings from. Perfect for
reusability and sharing configuration across repositories and projects. When defined, this setting
must be an HTTPS URL _or_ relative file system path that points to a valid YAML document!

.moon/tasks/all.yml

```yaml
extends: 'https://raw.githubusercontent.com/organization/repository/master/.moon/tasks/all.yml'
```

caution

For map-based settings, `fileGroups` and `tasks`, entries from both the extended configuration and
local configuration are merged into a new map, with the values of the local taking precedence. Map
values _are not_ deep merged!

## `fileGroups` [​](https://moonrepo.dev/docs/config/tasks\#filegroups "Direct link to filegroups")

> For more information on file group configuration, refer to the
> [`fileGroups`](https://moonrepo.dev/docs/config/project#filegroups) section in the [`moon.*`](https://moonrepo.dev/docs/config/project) doc.

Defines [file groups](https://moonrepo.dev/docs/concepts/file-group) that will be inherited by projects, and also enables
enforcement of organizational patterns and file locations. For example, encourage projects to place
source files in a `src` folder, and all test files in `tests`.

.moon/tasks/all.yml

```yaml
fileGroups:
  configs:
    - '*.config.{js,cjs,mjs}'
    - '*.json'
  sources:
    - 'src/**/*'
    - 'types/**/*'
  tests:
    - 'tests/**/*'
    - '**/__tests__/**/*'
  assets:
    - 'assets/**/*'
    - 'images/**/*'
    - 'static/**/*'
    - '**/*.{scss,css}'
```

info

File paths and globs used within a file group are relative from the inherited project's root, and
not the workspace root.

## `implicitDeps` [​](https://moonrepo.dev/docs/config/tasks\#implicitdeps "Direct link to implicitdeps")

Defines task [`deps`](https://moonrepo.dev/docs/config/project#deps) that are implicitly inserted into _all_ inherited tasks within
a project. This is extremely useful for pre-building projects that are used extensively throughout
the repo, or always building project dependencies. Defaults to an empty list.

.moon/tasks/all.yml

```yaml
implicitDeps:
  - '^:build'
```

info

Implicit dependencies are _always_ inherited, regardless of the [`mergeDeps`](https://moonrepo.dev/docs/config/project#mergedeps)
option.

## `implicitInputs` [​](https://moonrepo.dev/docs/config/tasks\#implicitinputs "Direct link to implicitinputs")

Defines task [`inputs`](https://moonrepo.dev/docs/config/project#inputs) that are implicitly inserted into _all_ inherited tasks
within a project. This is extremely useful for the "changes to these files should always trigger a
task" scenario.

Like `inputs`, file paths/globs defined here are relative from the inheriting project.
[Project and workspace relative file patterns](https://moonrepo.dev/docs/concepts/file-pattern#project-relative) are
supported and encouraged.

.moon/tasks/node.yml

```yaml
implicitInputs:
  - 'package.json'
```

info

Implicit inputs are _always_ inherited, regardless of the [`mergeInputs`](https://moonrepo.dev/docs/config/project#mergeinputs)
option.

## `inheritedBy`v2.0.0 [​](https://moonrepo.dev/docs/config/tasks\#inheritedby "Direct link to inheritedby")

A map of conditions that must be met for the configuration within the file to be inherited by a
project. When this field is not defined, or is an empty map, the configuration will be inherited by
all projects.

.moon/tasks/custom.yml

```yaml
inheritedBy:
  # Project belongs to either javascript or typescript toolchain, but not the ruby toolchain
  toolchains:
    or: ['javascript', 'typescript']
    not: ['ruby']
  # And project is either a frontend or backend stack
  stacks: ['frontend', 'backend']
  # And project is either a library or tool layer
  layers: ['library', 'tool']
```

info

View the [official task inheritance guide](https://moonrepo.dev/docs/concepts/task-inheritance) for more information!

## `tasks` [​](https://moonrepo.dev/docs/config/tasks\#tasks "Direct link to tasks")

> For more information on task configuration, refer to the [`tasks`](https://moonrepo.dev/docs/config/project#tasks) section in the
> [`moon.*`](https://moonrepo.dev/docs/config/project) doc.

As mentioned in the link above, [tasks](https://moonrepo.dev/docs/concepts/task) are actions that are ran within the
context of a project, and commonly wrap a command. For most workspaces, every project _should_ have
linting, typechecking, testing, code formatting, so on and so forth. To reduce the amount of
boilerplate that _every_ project would require, this setting offers the ability to define tasks that
are inherited by many projects within the workspace, but can also be overridden per project.

.moon/tasks/all.yml

```yaml
tasks:
  format:
    command: 'prettier --check .'

  lint:
    command: 'eslint --no-error-on-unmatched-pattern .'

  test:
    command: 'jest --passWithNoTests'

  typecheck:
    command: 'tsc --build'
```

info

Relative file paths and globs used within a task are relative from the inherited project's root, and
not the workspace root, or the location of the `.moon/tasks/*` file.

## `taskOptions`v1.20.0 [​](https://moonrepo.dev/docs/config/tasks\#taskoptions "Direct link to taskoptions")

> For more information on task options, refer to the [`options`](https://moonrepo.dev/docs/config/project#options) section in the
> [`moon.*`](https://moonrepo.dev/docs/config/project) doc.

Like [tasks](https://moonrepo.dev/docs/config/tasks#tasks), this setting allows you to define task options that will be inherited by _all_
_tasks_ within the configured file, and by all project-level inherited tasks. This setting is the 1st
link in the inheritance chain, and can be overridden within each task.

.moon/tasks/all.yml

```yaml
taskOptions:
  # Never cache builds
  cache: false
  # Always re-run flaky tests
  retryCount: 2

tasks:
  build:
    # ...
    options:
      # Override the default cache setting
      cache: true
```

- [`extends`](https://moonrepo.dev/docs/config/tasks#extends)
- [`fileGroups`](https://moonrepo.dev/docs/config/tasks#filegroups)
- [`implicitDeps`](https://moonrepo.dev/docs/config/tasks#implicitdeps)
- [`implicitInputs`](https://moonrepo.dev/docs/config/tasks#implicitinputs)
- [`inheritedBy`](https://moonrepo.dev/docs/config/tasks#inheritedby)
- [`tasks`](https://moonrepo.dev/docs/config/tasks#tasks)
- [`taskOptions`](https://moonrepo.dev/docs/config/tasks#taskoptions)