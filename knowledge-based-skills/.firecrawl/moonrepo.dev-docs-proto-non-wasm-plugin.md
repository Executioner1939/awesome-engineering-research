[Skip to main content](https://moonrepo.dev/docs/proto/non-wasm-plugin#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The non-WASM plugin is by design, very simple. It's a JSON, TOML, or YAML file that describes a
schema for the tool, how it should be installed, and how it should be invoked. Since this is a
static configuration file, it does not support any logic or complex behavior, and is merely for
simple and common use cases, like CLIs.

info

JSON and YAML support was added in proto v0.42.

## Create a plugin [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#create-a-plugin "Direct link to Create a plugin")

Let's start by creating a new plugin, and defining the `name` and `type` fields. The type can either
be `language`, `dependency-manager`, `package-manager`, or `cli`. For this example, we'll create a
plugin for our fake product called Protostar, a CLI tool.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "name": "Protostar",
  "type": "cli"
}
```

protostar.toml

```toml
name = "Protostar"
type = "cli"
```

protostar.yaml

```yaml
name: 'Protostar'
type: 'cli'
```

### Platform variations [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#platform-variations "Direct link to Platform variations")

Native tools are often platform specific, and proto supports this by allowing you to define
variations based on operating system using the `[platform]` section. For non-native tools, this
section can typically be skipped.

This section requires a mapping of Rust
[`OS` strings](https://doc.rust-lang.org/std/env/consts/constant.OS.html) to platform settings. The
following settings are available:

- `archs` \- A list of architectures supported for this platform. If not provided, supports all
archs.
- `archive-prefix` \- If the tool is distributed as an archive (zip, tar, etc), this is the name of
the direct folder within the archive that contains the tool, and will be removed when unpacking
the archive. If there is no prefix folder within the archive, this setting can be omitted.
- `exes-dir` \- A relative path to a directory that contains pre-installed executables.
- `exe-path` \- The path to the main executable binary within the archive (without the prefix). If
the tool is distributed as a single binary, this setting can be typically omitted.
- `checksum-file` \- Name of the checksum file to verify the downloaded file with. If the tool does
not support checksum verification, this setting can be omitted.
- `download-file` (required) - Name of the file to download.
[Learn more about downloading](https://moonrepo.dev/docs/proto/non-wasm-plugin#downloading-and-installing).

- JSON
- TOML
- YAML

protostar.json

```json
{
  "platform": {
    "linux": {
      "archivePrefix": "protostar-linux",
      "exePath": "bin/protostar",
      "checksumFile": "protostar-{arch}-unknown-linux-{libc}.sha256",
      "downloadFile": "protostar-{arch}-unknown-linux-{libc}.tar.gz"
    },
    "macos": {
      "archivePrefix": "protostar-macos",
      "exePath": "bin/protostar",
      "checksumFile": "protostar-{arch}-apple-darwin.sha256",
      "downloadFile": "protostar-{arch}-apple-darwin.tar.xz"
    },
    "windows": {
      "archivePrefix": "protostar-windows",
      "exePath": "bin/protostar.exe",
      "checksumFile": "protostar-{arch}-pc-windows-msvc.sha256",
      "downloadFile": "protostar-{arch}-pc-windows-msvc.zip"
    }
  }
}
```

protostar.toml

```toml
[platform.linux]
archive-prefix = "protostar-linux"
exe-path = "bin/protostar"
checksum-file = "protostar-{arch}-unknown-linux-{libc}.sha256"
download-file = "protostar-{arch}-unknown-linux-{libc}.tar.gz"

[platform.macos]
archive-prefix = "protostar-macos"
exe-path = "bin/protostar"
checksum-file = "protostar-{arch}-apple-darwin.sha256"
download-file = "protostar-{arch}-apple-darwin.tar.xz"

[platform.windows]
archive-prefix = "protostar-windows"
exe-path = "bin/protostar.exe"
checksum-file = "protostar-{arch}-pc-windows-msvc.sha256"
download-file = "protostar-{arch}-pc-windows-msvc.zip"
```

protostar.yaml

```yaml
platform:
  linux:
    archivePrefix: 'protostar-linux'
    exePath: 'bin/protostar'
    checksumFile: 'protostar-{arch}-unknown-linux-{libc}.sha256'
    downloadFile: 'protostar-{arch}-unknown-linux-{libc}.tar.gz'
  macos:
    archivePrefix: 'protostar-macos'
    exePath: 'bin/protostar'
    checksumFile: 'protostar-{arch}-apple-darwin.sha256'
    downloadFile: 'protostar-{arch}-apple-darwin.tar.xz'
  windows:
    archivePrefix: 'protostar-windows'
    exePath: 'bin/protostar.exe'
    checksumFile: 'protostar-{arch}-pc-windows-msvc.sha256'
    downloadFile: 'protostar-{arch}-pc-windows-msvc.zip'
