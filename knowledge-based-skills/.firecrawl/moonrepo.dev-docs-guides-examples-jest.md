[Skip to main content](https://moonrepo.dev/docs/guides/examples/jest#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Jest](https://jestjs.io/) into moon.

Begin by installing `jest` in your root. We suggest using the same version across the entire
repository.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn add --dev jest
```

```shell
yarn add --dev jest

# If using workspaces
yarn add --dev -W jest
```

```shell
npm install --save-dev jest
```

```shell
pnpm add --save-dev jest

# If using workspaces
pnpm add --save-dev -w jest
```

```shell
bun install --dev jest
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/jest\#setup "Direct link to Setup")

Since testing is a universal workflow, add a `test` task to [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks)
with the following parameters.

.moon/tasks/jest.yml

```yaml
tasks:
  test:
    command:
      - 'jest'
      # Always run code coverage
      - '--coverage'
      # Dont fail if a project has no tests
      - '--passWithNoTests'
    inputs:
      # Source and test files
      - 'src/**/*'
      - 'tests/**/*'
      # Project configs, any format
      - 'jest.config.*'
```

Projects can extend this task and provide additional parameters if need be, for example.

<project>/moon.yml

```yaml
tasks:
  test:
    args:
      # Disable caching for this project
      - '--no-cache'
```

## Configuration [​](https://moonrepo.dev/docs/guides/examples/jest\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/jest\#root-level "Direct link to Root-level")

A root-level Jest config is not required and should be avoided, instead, use a [preset](https://moonrepo.dev/docs/guides/examples/jest#sharing) to
share configuration.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/jest\#project-level "Direct link to Project-level")

A project-level Jest config can be utilized by creating a `jest.config.<js|ts|cjs|mjs>` in the
project root. This is optional, but necessary when defining project specific settings.

<project>/jest.config.js

```js
module.exports = {
  // Project specific settings
  testEnvironment: 'node',
};
```

### Sharing [​](https://moonrepo.dev/docs/guides/examples/jest\#sharing "Direct link to Sharing")

To share configuration across projects, you can utilize Jest's built-in
[`preset`](https://jestjs.io/docs/configuration#preset-string) functionality. If you're utilizing
package workspaces, create a local package with the following content, otherwise publish the npm
package for consumption.

packages/company-jest-preset/jest-preset.js

```js
module.exports = {
  testEnvironment: 'jsdom',
  watchman: true,
};
```

Within your project-level Jest config, you can extend the preset to inherit the settings.

<project>/jest.config.js

```js
module.exports = {
  preset: 'company-jest-preset',
};
```

> You can take this a step further by passing the `--preset` option in the [task above](https://moonrepo.dev/docs/guides/examples/jest#setup), so
> that all projects inherit the preset by default.

## FAQ [​](https://moonrepo.dev/docs/guides/examples/jest\#faq "Direct link to FAQ")

### How to test a single file or folder? [​](https://moonrepo.dev/docs/guides/examples/jest\#how-to-test-a-single-file-or-folder "Direct link to How to test a single file or folder?")

You can filter tests by passing a file name, folder name, glob, or regex pattern after `--`. Any
passed files are relative from the project's root, regardless of where the `moon` command is being
ran.

```shell
$ moon run <project>:test -- filename
```

### How to use `projects`? [​](https://moonrepo.dev/docs/guides/examples/jest\#how-to-use-projects "Direct link to how-to-use-projects")

With moon, there's no reason to use
[`projects`](https://jestjs.io/docs/configuration#projects-arraystring--projectconfig) as the `test`
task is ran _per_ project. If you'd like to test multiple projects, use
[`moon run :test`](https://moonrepo.dev/docs/commands/run).

- [Setup](https://moonrepo.dev/docs/guides/examples/jest#setup)
- [Configuration](https://moonrepo.dev/docs/guides/examples/jest#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/jest#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/jest#project-level)
  - [Sharing](https://moonrepo.dev/docs/guides/examples/jest#sharing)
- [FAQ](https://moonrepo.dev/docs/guides/examples/jest#faq)
  - [How to test a single file or folder?](https://moonrepo.dev/docs/guides/examples/jest#how-to-test-a-single-file-or-folder)
  - [How to use `projects`?](https://moonrepo.dev/docs/guides/examples/jest#how-to-use-projects)