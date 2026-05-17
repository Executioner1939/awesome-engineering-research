[Skip to main content](https://moonrepo.dev/docs/guides/examples/solid#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

[Solid](https://www.solidjs.com/) (also known as SolidJS) is a JavaScript framework for building
interactive web applications. Because of this, Solid is an application or library concern, and not a
build system one, since the bundling of Solid is abstracted away through the application or a
bundler.

With that being said, we do have some suggestions on utilizing Solid effectively in a monorepo. To
begin, install Solid to a project.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn workspace <project> add solid-js
```

```shell
yarn workspace <project> add solid-js
```

```shell
npm install --workspace <project> solid-js
```

```shell
pnpm add --filter <project> solid-js
```

```shell
bun install solid-js
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/solid\#setup "Direct link to Setup")

Solid utilizes JSX for rendering markup, which requires
[`babel-preset-solid`](https://www.npmjs.com/package/babel-preset-solid) for parsing and
transforming. To enable the preset for the entire monorepo, add the preset to a root
`babel.config.js`, otherwise add it to a `.babelrc.js` in each project that requires it.

```js
module.exports = {
  presets: ['solid'],
};
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/solid\#typescript-integration "Direct link to TypeScript integration")

For each project using Solid, add the following compiler options to the `tsconfig.json` found in the
project root.

<project>/tsconfig.json

```json
{
  "compilerOptions": {
    "jsx": "preserve",
    "jsxImportSource": "solid-js"
  }
}
```

### Vite integration [​](https://moonrepo.dev/docs/guides/examples/solid\#vite-integration "Direct link to Vite integration")

If you're using a [Vite](https://moonrepo.dev/docs/guides/examples/vite) powered application (Solid Start or starter templates), you should
enable [`vite-plugin-solid`](https://www.npmjs.com/package/vite-plugin-solid) instead of configuring
Babel. Be sure to read our [guide on Vite](https://moonrepo.dev/docs/guides/examples/vite) as well!

<project>/vite.config.js

```js
import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';

export default defineConfig({
  // ...
  plugins: [solidPlugin()],
});
```

- [Setup](https://moonrepo.dev/docs/guides/examples/solid#setup)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/solid#typescript-integration)
  - [Vite integration](https://moonrepo.dev/docs/guides/examples/solid#vite-integration)