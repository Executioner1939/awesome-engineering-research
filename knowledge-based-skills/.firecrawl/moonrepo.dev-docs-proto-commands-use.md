[Skip to main content](https://moonrepo.dev/docs/proto/commands/use#__docusaurus_skipToContent_fallback)

danger

This command has been deprecated and its functionality was merged into [`proto install`](https://moonrepo.dev/docs/proto/commands/install)
in v0.39. Use that command instead!

The `proto use` (or `proto u`) command will download and install _all_ tools and plugins from all
parent [`.prototools`](https://moonrepo.dev/docs/proto/config) configuration files, and any [versions detected](https://moonrepo.dev/docs/proto/detection) in
the current working directory (if not defined in `.prototools`).

```shell
$ proto use
```

> This command _does not_ install tools for versions pinned in the global `~/.proto/.prototools`
> file.