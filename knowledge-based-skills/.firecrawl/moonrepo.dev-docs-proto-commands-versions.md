[Skip to main content](https://moonrepo.dev/docs/proto/commands/versions#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.44.0

The `proto versions <tool>` command will list available versions by resolving versions from the
tool's remote release manifest. Furthermore, if a version has been installed locally, it will be
denoted with a timestamp.

```shell
$ proto versions node
...
22.0.0
22.1.0
22.2.0
22.3.0
22.4.0
22.4.1
22.5.0 - installed 12/25/24
22.5.1
22.6.0
22.7.0
22.8.0
22.9.0
22.10.0
22.11.0
22.12.0
23.0.0
23.1.0
23.2.0
23.3.0
23.4.0 - installed 12/19/24
23.5.0 - installed 12/25/24
```

### Filtering versionsv0.57.0 [​](https://moonrepo.dev/docs/proto/commands/versions\#filtering-versions "Direct link to filtering-versions")

To narrow the list down to a specific range, pass a
[version requirement](https://moonrepo.dev/docs/proto/tool-spec#requirements-and-ranges) as the second argument. Only versions
that satisfy the requirement will be displayed.

```shell
$ proto versions node 24
$ proto versions node ">=22, <24"
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/versions\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.
- `[filter]` \- Version range/requirement to filter the list by. v0.57.0

### Options [​](https://moonrepo.dev/docs/proto/commands/versions\#options "Direct link to Options")

- `--aliases` \- Include aliases in the list.
- `--installed` \- Only display installed versions.
- `--json` \- Print the versions and aliases in JSON format.

- [Filtering versions](https://moonrepo.dev/docs/proto/commands/versions#filtering-versions)
- [Arguments](https://moonrepo.dev/docs/proto/commands/versions#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/versions#options)