```

You may have noticed tokens above, like `{arch}`. These are special tokens that are replaced with a
dynamic value at runtime, based on the current host machine executing the code. The following tokens
are available:

- `{version}` \- The currently resolved version, as a fully-qualified semantic or calendar version.
- `{versionMajor}` / `{versionYear}` \- Only the major version. v0.41.4
- `{versionMinor}` / `{versionMonth}` \- Only the minor version. v0.45.2
- `{versionPatch}` / `{versionDay}` \- Only the patch version. v0.45.2
- `{versionPrerelease}` \- The prerelease identifier, if applicable. Returns an empty string
otherwise. v0.41.4
- `{versionBuild}` \- The build identifier, if applicable. Returns an empty string otherwise.v0.41.4
- `{arch}` \- The architecture of the host machine, like `x86_64`. These values map to Rust's
[`ARCH` constant](https://doc.rust-lang.org/std/env/consts/constant.ARCH.html), but can be
customized with [`install.arch`](https://moonrepo.dev/docs/proto/non-wasm-plugin#downloading-and-installing).
- `{os}` \- The operating system of the host machine, like `windows`. These values map to Rust's
[`OS` constant](https://doc.rust-lang.org/std/env/consts/constant.OS.html).
- `{libc}` \- For Linux machines, this is the current libc implementation, either `gnu` or `musl`.v0.31.2

### Downloading and installing [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#downloading-and-installing "Direct link to Downloading and installing")

A non-WASM plugin _only_ supports downloading pre-built tools, typically as an archive, and does
_not_ support building from source. The `[install]` section can be used to configure how the tool
should be downloaded and installed into the toolchain. The following settings are available:

- `arch` \- A mapping of Rust
[`ARCH` strings](https://doc.rust-lang.org/std/env/consts/constant.ARCH.html) to custom values for
the `{arch}` token. This is useful if the tool has different terminology.
- `libc` \- A mapping of custom values for the `{libc}` token.
- `checksum-url` \- A secure URL to download the checksum file for verification. If the tool does not
support checksum verification, this setting can be omitted.
- `checksum-url-canary` \- A URL for canary releases.
- `checksum-public-key` \- Public key used for verifying checksums. Only used for `.minisig` files.
- `download-url` (required) - A secure URL to download the tool/archive.
- `download-url-canary` \- A URL for canary releases.
- `primary` \- Configures the primary executable.
- `secondary` \- Configures secondary executables.

The URL settings support `{checksum_file}` and `{download_file}` tokens, which will be replaced with
the values from the `[platform]` section.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "install": {
    "checksumUrl": "https://github.com/moonrepo/protostar/releases/download/v{version}/{checksum_file}",
    "downloadUrl": "https://github.com/moonrepo/protostar/releases/download/v{version}/{download_file}",
    "arch": {
      "aarch64": "arm64",
      "x86_64": "x64"
    }
  }
}
```

protostar.toml

```toml
[install]
checksum-url = "https://github.com/moonrepo/protostar/releases/download/v{version}/{checksum_file}"
download-url = "https://github.com/moonrepo/protostar/releases/download/v{version}/{download_file}"

[install.arch]
aarch64 = "arm64"
x86_64 = "x64"
```

protostar.yaml

```yaml
install:
  checksumUrl: 'https://github.com/moonrepo/protostar/releases/download/v{version}/{checksum_file}'
  downloadUrl: 'https://github.com/moonrepo/protostar/releases/download/v{version}/{download_file}'
  arch:
    aarch64: 'arm64'
    x86_64: 'x64'
```

#### Executables [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#executables "Direct link to Executables")

The available executables (bins and shims) can be customized with the `[install.exes]` section,
which is required. This setting requires a map, where the key is the executable file name, and the
value is an object of the following options:

