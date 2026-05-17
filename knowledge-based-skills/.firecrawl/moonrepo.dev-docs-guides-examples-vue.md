[Skip to main content](https://moonrepo.dev/docs/guides/examples/vue#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Vue is an application or library concern, and not a build system one, since the bundling of Vue is
abstracted away through other tools. Because of this, moon has no guidelines around utilizing Vue
directly. You can use Vue however you wish!

However, with that being said, Vue is typically coupled with [Vite](https://vitejs.dev/). To
scaffold a new Vue project with Vite, run the following command in a project root.

```shell
npm init vue@latest
```

> We highly suggest reading our documentation on [using Vite (and Vitest) with moon](https://moonrepo.dev/docs/guides/examples/vite) for a
> more holistic view.

## Setup [​](https://moonrepo.dev/docs/guides/examples/vue\#setup "Direct link to Setup")

This section assumes Vue is being used with Vite.

### ESLint integration [​](https://moonrepo.dev/docs/guides/examples/vue\#eslint-integration "Direct link to ESLint integration")

When linting with [ESLint](https://moonrepo.dev/docs/guides/examples/eslint) and the
[`eslint-plugin-vue`](https://eslint.vuejs.org/user-guide/#installation) library, you'll need to
include the `.vue` extension within the `lint` task. This can be done by extending the top-level
task within the project (below), or by adding it to the top-level entirely.

<project>/moon.yml

```yaml
tasks:
  lint:
    args:
      - '--ext'
      - '.js,.ts,.vue'
```

Furthermore, when using TypeScript within ESLint, we need to make a few additional changes to the
`.eslintrc.js` config found in the root (if the entire repo is Vue), or within the project (if only
the project is Vue).

```js
module.exports = {
  parser: 'vue-eslint-parser',
  parserOptions: {
    extraFileExtensions: ['.vue'],
    parser: '@typescript-eslint/parser',
    project: 'tsconfig.json', // Or another config
    tsconfigRootDir: __dirname,
  },
};
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/vue\#typescript-integration "Direct link to TypeScript integration")

Vue does not use [TypeScript](https://moonrepo.dev/docs/guides/examples/typescript)'s `tsc` binary directly, but instead uses
[`vue-tsc`](https://vuejs.org/guide/typescript/overview.html), which is a thin wrapper around `tsc`
to support Vue components. Because of this, we should update the `typecheck` task in the project to
utilize this command instead.

<project>/moon.yml

```yaml
workspace:
  inheritedTasks:
    exclude: ['typecheck']

tasks:
  typecheck:
    command:
      - 'vue-tsc'
      - '--noEmit'
      # Always use pretty output
      - '--pretty'
    inputs:
      - 'env.d.ts'
      # Source and test files
      - 'src/**/*'
      - 'tests/**/*'
      # Project configs
      - 'tsconfig.json'
      - 'tsconfig.*.json'
      # Root configs (extended from only)
      - '/tsconfig.options.json'
```

> Be sure `tsconfig.json` compiler options are based on
> [`@vue/tsconfig`](https://vuejs.org/guide/typescript/overview.html#configuring-tsconfig-json).

- [Setup](https://moonrepo.dev/docs/guides/examples/vue#setup)
  - [ESLint integration](https://moonrepo.dev/docs/guides/examples/vue#eslint-integration)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/vue#typescript-integration)