[Skip to main content](https://moonrepo.dev/docs/guides/examples/nuxt#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Nuxt v3](https://nuxt.com/), a [Vue](https://moonrepo.dev/docs/guides/examples/vue) framework,
into moon.

Begin by creating a new Nuxt project at a specified folder path (this should not be created in the
workspace root, unless a polyrepo).

```shell
cd apps && npx nuxi init <project>
```

> View the [official Nuxt docs](https://nuxt.com/docs/getting-started/installation) for a more
> in-depth guide to getting started!

## Setup [​](https://moonrepo.dev/docs/guides/examples/nuxt\#setup "Direct link to Setup")

Since Nuxt is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

<project>/moon.yml

```yaml
fileGroups:
  nuxt:
    - 'assets/**/*'
    - 'components/**/*'
    - 'composables/**/*'
    - 'content/**/*'
    - 'layouts/**/*'
    - 'middleware/**/*'
    - 'pages/**/*'
    - 'plugins/**/*'
    - 'public/**/*'
    - 'server/**/*'
    - 'utils/**/*'
    - '.nuxtignore'
    - 'app.config.*'
    - 'app.vue'
    - 'nuxt.config.*'

tasks:
  nuxt:
    command: 'nuxt'
    preset: 'server'

  # Production build
  build:
    command: 'nuxt build'
    inputs:
      - '@group(nuxt)'
    outputs:
      - '.nuxt'
      - '.output'

  # Development server
  dev:
    command: 'nuxt dev'
    preset: 'server'

  # Preview production build locally
  preview:
    command: 'nuxt preview'
    deps:
      - '~:build'
    preset: 'server'
```

Be sure to keep the `postinstall` script in your project's `package.json`.

<project>/package.json

```json
{
  // ...
  "scripts": {
    "postinstall": "nuxt prepare"
  }
}
```

### ESLint integration [​](https://moonrepo.dev/docs/guides/examples/nuxt\#eslint-integration "Direct link to ESLint integration")

Refer to our [Vue documentation](https://moonrepo.dev/docs/guides/examples/vue#eslint-integration) for more information on linting.

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/nuxt\#typescript-integration "Direct link to TypeScript integration")

Nuxt requires `vue-tsc` for typechecking, so refer to our
[Vue documentation](https://moonrepo.dev/docs/guides/examples/vue#typescript-integration) for more information.

## Configuration [​](https://moonrepo.dev/docs/guides/examples/nuxt\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/nuxt\#root-level "Direct link to Root-level")

We suggest _against_ root-level configuration, as Nuxt should be installed per-project, and the
`nuxt` command expects the configuration to live relative to the project root.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/nuxt\#project-level "Direct link to Project-level")

When creating a new Nuxt project, a
[`nuxt.config.ts`](https://v3.nuxtjs.org/api/configuration/nuxt-config) is created, and _must_ exist
in the project root. This allows each project to configure Next.js for their needs.

<project>/nuxt.config.ts

```js
export default defineNuxtConfig({});
```

## Testing [​](https://moonrepo.dev/docs/guides/examples/nuxt\#testing "Direct link to Testing")

Nuxt supports testing through [Jest](https://jestjs.io/) or [Vitest](https://vitest.dev/). Refer to
our [Jest documentation](https://moonrepo.dev/docs/guides/examples/jest) or [Vitest documentation](https://moonrepo.dev/docs/guides/examples/vite) for more information on testing.

- [Setup](https://moonrepo.dev/docs/guides/examples/nuxt#setup)
  - [ESLint integration](https://moonrepo.dev/docs/guides/examples/nuxt#eslint-integration)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/nuxt#typescript-integration)
- [Configuration](https://moonrepo.dev/docs/guides/examples/nuxt#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/nuxt#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/nuxt#project-level)
- [Testing](https://moonrepo.dev/docs/guides/examples/nuxt#testing)