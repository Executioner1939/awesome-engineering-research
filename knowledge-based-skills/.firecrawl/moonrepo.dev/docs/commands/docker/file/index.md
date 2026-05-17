[Skip to main content](https://moonrepo.dev/docs/commands/docker/file#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.27.0

The `moon docker file <project>` command can be used to generate a multi-staged `Dockerfile` for a
project, that takes full advantage of Docker's layer caching, and is primarily for production
deploys (this should not be used for development).

```shell
$ moon docker file <project>
```

As mentioned above, the generated `Dockerfile` uses a multi-stage approach, where each stage is
broken up into the following:

- `base` \- The base stage, which simply installs moon for a chosen Docker image. This stage requires
Bash.
- `skeleton` \- Scaffolds workspace and sources repository skeletons using
[`moon docker scaffold`](https://moonrepo.dev/docs/commands/docker/scaffold).
- `build` \- Copies required sources, installs the toolchain using [`moon docker setup`](https://moonrepo.dev/docs/commands/docker/setup),
optionally builds the project, and optionally prunes the image using
[`moon docker prune`](https://moonrepo.dev/docs/commands/docker/prune).
- `start` \- Runs the project after it has been built. This is typically starting an HTTP server, or
executing a binary.

info

View the official [Docker usage guide](https://moonrepo.dev/docs/guides/docker) for a more in-depth example of how to
utilize this command.

### Arguments [​](https://moonrepo.dev/docs/commands/docker/file\#arguments "Direct link to Arguments")

- `<id>` \- Name or alias of a project, as defined in [`projects`](https://moonrepo.dev/docs/config/workspace#projects).
- `[dest]` \- Destination to write the file, relative from the project root. Defaults to
`Dockerfile`.

### Options [​](https://moonrepo.dev/docs/commands/docker/file\#options "Direct link to Options")

- `--defaults` \- Use default options instead of prompting in the terminal.
- `--build-task` \- Name of a task to build the project. Defaults to the
[`docker.file.buildTask`](https://moonrepo.dev/docs/config/project#buildtask) setting, or prompts in the terminal.
- `--image` \- Base Docker image to use. Defaults to an image derived from the toolchain, or prompts
in the terminal.
- `--no-prune` \- Do not prune dependencies in the build stage.
- `--no-setup` \- Do not setup dependencies in the build stage. v2.0.0
- `--no-toolchain` \- Do not use the toolchain and instead use system binaries.
- `--start-task` \- Name of a task to start the project. Defaults to the
[`docker.file.startTask`](https://moonrepo.dev/docs/config/project#starttask) setting, or prompts in the terminal.
- `--template` \- Template path, relative from the workspace root, to render the Dockerfile with.v2.0.0

### Configuration [​](https://moonrepo.dev/docs/commands/docker/file\#configuration "Direct link to Configuration")

- [`docker.file`](https://moonrepo.dev/docs/config/project#file) in `moon.*`

- [Arguments](https://moonrepo.dev/docs/commands/docker/file#arguments)
- [Options](https://moonrepo.dev/docs/commands/docker/file#options)
- [Configuration](https://moonrepo.dev/docs/commands/docker/file#configuration)