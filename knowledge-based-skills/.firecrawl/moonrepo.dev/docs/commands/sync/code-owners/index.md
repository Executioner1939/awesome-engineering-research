[Skip to main content](https://moonrepo.dev/docs/commands/sync/code-owners#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.8.0

The `moon sync code-owners` command will manually sync code owners, by aggregating all owners from
projects, and generating a single `CODEOWNERS` file. Refer to the official
[code owners](https://moonrepo.dev/docs/guides/codeowners) guide for more information.

```shell
$ moon sync code-owners
```

### Options [​](https://moonrepo.dev/docs/commands/sync/code-owners\#options "Direct link to Options")

- `--clean` \- Clean and remove previously generated file.
- `--force` \- Bypass cache and force create file.

### Configuration [​](https://moonrepo.dev/docs/commands/sync/code-owners\#configuration "Direct link to Configuration")

- [`codeowners`](https://moonrepo.dev/docs/config/workspace#codeowners) in `.moon/workspace.*`
- [`owners`](https://moonrepo.dev/docs/config/project#owners) in `moon.*`

- [Options](https://moonrepo.dev/docs/commands/sync/code-owners#options)
- [Configuration](https://moonrepo.dev/docs/commands/sync/code-owners#configuration)