- `exe-path` \- The file to execute, relative from the tool directory. On Windows, the `.exe`
extension will automatically be appended. If you need more control over platform variance, use
`[platform.*.exe-path]` instead.
- `no-bin` \- Do not symlink a binary in `~/.proto/bin`.
- `no-shim`\- Do not generate a shim in `~/.proto/shims`.
- `parent-exe-name` \- Name of a parent executable required to execute the executable path. For
example, `node` is required for `.js` files.
- `primary` \- Is the main executable in the tool. There can only be 1 primary!v0.42.0
- `shim-before-args` \- Custom args to prepend to user-provided args within the generated shim.
- `shim-after-args` \- Custom args to append to user-provided args within the generated shim.
- `shim-env-vars` \- Custom environment variables to set when executing the shim.

This field supports both the required primary executable, and optional secondary executables. The
primary executable must be marked with `primary = true`.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "install": {
    "exes": {
      "protostar": {
        "exePath": "bins/protostar",
        "primary": true,
        "shimBeforeArgs": [\
          "--verbose"\
        ]
      },
      "protostar-debug": {
        "exePath": "bins/protostar-debug",
        "noShim": true
      }
    }
  }
}
```

protostar.toml

```toml
[install.exes.protostar]
exe-path = "bins/protostar"
primary = true
shim-before-args = [ "--verbose" ]

[install.exes.protostar-debug]
exe-path = "bins/protostar-debug"
no-shim = true
```

protostar.yaml

```yaml
install:
  exes:
    protostar:
      exePath: 'bins/protostar'
      primary: true
      shimBeforeArgs:
        - '--verbose'
    protostar-debug:
      exePath: 'bins/protostar-debug'
      noShim: true
```

#### Global packages [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#global-packages "Direct link to Global packages")

The `[packages]` sections can be configured that provides information about where global packages
are stored.

- `globals-lookup-dirs` \- A list of directories where global binaries are stored. This setting
supports interpolating environment variables via the syntax `$ENV_VAR`.
- `globals-prefix` \- A string that all package names are prefixed with. For example, Cargo/Rust
binaries are prefixed with `cargo-`.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "packages": {
    "globalsLookupDirs": [\
      "$PROTOSTAR_HOME/bin",\
      "$HOME/.protostar/bin"\
    ]
  }
}
```

protostar.toml

```toml
[packages]
globals-lookup-dirs = [ "$PROTOSTAR_HOME/bin", "$HOME/.protostar/bin" ]
```

protostar.yaml

```yaml
packages:
  globalsLookupDirs:
    - '$PROTOSTAR_HOME/bin'
    - '$HOME/.protostar/bin'
```

### Resolving versions [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#resolving-versions "Direct link to Resolving versions")

Now that the tool can be downloaded and installed, we must configure how to resolve available
versions. Resolving is configured through the `[resolve]` section, which supports 2 patterns to
resolve with: Git tags or a JSON manifest.

#### Git tags [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#git-tags "Direct link to Git tags")

To resolve a list of available versions using Git tags, the following settings are available:

- `git-url` (required) - The remote URL to fetch tags from.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "resolve": {
    "gitUrl": "https://github.com/moonrepo/protostar"
  }
}
```

protostar.toml

```toml
[resolve]
git-url = "https://github.com/moonrepo/protostar"
```

protostar.yaml

```yaml
resolve:
  gitUrl: 'https://github.com/moonrepo/protostar'
```

#### JSON manifest [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#json-manifest "Direct link to JSON manifest")

To resolve a list of available versions using a JSON manifest, the following settings are available:

- `manifest-url` (required) - A URL that returns a JSON response of all versions. This response
_must be_ an array of strings, or an array of objects.
- `manifest-version-key` \- If the response is an array of objects, this is the key to extract the
version from. If the response is an array of strings, this setting can be omitted. Defaults to
`version`.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "resolve": {
    "manifestUrl": "https://someregistry.com/protostar/versions.json",
    "manifestVersionKey": "latest_version"
  }
}
```

protostar.toml

```toml
[resolve]
manifest-url = "https://someregistry.com/protostar/versions.json"
manifest-version-key = "latest_version"
```

protostar.yaml

```yaml
resolve:
  manifestUrl: 'https://someregistry.com/protostar/versions.json'
  manifestVersionKey: 'latest_version'
```

#### Versions and aliasesv0.36.0 [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#versions-and-aliases "Direct link to versions-and-aliases")

