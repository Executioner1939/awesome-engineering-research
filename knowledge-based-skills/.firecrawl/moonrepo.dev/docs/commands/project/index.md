[Skip to main content](https://moonrepo.dev/docs/commands/project#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon project [id]` (or `moon p`) command will display all available information about a project
that has been configured and exists within the graph. If a project does not exist, the program will
return with a 1 exit code.

```shell
$ moon project web
```

### Arguments [​](https://moonrepo.dev/docs/commands/project\#arguments "Direct link to Arguments")

- `[id]` \- ID or alias of a project, as defined in [`projects`](https://moonrepo.dev/docs/config/workspace#projects).

### Options [​](https://moonrepo.dev/docs/commands/project\#options "Direct link to Options")

- `--json` \- Print the project and its configuration as JSON.
- `--no-tasks` \- Do not list tasks for the project.

## Example output [​](https://moonrepo.dev/docs/commands/project\#example-output "Direct link to Example output")

The following output is an example of what this command prints, using our very own
`@moonrepo/runtime` package.

```text
RUNTIME

Project: runtime
Alias: @moonrepo/runtime
Source: packages/runtime
Root: ~/Projects/moon/packages/runtime
Toolchain: node
Language: typescript
Stack: unknown
Type: library

DEPENDS ON

  - types (implicit, production)

INHERITS FROM

  - .moon/tasks/node.yml

TASKS

build:
  › packemon build --addFiles --addExports --declaration
format:
  › prettier --check --config ../../prettier.config.js --ignore-path ../../.prettierignore --no-error-on-unmatched-pattern .
lint:
  › eslint --cache --cache-location ./.eslintcache --color --ext .js,.ts,.tsx --ignore-path ../../.eslintignore --exit-on-fatal-error --no-error-on-unmatched-pattern --report-unused-disable-directives .
lint-fix:
  › eslint --cache --cache-location ./.eslintcache --color --ext .js,.ts,.tsx --ignore-path ../../.eslintignore --exit-on-fatal-error --no-error-on-unmatched-pattern --report-unused-disable-directives . --fix
test:
  › jest --cache --color --preset jest-preset-moon --passWithNoTests
typecheck:
  › tsc --build

FILE GROUPS

configs:
  - packages/runtime/*.{js,json}
sources:
  - packages/runtime/src/**/*
  - packages/runtime/types/**/*
tests:
  - packages/runtime/tests/**/*
```

### Configuration [​](https://moonrepo.dev/docs/commands/project\#configuration "Direct link to Configuration")

- [`projects`](https://moonrepo.dev/docs/config/workspace#projects) in `.moon/workspace.*`
- [`project`](https://moonrepo.dev/docs/config/project#project) in `moon.*`

- [Arguments](https://moonrepo.dev/docs/commands/project#arguments)
- [Options](https://moonrepo.dev/docs/commands/project#options)
- [Example output](https://moonrepo.dev/docs/commands/project#example-output)
  - [Configuration](https://moonrepo.dev/docs/commands/project#configuration)