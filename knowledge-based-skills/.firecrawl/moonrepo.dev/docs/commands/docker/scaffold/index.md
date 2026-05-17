[Skip to main content](https://moonrepo.dev/docs/commands/docker/scaffold#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon docker scaffold <...projects>` command creates multiple repository skeletons for use
within `Dockerfile`s, to effectively take advantage of Docker's layer caching. It utilizes the
[project graph](https://moonrepo.dev/docs/config/workspace#projects) to copy only critical files, like manifests, lockfiles, and configuration.

```shell
# Scaffold a skeleton to .moon/docker
$ moon docker scaffold <project>
```

info

View the official [Docker usage guide](https://moonrepo.dev/docs/guides/docker) for a more in-depth example of how to
utilize this command.

### Arguments [​](https://moonrepo.dev/docs/commands/docker/scaffold\#arguments "Direct link to Arguments")

- `<...ids>` \- List of project IDs or aliases to scaffold sources for, as defined in
[`projects`](https://moonrepo.dev/docs/config/workspace#projects).

### Configuration [​](https://moonrepo.dev/docs/commands/docker/scaffold\#configuration "Direct link to Configuration")

- [`docker.scaffold`](https://moonrepo.dev/docs/config/workspace#scaffold) in `.moon/workspace.*` (entire workspace)
- [`docker.scaffold`](https://moonrepo.dev/docs/config/project#scaffold) in `moon.*` (per project)

## How it works [​](https://moonrepo.dev/docs/commands/docker/scaffold\#how-it-works "Direct link to How it works")

This command may seem like magic, but it's relative simple thanks to moon's infrastructure and its
project graph. When the command is ran, we generate 2 skeleton structures in `.moon/docker` (be sure
to gitignore this). One for configs, and the other for sources.

warning

Because scaffolding uses the project graph, it requires all projects to be [configured in\\
moon](https://moonrepo.dev/docs/config/workspace#projects). Otherwise, moon will fail to copy all required files and builds may fail.

### Configs [​](https://moonrepo.dev/docs/commands/docker/scaffold\#configs "Direct link to Configs")

The configs skeleton mirrors the project folder structure of the repository 1:1, and only copies
files required for dependencies to install. This is typically manifests (`package.json`), lockfiles
(`yarn.lock`, etc), other critical configs, and `.moon` itself. This is necessary for package
managers to install dependencies (otherwise they will fail), and for dependencies to be layer cached
in Docker.

An example of this skeleton using Yarn may look like the following:

```text
.moon/docker/configs/
├── .moon/
├── .yarn/
├── apps/
│   ├── client/
│   │   └── package.json
│   └── server/
│       └── package.json
├── packages/
│   ├── foo/
│   │   └── package.json
│   ├── bar/
│   │   └── package.json
│   └── baz/
│       └── package.json
├── .yarnrc.yml
├── package.json
└── yarn.lock
```

### Sources [​](https://moonrepo.dev/docs/commands/docker/scaffold\#sources "Direct link to Sources")

The sources skeleton is not a 1:1 mirror of the repository, and instead is the source files of a
project (passed as an argument to the command), and all of its dependencies. This allows
[`moon run`](https://moonrepo.dev/docs/commands/run) and other commands to work within the `Dockerfile`, and avoid having to
`COPY . .` the entire repository.

Using our example workspace above, our sources skeleton would look like the following, assuming our
`client` project is passed as an argument, and this project depends on the `foo` and `baz` projects.

```text
.moon/docker/sources/
├── apps/
│   └── client/
|       ├── src/
|       ├── tests/
|       ├── public/
|       ├── package.json
|       ├── tsconfig.json
│       └── (anything else)
└── packages/
    ├── foo/
    │   ├── lib/
    │   ├── src/
    │   ├── package.json
    │   ├── tsconfig.json
    │   └── (anything else)
    └── baz/
        ├── lib/
        ├── src/
        ├── package.json
        ├── tsconfig.json
        └── (anything else)
```

- [Arguments](https://moonrepo.dev/docs/commands/docker/scaffold#arguments)
- [Configuration](https://moonrepo.dev/docs/commands/docker/scaffold#configuration)
- [How it works](https://moonrepo.dev/docs/commands/docker/scaffold#how-it-works)
  - [Configs](https://moonrepo.dev/docs/commands/docker/scaffold#configs)
  - [Sources](https://moonrepo.dev/docs/commands/docker/scaffold#sources)