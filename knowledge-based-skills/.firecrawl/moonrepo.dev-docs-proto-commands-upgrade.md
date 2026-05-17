[Skip to main content](https://moonrepo.dev/docs/proto/commands/upgrade#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto upgrade` (or `proto up`) command can be used to upgrade your current proto binary to the
latest version, or check if you're currently outdated.

```shell
$ proto upgrade

# Up/downgrade to a specific version
$ proto upgrade 0.39.0
```

info

The previous binary will be moved to `~/.proto/tools/proto/<version>`, while the new binary will be
installed to `~/.proto/bin`.

### Arguments [​](https://moonrepo.dev/docs/proto/commands/upgrade\#arguments "Direct link to Arguments")

- `<version>` \- The version of proto to explicitly upgrade or downgrade to.v0.39.3

### Options [​](https://moonrepo.dev/docs/proto/commands/upgrade\#options "Direct link to Options")

- `--check` \- Check if there's a new version without executing the upgrade.
- `--json` \- Print the upgrade information as JSON.

- [Arguments](https://moonrepo.dev/docs/proto/commands/upgrade#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/upgrade#options)