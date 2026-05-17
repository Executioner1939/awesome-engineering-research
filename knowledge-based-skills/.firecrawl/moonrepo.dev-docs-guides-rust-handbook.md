[Skip to main content](https://moonrepo.dev/docs/guides/rust/handbook#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Utilizing Rust in a monorepo is a trivial task, thanks to Cargo, and also moon. With this handbook,
we'll help guide you through this process.

info

moon is not a build system and does _not_ replace Cargo. Instead, moon runs `cargo` commands, and
efficiently orchestrates those tasks within the workspace.

## moon setup [​](https://moonrepo.dev/docs/guides/rust/handbook\#moon-setup "Direct link to moon setup")

For this part of the handbook, we'll be focusing on [moon](https://moonrepo.dev/moon), our task runner. To start,
languages in moon act like plugins, where their functionality and support _is not_ enabled unless
explicitly configured. We follow this approach to avoid unnecessary overhead.

### Enabling the language [​](https://moonrepo.dev/docs/guides/rust/handbook\#enabling-the-language "Direct link to Enabling the language")

To enable Rust, define the [`rust`](https://moonrepo.dev/docs/config/toolchain#rust) setting in
[`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain), even if an empty object.

.moon/toolchains.yml

```yaml
# Enable Rust
rust: {}

# Enable Rust and override default settings
rust:
  syncToolchainConfig: true
```

Or by pinning a `rust` version in [`.prototools`](https://moonrepo.dev/docs/proto/config) in the workspace root.

.prototools

```toml
rust = "1.93.0"
```

This will enable the Rust toolchain and provide the following automations around its ecosystem:

- Manifests and lockfiles are parsed for accurate dependency versions for hashing purposes.
- Cargo binaries (in `~/.cargo/bin`) are properly located and executed.
- Automatically sync `rust-toolchain.toml` configuration files.
- For non-workspaces, will inherit `package.name` from `Cargo.toml` as a project alias.
- And more to come!

### Utilizing the toolchain [​](https://moonrepo.dev/docs/guides/rust/handbook\#utilizing-the-toolchain "Direct link to Utilizing the toolchain")

When a language is enabled, moon by default will assume that the language's binary is available
within the current environment (typically on `PATH`). This has the downside of requiring all
developers and machines to manually install the correct version of the language, _and to stay in_
_sync_.

Instead, you can utilize [moon's toolchain](https://moonrepo.dev/docs/concepts/toolchain), which will download and
install the language in the background, and ensure every task is executed using the exact version
across all machines.

Enabling the toolchain is as simple as defining the
[`rust.version`](https://moonrepo.dev/docs/config/toolchain#version-2) setting.

.moon/toolchains.yml

```yaml
# Enable Rust toolchain with an explicit version
rust:
  version: '1.69.0'
```

> Versions can also be defined with [`.prototools`](https://moonrepo.dev/docs/proto/config).

caution

moon requires `rustup` to exist in the environment, and will use this to install the necessary Rust
toolchains. moon will attempt to auto-install `rustup` if it's not found, but this may fail in some
environments.

## Repository structure [​](https://moonrepo.dev/docs/guides/rust/handbook\#repository-structure "Direct link to Repository structure")

Rust/Cargo repositories come in two flavors: a single crate with one `Cargo.toml`, or multiple
crates with many `Cargo.toml`s using
[Cargo workspaces](https://doc.rust-lang.org/book/ch14-03-cargo-workspaces.html). The latter is
highly preferred as it enables Cargo incremental caching.

With moon, you can place [`moon.*`](https://moonrepo.dev/docs/config/project) in each crate, or once relative to
`Cargo.lock`. The choice is yours! But be aware, if you do per-crate, Cargo itself will "wait for
build lock" when multiple processes are running.

An example of this layout is demonstrated below:

- Workspaces
- Workspaces (per-crate)
- Non-workspaces

```text
/
├── .moon/
├── crates/
│   ├── client/
|   │   ├── ...
│   │   └── Cargo.toml
│   ├── server/
|   │   ├── ...
│   │   └── Cargo.toml
│   └── utils/
|       ├── ...
│       └── Cargo.toml
├── target/
├── Cargo.lock
├── Cargo.toml
└── moon.yml
```

```text
/
├── .moon/
├── crates/
│   ├── client/
|   │   ├── ...
|   │   ├── moon.yml
│   │   └── Cargo.toml
│   ├── server/
|   │   ├── ...
|   │   ├── moon.yml
│   │   └── Cargo.toml
│   └── utils/
|       ├── ...
|   │   ├── moon.yml
│       └── Cargo.toml
├── target/
├── Cargo.lock
└── Cargo.toml
```

```text
/
├── .moon/
├── src/
│   └── lib.rs
├── tests/
│   └── ...
├── target/
├── Cargo.lock
├── Cargo.toml
└── moon.yml
```

### Example `moon.*` [​](https://moonrepo.dev/docs/guides/rust/handbook\#example-moon "Direct link to example-moon")

The following configuration represents a base that covers most Rust projects.

- Workspaces
- Workspaces (per-crate) / Non-workspaces

<project>/moon.yml

```yaml
language: 'rust'
layer: 'application'

env:
  CARGO_TERM_COLOR: 'always'

fileGroups:
  sources:
    - 'crates/*/src/**/*'
    - 'crates/*/Cargo.toml'
    - 'Cargo.toml'
  tests:
    - 'crates/*/benches/**/*'
    - 'crates/*/tests/**/*'

tasks:
  build:
    command: 'cargo build'
    inputs:
      - '@globs(sources)'
  check:
    command: 'cargo check --workspace'
    inputs:
      - '@globs(sources)'
  format:
    command: 'cargo fmt --all --check'
    inputs:
      - '@globs(sources)'
      - '@globs(tests)'
  lint:
    command: 'cargo clippy --workspace'
    inputs:
      - '@globs(sources)'
      - '@globs(tests)'
  test:
    command: 'cargo test --workspace'
    inputs:
      - '@globs(sources)'
      - '@globs(tests)'
```

<project>/moon.yml

```yaml
language: 'rust'
layer: 'application'

env:
  CARGO_TERM_COLOR: 'always'

fileGroups:
  sources:
    - 'src/**/*'
    - 'Cargo.toml'
  tests:
    - 'benches/**/*'
    - 'tests/**/*'

tasks:
  build:
    command: 'cargo build'
    inputs:
      - '@globs(sources)'
  check:
    command: 'cargo check'
    inputs:
      - '@globs(sources)'
  format:
    command: 'cargo fmt --check'
    inputs:
      - '@globs(sources)'
      - '@globs(tests)'
  lint:
    command: 'cargo clippy'
    inputs:
      - '@globs(sources)'
      - '@globs(tests)'
  test:
    command: 'cargo test'
    inputs:
      - '@globs(sources)'
      - '@globs(tests)'
```

## Cargo integration [​](https://moonrepo.dev/docs/guides/rust/handbook\#cargo-integration "Direct link to Cargo integration")

You can't use Rust without Cargo -- well you could but why would you do that? With moon, we're doing
our best to integrate with Cargo as much as possible. Here's a few of the benefits we currently
provide.

### Global binaries [​](https://moonrepo.dev/docs/guides/rust/handbook\#global-binaries "Direct link to Global binaries")

Cargo supports global binaries through the
[`cargo install`](https://doc.rust-lang.org/cargo/commands/cargo-install.html) command, which
installs a crate to `~/.cargo/bin`, or makes it available through the `cargo <crate>` command. These
are extremely beneficial for development, but they do require every developer to manually install
the crate (and appropriate version) to their machine.

With moon, this is no longer an issue with the [`rust.bins`](https://moonrepo.dev/docs/config/toolchain#bins) setting.
This setting requires a list of crates (with optional versions) to install, and moon will install
them as part of the task runner install dependencies action. Furthermore, binaries will be installed
with [`cargo-binstall`](https://crates.io/crates/cargo-binstall) in an effort to reduce build and
compilation times.

.moon/toolchains.yml

```yaml
rust:
  bins:
    - 'cargo-make@0.35.0'
    - 'cargo-nextest'
```

At this point, tasks can be configured to run this binary as a command. The `cargo` prefix is
optional, as we'll inject it when necessary.

<project>/moon.yml

```yaml
tasks:
  test:
    command: 'nextest run --workspace'
    toolchain: 'rust'
```

tip

The `cargo-binstall` crate may require a `GITHUB_TOKEN` environment variable to make GitHub Releases
API requests, especially in CI. If you're being rate limited, or fail to find a download, try
creating a token with necessary permissions.

### Lockfile handling [​](https://moonrepo.dev/docs/guides/rust/handbook\#lockfile-handling "Direct link to Lockfile handling")

To expand our integration even further, we also take `Cargo.lock` into account, and apply the
following automations when a target is being ran:

- If the lockfile does not exist, we generate one with
[`cargo generate-lockfile`](https://doc.rust-lang.org/cargo/commands/cargo-generate-lockfile.html).
- We parse and extract the resolved checksums and versions for more accurate hashing.

## FAQ [​](https://moonrepo.dev/docs/guides/rust/handbook\#faq "Direct link to FAQ")

### Should we cache the `target` directory as an output? [​](https://moonrepo.dev/docs/guides/rust/handbook\#should-we-cache-the-target-directory-as-an-output "Direct link to should-we-cache-the-target-directory-as-an-output")

No, definitely not! Both moon and Cargo support incremental caching, but they're not entirely
compatible, and will most likely cause problems when used together.

The biggest factor is that moon's caching and hydration uses a tarball strategy, where each task
would unpack a tarball on cache hit, and archive a tarball on cache miss. The Cargo target directory
is extremely large (moon's is around 50gb), and coupling this with our tarball strategy is not
viable. This would cause massive performance degradation.

However, at maximum, you _could_ cache the compiled binary itself as an output, instead of the
entire target directory. Example:

moon.yml

```yaml
tasks:
  build:
    command: 'cargo build --release'
    outputs: ['target/release/moon']
```

### How can we improve CI times? [​](https://moonrepo.dev/docs/guides/rust/handbook\#how-can-we-improve-ci-times "Direct link to How can we improve CI times?")

Rust is known for slow build times and CI is no exception. With that being said, there are a few
patterns to help alleviate this, both on the moon side and outside of it.

To start, you can cache Rust builds in CI. This is a non-moon solution to the `target` directory
problem above.

1. If you use GitHub Actions, feel free to use our
[moonrepo/setup-rust](https://github.com/moonrepo/setup-rust) action, which has built-in caching.
2. A more integrated solution is [sccache](https://crates.io/crates/sccache), which stores build
artifacts in a cloud storage provider.

- [moon setup](https://moonrepo.dev/docs/guides/rust/handbook#moon-setup)
  - [Enabling the language](https://moonrepo.dev/docs/guides/rust/handbook#enabling-the-language)
  - [Utilizing the toolchain](https://moonrepo.dev/docs/guides/rust/handbook#utilizing-the-toolchain)
- [Repository structure](https://moonrepo.dev/docs/guides/rust/handbook#repository-structure)
  - [Example `moon.*`](https://moonrepo.dev/docs/guides/rust/handbook#example-moon)
- [Cargo integration](https://moonrepo.dev/docs/guides/rust/handbook#cargo-integration)
  - [Global binaries](https://moonrepo.dev/docs/guides/rust/handbook#global-binaries)
  - [Lockfile handling](https://moonrepo.dev/docs/guides/rust/handbook#lockfile-handling)
- [FAQ](https://moonrepo.dev/docs/guides/rust/handbook#faq)
  - [Should we cache the `target` directory as an output?](https://moonrepo.dev/docs/guides/rust/handbook#should-we-cache-the-target-directory-as-an-output)
  - [How can we improve CI times?](https://moonrepo.dev/docs/guides/rust/handbook#how-can-we-improve-ci-times)