[Skip to main content](https://moonrepo.dev/docs/cheat-sheet#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Don't have time to read the docs? Here's a quick cheat sheet to get you started.

## Tasks [​](https://moonrepo.dev/docs/cheat-sheet\#tasks "Direct link to Tasks")

Learn more about [tasks](https://moonrepo.dev/docs/concepts/task) and [targets](https://moonrepo.dev/docs/concepts/target).

#### Run all build and test tasks for all projects [​](https://moonrepo.dev/docs/cheat-sheet\#run-all-build-and-test-tasks-for-all-projects "Direct link to Run all build and test tasks for all projects")

```shell
moon check --all
```

#### Run all build and test tasks in a project [​](https://moonrepo.dev/docs/cheat-sheet\#run-all-build-and-test-tasks-in-a-project "Direct link to Run all build and test tasks in a project")

```shell
moon check project
```

#### Run a task in all projects [​](https://moonrepo.dev/docs/cheat-sheet\#run-a-task-in-all-projects "Direct link to Run a task in all projects")

```shell
moon run :task
```

#### Run a task in all projects with a tag [​](https://moonrepo.dev/docs/cheat-sheet\#run-a-task-in-all-projects-with-a-tag "Direct link to Run a task in all projects with a tag")

```shell
moon run '#tag:task'
# OR
moon run \#tag:task
# OR
moon run :task --query "tag=tag"
```

#### Run a task in a project [​](https://moonrepo.dev/docs/cheat-sheet\#run-a-task-in-a-project "Direct link to Run a task in a project")

```shell
moon run project:task
```

#### Run multiple tasks in all projects [​](https://moonrepo.dev/docs/cheat-sheet\#run-multiple-tasks-in-all-projects "Direct link to Run multiple tasks in all projects")

```shell
moon run :task1 :task2
```

#### Run multiple tasks in any project [​](https://moonrepo.dev/docs/cheat-sheet\#run-multiple-tasks-in-any-project "Direct link to Run multiple tasks in any project")

```shell
moon run projecta:task1 projectb:task2
```

#### Run a task in applications, libraries, or tools [​](https://moonrepo.dev/docs/cheat-sheet\#run-a-task-in-applications-libraries-or-tools "Direct link to Run a task in applications, libraries, or tools")

```shell
moon run :task --query "projectLayer=application"
```

#### Run a task in projects of a specific language [​](https://moonrepo.dev/docs/cheat-sheet\#run-a-task-in-projects-of-a-specific-language "Direct link to Run a task in projects of a specific language")

```shell
moon run :task --query "language=typescript"
```

#### Run a task in projects matching a keyword [​](https://moonrepo.dev/docs/cheat-sheet\#run-a-task-in-projects-matching-a-keyword "Direct link to Run a task in projects matching a keyword")

```shell
moon run :task --query "project~react-*"
```

#### Run a task in projects based on file path [​](https://moonrepo.dev/docs/cheat-sheet\#run-a-task-in-projects-based-on-file-path "Direct link to Run a task in projects based on file path")

```shell
moon run :task --query "projectSource~packages/*"
```

## Task configuration [​](https://moonrepo.dev/docs/cheat-sheet\#task-configuration "Direct link to Task configuration")

Learn more about [available options](https://moonrepo.dev/docs/config/project#tasks).

#### Disable caching [​](https://moonrepo.dev/docs/cheat-sheet\#disable-caching "Direct link to Disable caching")

moon.yml

```yaml
tasks:
  example:
    # ...
    options:
      cache: false
```

#### Re-run flaky tasks [​](https://moonrepo.dev/docs/cheat-sheet\#re-run-flaky-tasks "Direct link to Re-run flaky tasks")

moon.yml

```yaml
tasks:
  example:
    # ...
    options:
      retryCount: 3
```

#### Depend on tasks from parent project's dependencies [​](https://moonrepo.dev/docs/cheat-sheet\#depend-on-tasks-from-parent-projects-dependencies "Direct link to Depend on tasks from parent project's dependencies")

moon.yml

```yaml
# Also inferred from the language
dependsOn:
  - 'project-a'
  - 'project-b'

tasks:
  example:
    # ...
    deps:
      - '^:build'
```

#### Depend on tasks from arbitrary projects [​](https://moonrepo.dev/docs/cheat-sheet\#depend-on-tasks-from-arbitrary-projects "Direct link to Depend on tasks from arbitrary projects")

moon.yml

```yaml
tasks:
  example:
    # ...
    deps:
      - 'other-project:task'
```

#### Run dependencies serially [​](https://moonrepo.dev/docs/cheat-sheet\#run-dependencies-serially "Direct link to Run dependencies serially")

moon.yml

```yaml
tasks:
  example:
    # ...
    deps:
      - 'first'
      - 'second'
      - 'third'
    options:
      runDepsInParallel: false
```

#### Run multiple watchers/servers in parallel [​](https://moonrepo.dev/docs/cheat-sheet\#run-multiple-watchersservers-in-parallel "Direct link to Run multiple watchers/servers in parallel")

moon.yml

```yaml
tasks:
  example:
    command: 'noop'
    deps:
      - 'app:watch'
      - 'backend:start'
      - 'tailwind:watch'
    preset: 'server'
```

> The `persistent` setting is required for this to work.

## Languages [​](https://moonrepo.dev/docs/cheat-sheet\#languages "Direct link to Languages")

#### Run system binaries available on `PATH` [​](https://moonrepo.dev/docs/cheat-sheet\#run-system-binaries-available-on-path "Direct link to run-system-binaries-available-on-path")

moon.yml

```yaml
language: 'bash' # batch, etc

tasks:
  example:
    command: 'printenv'
```

moon.yml

```yaml
tasks:
  example:
    command: 'printenv'
    toolchain: 'system'
```

#### Run language binaries not supported in moon's toolchain [​](https://moonrepo.dev/docs/cheat-sheet\#run-language-binaries-not-supported-in-moons-toolchain "Direct link to Run language binaries not supported in moon's toolchain")

moon.yml

```yaml
language: 'ruby'

tasks:
  example:
    command: 'rubocop'
    toolchain: 'system'
```

#### Run npm binaries (Node.js) [​](https://moonrepo.dev/docs/cheat-sheet\#run-npm-binaries-nodejs "Direct link to Run npm binaries (Node.js)")

moon.yml

```yaml
language: 'javascript' # typescript

tasks:
  example:
    command: 'eslint'
```

moon.yml

```yaml
tasks:
  example:
    command: 'eslint'
    toolchain: 'node'
```

- [Tasks](https://moonrepo.dev/docs/cheat-sheet#tasks)
  - [Run all build and test tasks for all projects](https://moonrepo.dev/docs/cheat-sheet#run-all-build-and-test-tasks-for-all-projects)
  - [Run all build and test tasks in a project](https://moonrepo.dev/docs/cheat-sheet#run-all-build-and-test-tasks-in-a-project)
  - [Run a task in all projects](https://moonrepo.dev/docs/cheat-sheet#run-a-task-in-all-projects)
  - [Run a task in all projects with a tag](https://moonrepo.dev/docs/cheat-sheet#run-a-task-in-all-projects-with-a-tag)
  - [Run a task in a project](https://moonrepo.dev/docs/cheat-sheet#run-a-task-in-a-project)
  - [Run multiple tasks in all projects](https://moonrepo.dev/docs/cheat-sheet#run-multiple-tasks-in-all-projects)
  - [Run multiple tasks in any project](https://moonrepo.dev/docs/cheat-sheet#run-multiple-tasks-in-any-project)
  - [Run a task in applications, libraries, or tools](https://moonrepo.dev/docs/cheat-sheet#run-a-task-in-applications-libraries-or-tools)
  - [Run a task in projects of a specific language](https://moonrepo.dev/docs/cheat-sheet#run-a-task-in-projects-of-a-specific-language)
  - [Run a task in projects matching a keyword](https://moonrepo.dev/docs/cheat-sheet#run-a-task-in-projects-matching-a-keyword)
  - [Run a task in projects based on file path](https://moonrepo.dev/docs/cheat-sheet#run-a-task-in-projects-based-on-file-path)
- [Task configuration](https://moonrepo.dev/docs/cheat-sheet#task-configuration)
  - [Disable caching](https://moonrepo.dev/docs/cheat-sheet#disable-caching)
  - [Re-run flaky tasks](https://moonrepo.dev/docs/cheat-sheet#re-run-flaky-tasks)
  - [Depend on tasks from parent project's dependencies](https://moonrepo.dev/docs/cheat-sheet#depend-on-tasks-from-parent-projects-dependencies)
  - [Depend on tasks from arbitrary projects](https://moonrepo.dev/docs/cheat-sheet#depend-on-tasks-from-arbitrary-projects)
  - [Run dependencies serially](https://moonrepo.dev/docs/cheat-sheet#run-dependencies-serially)
  - [Run multiple watchers/servers in parallel](https://moonrepo.dev/docs/cheat-sheet#run-multiple-watchersservers-in-parallel)
- [Languages](https://moonrepo.dev/docs/cheat-sheet#languages)
  - [Run system binaries available on `PATH`](https://moonrepo.dev/docs/cheat-sheet#run-system-binaries-available-on-path)
  - [Run language binaries not supported in moon's toolchain](https://moonrepo.dev/docs/cheat-sheet#run-language-binaries-not-supported-in-moons-toolchain)
  - [Run npm binaries (Node.js)](https://moonrepo.dev/docs/cheat-sheet#run-npm-binaries-nodejs)