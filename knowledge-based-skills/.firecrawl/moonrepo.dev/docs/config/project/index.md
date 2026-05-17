[Skip to main content](https://moonrepo.dev/docs/config/project#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon.*` configuration file _is not required_ but can be used to define additional metadata for
a project, override inherited tasks, and more at the project-level. When used, this file must exist
in a project's root, as configured in [`projects`](https://moonrepo.dev/docs/config/workspace#projects).

## `dependsOn` [​](https://moonrepo.dev/docs/config/project\#dependson "Direct link to dependson")

Explicitly defines _other_ projects that _this_ project depends on, primarily when generating the
project and task graphs. The most common use case for this is building those projects _before_
building this one. When defined, this setting requires an array of project names, which are the keys
found in the [`projects`](https://moonrepo.dev/docs/config/workspace#projects) map.

moon.yml

```yaml
dependsOn:
  - 'apiClients'
  - 'designSystem'
```

A dependency object can also be defined, where a specific `scope` can be assigned, which accepts
"production" (default), "development", "build", or "peer".

moon.yml

```yaml
dependsOn:
  - id: 'apiClients'
    scope: 'production'
  - id: 'designSystem'
    scope: 'peer'
```

> Learn more about [implicit and explicit dependencies](https://moonrepo.dev/docs/concepts/project#dependencies).

## Metadata [​](https://moonrepo.dev/docs/config/project\#metadata "Direct link to Metadata")

## `id`v1.18.0 [​](https://moonrepo.dev/docs/config/project\#id "Direct link to id")

Overrides the name (identifier) of the project, which was configured in or derived from the
[`projects`](https://moonrepo.dev/docs/config/workspace#projects) setting in [`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace). This setting is
useful when using glob based project location, and want to avoid using the folder name as the
project name.

moon.yml

```yaml
id: 'custom-id'
```

info

All references to the project must use the new identifier, including project and task dependencies.

## `language` [​](https://moonrepo.dev/docs/config/project\#language "Direct link to language")

The primary programming language the project is written in. This setting is required for
[task inheritance](https://moonrepo.dev/docs/config/tasks), editor extensions, and more. Supports the following values:

- `bash` \- A [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) based project (Unix only).
- `batch` \- A [Batch](https://en.wikibooks.org/wiki/Windows_Batch_Scripting)/PowerShell based
project (Windows only).
- `go` \- A [Go](https://go.dev/) based project.
- `javascript` \- A [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) based
project.
- `php` \- A [PHP](https://www.php.net/) based project.
- `python` \- A [Python](https://www.python.org/) based project.
- `ruby` \- A [Ruby](https://www.ruby-lang.org/en/) based project.
- `rust` \- A [Rust](https://www.rust-lang.org/) based project.
- `typescript` \- A [TypeScript](https://www.typescriptlang.org/) based project.
- `unknown` (default) - When not configured or inferred.
- `*` \- A custom language. Values will be converted to kebab-case.

moon.yml

```yaml
language: 'javascript'

# Custom
language: 'kotlin'
```

> For convenience, when this setting is not defined, moon will attempt to detect the language based
> on configuration files found in the project root. This only applies to non-custom languages!

## `owners`v1.8.0 [​](https://moonrepo.dev/docs/config/project\#owners "Direct link to owners")

Defines ownership of source code within the current project, by mapping file system paths to owners.
An owner is either a user, team, or group.

Currently supports
[GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners),
[GitLab](https://docs.gitlab.com/ee/user/project/codeowners/reference.html), and
[Bitbucket](https://marketplace.atlassian.com/apps/1218598/code-owners-for-bitbucket?tab=overview&hosting=cloud)
(via app).

### `customGroups`Bitbucket [​](https://moonrepo.dev/docs/config/project\#customgroups "Direct link to customgroups")

When using the
[Code Owners for Bitbucket](https://marketplace.atlassian.com/apps/1218598/code-owners-for-bitbucket?tab=overview&hosting=cloud)
app, this setting provides a way to define custom groups that will be injected at the top of the
`CODEOWNERS` file. These groups _must_ be unique across all projects.

moon.yml

```yaml
owners:
  customGroups:
    '@@@backend': ['@"user name"', '@@team']
```

### `defaultOwner` [​](https://moonrepo.dev/docs/config/project\#defaultowner "Direct link to defaultowner")

The default owner for all [`paths`](https://moonrepo.dev/docs/config/project#paths). This setting is optional in some cases but helps to
avoid unnecessary repetition.

moon.yml

```yaml
owners:
  defaultOwner: '@frontend'
```

### `optional`GitLab [​](https://moonrepo.dev/docs/config/project\#optional "Direct link to optional")

For GitLab, marks the project's
[code owners section](https://docs.gitlab.com/ee/user/project/codeowners/reference.html#optional-sections)
as optional. Defaults to `false`.

moon.yml

```yaml
owners:
  optional: true
```

### `paths` [​](https://moonrepo.dev/docs/config/project\#paths "Direct link to paths")

The primary setting for defining ownership of source code within the current project. This setting
supports 2 formats, the first being a list of file paths relative from the current project. This
format requires [`defaultOwner`](https://moonrepo.dev/docs/config/project#defaultowner) to be defined, and only supports 1 owner for every
path (the default owner).

moon.yml

```yaml
owners:
  defaultOwner: '@frontend'
  paths:
    - '**/*.ts'
    - '**/*.tsx'
    - '*.config.js'
```

The second format provides far more granularity, allowing for multiple owners per path. This format
requires a map, where the key is a file path relative from the current project, and the value is a
list of owners. Paths with an empty list of owners will fallback to [`defaultOwner`](https://moonrepo.dev/docs/config/project#defaultowner).

moon.yml

```yaml
owners:
  defaultOwner: '@frontend'
  paths:
    '**/*.rs': ['@backend']
    '**/*.js': []
    '*.config.js': ['@frontend', '@frontend-infra']
```

> The syntax for owners is dependent on the provider you are using for version control (GitHub,
> GitLab, Bitbucket). moon provides no validation or guarantees that these are correct.

### `requiredApprovals`Bitbucket / GitLab [​](https://moonrepo.dev/docs/config/project\#requiredapprovals "Direct link to requiredapprovals")

Requires a specific number of approvals for a pull/merge request to be satisfied. Defaults to `1`.

- For Bitbucket, defines the
[`Check()` condition](https://docs.mibexsoftware.com/codeowners/merge-checks#MergeChecks-2.MergeChecks:HowmanyoftheseCodeOwnersneedtoapprovebeforeapullrequestcanbemerged?)
when using a [`defaultOwner`](https://moonrepo.dev/docs/config/project#defaultowner).
- For GitLab, defines a requirement on the
[code owners section](https://docs.gitlab.com/ee/user/project/codeowners/reference.html#sections-requiring-multiple-approvals).

moon.yml

```yaml
owners:
  requiredApprovals: 2
```

## `layer` [​](https://moonrepo.dev/docs/config/project\#layer "Direct link to layer")

The layer within a [stack](https://moonrepo.dev/docs/config/project#stack). Supports the following values:

- `application` \- An application of any kind.
- `automation` \- An automated testing suite, like E2E, integration, or visual tests.v1.16.0
- `configuration` \- Configuration files or infrastructure.v1.22.0
- `library` \- A self-contained, shareable, and publishable set of code.
- `scaffolding` \- Templates or generators for scaffolding.v1.22.0
- `tool` \- An internal tool, CLI, one-off script, etc.
- `unknown` (default) - When not configured.

moon.yml

```yaml
layer: 'application'
```

info

The project layer is used in [task inheritance](https://moonrepo.dev/docs/concepts/task-inheritance),
[constraints and boundaries](https://moonrepo.dev/docs/config/workspace#constraints), editor extensions, and more!

## `project` [​](https://moonrepo.dev/docs/config/project\#project "Direct link to project")

The `project` setting defines metadata about the project itself.

moon.yml

```yaml
project:
  title: 'moon'
  description: 'A monorepo management tool.'
  channel: '#moon'
  owner: 'infra.platform'
  maintainers: ['miles.johnson']
```

The information listed within `project` is purely informational and primarily displayed within the
CLI. However, this setting exists for you, your team, and your company, as a means to identify and
organize all projects. Feel free to build your own tooling around these settings!

### `channel` [​](https://moonrepo.dev/docs/config/project\#channel "Direct link to channel")

The Slack, Discord, Teams, IRC, etc channel name (with leading #) in which to discuss the project.

### `description`Required [​](https://moonrepo.dev/docs/config/project\#description "Direct link to description")

A description of what the project does and aims to achieve. Be as descriptive as possible, as this
is the kind of information search engines would index on.

### `maintainers` [​](https://moonrepo.dev/docs/config/project\#maintainers "Direct link to maintainers")

A list of people/developers that maintain the project, review code changes, and can provide support.
Can be a name, email, LDAP name, GitHub username, etc, the choice is yours.

### `title` [​](https://moonrepo.dev/docs/config/project\#title "Direct link to title")

A human readable name of the project. This is _different_ from the unique project name configured in
[`projects`](https://moonrepo.dev/docs/config/workspace#projects).

### `owner` [​](https://moonrepo.dev/docs/config/project\#owner "Direct link to owner")

The team or organization that owns the project. Can be a title, LDAP name, GitHub team, etc. We
suggest _not_ listing people/developers as the owner, use [maintainers](https://moonrepo.dev/docs/config/project#maintainers) instead.

### Custom fieldsv2.0.0 [​](https://moonrepo.dev/docs/config/project\#custom-fields "Direct link to custom-fields")

Additional fields can be configured as custom metadata to associate to this project. Supports all
value types that are valid JSON.

moon.yml

```yaml
project:
  # ...
  deprecated: true
```

## `stack`v1.22.0 [​](https://moonrepo.dev/docs/config/project\#stack "Direct link to stack")

The technology stack this project belongs to, primarily for categorization. Supports the following
values:

- `backend` \- Server-side APIs, etc.
- `data` \- Data sources, database layers, etc. v2.0.0
- `frontend` \- Client-side user interfaces, etc.
- `infrastructure` \- Cloud/server infrastructure, Docker, etc.
- `systems` \- Low-level systems programming.
- `unknown` (default) - When not configured.

moon.yml

```yaml
stack: 'frontend'
```

info

The project stack is also used in [constraints and boundaries](https://moonrepo.dev/docs/config/workspace#constraints)!

## `tags` [​](https://moonrepo.dev/docs/config/project\#tags "Direct link to tags")

Tags are a simple mechanism for categorizing projects. They can be used to group projects together
for [easier querying](https://moonrepo.dev/docs/commands/query/projects), enforcing of
[project boundaries and constraints](https://moonrepo.dev/docs/config/workspace#constraints),
[task inheritance](https://moonrepo.dev/docs/concepts/task-inheritance), and more.

moon.yml

```yaml
tags:
  - 'react'
  - 'prisma'
```

## Integrations [​](https://moonrepo.dev/docs/config/project\#integrations "Direct link to Integrations")

## `docker`v1.27.0 [​](https://moonrepo.dev/docs/config/project\#docker "Direct link to docker")

Configures Docker integration for the current project.

### `file` [​](https://moonrepo.dev/docs/config/project\#file "Direct link to file")

Configures the `Dockerfile` generation process when [`moon docker file`](https://moonrepo.dev/docs/commands/docker/file) is
executed.

#### `buildTask` [​](https://moonrepo.dev/docs/config/project\#buildtask "Direct link to buildtask")

The name of a task within the current project that will be used for building the project before
running it. If not defined, does nothing.

moon.yml

```yaml
docker:
  file:
    buildTask: 'build'
```

#### `image` [​](https://moonrepo.dev/docs/config/project\#image "Direct link to image")

The Docker image to use in the base stage. Defaults to an image based on the first detected
toolchain.

moon.yml

```yaml
docker:
  file:
    image: 'node:latest'
```

#### `runPrune`v2.0.0 [​](https://moonrepo.dev/docs/config/project\#runprune "Direct link to runprune")

Run the `moon docker prune` command after building the project, but before starting it. Defaults to
`true`.

moon.yml

```yaml
docker:
  file:
    runPrune: false
```

#### `runSetup`v2.0.0 [​](https://moonrepo.dev/docs/config/project\#runsetup "Direct link to runsetup")

Run the `moon docker setup` command after scaffolding, but before building the project. Defaults to
`true`.

moon.yml

```yaml
docker:
  file:
    runSetup: false
```

#### `startTask` [​](https://moonrepo.dev/docs/config/project\#starttask "Direct link to starttask")

The name of a task within the current project that will run the project after it has been built (if
required). This task will be used as `CMD` within the `Dockerfile`.

moon.yml

```yaml
docker:
  file:
    startTask: 'start'
```

#### `template`v2.0.0 [​](https://moonrepo.dev/docs/config/project\#template "Direct link to template")

A custom template file, relative from the workspace root, to use when rendering the `Dockerfile`.
Powered by Tera.

moon.yml

```yaml
docker:
  file:
    template: 'templates/Dockerfile.tera'
```

### `scaffold` [​](https://moonrepo.dev/docs/config/project\#scaffold "Direct link to scaffold")

Configures aspects of the Docker scaffolding process when
[`moon docker scaffold`](https://moonrepo.dev/docs/commands/docker/scaffold) is executed. Only applies to the
[sources skeleton](https://moonrepo.dev/docs/commands/docker/scaffold#sources).

#### `configsPhaseGlobs` [​](https://moonrepo.dev/docs/config/project\#configsphaseglobs "Direct link to configsphaseglobs")

List of globs in which to copy project-relative files into the `.moon/docker/configs` skeleton. When
not defined, defaults to `**/*`. Applies to both project and workspace level scaffolding.

moon.yml

```yaml
docker:
  scaffold:
    configsPhaseGlobs:
      - '*.json'
```

#### `sourcesPhaseGlobs` [​](https://moonrepo.dev/docs/config/project\#sourcesphaseglobs "Direct link to sourcesphaseglobs")

List of globs in which to copy project-relative files into the `.moon/docker/sources` skeleton. When
not defined, defaults to `**/*`. Applies to both project and workspace level scaffolding.

moon.yml

```yaml
docker:
  scaffold:
    sourcesPhaseGlobs:
      - 'src/**/*'
```

## Tasks [​](https://moonrepo.dev/docs/config/project\#tasks "Direct link to Tasks")

## `env` [​](https://moonrepo.dev/docs/config/project\#env "Direct link to env")

The `env` field is map of strings that are passed as environment variables to _all tasks_ within the
current project. Project-level variables will not override task-level variables of the same name.

moon.yml

```yaml
env:
  NODE_ENV: 'production'
```

> View the task [`env`](https://moonrepo.dev/docs/config/project#env-1) setting for more usage examples and information.

## `fileGroups` [​](https://moonrepo.dev/docs/config/project\#filegroups "Direct link to filegroups")

Defines [file groups](https://moonrepo.dev/docs/concepts/file-group) to be used by local tasks. By default, this setting
_is not required_ for the following reasons:

- File groups are an optional feature, and are designed for advanced use cases.
- File groups defined in [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks) will be inherited by all projects.

When defined this setting requires a map, where the key is the file group name, and the value is a
list of [globs or file paths](https://moonrepo.dev/docs/concepts/file-pattern), or environment variables. Globs and paths
are [relative to a project](https://moonrepo.dev/docs/concepts/file-pattern#project-relative) (even when defined
[globally](https://moonrepo.dev/docs/config/tasks)).

moon.yml

```yaml
# Example groups
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

Once your groups have been defined, you can reference them within [`args`](https://moonrepo.dev/docs/config/project#args),
[`inputs`](https://moonrepo.dev/docs/config/project#inputs), [`outputs`](https://moonrepo.dev/docs/config/project#outputs), and more, using
[token functions and variables](https://moonrepo.dev/docs/concepts/token).

moon.yml

```yaml
tasks:
  build:
    command: 'vite build'
    inputs:
      - '@group(configs)'
      - '@group(sources)'
```

## `tasks` [​](https://moonrepo.dev/docs/config/project\#tasks-1 "Direct link to tasks-1")

Tasks are actions that are ran within the context of a [project](https://moonrepo.dev/docs/concepts/project), and commonly
wrap an npm binary or system command. This setting requires a map, where the key is a unique name
for the task, and the value is an object of task parameters.

moon.yml

```yaml
tasks:
  format:
    command: 'prettier'
  lint:
    command: 'eslint'
  test:
    command: 'jest'
  typecheck:
    command: 'tsc'
```

### `extends`v1.12.0 [​](https://moonrepo.dev/docs/config/project\#extends "Direct link to extends")

The `extends` field can be used to extend the settings from a sibling task within the same project,
or [inherited from the global scope](https://moonrepo.dev/docs/concepts/task-inheritance). This is useful for composing
similar tasks with different arguments or options.

When extending another task, the same
[merge strategies](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) used for inheritance are applied.

moon.yml

```yaml
tasks:
  lint:
    command: 'eslint .'
    inputs:
      - 'src/**/*'

  lint-fix:
    extends: 'lint'
    args: '--fix'
    preset: 'utility'
```

### `description`v1.22.0 [​](https://moonrepo.dev/docs/config/project\#description-1 "Direct link to description-1")

A human-readable description of what the task does. This information is displayed within the
[`moon project`](https://moonrepo.dev/docs/commands/project) and [`moon task`](https://moonrepo.dev/docs/commands/task) commands.

moon.yml

```yaml
tasks:
  build:
    description: 'Builds the project using Vite'
    command: 'vite build'
```

### `command` [​](https://moonrepo.dev/docs/config/project\#command "Direct link to command")

The `command` field is a _single_ command to execute for the task, including the command binary/name
(must be first) and any optional [arguments](https://moonrepo.dev/docs/config/project#args). This field supports task inheritance and
merging of arguments.

This setting can be defined using a string, or an array of strings. We suggest using arrays when
dealing with many args, or the args string cannot be parsed easily.

moon.yml

```yaml
tasks:
  format:
    # Using a string
    command: 'prettier --check .'
    # Using an array
    command:
      - 'prettier'
      - '--check'
      - '.'
```

info

If you need to support pipes, redirects, or multiple commands, use [`script`](https://moonrepo.dev/docs/config/project#script) instead.
Learn more about [commands vs scripts](https://moonrepo.dev/docs/concepts/task#commands-vs-scripts).

### `args` [​](https://moonrepo.dev/docs/config/project\#args "Direct link to args")

The `args` field is a collection of _additional_ arguments to append to the [`command`](https://moonrepo.dev/docs/config/project#command)
when executing the task. This field exists purely to provide arguments for
[inherited tasks](https://moonrepo.dev/docs/config/tasks#tasks).

This setting can be defined using a string, or an array of strings. We suggest using arrays when
dealing with many args, or the args string cannot be parsed easily.

moon.yml

```yaml
tasks:
  test:
    command: 'jest'
    # Using a string
    args: '--color --maxWorkers 3'
    # Using an array
    args:
      - '--color'
      - '--maxWorkers'
      - '3'
```

However, for the array approach to work correctly, each argument _must_ be its own distinct item,
including argument values. For example:

moon.yml

```yaml
tasks:
  test:
    command: 'jest'
    args:
      # Valid
      - '--maxWorkers'
      - '3'
      # Also valid
      - '--maxWorkers=3'
      # Invalid
      - '--maxWorkers 3'
```

### `deps` [​](https://moonrepo.dev/docs/config/project\#deps "Direct link to deps")

The `deps` field is a list of other tasks (known as [targets](https://moonrepo.dev/docs/concepts/target)), either within
this project or found in another project, that will be executed _before_ this task. It achieves this
by generating a directed task graph based on the project graph.

moon.yml

```yaml
tasks:
  build:
    command: 'webpack'
    deps:
      - 'apiClients:build'
      - 'designSystem:build'
      # A task within the current project
      - 'codegen'
```

#### Args & env [​](https://moonrepo.dev/docs/config/project\#args--env "Direct link to Args & env")

Furthermore, for each dependency target, you can configure additional command line arguments and
environment variables that'll be passed to the dependent task when it is ran. The `args` field
supports a list of strings, while `env` is an object of key-value pairs.

moon.yml

```yaml
tasks:
  build:
    command: 'webpack'
    deps:
      - target: 'apiClients:build'
        args: ['--env', 'production']
        env:
          NODE_ENV: 'production'
```

> Dependencies of inherited tasks will be excluded and renamed according to the
> [`workspace.inheritedTasks`](https://moonrepo.dev/docs/config/project#inheritedtasks) setting. This process _only_ uses filters from the
> current project, and not filters from dependent projects. Furthermore, `args` and `env` are not
> deeply merged.

#### Optional [​](https://moonrepo.dev/docs/config/project\#optional-1 "Direct link to Optional")

By default, all dependencies are required to exist when tasks are being built and expanded, but this
isn't always true when dealing with composition and inheritance. For dependencies that may not exist
based on what's inherited, you can mark it as `optional`.

moon.yml

```yaml
tasks:
  build:
    command: 'webpack'
    deps:
      - target: 'apiClients:build'
        optional: true
```

### `env` [​](https://moonrepo.dev/docs/config/project\#env-1 "Direct link to env-1")

The `env` field is map of strings that are passed as environment variables when running the command.
Variables defined here will take precedence over those loaded with [`envFile`](https://moonrepo.dev/docs/config/project#envfile).

moon.yml

```yaml
tasks:
  build:
    command: 'webpack'
    env:
      NODE_ENV: 'production'
```

Variables also support substitution using the syntax `${VAR_NAME}`. When using substitution, only
variables in the current process can be referenced, and not those currently defined in `env`.

moon.yml

```yaml
tasks:
  build:
    command: 'webpack'
    env:
      APP_TARGET: '${REGION}-${ENVIRONMENT}'
```

### `inputs` [​](https://moonrepo.dev/docs/config/project\#inputs "Direct link to inputs")

The `inputs` field is a list of sources that calculate whether to execute this task based on the
environment and files that have been touched since the last time the task has been ran. If _not_
defined or inherited, then all files within a project are considered an input (`**/*`), excluding
root-level tasks.

Inputs support the following source types:

- Environment variables
- Environment variable wildcardsv1.22.0
- Files, folders, and globs
- [Token functions and variables](https://moonrepo.dev/docs/concepts/token)

moon.yml

```yaml
tasks:
  lint:
    command: 'eslint'
    inputs:
      # Config files anywhere within the project
      - '**/.eslintignore'
      - '**/.eslintrc.js'
      # Config files at the workspace root
      - '/.eslintignore'
      - '/.eslintrc.js'
      # Tokens
      - '$projectRoot'
      - '@group(sources)'
```

#### Environment variables [​](https://moonrepo.dev/docs/config/project\#environment-variables "Direct link to Environment variables")

Environment variables can be used as inputs and must start with a `$`. Wildcard variables can use
`*` to match any character.

moon.yml

```yaml
tasks:
  example:
    inputs:
      - '$FOO_CACHE'
      - '$FOO_*'
```

caution

When using an environment variable, we assume _it's not defined_ by default, and will trigger an
affected state when it _is_ defined. If the environment variable always exists, then the task will
always run and bypass the cache.

#### File paths [​](https://moonrepo.dev/docs/config/project\#file-paths "Direct link to File paths")

File paths support
[project and workspace relative file/folder patterns](https://moonrepo.dev/docs/concepts/file-pattern#project-relative).
They can be defined as a literal path, or a `file://` URI v1.39.0,
or as an object with a `file` property v1.39.0. Additionally, the
following parameters are supported as a URI query or as object fields:

- `content`, `match`, `matches` (`string`) \- When determining affected state, will match against the
file's content using the defined regex pattern, instead of relying on file existence.
- `optional` (`boolean`) \- When hashing and set to `true` and the file is missing, will not log a
warning. When set to `false` and the file is missing, will fail with an error. Defaults to logging
a warning.

moon.yml

```yaml
tasks:
  example:
    inputs:
      # Literal paths
      - 'project/relative/file.js'
      - '/workspace/relative/file.js'
      # Using file protocol
      - 'file://project/relative/file.js?optional'
      - 'file:///workspace/relative/file.js?content=a|b|c'
      # Using an object
      - file: 'project/relative/file.js'
        optional: true
      - file: '/workspace/relative/file.js'
        content: 'a|b|c'
```

#### File groupsv1.41.0 [​](https://moonrepo.dev/docs/config/project\#file-groups "Direct link to file-groups")

A file group input will reference the defined files/globs within from a file group in the current
project. It can be defined with a `group://` URI, or as an object with a `group` property.
Additionally, the following parameters are supported as a URI query or as object fields:

- `format`, `as` (`string`) \- The format in which to gather the file group results. Supported values
are `static` (default), `files`, `dirs`, `globs`, `envs`, and `root`.

moon.yml

```yaml
fileGroups:
  sources:
    - 'src/**/*'

tasks:
  build:
    # ...
    inputs:
      # Using group protocol
      - 'group://sources?format=dirs'
      # Using an object
      - group: 'sources'
        format: 'dirs'
```

#### Glob patterns [​](https://moonrepo.dev/docs/config/project\#glob-patterns "Direct link to Glob patterns")

Glob patterns support
[project and workspace relative file/folder patterns](https://moonrepo.dev/docs/concepts/file-pattern#project-relative).
They can be defined as a literal path, or a `glob://` URI v1.39.0,
or as an object with a `glob` property v1.39.0. Additionally, the
following parameters are supported as a URI query or as object fields:

- `cache` (`boolean`) \- When gathering inputs for hashing, defines whether the glob results should
be cached for the duration of the moon process. Defaults to `true`.

moon.yml

```yaml
tasks:
  example:
    inputs:
      # Literal paths
      - 'project/relative/file.*'
      - '/workspace/relative/**/*'
      # Using glob protocol
      - 'glob://project/relative/file.*?cache=false'
      - 'glob:///workspace/relative/**/*?cache'
      # Using an object
      - glob: 'project/relative/file.*'
        cache: false
      - glob: '/workspace/relative/**/*'
```

Globs can also be negated by prefixing the path with `!`, which will exclude all files that match
the glob.

moon.yml

```yaml
tasks:
  example:
    inputs:
      - '!**/*.md'
      - 'glob://!/workspace/relative/**/*'
      - glob: '!/workspace/relative/**/*'
```

warning

Glob patterns that contain `?`, for example `*.tsx?`, cannot be used in URI format, as it conflicts
with the query string syntax. Use the path or object format instead.

danger

Be aware that files that match the glob, but are ignored via `.gitignore` (or similar), will _not_
be considered an input. To work around this, use explicit file inputs.

#### External projectsv1.41.0 [​](https://moonrepo.dev/docs/config/project\#external-projects "Direct link to external-projects")

Tasks can also depend on files and globs from other projects within the same workspace. This is
useful for handling cross-project relationships without needing to define explicit task
dependencies.

External projects can be defined as a `project://` URI, or as an object with a `project` property,
both of which require a project identifier, or `^` for all dependent projects. Additionally, the
following parameters are supported as a URI query or as object fields:

- `group`, `fileGroup` (`id`) \- The name of a file group within the external project in which file
and glob patterns will be used for matching. Takes precedence over `filter`.
- `filter` (`string[]`) \- A list of
[project relative glob patterns](https://moonrepo.dev/docs/concepts/file-pattern#project-relative) that will be used for
matching.

If neither `group` nor `filter` are defined, all files within the external project are considered a
match (`**/*`).

moon.yml

```yaml
tasks:
  example:
    inputs:
      # Using project protocol
      - 'project://foo'
      - 'project://bar?group=sources'
      - 'project://baz?filter=src/**/*'
      # Using an object
      - project: 'foo'
      - project: 'bar'
        group: 'sources'
      - project: 'baz'
        filter: ['src/**/*']
```

### `outputs` [​](https://moonrepo.dev/docs/config/project\#outputs "Direct link to outputs")

The `outputs` field is a list of [files and folders](https://moonrepo.dev/docs/concepts/file-pattern#project-relative) that
are _created_ as a result of executing this task, typically from a build or compilation related
task. Outputs are necessary for [incremental caching and hydration](https://moonrepo.dev/docs/concepts/cache). If you'd
prefer to avoid that functionality, omit this field.

#### File paths [​](https://moonrepo.dev/docs/config/project\#file-paths-1 "Direct link to File paths")

File paths support
[project and workspace relative file/folder patterns](https://moonrepo.dev/docs/concepts/file-pattern#project-relative).
They can be defined as a literal path, or a `file://` URI v1.41.0,
or as an object with a `file` property v1.41.0. Additionally, the
following parameters are supported as a URI query or as object fields:

- `optional` (`boolean`) \- When archiving and set to `true` and the file is missing, will not fail
with a missing output error. Defaults to `false`.

moon.yml

```yaml
tasks:
  example:
    inputs:
      # Literal paths
      - 'build/'
      # Using file protocol
      - 'file://build/'
      # Using an object
      - file: 'build/'
        optional: true
```

#### Glob patterns [​](https://moonrepo.dev/docs/config/project\#glob-patterns-1 "Direct link to Glob patterns")

Glob patterns support
[project and workspace relative file/folder patterns](https://moonrepo.dev/docs/concepts/file-pattern#project-relative).
They can be defined as a literal path, or a `glob://` URI v1.41.0,
or as an object with a `glob` property v1.41.0. Additionally, the
following parameters are supported as a URI query or as object fields:

- `optional` (`boolean`) \- When archiving and set to `true` and the glob produced no results, will
not fail with a missing output error. Defaults to `false`.

moon.yml

```yaml
tasks:
  example:
    inputs:
      # Literal paths
      - 'build/**/*.js'
      - '!build/internal.js'
      # Using glob protocol
      - 'glob://build/**/*.js'
      # Using an object
      - glob: 'build/**/*.js'
```

warning

Glob patterns that contain `?`, for example `*.tsx?`, cannot be used in URI format, as it conflicts
with the query string syntax. Use the path or object format instead.

danger

When using globs and moon hydrates an output (a cache hit), all files not matching the glob will be
**deleted**. Ensure that all files critical for the build to function correctly are included.

### `preset`v1.28.0 [​](https://moonrepo.dev/docs/config/project\#preset "Direct link to preset")

Applies the chosen preset to the task. A preset defines a collection of task options that will be
inherited as the default, and can then be overridden within the task itself. The following presets
are available:

- `server`
  - [`cache`](https://moonrepo.dev/docs/config/project#cache) -\> Turned off
  - [`outputStyle`](https://moonrepo.dev/docs/config/project#outputstyle) -\> Set to "stream"
  - [`persistent`](https://moonrepo.dev/docs/config/project#persistent) -\> Turned on
  - [`runInCI`](https://moonrepo.dev/docs/config/project#runinci) -\> Turned off
- `utility`v2.0.0
  - [`cache`](https://moonrepo.dev/docs/config/project#cache) -\> Turned off
  - [`interactive`](https://moonrepo.dev/docs/config/project#interactive) -\> Turned on
  - [`outputStyle`](https://moonrepo.dev/docs/config/project#outputstyle) -\> Set to "stream"
  - [`persistent`](https://moonrepo.dev/docs/config/project#persistent) -\> Turned off
  - [`runInCI`](https://moonrepo.dev/docs/config/project#runinci) -\> Skipped

Tasks named "dev", "start", or "serve" are marked as `server` automatically.

moon.yml

```yaml
tasks:
  dev:
    command: 'webpack server'
    preset: 'server'
```

### `script`v1.27.0 [​](https://moonrepo.dev/docs/config/project\#script "Direct link to script")

The `script` field is _one or many_ commands to execute for the task, with support for pipes,
redirects, and more. This field does _not_ support task inheritance merging, and can only be defined
with a string.

If defined, will supersede [`command`](https://moonrepo.dev/docs/config/project#command) and [`args`](https://moonrepo.dev/docs/config/project#args).

moon.yml

```yaml
tasks:
  exec:
    # Single command
    script: 'cp ./in ./out'
    # Multiple commands
    script: 'rm -rf ./out && cp ./in ./out'
    # Pipes
    script: 'ps aux | grep 3000'
    # Redirects
    script: './gen.sh > out.json'
```

info

If you need to support merging during task inheritance, use [`command`](https://moonrepo.dev/docs/config/project#command) instead. Learn
more about [commands vs scripts](https://moonrepo.dev/docs/concepts/task#commands-vs-scripts).

### `toolchains`v1.31.0 [​](https://moonrepo.dev/docs/config/project\#toolchains "Direct link to toolchains")

The `toolchain` field defines additional [toolchain(s)](https://moonrepo.dev/docs/concepts/toolchain) the command runs on,
where to locate its executable, and more. By default, moon will set to a value based on the
project's [`language`](https://moonrepo.dev/docs/config/project#language), default [`toolchains.default`](https://moonrepo.dev/docs/config/project#toolchain-1), or via detection.

moon.yml

```yaml
tasks:
  env:
    command: 'printenv'
    toolchains: 'system'
```

This setting also supports multiple values.

moon.yml

```yaml
tasks:
  build:
    command: 'npm run build'
    toolchains: ['javascript', 'node', 'npm']
```

### `options` [​](https://moonrepo.dev/docs/config/project\#options "Direct link to options")

The `options` field is an object of configurable options that can be used to modify the task and its
execution. The following fields can be provided, with merge related fields supporting all
[merge strategies](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies).

moon.yml

```yaml
tasks:
  typecheck:
    command: 'tsc --noEmit'
    options:
      mergeArgs: 'replace'
      runFromWorkspaceRoot: true
```

#### `affectedFiles` [​](https://moonrepo.dev/docs/config/project\#affectedfiles "Direct link to affectedfiles")

When enabled and the [`--affected` option](https://moonrepo.dev/docs/run-task#running-based-on-affected-files-only) is
provided, all affected files that match this task's [`inputs`](https://moonrepo.dev/docs/config/project#inputs) will be passed as relative
file paths as command line arguments, and as a `MOON_AFFECTED_FILES` environment variable.

If there are no affected files, `.` (current directory) will be passed instead for arguments, and an
empty value for the environment variable. This functionality can be changed with the
[`affectedPassInputs`](https://moonrepo.dev/docs/config/project#affectedpassinputs) setting.

moon.yml

```yaml
tasks:
  lint:
    command: 'eslint'
    options:
      affectedFiles: true
      # Only pass args
      affectedFiles: 'args'
      # Only set env var
      affectedFiles: 'env'
```

caution

When using this option, ensure that explicit files or `.` _are not present_ in the [`args`](https://moonrepo.dev/docs/config/project#args)
list. Furthermore, this functionality will only work if the task's command supports an arbitrary
list of files being passed as arguments.

This setting also supports an object format with additional parameters. The `pass` field is
required, which accepts a value described above.

moon.yml

```yaml
tasks:
  lint:
    command: 'eslint'
    options:
      affectedFiles:
        pass: 'args'
```

The following additional parameters are supported:

- `filter` (`boolean`) v2.1.0 \- A list of glob patterns to filter the
affected files list before passing to the task. Globs must start with `**` to match against
absolute paths.
- `ignoreProjectBoundary` (`boolean`) v2.1.0 \- When matching affected
files, ignore the project boundary and include workspace relative files. Otherwise, only files
within the project are matched. Defaults to `false`.
- `passDotWhenNoResults` (`boolean`) v2.1.0 \- When no affected files are
found, will pass `.` instead of an empty or no value. Defaults to `true`.
- `passInputsWhenNoMatch` (`boolean`) \- When no affected files are found, will pass all configured
[`inputs`](https://moonrepo.dev/docs/config/project#inputs) as relative file paths instead. Defaults to `false`.

#### `allowFailure`v1.13.0 [​](https://moonrepo.dev/docs/config/project\#allowfailure "Direct link to allowfailure")

Allows a task to fail without failing the entire pipeline. When enabled, the following changes
occur:

- Other tasks _cannot_ depend on this task, as we can't ensure it's side-effect free.
- For [`moon run`](https://moonrepo.dev/docs/commands/run), the process will not bail early and will run to completion.
- For [`moon ci`](https://moonrepo.dev/docs/commands/ci), the process will not exit with a non-zero exit code, if the only
failing tasks are allowed to fail.

moon.yml

```yaml
tasks:
  lint:
    command: 'eslint'
    options:
      allowFailure: true
```

#### `cache` [​](https://moonrepo.dev/docs/config/project\#cache "Direct link to cache")

Whether to cache the task's execution result using our [smart hashing](https://moonrepo.dev/docs/concepts/cache#hashing)
system. If disabled, _will not_ create a cache hash, and _will not_ persist a task's
[outputs](https://moonrepo.dev/docs/config/project#outputs). Supports the following values:

- `true` (default) - Cache the task's output.
- `false` \- Do not cache the task's output.
- `local` \- Only cache locally. v1.40.0
- `remote` \- Only cache [remotely](https://moonrepo.dev/docs/guides/remote-cache). v1.40.0

We suggest disabling caching when defining cleanup tasks, one-off scripts, or file system heavy
operations.

moon.yml

```yaml
tasks:
  clean:
    command: 'rm -rf ./temp'
    options:
      cache: false
```

#### `cacheKey`v1.35.0 [​](https://moonrepo.dev/docs/config/project\#cachekey "Direct link to cachekey")

A custom key to include in the cache and task hashing process. Can be used to invalidate local and
remote caches.

moon.yml

```yaml
tasks:
  build:
    command: 'some-costly-build'
    options:
      cacheKey: 'v1'
```

#### `cacheLifetime`v1.29.0 [​](https://moonrepo.dev/docs/config/project\#cachelifetime "Direct link to cachelifetime")

The lifetime in which a [cached task](https://moonrepo.dev/docs/config/project#cache) will live before being marked as stale and re-running.
This applies to a task even if it does not produce [outputs](https://moonrepo.dev/docs/config/project#outputs).

The lifetime can be configured in a human-readable string format, for example, `1 day`, `3 hr`,
`1m`, etc. If the lifetime is not defined, the cache will live forever, or until the task inputs are
touched.

moon.yml

```yaml
tasks:
  build:
    command: 'some-costly-build'
    options:
      cacheLifetime: '1 day'
```

> String formats are powered by the
> [humantime](https://docs.rs/humantime/2.1.0/humantime/fn.parse_duration.html) crate.

#### `envFile` [​](https://moonrepo.dev/docs/config/project\#envfile "Direct link to envfile")

A boolean or path to a `.env` file (also know as dotenv file) that defines a collection of
[environment variables](https://moonrepo.dev/docs/config/project#env-1) for the current task. Variables will be loaded on project creation,
but will _not_ override those defined in [`env`](https://moonrepo.dev/docs/config/project#env-1).

Variables defined in the file support value substitution/expansion by wrapping the variable name in
curly brackets, such as `${VAR_NAME}`.

moon.yml

```yaml
tasks:
  build:
    command: 'webpack'
    options:
      # Defaults to .env
      envFile: true
      # Or
      envFile: '.env.production'
      # Or from the workspace root
      envFile: '/.env.shared'
```

When set to `true`, moon will load the following files in order, with later files taking precedence
over earlier ones:

- `/.env`
- `/.env.local`
- `.env`
- `.env.local`
- `.env.<task_id>`
- `.env.<task_id>.local`

Additionally, a list of file paths can also be provided. When using a list, the order of the files
is important, as environment variables from all files will be aggregated into a single map, with
subsequent files taking precedence over previous ones. Once aggregated, the variables will be passed
to the task, but will _not_ override those defined in [`env`](https://moonrepo.dev/docs/config/project#env-1).

moon.yml

```yaml
tasks:
  build:
    command: 'webpack'
    options:
      envFile:
        - '.env'
        - '.env.production'
```

#### `inferInputs`v1.31.0 [​](https://moonrepo.dev/docs/config/project\#inferinputs "Direct link to inferinputs")

Automatically infer [inputs](https://moonrepo.dev/docs/config/project#inputs) based on the following parameters configured within the task's
`command`, `script`, `args`, or `env`. Defaults to `false`.

- File/glob paths derived from [file group based token functions](https://moonrepo.dev/docs/concepts/token#file-groups).
- Environment variables being substituted within a command or script.

moon.yml

```yaml
tasks:
  build:
    # ...
    options:
      inferInputs: false
```

#### `internal`v1.23.0 [​](https://moonrepo.dev/docs/config/project\#internal "Direct link to internal")

Marks the task as internal only. [Internal tasks](https://moonrepo.dev/docs/concepts/task#internal-only) can not be
explicitly ran on the command line, but can be depended on by other tasks.

moon.yml

```yaml
tasks:
  prepare:
    # ...
    options:
      internal: true
```

#### `interactive`v1.12.0 [​](https://moonrepo.dev/docs/config/project\#interactive "Direct link to interactive")

Marks the task as interactive. [Interactive tasks](https://moonrepo.dev/docs/concepts/task#interactive) run in isolation so
that they can interact with stdin.

This setting also disables caching, turns of CI, and other functionality, similar to the
[`preset`](https://moonrepo.dev/docs/config/project#preset) setting.

moon.yml

```yaml
tasks:
  init:
    # ...
    options:
      interactive: true
```

#### `merge`v1.29.0 [​](https://moonrepo.dev/docs/config/project\#merge "Direct link to merge")

The [strategy](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) to use when merging [`args`](https://moonrepo.dev/docs/config/project#args),
[`deps`](https://moonrepo.dev/docs/config/project#deps), [`env`](https://moonrepo.dev/docs/config/project#env-1), [`inputs`](https://moonrepo.dev/docs/config/project#inputs), and [`outputs`](https://moonrepo.dev/docs/config/project#outputs) with an inherited
task. This option can be overridden with the field specific merge options below.

#### `mergeArgs` [​](https://moonrepo.dev/docs/config/project\#mergeargs "Direct link to mergeargs")

The [strategy](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) to use when merging the
[`args`](https://moonrepo.dev/docs/config/project#args) list with an inherited task. Defaults to "append".

#### `mergeDeps` [​](https://moonrepo.dev/docs/config/project\#mergedeps "Direct link to mergedeps")

The [strategy](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) to use when merging the
[`deps`](https://moonrepo.dev/docs/config/project#deps) list with an inherited task. Defaults to "append".

#### `mergeEnv` [​](https://moonrepo.dev/docs/config/project\#mergeenv "Direct link to mergeenv")

The [strategy](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) to use when merging the
[`env`](https://moonrepo.dev/docs/config/project#env-1) map with an inherited task. Defaults to "append".

#### `mergeInputs` [​](https://moonrepo.dev/docs/config/project\#mergeinputs "Direct link to mergeinputs")

The [strategy](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) to use when merging the
[`inputs`](https://moonrepo.dev/docs/config/project#inputs) list with an inherited task. Defaults to "append".

#### `mergeOutputs` [​](https://moonrepo.dev/docs/config/project\#mergeoutputs "Direct link to mergeoutputs")

The [strategy](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) to use when merging the
[`outputs`](https://moonrepo.dev/docs/config/project#outputs) list with an inherited task. Defaults to "append".

#### `mergeToolchains` [​](https://moonrepo.dev/docs/config/project\#mergetoolchains "Direct link to mergetoolchains")

The [strategy](https://moonrepo.dev/docs/concepts/task-inheritance#merge-strategies) to use when merging the
[`toolchains`](https://moonrepo.dev/docs/config/project#toolchains) list with an inherited task. Defaults to "append".

#### `mutex`v1.24.0 [​](https://moonrepo.dev/docs/config/project\#mutex "Direct link to mutex")

Creates an exclusive lock on a "virtual resource", preventing other tasks using the same "virtual
resource" from running concurrently.

If you have many tasks that require exclusive access to a resource that can't be tracked by moon
(like a database, an ignored file, a file that's not part of the project, or a remote resource) you
can use the `mutex` option to prevent them from running at the same time.

moon.yml

```yaml
tasks:
  a:
    # ...
    options:
      mutex: 'virtual_resource_name'

  # b doesn't necessarily have to be in the same project
  b:
    # ...
    options:
      mutex: 'virtual_resource_name'
```

#### `os`v1.28.0 [​](https://moonrepo.dev/docs/config/project\#os "Direct link to os")

When defined, the task will _only_ run on the configured operating system. For other operating
systems, the task becomes a no-operation. Supports the values `linux`, `macos`, and `windows`.

Can be defined as a single value, or a list of values.

moon.yml

```yaml
tasks:
  build-unix:
    # ...
    options:
      os: ['linux', 'macos']

  build-windows:
    # ...
    options:
      os: 'windows'
```

#### `outputStyle` [​](https://moonrepo.dev/docs/config/project\#outputstyle "Direct link to outputstyle")

Controls how stdout/stderr is displayed when the task is ran as a _transitive target_. By default,
this setting is not defined and defers to the action pipeline, but can be overridden with one of the
following values:

- `buffer` \- Buffers output and displays after the task has exited (either success or failure).
- `buffer-only-failure` \- Like `buffer`, but only displays on failures.
- `hash` \- Ignores output and only displays the generated [hash](https://moonrepo.dev/docs/concepts/cache#hashing).
- `none` \- Ignores output.
- `stream` \- Streams output directly to the terminal. Will prefix each line of output with the
target.

moon.yml

```yaml
tasks:
  test:
    # ...
    options:
      outputStyle: 'stream'
```

#### `persistent`v1.6.0 [​](https://moonrepo.dev/docs/config/project\#persistent "Direct link to persistent")

Marks the task as persistent (continuously running). [Persistent tasks](https://moonrepo.dev/docs/concepts/task#persistent)
are handled differently than non-persistent tasks in the action graph. When running a target, all
persistent tasks are _ran last_ and _in parallel_, after all their dependencies have completed.

This is extremely useful for running a server (or a watcher) in the background while other tasks are
running.

moon.yml

```yaml
tasks:
  dev:
    # ...
    options:
      persistent: true
```

> We suggest using the [`preset`](https://moonrepo.dev/docs/config/project#preset) setting instead, which enables this setting, amongst
> other useful settings.

#### `priority`v1.35.0 [​](https://moonrepo.dev/docs/config/project\#priority "Direct link to priority")

The priority level determines the position of the task within the action pipeline queue. A task with
a higher priority will run sooner rather than later, while still respecting the topological order.
Supports the following levels:

- `critical`
- `high`
- `normal` (default)
- `low`

moon.yml

```yaml
tasks:
  build:
    # ...
    options:
      priority: 'high'
```

#### `retryCount` [​](https://moonrepo.dev/docs/config/project\#retrycount "Direct link to retrycount")

The number of attempts the task will retry execution before returning a failure. This is especially
useful for flaky tasks. Defaults to `0`.

moon.yml

```yaml
tasks:
  test:
    # ...
    options:
      retryCount: 3
```

#### `runDepsInParallel` [​](https://moonrepo.dev/docs/config/project\#rundepsinparallel "Direct link to rundepsinparallel")

Whether to run the task's direct [`deps`](https://moonrepo.dev/docs/config/project#deps) in parallel or serial (in order). Defaults to
`true`.

When disabled, this _does not_ run dependencies of dependencies in serial, only direct dependencies.

moon.yml

```yaml
tasks:
  start:
    # ...
    deps:
      - '~:clean'
      - '~:build'
    options:
      runDepsInParallel: false
```

#### `runInCI` [​](https://moonrepo.dev/docs/config/project\#runinci "Direct link to runinci")

Whether to run the task automatically in a CI (continuous integration) environment when affected by
changed files using the [`moon ci`](https://moonrepo.dev/docs/commands/ci) command. Supports the following values:

- `always` \- Always run in CI, regardless if affected or not. v1.31.0
- `affected`, `true` (default) - Only run in CI if affected by changed files.
- `false` \- Never run in CI.
- `only` \- Only run in CI, and not locally, if affected by changed files.v1.41.0
- `skip` \- Skip running in CI but run locally and allow task relationships to be valid.v1.41.0

moon.yml

```yaml
tasks:
  build:
    # ...
    options:
      runInCI: false
```

#### `runInSyncPhase`v2.1.0 [​](https://moonrepo.dev/docs/config/project\#runinsyncphase "Direct link to runinsyncphase")

Whether to run the task automatically during `moon sync`. Defaults to `false`.

moon.yml

```yaml
tasks:
  generate-schema:
    # ...
    options:
      runInSyncPhase: true
```

#### `runFromWorkspaceRoot` [​](https://moonrepo.dev/docs/config/project\#runfromworkspaceroot "Direct link to runfromworkspaceroot")

Whether to use the workspace root as the working directory when executing a task. Defaults to
`false` and runs from the task's project root.

moon.yml

```yaml
tasks:
  typecheck:
    # ...
    options:
      runFromWorkspaceRoot: true
```

#### `shell` [​](https://moonrepo.dev/docs/config/project\#shell "Direct link to shell")

Whether to run the command within a shell or not. Defaults to `true` for system toolchain or
Windows, and `false` otherwise. The shell to run is determined by the [`unixShell`](https://moonrepo.dev/docs/config/project#unixshell) and
[`windowsShell`](https://moonrepo.dev/docs/config/project#windowsshell) options respectively.

moon.yml

```yaml
tasks:
  native:
    command: 'echo $SHELL'
    options:
      shell: true
```

However, if you'd like to use a different shell, or customize the shell's arguments, or have
granular control, you can set `shell` to false and configure a fully qualified command.

moon.yml

```yaml
tasks:
  native:
    command: '/bin/zsh -c "echo $SHELL"'
    options:
      shell: false
```

#### `timeout`v1.26.0 [​](https://moonrepo.dev/docs/config/project\#timeout "Direct link to timeout")

The maximum time in seconds that the task is allowed to run, before it is force cancelled. If not
defined, will run indefinitely.

moon.yml

```yaml
tasks:
  build:
    # ...
    options:
      timeout: 120
```

#### `unixShell`v1.21.0 [​](https://moonrepo.dev/docs/config/project\#unixshell "Direct link to unixshell")

Customize the shell to run with when on a Unix operating system. Accepts `bash`, `elvish`, `fish`,
`ion`, `murex`, `nu`, `pwsh`, `xonsh`, or `zsh`. If not defined, will derive the shell from the
`SHELL` environment variable, or defaults to `bash`.

moon.yml

```yaml
tasks:
  native:
    command: 'echo $SHELL'
    options:
      unixShell: 'fish'
```

#### `windowsShell`v1.21.0 [​](https://moonrepo.dev/docs/config/project\#windowsshell "Direct link to windowsshell")

Customize the shell to run with when on a Windows operating system. Accepts `bash` (typically via
Git), `elvish`, `fish`, `murex`, `nu`, `pwsh`, or `xonsh`. If not defined, defaults to `pwsh`.

moon.yml

```yaml
tasks:
  native:
    command: 'echo $SHELL'
    options:
      windowsShell: 'bash'
```

## Overrides [​](https://moonrepo.dev/docs/config/project\#overrides "Direct link to Overrides")

Dictates how a project interacts with settings defined at the top-level.

## `toolchains` [​](https://moonrepo.dev/docs/config/project\#toolchains-1 "Direct link to toolchains-1")

### `default`v1.31.0 [​](https://moonrepo.dev/docs/config/project\#default "Direct link to default")

The default [`toolchain`](https://moonrepo.dev/docs/config/project#toolchain-1) for all task's within the current project. When a task's
`toolchain` has _not been_ explicitly configured, the toolchain will fallback to this configured
value, otherwise the toolchain will be detected from the project's environment.

moon.yml

```yaml
toolchains:
  default: 'node'
```

### `*`v2.0.0

Configures and overrides [workspace-level settings](https://moonrepo.dev/docs/config/toolchain) for specific toolchains. The key is
the name of the toolchain, and the value is an object of settings to override.

moon.yml

```yaml
toolchains:
  typescript:
    # Disable refs for this project
    syncProjectReferences: false
```

Alternatively, if you want to _disable_ a toolchain for a project, you can set the value to `false`
or `null`, which will prevent the toolchain from being auto-detected and used within the project.

moon.yml

```yaml
toolchains:
  typescript: false
```

## `workspace` [​](https://moonrepo.dev/docs/config/project\#workspace "Direct link to workspace")

### `inheritedTasks` [​](https://moonrepo.dev/docs/config/project\#inheritedtasks "Direct link to inheritedtasks")

Provides a layer of control when inheriting tasks from [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks).

#### `exclude` [​](https://moonrepo.dev/docs/config/project\#exclude "Direct link to exclude")

The optional `exclude` setting permits a project to exclude specific tasks from being inherited. It
accepts a list of strings, where each string is the name of a global task to exclude.

moon.yml

```yaml
workspace:
  inheritedTasks:
    # Exclude the inherited `test` task for this project
    exclude: ['test']
```

> Exclusion is applied after inclusion and before renaming.

#### `include` [​](https://moonrepo.dev/docs/config/project\#include "Direct link to include")

The optional `include` setting permits a project to _only_ include specific inherited tasks (works
like an allow/white list). It accepts a list of strings, where each string is the name of a global
task to include.

When this field is not defined, the project will inherit all tasks from the global project config.

moon.yml

```yaml
workspace:
  inheritedTasks:
    # Include *no* tasks (works like a full exclude)
    include: []

    # Only include the `lint` and `test` tasks for this project
    include:
      - 'lint'
      - 'test'
```

> Inclusion is applied before exclusion and renaming.

#### `rename` [​](https://moonrepo.dev/docs/config/project\#rename "Direct link to rename")

The optional `rename` setting permits a project to rename the inherited task within the current
project. It accepts a map of strings, where the key is the original name (found in the global
project config), and the value is the new name to use.

For example, say we have 2 tasks in the global project config called `buildPackage` and
`buildApplication`, but we only need 1, and since we're an application, we should omit and rename.

moon.yml

```yaml
workspace:
  inheritedTasks:
    exclude: ['buildPackage']
    rename:
      buildApplication: 'build'
```

> Renaming occurs after inclusion and exclusion.

- [`dependsOn`](https://moonrepo.dev/docs/config/project#dependson)
- [Metadata](https://moonrepo.dev/docs/config/project#metadata)
- [`id`](https://moonrepo.dev/docs/config/project#id)
- [`language`](https://moonrepo.dev/docs/config/project#language)
- [`owners`](https://moonrepo.dev/docs/config/project#owners)
  - [`customGroups`](https://moonrepo.dev/docs/config/project#customgroups)
  - [`defaultOwner`](https://moonrepo.dev/docs/config/project#defaultowner)
  - [`optional`](https://moonrepo.dev/docs/config/project#optional)
  - [`paths`](https://moonrepo.dev/docs/config/project#paths)
  - [`requiredApprovals`](https://moonrepo.dev/docs/config/project#requiredapprovals)
- [`layer`](https://moonrepo.dev/docs/config/project#layer)
- [`project`](https://moonrepo.dev/docs/config/project#project)
  - [`channel`](https://moonrepo.dev/docs/config/project#channel)
  - [`description`](https://moonrepo.dev/docs/config/project#description)
  - [`maintainers`](https://moonrepo.dev/docs/config/project#maintainers)
  - [`title`](https://moonrepo.dev/docs/config/project#title)
  - [`owner`](https://moonrepo.dev/docs/config/project#owner)
  - [Custom fields](https://moonrepo.dev/docs/config/project#custom-fields)
- [`stack`](https://moonrepo.dev/docs/config/project#stack)
- [`tags`](https://moonrepo.dev/docs/config/project#tags)
- [Integrations](https://moonrepo.dev/docs/config/project#integrations)
- [`docker`](https://moonrepo.dev/docs/config/project#docker)
  - [`file`](https://moonrepo.dev/docs/config/project#file)
    - [`buildTask`](https://moonrepo.dev/docs/config/project#buildtask)
    - [`image`](https://moonrepo.dev/docs/config/project#image)
    - [`runPrune`](https://moonrepo.dev/docs/config/project#runprune)
    - [`runSetup`](https://moonrepo.dev/docs/config/project#runsetup)
    - [`startTask`](https://moonrepo.dev/docs/config/project#starttask)
    - [`template`](https://moonrepo.dev/docs/config/project#template)
  - [`scaffold`](https://moonrepo.dev/docs/config/project#scaffold)
    - [`configsPhaseGlobs`](https://moonrepo.dev/docs/config/project#configsphaseglobs)
    - [`sourcesPhaseGlobs`](https://moonrepo.dev/docs/config/project#sourcesphaseglobs)
- [Tasks](https://moonrepo.dev/docs/config/project#tasks)
- [`env`](https://moonrepo.dev/docs/config/project#env)
- [`fileGroups`](https://moonrepo.dev/docs/config/project#filegroups)
- [`tasks`](https://moonrepo.dev/docs/config/project#tasks-1)
  - [`extends`](https://moonrepo.dev/docs/config/project#extends)
  - [`description`](https://moonrepo.dev/docs/config/project#description-1)
  - [`command`](https://moonrepo.dev/docs/config/project#command)
  - [`args`](https://moonrepo.dev/docs/config/project#args)
  - [`deps`](https://moonrepo.dev/docs/config/project#deps)
    - [Args & env](https://moonrepo.dev/docs/config/project#args--env)
    - [Optional](https://moonrepo.dev/docs/config/project#optional-1)
  - [`env`](https://moonrepo.dev/docs/config/project#env-1)
  - [`inputs`](https://moonrepo.dev/docs/config/project#inputs)
    - [Environment variables](https://moonrepo.dev/docs/config/project#environment-variables)
    - [File paths](https://moonrepo.dev/docs/config/project#file-paths)
    - [File groups](https://moonrepo.dev/docs/config/project#file-groups)
    - [Glob patterns](https://moonrepo.dev/docs/config/project#glob-patterns)
    - [External projects](https://moonrepo.dev/docs/config/project#external-projects)
  - [`outputs`](https://moonrepo.dev/docs/config/project#outputs)
    - [File paths](https://moonrepo.dev/docs/config/project#file-paths-1)
    - [Glob patterns](https://moonrepo.dev/docs/config/project#glob-patterns-1)
  - [`preset`](https://moonrepo.dev/docs/config/project#preset)
  - [`script`](https://moonrepo.dev/docs/config/project#script)
  - [`toolchains`](https://moonrepo.dev/docs/config/project#toolchains)
  - [`options`](https://moonrepo.dev/docs/config/project#options)
    - [`affectedFiles`](https://moonrepo.dev/docs/config/project#affectedfiles)
    - [`allowFailure`](https://moonrepo.dev/docs/config/project#allowfailure)
    - [`cache`](https://moonrepo.dev/docs/config/project#cache)
    - [`cacheKey`](https://moonrepo.dev/docs/config/project#cachekey)
    - [`cacheLifetime`](https://moonrepo.dev/docs/config/project#cachelifetime)
    - [`envFile`](https://moonrepo.dev/docs/config/project#envfile)
    - [`inferInputs`](https://moonrepo.dev/docs/config/project#inferinputs)
    - [`internal`](https://moonrepo.dev/docs/config/project#internal)
    - [`interactive`](https://moonrepo.dev/docs/config/project#interactive)
    - [`merge`](https://moonrepo.dev/docs/config/project#merge)
    - [`mergeArgs`](https://moonrepo.dev/docs/config/project#mergeargs)
    - [`mergeDeps`](https://moonrepo.dev/docs/config/project#mergedeps)
    - [`mergeEnv`](https://moonrepo.dev/docs/config/project#mergeenv)
    - [`mergeInputs`](https://moonrepo.dev/docs/config/project#mergeinputs)
    - [`mergeOutputs`](https://moonrepo.dev/docs/config/project#mergeoutputs)
    - [`mergeToolchains`](https://moonrepo.dev/docs/config/project#mergetoolchains)
    - [`mutex`](https://moonrepo.dev/docs/config/project#mutex)
    - [`os`](https://moonrepo.dev/docs/config/project#os)
    - [`outputStyle`](https://moonrepo.dev/docs/config/project#outputstyle)
    - [`persistent`](https://moonrepo.dev/docs/config/project#persistent)
    - [`priority`](https://moonrepo.dev/docs/config/project#priority)
    - [`retryCount`](https://moonrepo.dev/docs/config/project#retrycount)
    - [`runDepsInParallel`](https://moonrepo.dev/docs/config/project#rundepsinparallel)
    - [`runInCI`](https://moonrepo.dev/docs/config/project#runinci)
    - [`runInSyncPhase`](https://moonrepo.dev/docs/config/project#runinsyncphase)
    - [`runFromWorkspaceRoot`](https://moonrepo.dev/docs/config/project#runfromworkspaceroot)
    - [`shell`](https://moonrepo.dev/docs/config/project#shell)
    - [`timeout`](https://moonrepo.dev/docs/config/project#timeout)
    - [`unixShell`](https://moonrepo.dev/docs/config/project#unixshell)
    - [`windowsShell`](https://moonrepo.dev/docs/config/project#windowsshell)
- [Overrides](https://moonrepo.dev/docs/config/project#overrides)
- [`toolchains`](https://moonrepo.dev/docs/config/project#toolchains-1)
  - [`default`](https://moonrepo.dev/docs/config/project#default)
  - [`*`](https://moonrepo.dev/docs/config/project#)
- [`workspace`](https://moonrepo.dev/docs/config/project#workspace)
  - [`inheritedTasks`](https://moonrepo.dev/docs/config/project#inheritedtasks)
    - [`exclude`](https://moonrepo.dev/docs/config/project#exclude)
    - [`include`](https://moonrepo.dev/docs/config/project#include)
    - [`rename`](https://moonrepo.dev/docs/config/project#rename)