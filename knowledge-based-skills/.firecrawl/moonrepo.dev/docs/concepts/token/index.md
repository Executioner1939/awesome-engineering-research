[Skip to main content](https://moonrepo.dev/docs/concepts/token#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Tokens are variables and functions that can be used by [`command`](https://moonrepo.dev/docs/config/project#command),
[`args`](https://moonrepo.dev/docs/config/project#args), [`env`](https://moonrepo.dev/docs/config/project#env) (>= v1.12),
[`inputs`](https://moonrepo.dev/docs/config/project#inputs), and [`outputs`](https://moonrepo.dev/docs/config/project#outputs) when configuring a
task. They provide a way of accessing file group paths, referencing values from other task fields,
and referencing metadata about the project and task itself.

## Functions [​](https://moonrepo.dev/docs/concepts/token\#functions "Direct link to Functions")

A token function is labeled as such as it takes a single argument, starts with an `@`, and is
formatted as `@name(arg)`. The following token functions are available, grouped by their
functionality.

caution

Token functions _must_ be the only content within a value, as they expand to multiple files. When
used in an `env` value, multiple files are joined with a comma (`,`).

### File groups [​](https://moonrepo.dev/docs/concepts/token\#file-groups "Direct link to File groups")

These functions reference file groups by name, where the name is passed as the argument.

### `@group` [​](https://moonrepo.dev/docs/concepts/token\#group "Direct link to group")

> Usable in `args`, `env`, `inputs`, and `outputs`.

The `@group(file_group)` token is a standard token that will be replaced with the file group items
as-is, for both file paths and globs. This token merely exists for reusability purposes.

```yaml
fileGroups:
  storybook:
    - '.storybook/**/*'
    - 'src/**/*'
    - '**/*.stories.*'

# Configured as
tasks:
  build:
    command: 'build-storybook'
    inputs:
      - '@group(storybook)'
  start:
    command: 'start-storybook'
    inputs:
      - '@group(storybook)'

# Resolves to
tasks:
  build:
    command: 'build-storybook'
    inputs:
      - '/path/to/project/.storybook/**/*'
      - '/path/to/project/src/**/*'
      - '/path/to/project/**/*.stories.*'
  start:
    command: 'start-storybook'
    inputs:
      - '/path/to/project/.storybook/**/*'
      - '/path/to/project/src/**/*'
      - '/path/to/project/**/*.stories.*'
```

### `@dirs` [​](https://moonrepo.dev/docs/concepts/token\#dirs "Direct link to dirs")

> Usable in `args`, `env`, `inputs`, and `outputs`.

The `@dirs(file_group)` token will be replaced with an expanded list of directory paths, derived
from the file group of the same name. If a glob pattern is detected within the file group, it will
aggregate all directories found.

warning

This token walks the file system to verify each directory exists, and filters out those that don't.
If using within `outputs`, you're better off using [`@group`](https://moonrepo.dev/docs/concepts/token#group) instead.

```yaml
fileGroups:
  lintable:
    - 'src'
    - 'tests'
    - 'scripts'
    - '*.config.js'

# Configured as
tasks:
  lint:
    command: 'eslint @dirs(lintable) --color'
    inputs:
      - '@dirs(lintable)'

# Resolves to
tasks:
  lint:
    command:
      - 'eslint'
      - 'src'
      - 'tests'
      - 'scripts'
      - '--color'
    inputs:
      - '/path/to/project/src'
      - '/path/to/project/tests'
      - '/path/to/project/scripts'
```

### `@files` [​](https://moonrepo.dev/docs/concepts/token\#files "Direct link to files")

> Usable in `args`, `env`, `inputs`, and `outputs`.

The `@files(file_group)` token will be replaced with an expanded list of file paths, derived from
the file group of the same name. If a glob pattern is detected within the file group, it will
aggregate all files found.

warning

This token walks the file system to verify each file exists, and filters out those that don't. If
using within `outputs`, you're better off using [`@group`](https://moonrepo.dev/docs/concepts/token#group) instead.

```yaml
fileGroups:
  config:
    - '*.config.js'
    - 'package.json'

# Configured as
tasks:
  build:
    command: 'webpack build @files(config)'
    inputs:
      - '@files(config)'

# Resolves to
tasks:
  build:
    command:
      - 'webpack'
      - 'build'
      - 'babel.config.js'
      - 'webpack.config.js'
      - 'package.json'
    inputs:
      - '/path/to/project/babel.config.js'
      - '/path/to/project/webpack.config.js'
      - '/path/to/project/package.json'
```

### `@globs` [​](https://moonrepo.dev/docs/concepts/token\#globs "Direct link to globs")

> Usable in `args`, `env`, `inputs`, and `outputs`.

The `@globs(file_group)` token will be replaced with the list of glob patterns as-is, derived from
the file group of the same name. If a non-glob pattern is detected within the file group, it will be
ignored.

```yaml
fileGroups:
  tests:
    - 'tests/**/*'
    - '**/__tests__/**/*'

# Configured as
tasks:
  test:
    command: 'jest --testMatch @globs(tests)'
    inputs:
      - '@globs(tests)'

# Resolves to
tasks:
  test:
    command:
      - 'jest'
      - '--testMatch'
      - 'tests/**/*'
      - '**/__tests__/**/*'
    inputs:
      - '/path/to/project/tests/**/*'
      - '/path/to/project/**/__tests__/**/*'
```

### `@root` [​](https://moonrepo.dev/docs/concepts/token\#root "Direct link to root")

> Usable in `args`, `env`, `inputs`, and `outputs`.

The `@root(file_group)` token will be replaced with the lowest common directory, derived from the
file group of the same name. If a glob pattern is detected within the file group, it will walk the
file system and aggregate all directories found before reducing.

```yaml
fileGroups:
  sources:
    - 'src/app'
    - 'src/packages'
    - 'src/scripts'

# Configured as
tasks:
  format:
    command: 'prettier --write @root(sources)'
    inputs:
      - '@root(sources)'

# Resolves to
tasks:
  format:
    command:
      - 'prettier'
      - '--write'
      - 'src'
    inputs:
      - '/path/to/project/src'
```

> When there's no directies, or too many directories, this function will return the project root
> using `.`.

### `@envs`v1.21.0 [​](https://moonrepo.dev/docs/concepts/token\#envs "Direct link to envs")

> Usable in `inputs`.

The `@envs(file_group)` token will be replaced with all environment variables that have been
configured in the group of the provided name.

```yaml
fileGroups:
  sources:
    - 'src/**/*'
    - '$NODE_ENV'

# Configured as
tasks:
  build:
    command: 'vite build'
    inputs:
      - '@envs(sources)'

# Resolves to
tasks:
  build:
    command: 'vite build'
    inputs:
      - '$NODE_ENV'
```

### Inputs & outputs [​](https://moonrepo.dev/docs/concepts/token\#inputs--outputs "Direct link to Inputs & outputs")

### `@in` [​](https://moonrepo.dev/docs/concepts/token\#in "Direct link to in")

> Usable in `script` and `args` only.

The `@in(index)` token will be replaced with a single path, derived from
[`inputs`](https://moonrepo.dev/docs/config/project#inputs) by numerical index. If a glob pattern is referenced by index,
the glob will be used as-is, instead of returning the expanded list of files.

```yaml
# Configured as
tasks:
  build:
    command:
      - 'babel'
      - '--copy-files'
      - '--config-file'
      - '@in(1)'
      - '@in(0)'
    inputs:
      - 'src'
      - 'babel.config.js'

# Resolves to
tasks:
  build:
    command:
      - 'babel'
      - '--copy-files'
      - '--config-file'
      - 'babel.config.js'
      - 'src'
    inputs:
      - '/path/to/project/src'
      - '/path/to/project/babel.config.js'
```

### `@out` [​](https://moonrepo.dev/docs/concepts/token\#out "Direct link to out")

> Usable in `script` and `args` only.

The `@out(index)` token will be replaced with a single path, derived from
[`outputs`](https://moonrepo.dev/docs/config/project#outputs) by numerical index.

```yaml
# Configured as
tasks:
  build:
    command:
      - 'babel'
      - '.'
      - '--out-dir'
      - '@out(0)'
    outputs:
      - 'lib'

# Resolves to
tasks:
  build:
    command:
      - 'babel'
      - '.'
      - '--out-dir'
      - 'lib'
    outputs:
      - '/path/to/project/lib'
```

### Miscellaneous [​](https://moonrepo.dev/docs/concepts/token\#miscellaneous "Direct link to Miscellaneous")

### `@meta`v1.28.0 [​](https://moonrepo.dev/docs/concepts/token\#meta "Direct link to meta")

> Usable in `command`, `script`, `args`, `env`, `inputs`, and `outputs` only.

The `@meta(key)` token can be used to access project metadata and will be replaced with a value
derived from [`project`](https://moonrepo.dev/docs/config/project#project) in [`moon.*`](https://moonrepo.dev/docs/config/project).

The top-level fields (like `name` and `description`) will be used as-is (no quotes). If the setting
is not defined, it will default to nothing or an empty string. For lists of values, they will be
joined with `,`.

Custom metadata defined in [`project`](https://moonrepo.dev/docs/config/project#project) can also be accessed by key, but
will return a JSON stringified value. For example, a custom string value of `example` will be
stringified to `"example"` (with quotes).

```yaml
project:
  title: 'example'
  index: 123

# Configured as
tasks:
  build:
    script: 'build --name @meta(title) --index @meta(index)'

# Resolves to
tasks:
  build:
    script: 'build --name example --index 123'
```

## Variables [​](https://moonrepo.dev/docs/concepts/token\#variables "Direct link to Variables")

A token variable is a value that starts with `$` and is substituted to a value derived from the
current workspace, project, and task. And unlike token functions, token variables can be placed
_within_ content when necessary, and supports multiple variables within the same content.

### Environmentv1.30.0 [​](https://moonrepo.dev/docs/concepts/token\#environment "Direct link to environment")

- `$arch` \- The current host architecture, derived from the Rust
[`ARCH` constant](https://doc.rust-lang.org/std/env/consts/constant.ARCH.html).
- `$os` \- The current operating system, derived from the Rust
[`OS` constant](https://doc.rust-lang.org/std/env/consts/constant.OS.html).
- `$osFamily` \- The current operating system family, either `unix` or `windows`.

```yaml
# Configured as
tasks:
  build:
    command: 'example --arch $arch'

# Resolves to
tasks:
  build:
    command:
      - 'example'
      - '--arch'
      - 'aarch64'
```

### Workspace [​](https://moonrepo.dev/docs/concepts/token\#workspace "Direct link to Workspace")

- `$workingDir` \- The current working directory.
- `$workspaceRoot` \- Absolute file path to the workspace root.

```yaml
# Configured as
tasks:
  build:
    command:
      - 'example'
      - '--cwd'
      - '$workspaceRoot'

# Resolves to
tasks:
  build:
    command:
      - 'example'
      - '--cwd'
      - '/path/to/repo'
```

### Project [​](https://moonrepo.dev/docs/concepts/token\#project "Direct link to Project")

Most values are derived from settings in [`moon.*`](https://moonrepo.dev/docs/config/project). When a setting is not
defined, or does not have a config, the variable defaults to "unknown" (for enums) or an empty
string.

- `$language` Programming language the project is written in, as defined with
[`language`](https://moonrepo.dev/docs/config/project#language).
- `$project` \- ID of the project that owns the currently running task, as defined in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace).
- `$projectAlias` \- Alias of the project that owns the currently running task.
- `$projectChannel` \- The discussion channel for the project, as defined with
[`project.channel`](https://moonrepo.dev/docs/config/project#channel).v1.28.0
- `$projectLayer` \- The project layer, as defined with [`layer`](https://moonrepo.dev/docs/config/project#layer).v1.39.0
- `$projectTitle` \- The human-readable name of the project, as defined with
[`project.title`](https://moonrepo.dev/docs/config/project#title).v1.28.0
- `$projectOwner` \- The owner of the project, as defined with
[`project.owner`](https://moonrepo.dev/docs/config/project#name).v1.28.0
- `$projectRoot` \- Absolute file path to the project root.
- `$projectSource` \- Relative file path from the workspace root to the project root, as defined in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace).
- `$projectStack` \- The stack of the project, as defined with [`stack`](https://moonrepo.dev/docs/config/project#stack).v1.22.0

```yaml
# Configured as
tasks:
  build:
    command: 'example debug $language'

# Resolves to
tasks:
  build:
    command:
      - 'example'
      - 'debug'
      - 'node'
```

### Task [​](https://moonrepo.dev/docs/concepts/token\#task "Direct link to Task")

- `$target` \- Fully-qualified target that is currently running.
- `$task` \- ID of the task that is currently running. Does not include the project ID.
- `$taskToolchain` \- The toolchain that task will run against, as defined in
[`moon.*`](https://moonrepo.dev/docs/config/project). v1.31.0
- `$taskType` \- The [type of task](https://moonrepo.dev/docs/concepts/task#types), based on its configured settings.

```yaml
# Configured as
tasks:
  build:
    command: 'example $target'

# Resolves to
tasks:
  build:
    command:
      - 'example'
      - 'web:build'
```

### Date/Time [​](https://moonrepo.dev/docs/concepts/token\#datetime "Direct link to Date/Time")

- `$date` \- The current date in the format of `YYYY-MM-DD`.
- `$datetime` \- The current date and time in the format of `YYYY-MM-DD_HH:MM:SS`.
- `$time` \- The current time in the format of `HH:MM:SS`.
- `$timestamp` \- The current date and time as a UNIX timestamp in seconds.

```yaml
# Configured as
tasks:
  build:
    command: 'example --date $date'

# Resolves to
tasks:
  build:
    command:
      - 'example'
      - '--date'
      - '2023-03-17'
```

### VCSv1.30.0 [​](https://moonrepo.dev/docs/concepts/token\#vcs "Direct link to vcs")

- `$vcsBranch` \- The current branch.
- `$vcsRepository` \- The repository slug, in the format of `owner/repo`.
- `$vcsRevision` \- The current revision (commit, etc).

```yaml
# Configured as
tasks:
  build:
    command: 'example --branch $vcsBranch'

# Resolves to
tasks:
  build:
    command:
      - 'example'
      - '--branch'
      - 'master'
```

- [Functions](https://moonrepo.dev/docs/concepts/token#functions)
  - [File groups](https://moonrepo.dev/docs/concepts/token#file-groups)
  - [`@group`](https://moonrepo.dev/docs/concepts/token#group)
  - [`@dirs`](https://moonrepo.dev/docs/concepts/token#dirs)
  - [`@files`](https://moonrepo.dev/docs/concepts/token#files)
  - [`@globs`](https://moonrepo.dev/docs/concepts/token#globs)
  - [`@root`](https://moonrepo.dev/docs/concepts/token#root)
  - [`@envs`](https://moonrepo.dev/docs/concepts/token#envs)
  - [Inputs & outputs](https://moonrepo.dev/docs/concepts/token#inputs--outputs)
  - [`@in`](https://moonrepo.dev/docs/concepts/token#in)
  - [`@out`](https://moonrepo.dev/docs/concepts/token#out)
  - [Miscellaneous](https://moonrepo.dev/docs/concepts/token#miscellaneous)
  - [`@meta`](https://moonrepo.dev/docs/concepts/token#meta)
- [Variables](https://moonrepo.dev/docs/concepts/token#variables)
  - [Environment](https://moonrepo.dev/docs/concepts/token#environment)
  - [Workspace](https://moonrepo.dev/docs/concepts/token#workspace)
  - [Project](https://moonrepo.dev/docs/concepts/token#project)
  - [Task](https://moonrepo.dev/docs/concepts/token#task)
  - [Date/Time](https://moonrepo.dev/docs/concepts/token#datetime)
  - [VCS](https://moonrepo.dev/docs/concepts/token#vcs)