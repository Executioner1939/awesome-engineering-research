[Skip to main content](https://moonrepo.dev/docs/concepts/workspace#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

A workspace is a directory that contains [projects](https://moonrepo.dev/docs/concepts/project), manages a [toolchain](https://moonrepo.dev/docs/concepts/toolchain),
runs [tasks](https://moonrepo.dev/docs/concepts/task), and is coupled with a VCS repository. The root of a workspace is denoted by a
`.moon` folder.

By default moon has been designed for monorepos, but can also be used for polyrepos.

## Configuration [​](https://moonrepo.dev/docs/concepts/workspace\#configuration "Direct link to Configuration")

Configuration that's applied to the entire workspace is defined in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace).

- [Configuration](https://moonrepo.dev/docs/concepts/workspace#configuration)