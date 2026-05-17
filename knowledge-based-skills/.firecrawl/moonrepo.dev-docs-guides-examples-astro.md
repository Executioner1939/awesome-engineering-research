[Skip to main content](https://moonrepo.dev/docs/guides/examples/astro#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Astro](https://docs.astro.build/).

Begin by creating a new Astro project in the root of an existing moon project (this should not be
created in the workspace root, unless a polyrepo).

```shell
cd apps && npm create astro@latest
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/astro\#setup "Direct link to Setup")

Since Astro is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

tip

We suggest inheriting Astro tasks from the
[official moon configuration preset](https://github.com/moonrepo/moon-configs/tree/master/javascript/astro).

<project>/moon.yml

```yaml
# Inherit tasks from the `astro` preset
# https://github.com/moonrepo/moon-configs
tags: ['astro']

# Disable project references
toolchains:
  typescript:
    syncProjectReferences: false
```

### ESLint integration [​](https://moonrepo.dev/docs/guides/examples/astro\#eslint-integration "Direct link to ESLint integration")

When using a [`lint`](https://moonrepo.dev/docs/guides/examples/eslint) task, the
[`eslint-plugin-astro`](https://ota-meshi.github.io/eslint-plugin-astro/user-guide/) package must be
installed to lint `.astro` files.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn workspace <app> add --dev eslint-plugin-astro
```

```shell
yarn workspace <app> add --dev eslint-plugin-astro
```

```shell
npm install --save-dev --workspace <app> eslint-plugin-astro
```

```shell
pnpm add --save-dev --filter <app> eslint-plugin-astro
```

```shell
bun install --dev eslint-plugin-astro
```

Once the dependency has been installed in the application's `package.json`. We can then enable this
configuration by creating an `.eslintrc.js` file in the project root. Be sure this file is listed in
your lint task's inputs!

<project>/.eslintrc.js

```js
module.exports = {
  extends: ['plugin:astro/recommended'],
  overrides: [\
    {\
      files: ['*.astro'],\
      parser: 'astro-eslint-parser',\
      // If using TypeScript\
      parserOptions: {\
        parser: '@typescript-eslint/parser',\
        extraFileExtensions: ['.astro'],\
        project: 'tsconfig.json',\
        tsconfigRootDir: __dirname,\
      },\
    },\
  ],
};
```

And lastly, when linting through moon's command line, you'll need to include the `.astro` extension
within the `lint` task. This can be done by extending the top-level task within the project (below),
or by adding it to the top-level entirely.

<project>/moon.yml

```yaml
tasks:
  lint:
    args:
      - '--ext'
      - '.ts,.tsx,.astro'
```

### Prettier integration [​](https://moonrepo.dev/docs/guides/examples/astro\#prettier-integration "Direct link to Prettier integration")

When using a [`format`](https://moonrepo.dev/docs/guides/examples/prettier) task, the `prettier-plugin-astro` package must be installed to
format `.astro` files. View the official
[Astro docs](https://docs.astro.build/en/editor-setup/#prettier) for more information.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn workspace <app> add --dev prettier-plugin-astro
```

```shell
yarn workspace <app> add --dev prettier-plugin-astro
```

```shell
npm install --save-dev --workspace <app> prettier-plugin-astro
```

```shell
pnpm add --save-dev --filter <app> prettier-plugin-astro
```

```shell
bun install --dev prettier-plugin-astro
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/astro\#typescript-integration "Direct link to TypeScript integration")

Since Astro utilizes custom `.astro` files, it requires a specialized TypeScript integration, and
luckily Astro provides an [in-depth guide](https://docs.astro.build/en/guides/typescript/). With
that being said, we do have a few requirements and pointers!

- Use the official [Astro `tsconfig.json`](https://docs.astro.build/en/guides/typescript/#setup) as
a basis.
- From our internal testing, the `astro check` command (that typechecks `.astro` files) _does not_
_support project references_. If the `composite` compiler option is enabled, the checker will fail
to find `.astro` files. To work around this, we disable `workspace.typescript` in our moon config
above.
- Since typechecking requires 2 commands, one for `.astro` files, and the other for `.ts`, `.tsx`
files, we've added the [`typecheck`](https://moonrepo.dev/docs/guides/examples/typescript) task as a dependency for the `check` task. This
will run both commands through a single task!

## Configuration [​](https://moonrepo.dev/docs/guides/examples/astro\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/astro\#root-level "Direct link to Root-level")

We suggest _against_ root-level configuration, as Astro should be installed per-project, and the
`astro` command expects the configuration to live relative to the project root.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/astro\#project-level "Direct link to Project-level")

When creating a new Astro project, a
[`astro.config.mjs`](https://docs.astro.build/en/reference/configuration-reference/) is created, and
_must_ exist in the project root. This allows each project to configure Astro for their needs.

<project>/astro.config.mjs

```js
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({});
```

- [Setup](https://moonrepo.dev/docs/guides/examples/astro#setup)
  - [ESLint integration](https://moonrepo.dev/docs/guides/examples/astro#eslint-integration)
  - [Prettier integration](https://moonrepo.dev/docs/guides/examples/astro#prettier-integration)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/astro#typescript-integration)
- [Configuration](https://moonrepo.dev/docs/guides/examples/astro#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/astro#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/astro#project-level)