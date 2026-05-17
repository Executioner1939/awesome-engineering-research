[Skip to main content](https://moonrepo.dev/docs/guides/examples/remix#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Remix](https://remix.run/) into moon.

Begin by creating a new Remix project at a specified folder path (this should not be created in the
workspace root, unless a polyrepo).

```shell
cd apps && npx create-remix
```

During this installation, Remix will ask a handful of questions, but be sure to answer "No" for the
"Do you want me to run `npm install`?" question. We suggest installing dependencies at the workspace
root via package workspaces!

> View the [official Remix docs](https://remix.run/docs/en/v1) for a more in-depth guide to getting
> started!

## Setup [​](https://moonrepo.dev/docs/guides/examples/remix\#setup "Direct link to Setup")

Since Remix is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

tip

We suggest inheriting Remix tasks from the
[official moon configuration preset](https://github.com/moonrepo/moon-configs/tree/master/javascript/remix).

<project>/moon.yml

```yaml
# Inherit tasks from the `remix` preset
# https://github.com/moonrepo/moon-configs
tags: ['remix']
```

### ESLint integration [​](https://moonrepo.dev/docs/guides/examples/remix\#eslint-integration "Direct link to ESLint integration")

Remix does not provide a built-in linting abstraction, and instead provides a simple ESLint
configuration package,
[`@remix-run/eslint-config`](https://www.npmjs.com/package/@remix-run/eslint-config). For the rest
of this section, we're going to assume that a [global `lint` task](https://moonrepo.dev/docs/guides/examples/eslint) has been configured.

Begin be installing the `@remix-run/eslint-config` dependency in the application's `package.json`.
We can then enable this configuration by creating an `.eslintrc.js` file in the project root. Be
sure this file is listed in your `lint` task's inputs!

<project>/.eslintrc.js

```js
module.exports = {
  extends: ['@remix-run/eslint-config', '@remix-run/eslint-config/node'],

  // If using TypeScript
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.json',
    tsconfigRootDir: __dirname,
  },
};
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/remix\#typescript-integration "Direct link to TypeScript integration")

Remix ships with TypeScript support (when enabled during installation), but the `tsconfig.json` it
generates is _not_ setup for TypeScript project references, which we suggest using with a
[global `typecheck` task](https://moonrepo.dev/docs/guides/examples/typescript).

When using project references, we suggest the following `tsconfig.json`, which is a mix of Remix and
moon. Other compiler options, like `isolatedModules` and `esModuleInterop`, should be declared in a
shared configuration found in the workspace root (`tsconfig.projectOptions.json` in the example).

<project>/tsconfig.json

```json
{
  "extends": "../../tsconfig.projectOptions.json",
  "compilerOptions": {
    "baseUrl": ".",
    "emitDeclarationOnly": false,
    "jsx": "react-jsx",
    "resolveJsonModule": true,
    "moduleResolution": "node",
    "noEmit": true,
    "paths": {
      "~/*": ["./app/*"]
    }
  },
  "include": [".eslintrc.js", "remix.env.d.ts", "**/*"],
  "exclude": [".cache", "build", "public"]
}
```

## Configuration [​](https://moonrepo.dev/docs/guides/examples/remix\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/remix\#root-level "Direct link to Root-level")

We suggest _against_ root-level configuration, as Remix should be installed per-project, and the
`remix` command expects the configuration to live relative to the project root.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/remix\#project-level "Direct link to Project-level")

When creating a new Remix project, a
[`remix.config.js`](https://remix.run/docs/en/v1/api/conventions) is created, and _must_ exist in
the project root. This allows each project to configure Remix for their needs.

<project>/remix.config.js

```js
module.exports = {
  appDirectory: 'app',
};
```

- [Setup](https://moonrepo.dev/docs/guides/examples/remix#setup)
  - [ESLint integration](https://moonrepo.dev/docs/guides/examples/remix#eslint-integration)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/remix#typescript-integration)
- [Configuration](https://moonrepo.dev/docs/guides/examples/remix#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/remix#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/remix#project-level)