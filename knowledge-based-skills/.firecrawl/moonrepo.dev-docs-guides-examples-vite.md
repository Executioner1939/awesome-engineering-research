[Skip to main content](https://moonrepo.dev/docs/guides/examples/vite#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Vite](https://vitejs.dev/) and
[Vitest](https://vitest.dev/) into moon.

Begin by creating a new Vite project in the root of an existing moon project (this should not be
created in the workspace root, unless a polyrepo).

- Yarn
- Yarn (classic)
- npm
- pnpm

```shell
yarn create vite
```

```shell
yarn create vite
```

```shell
npm create vite
```

```shell
pnpm create vite
```

If you plan on using Vitest, run the following command to add the `vitest` dependency to a project,
otherwise skip to the setup section.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn workspace <project> add --dev vitest
```

```shell
yarn workspace <project> add --dev vitest
```

```shell
npm install --save-dev --workspace <project> vitest
```

```shell
pnpm add --save-dev --filter <project> vitest
```

```shell
bun install --dev vitest
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/vite\#setup "Direct link to Setup")

Since Vite is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

tip

We suggest inheriting Vite tasks from the
[official moon configuration preset](https://github.com/moonrepo/moon-configs/tree/master/javascript/vite).

<project>/moon.yml

```yaml
# Inherit tasks from the `vite` and `vitest` presets
# https://github.com/moonrepo/moon-configs
tags: ['vite', 'vitest']
```

## Configuration [​](https://moonrepo.dev/docs/guides/examples/vite\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/vite\#root-level "Direct link to Root-level")

We suggest _against_ root-level configuration, as Vite should be installed per-project, and the
`vite` command expects the configuration to live relative to the project root.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/vite\#project-level "Direct link to Project-level")

When creating a new Vite project, a [`vite.config.<js|ts>`](https://vitejs.dev/config) is created,
and _must_ exist in the project root.

<project>/vite.config.js

```js
import { defineConfig } from 'vite';

export default defineConfig({
  // ...
  build: {
    // These must be `outputs` in the `build` task
    outDir: 'dist',
  },
  test: {
    // Vitest settings
  },
});
```

> If you'd prefer to configure Vitest in a
> [separate configuration file](https://vitest.dev/guide/#configuring-vitest), create a
> `vitest.config.<js|ts>` file.

- [Setup](https://moonrepo.dev/docs/guides/examples/vite#setup)
- [Configuration](https://moonrepo.dev/docs/guides/examples/vite#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/vite#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/vite#project-level)