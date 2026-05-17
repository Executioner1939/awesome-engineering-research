[Skip to main content](https://moonrepo.dev/docs/concepts/file-group#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

File groups are a mechanism for grouping similar types of files and environment variables within a
project using [file glob patterns or literal file paths](https://moonrepo.dev/docs/concepts/file-pattern). These groups are then used
by [tasks](https://moonrepo.dev/docs/concepts/task) to calculate functionality like cache computation, affected files since last
change, deterministic builds, and more.

## Configuration [​](https://moonrepo.dev/docs/concepts/file-group\#configuration "Direct link to Configuration")

File groups can be configured per project through [`moon.*`](https://moonrepo.dev/docs/config/project), or for many
projects through [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks).

### Token functions [​](https://moonrepo.dev/docs/concepts/file-group\#token-functions "Direct link to Token functions")

File groups can be referenced in [tasks](https://moonrepo.dev/docs/concepts/task) using [token functions](https://moonrepo.dev/docs/concepts/token). For example, the
`@group(name)` token will expand to all paths configured in the `sources` file group.

moon.yml

```yaml
tasks:
  build:
    command: 'vite build'
    inputs:
      - '@group(sources)'
```

## Inheritance and merging [​](https://moonrepo.dev/docs/concepts/file-group\#inheritance-and-merging "Direct link to Inheritance and merging")

When a file group of the same name exists in both [configuration files](https://moonrepo.dev/docs/concepts/file-group#configuration), the
project-level group will override the workspace-level group, and all other workspace-level groups
will be inherited as-is.

A primary scenario in which to define file groups at the project-level is when you want to
_override_ file groups defined at the workspace-level. For example, say we want to override the
`sources` file group because our source folder is named "lib" and not "src", we would define our
file groups as followed.

.moon/tasks/all.yml

```yaml
fileGroups:
  sources:
    - 'src/**/*'
    - 'types/**/*'
  tests:
    - 'tests/**/*.test.*'
    - '**/__tests__/**/*'
```

moon.yml

```yaml
fileGroups:
  # Overrides global
  sources:
    - 'lib/**/*'
    - 'types/**/*'
  # Inherited as-is
  tests:
    - 'tests/**/*.test.*'
    - '**/__tests__/**/*'
```

- [Configuration](https://moonrepo.dev/docs/concepts/file-group#configuration)
  - [Token functions](https://moonrepo.dev/docs/concepts/file-group#token-functions)
- [Inheritance and merging](https://moonrepo.dev/docs/concepts/file-group#inheritance-and-merging)