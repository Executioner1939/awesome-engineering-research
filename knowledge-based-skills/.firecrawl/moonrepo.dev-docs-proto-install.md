[Skip to main content](https://moonrepo.dev/docs/proto/install#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

1 min

The following guide can be used to install proto into your environment.

## Requirements [​](https://moonrepo.dev/docs/proto/install\#requirements "Direct link to Requirements")

- Git - for fetching available versions/tags
- tar, unzip, gz, xz - for unpacking archives

```shell
# macOS
brew install git unzip gzip xz

# Ubuntu / Debian
apt-get install git unzip gzip xz-utils

# RHEL-based / Fedora
dnf install git unzip gzip xz
```

## Installing [​](https://moonrepo.dev/docs/proto/install\#installing "Direct link to Installing")

The entirety of proto is packaged and shipped as 2 binaries. It works on _most_ operating systems,
and does not require any external dependencies. For convenience, we provide the following scripts to
download and install proto.

info

The install location can be customized with the `PROTO_HOME` environment variable. If not provided,
the default location is `~/.proto`.

### Linux, macOS, WSL [​](https://moonrepo.dev/docs/proto/install\#linux-macos-wsl "Direct link to Linux, macOS, WSL")

In a terminal that supports Bash, run the following command. This will download and install proto,
then open an interactive prompt to complete the installation.

```shell
bash <(curl -fsSL https://moonrepo.dev/install/proto.sh)
```

For Fish shell, use process substitution with `psub` to execute the installer.

```shell
bash (curl -fsSL https://moonrepo.dev/install/proto.sh | psub)
```

Furthermore, the version of proto to install can be passed as an argument to the install script. We
also accept `--no-profile` to avoid modifying your shell profile, and `--yes` to avoid interactive
prompts.

```shell
bash <(curl -fsSL https://moonrepo.dev/install/proto.sh) 1.2.3 --yes
```

### Windows [​](https://moonrepo.dev/docs/proto/install\#windows "Direct link to Windows")

In an _administrator_ Powershell or Windows Terminal, run the following command. This will download
and install proto, then open an interactive prompt to complete the installation.

```text
irm https://moonrepo.dev/install/proto.ps1 | iex
```

You may also need to run the following command for shims to be executable:

```shell
Set-ExecutionPolicy RemoteSigned

# Without admin privileges
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Other [​](https://moonrepo.dev/docs/proto/install\#other "Direct link to Other")

proto can also be downloaded and installed manually, by downloading an asset from
[https://github.com/moonrepo/proto/releases](https://github.com/moonrepo/proto/releases). Be sure to
rename the file after downloading, and apply the executable bit (`chmod +x`) on macOS and Linux.

## Upgrading [​](https://moonrepo.dev/docs/proto/install\#upgrading "Direct link to Upgrading")

To upgrade proto, run the [`proto upgrade`](https://moonrepo.dev/docs/proto/commands/upgrade) command, or re-run the install
scripts above.

## Uninstalling [​](https://moonrepo.dev/docs/proto/install\#uninstalling "Direct link to Uninstalling")

To uninstall proto, delete the `~/.proto` directory, and remove any `PROTO_HOME` references from
your shell profile.

## Canary releases [​](https://moonrepo.dev/docs/proto/install\#canary-releases "Direct link to Canary releases")

proto supports canary releases, which are built and published for every commit to our development
branches. These releases will include features and functionality that have not yet landed on master.
Canary releases are available as a
[GitHub prerelease](https://github.com/moonrepo/proto/releases/tag/canary) using the `canary` tag.

## Nightly releases [​](https://moonrepo.dev/docs/proto/install\#nightly-releases "Direct link to Nightly releases")

proto supports nightly releases, which are built and published once a day from the latest commit on
master. Nightly releases are available as a
[GitHub prerelease](https://github.com/moonrepo/proto/releases/tag/nightly) using the `nightly` tag.

## Next steps [​](https://moonrepo.dev/docs/proto/install\#next-steps "Direct link to Next steps")

[Choose a workflow](https://moonrepo.dev/docs/proto/workflows) [Learn about `.prototools`](https://moonrepo.dev/docs/proto/config)

- [Requirements](https://moonrepo.dev/docs/proto/install#requirements)
- [Installing](https://moonrepo.dev/docs/proto/install#installing)
  - [Linux, macOS, WSL](https://moonrepo.dev/docs/proto/install#linux-macos-wsl)
  - [Windows](https://moonrepo.dev/docs/proto/install#windows)
  - [Other](https://moonrepo.dev/docs/proto/install#other)
- [Upgrading](https://moonrepo.dev/docs/proto/install#upgrading)
- [Uninstalling](https://moonrepo.dev/docs/proto/install#uninstalling)
- [Canary releases](https://moonrepo.dev/docs/proto/install#canary-releases)
- [Nightly releases](https://moonrepo.dev/docs/proto/install#nightly-releases)
- [Next steps](https://moonrepo.dev/docs/proto/install#next-steps)