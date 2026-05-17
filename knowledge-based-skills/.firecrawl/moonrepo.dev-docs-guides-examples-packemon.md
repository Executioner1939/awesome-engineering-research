[Skip to main content](https://moonrepo.dev/docs/guides/examples/packemon#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [Packemon](https://packemon.dev/) into moon. Packemon
is a tool for properly building npm packages for distribution, it does this by providing the
following functionality:

- Compiles source code to popular formats: CJS, MJS, ESM, UMD, etc.
- Validates the `package.json` for incorrect fields or values.
- Generates `exports` mappings for `package.json` based on the define configuration.
- And many more [optimizations and features](https://packemon.dev/docs/features)!

Begin by installing `packemon` in your root. We suggest using the same version across the entire
repository.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn add --dev packemon
```

```shell
yarn add --dev packemon

# If using workspaces
yarn add --dev -W packemon
```

```shell
npm install --save-dev packemon
```

```shell
pnpm add --save-dev packemon

# If using workspaces
pnpm add --save-dev -w packemon
```

```shell
bun install --dev packemon
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/packemon\#setup "Direct link to Setup")

Since Packemon is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

tip

We suggest inheriting Packemon tasks from the
[official moon configuration preset](https://github.com/moonrepo/moon-configs/tree/master/javascript/packemon).

<project>/moon.yml

```yaml
# Inherit tasks from the `packemon` preset
# https://github.com/moonrepo/moon-configs
tags: ['packemon']

# Set the output formats
tasks:
  build:
    outputs:
      - 'cjs'
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/packemon\#typescript-integration "Direct link to TypeScript integration")

Packemon has built-in support for TypeScript, but to _not_ conflict with a
[typecheck task](https://moonrepo.dev/docs/guides/examples/typescript), a separate `tsconfig.json` file is required, which is named
`tsconfig.<format>.json`.

This config is necessary to _only_ compile source files, and to not include unwanted files in the
declaration output directory.

tsconfig.esm.json

```json
{
  "extends": "../../tsconfig.options.json",
  "compilerOptions": {
    "outDir": "esm",
    "rootDir": "src"
  },
  "include": ["src/**/*"],
  "references": []
}
```

### Build targets [​](https://moonrepo.dev/docs/guides/examples/packemon\#build-targets "Direct link to Build targets")

To configure the target platform(s) and format(s), you must define a
[`packemon` block](https://packemon.dev/docs/config) in the project's `package.json`. The chosen
formats must also be listed as `outputs` in the task.

package.json

```json
{
  "name": "package",
  // ...
  "packemon": {
    "format": "esm",
    "platform": "browser"
  }
}
```

- [Setup](https://moonrepo.dev/docs/guides/examples/packemon#setup)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/packemon#typescript-integration)
  - [Build targets](https://moonrepo.dev/docs/guides/examples/packemon#build-targets)