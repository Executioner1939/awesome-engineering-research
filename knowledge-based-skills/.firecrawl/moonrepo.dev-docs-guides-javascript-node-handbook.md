[Skip to main content](https://moonrepo.dev/docs/guides/javascript/node-handbook#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Utilizing JavaScript (and TypeScript) in a monorepo can be a daunting task, especially when using
Node.js, as there are many ways to structure your code and to configure your tools. With this
handbook, we'll help guide you through this process.

info

This guide is a living document and will continue to be updated over time!

## moon setup [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#moon-setup "Direct link to moon setup")

For this part of the handbook, we'll be focusing on [moon](https://moonrepo.dev/moon), our task runner. To start,
languages in moon act like plugins, where their functionality and support _is not_ enabled unless
explicitly configured. We follow this approach to avoid unnecessary overhead.

### Enabling the language [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#enabling-the-language "Direct link to Enabling the language")

To enable JavaScript support via Node.js, define the [`node`](https://moonrepo.dev/docs/config/toolchain#node) setting
in [`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain), even if an empty object. The
[`javascript`](https://moonrepo.dev/docs/config/toolchain#javascript) toolchain must also be enabled, and configured to
use Bun as the package manager.

.moon/toolchains.yml

```yaml
# Enable JavaScript
javascript:
  packageManager: 'pnpm'

# Enable Node.js and pnpm
node: {}
pnpm: {}
```

Or by pinning a `node` version in [`.prototools`](https://moonrepo.dev/docs/proto/config) in the workspace root.

.prototools

```toml
node = "24.0.0"
pnpm = "7.29.0"
```

This will enable the Node.js toolchain and provide the following automations around its ecosystem:

- Node modules will automatically be installed if dependencies in `package.json` have changed, or
the lockfile has changed, since the last time a task has ran.
  - We'll also take `package.json` workspaces into account and install modules in the correct
    location; either the workspace root, in a project, or both.
- Relationships between projects will automatically be discovered based on `dependencies`,
`devDependencies`, and `peerDependencies` in `package.json`.
  - The versions of these packages will also be automatically synced when changed.
- Tasks can be [automatically inferred](https://moonrepo.dev/docs/config/toolchain#infertasksfromscripts) from
`package.json` scripts.
- And much more!

### Utilizing the toolchain [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#utilizing-the-toolchain "Direct link to Utilizing the toolchain")

When a language is enabled, moon by default will assume that the language's binary is available
within the current environment (typically on `PATH`). This has the downside of requiring all
developers and machines to manually install the correct version of the language, _and to stay in_
_sync_.

Instead, you can utilize [moon's toolchain](https://moonrepo.dev/docs/concepts/toolchain), which will download and
install the language in the background, and ensure every task is executed using the exact version
across all machines.

Enabling the toolchain is as simple as defining the [`node.version`](https://moonrepo.dev/docs/config/toolchain#version)
setting.

.moon/toolchains.yml

```yaml
# Enable Node.js toolchain with an explicit version
node:
  version: '18.0.0'
```

> Versions can also be defined with [`.prototools`](https://moonrepo.dev/docs/proto/config).

### Using `package.json` scripts [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#using-packagejson-scripts "Direct link to using-packagejson-scripts")

If you're looking to prototype moon, or reduce the migration effort to moon tasks, you can configure
moon to inherit `package.json` scripts, and internally convert them to moon tasks. This can be
achieved with the [`javascript.inferTasksFromScripts`](https://moonrepo.dev/docs/config/toolchain#infertasksfromscripts)
setting.

.moon/toolchains.yml

```yaml
javascript:
  inferTasksFromScripts: true
```

Or you can run scripts through `npm run` (or `pnpm`, `yarn`) calls.

moon.yml

```yaml
tasks:
  build:
    command: 'npm run build'
```

## Repository structure [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#repository-structure "Direct link to Repository structure")

JavaScript monorepo's work best when projects are split into applications and packages, with each
project containing its own `package.json` and dependencies. A root `package.json` must also exist
that pieces all projects together through workspaces.

For small repositories, the following structure typically works well:

```text
/
├── .moon/
├── package.json
├── apps/
│   ├── client/
|   |   ├── ...
│   |   └── package.json
│   └── server/
|       ├── ...
│       └── package.json
└── packages/
    ├── components/
    |   ├── ...
    │   └── package.json
    ├── theme/
    |   ├── ...
    │   └── package.json
    └── utils/
        ├── ...
        └── package.json
```

For large repositories, grouping projects by team or department helps with ownership and
organization. With this structure, applications and libraries can be nested at any depth.

```text
/
├── .moon/
├── package.json
├── infra/
│   └── ...
├── internal/
│   └── ...
├── payments/
│   └── ...
└── shared/
    └── ...
```

### Applications [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#applications "Direct link to Applications")

Applications are runnable or executable, like an HTTP server, and are pieced together with packages
and its own encapsulated code. They represent the whole, while packages are the pieces. Applications
can import and depend on packages, but they _must not_ import and depend on other applications.

In moon, you can denote a project as an application using the [`layer`](https://moonrepo.dev/docs/config/project#layer)
setting in [`moon.*`](https://moonrepo.dev/docs/config/project).

moon.yml

```yaml
layer: 'application'
```

### Packages [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#packages "Direct link to Packages")

Packages (also known as a libraries) are self-contained reusable pieces of code, and are the
suggested pattern for [code sharing](https://moonrepo.dev/docs/guides/javascript/node-handbook#code-sharing). Packages can import and depend on other
packages, but they _must not_ import and depend on applications!

In moon, you can denote a project as a library using the [`layer`](https://moonrepo.dev/docs/config/project#layer)
setting in [`moon.*`](https://moonrepo.dev/docs/config/project).

moon.yml

```yaml
layer: 'library'
```

### Configuration [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#configuration "Direct link to Configuration")

Every tool that you'll utilize in a repository will have its own configuration file. This will be a
lot of config files, but regardless of what tool it is, where the config file should go will fall
into 1 of these categories:

- **Settings are inherited by all projects.**These are known as universal tools, and enforce code
consistency and quality across the entire repository. Their config file must exist in the
repository root, but may support overrides in each project.
  - Examples: Babel, [ESLint](https://moonrepo.dev/docs/guides/examples/eslint), [Prettier](https://moonrepo.dev/docs/guides/examples/prettier),
    [TypeScript](https://moonrepo.dev/docs/guides/examples/typescript)
- **Settings are unique per project.**These are developers tools that must be configured separately
for each project, as they'll have different concerns. Their config file must exist in each
project, but a shared configuration may exist as a base (for example, Jest presets).
  - Examples: [Jest](https://moonrepo.dev/docs/guides/examples/jest), [TypeScript](https://moonrepo.dev/docs/guides/examples/typescript) (with project
    references)
- **Settings are one-offs.**These are typically for applications or tools that require their own
config, but aren't prevalent throughout the entire repository.
  - Examples: [Astro](https://moonrepo.dev/docs/guides/examples/astro), [Next](https://moonrepo.dev/docs/guides/examples/next), [Nuxt](https://moonrepo.dev/docs/guides/examples/nuxt),
    [Remix](https://moonrepo.dev/docs/guides/examples/remix), Tailwind

## Dependency management [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#dependency-management "Direct link to Dependency management")

Dependencies, also known as node modules, are required by all projects, and are installed through a
package manager like npm, pnpm, or yarn. It doesn't matter which package manager you choose, but we
highly suggest choosing one that has proper workspaces support. If you're unfamiliar with
workspaces, they will:

- Resolve all `package.json`'s in a repository using glob patterns.
- Install dependencies from all `package.json`'s at once, in the required locations.
- Create symlinks of local packages in `node_modules` (to emulate an installed package).
- Deduplicate and hoist `node_modules` when applicable.

All of this functionality enables robust monorepo support, and can be enabled with the following:

- npm
- pnpm
- Yarn
- Yarn (classic)

package.json

```json
{
  // ...
  "workspaces": ["apps/*", "packages/*"]
}
```

.yarnrc.yml

```yaml
# ...
nodeLinker: 'node-modules'
```

- [Documentation](https://yarnpkg.com/features/workspaces)

package.json

```json
{
  // ...
  "workspaces": ["apps/*", "packages/*"]
}
```

- [Documentation](https://classic.yarnpkg.com/en/docs/workspaces)

package.json

```json
{
  // ...
  "workspaces": ["apps/*", "packages/*"]
}
```

- [Documentation](https://docs.npmjs.com/cli/v8/using-npm/workspaces)

pnpm-workspace.yaml

```yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

- [Documentation](https://pnpm.io/workspaces)

info

Package workspaces are not a requirement for monorepos, but they do solve an array of problems
around module resolution, avoiding duplicate packages in bundles, and general interoperability.
Proceed with caution for non-workspaces setups!

### Workspace commands [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#workspace-commands "Direct link to Workspace commands")

The following common commands can be used for adding, removing, or managing dependencies in a
workspace. View the package manager's official documentation for a thorough list of commands.

- npm
- pnpm
- Yarn
- Yarn (classic)

Install dependencies:

```shell
npm install
```

Add a package:

```shell
# At the root
npm install <dependency>

# In a project
npm install <dependency> --workspace <project>
```

Remove a package:

```shell
# At the root
npm install <dependency>

# In a project
npm install <dependency> --workspace <project>
```

Update packages:

```shell
npx npm-check-updates --interactive
```

Install dependencies:

```shell
pnpm install
```

Add a package:

```shell
# At the root
pnpm add <dependency>

# In a project
pnpm add <dependency> --filter <project>
```

Remove a package:

```shell
# At the root
pnpm remove <dependency>

# In a project
pnpm remove <dependency> --filter <project>
```

Update packages:

```shell
pnpm update -i -r --latest
```

Install dependencies:

```shell
yarn install
```

Add a package:

```shell
# At the root
yarn add <dependency>

# In a project
yarn workspace <project> add <dependency>
```

Remove a package:

```shell
# At the root
yarn remove <dependency>

# In a project
yarn workspace <project> remove <dependency>
```

Update packages:

```shell
yarn upgrade-interactive
```

Install dependencies:

```shell
yarn install
```

Add a package:

```shell
# At the root
yarn add <dependency> -w

# In a project
yarn workspace <project> add <dependency>
```

Remove a package:

```shell
# At the root
yarn remove <dependency> -w

# In a project
yarn workspace <project> remove <dependency>
```

Update packages:

```shell
yarn upgrade-interactive --latest
```

### Developer tools at the root [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#developer-tools-at-the-root "Direct link to Developer tools at the root")

While not a strict guideline to follow, we've found that installing universal developer tool related
dependencies (Babel, ESLint, Jest, TypeScript, etc) in the root `package.json` as `devDependencies`
to be a good pattern for consistency, quality, and the health of the repository. It provides the
following benefits:

- It ensures all projects are utilizing the same version (and sometimes configuration) of a tool.
- It allows the tool to easily be upgraded. Upgrade once, applied everywhere.
- It avoids conflicting or outdated versions of the same package.

With that being said, this _does not_ include development dependencies that are unique to a project!

### Product libraries in a project [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#product-libraries-in-a-project "Direct link to Product libraries in a project")

Product, application, and or framework specific packages should be installed as production
`dependencies` in a project's `package.json`. We've found this pattern to work well for the
following reasons:

- Application dependencies are pinned per project, avoiding accidental regressions.
- Applications can upgrade their dependencies and avoid breaking neighbor applications.

## Code sharing [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#code-sharing "Direct link to Code sharing")

One of the primary reasons to use a monorepo is to easily share code between projects. When code is
co-located within the same repository, it avoids the overhead of the "build -> version -> publish to
registry -> upgrade in consumer" workflow (when the code is located in an external repository).

Co-locating code also provides the benefit of fast iteration, fast adoption, and easier migration
(when making breaking changes for example).

With [package workspaces](https://moonrepo.dev/docs/guides/javascript/node-handbook#dependency-management), code sharing is a breeze. As mentioned above,
every project that contains a `package.json` that is part of the workspace, will be symlinked into
`node_modules`. Because of this, these packages can easily be imported using their `package.json`
name.

```ts
// Imports from /packages/utils/package.json
import utils from '@company/utils';
```

### Depending on packages [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#depending-on-packages "Direct link to Depending on packages")

Because packages are symlinked into `node_modules`, we can depend on them as if they were normal npm
packages, but with 1 key difference. Since these packages aren't published, they do not have a
version to reference, and instead, we can use the special `workspace:^` version (yarn and pnpm only,
use `*` for npm).

```json
{
  "name": "@company/consumer",
  "dependencies": {
    "@company/provider": "workspace:^"
  }
}
```

The `workspace:` version basically means "use the package found in the current workspace". The `:^`
determines the version range to _substitute with when publishing_. For example, the `workspace:^`
above would be replaced with version of `@company/provider` as `^<version>` when the
`@company/consumer` package is published.

There's also `workspace:~` and `workspace:*` which substitutes to `~<version>` and `<version>`
respectively. We suggest using `:^` so that version ranges can be deduped.

### Types of packages [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#types-of-packages "Direct link to Types of packages")

When sharing packages in a monorepo, there's typically 3 different kinds of packages:

#### Local only [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#local-only "Direct link to Local only")

A local only package is just that, it's only available locally to the repository and _is not_
published to a registry, and _is not_ available to external repositories. For teams and companies
that utilize a single repository, this will be the most common type of package.

A benefit of local packages is that they do not require a build step, as source files can be
imported directly ( [when configured correctly](https://moonrepo.dev/docs/guides/javascript/node-handbook#bundler-integration)). This avoids a lot of
`package.json` overhead, especially in regards to `exports`, `imports`, and other import patterns.

#### Internally published [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#internally-published "Direct link to Internally published")

An internal package is published to a private registry, and _is not_ available to the public.
Published packages are far more strict than local packages, as the `package.json` structure plays a
much larger role for downstream consumers, as it dictates how files are imported, where they can be
found, what type of formats are supported (CJS, ESM), so on and so forth.

Published packages require a build step, for both source code and TypeScript types (when
applicable). We suggest using [esbuild](https://esbuild.github.io/) or
[Packemon](https://moonrepo.dev/docs/guides/examples/packemon) to handle this entire flow. With that being said, local projects
can still [import their source files](https://moonrepo.dev/docs/guides/javascript/node-handbook#bundler-integration).

#### Externally published [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#externally-published "Direct link to Externally published")

An external package is structured similarly to an internal package, but instead of publishing to a
private registry, it's published to the npm public registry.

External packages are primarily for open source projects, and require the repository to also be
public.

### Bundler integration [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#bundler-integration "Direct link to Bundler integration")

Co-locating packages is great, but how do you import and use them effectively? The easiest solution
is to configure resolver aliases within your bundler (Webpack, Vite, etc). By doing so, you enable
the following functionality:

- Avoids having to build (and rebuild) the package everytime its code changes.
- Enables file system watching of the package, not just the application.
- Allows for hot module reloading (HMR) to work.
- Package code is transpiled and bundled alongside application code.

- Vite
- Webpack

vite.config.ts

```ts
import path from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  // ...
  resolve: {
    alias: {
      '@company/utils': path.join(__dirname, '../packages/utils/src'),
    },
  },
});
```

webpack.config.js

```ts
const path = require('path');

module.exports = {
  // ...
  resolve: {
    alias: {
      '@company/utils': path.join(__dirname, '../packages/utils/src'),
    },
  },
};
```

info

When configuring aliases, we suggest using the `package.json` name as the alias! This ensures that
on the consuming side, you're using the package as if it's a normal node module, and avoids
deviating from the ecosystem.

### TypeScript integration [​](https://moonrepo.dev/docs/guides/javascript/node-handbook\#typescript-integration "Direct link to TypeScript integration")

We suggest using TypeScript project references. Luckily, we have an
[in-depth guide on how to properly and efficiently integrate them](https://moonrepo.dev/docs/guides/javascript/typescript-project-refs)!

- [moon setup](https://moonrepo.dev/docs/guides/javascript/node-handbook#moon-setup)
  - [Enabling the language](https://moonrepo.dev/docs/guides/javascript/node-handbook#enabling-the-language)
  - [Utilizing the toolchain](https://moonrepo.dev/docs/guides/javascript/node-handbook#utilizing-the-toolchain)
  - [Using `package.json` scripts](https://moonrepo.dev/docs/guides/javascript/node-handbook#using-packagejson-scripts)
- [Repository structure](https://moonrepo.dev/docs/guides/javascript/node-handbook#repository-structure)
  - [Applications](https://moonrepo.dev/docs/guides/javascript/node-handbook#applications)
  - [Packages](https://moonrepo.dev/docs/guides/javascript/node-handbook#packages)
  - [Configuration](https://moonrepo.dev/docs/guides/javascript/node-handbook#configuration)
- [Dependency management](https://moonrepo.dev/docs/guides/javascript/node-handbook#dependency-management)
  - [Workspace commands](https://moonrepo.dev/docs/guides/javascript/node-handbook#workspace-commands)
  - [Developer tools at the root](https://moonrepo.dev/docs/guides/javascript/node-handbook#developer-tools-at-the-root)
  - [Product libraries in a project](https://moonrepo.dev/docs/guides/javascript/node-handbook#product-libraries-in-a-project)
- [Code sharing](https://moonrepo.dev/docs/guides/javascript/node-handbook#code-sharing)
  - [Depending on packages](https://moonrepo.dev/docs/guides/javascript/node-handbook#depending-on-packages)
  - [Types of packages](https://moonrepo.dev/docs/guides/javascript/node-handbook#types-of-packages)
    - [Local only](https://moonrepo.dev/docs/guides/javascript/node-handbook#local-only)
    - [Internally published](https://moonrepo.dev/docs/guides/javascript/node-handbook#internally-published)
    - [Externally published](https://moonrepo.dev/docs/guides/javascript/node-handbook#externally-published)
  - [Bundler integration](https://moonrepo.dev/docs/guides/javascript/node-handbook#bundler-integration)
  - [TypeScript integration](https://moonrepo.dev/docs/guides/javascript/node-handbook#typescript-integration)