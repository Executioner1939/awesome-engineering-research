[Skip to main content](https://moonrepo.dev/docs/concepts/task#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Tasks are commands that are ran in the context of a [project](https://moonrepo.dev/docs/concepts/project). Underneath the hood, a
task is simply a binary or system command that is ran as a child process.

## IDs [​](https://moonrepo.dev/docs/concepts/task\#ids "Direct link to IDs")

A task identifier (or name) is a unique resource for locating a task _within_ a project. The ID is
explicitly configured as a key within the [`tasks`](https://moonrepo.dev/docs/config/project#tasks) setting, and can be
written in camel/kebab/snake case. IDs support alphabetic unicode characters, `0-9`, `_`, `-`, `/`,
`.`, and must start with a character.

A task ID can be paired with a scope to create a [target](https://moonrepo.dev/docs/concepts/target).

## Types [​](https://moonrepo.dev/docs/concepts/task\#types "Direct link to Types")

Tasks are grouped into 1 of the following types based on their configured parameters.

- **Build** \- Task generates one or many artifacts, and is derived from the
[`outputs`](https://moonrepo.dev/docs/config/project#outputs) setting.
- **Run** \- Task runs a one-off, long-running, or never-ending process, and is derived from the
[`options.persistent`](https://moonrepo.dev/docs/config/project#persistent) setting.
- **Test** \- Task asserts code is correct and behaves as expected. This includes linting,
typechecking, unit tests, and any other form of testing. Is the default.

## Modes [​](https://moonrepo.dev/docs/concepts/task\#modes "Direct link to Modes")

Alongside types, tasks can also grouped into a special mode that provides unique handling within the
action graph and pipelines.

### Local server [​](https://moonrepo.dev/docs/concepts/task\#local-server "Direct link to Local server")

Tasks either run locally, in CI (continuous integration pipelines), or both. For tasks that should
_only_ be ran locally, for example, development servers, we provide a mechanism for marking a task
as local only server. When enabled, caching is turned off, the task will not run in CI, terminal
output is not captured, and the task is marked as [persistent](https://moonrepo.dev/docs/concepts/task#persistent).

To mark a task as local only, enable the [`preset`](https://moonrepo.dev/docs/config/project#preset) setting.

moon.yml

```yaml
tasks:
  dev:
    command: 'start-dev-server'
    preset: 'server'
```

### Internal onlyv1.23.0 [​](https://moonrepo.dev/docs/concepts/task\#internal-only "Direct link to internal-only")

Internal tasks are tasks that are not meant to be ran explicitly by the user (via the command line),
but are used internally as dependencies of other tasks. Additionally, internal tasks are not
displayed in a project's tasks list, but can be inspected with [`moon task`](https://moonrepo.dev/docs/commands/task).

To mark a task as internal, enable the [`options.internal`](https://moonrepo.dev/docs/config/project#internal) setting.

moon.yml

```yaml
tasks:
  prepare:
    command: 'intermediate-step'
    options:
      internal: true
```

### Interactivev1.12.0 [​](https://moonrepo.dev/docs/concepts/task\#interactive "Direct link to interactive")

Tasks that need to interact with the user via terminal prompts are known as interactive tasks.
Because interactive tasks require stdin, and it's not possible to have multiple parallel running
tasks interact with stdin, we isolate interactive tasks from other tasks in the action graph. This
ensures that only 1 interactive task is ran at a time.

To mark a task as interactive, enable the [`options.interactive`](https://moonrepo.dev/docs/config/project#interactive)
setting.

moon.yml

```yaml
tasks:
  init:
    command: 'init-app'
    options:
      interactive: true
```

### Persistentv1.6.0 [​](https://moonrepo.dev/docs/concepts/task\#persistent "Direct link to persistent")

Tasks that never complete, like servers and watchers, are known as persistent tasks. Persistent
tasks are typically problematic when it comes to dependency graphs, because if they run in the
middle of the graph, subsequent tasks will never run because the persistent task never completes!

However in moon, this is a non-issue, as we collect all persistent tasks within the action graph and
run them _last as a batch_. This is perfect for a few reasons:

- All persistent tasks are ran in parallel, so they don't block each other.
- Running both the backend API and frontend webapp in parallel is a breeze.
- Dependencies of persistent tasks are guaranteed to have ran and completed.

To mark a task as persistent, enable the [`options.persistent`](https://moonrepo.dev/docs/config/project#persistent)
setting.

moon.yml

```yaml
tasks:
  dev:
    command: 'start-dev-server'
    options:
      persistent: true
    # OR
    preset: 'server'
```

## Configuration [​](https://moonrepo.dev/docs/concepts/task\#configuration "Direct link to Configuration")

Tasks can be configured per project through [`moon.*`](https://moonrepo.dev/docs/config/project), or for many projects
through [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks).

### Commands vs Scripts [​](https://moonrepo.dev/docs/concepts/task\#commands-vs-scripts "Direct link to Commands vs Scripts")

A task is either a command or script, but not both. So what's the difference exactly? In the context
of a moon task, a command is a single binary execution with optional arguments, configured with the
[`command`](https://moonrepo.dev/docs/config/project#command) and [`args`](https://moonrepo.dev/docs/config/project#args) settings (which both
support a string or array). While a script is one or many binary executions, with support for pipes
and redirects, and configured with the [`script`](https://moonrepo.dev/docs/config/project#script) setting (which is only a
string).

A command also supports merging during task inheritance, while a script does not and will always
replace values. Refer to the table below for more differences between the 2.

|  | Command | Script |
| --- | --- | --- |
| Configured as | string, array | string |
| Inheritance merging | ✅ via `mergeArgs` option | ⚠️ always replaces |
| Additional args | ✅ via `args` setting | ❌ |
| Passthrough args (from CLI) | ✅ | ❌ |
| Multiple commands (with `&&` or `;`) | ❌ | ✅ |
| Pipes, redirects, etc | ❌ | ✅ |
| Always ran in a shell | ❌ | ✅ |
| Custom platform/toolchain | ✅ | ✅ |
| [Token](https://moonrepo.dev/docs/concepts/token) functions and variables | ✅ | ✅ |

### Inheritance [​](https://moonrepo.dev/docs/concepts/task\#inheritance "Direct link to Inheritance")

View the official documentation on [task inheritance](https://moonrepo.dev/docs/concepts/task-inheritance).

- [IDs](https://moonrepo.dev/docs/concepts/task#ids)
- [Types](https://moonrepo.dev/docs/concepts/task#types)
- [Modes](https://moonrepo.dev/docs/concepts/task#modes)
  - [Local server](https://moonrepo.dev/docs/concepts/task#local-server)
  - [Internal only](https://moonrepo.dev/docs/concepts/task#internal-only)
  - [Interactive](https://moonrepo.dev/docs/concepts/task#interactive)
  - [Persistent](https://moonrepo.dev/docs/concepts/task#persistent)
- [Configuration](https://moonrepo.dev/docs/concepts/task#configuration)
  - [Commands vs Scripts](https://moonrepo.dev/docs/concepts/task#commands-vs-scripts)
  - [Inheritance](https://moonrepo.dev/docs/concepts/task#inheritance)