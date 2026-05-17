[Skip to main content](https://moonrepo.dev/docs/commands/setup#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon setup` command can be used to setup the developer and pipeline environments. It achieves
this by downloading and installing all configured toolchains.

```shell
$ moon setup
```

info

This command should rarely be used, as the environment is automatically setup when running other
commands, like detecting affected projects, running a task, or generating a build artifact.

### Configuration [​](https://moonrepo.dev/docs/commands/setup\#configuration "Direct link to Configuration")

- [`*`](https://moonrepo.dev/docs/config/toolchain) in `.moon/toolchains.*`

- [Configuration](https://moonrepo.dev/docs/commands/setup#configuration)