As an alternative, we also support a static configuration of explicit versions and aliases. This is
useful if you have an internal tool that is relatively stable, or does not provide a means in which
to extract version information.

- `versions` \- A list of versions.
- `aliases` \- A mapping of alias names to versions.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "resolve": {
    "versions": [\
      "1.2.3",\
      "1.2.4",\
      "1.2.5"\
    ],
    "aliases": {
      "stable": "1.2.4"
    }
  }
}
```

protostar.toml

```toml
[resolve]
versions = [ "1.2.3", "1.2.4", "1.2.5" ]

[resolve.aliases]
stable = "1.2.4"
```

protostar.yaml

```yaml
resolve:
  versions:
    - '1.2.3'
    - '1.2.4'
    - '1.2.5'
  aliases:
    stable: '1.2.4'
```

#### Version patterns [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#version-patterns "Direct link to Version patterns")

When a version is found, either from a git tag or manifest key, we attempt to parse it into a
[valid version](https://moonrepo.dev/docs/proto/tool-spec) using a Rust based regex pattern and the `version-pattern` setting.

This pattern uses named regex capture groups (`(?<name>...)`) to build the version, and to support
found versions that are not fully-qualified (they may be missing patch or minor versions). The
following groups are supported:

- `major` / `year` \- The major version number. Defaults to `0` if missing.
- `minor` / `month` \- The minor version number. Defaults to `0` if missing.
- `patch` / `day` \- The patch version number. Defaults to `0` if missing.
- `pre` \- The pre-release identifier, like "rc.0" or "alpha.0". Supports an optional leading `-`.
Does nothing if missing.
- `build` \- The build metadata, like a timestamp. Supports an optional leading `+`. Does nothing if
missing.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "resolve": {
    "versionPattern": "^@protostar/cli@((?<major>\\d+)\\.(?<minor>\\d+)\\.(?<patch>\\d+))"
  }
}
```

protostar.toml

```toml
[resolve]
version-pattern = "^@protostar/cli@((?<major>\\d+)\\.(?<minor>\\d+)\\.(?<patch>\\d+))"
```

protostar.yaml

```yaml
resolve:
  versionPattern: '^@protostar/cli@((?<major>\d+)\.(?<minor>\d+)\.(?<patch>\d+))'
```

> If no named capture groups are found, the match at index `1` is used as the version.

### Detecting versions [​](https://moonrepo.dev/docs/proto/non-wasm-plugin\#detecting-versions "Direct link to Detecting versions")

And lastly, we can configure how to [detect a version](https://moonrepo.dev/docs/proto/detection) contextually at runtime, using
the `[detect]` setting. At this time, we only support 1 setting:

- `version-files` \- A list of version files to extract from. The contents of these files can _only_
be the version string itself.

- JSON
- TOML
- YAML

protostar.json

```json
{
  "detect": {
    "versionFiles": [\
      ".protostar-version",\
      ".protostarrc"\
    ]
  }
}
```

protostar.toml

```toml
[detect]
version-files = [ ".protostar-version", ".protostarrc" ]
```

protostar.yaml

```yaml
detect:
  versionFiles:
    - '.protostar-version'
    - '.protostarrc'
```

- [Create a plugin](https://moonrepo.dev/docs/proto/non-wasm-plugin#create-a-plugin)
  - [Platform variations](https://moonrepo.dev/docs/proto/non-wasm-plugin#platform-variations)
  - [Downloading and installing](https://moonrepo.dev/docs/proto/non-wasm-plugin#downloading-and-installing)
    - [Executables](https://moonrepo.dev/docs/proto/non-wasm-plugin#executables)
    - [Global packages](https://moonrepo.dev/docs/proto/non-wasm-plugin#global-packages)
  - [Resolving versions](https://moonrepo.dev/docs/proto/non-wasm-plugin#resolving-versions)
    - [Git tags](https://moonrepo.dev/docs/proto/non-wasm-plugin#git-tags)
    - [JSON manifest](https://moonrepo.dev/docs/proto/non-wasm-plugin#json-manifest)
    - [Versions and aliases](https://moonrepo.dev/docs/proto/non-wasm-plugin#versions-and-aliases)
    - [Version patterns](https://moonrepo.dev/docs/proto/non-wasm-plugin#version-patterns)
  - [Detecting versions](https://moonrepo.dev/docs/proto/non-wasm-plugin#detecting-versions)