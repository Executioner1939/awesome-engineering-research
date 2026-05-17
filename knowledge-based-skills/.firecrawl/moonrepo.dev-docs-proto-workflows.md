[Skip to main content](https://moonrepo.dev/docs/proto/workflows#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

With proto, we provide multiple workflows for everyday use for you to choose from. They can be used
individually, or together, it's up to you!

## Shims [​](https://moonrepo.dev/docs/proto/workflows\#shims "Direct link to Shims")

proto is primarily powered by the industry standard concept of shims. For each tool installed in
proto, a shim file will exist at `~/.proto/shims` for the primary executable, and some secondary
executables. Shims _are not_ symlinks to the tool's binary, but are thin wrappers around
[`proto run`](https://moonrepo.dev/docs/proto/commands/run), enabling [runtime version detection](https://moonrepo.dev/docs/proto/detection) on every
invocation! For example, these are equivalent:

```shell
$ proto run node -- --version
20.0.0

$ node --version
20.0.0

$ which node
~/.proto/shims/node
```

### Setup [​](https://moonrepo.dev/docs/proto/workflows\#setup "Direct link to Setup")

To make use of shims, prepend the `~/.proto/shims` directory to `PATH` in your shell profile. This
_must come before_ the [bin directory](https://moonrepo.dev/docs/proto/workflows#binary-linking) if using both.

If you're using or plan to use [shell activation](https://moonrepo.dev/docs/proto/workflows#shell-activation), the `PATH` configuration
happens automatically, but shell activation will only work if the `proto` command is accessible,
which requires `~/.proto/bin` to be in your `PATH`.

## Binary linking [​](https://moonrepo.dev/docs/proto/workflows\#binary-linking "Direct link to Binary linking")

Alternatively, we also support a non-shim based approach, which creates symlinks to a versioned
tool's primary and secondary executables. For each tool installed in proto, a symlink will exist at
`~/.proto/bin`.

```shell
$ node --version
23.1.0

$ which node
~/.proto/bin/node -> ~/.proto/tools/node/23.1.0/bin/node
```

When a tool is installed into proto, we symlink many binaries based on all the versions that are
installed in the toolchain. The primary binary will always point to the highest installed version,
while we also create binaries for the highest major, and highest major + minor combinations. For
example:

- `~/.proto/bin/node` \- Points to the highest version.
- `~/.proto/bin/node-<major>` \- Points to the highest version within that major range (`~major`). Is
created for each separate major version, for example: `node-20`, `node-22`.
- `~/.proto/bin/node-<major>.<minor>` \- Points to the highest version within that major + minor
range (`~major.minor`). Is created for each separate major + minor version, for example:
`node-20.1`, `node-22.4`.
- `~/.proto/bin/node-canary` \- Points to a canary install, if it exists.

```shell
$ node-22 --version
22.5.1

$ which node-22
~/.proto/bin/node-22 -> ~/.proto/tools/node/22.5.1/bin/node
```

info

Not all tools support symlinking a binary, as not all files are executable. For example, most
Node.js package managers currently do not support this, as JavaScript files are not executable
(especially on Windows). Shims are required for these tools.

### Setup [​](https://moonrepo.dev/docs/proto/workflows\#setup-1 "Direct link to Setup")

To make use of bins, prepend the `~/.proto/bin` directory to `PATH` in your shell profile. This
_must come after_ the [shim directory](https://moonrepo.dev/docs/proto/workflows#shims) if using shims.

If you're using or plan to use [shell activation](https://moonrepo.dev/docs/proto/workflows#shell-activation), the `PATH` configuration
happens automatically, but shell activation will only work if the `proto` command is accessible,
which requires `~/.proto/bin` to be in your `PATH`.

warning

This directory must always exist in `PATH`, as the official proto binaries `~/.proto/bin/proto` and
`~/.proto/bin/proto-shim` are located here. If you move those binaries to another location, you can
omit `~/.proto/bin` from `PATH` if you like.

## Shell activationv0.38.0 [​](https://moonrepo.dev/docs/proto/workflows\#shell-activation "Direct link to shell-activation")

Our last workflow is what we call shell activation (or shell hooks), and it's where the proto
environment is setup/reset every time you change directories. If you're coming from another version
manager, you may be familiar with this kind of workflow.

So how does this work exactly? In your shell profile, you'll evaluate a call to
[`proto activate <shell>`](https://moonrepo.dev/docs/proto/commands/activate), which generates a bunch of shell specific syntax
that registers a hook for "run this code when the current directory or prompt line changes". Once
this hook is registered and you run `cd` (for example), proto will...

- Load all `.prototools` files
- Extract tools with a [configured version](https://moonrepo.dev/docs/proto/config#pinning-versions)
- For each tool:
  - Load associated WASM plugin
  - Export environment variables based on [`[env]`](https://moonrepo.dev/docs/proto/config#env) and
    [`[tools.*.env]`](https://moonrepo.dev/docs/proto/config#toolsenv)
  - Prepend `PATH` with tool-specific directories (like local and global executables) for the
    detected version

```shell
$ cd /some/path && node --version
20.0.0

$ cd /another/path && node --version
18.0.0
```

### Setup [​](https://moonrepo.dev/docs/proto/workflows\#setup-2 "Direct link to Setup")

View the [`proto activate`](https://moonrepo.dev/docs/proto/commands/activate#setup) documentation for information on how to setup
your shell profile for this workflow.

## Comparison [​](https://moonrepo.dev/docs/proto/workflows\#comparison "Direct link to Comparison")

The workflows above may come across as information overload, so we've provided the following
comparison table outlining the features each workflow supports.

|  | Shims | Bins | Activate |
| --- | --- | --- | --- |
| Runtime version detection | 🟢 | 🔴 | 🟠 only when the hook triggers |
| Supports multiple versions | 🟢 | 🟢 | 🟢 |
| Fixed to a single version | 🟠 with arg or env var | 🟢 | 🟠 if not using shims |
| Includes all tool executables | 🔴 | 🔴 | 🟢 |
| Includes tool globals/packages | 🔴 | 🔴 | 🟢 |
| Exports environment variables | 🔴 | 🔴 | 🟢 |
| Prepends `PATH` | 🔴 | 🔴 | 🟢 |
| Can pin proto's version | 🔴 | 🔴 | 🟢 |

- [Shims](https://moonrepo.dev/docs/proto/workflows#shims)
  - [Setup](https://moonrepo.dev/docs/proto/workflows#setup)
- [Binary linking](https://moonrepo.dev/docs/proto/workflows#binary-linking)
  - [Setup](https://moonrepo.dev/docs/proto/workflows#setup-1)
- [Shell activation](https://moonrepo.dev/docs/proto/workflows#shell-activation)
  - [Setup](https://moonrepo.dev/docs/proto/workflows#setup-2)
- [Comparison](https://moonrepo.dev/docs/proto/workflows#comparison)