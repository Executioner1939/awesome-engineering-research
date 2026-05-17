[Skip to main content](https://moonrepo.dev/docs/proto/commands/debug/env#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.26.0

The `proto debug env` command will print information about your current proto environment. Primarily
the store location, relevant file paths, and environment variables.

```text
$ proto debug env

Store ─────────────────────────────────────────────────────────────────────

  Root: /Users/name/.proto
  Bins: /Users/name/.proto/bin
  Shims: /Users/name/.proto/shims
  Plugins: /Users/name/.proto/plugins
  Tools: /Users/name/.proto/tools
  Temp: /Users/name/.proto/temp

Environment ───────────────────────────────────────────────────────────────

  Proto version: 0.44.0
  Operating system: macos
  Architecture: arm64
  Config sources:
    - /Users/name/Projects/example/.prototools
    - /Users/name/.proto/.prototools
  Virtual paths:
    /userhome = /Users/name
    /proto = /Users/name/.proto
  Environment variables:
    PROTO_APP_LOG = proto=info,schematic=info,starbase=info,warpgate=info,extism::pdk=info
    PROTO_HOME = /Users/name/.proto
    PROTO_OFFLINE_TIMEOUT = 750
    PROTO_VERSION = 0.44.0
```

### Options [​](https://moonrepo.dev/docs/proto/commands/debug/env\#options "Direct link to Options")

- `--json` \- Print the list in JSON format.

- [Options](https://moonrepo.dev/docs/proto/commands/debug/env#options)