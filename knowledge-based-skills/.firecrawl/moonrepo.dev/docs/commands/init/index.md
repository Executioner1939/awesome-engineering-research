[Skip to main content](https://moonrepo.dev/docs/commands/init#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon init` command will initialize moon into a repository and scaffold necessary config files
by creating a `.moon` folder.

```shell
$ moon init

# In another directory
$ moon init ./app
```

### Arguments [​](https://moonrepo.dev/docs/commands/init\#arguments "Direct link to Arguments")

- `[dest]` \- Destination to initialize and scaffold into. Defaults to `.` (current working
directory).

### Options [​](https://moonrepo.dev/docs/commands/init\#options "Direct link to Options")

- `--force` \- Overwrite existing config files if they exist.
- `--minimal` \- Generate minimal configurations and sane defaults.
- `--yes` \- Skip all prompts and enables tools based on file detection.

- [Arguments](https://moonrepo.dev/docs/commands/init#arguments)
- [Options](https://moonrepo.dev/docs/commands/init#options)