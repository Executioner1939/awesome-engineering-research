[Skip to main content](https://moonrepo.dev/docs/commands/bin#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon bin <toolchain>` command will return an absolute path to a tool's binary within the
toolchain. If a tool has not been configured or installed, this will return a 1 or 2 exit code with
no value respectively.

```shell
$ moon bin node
/Users/example/.proto/tools/node/x.x.x/bin/node
```

> A tool is considered "not configured" when not in use, for example, querying yarn/pnpm when the
> package manager is configured for "npm". A tool is considered "not installed", when it has not
> been downloaded and installed into the tools directory.

### Arguments [​](https://moonrepo.dev/docs/commands/bin\#arguments "Direct link to Arguments")

- `<toolchain>` \- Name of the toolchain to query.

- [Arguments](https://moonrepo.dev/docs/commands/bin#arguments)