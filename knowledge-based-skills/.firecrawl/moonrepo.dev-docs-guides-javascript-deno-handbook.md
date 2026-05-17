[Skip to main content](https://moonrepo.dev/docs/guides/javascript/deno-handbook#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Utilizing Deno in a TypeScript based monorepo can be a non-trivial task. With this handbook, we'll
help guide you through this process.

info

This guide is a living document and will continue to be updated over time!

## moon setup [​](https://moonrepo.dev/docs/guides/javascript/deno-handbook\#moon-setup "Direct link to moon setup")

For this part of the handbook, we'll be focusing on [moon](https://moonrepo.dev/moon), our task runner. To start,
languages in moon act like plugins, where their functionality and support _is not_ enabled unless
explicitly configured. We follow this approach to avoid unnecessary overhead.

### Enabling the language [​](https://moonrepo.dev/docs/guides/javascript/deno-handbook\#enabling-the-language "Direct link to Enabling the language")

To enable TypeScript support via Deno, define the [`deno`](https://moonrepo.dev/docs/config/toolchain#deno) setting in
[`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain), even if an empty object. The
[`javascript`](https://moonrepo.dev/docs/config/toolchain#javascript) toolchain must also be enabled, and configured to
use Bun as the package manager.

.moon/toolchains.yml

```yaml
# Enable JavaScript
javascript:
  packageManager: 'deno'

# Enable Deno
deno: {}
```

Or by pinning a `deno` version in [`.prototools`](https://moonrepo.dev/docs/proto/config) in the workspace root.

.prototools

```toml
deno = "2.0.0"
```

This will enable the Deno toolchain and provide the following automations around its ecosystem:

- Automatic handling and caching of lockfiles (when the setting is enabled).
- Relationships between projects will automatically be discovered based on `imports`, `importMap`,
and `deps.ts` (currently experimental).
- And more to come!

## Coming soon! [​](https://moonrepo.dev/docs/guides/javascript/deno-handbook\#coming-soon "Direct link to Coming soon!")

The handbook is currently being written while we finalize our Deno integration support!

- [moon setup](https://moonrepo.dev/docs/guides/javascript/deno-handbook#moon-setup)
  - [Enabling the language](https://moonrepo.dev/docs/guides/javascript/deno-handbook#enabling-the-language)
- [Coming soon!](https://moonrepo.dev/docs/guides/javascript/deno-handbook#coming-soon)