[Skip to main content](https://moonrepo.dev/docs/concepts/file-pattern#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

## Globs [​](https://moonrepo.dev/docs/concepts/file-pattern\#globs "Direct link to Globs")

Globs in moon are [Rust-based globs](https://github.com/olson-sean-k/wax), _not_ JavaScript-based.
This may result in different or unexpected results. The following guidelines must be met when using
globs:

- Must use forward slashes (`/`) for path separators, even on Windows.
- Must _not_ start with or use any relative path parts, `.` or `..`.

### Supported syntax [​](https://moonrepo.dev/docs/concepts/file-pattern\#supported-syntax "Direct link to Supported syntax")

- `*` \- Matches zero or more characters, but does not match the `/` character. Will attempt to match
the longest possible text (eager).
- `$` \- Like `*`, but will attempt to match the shortest possible text (lazy).
- `**` \- Matches zero or more directories.
- `?` \- Matches exactly one character, but not `/`.
- `[abc]` \- Matches one case-sensitive character listed in the brackets.
- `[!xyz]` \- Like the above, but will match any character _not_ listed.
- `[a-z]` \- Matches one case-sensitive character in range in the brackets.
- `[!x-z]` \- Like the above, but will match any character _not_ in range.
- `{glob,glob}` \- Matches one or more comma separated list of sub-glob patterns.
- `<glob:n,n>` \- Matches a sub-glob within a defined bounds.
- `!` \- At the start of a pattern, will negate previous positive patterns.

### Examples [​](https://moonrepo.dev/docs/concepts/file-pattern\#examples "Direct link to Examples")

```bash
README.{md,mdx,txt}
src/**/*
tests/**/*.?js
!**/__tests__/**/*
logs/<[0-9]:4>-<[0-9]:2>-<[0-9]:2>.log
```

## Project relative [​](https://moonrepo.dev/docs/concepts/file-pattern\#project-relative "Direct link to Project relative")

When configuring [`fileGroups`](https://moonrepo.dev/docs/config/project#filegroups), [`inputs`](https://moonrepo.dev/docs/config/project#inputs),
and [`outputs`](https://moonrepo.dev/docs/config/project#outputs), all listed file paths and globs are relative from the
project root they will be ran in. They _must not_ traverse upwards with `..`.

```bash
# Valid
src/**/*
./src/**/*
package.json

# Invalid
../utils
```

## Workspace relative [​](https://moonrepo.dev/docs/concepts/file-pattern\#workspace-relative "Direct link to Workspace relative")

When configuring [`fileGroups`](https://moonrepo.dev/docs/config/project#filegroups), [`inputs`](https://moonrepo.dev/docs/config/project#inputs),
and [`outputs`](https://moonrepo.dev/docs/config/project#outputs), a listed file path or glob can be prefixed with `/` to
resolve relative from the workspace root, and _not_ the project root.

```bash
# In project
package.json

# In workspace
/package.json
```

- [Globs](https://moonrepo.dev/docs/concepts/file-pattern#globs)
  - [Supported syntax](https://moonrepo.dev/docs/concepts/file-pattern#supported-syntax)
  - [Examples](https://moonrepo.dev/docs/concepts/file-pattern#examples)
- [Project relative](https://moonrepo.dev/docs/concepts/file-pattern#project-relative)
- [Workspace relative](https://moonrepo.dev/docs/concepts/file-pattern#workspace-relative)