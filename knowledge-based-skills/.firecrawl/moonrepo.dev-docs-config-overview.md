[Skip to main content](https://moonrepo.dev/docs/config/overview#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

## Supported formatsv2.0.0 [​](https://moonrepo.dev/docs/config/overview\#supported-formats "Direct link to supported-formats")

In moon, you can define configuration files in a variety of formats. We currently support the
following:

- JSON (`.json`)
- JSON with comments (`.jsonc`)
- [HCL](https://github.com/hashicorp/hcl) (`.hcl`)
- [Pkl](https://pkl-lang.org/) (`.pkl`)
- [TOML](https://toml.io/en/) (`.toml`)
- YAML (`.yml`, `.yaml`)

info

In moon v1, only YAML (`.yml`) and Pkl (`.pkl`) configuration files were supported.

## Schema validationv1.33.0 [​](https://moonrepo.dev/docs/config/overview\#schema-validation "Direct link to schema-validation")

We support schema validation for all configuration files through
[JSON Schema](https://json-schema.org/), even for formats that are not JSON (depends on tool/editor
support). To reference the schema for a specific configuration file, configure the `$schema`
property at the top of the file with the appropriate schema found at `.moon/cache/schemas`.

- .moon/workspace
- .moon/extensions
- .moon/toolchains
- .moon/tasks
- moon
- template

.moon/workspace.yml

```yaml
$schema: './cache/schemas/workspace.json'
```

.moon/extensions.yml

```yaml
$schema: './cache/schemas/extensions.json'
```

.moon/toolchains.yml

```yaml
$schema: './cache/schemas/toolchains.json'
```

.moon/tasks/all.yml

```yaml
$schema: '../cache/schemas/tasks.json'
```

moon.yml

```yaml
$schema: '../path/to/.moon/cache/schemas/project.json'
```

template.yml

```yaml
$schema: '../path/to/.moon/cache/schemas/template.json'
```

info

The schemas are automatically created when running a task. If they do not exist yet, you can run
[`moon sync config-schemas`](https://moonrepo.dev/docs/commands/sync/config-schemas) to generate them manually.

danger

In older versions of moon, the schema files were located at `https://moonrepo.dev/schemas`. These
URLs are now deprecated, as they do not support dynamic settings. Please update your `$schema`
references to point to the local schema files in `.moon/cache/schemas`.

## Setup & usage [​](https://moonrepo.dev/docs/config/overview\#setup--usage "Direct link to Setup & usage")

### Pkl [​](https://moonrepo.dev/docs/config/overview\#pkl "Direct link to Pkl")

Pkl utilizes a client-server architecture, which means that the `pkl` binary must exist in the
environment for parsing and evaluating `.pkl` files. Jump over to the
[official documentation for instructions on how to install Pkl](https://pkl-lang.org/main/current/pkl-cli/index.html#installation).

If you are using [proto](https://moonrepo.dev/proto), you can install Pkl with the following commands.

```shell
proto plugin add pkl https://raw.githubusercontent.com/milesj/proto-plugins/refs/heads/master/pkl.toml
proto install pkl --pin
```

To start using Pkl in moon, simply:

- Install [Pkl](https://moonrepo.dev/docs/config/overview#installing-pkl) and the
[VS Code extension](https://pkl-lang.org/vscode/current/index.html).
- Create configs with the `.pkl` extension.

info

We highly suggest reading the Pkl
[language reference](https://pkl-lang.org/main/current/language-reference/index.html) and the
[standard library](https://pkl-lang.org/main/current/standard-library.html).

#### Caveats and restrictions [​](https://moonrepo.dev/docs/config/overview\#caveats-and-restrictions "Direct link to Caveats and restrictions")

Since this is an entirely new configuration format that is quite dynamic compared to YAML, there are
some key differences to be aware of!

- Only files are supported. Cannot use or extend from URLs.

- Each `.pkl` file is evaluated in isolation (loops are processed, variables assigned, etc). This
means that task inheritance and file merging cannot extend or infer this native functionality.

- `default` is a
[special feature](https://pkl-lang.org/main/current/language-reference/index.html#default-element)
in Pkl and cannot be used as a setting name. This only applies to
[`template.pkl`](https://moonrepo.dev/docs/config/template#default), but can be worked around by using `defaultValue`
instead.


template.pkl

```pkl
variables {
  ["age"] {
    type = "number"
    prompt = "Age?"
    defaultValue = 0
}
```

#### Example functionality [​](https://moonrepo.dev/docs/config/overview\#example-functionality "Direct link to Example functionality")

Loops and conditionals:

```pkl
tasks {
  for (_os in List("linux", "macos", "windows")) {
    ["build-\(_os)"] {
      command = "cargo"
      args = List(
        "--target",
        if (_os == "linux") "x86_64-unknown-linux-gnu"
          else if (_os == "macos") "x86_64-apple-darwin"
          else "i686-pc-windows-msvc",
        "--verbose"
      )
      options {
        os = _os
      }
    }
  }
}
```

Local variables:

```pkl
local _sharedInputs = List("src/**/*")

tasks {
  ["test"] {
    // ...
    inputs = List("tests/**/*") + _sharedInputs
  }
  ["lint"] {
    // ...
    inputs = List("**/*.graphql") + _sharedInputs
  }
}
```

- [Supported formats](https://moonrepo.dev/docs/config/overview#supported-formats)
- [Schema validation](https://moonrepo.dev/docs/config/overview#schema-validation)
- [Setup & usage](https://moonrepo.dev/docs/config/overview#setup--usage)
  - [Pkl](https://moonrepo.dev/docs/config/overview#pkl)
    - [Caveats and restrictions](https://moonrepo.dev/docs/config/overview#caveats-and-restrictions)
    - [Example functionality](https://moonrepo.dev/docs/config/overview#example-functionality)