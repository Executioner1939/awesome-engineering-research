[Skip to main content](https://moonrepo.dev/docs/config/workspace#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `.moon/workspace.*` file configures projects and services in the workspace. This file is
_required_.

## `extends` [​](https://moonrepo.dev/docs/config/workspace\#extends "Direct link to extends")

Defines one or many external `.moon/workspace.*`'s to extend and inherit settings from. Perfect for
reusability and sharing configuration across repositories and projects. When defined, this setting
must be an HTTPS URL _or_ relative file system path that points to a valid YAML document!

.moon/workspace.yml

```yaml
extends: 'https://raw.githubusercontent.com/organization/repository/master/.moon/workspace.yml'
```

info

Settings will be merged recursively for blocks, with values defined in the local configuration
taking precedence over those defined in the extended configuration. However, the `projects` setting
_does not merge_!

## `projects`Required [​](https://moonrepo.dev/docs/config/workspace\#projects "Direct link to projects")

Defines the location of all [projects](https://moonrepo.dev/docs/concepts/project) within the workspace. Supports either a
manual map of projects (default), a list of globs in which to automatically locate projects, _or_
both.

caution

Projects that depend on each other and form a cycle must be avoided! While we do our best to avoid
an infinite loop and disconnect nodes from each other, there's no guarantee that tasks will run in
the correct order.

### Using a map [​](https://moonrepo.dev/docs/config/workspace\#using-a-map "Direct link to Using a map")

When using a map, each project must be _manually_ configured and requires a unique
[name](https://moonrepo.dev/docs/concepts/project#names) as the map key, where this name is used heavily on the command
line and within the project graph for uniquely identifying the project amongst all projects. The map
value (known as the project source) is a file system path to the project folder, relative from the
workspace root, and must be contained within the workspace boundary.

.moon/workspace.yml

```yaml
projects:
  admin: 'apps/admin'
  apiClients: 'packages/api-clients'
  designSystem: 'packages/design-system'
  web: 'apps/web'
```

### Using globs [​](https://moonrepo.dev/docs/config/workspace\#using-globs "Direct link to Using globs")

If manually mapping projects is too tedious or cumbersome, you may provide a list of
[globs](https://moonrepo.dev/docs/concepts/file-pattern#globs) to automatically locate all project folders, relative from
the workspace root.

When using this approach, the project name is derived from the project folder name, and is cleaned
to our [supported characters](https://moonrepo.dev/docs/concepts/project#names), but can be customized with the
[`id`](https://moonrepo.dev/docs/config/project#id) setting in [`moon.*`](https://moonrepo.dev/docs/config/project). Furthermore, globbing **does risk the chance**
**of collision**, and when that happens, we log a warning and skip the conflicting project from being
configured in the project graph.

.moon/workspace.yml

```yaml
projects:
  - 'apps/*'
  - 'packages/*'
  # Only shared folders with a moon configuration
  - 'shared/*/moon.yml'
```

### Using a map _and_ globs [​](https://moonrepo.dev/docs/config/workspace\#using-a-map-and-globs "Direct link to using-a-map-and-globs")

For those situations where you want to use _both_ patterns, you can! The list of globs can be
defined under a `globs` field, while the map of projects under a `sources` field.

.moon/workspace.yml

```yaml
projects:
  globs:
    - 'apps/*'
    - 'packages/*'
  sources:
    www: 'www'
```

Additionally, you can customize the format of project IDs for glob discovered projects. By default
it inherits the fodler name, but this has a high chance of collision. Instead you can configure
`globFormat` to use a different format, for example, using the full workspace relative path as the
project ID.

.moon/workspace.yml

```yaml
projects:
  globFormat: 'source-path'
  globs:
    - 'packages/**/moon.yml'
```

## `defaultProject`v2.0.0 [​](https://moonrepo.dev/docs/config/workspace\#defaultproject "Direct link to defaultproject")

Defines the default project to focus on when no project scope is specified on the command line for
task targets.

.moon/workspace.yml

```yaml
defaultProject: 'web'
```

## `codeowners`v1.8.0 [​](https://moonrepo.dev/docs/config/workspace\#codeowners "Direct link to codeowners")

Configures code owners (`CODEOWNERS`) integration across the entire workspace.

### `globalPaths` [​](https://moonrepo.dev/docs/config/workspace\#globalpaths "Direct link to globalpaths")

This setting defines file patterns and their owners at the workspace-level, and are applied to any
matching path, at any depth, within the entire workspace. This is useful for defining global or
fallback owners when a granular [project-level path](https://moonrepo.dev/docs/config/project#paths) does not match or exist.

.moon/workspace.yml

```yaml
codeowners:
  globalPaths:
    '*': ['@admins']
    'config/': ['@infra']
    '/.github/': ['@infra']
```

### `orderBy` [​](https://moonrepo.dev/docs/config/workspace\#orderby "Direct link to orderby")

The order in which code owners, grouped by project, are listed in the `CODEOWNERS` file. Accepts
"file-source" (default) or "project-id".

.moon/workspace.yml

```yaml
codeowners:
  orderBy: 'project-id'
```

### `sync` [​](https://moonrepo.dev/docs/config/workspace\#sync "Direct link to sync")

Will automatically generate a `CODEOWNERS` file by aggregating and syncing all project
[`owners`](https://moonrepo.dev/docs/config/project#owners) in the workspace when a [target is run](https://moonrepo.dev/docs/concepts/target). The format
and location of the `CODEOWNERS` file is based on the [`vcs.provider`](https://moonrepo.dev/docs/config/workspace#provider) setting. Defaults
to `false`.

.moon/workspace.yml

```yaml
codeowners:
  sync: true
```

## `constraints` [​](https://moonrepo.dev/docs/config/workspace\#constraints "Direct link to constraints")

Configures constraints between projects that are enforced during project graph generation. This is
also known as project boundaries.

### `enforceLayerRelationships` [​](https://moonrepo.dev/docs/config/workspace\#enforcelayerrelationships "Direct link to enforcelayerrelationships")

Enforces allowed relationships between a project and its dependencies based on the project's
[`layer`](https://moonrepo.dev/docs/config/project#layer) and [`stack`](https://moonrepo.dev/docs/config/project#stack) settings. When a project depends on
another project of an invalid layer, a layering violation error will be thrown when attempting to
run a task.

Layers are allowed to depend on lower layers in the same stack, but not higher layers. Additionally,
layers may depend on itself, excluding automations and applications. The following layers are
stacked as such:

| Layer | Description |
| --- | --- |
| `automation` | An automated testing suite, like E2E, integration, or visual tests. |
| `application` | An application of any kind. |
| `tool` | An internal tool, CLI, one-off script, etc. |
| `library` | A self-contained, shareable, and publishable set of code. |
| `scaffolding` | Templates or generators for scaffolding. |
| `configuration` | Configuration files or infrastructure. |
| `unknown` | When not configured. |

When the project `stack` setting is defined, it alters these rules to allow these kinds of
relationships. For example, a frontend application can depend on a backend application, but not
another frontend application.

.moon/workspace.yml

```yaml
constraints:
  enforceLayerRelationships: false
```

> Projects with an unconfigured or unknown layer are ignored during enforcement.

### `tagRelationships` [​](https://moonrepo.dev/docs/config/workspace\#tagrelationships "Direct link to tagrelationships")

Enforces allowed relationships between a project and its dependencies based on the project's
[`tags`](https://moonrepo.dev/docs/config/project#tags) setting. This works in a similar fashion to `enforceLayerRelationships`,
but gives you far more control over what these relationships look like.

For example, let's enforce that Next.js projects using the `next` tag can only depend on React
projects using the `react` tag. If a dependency does not have one of the configured required tags,
in this case `react`, an error will occur.

.moon/workspace.yml

```yaml
constraints:
  tagRelationships:
    next: ['react']
```

On the project side, we would configure [`moon.*`](https://moonrepo.dev/docs/config/project#tags) like so:

app/moon.yml

```yaml
tags: ['next']
dependsOn: ['components']
```

packages/components/moon.yml

```yaml
tags: ['react']
```

## `docker`v1.27.0 [​](https://moonrepo.dev/docs/config/workspace\#docker "Direct link to docker")

Configures Docker integration for the entire workspace.

### `prune` [​](https://moonrepo.dev/docs/config/workspace\#prune "Direct link to prune")

Configures aspects of the Docker pruning process when
[`moon docker prune`](https://moonrepo.dev/docs/commands/docker/prune) is executed.

#### `deleteVendorDirectories` [​](https://moonrepo.dev/docs/config/workspace\#deletevendordirectories "Direct link to deletevendordirectories")

Automatically delete vendor directories (package manager dependencies, build targets, etc) while
pruning. For example, `node_modules` for JavaScript, or `target` for Rust. Defaults to `true`.

.moon/workspace.yml

```yaml
docker:
  prune:
    deleteVendorDirectories: false
```

> This process happens before toolchain dependencies are installed.

#### `installToolchainDependencies` [​](https://moonrepo.dev/docs/config/workspace\#installtoolchaindependencies "Direct link to installtoolchaindependencies")

Automatically install production dependencies for all required toolchain's of the focused projects
within the Docker build. For example, `node_modules` for JavaScript. Defaults to `true`.

.moon/workspace.yml

```yaml
docker:
  prune:
    installToolchainDependencies: false
```

> This process happens after vendor directories are deleted.

### `scaffold` [​](https://moonrepo.dev/docs/config/workspace\#scaffold "Direct link to scaffold")

Configures aspects of the Docker scaffolding process when
[`moon docker scaffold`](https://moonrepo.dev/docs/commands/docker/scaffold) is executed. Only applies to the
[workspace skeleton](https://moonrepo.dev/docs/commands/docker/scaffold#workspace).

#### `configsPhaseGlobs` [​](https://moonrepo.dev/docs/config/workspace\#configsphaseglobs "Direct link to configsphaseglobs")

List of globs in which to copy additional workspace-relative files into the `.moon/docker/workspace`
skeleton. When not defined, does nothing.

.moon/workspace.yml

```yaml
docker:
  scaffold:
    configsPhaseGlobs:
      - '**/package.json'
```

## `experiments` [​](https://moonrepo.dev/docs/config/workspace\#experiments "Direct link to experiments")

Enable or disable experiments that alter core functionality.

warning

Experiments are a work in progress and may be buggy. Please report any issues you encounter!

### `asyncAffectedTracking`v2.2.0 [​](https://moonrepo.dev/docs/config/workspace\#asyncaffectedtracking "Direct link to asyncaffectedtracking")

Utilizes a new asynchronous implementation of the affected tracker that can improve performance by
100-150%. Defaults to `false`.

.moon/workspace.yml

```yaml
experiments:
  asyncAffectedTracking: true
```

Can also be enabled with the `MOON_EXPERIMENT_ASYNC_AFFECTED_TRACKING` environment variable.

### `asyncGraphBuilding`v2.2.0 [​](https://moonrepo.dev/docs/config/workspace\#asyncgraphbuilding "Direct link to asyncgraphbuilding")

Utilizes an asynchronous graph building implementation that can improve performance by 100-170% in
large workspaces. Defaults to `false`.

.moon/workspace.yml

```yaml
experiments:
  asyncGraphBuilding: true
```

Can also be enabled with the `MOON_EXPERIMENT_ASYNC_GRAPH_BUILDING` environment variable.

## `generator` [​](https://moonrepo.dev/docs/config/workspace\#generator "Direct link to generator")

Configures aspects of the template generator.

### `templates` [​](https://moonrepo.dev/docs/config/workspace\#templates "Direct link to templates")

A list of paths in which templates can be located. Supports the following types of paths, and
defaults to `./templates`.

- File system paths, relative from the workspace root.
- Git repositories and a revision, prefixed with `git://`. v1.23.0
- npm packages and a version, prefixed with `npm://`. v1.23.0

.moon/workspace.yml

```yaml
generator:
  templates:
    - './templates'
    - 'file://./other/templates'
    - 'git://github.com/moonrepo/templates#master'
    - 'npm://@moonrepo/templates#1.2.3'
```

> Learn more about this in the official
> [code generation guide](https://moonrepo.dev/docs/guides/codegen#configuring-template-locations)!

## `hasher` [​](https://moonrepo.dev/docs/config/workspace\#hasher "Direct link to hasher")

Configures aspects of the smart hashing layer.

### `ignoreMissingPatterns`v1.10.0 [​](https://moonrepo.dev/docs/config/workspace\#ignoremissingpatterns "Direct link to ignoremissingpatterns")

When [`hasher.warnOnMissingInputs`](https://moonrepo.dev/docs/config/workspace#warnonmissinginputs) is enabled, moon will log a warning to the
terminal that an input is missing. This is useful for uncovering misconfigurations, but can be quite
noisy when inputs are truly optional.

To ignore warnings for missing inputs, a list of [glob patterns](https://moonrepo.dev/docs/concepts/file-pattern#globs) can
be configured to filter and ignore files. Files are matched against workspace relative paths, so
prefixing patterns with `**/` is suggested.

Defaults to `**/.env` and `**/.env.*` but will be overwritten when configured.

.moon/workspace.yml

```yaml
hasher:
  ignoreMissingPatterns:
    - '**/.eslintrc.*'
    - '**/*.config.*'
```

### `ignorePatterns`v1.10.0 [​](https://moonrepo.dev/docs/config/workspace\#ignorepatterns "Direct link to ignorepatterns")

A list of [glob patterns](https://moonrepo.dev/docs/concepts/file-pattern#globs) used to filter and ignore files during the
inputs hashing process. Files are matched against workspace relative paths, so prefixing patterns
with `**/` is suggested.

.moon/workspace.yml

```yaml
hasher:
  ignorePatterns:
    - '**/*.png'
```

### `optimization` [​](https://moonrepo.dev/docs/config/workspace\#optimization "Direct link to optimization")

Determines the optimization level to utilize when hashing content before running targets.

- `accuracy` (default) - When hashing dependency versions, utilize the resolved value in the
lockfile. This requires parsing the lockfile, which may reduce performance.
- `performance` \- When hashing dependency versions, utilize the value defined in the manifest. This
is typically a version range or requirement.

.moon/workspace.yml

```yaml
hasher:
  optimization: 'performance'
```

### `walkStrategy` [​](https://moonrepo.dev/docs/config/workspace\#walkstrategy "Direct link to walkstrategy")

Defines the file system walking strategy to utilize when discovering inputs to hash.

- `glob` \- Walks the file system using glob patterns.
- `vcs` (default) - Calls out to the [VCS](https://moonrepo.dev/docs/config/workspace#vcs) to extract files from its working tree.

.moon/workspace.yml

```yaml
hasher:
  walkStrategy: 'glob'
```

### `warnOnMissingInputs` [​](https://moonrepo.dev/docs/config/workspace\#warnonmissinginputs "Direct link to warnonmissinginputs")

When enabled, will log warnings to the console when attempting to hash an input that does not exist.
This is useful in uncovering misconfigured tasks. Defaults to `true`.

.moon/workspace.yml

```yaml
hasher:
  warnOnMissingInputs: false
```

## `notifier` [​](https://moonrepo.dev/docs/config/workspace\#notifier "Direct link to notifier")

Configures how moon notifies and interacts with a developer or an external system.

### `terminalNotifications`v1.38.0 [​](https://moonrepo.dev/docs/config/workspace\#terminalnotifications "Direct link to terminalnotifications")

When defined, will display OS notifications for action pipeline events when running commands from a
terminal. Supports the following values:

- `always` \- Display on pipeline success and failure.
- `failure` \- Display on pipeline failure only.
- `success` \- Display on pipeline success only.
- `task-failure` \- Display for each task failure.

.moon/workspace.yml

```yaml
notifier:
  terminalNotifications: 'always'
```

### `webhookUrl` [​](https://moonrepo.dev/docs/config/workspace\#webhookurl "Direct link to webhookurl")

Defines an HTTPS URL that all pipeline events will be posted to. View the
[webhooks guide for more information](https://moonrepo.dev/docs/guides/webhooks) on available events.

.moon/workspace.yml

```yaml
notifier:
  webhookUrl: 'https://api.company.com/some/endpoint'
```

### `acknowledge` [​](https://moonrepo.dev/docs/config/workspace\#acknowledge "Direct link to acknowledge")

When enabled, webhook notifier will wait for request result and validates the return code for 2xx.
Defaults to `false`.

warning

Activating this setting will slow down your pipeline, because every webhook request will be
evaluated!

.moon/workspace.yml

```yaml
notifier:
  webhookUrl: 'https://api.company.com/some/endpoint'
  webhookAcknowledge: true
```

## `pipeline` [​](https://moonrepo.dev/docs/config/workspace\#pipeline "Direct link to pipeline")

Configures aspects of task running and the action pipeline.

### `autoCleanCache`v1.24.0 [​](https://moonrepo.dev/docs/config/workspace\#autocleancache "Direct link to autocleancache")

Automatically cleans cached artifacts older than [`cacheLifetime`](https://moonrepo.dev/docs/config/workspace#cachelifetime) from the cache
directory (`.moon/cache`) after every run. This is useful for keeping the cache directory lean.
Defaults to `true`.

.moon/workspace.yml

```yaml
pipeline:
  autoCleanCache: false
```

### `cacheLifetime` [​](https://moonrepo.dev/docs/config/workspace\#cachelifetime "Direct link to cachelifetime")

The maximum lifetime of cached artifacts before they're marked as stale and automatically removed by
the action pipeline. Defaults to "7 days". This field requires an integer and a timeframe unit that
can be [parsed as a duration](https://docs.rs/humantime/2.1.0/humantime/fn.parse_duration.html).

.moon/workspace.yml

```yaml
pipeline:
  cacheLifetime: '24 hours'
```

### `inheritColorsForPipedTasks` [​](https://moonrepo.dev/docs/config/workspace\#inheritcolorsforpipedtasks "Direct link to inheritcolorsforpipedtasks")

Force colors to be inherited from the current terminal for all tasks that are ran as a child process
and their output is piped to the action pipeline. Defaults to `true`.
[View more about color handling in moon](https://moonrepo.dev/docs/commands/overview#colors).

.moon/workspace.yml

```yaml
pipeline:
  inheritColorsForPipedTasks: true
```

### `installDependencies`v1.34.0 [​](https://moonrepo.dev/docs/config/workspace\#installdependencies "Direct link to installdependencies")

When enabled, runs the
[`InstallWorkspaceDeps` and `InstallProjectDeps` actions](https://moonrepo.dev/docs/how-it-works/action-graph#install-dependencies)
within the pipeline before running an applicable task. Installation is determined based on changed
manifests and lockfiles. Defaults to `true`.

.moon/workspace.yml

```yaml
pipeline:
  installDependencies: false
```

Instead of a boolean, a list of toolchain IDs can be provided to only allow those toolchains to
install dependencies.

.moon/workspace.yml

```yaml
pipeline:
  installDependencies: ['node']
```

### `killProcessThreshold`v1.32.1 [​](https://moonrepo.dev/docs/config/workspace\#killprocessthreshold "Direct link to killprocessthreshold")

Threshold in milliseconds in which to force kill running child processes after the pipeline receives
an external signal (like `SIGINT` or `SIGTERM`). A value of 0 will not kill the process and let them
run to completion. Defaults to `2000` (2 seconds).

.moon/workspace.yml

```yaml
pipeline:
  killProcessThreshold: 5000
```

### `logRunningCommand` [​](https://moonrepo.dev/docs/config/workspace\#logrunningcommand "Direct link to logrunningcommand")

When enabled, will log the task's command, resolved arguments, and working directory when a target
is ran. Defaults to `false`.

.moon/workspace.yml

```yaml
pipeline:
  logRunningCommand: true
```

### `syncProjects`v1.34.0 [​](https://moonrepo.dev/docs/config/workspace\#syncprojects "Direct link to syncprojects")

When enabled, runs the [`SyncProject` action](https://moonrepo.dev/docs/how-it-works/action-graph#sync-project) within the
pipeline before running an applicable task. Defaults to `true`.

.moon/workspace.yml

```yaml
pipeline:
  syncProjects: false
```

Instead of a boolean, a list of project IDs can be provided to only sync those projects.

.moon/workspace.yml

```yaml
pipeline:
  syncProjects: ['app']
```

> The [`moon sync projects`](https://moonrepo.dev/docs/commands/sync/projects) command can be executed to manually sync
> projects.

### `syncWorkspace`v1.34.0 [​](https://moonrepo.dev/docs/config/workspace\#syncworkspace "Direct link to syncworkspace")

When enabled, runs the [`SyncWorkspace` action](https://moonrepo.dev/docs/how-it-works/action-graph#sync-workspace) within
the pipeline before all other actions. This syncing includes operations such as codeowners, VCS
hooks, and more. Defaults to `true`.

.moon/workspace.yml

```yaml
pipeline:
  syncWorkspace: false
```

> The [`moon sync ...`](https://moonrepo.dev/docs/commands/sync) sub-commands can be executed to manually sync features.

## `remote`v1.30.0 [​](https://moonrepo.dev/docs/config/workspace\#remote "Direct link to remote")

Configures a remote service, primarily for cloud-based caching of artifacts. Learn more about this
in the [remote caching](https://moonrepo.dev/docs/guides/remote-cache) guide.

### `api`v1.32.0 [​](https://moonrepo.dev/docs/config/workspace\#api "Direct link to api")

The API format of the remote server. This format dictates which type of client moon uses for
communicating with. Supports the following:

- `grpc` (default) - Uses the gRPC API: [https://github.com/bazelbuild/remote-apis](https://github.com/bazelbuild/remote-apis)
- `http` \- Uses the HTTP API: [https://bazel.build/remote/caching#http-caching](https://bazel.build/remote/caching#http-caching)

.moon/workspace.yml

```yaml
remote:
  api: 'grpc'
```

### `auth`v1.32.0 [​](https://moonrepo.dev/docs/config/workspace\#auth "Direct link to auth")

Configures authorization and authentication level features of our remote clients.

#### `headers`v1.32.0 [​](https://moonrepo.dev/docs/config/workspace\#headers "Direct link to headers")

A mapping of HTTP headers to include in all requests to the remote server. These headers are applied
to all [API formats and protocols](https://moonrepo.dev/docs/config/workspace#api), not just HTTP.

.moon/workspace.yml

```yaml
remote:
  auth:
    headers:
      'X-Custom-Header': 'value'
```

#### `token`v1.32.0 [​](https://moonrepo.dev/docs/config/workspace\#token "Direct link to token")

The name of an environment variable in which to extract a token for
[Bearer HTTP authorization](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/).
An `Authorization` HTTP header will be included in all requests to the remote server.

If the token does not exist, or is not enabled, remote caching will be disabled.

.moon/workspace.yml

```yaml
remote:
  auth:
    token: 'ENV_VAR_NAME'
```

### `cache` [​](https://moonrepo.dev/docs/config/workspace\#cache "Direct link to cache")

Configures aspects of the caching layer, primarily the action cache (AC) and content addressable
cache (CAS).

#### `compression`v1.31.0 [​](https://moonrepo.dev/docs/config/workspace\#compression "Direct link to compression")

The compression format to use when uploading/downloading blobs. Supports `none` and `zstd`, and
defaults to no compression (`identity` format in RE API).

.moon/workspace.yml

```yaml
remote:
  cache:
    compression: 'zstd'
```

info

Compression is only applied to gRPC based APIs, not HTTP.

#### `instanceName` [​](https://moonrepo.dev/docs/config/workspace\#instancename "Direct link to instancename")

A
[unique identifier](https://github.com/bazelbuild/remote-apis/blob/main/build/bazel/remote/execution/v2/remote_execution.proto#L223)
used to distinguish between the various instances on the host. This allows the same remote service
to serve and partition multiple moon repositories. Defaults to `moon-outputs`.

.moon/workspace.yml

```yaml
remote:
  cache:
    instanceName: 'custom-dir-name'
```

> We suggest changing the instance name to the name of your repository!

#### `localReadOnly`v1.40.0 [​](https://moonrepo.dev/docs/config/workspace\#localreadonly "Direct link to localreadonly")

When enabled and developing locally, existing remote blobs will only be downloaded, but new local
blobs will _not_ be uploaded. Blobs will only be uploaded in CI environments.

.moon/workspace.yml

```yaml
remote:
  cache:
    localReadOnly: true
```

#### `verifyIntegrity`v1.36.0 [​](https://moonrepo.dev/docs/config/workspace\#verifyintegrity "Direct link to verifyintegrity")

When downloading blobs, verify the digests/hashes in the response match the associated blob
contents. This will reduce performance but ensure partial or corrupted blobs won't cause failures.
Defaults to `false`.

.moon/workspace.yml

```yaml
remote:
  cache:
    verifyIntegrity: true
```

### `host` [​](https://moonrepo.dev/docs/config/workspace\#host "Direct link to host")

The host URL to communicate with when uploading and downloading artifacts. Supports both
`grpc(s)://` and `http(s)://` protocols. This field is required!

.moon/workspace.yml

```yaml
remote:
  host: 'grpcs://your-host.com:9092'
```

### `mtls` [​](https://moonrepo.dev/docs/config/workspace\#mtls "Direct link to mtls")

Connect to the host using server and client authentication with mTLS. This takes precedence over
normal TLS.

.moon/workspace.yml

```yaml
remote:
  # ...
  mtls:
    caCert: 'certs/ca.pem'
    clientCert: 'certs/client.pem'
    clientKey: 'certs/client.key'
    domain: 'your-host.com'
```

#### `assumeHttp2` [​](https://moonrepo.dev/docs/config/workspace\#assumehttp2 "Direct link to assumehttp2")

If true, assume that the host supports HTTP/2, even if it doesn't provide protocol negotiation via
ALPN.

#### `caCert` [​](https://moonrepo.dev/docs/config/workspace\#cacert "Direct link to cacert")

A file path, relative from the workspace root, to the certificate authority PEM encoded X509
certificate (typically `ca.pem`).

#### `clientCert` [​](https://moonrepo.dev/docs/config/workspace\#clientcert "Direct link to clientcert")

A file path, relative from the workspace root, to the client's PEM encoded X509 certificate
(typically `client.pem`).

#### `clientKey` [​](https://moonrepo.dev/docs/config/workspace\#clientkey "Direct link to clientkey")

A file path, relative from the workspace root, to the client's PEM encoded X509 private key
(typically `client.key`).

#### `domain` [​](https://moonrepo.dev/docs/config/workspace\#domain "Direct link to domain")

The domain name in which to verify the TLS certificate.

### `tls` [​](https://moonrepo.dev/docs/config/workspace\#tls "Direct link to tls")

Connect to the host using server-only authentication with TLS.

.moon/workspace.yml

```yaml
remote:
  # ...
  tls:
    cert: 'certs/ca.pem'
    domain: 'your-host.com'
```

#### `assumeHttp2` [​](https://moonrepo.dev/docs/config/workspace\#assumehttp2-1 "Direct link to assumehttp2-1")

If true, assume that the host supports HTTP/2, even if it doesn't provide protocol negotiation via
ALPN.

#### `cert` [​](https://moonrepo.dev/docs/config/workspace\#cert "Direct link to cert")

A file path, relative from the workspace root, to the certificate authority PEM encoded X509
certificate (typically `ca.pem`).

#### `domain` [​](https://moonrepo.dev/docs/config/workspace\#domain-1 "Direct link to domain-1")

The domain name in which to verify the TLS certificate.

## `telemetry` [​](https://moonrepo.dev/docs/config/workspace\#telemetry "Direct link to telemetry")

When enabled, will check for a newer moon version and send anonymous usage data to the moonrepo
team. This data is used to improve the quality and reliability of the tool. Defaults to `true`.

.moon/workspace.yml

```yaml
telemetry: false
```

## `vcs` [​](https://moonrepo.dev/docs/config/workspace\#vcs "Direct link to vcs")

Configures the version control system to utilize within the workspace (and repository). A VCS is
required for determining touched (added, modified, etc) files, calculating file hashes, computing
affected files, and much more.

### `defaultBranch` [​](https://moonrepo.dev/docs/config/workspace\#defaultbranch "Direct link to defaultbranch")

Defines the default branch in the repository for comparing differences against. For git, this is
typically "master" (default) or "main".

.moon/workspace.yml

```yaml
vcs:
  defaultBranch: 'master'
```

### `hooks`v1.9.0 [​](https://moonrepo.dev/docs/config/workspace\#hooks "Direct link to hooks")

Defines a mapping of hooks to a list of commands to run when that event is triggered. There are no
restrictions to what commands can be run, but the binaries for each command must exist on each
machine that will be running hooks.

For Git, each [hook name](https://git-scm.com/docs/githooks#_hooks) must be a valid kebab-cased
name. [Learn more about Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

.moon/workspace.yml

```yaml
vcs:
  hooks:
    pre-commit:
      - 'moon run :lint :format --affected --status=staged --no-bail'
      - 'another-command'
```

info

If running `moon` commands directly, the `moon` binary must be installed globally!

### `hookFormat`v1.29.0 [​](https://moonrepo.dev/docs/config/workspace\#hookformat "Direct link to hookformat")

The shell and file type in which generated hook files are formatted with. Supports the following:

- `native` (default) - The format native to the current operating system. Bash on Unix, and
PowerShell on Windows.
- `bash` \- Forces the format to Bash for all operating systems.

.moon/workspace.yml

```yaml
vcs:
  hookFormat: 'bash'
```

### `client` [​](https://moonrepo.dev/docs/config/workspace\#client "Direct link to client")

Defines the VCS tool/binary that is being used for managing the repository. Accepts "git" (default).
Expect more version control systems in the future!

.moon/workspace.yml

```yaml
vcs:
  client: 'git'
```

### `provider`v1.8.0 [​](https://moonrepo.dev/docs/config/workspace\#provider "Direct link to provider")

Defines the service provider that the repository is hosted on. Accepts "github" (default), "gitlab",
"bitbucket", or "other".

.moon/workspace.yml

```yaml
vcs:
  provider: 'github'
```

### `remoteCandidates` [​](https://moonrepo.dev/docs/config/workspace\#remotecandidates "Direct link to remotecandidates")

(Git only) Defines a list of remote candidates to query against to determine merge bases. Defaults
to "origin" and "upstream".

.moon/workspace.yml

```yaml
vcs:
  remoteCandidates:
    - 'origin'
    - 'upstream'
```

### `sync`v1.9.0 [​](https://moonrepo.dev/docs/config/workspace\#sync-1 "Direct link to sync-1")

Will automatically generate [hook scripts](https://moonrepo.dev/docs/config/workspace#hooks) to `.moon/hooks` and sync the scripts to the
local VCS checkout. The hooks format and location is based on the [`vcs.client`](https://moonrepo.dev/docs/config/workspace#client) setting.
Defaults to `false`.

.moon/workspace.yml

```yaml
vcs:
  hooks:
    # ...
  sync: true
```

caution

When enabled, this will sync hooks for _all_ users of the repository. For personal or small
projects, this may be fine, but for larger projects, this may be undesirable and disruptive!

## `versionConstraint` [​](https://moonrepo.dev/docs/config/workspace\#versionconstraint "Direct link to versionconstraint")

Defines a version requirement for the currently running moon binary. This provides a mechanism for
enforcing that the globally installed moon on every developers machine is using an applicable
version.

.moon/workspace.yml

```yaml
versionConstraint: '>=0.20.0'
```

- [`extends`](https://moonrepo.dev/docs/config/workspace#extends)
- [`projects`](https://moonrepo.dev/docs/config/workspace#projects)
  - [Using a map](https://moonrepo.dev/docs/config/workspace#using-a-map)
  - [Using globs](https://moonrepo.dev/docs/config/workspace#using-globs)
  - [Using a map _and_ globs](https://moonrepo.dev/docs/config/workspace#using-a-map-and-globs)
- [`defaultProject`](https://moonrepo.dev/docs/config/workspace#defaultproject)
- [`codeowners`](https://moonrepo.dev/docs/config/workspace#codeowners)
  - [`globalPaths`](https://moonrepo.dev/docs/config/workspace#globalpaths)
  - [`orderBy`](https://moonrepo.dev/docs/config/workspace#orderby)
  - [`sync`](https://moonrepo.dev/docs/config/workspace#sync)
- [`constraints`](https://moonrepo.dev/docs/config/workspace#constraints)
  - [`enforceLayerRelationships`](https://moonrepo.dev/docs/config/workspace#enforcelayerrelationships)
  - [`tagRelationships`](https://moonrepo.dev/docs/config/workspace#tagrelationships)
- [`docker`](https://moonrepo.dev/docs/config/workspace#docker)
  - [`prune`](https://moonrepo.dev/docs/config/workspace#prune)
    - [`deleteVendorDirectories`](https://moonrepo.dev/docs/config/workspace#deletevendordirectories)
    - [`installToolchainDependencies`](https://moonrepo.dev/docs/config/workspace#installtoolchaindependencies)
  - [`scaffold`](https://moonrepo.dev/docs/config/workspace#scaffold)
    - [`configsPhaseGlobs`](https://moonrepo.dev/docs/config/workspace#configsphaseglobs)
- [`experiments`](https://moonrepo.dev/docs/config/workspace#experiments)
  - [`asyncAffectedTracking`](https://moonrepo.dev/docs/config/workspace#asyncaffectedtracking)
  - [`asyncGraphBuilding`](https://moonrepo.dev/docs/config/workspace#asyncgraphbuilding)
- [`generator`](https://moonrepo.dev/docs/config/workspace#generator)
  - [`templates`](https://moonrepo.dev/docs/config/workspace#templates)
- [`hasher`](https://moonrepo.dev/docs/config/workspace#hasher)
  - [`ignoreMissingPatterns`](https://moonrepo.dev/docs/config/workspace#ignoremissingpatterns)
  - [`ignorePatterns`](https://moonrepo.dev/docs/config/workspace#ignorepatterns)
  - [`optimization`](https://moonrepo.dev/docs/config/workspace#optimization)
  - [`walkStrategy`](https://moonrepo.dev/docs/config/workspace#walkstrategy)
  - [`warnOnMissingInputs`](https://moonrepo.dev/docs/config/workspace#warnonmissinginputs)
- [`notifier`](https://moonrepo.dev/docs/config/workspace#notifier)
  - [`terminalNotifications`](https://moonrepo.dev/docs/config/workspace#terminalnotifications)
  - [`webhookUrl`](https://moonrepo.dev/docs/config/workspace#webhookurl)
  - [`acknowledge`](https://moonrepo.dev/docs/config/workspace#acknowledge)
- [`pipeline`](https://moonrepo.dev/docs/config/workspace#pipeline)
  - [`autoCleanCache`](https://moonrepo.dev/docs/config/workspace#autocleancache)
  - [`cacheLifetime`](https://moonrepo.dev/docs/config/workspace#cachelifetime)
  - [`inheritColorsForPipedTasks`](https://moonrepo.dev/docs/config/workspace#inheritcolorsforpipedtasks)
  - [`installDependencies`](https://moonrepo.dev/docs/config/workspace#installdependencies)
  - [`killProcessThreshold`](https://moonrepo.dev/docs/config/workspace#killprocessthreshold)
  - [`logRunningCommand`](https://moonrepo.dev/docs/config/workspace#logrunningcommand)
  - [`syncProjects`](https://moonrepo.dev/docs/config/workspace#syncprojects)
  - [`syncWorkspace`](https://moonrepo.dev/docs/config/workspace#syncworkspace)
- [`remote`](https://moonrepo.dev/docs/config/workspace#remote)
  - [`api`](https://moonrepo.dev/docs/config/workspace#api)
  - [`auth`](https://moonrepo.dev/docs/config/workspace#auth)
    - [`headers`](https://moonrepo.dev/docs/config/workspace#headers)
    - [`token`](https://moonrepo.dev/docs/config/workspace#token)
  - [`cache`](https://moonrepo.dev/docs/config/workspace#cache)
    - [`compression`](https://moonrepo.dev/docs/config/workspace#compression)
    - [`instanceName`](https://moonrepo.dev/docs/config/workspace#instancename)
    - [`localReadOnly`](https://moonrepo.dev/docs/config/workspace#localreadonly)
    - [`verifyIntegrity`](https://moonrepo.dev/docs/config/workspace#verifyintegrity)
  - [`host`](https://moonrepo.dev/docs/config/workspace#host)
  - [`mtls`](https://moonrepo.dev/docs/config/workspace#mtls)
    - [`assumeHttp2`](https://moonrepo.dev/docs/config/workspace#assumehttp2)
    - [`caCert`](https://moonrepo.dev/docs/config/workspace#cacert)
    - [`clientCert`](https://moonrepo.dev/docs/config/workspace#clientcert)
    - [`clientKey`](https://moonrepo.dev/docs/config/workspace#clientkey)
    - [`domain`](https://moonrepo.dev/docs/config/workspace#domain)
  - [`tls`](https://moonrepo.dev/docs/config/workspace#tls)
    - [`assumeHttp2`](https://moonrepo.dev/docs/config/workspace#assumehttp2-1)
    - [`cert`](https://moonrepo.dev/docs/config/workspace#cert)
    - [`domain`](https://moonrepo.dev/docs/config/workspace#domain-1)
- [`telemetry`](https://moonrepo.dev/docs/config/workspace#telemetry)
- [`vcs`](https://moonrepo.dev/docs/config/workspace#vcs)
  - [`defaultBranch`](https://moonrepo.dev/docs/config/workspace#defaultbranch)
  - [`hooks`](https://moonrepo.dev/docs/config/workspace#hooks)
  - [`hookFormat`](https://moonrepo.dev/docs/config/workspace#hookformat)
  - [`client`](https://moonrepo.dev/docs/config/workspace#client)
  - [`provider`](https://moonrepo.dev/docs/config/workspace#provider)
  - [`remoteCandidates`](https://moonrepo.dev/docs/config/workspace#remotecandidates)
  - [`sync`](https://moonrepo.dev/docs/config/workspace#sync-1)
- [`versionConstraint`](https://moonrepo.dev/docs/config/workspace#versionconstraint)