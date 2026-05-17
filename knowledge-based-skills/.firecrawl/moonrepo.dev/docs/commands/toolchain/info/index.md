[Skip to main content](https://moonrepo.dev/docs/commands/toolchain/info#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.38.0

The `moon toolchain info <id> [plugin]` command will display detailed information about a toolchain,
like what files are scanned, what configuration settings are available, and what tier APIs are
supported. To do this, the command will download the WASM plugin, extract information, and call
specific functions.

For built-in toolchains, the \[plugin locator\]\[locator\] argument is optional, and will be derived
from the identifier.

```shell
$ moon toolchain info typescript
```

For third-party toolchains, the \[plugin locator\]\[locator\] argument is required, and must point to
the WASM plugin.

```shell
$ moon toolchain info custom https://example.com/path/to/plugin.wasm
```

### Arguments [​](https://moonrepo.dev/docs/commands/toolchain/info\#arguments "Direct link to Arguments")

- `<id>` \- ID of the toolchain to view.
- `[plugin]` \- Optional \[plugin locator\]\[locator\] for third-party toolchains.

## Example output [​](https://moonrepo.dev/docs/commands/toolchain/info\#example-output "Direct link to Example output")

```text
Toolchain ─────────────────────────────────────────────────────────────────

  Provides sync operations that keep tsconfig.json's in a healthy state.

  ID: typescript
  Name: TypeScript
  Version: 0.2.0

Configuration ─────────────────────────────────────────────────────────────

  createMissingConfig: bool
  When `syncProjectReferences` is enabled, will create a `tsconfig.json`
  in referenced projects if it does not exist.

  includeProjectReferenceSources: bool
  Appends sources of project reference to `include` in `tsconfig.json`,
  for each project.

  includeSharedTypes: bool
  Appends shared types to `include` in `tsconfig.json`, for each project.

  projectConfigFileName: string
  Name of the `tsconfig.json` file within each project.

  root: string
  The relative root to the TypeScript root. Primarily used for
  resolving project references.

  rootConfigFileName: string
  Name of the `tsconfig.json` file at the workspace root.

  rootOptionsConfigFileName: string
  Name of the shared compiler options `tsconfig.json` file
  at the workspace root.

  routeOutDirToCache: bool
  Updates and routes `outDir` in `tsconfig.json` to moon's cache,
  for each project.

  syncProjectReferences: bool
  Syncs all project dependencies as `references` in `tsconfig.json`,
  for each project.

  syncProjectReferencesToPaths: bool
  Syncs all project dependencies as `paths` in `tsconfig.json`,
  for each project.

Tier 1 - Usage detection ──────────────────────────────────────────────────

  Config files: tsconfig.json, tsconfig.*.json, *.tsconfig.json, .tsbuildinfo, *.tsbuildinfo
  Executable names: tsc, tsserver
  APIs:
    🟢 register_toolchain (required)
    🟢 define_toolchain_config
    🟢 initialize_toolchain
    ⚫️ detect_version_files
    ⚫️ parse_version_file
    🟢 define_docker_metadata
    ⚫️ scaffold_docker
    ⚫️ prune_docker
    🟢 sync_project
    ⚫️ sync_workspace

Tier 2 - Ecosystem integration ─────────────────────────────────────────────

  APIs:
    ⚫️ extend_project_graph
    ⚫️ extend_task_command
    ⚫️ extend_task_script
    ⚫️ locate_dependencies_root
    ⚫️ install_dependencies
    🟢 hash_task_contents
    ⚫️ parse_lock
    ⚫️ parse_manifest
    ⚫️ setup_environment

Tier 3 - Tool management ──────────────────────────────────────────────────

  APIs:
    ⚫️ register_tool (required)
    ⚫️ load_versions
    ⚫️ resolve_version
    ⚫️ download_prebuilt (required)
    ⚫️ unpack_archive
    ⚫️ locate_executables (required)
    ⚫️ setup_toolchain
    ⚫️ teardown_toolchain
```

- [Arguments](https://moonrepo.dev/docs/commands/toolchain/info#arguments)
- [Example output](https://moonrepo.dev/docs/commands/toolchain/info#example-output)