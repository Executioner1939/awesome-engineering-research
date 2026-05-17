[Skip to main content](https://moonrepo.dev/docs/guides/extensions#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.20.0

An extension is a WASM plugin that allows you to extend moon with additional functionality, have
whitelisted access to the file system, and receive partial information about the current workspace.
Extensions are extremely useful in offering new and unique functionality that doesn't need to be
built into moon's core. It also enables the community to build and share their own extensions!

## Using extensions [​](https://moonrepo.dev/docs/guides/extensions\#using-extensions "Direct link to Using extensions")

Before an extension can be executed with the [`moon ext`](https://moonrepo.dev/docs/commands/ext) command, it must be
configured with [`.moon/extensions.*`](https://moonrepo.dev/docs/config/extensions) (excluding
[built-in's](https://moonrepo.dev/docs/guides/extensions#built-in-extensions)).

.moon/extensions.yml

```yaml
example:
  plugin: 'https://example.com/path/to/example.wasm'
```

Once configured, it can be executed with [`moon ext`](https://moonrepo.dev/docs/commands/ext) by name. Arguments unique to
the extension _must_ be passed after a `--` separator.

```shell
$ moon ext example -- --arg1 --arg2
```

## Built-in extensions [​](https://moonrepo.dev/docs/guides/extensions\#built-in-extensions "Direct link to Built-in extensions")

moon is shipped with a few built-in extensions that are configured and enabled by default. Official
moon extensions are built and published in our [moonrepo/moon-extensions](https://github.com/moonrepo/plugins) repository.

### `download` [​](https://moonrepo.dev/docs/guides/extensions\#download "Direct link to download")

The `download` extension can be used to download a file from a URL into the current workspace, as
defined by the `--url` argument. For example, say we want to download the latest [proto](https://moonrepo.dev/proto)
binary:

```shell
$ moon ext download --\
  --url https://github.com/moonrepo/proto/releases/latest/download/proto_cli-aarch64-apple-darwin.tar.xz
```

By default this will download `proto_cli-aarch64-apple-darwin.tar.xz` into the current working
directory. To customize the location, use the `--dest` argument. However, do note that the
destination _must be_ within the current moon workspace, as only certain directories are whitelisted
for WASM.

```shell
$ moon ext download --\
  --url https://github.com/moonrepo/proto/releases/latest/download/proto_cli-aarch64-apple-darwin.tar.xz\
  --dest ./temp
```

#### Arguments [​](https://moonrepo.dev/docs/guides/extensions\#arguments "Direct link to Arguments")

- `--url` (required) - URL of a file to download.
- `--dest` \- Destination folder to save the file. Defaults to the current working directory.
- `--name` \- Override the file name. Defaults to the file name in the URL.

### `migrate-nx`v1.22.0 [​](https://moonrepo.dev/docs/guides/extensions\#migrate-nx "Direct link to migrate-nx")

> This extension is currently _experimental_ and will be improved over time.

The `migrate-nx` extension can be used to migrate an Nx powered repository to moon. This process
will convert the root `nx.json` and `workspace.json` files, and any `project.json` and
`package.json` files found within the repository. The following changes are made:

- Migrates `targetDefaults` as global tasks to [`.moon/tasks/node.yml`](https://moonrepo.dev/docs/config/tasks#tasks) (or
`bun.yml`), `namedInputs` as file groups, `workspaceLayout` as projects, and more.
- Migrates all `project.json` settings to [`moon.yml`](https://moonrepo.dev/docs/config/project#tasks) equivalent settings.
Target to task conversion assumes the following:
  - Target `executor` will be removed, and we'll attempt to extract the appropriate npm package
    command. For example, `@nx/webpack:build` -\> `webpack build`.
  - Target `options` will be converted to task `args`.
  - The `{projectRoot}` and `{workspaceRoot}` interpolations will be replaced with moon tokens.

```shell
$ moon ext migrate-nx
```

caution

Nx and moon are quite different, so many settings are either ignored when converting, or are not a
1:1 conversion. We do our best to convert as much as possible, but some manual patching will most
likely be required! We suggest testing each converted task 1-by-1 to ensure it works as expected.

#### Arguments [​](https://moonrepo.dev/docs/guides/extensions\#arguments-1 "Direct link to Arguments")

- `--bun` \- Migrate to Bun based commands instead of Node.js.
- `--cleanup` \- Remove Nx configs/files after migrating.

#### Unsupported [​](https://moonrepo.dev/docs/guides/extensions\#unsupported "Direct link to Unsupported")

The following features are not supported in moon, and are ignored when converting.

- Most settings in `nx.json`.
- Named input variants: external dependencies, dependent task output files, dependent project
inputs, or runtime commands.
- Target `configurations` and `defaultConfiguration`. Another task will be created instead that uses
`extends`.
- Project `root` and `sourceRoot`.

### `migrate-turborepo`v1.21.0 [​](https://moonrepo.dev/docs/guides/extensions\#migrate-turborepo "Direct link to migrate-turborepo")

The `migrate-turborepo` extension can be used to migrate a Turborepo powered repository to moon.
This process will convert the root `turbo.json` file, and any `turbo.json` files found within the
repository. The following changes are made:

- Migrates `pipeline` (v1) and `tasks` (v2) global tasks to
[`.moon/tasks/node.yml`](https://moonrepo.dev/docs/config/tasks#tasks) (or `bun.yml`) and project scoped tasks to
[`moon.*`](https://moonrepo.dev/docs/config/project#tasks). Task commands will execute `package.json` scripts through a
package manager.
- Migrates root `global*` settings to [`.moon/tasks/node.yml`](https://moonrepo.dev/docs/config/tasks#implicitinputs) (or
`bun.yml`) as `implicitInputs`.

```shell
$ moon ext migrate-turborepo
```

#### Arguments [​](https://moonrepo.dev/docs/guides/extensions\#arguments-2 "Direct link to Arguments")

- `--bun` \- Migrate to Bun based commands instead of Node.js.
- `--cleanup` \- Remove Turborepo configs/files after migrating.

### `unpack`v2.0.0 [​](https://moonrepo.dev/docs/guides/extensions\#unpack "Direct link to unpack")

The `unpack` extension can be used to unpack an archive (zip/tar) from a file path or URL into a
destination folder.

```shell
$ moon ext unpack -- --src ./path/to/archive.zip --dest ./output --prefix path/to/strip
```

#### Arguments [​](https://moonrepo.dev/docs/guides/extensions\#arguments-3 "Direct link to Arguments")

- `--src` (required) - Path or URL of a file to unpack.
- `--dest` \- Destination folder to unpack into. Defaults to the current working directory.
- `--prefix` \- A prefix path to strip from unpacked files.

## Creating an extension [​](https://moonrepo.dev/docs/guides/extensions\#creating-an-extension "Direct link to Creating an extension")

Refer to our [official WASM guide](https://moonrepo.dev/docs/guides/wasm-plugins) for more information on how our WASM plugins
work, critical concepts to know, how to create a plugin, and more. Once you have a good
understanding, you may continue this specific guide.

note

Refer to our [moonrepo/plugins](https://github.com/moonrepo/plugins) repository for in-depth examples.

### Registering metadata [​](https://moonrepo.dev/docs/guides/extensions\#registering-metadata "Direct link to Registering metadata")

Before we begin, we must implement the `register_extension` function, which simply provides some
metadata that we can bubble up to users, or to use for deeper integrations.

```rust
use extism_pdk::*;
use moon_pdk::*;

#[plugin_fn]
pub fn register_extension(Json(input): Json<ExtensionMetadataInput>) -> FnResult<Json<ExtensionMetadataOutput>> {
   Ok(Json(ExtensionMetadataOutput {
        name: "Extension name".into(),
        description: Some("A description about what the extension does.".into()),
        plugin_version: env!("CARGO_PKG_VERSION").into(),
        ..ExtensionMetadataOutput::default()
    }))
}
```

#### Configuration schema [​](https://moonrepo.dev/docs/guides/extensions\#configuration-schema "Direct link to Configuration schema")

If you are using [configuration](https://moonrepo.dev/docs/guides/extensions#supporting-configuration), you can register the shape of the
configuration using the [`schematic`](https://crates.io/crates/schematic) crate. This shape will be
used to generate outputs such as JSON schemas, or TypeScript types.

```rust
#[plugin_fn]
pub fn define_extension_config() -> FnResult<Json<DefineExtensionConfigOutput>> {
    Ok(Json(DefineExtensionConfigOutput {
        schema: schematic::SchemaBuilder::build_root::<ExampleExtensionConfig>(),
    }))
}
```

Schematic is a heavy library, so we suggest adding the dependency like so:

```toml
[dependencies]
schematic = { version = "*", default-features = false, features = ["schema"] }
```

### Implementing execution [​](https://moonrepo.dev/docs/guides/extensions\#implementing-execution "Direct link to Implementing execution")

Extensions support a single plugin function, `execute_extension`, which is called by the
[`moon ext`](https://moonrepo.dev/docs/commands/ext) command to execute the extension. This is where all your business
logic will reside.

```rust
#[host_fn]
extern "ExtismHost" {
    fn host_log(input: Json<HostLogInput>);
}

#[plugin_fn]
pub fn execute_extension(Json(input): Json<ExecuteExtensionInput>) -> FnResult<()> {
  host_log!(stdout, "Executing extension!");

  Ok(())
}
```

### Supporting arguments [​](https://moonrepo.dev/docs/guides/extensions\#supporting-arguments "Direct link to Supporting arguments")

Most extensions will require arguments, as it provides a mechanism for users to pass information
into the WASM runtime. To parse arguments, we provide the
[`Args`](https://docs.rs/clap/latest/clap/trait.Args.html) trait/macro from the
[clap](https://crates.io/crates/clap) crate. Refer to their
[official documentation on usage](https://docs.rs/clap/latest/clap/_derive/index.html) (we don't
support everything).

```rust
use moon_pdk::*;

#[derive(Args)]
pub struct ExampleExtensionArgs {
  // --url, -u
  #[arg(long, short = 'u', required = true)]
  pub url: String,
}
```

Once your struct has been defined, you can parse the provided input arguments using the
[`parse_args`](https://docs.rs/moon_pdk/latest/moon_pdk/args/fn.parse_args.html) function.

```rust
#[plugin_fn]
pub fn execute_extension(Json(input): Json<ExecuteExtensionInput>) -> FnResult<()> {
  let args = parse_args::<ExampleExtensionArgs>(&input.args)?;

  args.url; // --url

  Ok(())
}
```

### Supporting configuration [​](https://moonrepo.dev/docs/guides/extensions\#supporting-configuration "Direct link to Supporting configuration")

Users can configure [extensions](https://moonrepo.dev/docs/config/workspace#extensions) with additional settings in
[`.moon/extensions.*`](https://moonrepo.dev/docs/config/extensions). Do note that settings should be in camelCase for them
to be parsed correctly!

.moon/extensions.yml

```yaml
example:
  plugin: 'file://./path/to/example.wasm'
  someSetting: 'abc'
  anotherSetting: 123
```

In the plugin, we can map these settings (excluding `plugin`) into a struct. The `Default` trait
must be implemented to handle situations where settings were not configured, or some are missing.

```rust
config_struct!(
  #[derive(Default)]
  pub struct ExampleExtensionConfig {
    pub some_setting: String,
    pub another_setting: u32,
  }
);
```

Once your struct has been defined, you can access the configuration using the
[`get_extension_config`](https://docs.rs/moon_pdk/latest/moon_pdk/extension/fn.get_extension_config.html)
function.

```rust
#[plugin_fn]
pub fn execute_extension(Json(input): Json<ExecuteExtensionInput>) -> FnResult<()> {
  let config = get_extension_config::<ExampleExtensionConfig>()?;

  config.another_setting; // 123

  Ok(())
}
```

- [Using extensions](https://moonrepo.dev/docs/guides/extensions#using-extensions)
- [Built-in extensions](https://moonrepo.dev/docs/guides/extensions#built-in-extensions)
  - [`download`](https://moonrepo.dev/docs/guides/extensions#download)
    - [Arguments](https://moonrepo.dev/docs/guides/extensions#arguments)
  - [`migrate-nx`](https://moonrepo.dev/docs/guides/extensions#migrate-nx)
    - [Arguments](https://moonrepo.dev/docs/guides/extensions#arguments-1)
    - [Unsupported](https://moonrepo.dev/docs/guides/extensions#unsupported)
  - [`migrate-turborepo`](https://moonrepo.dev/docs/guides/extensions#migrate-turborepo)
    - [Arguments](https://moonrepo.dev/docs/guides/extensions#arguments-2)
  - [`unpack`](https://moonrepo.dev/docs/guides/extensions#unpack)
    - [Arguments](https://moonrepo.dev/docs/guides/extensions#arguments-3)
- [Creating an extension](https://moonrepo.dev/docs/guides/extensions#creating-an-extension)
  - [Registering metadata](https://moonrepo.dev/docs/guides/extensions#registering-metadata)
    - [Configuration schema](https://moonrepo.dev/docs/guides/extensions#configuration-schema)
  - [Implementing execution](https://moonrepo.dev/docs/guides/extensions#implementing-execution)
  - [Supporting arguments](https://moonrepo.dev/docs/guides/extensions#supporting-arguments)
  - [Supporting configuration](https://moonrepo.dev/docs/guides/extensions#supporting-configuration)