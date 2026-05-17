[Skip to main content](https://moonrepo.dev/docs/create-project#__docusaurus_skipToContent_fallback)

BunDenoGoNode.jsPHPPythonRubyRust

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

3 min

With a [workspace](https://moonrepo.dev/docs/setup-workspace), we can now house one or many [projects](https://moonrepo.dev/docs/concepts/project),
with a project being an application, library, or more. In the end, each project will have its own
build layer, personal tasks, and custom configuration.

## Declaring a project in the workspace [​](https://moonrepo.dev/docs/create-project\#declaring-a-project-in-the-workspace "Direct link to Declaring a project in the workspace")

Although a project may exist in your repository, it's not accessible from moon until it's been
mapped in the [`projects`](https://moonrepo.dev/docs/config/workspace#projects) setting found in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace). When mapping a project, we require a unique name for the
project, and a project source location (path relative from the workspace root).

Let's say we have a frontend web application called "client", and a backend application called
"server", our `projects` setting would look like the following.

.moon/workspace.yml

```yaml
projects:
  client: 'apps/client'
  server: 'apps/server'
```

We can now run [`moon project client`](https://moonrepo.dev/docs/commands/project) and
[`moon project server`](https://moonrepo.dev/docs/commands/project) to display information about each project. If these
projects were not mapped, or were pointing to an invalid source, the command would throw an error.

success

The [`projects`](https://moonrepo.dev/docs/config/workspace#projects) setting also supports a list of globs, if you'd prefer
to not manually curate the projects list!

## Configuring a project [​](https://moonrepo.dev/docs/create-project\#configuring-a-project "Direct link to Configuring a project")

A project can be configured in 1 of 2 ways:

- Through the [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks) config files, which defines file groups and tasks
that are inherited by _matching_ projects within the workspace. Perfect for standardizing common
tasks like linting, typechecking, and code formatting.
- Through the [`<project>/moon.*`](https://moonrepo.dev/docs/config/project) config file, found at the root of each project,
which defines files groups, tasks, dependencies, and more that are unique to that project.

Both config files are optional, and can be used separately or together, the choice is yours!

Now let's continue with our client and server example above. If we wanted to configure both
projects, and define config that's also shared between the 2, we could do something like the
following:

- Client
- Server
- Both (inherited)

apps/client/moon.yml

```yaml
tasks:
  build:
    command: 'vite dev'
    inputs:
      - 'src/**/*'
    outputs:
      - 'dist'
```

apps/server/moon.yml

```yaml
tasks:
  build:
    command: 'babel src --out-dir build'
    inputs:
      - 'src/**/*'
    outputs:
      - 'build'
```

.moon/tasks/all.yml

```yaml
tasks:
  format:
    command: 'prettier --check .'
  lint:
    command: 'eslint --no-error-on-unmatched-pattern .'
  test:
    command: 'jest --passWithNoTests .'
  typecheck:
    command: 'tsc --build'
```

### Adding optional metadata [​](https://moonrepo.dev/docs/create-project\#adding-optional-metadata "Direct link to Adding optional metadata")

When utilizing moon in a large monorepo or organization, ownership becomes very important, but also
difficult to maintain. To combat this problem, moon supports the
[`project`](https://moonrepo.dev/docs/config/project#project) field within a project's [`moon.*`](https://moonrepo.dev/docs/config/project) config.

This field is _optional_ by default, but when defined it provides metadata about the project,
specifically around team ownership, which developers maintain the project, where to discuss it, and
more!

Furthermore, we also support the [`layer`](https://moonrepo.dev/docs/config/project#layer) and
[`language`](https://moonrepo.dev/docs/config/project#language) settings for a more granular breakdown of what exists in the
repository.

<project>/moon.yml

```yaml
layer: 'tool'
language: 'typescript'

project:
  name: 'moon'
  description: 'A repo management tool.'
  channel: '#moon'
  owner: 'infra.platform'
  maintainers: ['miles.johnson']
```

## Next steps [​](https://moonrepo.dev/docs/create-project\#next-steps "Direct link to Next steps")

[Setup toolchain](https://moonrepo.dev/docs/setup-toolchain) [Configure `.moon/workspace.*` further](https://moonrepo.dev/docs/config/workspace) [Configure `.moon/tasks/**/*` further](https://moonrepo.dev/docs/config/tasks) [Configure `moon.*` further](https://moonrepo.dev/docs/config/project) [Learn about projects](https://moonrepo.dev/docs/concepts/project)

- [Declaring a project in the workspace](https://moonrepo.dev/docs/create-project#declaring-a-project-in-the-workspace)
- [Configuring a project](https://moonrepo.dev/docs/create-project#configuring-a-project)
  - [Adding optional metadata](https://moonrepo.dev/docs/create-project#adding-optional-metadata)
- [Next steps](https://moonrepo.dev/docs/create-project#next-steps)