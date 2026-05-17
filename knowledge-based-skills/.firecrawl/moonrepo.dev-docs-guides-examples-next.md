[Skip to main content](https://moonrepo.dev/docs/guides/examples/next#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Next.js](https://nextjs.org/) into moon.

Begin by creating a new Next.js project at a specified folder path (this should not be created in
the workspace root, unless a polyrepo).

```shell
cd apps && npx create-next-app <project> --typescript
```

> View the [official Next.js docs](https://nextjs.org/learn/basics/create-nextjs-app/setup) for a
> more in-depth guide to getting started!

## Setup [​](https://moonrepo.dev/docs/guides/examples/next\#setup "Direct link to Setup")

Since Next.js is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

tip

We suggest inheriting Next.js tasks from the
[official moon configuration preset](https://github.com/moonrepo/moon-configs/tree/master/javascript/next).

<project>/moon.yml

```yaml
# Inherit tasks from the `next` preset
# https://github.com/moonrepo/moon-configs
tags: ['next']
```

### ESLint integration [​](https://moonrepo.dev/docs/guides/examples/next\#eslint-integration "Direct link to ESLint integration")

Next.js has [built-in support for ESLint](https://nextjs.org/docs/basic-features/eslint), which is
great, but complicates things a bit. Because of this, you have two options for moving forward:

- Use a [global `lint` task](https://moonrepo.dev/docs/guides/examples/eslint) and bypass Next.js's solution (preferred).
- Use Next.js's solution only.

Regardless of which option is chosen, the following changes are applicable to all options and should
be made. Begin be installing the
[`eslint-config-next`](https://nextjs.org/docs/basic-features/eslint#eslint-config) dependency in
the application's `package.json`.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn workspace <project> add --dev eslint-config-next
```

```shell
yarn workspace <project> add --dev eslint-config-next
```

```shell
npm install --save-dev --workspace <project> eslint-config-next
```

```shell
pnpm add --save-dev --filter <project> eslint-config-next
```

```shell
bun install --dev eslint-config-next
```

Since the Next.js app is located within a subfolder, we'll need to tell the ESLint plugin where to
locate it. This can be achieved with a project-level `.eslintrc.js` file.

<project>/.eslintrc.js

```js
module.exports = {
  extends: 'next', // or 'next/core-web-vitals'
  settings: {
    next: {
      rootDir: __dirname,
    },
  },
};
```

With the basics now setup, choose the option that works best for you.

- Global lint
- Next.js lint

We encourage using the global `lint` task for consistency across all projects within the repository.
With this approach, the `eslint` command itself will be ran and the `next lint` command will be
ignored, but the `eslint-config-next` rules will still be used.

Additionally, we suggest disabling the linter during the build process, but is not a requirement. As
a potential alternative, add the `lint` task as a dependency for the `build` task.

<project>/next.config.js

```js
module.exports = {
  eslint: {
    ignoreDuringBuilds: true,
  },
};
```

If you'd prefer to use the `next lint` command, add it as a task to the project's
[`moon.*`](https://moonrepo.dev/docs/config/project).

<project>/moon.yml

```yaml
tasks:
  lint:
    command: 'next lint'
    inputs:
      - '@group(next)'
```

Furthermore, if a global `lint` task exists, be sure to exclude it from being inherited.

<project>/moon.yml

```yaml
workspace:
  inheritedTasks:
    exclude: ['lint']
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/next\#typescript-integration "Direct link to TypeScript integration")

Next.js also has
[built-in support for TypeScript](https://nextjs.org/docs/basic-features/typescript), but has
similar caveats to the [ESLint integration](https://moonrepo.dev/docs/guides/examples/next#eslint-integration). TypeScript itself is a bit
involved, so we suggest reading the official Next.js documentation before continuing.

At this point we'll assume that a `tsconfig.json` has been created in the application, and
typechecking works. From here we suggest utilizing a [global `typecheck` task](https://moonrepo.dev/docs/guides/examples/typescript) for
consistency across all projects within the repository.

Additionally, we suggest disabling the typechecker during the build process, but is not a
requirement. As a potential alternative, add the `typecheck` task as a dependency for the `build`
task.

<project>/next.config.js

```js
module.exports = {
  typescript: {
    ignoreBuildErrors: true,
  },
};
```

## Configuration [​](https://moonrepo.dev/docs/guides/examples/next\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/next\#root-level "Direct link to Root-level")

We suggest _against_ root-level configuration, as Next.js should be installed per-project, and the
`next` command expects the configuration to live relative to the project root.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/next\#project-level "Direct link to Project-level")

When creating a new Next.js project, a
[`next.config.<js|mjs>`](https://nextjs.org/docs/api-reference/next.config.js/introduction) is
created, and _must_ exist in the project root. This allows each project to configure Next.js for
their needs.

<project>/next.config.js

```js
module.exports = {
  compress: true,
};
```

- [Setup](https://moonrepo.dev/docs/guides/examples/next#setup)
  - [ESLint integration](https://moonrepo.dev/docs/guides/examples/next#eslint-integration)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/next#typescript-integration)
- [Configuration](https://moonrepo.dev/docs/guides/examples/next#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/next#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/next#project-level)