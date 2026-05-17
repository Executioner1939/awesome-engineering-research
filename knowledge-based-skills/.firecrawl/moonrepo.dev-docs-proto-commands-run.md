[Skip to main content](https://moonrepo.dev/docs/proto/commands/run#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto run <tool> [version]` (or `proto r`) command will run a tool after
[detecting a version](https://moonrepo.dev/docs/proto/detection) from the environment.

```shell
# Run and detect version from environment
$ proto run bun

# Run with explicit version
$ proto run bun 0.5.3

# Run with version from environment variable
$ PROTO_BUN_VERSION=0.5.3 proto run bun
```

Arguments can be passed to the underlying tool binary by providing additional arguments after `--`.

```shell
$ proto run bun -- run ./script.ts

# When using the binary on PATH
$ bun run ./script.ts
```

### Arguments [​](https://moonrepo.dev/docs/proto/commands/run\#arguments "Direct link to Arguments")

- `<tool>` \- Type of tool.
- `[version]` \- Version of tool. If not provided, will attempt to detect the version from the
environment.

- [Arguments](https://moonrepo.dev/docs/proto/commands/run#arguments)