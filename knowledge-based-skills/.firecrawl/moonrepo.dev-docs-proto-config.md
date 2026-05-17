[Skip to main content](https://moonrepo.dev/docs/proto/config#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

We support configuration at both the project-level and user-level using a
[TOML](https://toml.io/en/) based `.prototools` file. This file can be used to pin versions of
tools, provide tool specific configuration, enable new tools via plugins, define proto settings, and
more.

## Locationsv0.41.0 [​](https://moonrepo.dev/docs/proto/config\#locations "Direct link to locations")

proto supports 3 locations in which a `.prototools` file can exist. These locations are used
throughout the command line and proto's own settings.

- `local` -\> `./.prototools`, `.\.prototools` (current directory)
- `global` -\> `~/.proto/.prototools`, `%USERPROFILE%\.proto\.prototools`
- `user` -\> `~/.prototools`, `%USERPROFILE%\.prototools`

> Local is a bit of a misnomer as a `.prototools` file can theoretically exist in any directory, but
> when reading/writing to a file, `local` refers to the current working directory.

### Where to configure? [​](https://moonrepo.dev/docs/proto/config\#where-to-configure "Direct link to Where to configure?")

With so many locations to store proto configuration, the question of where to store certain
configurations become blurred, especially when [resolution](https://moonrepo.dev/docs/proto/config#resolution-mode) comes into play. We
suggest the following locations:

- Default/fallback [versions](https://moonrepo.dev/docs/proto/config#pinning-versions) of tools -> `global`
- Project specific [versions](https://moonrepo.dev/docs/proto/config#pinning-versions) of tools -> `local`
- Project specific [settings](https://moonrepo.dev/docs/proto/config#settings) -\> `local`
- Shared/developer [settings](https://moonrepo.dev/docs/proto/config#settings) -\> `user`
- Non-project related -> `user`

## Resolution modev0.40.0 [​](https://moonrepo.dev/docs/proto/config\#resolution-mode "Direct link to resolution-mode")

When a `proto` command or shim is ran, we must find and load all applicable `.prototools` files. We
then deeply merge all of these configuration files into a final configuration object, with the
current directory taking highest precedence.

The order in which to resolve configuration can be defined using the `--config-mode` (`-c`) command
line option, or the `PROTO_CONFIG_MODE` environment variable. The following 4 modes are supported:

### `global` [​](https://moonrepo.dev/docs/proto/config\#global "Direct link to global")

In this mode, proto will _only_ load the `~/.proto/.prototools` file. This "global" file acts as
configuration at the user-level and allows for fallback settings.

```text
~/.proto/.prototools
```

### `local` [​](https://moonrepo.dev/docs/proto/config\#local "Direct link to local")

In this mode, proto will _only_ load the `.prototools` file in the current directory.

```text
./.prototools
```

### `upwards` [​](https://moonrepo.dev/docs/proto/config\#upwards "Direct link to upwards")

In this mode, proto will traverse upwards starting from the current directory, and load
`.prototools` within each directory, until we reach the system root or the user directory (`~`),
whichever comes first.

```text
~/Projects/app/.prototools (cwd)
~/Projects/.prototools
~/.prototools
```

> This is the default mode for the [`activate`](https://moonrepo.dev/docs/proto/commands/activate),
> [`install`](https://moonrepo.dev/docs/proto/commands/install), [`outdated`](https://moonrepo.dev/docs/proto/commands/outdated), and
> [`status`](https://moonrepo.dev/docs/proto/commands/status) commands.

### `upwards-global` / `all` [​](https://moonrepo.dev/docs/proto/config\#upwards-global--all "Direct link to upwards-global--all")

This mode works exactly like [`upwards`](https://moonrepo.dev/docs/proto/config#upwards) but with the functionality of [`global`](https://moonrepo.dev/docs/proto/config#global)
as well. The global `~/.proto/.prototools` file is appended as the final entry.

```text
~/Projects/app/.prototools (cwd)
~/Projects/.prototools
~/.prototools
~/.proto/.prototools
```

> This is the default mode for all other commands not listed above in `upwards`.

## Environment modev0.29.0 [​](https://moonrepo.dev/docs/proto/config\#environment-mode "Direct link to environment-mode")

We also support environment specific configuration, such as `.prototools.production` or
`.prototools.development`, when the `PROTO_ENV` environment variable is set. This is useful for
defining environment specific aliases, or tool specific configuration.

These environment aware settings take precedence over the default `.prototools` file, for the
directory it's located in, and are merged in the same way as the default configuration. For example,
the lookup order would be the following when `PROTO_ENV=production`:

```text
~/Projects/.prototools.production
~/Projects/.prototools
~/.prototools.production
~/.prototools
~/.proto/.prototools
```

> The global `~/.proto/.prototools` file does not support environment modes.

## Pinning versions [​](https://moonrepo.dev/docs/proto/config\#pinning-versions "Direct link to Pinning versions")

proto supports pinning versions of tools on a per-directory basis through our `.prototools`
configuration file. This file takes precedence during [version detection](https://moonrepo.dev/docs/proto/detection) and can be
created/updated with [`proto pin`](https://moonrepo.dev/docs/proto/commands/pin).

At its most basic level, you can map tools to specific versions, for the directory the file is
located in. A [version](https://moonrepo.dev/docs/proto/tool-spec) can either be a fully-qualified version, a partial version, a
range or requirement, or an alias.

.prototools

```toml
node = "16.16.0"
npm = "9"
go = "~1.20"
rust = "stable"
```

### Lock `proto` versionv0.39.0 [​](https://moonrepo.dev/docs/proto/config\#lock-proto-version "Direct link to lock-proto-version")

You can also pin the version of proto that you want all tools to execute with by adding a `proto`
version entry. This approach uses shims and dynamic version detection like other tools.

.prototools

```toml
proto = "0.38.0"
```

## Available settings [​](https://moonrepo.dev/docs/proto/config\#available-settings "Direct link to Available settings")

### `[env]`v0.29.0 [​](https://moonrepo.dev/docs/proto/config\#env "Direct link to env")

This setting is a map of environment variables that will be applied to _all_ tools when they are
executed, or when [`proto activate`](https://moonrepo.dev/docs/proto/commands/activate) is ran in a shell profile. Variables
defined here _will not_ override existing environment variables (either passed on the command line,
or inherited from the shell).

.prototools

```toml
[env]
DEBUG = "*"
```

Additionally, `false` can be provided as a value, which will _remove_ the environment variable. This
is useful for removing inherited shell variables.

.prototools

```toml
[env]
DEBUG = false
```

Variables also support substitution using the syntax `${VAR_NAME}`. When using substitution,
variables in the current process and merged `[env]` can be referenced. Recursive substitution is not
supported!

> This functionality enables per-directory environment variables!

#### `file`v0.43.0 [​](https://moonrepo.dev/docs/proto/config\#file "Direct link to file")

This is a special field that points to a dotenv file, relative from the current configuration file,
that will be loaded into the environment variables mapping. Variables defined in a dotenv file will
be loaded _before_ variables manually defined within `[env]`.

This feature utilizes the [dotenvy](https://github.com/allan2/dotenvy) crate for parsing dotfiles.

.prototools

```toml
[env]
file = ".env"
```

### `[settings]` [​](https://moonrepo.dev/docs/proto/config\#settings "Direct link to settings")

#### `auto-install` [​](https://moonrepo.dev/docs/proto/config\#auto-install "Direct link to auto-install")

When enabled, will automatically install a missing version of a tool when
[`proto run`](https://moonrepo.dev/docs/proto/commands/run) is ran, instead of erroring. Defaults to `false` or
`PROTO_AUTO_INSTALL`.

.prototools

```toml
[settings]
auto-install = true
```

warning

This functionality requires shims (not activation) and will only work after a tool has been
installed at least once. This is because the shim executable handles the interception and the shim
is created after a tool is installed.

#### `auto-clean` [​](https://moonrepo.dev/docs/proto/config\#auto-clean "Direct link to auto-clean")

When enabled, will automatically clean up the proto store in the background, by removing unused
tools and outdated plugins. Defaults to `false` or `PROTO_AUTO_CLEAN`.

.prototools

```toml
[settings]
auto-clean = true
```

#### `builtin-plugins`v0.39.0 [​](https://moonrepo.dev/docs/proto/config\#builtin-plugins "Direct link to builtin-plugins")

Can be used to customize the [built-in plugins](https://moonrepo.dev/docs/proto/tools#built-in) within proto. Can disable all
built-ins by passing `false`, or enabling a select few by name. Defaults to `true`, which enables
all.

.prototools

```toml
[settings]
# Disable all
builtin-plugins = false
# Enable some
builtin-plugins = ["node", "bun"]
```

#### `cache-duration`v0.50.1 [​](https://moonrepo.dev/docs/proto/config\#cache-duration "Direct link to cache-duration")

The duration in seconds in which to cache downloaded plugins. Defaults to 30 days.

.prototools

```toml
[settings]
cache-duration = 3600
```

#### `detect-strategy` [​](https://moonrepo.dev/docs/proto/config\#detect-strategy "Direct link to detect-strategy")

The strategy to use when [detecting versions](https://moonrepo.dev/docs/proto/detection). Defaults to `first-available` or
`PROTO_DETECT_STRATEGY`.

- `first-available` \- Will use the first available version that is found. Either from `.prototools`
or a tool specific file (`.nvmrc`, etc).
- `prefer-prototools` \- Prefer a `.prototools` version, even if found in a parent directory. If none
found, falls back to tool specific file.
- `only-prototools` \- Only use a version defined in `.prototools`. v0.34.0

.prototools

```toml
[settings]
detect-strategy = "prefer-prototools"
```

#### `pin-latest` [​](https://moonrepo.dev/docs/proto/config\#pin-latest "Direct link to pin-latest")

When defined and a tool is installed with the "latest" alias, will automatically pin the resolved
version to the configured location. Defaults to disabled or `PROTO_PIN_LATEST`.

- `global` \- Pins globally to `~/.proto/.prototools`.
- `local` \- Pins locally to `./.prototools` in current directory.
- `user` \- Pins to the user's `~/.prototools` in their home directory.v0.41.0

.prototools

```toml
[settings]
pin-latest = "local"
```

#### `telemetry` [​](https://moonrepo.dev/docs/proto/config\#telemetry "Direct link to telemetry")

When enabled, we collect anonymous usage statistics for tool installs and uninstalls. This helps us
prioritize which tools to support, what tools or their versions may be broken, the plugins currently
in use, and more. Defaults to `true`.

.prototools

```toml
[settings]
telemetry = false
```

> The data we track is publicly available and
> [can be found here](https://github.com/moonrepo/proto/blob/master/crates/cli/src/telemetry.rs).

#### `unstable-lockfile`v0.51.0 [​](https://moonrepo.dev/docs/proto/config\#unstable-lockfile "Direct link to unstable-lockfile")

When enabled, will create a `.protolock` file relative to this configuration file. The lockfile will
record and lock all tools, their versions, and checksums from the configuration file, ensuring
consistency across machines, and reliability.

.prototools

```toml
[settings]
unstable-lockfile = true
```

#### `unstable-registries`v0.51.0 [​](https://moonrepo.dev/docs/proto/config\#unstable-registries "Direct link to unstable-registries")

A list of OCI registries to query for plugins by
[reference](https://oras.land/docs/concepts/reference). Registries will be queried in the order they
are configured. Each registry object supports the following fields:

- `registry` \- The registry host, e.g. `ghcr.io`.
- `namespace` \- The namespace (or organization) that the plugin belongs to.
- `auth` (bool) - Whether the registry requires authentication. When true, proto will attempt to
load credentials for this host from the Docker config. v0.57.0
- `default` (bool) - Whether this registry should be used as the default when the locator only
provides an identifier (no registry host or namespace). v0.57.0

.prototools

```toml
[settings]
unstable-registries = [\
  { registry = "ghcr.io", namespace = "moonrepo", default = true },\
  { registry = "custom.host.com", namespace = "my-org", auth = true },\
]
```

#### `url-rewrites`v0.50.0 [​](https://moonrepo.dev/docs/proto/config\#url-rewrites "Direct link to url-rewrites")

Provides a mechanism for rewriting most URLs used by proto, such as those used for downloading
tools. This setting accepts a map of [Rust regular expressions](https://docs.rs/regex/latest/regex/)
to [replacement strings](https://docs.rs/regex/latest/regex/struct.Regex.html#method.replace). When
a URL is rewritten, all entries in the map are applied in order, and all matches are replaced.

.prototools

```toml
[settings.url-rewrites]
"github.com/(\\w+)/(\\w+)" = "gh-mirror.corp.com/$1/$2"
"mo+n" = "lunar"
```

The following types of URLs are rewritten:

- Tool download/checksum URLs (even from third-party plugins)
- Plugin download URLs
- Build script URLs
- Archive URLs

The following are _not_ rewritten:

- Git repository URLs
- proto version check/telemetry URLs

### `[settings.build]`v0.46.0 [​](https://moonrepo.dev/docs/proto/config\#settingsbuild "Direct link to settingsbuild")

Can be used to customize the build from source flow.

#### `exclude-packages` [​](https://moonrepo.dev/docs/proto/config\#exclude-packages "Direct link to exclude-packages")

Configures a list of packages that should be excluded during installation.

.prototools

```toml
[settings.build]
exclude-packages = ["git", "python3", "libssl-dev"]
```

#### `install-system-packages` [​](https://moonrepo.dev/docs/proto/config\#install-system-packages "Direct link to install-system-packages")

When enabled, will install packages required for building using the system package manager. Defaults
to `true`.

.prototools

```toml
[settings.build]
install-system-packages = false
```

#### `system-package-manager` [​](https://moonrepo.dev/docs/proto/config\#system-package-manager "Direct link to system-package-manager")

Customize the system package manager to use when installing system packages and their dependencies.
By default we attempt to detect the package manager to use from the environment.

This setting accepts a map, where the key is the name of the
[operating system](https://doc.rust-lang.org/std/env/consts/constant.OS.html), and the value is the
[package manager](https://docs.rs/system_env/latest/system_env/enum.SystemPackageManager.html) to
use. Both the key and value are in kebab-case.

.prototools

```toml
[settings.build.system-package-manager]
windows = "choco"
```

#### `write-log-file` [​](https://moonrepo.dev/docs/proto/config\#write-log-file "Direct link to write-log-file")

When a build has completed, write a log file to the current directory. This is always `true` when a
build fails, but `false` otherwise.

.prototools

```toml
[settings.build]
write-log-file = true
```

### `[settings.http]` [​](https://moonrepo.dev/docs/proto/config\#settingshttp "Direct link to settingshttp")

Can be used to customize the HTTP client used by proto, primarily for requesting files to download,
available versions, and more.

#### `allow-invalid-certs` [​](https://moonrepo.dev/docs/proto/config\#allow-invalid-certs "Direct link to allow-invalid-certs")

When enabled, will allow invalid certificates instead of failing. This is an _escape hatch_ and
should only be used if other settings have failed. Be sure you know what you're doing! Defaults to
`false`.

.prototools

```toml
[settings.http]
allow-invalid-certs = true
```

#### `proxies` [​](https://moonrepo.dev/docs/proto/config\#proxies "Direct link to proxies")

A list of proxy URLs to use for requests. As an alternative, the `HTTP_PROXY` and `HTTPS_PROXY`
environment variables can be set. URLs that start with `http://` will be considered insecure, while
`https://` will be secure.

.prototools

```toml
[settings.http]
proxies = ["https://internal.proxy", "https://corp.net/proxy"]
```

#### `secure-proxies`v0.40.3 [​](https://moonrepo.dev/docs/proto/config\#secure-proxies "Direct link to secure-proxies")

A list of proxy URLs that will be considered secure, regardless of the HTTP protocol.

.prototools

```toml
[settings.http]
secure-proxies = ["http://internal.proxy", "http://corp.net/proxy"]
```

#### `root-cert` [​](https://moonrepo.dev/docs/proto/config\#root-cert "Direct link to root-cert")

The path to a root certificate to use for requests. This is useful for overriding the native
certificate, or for using a self-signed certificate, especially when in a corporate/internal
environment. Supports `pem` and `der` files.

.prototools

```toml
[settings.http]
root-cert = "/path/to/root/cert.pem"
```

### `[settings.offline]`v0.41.0 [​](https://moonrepo.dev/docs/proto/config\#settingsoffline "Direct link to settingsoffline")

Can be used to customize how we detect an internet connection for offline based logic. These
settings are useful if you're behind a VPN or corporate proxy.

#### `custom-hosts` [​](https://moonrepo.dev/docs/proto/config\#custom-hosts "Direct link to custom-hosts")

A list of custom hosts to ping. Will be appended to our
[default list of hosts](https://moonrepo.dev/docs/proto/config#override-default-hosts) and will be ran last.

.prototools

```toml
[settings.offline]
custom-hosts = ["proxy.corp.domain.com:80"]
```

#### `override-default-hosts` [​](https://moonrepo.dev/docs/proto/config\#override-default-hosts "Direct link to override-default-hosts")

If our default hosts are blocked or are too slow, you can disable pinging them by setting this
option to true. Our default hosts are Google DNS, Cloudflare DNS, and then Google and Mozilla hosts.

This should be used in parallel with [`custom-hosts`](https://moonrepo.dev/docs/proto/config#custom-hosts).

.prototools

```toml
[settings.offline]
override-default-hosts = true
```

#### `timeout` [​](https://moonrepo.dev/docs/proto/config\#timeout "Direct link to timeout")

The timeout in milliseconds to wait for a ping against a host to resolve. Default timeout is 750ms.

.prototools

```toml
[settings.offline]
timeout = 500
```

### `[shell]`v0.56.0 [​](https://moonrepo.dev/docs/proto/config\#shell "Direct link to shell")

#### `aliases`v0.56.0 [​](https://moonrepo.dev/docs/proto/config\#aliases "Direct link to aliases")

A map of shell aliases that will be injected into your shell when running `proto activate`. This is
useful for defining aliases to share between developers, or to define aliases for tools that don't
support them natively.

.prototools

```toml
[shell.aliases]
gs = "git status"
```

### `[plugins]` [​](https://moonrepo.dev/docs/proto/config\#plugins "Direct link to plugins")

This setting was renamed to [`[plugins.tools]`](https://moonrepo.dev/docs/proto/config#pluginstools) in v0.52 but exists for backwards
compatibility.

## Backend specific settings [​](https://moonrepo.dev/docs/proto/config\#backend-specific-settings "Direct link to Backend specific settings")

### `[plugins.backends]`v0.52.0 [​](https://moonrepo.dev/docs/proto/config\#pluginsbackends "Direct link to pluginsbackends")

Custom [backend plugins](https://moonrepo.dev/docs/proto/plugins) can be configured with the `[plugins.backends]` section.
[Learn more about this syntax](https://moonrepo.dev/docs/proto/plugins#enabling-plugins).

.prototools

```toml
[plugins.backends]
my-backend = "https://raw.githubusercontent.com/my/backend/master/proto-plugin.toml"
```

Once configured, you can manage a tool plugin using your custom backend:

```shell
$ proto install my-backend:tool-id
```

### `[backends.*]`v0.53.0 [​](https://moonrepo.dev/docs/proto/config\#backends "Direct link to backends")

Backends support custom configuration that will be passed to their WASM plugin, which can be used to
control the behavior for _all_ tools managed by the backend. Please refer to the
[official documentation](https://moonrepo.dev/docs/proto/tool-spec#backends) around backends.

.prototools

```toml
[backends.example]
setting = true
```

### `[backends.*.env]`v0.53.0 [​](https://moonrepo.dev/docs/proto/config\#backendsenv "Direct link to backendsenv")

This setting is a map of environment variables for a specific backend, and will be applied when that
backend is executed through a managed tool, or when [`proto activate`](https://moonrepo.dev/docs/proto/commands/activate) is ran
in a shell profile. These variables will override those defined in `[env]`. Refer to [`[env]`](https://moonrepo.dev/docs/proto/config#env)
for usage examples.

.prototools

```toml
[backends.example.env]
KEY = "value"
```

#### `file`v0.53.0 [​](https://moonrepo.dev/docs/proto/config\#file-1 "Direct link to file-1")

Like [`[env].file`](https://moonrepo.dev/docs/proto/config#file), this is a path to a dotenv file, relative from the current configuration
file, that will be loaded into the environment variables mapping for this specific backend.

.prototools

```toml
[backends.example.env]
file = "backend/.env"
```

## Tool specific settings [​](https://moonrepo.dev/docs/proto/config\#tool-specific-settings "Direct link to Tool specific settings")

### `[plugins.tools]`v0.52.0 [​](https://moonrepo.dev/docs/proto/config\#pluginstools "Direct link to pluginstools")

Custom [tool plugins](https://moonrepo.dev/docs/proto/plugins) can be configured with the `[plugins.tools]` section.
[Learn more about this syntax](https://moonrepo.dev/docs/proto/plugins#enabling-plugins).

.prototools

```toml
[plugins.tools]
my-tool = "https://raw.githubusercontent.com/my/tool/master/proto-plugin.toml"
```

Once configured, you can manage a tool plugin:

```shell
$ proto install my-tool
```

### `[tools.*]` [​](https://moonrepo.dev/docs/proto/config\#tools "Direct link to tools")

Tools support custom configuration that will be passed to their WASM plugin, which can be used to
control the business logic within the plugin. Please refer to the [official documentation](https://moonrepo.dev/docs/proto/tools)
of each tool (typically on their repository) for a list of available settings.

As an example, let's configure [Node.js](https://github.com/moonrepo/node-plugin) (using the `node`
identifier).

.prototools

```toml
npm = "bundled" # use bundled npm instead of specific version

[tools.node]
bundled-npm = true

[tools.npm]
shared-globals-dir = true
```

### `[tools.*.aliases]` [​](https://moonrepo.dev/docs/proto/config\#toolsaliases "Direct link to toolsaliases")

Aliases are custom and unique labels that map to a specific version, and can be configured manually
within `.prototools`, or by calling the [`proto alias`](https://moonrepo.dev/docs/proto/commands/alias) command.

.prototools

```toml
[tools.node.aliases]
work = "18"
oss = "20"
```

### `[tools.*.env]`v0.29.0 [​](https://moonrepo.dev/docs/proto/config\#toolsenv "Direct link to toolsenv")

This setting is a map of environment variables for a specific tool, and will be applied when that
tool is executed, or when [`proto activate`](https://moonrepo.dev/docs/proto/commands/activate) is ran in a shell profile. These
variables will override those defined in `[env]`. Refer to [`[env]`](https://moonrepo.dev/docs/proto/config#env) for usage examples.

.prototools

```toml
[tools.node.env]
NODE_ENV = "production"
```

#### `file`v0.43.0 [​](https://moonrepo.dev/docs/proto/config\#file-2 "Direct link to file-2")

Like [`[env].file`](https://moonrepo.dev/docs/proto/config#file), this is a path to a dotenv file, relative from the current configuration
file, that will be loaded into the environment variables mapping for this specific tool.

.prototools

```toml
[tools.node.env]
file = "frontend/.env"
```

## GitHub Action [​](https://moonrepo.dev/docs/proto/config\#github-action "Direct link to GitHub Action")

To streamline GitHub CI workflows, we provide the
[`moonrepo/setup-toolchain`](https://github.com/moonrepo/setup-toolchain) action, which can be used
to install `proto` globally, and cache the toolchain found at `~/.proto`.

.github/workflows/ci.yml

```yaml
# ...
jobs:
  ci:
    name: 'CI'
    runs-on: 'ubuntu-latest'
    steps:
      - uses: 'actions/checkout@v4'
      - uses: 'moonrepo/setup-toolchain@v0'
        with:
          auto-install: true
```

- [Locations](https://moonrepo.dev/docs/proto/config#locations)
  - [Where to configure?](https://moonrepo.dev/docs/proto/config#where-to-configure)
- [Resolution mode](https://moonrepo.dev/docs/proto/config#resolution-mode)
  - [`global`](https://moonrepo.dev/docs/proto/config#global)
  - [`local`](https://moonrepo.dev/docs/proto/config#local)
  - [`upwards`](https://moonrepo.dev/docs/proto/config#upwards)
  - [`upwards-global` / `all`](https://moonrepo.dev/docs/proto/config#upwards-global--all)
- [Environment mode](https://moonrepo.dev/docs/proto/config#environment-mode)
- [Pinning versions](https://moonrepo.dev/docs/proto/config#pinning-versions)
  - [Lock `proto` version](https://moonrepo.dev/docs/proto/config#lock-proto-version)
- [Available settings](https://moonrepo.dev/docs/proto/config#available-settings)
  - [`[env]`](https://moonrepo.dev/docs/proto/config#env)
    - [`file`](https://moonrepo.dev/docs/proto/config#file)
  - [`[settings]`](https://moonrepo.dev/docs/proto/config#settings)
    - [`auto-install`](https://moonrepo.dev/docs/proto/config#auto-install)
    - [`auto-clean`](https://moonrepo.dev/docs/proto/config#auto-clean)
    - [`builtin-plugins`](https://moonrepo.dev/docs/proto/config#builtin-plugins)
    - [`cache-duration`](https://moonrepo.dev/docs/proto/config#cache-duration)
    - [`detect-strategy`](https://moonrepo.dev/docs/proto/config#detect-strategy)
    - [`pin-latest`](https://moonrepo.dev/docs/proto/config#pin-latest)
    - [`telemetry`](https://moonrepo.dev/docs/proto/config#telemetry)
    - [`unstable-lockfile`](https://moonrepo.dev/docs/proto/config#unstable-lockfile)
    - [`unstable-registries`](https://moonrepo.dev/docs/proto/config#unstable-registries)
    - [`url-rewrites`](https://moonrepo.dev/docs/proto/config#url-rewrites)
  - [`[settings.build]`](https://moonrepo.dev/docs/proto/config#settingsbuild)
    - [`exclude-packages`](https://moonrepo.dev/docs/proto/config#exclude-packages)
    - [`install-system-packages`](https://moonrepo.dev/docs/proto/config#install-system-packages)
    - [`system-package-manager`](https://moonrepo.dev/docs/proto/config#system-package-manager)
    - [`write-log-file`](https://moonrepo.dev/docs/proto/config#write-log-file)
  - [`[settings.http]`](https://moonrepo.dev/docs/proto/config#settingshttp)
    - [`allow-invalid-certs`](https://moonrepo.dev/docs/proto/config#allow-invalid-certs)
    - [`proxies`](https://moonrepo.dev/docs/proto/config#proxies)
    - [`secure-proxies`](https://moonrepo.dev/docs/proto/config#secure-proxies)
    - [`root-cert`](https://moonrepo.dev/docs/proto/config#root-cert)
  - [`[settings.offline]`](https://moonrepo.dev/docs/proto/config#settingsoffline)
    - [`custom-hosts`](https://moonrepo.dev/docs/proto/config#custom-hosts)
    - [`override-default-hosts`](https://moonrepo.dev/docs/proto/config#override-default-hosts)
    - [`timeout`](https://moonrepo.dev/docs/proto/config#timeout)
  - [`[shell]`](https://moonrepo.dev/docs/proto/config#shell)
    - [`aliases`](https://moonrepo.dev/docs/proto/config#aliases)
  - [`[plugins]`](https://moonrepo.dev/docs/proto/config#plugins)
- [Backend specific settings](https://moonrepo.dev/docs/proto/config#backend-specific-settings)
  - [`[plugins.backends]`](https://moonrepo.dev/docs/proto/config#pluginsbackends)
  - [`[backends.*]`](https://moonrepo.dev/docs/proto/config#backends)
  - [`[backends.*.env]`](https://moonrepo.dev/docs/proto/config#backendsenv)
    - [`file`](https://moonrepo.dev/docs/proto/config#file-1)
- [Tool specific settings](https://moonrepo.dev/docs/proto/config#tool-specific-settings)
  - [`[plugins.tools]`](https://moonrepo.dev/docs/proto/config#pluginstools)
  - [`[tools.*]`](https://moonrepo.dev/docs/proto/config#tools)
  - [`[tools.*.aliases]`](https://moonrepo.dev/docs/proto/config#toolsaliases)
  - [`[tools.*.env]`](https://moonrepo.dev/docs/proto/config#toolsenv)
    - [`file`](https://moonrepo.dev/docs/proto/config#file-2)
- [GitHub Action](https://moonrepo.dev/docs/proto/config#github-action)