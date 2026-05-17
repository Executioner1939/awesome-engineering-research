[Skip to main content](https://moonrepo.dev/docs/setup-workspace#__docusaurus_skipToContent_fallback)

BunDenoGoNode.jsPHPPythonRubyRust

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

2 min

Once moon has been [installed](https://moonrepo.dev/docs/install), we must setup the [workspace](https://moonrepo.dev/docs/concepts/workspace),
which is denoted by the `.moon` folder (or `.config/moon`) — this is known as the workspace root.
The workspace is in charge of:

- Integrating with a version control system.
- Defining configuration that applies to its entire tree.
- Housing [projects](https://moonrepo.dev/docs/concepts/project) to build a [project graph](https://moonrepo.dev/docs/how-it-works/project-graph).
- Running tasks with the [action graph](https://moonrepo.dev/docs/how-it-works/action-graph).

## Initializing the repository [​](https://moonrepo.dev/docs/setup-workspace\#initializing-the-repository "Direct link to Initializing the repository")

Let's scaffold and initialize moon in a repository with the [`moon init`](https://moonrepo.dev/docs/commands/init) command.
This should typically be ran at the root, but can be nested within a directory.

```shell
$ moon init
```

When executed, the following operations will be applied.

- Creates a `.moon` folder with a [`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace) configuration file.
- Appends necessary ignore patterns to the relative `.gitignore`.
- Infers the version control system from the environment.

info

If you're investigating moon, or merely want to prototype, you can use `moon init --minimal` to
quickly initialize and create minimal configuration files.

## Migrate from an existing build system [​](https://moonrepo.dev/docs/setup-workspace\#migrate-from-an-existing-build-system "Direct link to Migrate from an existing build system")

Looking to migrate from Nx or Turborepo to moon? Use our
[`moon ext migrate-nx`](https://moonrepo.dev/docs/guides/extensions#migrate-nx) or
[`moon ext migrate-turborepo`](https://moonrepo.dev/docs/guides/extensions#migrate-turborepo) commands for a (somewhat)
seamless migration!

These extensions will convert your existing configuration files to moon's format as best as
possible, but is not a requirement.

## Configuring a version control system [​](https://moonrepo.dev/docs/setup-workspace\#configuring-a-version-control-system "Direct link to Configuring a version control system")

moon requires a version control system (VCS) to be present for functionality like file diffing,
hashing, and revision comparison. The VCS and its default branch can be configured through the
[`vcs`](https://moonrepo.dev/docs/config/workspace#vcs) setting.

.moon/workspace.yml

```yaml
vcs:
  client: 'git'
  defaultBranch: 'master'
```

> moon defaults to `git` and the settings above, so feel free to skip this.

## Next steps [​](https://moonrepo.dev/docs/setup-workspace\#next-steps "Direct link to Next steps")

[Create a project](https://moonrepo.dev/docs/create-project) [Configure `.moon/workspace.*` further](https://moonrepo.dev/docs/config/workspace) [Learn about the workspace](https://moonrepo.dev/docs/concepts/workspace)

- [Initializing the repository](https://moonrepo.dev/docs/setup-workspace#initializing-the-repository)
- [Migrate from an existing build system](https://moonrepo.dev/docs/setup-workspace#migrate-from-an-existing-build-system)
- [Configuring a version control system](https://moonrepo.dev/docs/setup-workspace#configuring-a-version-control-system)
- [Next steps](https://moonrepo.dev/docs/setup-workspace#next-steps)