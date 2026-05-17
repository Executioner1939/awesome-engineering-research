[Skip to main content](https://moonrepo.dev/docs/proto/commands/diagnose#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.37.0

The `proto diagnose` command will diagnose your proto installation for any potential issues. Issues
are categorized into errors and warnings, with the former being a must fix, and the latter being a
maybe fix (depending on your usage of proto).

```text
$ proto diagnose

Shell: zsh
Shell profile: /Users/name/.zshrc

Errors ────────────────────────────────────────────────────────────────────

  - Issue: Bin directory /Users/name/.proto/bin was found BEFORE the shims directory /Users/name/.proto/shims on PATH
    Resolution: Ensure the shims path comes before the bin path in your shell
    Comment: Runtime version detection will not work correctly unless shims are used
```

### Options [​](https://moonrepo.dev/docs/proto/commands/diagnose\#options "Direct link to Options")

- `--shell` \- The shell to diagnose (will detect automatically).
- `--json` \- Print the diagnosis in JSON format.

- [Options](https://moonrepo.dev/docs/proto/commands/diagnose#options)