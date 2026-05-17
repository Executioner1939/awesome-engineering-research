[Skip to main content](https://moonrepo.dev/docs/commands/task#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.1.0

The `moon task [target]` (or `moon t`) command will display information about a task that has been
configured and exists within a project. If a task does not exist, the program will return with a 1
exit code.

```shell
$ moon task web:build
```

### Arguments [​](https://moonrepo.dev/docs/commands/task\#arguments "Direct link to Arguments")

- `[target]` \- Fully qualified project + task target.

### Options [​](https://moonrepo.dev/docs/commands/task\#options "Direct link to Options")

- `--json` \- Print the task and its configuration as JSON.

## Example output [​](https://moonrepo.dev/docs/commands/task\#example-output "Direct link to Example output")

The following output is an example of what this command prints, using our very own
`@moonrepo/runtime` package.

```text
RUNTIME:BUILD

Task: build
Project: runtime
Toolchain: node
Type: build

PROCESS

Command: packemon build --addFiles --addExports --declaration
Environment variables:
  - NODE_ENV = production
Working directory: ~/Projects/moon/packages/runtime
Runs dependencies: Concurrently
Runs in CI: Yes

DEPENDS ON

  - types:build

INHERITS FROM

  - .moon/tasks/node.yml

INPUTS

  - .moon/*.yml
  - .moon/tasks/node.yml
  - packages/runtime/package.json
  - packages/runtime/src/**/*
  - packages/runtime/tsconfig.*.json
  - packages/runtime/tsconfig.json
  - packages/runtime/types/**/*
  - tsconfig.options.json

OUTPUTS

  - packages/runtime/cjs
```

### Configuration [​](https://moonrepo.dev/docs/commands/task\#configuration "Direct link to Configuration")

- [`tasks`](https://moonrepo.dev/docs/config/tasks#tasks) in `.moon/tasks/*`
- [`tasks`](https://moonrepo.dev/docs/config/project#tasks) in `moon.*`

- [Arguments](https://moonrepo.dev/docs/commands/task#arguments)
- [Options](https://moonrepo.dev/docs/commands/task#options)
- [Example output](https://moonrepo.dev/docs/commands/task#example-output)
  - [Configuration](https://moonrepo.dev/docs/commands/task#configuration)