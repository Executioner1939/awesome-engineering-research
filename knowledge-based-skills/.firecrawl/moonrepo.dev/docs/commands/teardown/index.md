[Skip to main content](https://moonrepo.dev/docs/commands/teardown#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon teardown` command, as its name infers, will teardown and clean the current environment,
opposite the [`setup`](https://moonrepo.dev/docs/commands/setup) command. It achieves this by doing the following:

- Uninstalling all configured toolchains.
- Removing any download or temporary files/folders.

```shell
$ moon teardown
```

### Configuration [​](https://moonrepo.dev/docs/commands/teardown\#configuration "Direct link to Configuration")

- [`*`](https://moonrepo.dev/docs/config/toolchain) in `.moon/toolchains.*`

- [Configuration](https://moonrepo.dev/docs/commands/teardown#configuration)