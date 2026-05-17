[Skip to main content](https://moonrepo.dev/docs/commands/generate#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon generate <id>` (or `moon g`) command will generate code (files and folders) from a
pre-defined template of the same name, using an interactive series of prompts. Templates are located
based on the [`generator.templates`](https://moonrepo.dev/docs/config/workspace#templates) setting.

```shell
# Generate code from a template
$ moon generate npm-package

# Generate code from a template to a target directory
$ moon generate npm-package --to ./packages/example

# Generate code while declaring custom variable values
$ moon generate npm-package --to ./packages/example -- --name "@company/example"

# Create a new template
$ moon generate react-app --template
```

> View the official [code generation guide](https://moonrepo.dev/docs/guides/codegen) for a more in-depth example of how to
> utilize this command.

### Arguments [​](https://moonrepo.dev/docs/commands/generate\#arguments "Direct link to Arguments")

- `<id>` \- ID of the template to generate.
- `[-- <vars>]` \- Additional arguments to override default variable values.

### Options [​](https://moonrepo.dev/docs/commands/generate\#options "Direct link to Options")

- `--defaults` \- Use the default value of all variables instead of prompting the user.
- `--dry-run` \- Run entire generator process without writing files.
- `--force` \- Force overwrite any existing files at the destination.
- `--template` \- Create a new template with the provided name.
- `--to` \- Destination to write files to, relative from the current working directory. If not
defined, will be prompted during generation.

### Configuration [​](https://moonrepo.dev/docs/commands/generate\#configuration "Direct link to Configuration")

- [`generator`](https://moonrepo.dev/docs/config/workspace#generator) in `.moon/workspace.*`

- [Arguments](https://moonrepo.dev/docs/commands/generate#arguments)
- [Options](https://moonrepo.dev/docs/commands/generate#options)
- [Configuration](https://moonrepo.dev/docs/commands/generate#configuration)