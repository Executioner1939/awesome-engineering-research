[Skip to main content](https://moonrepo.dev/docs/proto#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

3 min

proto is a pluggable version manager, a unified toolchain.

If you're unfamiliar with the concept of a toolchain, a toolchain is a collection of tools that are
downloaded, installed, and managed by version through a single interface. In the context of proto's
toolchain, a tool is either a programming language, a dependency/package manager for a language, or
a custom implementation provided by a plugin. It's the next step in the version manager evolution.

## Features [​](https://moonrepo.dev/docs/proto\#features "Direct link to Features")

- Lightspeed! With Rust and WASM, we can guarantee exceptional performance.
- Multi-language. A single CLI for managing versions for all of your languages.
- Cross-platform, for a consistent experience across machines and teams.
- [Contextual version detection](https://moonrepo.dev/docs/proto/detection), ensuring the correct version of a tool is
always used.
- Checksum verification, ensuring a tool came from a trusted source.
- Detects and infers from a language's ecosystem for maximum compatibility.
- [Pluggable architecture](https://moonrepo.dev/docs/proto/plugins), allowing for custom tooling.

## Why proto? [​](https://moonrepo.dev/docs/proto\#why-proto "Direct link to Why proto?")

proto was designed to be a modern and holistic version manager for all of your favorite programming
languages. We believe a single tool that works the same across every language is better than
multiple ad-hoc tools. While we only support a handful of languages today, we aim to support many
more in the future!

success

proto powers [moon](https://moonrepo.dev/moon)'s toolchain, enabling a single source of truth for both tools!

## How does it work? [​](https://moonrepo.dev/docs/proto\#how-does-it-work "Direct link to How does it work?")

The toolchain is a `.proto` directory within the current user's home directory, e.g., `~/.proto`.

The first step in a tool's life-cycle is being downloaded to `~/.proto/temp`. Downloads are
typically an archive that can be unpacked into a target directory. Once downloaded, we verify the
downloaded file by running a checksum. If this check fails for _any reason_, the tool is unusable,
and the process is aborted.

After a successful verification, the last step in the tool's life-cycle can begin, installation.
Depending on the type of download, the installation process may differ. For archives, we unpack the
tool to `~/.proto/tools/<name>/<version>`. In the future, we'll support building from source.

From here, we make these tools globally available by prepending `~/.proto/shims` and `~/.proto/bin`
to `PATH` (typically as part of your shell profile). Continue reading for more about these folders.

## Supported tools [​](https://moonrepo.dev/docs/proto\#supported-tools "Direct link to Supported tools")

The following tools are [officially supported](https://moonrepo.dev/docs/proto/tools) in proto via moonrepo. Additional
tools can be supported through [third-party plugins](https://moonrepo.dev/docs/proto/plugins).

\+ npm, pnpm, yarn

\+ pip, poetry, uv

... with [126 more proto plugins](https://moonrepo.dev/docs/proto/tools#third-party), and over [800 asdf plugins](https://moonrepo.dev/docs/proto/tool-spec#asdf)...

## Supported targets [​](https://moonrepo.dev/docs/proto\#supported-targets "Direct link to Supported targets")

Because proto is written in Rust, we only support targets that are explicitly compiled for, which
are currently:

| Operating system | Architecture | Target |
| --- | --- | --- |
| macOS 64-bit | Intel | `x86_64-apple-darwin` |
| macOS 64-bit | ARM | `aarch64-apple-darwin` |
| Linux 64-bit | Intel GNU | `x86_64-unknown-linux-gnu` |
| Linux 64-bit | Intel musl | `x86_64-unknown-linux-musl` |
| Linux 64-bit | ARM GNU | `aarch64-unknown-linux-gnu` |
| Linux 64-bit | ARM musl | `aarch64-unknown-linux-musl` |
| Windows 64-bit | Intel | `x86_64-pc-windows-msvc` |

- [Features](https://moonrepo.dev/docs/proto#features)
- [Why proto?](https://moonrepo.dev/docs/proto#why-proto)
- [How does it work?](https://moonrepo.dev/docs/proto#how-does-it-work)
- [Supported tools](https://moonrepo.dev/docs/proto#supported-tools)
- [Supported targets](https://moonrepo.dev/docs/proto#supported-targets)