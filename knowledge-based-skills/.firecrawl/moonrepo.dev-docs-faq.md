[Skip to main content](https://moonrepo.dev/docs/faq#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

## General [​](https://moonrepo.dev/docs/faq\#general "Direct link to General")

### Where did the name "moon" come from? [​](https://moonrepo.dev/docs/faq\#where-did-the-name-moon-come-from "Direct link to Where did the name \"moon\" come from?")

The first incarnation of the name was a misspelling of monorepo (= moonrepo). This is where the
domain moonrepo.dev came from, and our official company, moonrepo, Inc.

However, moonrepo is quite a long name with many syllables, and as someone who prefers short 1
syllable words, moon was perfect. The word moon also has great symmetry, as you can see in our logo!

But that's not all... moon is also an acronym. It originally stood for **m** onorepo,
**o** rganization, **o** rchestration, and **n** otification tool. But since moon can also be used for
polyrepos, we replaced monorepo with **m** anagement (as shown on the homepage). This is a great
acronym, as it embraces what moon is trying to solve:

- **M** anage repos, projects, and tasks with ease.
- **O** rganize projects and the repo to scale.
- **O** rchestrate tasks as efficiently as possible.
- **N** otify developers and systems about important events.

### Will moon support other languages? [​](https://moonrepo.dev/docs/faq\#will-moon-support-other-languages "Direct link to Will moon support other languages?")

Yes! Although we're focusing right now on the web ecosystem (Node.js, Rust, Go, PHP, Python, etc),
we've designed moon to be language agnostic and easily pluggable in the future. View our
[supported languages for more information](https://moonrepo.dev/docs#supported-languages).

### Will moon support continuous deployment? [​](https://moonrepo.dev/docs/faq\#will-moon-support-continuous-deployment "Direct link to Will moon support continuous deployment?")

Yes! We plan to integrate CD with the current build and CI system, but we are focusing on the latter
2 for the time being. Why not start using moon today so that you can easily adopt CD when it's
ready?

### How to stop moon formatting JSON and YAML files? [​](https://moonrepo.dev/docs/faq\#how-to-stop-moon-formatting-json-and-yaml-files "Direct link to How to stop moon formatting JSON and YAML files?")

To ensure a healthy repository state, moon constantly modifies JSON and YAML files, specifically
`package.json` and `tsconfig.json`. This may result in a different formatting style in regards to
indentation. While there is no way to stop or turn off this functionality, we respect
[EditorConfig](https://editorconfig.org/) during this process.

Create a root `.editorconfig` file to enforce a consistent syntax.

.editorconfig

```ini
[*.{json,yaml,yml}]
indent_style = space
indent_size = 4
```

## Projects & tasks [​](https://moonrepo.dev/docs/faq\#projects--tasks "Direct link to Projects & tasks")

### How to pipe or redirect tasks? [​](https://moonrepo.dev/docs/faq\#how-to-pipe-or-redirect-tasks "Direct link to How to pipe or redirect tasks?")

Piping (`|`) or redirecting (`>`) the output of one moon task to another moon task, whether via
stdin or through `inputs`, is not possible within our pipeline (task runner) directly.

However, we do support this functionality on the command line, or within a task itself, using the
[`script`](https://moonrepo.dev/docs/config/project#script) setting.

moon.yml

```yaml
tasks:
  pipe:
    script: 'gen-json | jq ...'
```

Alternativaly, you can wrap this script in something like a Bash file, and execute that instead.

scripts/pipe.sh

```bash
#!/usr/bin/env bash
gen-json | jq ...
```

moon.yml

```yaml
tasks:
  pipe:
    command: 'bash ./scripts/pipe.sh'
```

### How to run multiple commands within a task? [​](https://moonrepo.dev/docs/faq\#how-to-run-multiple-commands-within-a-task "Direct link to How to run multiple commands within a task?")

Only [`script`](https://moonrepo.dev/docs/config/project#script) based tasks can run multiple commands via `&&` or `;`
syntax. This is possible as we execute the entire script within a shell, and not directly with the
toolchain.

moon.yml

```yaml
tasks:
  multiple:
    script: 'mkdir test && cd test && do-something'
```

### How to run tasks in a shell? [​](https://moonrepo.dev/docs/faq\#how-to-run-tasks-in-a-shell "Direct link to How to run tasks in a shell?")

By default, all tasks run in a shell, based on the task's [`shell`](https://moonrepo.dev/docs/config/project#shell) option,
as demonstrated below:

moon.yml

```yaml
tasks:
  # Runs in a shell
  global:
    command: 'some-command-on-path'

  # Custom shells
  unix:
    command: 'bash -c some-command'
    options:
      shell: false
  windows:
    command: 'pwsh.exe -c some-command'
    options:
      shell: false
```

### Can we run other languages? [​](https://moonrepo.dev/docs/faq\#can-we-run-other-languages "Direct link to Can we run other languages?")

Yes! Although our toolchain only supports a few languages at this time, you can still run other
languages within tasks by setting their [`toolchain`](https://moonrepo.dev/docs/config/project#toolchain) to "system".
System tasks are an escape hatch that will use any command available on the current machine.

moon.yml

```yaml
tasks:
  # Ruby
  lint:
    command: 'rubocop'
    toolchain: 'system'
  # PHP
  test:
    command: 'phpunit tests'
    toolchain: 'system'
```

However, because these languages are not supported directly within our toolchain, they will not
receive the benefits of the toolchain. Some of which are:

- Automatic installation of the language. System tasks expect the command to already exist in the
environment, which requires the user to manually install them.
- Consistent language and dependency manager versions across all machines.
- Built-in cpu and heap profiling (language specific).
- Automatic dependency installs when the lockfile changes.
- And many more.

## JavaScript ecosystem [​](https://moonrepo.dev/docs/faq\#javascript-ecosystem "Direct link to JavaScript ecosystem")

### Can we use `package.json` scripts? [​](https://moonrepo.dev/docs/faq\#can-we-use-packagejson-scripts "Direct link to can-we-use-packagejson-scripts")

We encourage everyone to define tasks in a [`moon.*`](https://moonrepo.dev/docs/config/project#tasks) file, as it allows for
additional metadata like `inputs`, `outputs`, `options`, and more. However, if you'd like to keep
using `package.json` scripts, enable the
[`node.inferTasksFromScripts`](https://moonrepo.dev/docs/config/toolchain#infertasksfromscripts) setting.

### Can moon version/publish packages? [​](https://moonrepo.dev/docs/faq\#can-moon-versionpublish-packages "Direct link to Can moon version/publish packages?")

At this time, no, as we're focusing on the build and test aspect of development. With that being
said, this is something we'd like to support first-class in the future, but until then, we suggest
the following popular tools:

- [Yarn releases](https://yarnpkg.com/features/release-workflow) (requires >= v2)
- [Changesets](https://github.com/changesets/changesets)
- [Lerna](https://github.com/lerna/lerna)

### Why is npm/pnpm/yarn install running twice when running a task? [​](https://moonrepo.dev/docs/faq\#why-is-npmpnpmyarn-install-running-twice-when-running-a-task "Direct link to Why is npm/pnpm/yarn install running twice when running a task?")

moon will automatically install dependencies in a project or in the workspace root (when using
package workspaces) when the lockfile or `package.json` has been modified since the last time the
install ran. If you are running a task and multiple installs are occurring (and it's causing
issues), it can mean 1 of 2 things:

- If you are using package workspaces, then one of the projects triggering the install is not listed
within the `workspaces` field in the root `package.json` (for npm and yarn), or in
`pnpm-workspace.*` (for pnpm).
- If the install is triggering in a non-JavaScript related project, then this project is incorrectly
listed as a package workspace.
- If you don't want a package included in the workspace, but do want to install its dependencies,
then it'll need its own lockfile.

## Troubleshooting [​](https://moonrepo.dev/docs/faq\#troubleshooting "Direct link to Troubleshooting")

### How to resolve the "version 'GLIBC\_X.XX' not found" error? [​](https://moonrepo.dev/docs/faq\#how-to-resolve-the-version-glibc_xxx-not-found-error "Direct link to How to resolve the \"version 'GLIBC_X.XX' not found\" error?")

This is typically caused by running moon in an old environment, like Ubuntu 18, and the minimum
required libc doesn't exist or is too old. Since moon is Rust based, we're unable to support all
environments and versions perpetually, and will only support relatively modern environments.

There's not an easy fix to this problem, but there are a few potential solutions, from easiest to
hardest:

- Run moon in a Docker container/image that has the correct environment and libs. For example, the
`node:latest` image.
- Upgrade the environment to a newer one. For example, Ubuntu 18 -> 22.
- Try and install a newer libc
( [more information](https://stackoverflow.com/questions/72513993/how-install-glibc-2-29-or-higher-in-ubuntu-18-04)).

For more information on this problem as a whole,
[refer to this in-depth article](https://kobzol.github.io/rust/ci/2021/05/07/building-rust-binaries-in-ci-that-work-with-older-glibc.html).

- [General](https://moonrepo.dev/docs/faq#general)
  - [Where did the name "moon" come from?](https://moonrepo.dev/docs/faq#where-did-the-name-moon-come-from)
  - [Will moon support other languages?](https://moonrepo.dev/docs/faq#will-moon-support-other-languages)
  - [Will moon support continuous deployment?](https://moonrepo.dev/docs/faq#will-moon-support-continuous-deployment)
  - [How to stop moon formatting JSON and YAML files?](https://moonrepo.dev/docs/faq#how-to-stop-moon-formatting-json-and-yaml-files)
- [Projects & tasks](https://moonrepo.dev/docs/faq#projects--tasks)
  - [How to pipe or redirect tasks?](https://moonrepo.dev/docs/faq#how-to-pipe-or-redirect-tasks)
  - [How to run multiple commands within a task?](https://moonrepo.dev/docs/faq#how-to-run-multiple-commands-within-a-task)
  - [How to run tasks in a shell?](https://moonrepo.dev/docs/faq#how-to-run-tasks-in-a-shell)
  - [Can we run other languages?](https://moonrepo.dev/docs/faq#can-we-run-other-languages)
- [JavaScript ecosystem](https://moonrepo.dev/docs/faq#javascript-ecosystem)
  - [Can we use `package.json` scripts?](https://moonrepo.dev/docs/faq#can-we-use-packagejson-scripts)
  - [Can moon version/publish packages?](https://moonrepo.dev/docs/faq#can-moon-versionpublish-packages)
  - [Why is npm/pnpm/yarn install running twice when running a task?](https://moonrepo.dev/docs/faq#why-is-npmpnpmyarn-install-running-twice-when-running-a-task)
- [Troubleshooting](https://moonrepo.dev/docs/faq#troubleshooting)
  - [How to resolve the "version 'GLIBC\_X.XX' not found" error?](https://moonrepo.dev/docs/faq#how-to-resolve-the-version-glibc_xxx-not-found-error)