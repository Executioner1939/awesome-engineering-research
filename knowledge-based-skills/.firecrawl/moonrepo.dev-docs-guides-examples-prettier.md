[Skip to main content](https://moonrepo.dev/docs/guides/examples/prettier#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Prettier](https://prettier.io/) into moon.

Begin by installing `prettier` in your root. We suggest using the same version across the entire
repository.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn add --dev prettier
```

```shell
yarn add --dev prettier

# If using workspaces
yarn add --dev -W prettier
```

```shell
npm install --save-dev prettier
```

```shell
pnpm add --save-dev prettier

# If using workspaces
pnpm add --save-dev -w prettier
```

```shell
bun install --dev prettier
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/prettier\#setup "Direct link to Setup")

Since code formatting is a universal workflow, add a `format` task to
[`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks) with the following parameters.

.moon/tasks/prettier.yml

```yaml
tasks:
  format:
    command:
      - 'prettier'
      # Use the same config for the entire repo
      - '--config'
      - '@in(4)'
      # Use the same ignore patterns as well
      - '--ignore-path'
      - '@in(3)'
      # Fail for unformatted code
      - '--check'
      # Run in current dir
      - '.'
    inputs:
      # Source and test files
      - 'src/**/*'
      - 'tests/**/*'
      # Config and other files
      - '**/*.{md,mdx,yml,yaml,json}'
      # Root configs, any format
      - '/.prettierignore'
      - '/.prettierrc.*'
```

## Configuration [​](https://moonrepo.dev/docs/guides/examples/prettier\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/prettier\#root-level "Direct link to Root-level")

The root-level Prettier config is _required_, as it defines conventions and standards to apply to
the entire repository.

.prettierrc.js

```js
module.exports = {
  arrowParens: 'always',
  semi: true,
  singleQuote: true,
  tabWidth: 2,
  trailingComma: 'all',
  useTabs: true,
};
```

The `.prettierignore` file must also be defined at the root, as
[only 1 ignore file](https://prettier.io/docs/en/ignore.html#ignoring-files-prettierignore) can
exist in a repository. We ensure this ignore file is used by passing `--ignore-path` above.

.prettierignore

```bash
node_modules/
*.min.js
*.map
*.snap
```

### Project-level [​](https://moonrepo.dev/docs/guides/examples/prettier\#project-level "Direct link to Project-level")

We suggest _against_ project-level configurations, as the entire repository should be formatted
using the same standards. However, if you're migrating code and need an escape hatch,
[overrides in the root](https://prettier.io/docs/en/configuration.html#configuration-overrides) will
work.

## FAQ [​](https://moonrepo.dev/docs/guides/examples/prettier\#faq "Direct link to FAQ")

### How to use `--write`? [​](https://moonrepo.dev/docs/guides/examples/prettier\#how-to-use---write "Direct link to how-to-use---write")

Unfortunately, this isn't currently possible, as the `prettier` binary itself requires either the
`--check` or `--write` options, and since we're configuring `--check` in the task above, that takes
precedence. This is also the preferred pattern as checks will run (and fail) in CI.

To work around this limitation, we suggest the following alternatives:

- Configure your editor to run Prettier on save.
- Define another task to write the formatted code, like `format-write`.

- [Setup](https://moonrepo.dev/docs/guides/examples/prettier#setup)
- [Configuration](https://moonrepo.dev/docs/guides/examples/prettier#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/prettier#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/prettier#project-level)
- [FAQ](https://moonrepo.dev/docs/guides/examples/prettier#faq)
  - [How to use `--write`?](https://moonrepo.dev/docs/guides/examples/prettier#how-to-use---write)