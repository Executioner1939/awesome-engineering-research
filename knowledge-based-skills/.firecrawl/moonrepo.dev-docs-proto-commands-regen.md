[Skip to main content](https://moonrepo.dev/docs/proto/commands/regen#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.27.0

The `proto regen` command can be used to regenerate all shims in the `~/.proto/shims` directory.
This command will also clean the shims directory before regenerating, in an effort to remove
unexpected or broken shims.

```shell
$ proto regen
```

By default this will only regenerate shims. If you want to regenerate bins in `~/.proto/bin` as
well, pass the `--bin` flag. This will also clean the bins directory before regenerating.

```shell
$ proto regen --bin
```

> Only versions pinned in `~/.proto/.prototools` will be linked as bins.

## Options [​](https://moonrepo.dev/docs/proto/commands/regen\#options "Direct link to Options")

- `--bin` \- Also recreate `~/.proto/bin` symlinks.

- [Options](https://moonrepo.dev/docs/proto/commands/regen#options)