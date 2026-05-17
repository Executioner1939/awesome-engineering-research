[Skip to main content](https://moonrepo.dev/docs/commands/docker/setup#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon docker setup` command will efficiently install dependencies for focused projects. This is
an all-in-one command for toolchain and dependency installations, and should replace `npm install`
and other commands.

```shell
$ moon docker setup
```

info

View the official [Docker usage guide](https://moonrepo.dev/docs/guides/docker) for a more in-depth example of how to
utilize this command.

caution

This command _must be_ ran after [`moon docker scaffold`](https://moonrepo.dev/docs/commands/docker/scaffold) and is typically ran within a
`Dockerfile`! The [`moon docker file`](https://moonrepo.dev/docs/commands/docker/file) command can be used to generate a `Dockerfile`.

### Configuration [​](https://moonrepo.dev/docs/commands/docker/setup\#configuration "Direct link to Configuration")

- [`*`](https://moonrepo.dev/docs/config/toolchain) in `.moon/toolchains.*`

- [Configuration](https://moonrepo.dev/docs/commands/docker/setup#configuration)