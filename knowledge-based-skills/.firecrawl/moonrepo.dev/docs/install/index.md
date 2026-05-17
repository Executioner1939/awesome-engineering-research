[Skip to main content](https://moonrepo.dev/docs/install#__docusaurus_skipToContent_fallback)

BunDenoGoNode.jsPHPPythonRubyRust

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

2 min

The following guide can be used to install moon and integrate it into an existing repository (with
or without incremental adoption), or to a fresh repository.

## Installing [​](https://moonrepo.dev/docs/install\#installing "Direct link to Installing")

The entirety of moon is packaged and shipped as a single binary. It works on all major operating
systems, and does not require any external dependencies. For convenience, we provide the following
scripts to download and install moon.

### proto [​](https://moonrepo.dev/docs/install\#proto "Direct link to proto")

moon can be installed and managed in [proto's toolchain](https://moonrepo.dev/proto). This will install moon to
`~/.proto/tools/moon` and make the binary available at `~/.proto/bin`.

```shell
proto install moon
```

Furthermore, the version of moon can be pinned on a per-project basis using the
[`.prototools` config file](https://moonrepo.dev/docs/proto/config).

.prototools

```toml
moon = "2.0.0"
```

info

We suggest using proto to manage moon (and other tools), as it allows for multiple versions to be
installed and used. The other installation options only allow for a single version (typically the
last installed).

### Linux, macOS, WSL [​](https://moonrepo.dev/docs/install\#linux-macos-wsl "Direct link to Linux, macOS, WSL")

In a terminal that supports Bash, run:

```shell
bash <(curl -fsSL https://moonrepo.dev/install/moon.sh)
```

This will install moon to `~/.moon/bin`. You'll then need to set `PATH` manually in your shell
profile.

```shell
export PATH="$HOME/.moon/bin:$PATH"
```

### Windows [​](https://moonrepo.dev/docs/install\#windows "Direct link to Windows")

In Powershell or Windows Terminal, run:

```shell
irm https://moonrepo.dev/install/moon.ps1 | iex
```

This will install moon to `~\.moon\bin` and prepend to the `PATH` environment variable for the
current session. To persist across sessions, update `PATH` manually in your system environment
variables.

info

If you are using Git Bash on Windows, you can run the [Unix commands](https://moonrepo.dev/docs/install#linux-macos-wsl) above.

### npm [​](https://moonrepo.dev/docs/install\#npm "Direct link to npm")

moon is also packaged and shipped as a single binary through the
[`@moonrepo/cli`](https://www.npmjs.com/package/@moonrepo/cli) npm package. Begin by installing this
package at the root of the repository.

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn add --dev @moonrepo/cli
```

```shell
yarn add --dev @moonrepo/cli

# If using workspaces
yarn add --dev -W @moonrepo/cli
```

```shell
npm install --save-dev @moonrepo/cli
```

```shell
pnpm add --save-dev @moonrepo/cli

# If using workspaces
pnpm add --save-dev -w @moonrepo/cli
```

```shell
bun install --dev @moonrepo/cli
```

If you are installing with Bun, you'll need to add `@moonrepo/cli` as a
[trusted dependency](https://bun.sh/docs/install/lifecycle#trusteddependencies).

info

When a global `moon` binary is executed, and the `@moonrepo/cli` binary exists within the
repository, the npm package version will be executed instead. We do this because the npm package
denotes the exact version the repository is pinned it.

### Other [​](https://moonrepo.dev/docs/install\#other "Direct link to Other")

moon can also be downloaded and installed manually, by downloading an asset from
[https://github.com/moonrepo/moon/releases](https://github.com/moonrepo/moon/releases). Be sure to
rename the file after downloading, and apply the executable bit (`chmod +x`) on macOS and Linux.

## Upgrading [​](https://moonrepo.dev/docs/install\#upgrading "Direct link to Upgrading")

If using proto, moon can be upgraded using the following command:

```shell
proto install moon --pin
```

Otherwise, moon can be upgraded with the [`moon upgrade`](https://moonrepo.dev/docs/commands/upgrade) command. However, this
will only upgrade moon if it was installed in `~/.moon/bin`.

```shell
moon upgrade
```

Otherwise, you can re-run the installers above and it will download, install, and overwrite with the
latest version.

## Next steps [​](https://moonrepo.dev/docs/install\#next-steps "Direct link to Next steps")

[Setup workspace](https://moonrepo.dev/docs/setup-workspace)

- [Installing](https://moonrepo.dev/docs/install#installing)
  - [proto](https://moonrepo.dev/docs/install#proto)
  - [Linux, macOS, WSL](https://moonrepo.dev/docs/install#linux-macos-wsl)
  - [Windows](https://moonrepo.dev/docs/install#windows)
  - [npm](https://moonrepo.dev/docs/install#npm)
  - [Other](https://moonrepo.dev/docs/install#other)
- [Upgrading](https://moonrepo.dev/docs/install#upgrading)
- [Next steps](https://moonrepo.dev/docs/install#next-steps)