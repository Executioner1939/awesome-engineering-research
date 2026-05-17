[Skip to main content](https://moonrepo.dev/docs/concepts/target#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

A target is a compound identifier that pairs a [scope](https://moonrepo.dev/docs/concepts/target#common-scopes) to a [task](https://moonrepo.dev/docs/concepts/task),
separated by a `:`, in the format of `scope:task`.

Targets are used by terminal commands...

```shell
$ moon run designSystem:build
```

And configurations for declaring cross-project or cross-task dependencies.

```yaml
tasks:
  build:
    command: 'webpack'
    deps:
      - 'designSystem:build'
```

## Common scopes [​](https://moonrepo.dev/docs/concepts/target\#common-scopes "Direct link to Common scopes")

These scopes are available for both running targets and configuring them.

### By project [​](https://moonrepo.dev/docs/concepts/target\#by-project "Direct link to By project")

The most common scope is the project scope, which requires the name of a project, as defined in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace). When paired with a task name, it will run a specific
task from that project.

```shell
# Run `lint` in project `app`
$ moon run app:lint
```

### By tagv1.4.0 [​](https://moonrepo.dev/docs/concepts/target\#by-tag "Direct link to by-tag")

Another way to target projects is with the tag scope, which requires the name of a tag prefixed with
`#`, and will run a specific task in all projects with that tag.

```shell
# Run `lint` in projects with the tag `frontend`
$ moon run '#frontend:lint'
```

caution

Because `#` is a special character in the terminal (is considered a comment), you'll need to wrap
the target in quotes, or escape it like so `\#`.

## Run scopes [​](https://moonrepo.dev/docs/concepts/target\#run-scopes "Direct link to Run scopes")

These scopes are only available on the command line when running tasks with `moon run` or `moon ci`.

### All projects [​](https://moonrepo.dev/docs/concepts/target\#all-projects "Direct link to All projects")

For situations where you want to run a specific target in _all_ projects, for example `lint`ing, you
can utilize the all projects scope by omitting the project name from the target: `:lint`.

```shell
# Run `lint` in all projects
$ moon run :lint
```

### Closest project `~`v1.33.0 [​](https://moonrepo.dev/docs/concepts/target\#closest-project- "Direct link to closest-project-")

If you are within a project folder, or an arbitrarily nested folder, and want to run a task in the
closest project (traversing upwards), the `~` scope can be used.

```shell
# Run `lint` in the closest project
$ moon run '~:lint'
```

caution

Because `~` is a special character in the terminal (tilde expansion), you'll need to wrap the target
in quotes, or escape it like so `\~`.

## Config scopes [​](https://moonrepo.dev/docs/concepts/target\#config-scopes "Direct link to Config scopes")

These scopes are only available when configuring a task.

### Dependencies `^` [​](https://moonrepo.dev/docs/concepts/target\#dependencies- "Direct link to dependencies-")

When you want to include a reference for each project [that's depended on](https://moonrepo.dev/docs/concepts/project#dependencies),
you can utilize the `^` scope. This will be expanded to _all_ depended on projects. If you do not
want all projects, then you'll need to explicitly define them.

moon.yml

```yaml
dependsOn:
  - 'apiClients'
  - 'designSystem'

# Configured as
tasks:
  build:
    command: 'webpack'
    deps:
      - '^:build'

# Resolves to
tasks:
  build:
    command: 'webpack'
    deps:
      - 'apiClients:build'
      - 'designSystem:build'
```

### Owning project `~` [​](https://moonrepo.dev/docs/concepts/target\#owning-project- "Direct link to owning-project-")

When referring to another task within the current project, you can utilize the `~` scope, or omit
the `~:` prefix altogether, which will be expanded to the current project's name. This is useful for
situations where the name is unknown, for example, when configuring
[`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks), or if you just want a shortcut!

.moon/tasks/all.yml

```yaml
# Configured as
tasks:
  lint:
    command: 'eslint'
    deps:
      - '~:typecheck'
      # OR
      - 'typecheck'
  typecheck:
    command: 'tsc'

# Resolves to (assuming project is "foo")
tasks:
  lint:
    command: 'eslint'
    deps:
      - 'foo:typecheck'
  typecheck:
    command: 'tsc'
```

- [Common scopes](https://moonrepo.dev/docs/concepts/target#common-scopes)
  - [By project](https://moonrepo.dev/docs/concepts/target#by-project)
  - [By tag](https://moonrepo.dev/docs/concepts/target#by-tag)
- [Run scopes](https://moonrepo.dev/docs/concepts/target#run-scopes)
  - [All projects](https://moonrepo.dev/docs/concepts/target#all-projects)
  - [Closest project `~`](https://moonrepo.dev/docs/concepts/target#closest-project-)
- [Config scopes](https://moonrepo.dev/docs/concepts/target#config-scopes)
  - [Dependencies `^`](https://moonrepo.dev/docs/concepts/target#dependencies-)
  - [Owning project `~`](https://moonrepo.dev/docs/concepts/target#owning-project-)