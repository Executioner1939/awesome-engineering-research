[Skip to main content](https://moonrepo.dev/docs/guides/examples/nest#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

In this guide, you'll learn how to integrate [NestJS](https://nestjs.com/) into moon.

Begin by creating a new NestJS project in the root of an existing moon project (this should not be
created in the workspace root, unless a polyrepo).

```shell
npx @nestjs/cli@latest new nestjs-app --skip-git
```

> View the [official NestJS docs](https://docs.nestjs.com/first-steps) for a more in-depth guide to
> getting started!

## Setup [​](https://moonrepo.dev/docs/guides/examples/nest\#setup "Direct link to Setup")

Since NestJS is per-project, the associated moon tasks should be defined in each project's
[`moon.*`](https://moonrepo.dev/docs/config/project) file.

<project>/moon.yml

```yaml
layer: 'application'

fileGroups:
  app:
    - 'nest-cli.*'

tasks:
  dev:
    command: 'nest start --watch'
    preset: 'server'

  build:
    command: 'nest build'
    inputs:
      - '@group(app)'
      - '@group(sources)'
```

### TypeScript integration [​](https://moonrepo.dev/docs/guides/examples/nest\#typescript-integration "Direct link to TypeScript integration")

NestJS has [built-in support for TypeScript](https://nestjs.io/guide/typescript-configuration), so
there is no need for additional configuration to enable TypeScript support.

At this point we'll assume that a `tsconfig.json` has been created in the application, and
typechecking works. From here we suggest utilizing a [global `typecheck` task](https://moonrepo.dev/docs/guides/examples/typescript) for
consistency across all projects within the repository.

## Configuration [​](https://moonrepo.dev/docs/guides/examples/nest\#configuration "Direct link to Configuration")

### Root-level [​](https://moonrepo.dev/docs/guides/examples/nest\#root-level "Direct link to Root-level")

We suggest _against_ root-level configuration, as NestJS should be installed per-project, and the
`nest` command expects the configuration to live relative to the project root.

### Project-level [​](https://moonrepo.dev/docs/guides/examples/nest\#project-level "Direct link to Project-level")

When creating a new NestJS project, a [`nest-cli.json`](https://docs.nestjs.com/cli/monorepo) is
created, and _must_ exist in the project root. This allows each project to configure NestJS for
their needs.

<project>/nest-cli.json

```json
{
  "$schema": "https://json.schemastore.org/nest-cli",
  "collection": "@nestjs/schematics",
  "type": "application",
  "root": "./",
  "sourceRoot": "src",
  "compilerOptions": {
    "tsConfigPath": "tsconfig.build.json"
  }
}
```

- [Setup](https://moonrepo.dev/docs/guides/examples/nest#setup)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/examples/nest#typescript-integration)
- [Configuration](https://moonrepo.dev/docs/guides/examples/nest#configuration)
  - [Root-level](https://moonrepo.dev/docs/guides/examples/nest#root-level)
  - [Project-level](https://moonrepo.dev/docs/guides/examples/nest#project-level)