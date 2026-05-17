[Skip to main content](https://moonrepo.dev/docs/proto/commands/debug/config#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.25.0

The `proto debug config` command will list all `.prototools` configuration files (in TOML format)
that have been loaded, in order of precedence, with the final merged configuration printed at the
end.

```text
$ proto debug config

/Users/name/.proto/.prototools ───────────────────────────────────────────

  node = "20.0.0"
  npm = "bundled"

  [tools.node.aliases]
  stable = "~20"

  [settings]
  auto-clean = false

Final configuration ───────────────────────────────────────────────────────

  node = "20.0.0"
  npm = "bundled"

  [tools.node.aliases]
  stable = "~20"

  [plugins.tools]
  node = "https://github.com/moonrepo/node-plugin/releases/download/v0.6.1/node_plugin.wasm"

  [settings]
  auto-clean = false
  auto-install = false
  detect-strategy = "first-available"

  [settings.http]
  allow-invalid-certs = false
  proxies = []
```

### Options [​](https://moonrepo.dev/docs/proto/commands/debug/config\#options "Direct link to Options")

- `--json` \- Print the list in JSON format.

- [Options](https://moonrepo.dev/docs/proto/commands/debug/config#options)