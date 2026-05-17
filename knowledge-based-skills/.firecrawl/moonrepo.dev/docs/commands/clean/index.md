[Skip to main content](https://moonrepo.dev/docs/commands/clean#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon clean` command will clean the current workspace by deleting stale cache. For the most
part, the action pipeline will clean automatically, but this command can be used to reset the
workspace entirely.

```shell
$ moon clean

# Delete cache with a custom lifetime
$ moon clean --lifetime '24 hours'
```

### Options [​](https://moonrepo.dev/docs/commands/clean\#options "Direct link to Options")

- `--all` \- Clean all cached items and reset state. v2.0.0
- `--lifetime` \- The maximum lifetime of cached artifacts before being marked as stale. Defaults to
"7 days".

- [Options](https://moonrepo.dev/docs/commands/clean#options)