[Skip to main content](https://moonrepo.dev/docs/guides/examples/sveltekit#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

[SvelteKit](https://kit.svelte.dev/) is built on [Svelte](https://svelte.dev/), a UI framework that
uses a compiler to let you write breathtakingly concise components that do minimal work in the
browser, using languages you already know — HTML, CSS and JavaScript. It's a love letter to web
development.

```shell
cd apps && npm create svelte@latest <project>
```

You will be prompted to choose between select templates, TypeScript, ESLint, Prettier, Playwright
and Vitest among other options. moon supports and has guides for many of these tools.

> We highly suggest reading our documentation on [using Vite (and Vitest) with moon](https://moonrepo.dev/docs/guides/examples/vite),
> [using ESLint with moon](https://moonrepo.dev/docs/guides/examples/eslint) and [using Prettier with moon](https://moonrepo.dev/docs/guides/examples/prettier) for a more holistic
> view.

## Setup [​](https://moonrepo.dev/docs/guides/examples/sveltekit\#setup "Direct link to Setup")

Since SvelteKit is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

tip

We suggest inheriting SvelteKit tasks from the
[official moon configuration preset](https://github.com/moonrepo/moon-configs/tree/master/javascript/sveltekit).

<project>/moon.yml

```yaml
# Inherit tasks from the `sveltekit` preset
# https://github.com/moonrepo/moon-configs
tags: ['sveltekit']
```

### ESLint integration [​](https://moonrepo.dev/docs/guides/examples/sveltekit\#eslint-integration "Direct link to ESLint integration")

SvelteKit provides an option to setup ESLint along with your project, with moon you can use a
[global `lint` task](https://moonrepo.dev/docs/guides/examples/eslint). We encourage using the global `lint` task for consistency across all
projects within the repository. With this approach, the `eslint` command itself will be ran and the
`svelte3` rules will still be used.

<project>/moon.yml

```yaml
tasks:
  # Extends the top-level lint
  lint:
    args:
      - '--ext'
      - '.ts,.svelte'
```

Be sure to enable the Svelte parser and plugin in a project local ESLint configuration file.

.eslintrc.cjs

```js
module.exports = {
  plugins: ['svelte3'],
  ignorePatterns: ['*.cjs'],
  settings: {
    'svelte3/typescript': () => require('typescript'),
  },
  overrides: [{ files: ['*.svelte'], processor: 'svelte3/svelte3' }],
};
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/sveltekit\#typescript-integration "Direct link to TypeScript integration")

SvelteKit also has built-in support for TypeScript, but has similar caveats to the
[ESLint integration](https://moonrepo.dev/docs/guides/examples/sveltekit#eslint-integration). TypeScript itself is a bit involved, so we suggest
reading the official [SvelteKit documentation](https://kit.svelte.dev/docs/introduction) before
continuing.

At this point we'll assume that a `tsconfig.json` has been created in the application, and
typechecking works. From here we suggest utilizing a [global `typecheck` task](https://moonrepo.dev/docs/guides/examples/typescript) for
consistency across all projects within the repository. However, because Svelte isn't standard
JavaScript, it requires the use of the `svelte-check` command for type-checking.

info

The
[moon configuration preset](https://github.com/moonrepo/moon-configs/tree/master/javascript/sveltekit)
provides the `check` task below.

<project>/moon.yml

```yaml
workspace:
  inheritedTasks:
    exclude: ['typecheck']

tasks:
  check:
    command: 'svelte-check --tsconfig ./tsconfig.json'
    deps:
      - 'typecheck-sync'
    inputs:
      - '@group(svelte)'
      - 'tsconfig.json'
```

In case Svelte doesn't automatically create a `tsconfig.json`, you can use the following:

<project>/tsconfig.json

```json
{
  "extends": "./.svelte-kit/tsconfig.json",
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "skipLibCheck": true,
    "sourceMap": true,
    "strict": true
  }
}
```

## Configuration [​](https://moonrepo.dev/docs/guides/examples/sveltekit\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/sveltekit\#root-level "Direct link to Root-level")

We suggest _against_ root-level configuration, as SvelteKit should be installed per-project, and the
`vite` command expects the configuration to live relative to the project root.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/sveltekit\#project-level "Direct link to Project-level")

When creating a new SvelteKit project, a
[`svelte.config.js`](https://kit.svelte.dev/docs/configuration) is created, and _must_ exist in the
project root. This allows each project to configure SvelteKit for their needs.

<project>/svelte.config.js

```js
import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://kit.svelte.dev/docs/integrations#preprocessors
  // for more information about preprocessors
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter(),
  },
};

export default config;
```

- [Setup](https://moonrepo.dev/docs/guides/examples/sveltekit#setup)
  - [ESLint integration](https://moonrepo.dev/docs/guides/examples/sveltekit#eslint-integration)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/sveltekit#typescript-integration)
- [Configuration](https://moonrepo.dev/docs/guides/examples/sveltekit#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/sveltekit#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/sveltekit#project-level)