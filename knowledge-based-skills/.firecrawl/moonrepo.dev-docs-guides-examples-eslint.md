[Skip to main content](https://moonrepo.dev/docs/guides/examples/eslint#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [ESLint](https://eslint.org/) into moon.

Begin by installing `eslint` and any plugins in your root. We suggest using the same version across
the entire repository.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn add --dev eslint eslint-config-moon
```

```shell
yarn add --dev eslint eslint-config-moon

# If using workspaces
yarn add --dev -W eslint eslint-config-moon
```

```shell
npm install --save-dev eslint eslint-config-moon
```

```shell
pnpm add --save-dev eslint eslint-config-moon

# If using workspaces
pnpm add --save-dev -w eslint eslint-config-moon
```

```shell
bun install --dev eslint eslint-config-moon
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/eslint\#setup "Direct link to Setup")

Since linting is a universal workflow, add a `lint` task to [`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks)
with the following parameters.

.moon/tasks/eslint.yml

```yaml
tasks:
  lint:
    command:
      - 'eslint'
      # Support other extensions
      - '--ext'
      - '.js,.jsx,.ts,.tsx'
      # Always fix and run extra checks
      - '--fix'
      - '--report-unused-disable-directives'
      # Dont fail if a project has nothing to lint
      - '--no-error-on-unmatched-pattern'
      # Do fail if we encounter a fatal error
      - '--exit-on-fatal-error'
      # Only 1 ignore file is supported, so use the root
      - '--ignore-path'
      - '@in(4)'
      # Run in current dir
      - '.'
    inputs:
      # Source and test files
      - 'src/**/*'
      - 'tests/**/*'
      # Other config files
      - '*.config.*'
      # Project configs, any format, any depth
      - '**/.eslintrc.*'
      # Root configs, any format
      - '/.eslintignore'
      - '/.eslintrc.*'
```

Projects can extend this task and provide additional parameters if need be, for example.

<project>/moon.yml

```yaml
tasks:
  lint:
    args:
      # Enable caching for this project
      - '--cache'
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/eslint\#typescript-integration "Direct link to TypeScript integration")

If you're using the [`@typescript-eslint`](https://typescript-eslint.io/) packages, and want to
enable type-safety based lint rules, we suggest something similar to the official
[monorepo configuration](https://typescript-eslint.io/docs/linting/monorepo).

Create a `tsconfig.eslint.json` in your repository root, extend your shared compiler options (we use
[`tsconfig.options.json`](https://moonrepo.dev/docs/guides/examples/typescript)), and include all your project files.

tsconfig.eslint.json

```json
{
  "extends": "./tsconfig.options.json",
  "compilerOptions": {
    "emitDeclarationOnly": false,
    "noEmit": true
  },
  "include": ["apps/**/*", "packages/**/*"]
}
```

Append the following inputs to your `lint` task.

.moon/tasks/node.yml

```yaml
tasks:
  lint:
    # ...
    inputs:
      # TypeScript support
      - 'types/**/*'
      - 'tsconfig.json'
      - '/tsconfig.eslint.json'
      - '/tsconfig.options.json'
```

And lastly, add `parserOptions` to your [root-level config](https://moonrepo.dev/docs/guides/examples/eslint#root-level).

## Configuration [​](https://moonrepo.dev/docs/guides/examples/eslint\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/eslint\#root-level "Direct link to Root-level")

The root-level ESLint config is _required_, as ESLint traverses upwards from each file to find
configurations, and this denotes the stopping point. It's also used to define rules for the _entire_
repository.

.eslintrc.js

```js
module.exports = {
  root: true, // Required!
  extends: ['moon'],
  rules: {
    'no-console': 'error',
  },

  // TypeScript support
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.eslint.json',
    tsconfigRootDir: __dirname,
  },
};
```

The `.eslintignore` file must also be defined at the root, as
[only 1 ignore file](https://eslint.org/docs/user-guide/configuring/ignoring-code#the-eslintignore-file)
can exist in a repository. We ensure this ignore file is used by passing `--ignore-path` above.

.eslintignore

```bash
node_modules/
*.min.js
*.map
*.snap
```

### Project-level [​](https://moonrepo.dev/docs/guides/examples/eslint\#project-level "Direct link to Project-level")

A project-level ESLint config can be utilized by creating a `.eslintrc.<json|js|cjs|yml>` in the
project root. This is optional, but necessary when defining rules and ignore patterns unique to the
project.

<project>/.eslintrc.js

```js
module.exports = {
  // Patterns to ignore (alongside the root .eslintignore)
  ignorePatterns: ['build', 'lib'],
  // Project specific rules
  rules: {
    'no-console': 'off',
  },
};
```

> The
> [`extends`](https://eslint.org/docs/user-guide/configuring/configuration-files#extending-configuration-files)
> setting should **not** extend the root-level config, as ESLint will automatically merge configs
> while traversing upwards!

### Sharing [​](https://moonrepo.dev/docs/guides/examples/eslint\#sharing "Direct link to Sharing")

To share configuration across projects, you have 3 options:

- Define settings in the [root-level config](https://moonrepo.dev/docs/guides/examples/eslint#root-level). This only applies to the parent
repository.
- Create and publish an
[`eslint-config`](https://eslint.org/docs/developer-guide/shareable-configs#using-a-shareable-config)
or [`eslint-plugin`](https://eslint.org/docs/developer-guide/working-with-plugins) npm package.
This can be used in any repository.
- A combination of 1 and 2.

For options 2 and 3, if you're utilizing package workspaces, create a local package with the
following content.

packages/eslint-config-company/index.js

```js
module.exports = {
  extends: ['airbnb'],
};
```

Within your root-level ESLint config, you can extend this package to inherit the settings.

.eslintrc.js

```js
module.exports = {
  extends: 'eslint-config-company',
};
```

> When using this approach, the package must be built and symlinked into `node_modules` _before_ the
> linter will run correctly. Take this into account when going down this path!

## FAQ [​](https://moonrepo.dev/docs/guides/examples/eslint\#faq "Direct link to FAQ")

### How to lint a single file or folder? [​](https://moonrepo.dev/docs/guides/examples/eslint\#how-to-lint-a-single-file-or-folder "Direct link to How to lint a single file or folder?")

Unfortunately, this isn't currently possible, as the `eslint` binary itself requires a file or
folder path to operate on, and in the task above we pass `.` (current directory). If this was not
passed, then nothing would be linted.

This has the unintended side-effect of not being able to filter down lintable targets by passing
arbitrary file paths. This is something we hope to resolve in the future.

To work around this limitation, you can create another lint task.

### Should we use `overrides`? [​](https://moonrepo.dev/docs/guides/examples/eslint\#should-we-use-overrides "Direct link to should-we-use-overrides")

Projects should define their own rules using an ESLint config in their project root. However, if you
want to avoid touching many ESLint configs (think migrations), then
[overrides in the root](https://eslint.org/docs/user-guide/configuring/configuration-files#configuration-based-on-glob-patterns)
are a viable option. Otherwise, we highly encourage project-level configs.

.eslintrc.js

```js
module.exports = {
  // ...
  overrides: [\
    // Only apply to apps "foo" and "bar", but not others\
    {\
      files: ['apps/foo/**/*', 'apps/bar/**/*'],\
      rules: {\
        'no-magic-numbers': 'off',\
      },\
    },\
  ],
};
```

- [Setup](https://moonrepo.dev/docs/guides/examples/eslint#setup)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/eslint#typescript-integration)
- [Configuration](https://moonrepo.dev/docs/guides/examples/eslint#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/eslint#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/eslint#project-level)
  - [Sharing](https://moonrepo.dev/docs/guides/examples/eslint#sharing)
- [FAQ](https://moonrepo.dev/docs/guides/examples/eslint#faq)
  - [How to lint a single file or folder?](https://moonrepo.dev/docs/guides/examples/eslint#how-to-lint-a-single-file-or-folder)
  - [Should we use `overrides`?](https://moonrepo.dev/docs/guides/examples/eslint#should-we-use-overrides)