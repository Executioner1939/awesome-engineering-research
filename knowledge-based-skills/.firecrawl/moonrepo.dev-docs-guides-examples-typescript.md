[Skip to main content](https://moonrepo.dev/docs/guides/examples/typescript#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [TypeScript](https://www.typescriptlang.org/) into
moon. We'll be using [project references](https://moonrepo.dev/docs/guides/javascript/typescript-project-refs), as it ensures that
only affected projects are built, and not the entire repository.

Begin by installing `typescript` and any pre-configured tsconfig packages in your root. We suggest
using the same version across the entire repository.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn add --dev typescript tsconfig-moon
```

```shell
yarn add --dev typescript tsconfig-moon

# If using workspaces
yarn add --dev -W typescript tsconfig-moon
```

```shell
npm install --save-dev typescript tsconfig-moon
```

```shell
pnpm add --save-dev typescript tsconfig-moon

# If using workspaces
pnpm add --save-dev -w typescript tsconfig-moon
```

```shell
bun install --dev typescript tsconfig-moon
```

## Setup [​](https://moonrepo.dev/docs/guides/examples/typescript\#setup "Direct link to Setup")

Since typechecking is a universal workflow, add a `typecheck` task to
[`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks) with the following parameters.

.moon/tasks/typescript.yml

```yaml
tasks:
  typecheck:
    command:
      - 'tsc'
      # Use incremental builds with project references
      - '--build'
      # Always use pretty output
      - '--pretty'
      # Use verbose logging to see affected projects
      - '--verbose'
    inputs:
      # Source and test files
      - 'src/**/*'
      - 'tests/**/*'
      # Type declarations
      - 'types/**/*'
      # Project configs
      - 'tsconfig.json'
      - 'tsconfig.*.json'
      # Root configs (extended from only)
      - '/tsconfig.options.json'
    outputs:
      # Matches `compilerOptions.outDir`
      - 'lib'
```

Projects can extend this task and provide additional parameters if need be, for example.

<project>/moon.yml

```yaml
tasks:
  typecheck:
    args:
      # Force build every time
      - '--force'
```

## Configuration [​](https://moonrepo.dev/docs/guides/examples/typescript\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/typescript\#root-level "Direct link to Root-level")

Multiple root-level TypeScript configs are _required_, as we need to define compiler options that
are shared across the repository, and we need to house a list of all project references.

To start, let's create a `tsconfig.options.json` that will contain our compiler options. In our
example, we'll extend [tsconfig-moon](https://www.npmjs.com/package/tsconfig-moon) for convenience.
Specifically, the `tsconfig.workspaces.json` config, which enables ECMAScript modules, composite
mode, declaration emitting, and incremental builds.

tsconfig.options.json

```json
{
  "extends": "tsconfig-moon/tsconfig.projects.json",
  "compilerOptions": {
    // Your custom options
    "moduleResolution": "nodenext",
    "target": "es2022"
  }
}
```

We'll also need the standard `tsconfig.json` to house our project references. This is used by
editors and tooling for deep integrations.

tsconfig.json

```json
{
  "extends": "./tsconfig.options.json",
  "files": [],
  // All project references in the repo
  "references": []
}
```

> The [`typescript.rootConfigFileName`](https://moonrepo.dev/docs/config/toolchain#rootconfigfilename) setting can be
> used to change the root-level config name and the
> [`typescript.syncProjectReferences`](https://moonrepo.dev/docs/config/toolchain#syncprojectreferences) setting will
> automatically keep project references in sync!

### Project-level [​](https://moonrepo.dev/docs/guides/examples/typescript\#project-level "Direct link to Project-level")

Every project will require a `tsconfig.json`, as TypeScript itself requires it. The following
`tsconfig.json` will typecheck the entire project, including source and test files.

<project>/tsconfig.json

```json
{
  // Extend the root compiler options
  "extends": "../../tsconfig.options.json",
  "compilerOptions": {
    // Declarations are written here
    "outDir": "lib"
  },
  // Include files in the project
  "include": ["src/**/*", "tests/**/*"],
  // Depends on other projects
  "references": []
}
```

> The [`typescript.projectConfigFileName`](https://moonrepo.dev/docs/config/toolchain#projectconfigfilename) setting can
> be used to change the project-level config name.

### Sharing [​](https://moonrepo.dev/docs/guides/examples/typescript\#sharing "Direct link to Sharing")

To share configuration across projects, you have 3 options:

- Define settings in a [root-level config](https://moonrepo.dev/docs/guides/examples/typescript#root-level). This only applies to the parent repository.
- Create and publish an
[`tsconfig base`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html#tsconfig-bases)
npm package. This can be used in any repository.
- A combination of 1 and 2.

For options 2 and 3, if you're utilizing package workspaces, create a local package with the
following content.

packages/tsconfig-company/tsconfig.json

```json
{
  "compilerOptions": {
    // ...
    "lib": ["esnext"]
  }
}
```

Within another `tsconfig.json`, you can extend this package to inherit the settings.

tsconfig.json

```json
{
  "extends": "tsconfig-company/tsconfig.json"
}
```

## FAQ [​](https://moonrepo.dev/docs/guides/examples/typescript\#faq "Direct link to FAQ")

### How to preserve pretty output? [​](https://moonrepo.dev/docs/guides/examples/typescript\#how-to-preserve-pretty-output "Direct link to How to preserve pretty output?")

TypeScript supports a pretty format where it includes codeframes and color highlighting for
failures. However, when `tsc` is piped or the terminal is not a TTY, the pretty format is lost. To
preserve and always display the pretty format, be sure to pass the `--pretty` argument!

- [Setup](https://moonrepo.dev/docs/guides/examples/typescript#setup)
- [Configuration](https://moonrepo.dev/docs/guides/examples/typescript#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/typescript#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/typescript#project-level)
  - [Sharing](https://moonrepo.dev/docs/guides/examples/typescript#sharing)
- [FAQ](https://moonrepo.dev/docs/guides/examples/typescript#faq)
  - [How to preserve pretty output?](https://moonrepo.dev/docs/guides/examples/typescript#how-to-preserve-pretty-output)