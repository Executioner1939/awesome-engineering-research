[Skip to main content](https://moonrepo.dev/docs/commands/sync/vcs-hooks#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.9.0

The `moon sync vcs-hooks` command will manually sync hooks for the configured
[VCS](https://moonrepo.dev/docs/config/workspace#vcs), by generating and referencing hook scripts from the
[`vcs.hooks`](https://moonrepo.dev/docs/config/workspace#hooks) setting. Refer to the official
[VCS hooks](https://moonrepo.dev/docs/guides/vcs-hooks) guide for more information.

```shell
$ moon sync vcs-hooks
```

### Options [​](https://moonrepo.dev/docs/commands/sync/vcs-hooks\#options "Direct link to Options")

- `--clean` \- Clean and remove previously generated hooks.
- `--force` \- Bypass cache and force create hooks.

### Configuration [​](https://moonrepo.dev/docs/commands/sync/vcs-hooks\#configuration "Direct link to Configuration")

- [`vcs.hooks`](https://moonrepo.dev/docs/config/workspace#hooks) in `.moon/workspace.*`

- [Options](https://moonrepo.dev/docs/commands/sync/vcs-hooks#options)
- [Configuration](https://moonrepo.dev/docs/commands/sync/vcs-hooks#configuration)