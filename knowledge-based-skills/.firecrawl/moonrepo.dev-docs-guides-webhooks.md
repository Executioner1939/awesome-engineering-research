[Skip to main content](https://moonrepo.dev/docs/guides/webhooks#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Looking to gather metrics for your pipelines? Gain insight into run durations and failures? Maybe
you want to send Slack or Discord notifications? With our webhooks, all of these are possible!

When the [`notifier.webhookUrl`](https://moonrepo.dev/docs/config/workspace#webhookurl) setting is configured with an HTTPS
URL, and moon is running in a CI environment, moon will POST a payload to this endpoint for every
event in our pipeline.

## Payload structure [​](https://moonrepo.dev/docs/guides/webhooks\#payload-structure "Direct link to Payload structure")

Every webhook event is posted with the following request body, known as a payload.

- `type` (`string`) \- The type of [event](https://moonrepo.dev/docs/guides/webhooks#events).
- `environment` (`object | null`) \- Information about the current CI/CD pipeline environment.
- `event` (`object`) \- The event specific payload. View each event for an example of their
structure.
- `createdAt` (`string`) \- When the event was created, as a UTC timestamp in ISO 8601 (RFC 3339)
format.
- `uuid` (`string`) \- A unique identifier for all webhooks in the current run batch.
- `trace` (`string`) \- A unique identifier for all webhooks in the overall run batch. Can be defined
via `MOON_TRACE_ID` environment variable.

```json
{
  "type": "...",
  "environment": "...",
  "event": {
    // ...
  },
  "createdAt": "...",
  "uuid": "...",
  "trace": "..."
}
```

> The `uuid` field can be used to differentiate concurrently running pipelines!

### Pipeline environment [​](https://moonrepo.dev/docs/guides/webhooks\#pipeline-environment "Direct link to Pipeline environment")

When webhooks are sent from a CI/CD pipeline, we attempt to include information about the
environment under the `environment` field. If information could not be detected, this field is null,
otherwise it contains these fields.

- `baseBranch` (`string | null`) \- When a merge/pull request, the target (base) branch, otherwise
null.
- `branch` (`string`) \- When a merge/pull request, the source (head) branch, otherwise the
triggering branch.
- `id` (`string`) \- ID of the current pipeline instance.
- `provider` (`string`) \- Name of your CI/CD provider. GitHub Actions, GitLab, CircleCI, etc.
- `requestId` (`string | null`) \- The ID of the merge/pull request.
- `requestUrl` (`string | null`) \- Link to the merge/pull request.
- `revision` (`string`) \- The HEAD commit, revision, tag, ref, etc, that triggered the pipeline.
- `url` (`string | null`) \- Link to the current pipeline, when available.

## Events [​](https://moonrepo.dev/docs/guides/webhooks\#events "Direct link to Events")

### Pipeline [​](https://moonrepo.dev/docs/guides/webhooks\#pipeline "Direct link to Pipeline")

Runs actions within moon using a robust dependency graph. Is triggered when using
[`moon run`](https://moonrepo.dev/docs/commands/run).

### `pipeline.started` [​](https://moonrepo.dev/docs/guides/webhooks\#pipelinestarted "Direct link to pipelinestarted")

Triggered when the pipeline has been created but before actions have started to run.

This event includes the number of actions registered within the pipeline, but does not provide
detailed information about the actions. Use the [`action.*`](https://moonrepo.dev/docs/guides/webhooks#actionstarted) events for this.

```json
{
  "type": "pipeline.started",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "actionsCount": 15
  },
  "uuid": "..."
}
```

### `pipeline.finished` [​](https://moonrepo.dev/docs/guides/webhooks\#pipelinefinished "Direct link to pipelinefinished")

Triggered when the pipeline has finished running all actions, with aggregated counts based on final
status.

This event is _not_ triggered if the pipeline crashes (this does not include actions that have
failed, as those are legitimate runs). Use the [`pipeline.aborted`](https://moonrepo.dev/docs/guides/webhooks#pipelineaborted) event if you
want to also catch crashes.

```json
{
  "type": "pipeline.finished",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "cachedCount": 10,
    "baselineDuration": {
      "secs": 60,
      "nanos": 3591693
    },
    "duration": {
      "secs": 120,
      "nanos": 3591693
    },
    "estimatedSavings": {
      "secs": 60,
      "nanos": 0
    },
    "failedCount": 1,
    "passedCount": 4
  },
  "uuid": "..."
}
```

### `pipeline.aborted` [​](https://moonrepo.dev/docs/guides/webhooks\#pipelineaborted "Direct link to pipelineaborted")

Triggered when the pipeline has crashed for unknown reasons, or had to abort as a result of a
critical action failing.

```json
{
  "type": "pipeline.aborted",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "error": "..."
  },
  "uuid": "..."
}
```

### Actions [​](https://moonrepo.dev/docs/guides/webhooks\#actions "Direct link to Actions")

Actions are "jobs" within the pipeline that are executed topologically.

### `action.started` [​](https://moonrepo.dev/docs/guides/webhooks\#actionstarted "Direct link to actionstarted")

Triggered when an action within the pipeline has started to run.

```json
{
  "type": "action.started",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "action": {
      "attempts": null,
      "createdAt": "...",
      "duration": {
        "secs": 0,
        "nanos": 3591693
      },
      "error": null,
      "label": "InstallWorkspaceDeps(node:18.0.0)",
      "nodeIndex": 5,
      "status": "passed"
    },
    "node": {
      "action": "InstallDeps",
      "params": [\
        {\
          "toolchain": "Node",\
          "version": "18.0.0"\
        }\
      ]
    }
  },
  "uuid": "..."
}
```

### `action.finished` [​](https://moonrepo.dev/docs/guides/webhooks\#actionfinished "Direct link to actionfinished")

Triggered when an action within the pipeline has finished running, either with a success or failure.
If the action failed, the `error` field will be set with the error message.

```json
{
  "type": "action.finished",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "action": {
      "attempts": null,
      "createdAt": "...",
      "duration": {
        "secs": 0,
        "nanos": 3591693
      },
      "error": null,
      "label": "InstallWorkspaceDeps(node:18.0.0)",
      "nodeIndex": 5,
      "status": "passed"
    },
    "error": null,
    "node": {
      "action": "InstallDeps",
      "params": {
        "toolchain": "Node",
        "version": "18.0.0"
      }
    }
  },
  "uuid": "..."
}
```

### `dependencies.installing` [​](https://moonrepo.dev/docs/guides/webhooks\#dependenciesinstalling "Direct link to dependenciesinstalling")

Triggered when dependencies for a workspace or project have started to install. When targeting a
project, the `project` field will be set, otherwise `null` for the entire workspace.

```json
{
  "type": "dependencies.installing",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "project": {
      "id": "server"
      // ...
    },
    "runtime": {
      "toolchain": "Node",
      "version": "18.0.0"
    },
    "root": ".",
    "toolchain": "node"
  },
  "uuid": "..."
}
```

### `dependencies.installed` [​](https://moonrepo.dev/docs/guides/webhooks\#dependenciesinstalled "Direct link to dependenciesinstalled")

Triggered when dependencies for a workspace or project have finished installing. When targeting a
project, the `project` field will be set, otherwise `null` for the entire workspace. If the install
failed, the `error` field will be set with the error message.

For more information about the action, refer to the [`action.finished`](https://moonrepo.dev/docs/guides/webhooks#actionfinished) event.
Installed deps can be scoped with the `InstallDeps(...)` labels.

```json
{
  "type": "dependencies.installed",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "error": null,
    "project": null,
    "runtime": {
      "toolchain": "Node",
      "version": "18.0.0"
    },
    "root": ".",
    "toolchain": "node"
  },
  "uuid": "..."
}
```

### `environment.initializing`v1.37.0 [​](https://moonrepo.dev/docs/guides/webhooks\#environmentinitializing "Direct link to environmentinitializing")

Triggered when an environment is being setup for a toolchain. When targeting a project, the
`project` field will be set, otherwise `null` for the entire workspace.

```json
{
  "type": "environment.initializing",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "project": {
      "id": "server"
      // ...
    },
    "root": ".",
    "toolchain": "node"
  },
  "uuid": "..."
}
```

### `environment.initialized`v1.37.0 [​](https://moonrepo.dev/docs/guides/webhooks\#environmentinitialized "Direct link to environmentinitialized")

Triggered when an environment has been setup for a toolchain. When targeting a project, the
`project` field will be set, otherwise `null` for the entire workspace. If setup failed, the `error`
field will be set with the error message.

For more information about the action, refer to the [`action.finished`](https://moonrepo.dev/docs/guides/webhooks#actionfinished) event.
Installed deps can be scoped with the `SetupEnvironment(...)` labels.

```json
{
  "type": "environment.initialized",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "error": null,
    "project": null,
    "root": ".",
    "toolchain": "node"
  },
  "uuid": "..."
}
```

### `project.syncing` [​](https://moonrepo.dev/docs/guides/webhooks\#projectsyncing "Direct link to projectsyncing")

Triggered when an affected project has started syncing its workspace state. This occurs
automatically before a project's task is ran.

```json
{
  "type": "project.syncing",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "project": {
      "id": "client"
      // ...
    },
    "runtime": {
      "toolchain": "Node",
      "version": "18.0.0"
    }
  },
  "uuid": "..."
}
```

### `project.synced` [​](https://moonrepo.dev/docs/guides/webhooks\#projectsynced "Direct link to projectsynced")

Triggered when an affected project has finished syncing. If the sync failed, the `error` field will
be set with the error message.

For more information about the action, refer to the [`action.finished`](https://moonrepo.dev/docs/guides/webhooks#actionfinished) event.
Synced projects can be scoped with the `SyncProject(...)` labels.

```json
{
  "type": "project.synced",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "error": null,
    "project": {
      "id": "client"
      // ...
    },
    "runtime": {
      "toolchain": "Node",
      "version": "18.0.0"
    }
  },
  "uuid": "..."
}
```

### `toolchain.installing` [​](https://moonrepo.dev/docs/guides/webhooks\#toolchaininstalling "Direct link to toolchaininstalling")

Triggered when a toolchain plugin has started downloading and installing.

This event is _always_ triggered, regardless of whether the tool has already been installed or not.
For an accurate state, use the [`action.finished`](https://moonrepo.dev/docs/guides/webhooks#actionfinished) event. If the `status` is
"skipped", then the tool was already installed.

```json
{
  "type": "toolchain.installing",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "spec": {
      "id": "node",
      "req": "18.0.0"
    }
  },
  "uuid": "..."
}
```

### `toolchain.installed` [​](https://moonrepo.dev/docs/guides/webhooks\#toolchaininstalled "Direct link to toolchaininstalled")

Triggered when a toolchain plugin has finished installing. If the install failed, the `error` field
will be set with the error message.

For more information about the action, refer to the [`action.finished`](https://moonrepo.dev/docs/guides/webhooks#actionfinished) event.
Tools can be scoped with the `SetupToolchain(...)` labels.

```json
{
  "type": "toolchain.installed",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "error": null,
    "spec": {
      "id": "node",
      "req": "18.0.0"
    }
  },
  "uuid": "..."
}
```

### `task.running` [​](https://moonrepo.dev/docs/guides/webhooks\#taskrunning "Direct link to taskrunning")

Triggered when a [task](https://moonrepo.dev/docs/concepts/task) has started to run (via [`moon run`](https://moonrepo.dev/docs/commands/run) or
similar command).

```json
{
  "type": "task.running",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "target": "app:build"
  },
  "uuid": "..."
}
```

### `task.ran` [​](https://moonrepo.dev/docs/guides/webhooks\#taskran "Direct link to taskran")

Triggered when a [task](https://moonrepo.dev/docs/concepts/task) has finished running. If the run failed, the `error` field
will be set with the error message.

For more information about the action, refer to the [`action.finished`](https://moonrepo.dev/docs/guides/webhooks#actionfinished) event. Ran
tasks can be scoped with the `RunTask(...)`, `RunInteractiveTask(...)`, and `RunPersistentTask(...)`
labels.

```json
{
  "type": "task.ran",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "error": null,
    "target": "app:build"
  },
  "uuid": "..."
}
```

### `workspace.syncing` [​](https://moonrepo.dev/docs/guides/webhooks\#workspacesyncing "Direct link to workspacesyncing")

Triggered when the workspace is being synced.

```json
{
  "type": "workspace.syncing",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "target": "app:build"
  },
  "uuid": "..."
}
```

### `workspace.synced` [​](https://moonrepo.dev/docs/guides/webhooks\#workspacesynced "Direct link to workspacesynced")

Triggered when the workspace has finished syncing. If the action failed, the `error` field will be
set with the error message.

```json
{
  "type": "workspace.synced",
  "createdAt": "...",
  "environment": "...",
  "event": {
    "error": null
  },
  "uuid": "..."
}
```

- [Payload structure](https://moonrepo.dev/docs/guides/webhooks#payload-structure)
  - [Pipeline environment](https://moonrepo.dev/docs/guides/webhooks#pipeline-environment)
- [Events](https://moonrepo.dev/docs/guides/webhooks#events)
  - [Pipeline](https://moonrepo.dev/docs/guides/webhooks#pipeline)
  - [`pipeline.started`](https://moonrepo.dev/docs/guides/webhooks#pipelinestarted)
  - [`pipeline.finished`](https://moonrepo.dev/docs/guides/webhooks#pipelinefinished)
  - [`pipeline.aborted`](https://moonrepo.dev/docs/guides/webhooks#pipelineaborted)
  - [Actions](https://moonrepo.dev/docs/guides/webhooks#actions)
  - [`action.started`](https://moonrepo.dev/docs/guides/webhooks#actionstarted)
  - [`action.finished`](https://moonrepo.dev/docs/guides/webhooks#actionfinished)
  - [`dependencies.installing`](https://moonrepo.dev/docs/guides/webhooks#dependenciesinstalling)
  - [`dependencies.installed`](https://moonrepo.dev/docs/guides/webhooks#dependenciesinstalled)
  - [`environment.initializing`](https://moonrepo.dev/docs/guides/webhooks#environmentinitializing)
  - [`environment.initialized`](https://moonrepo.dev/docs/guides/webhooks#environmentinitialized)
  - [`project.syncing`](https://moonrepo.dev/docs/guides/webhooks#projectsyncing)
  - [`project.synced`](https://moonrepo.dev/docs/guides/webhooks#projectsynced)
  - [`toolchain.installing`](https://moonrepo.dev/docs/guides/webhooks#toolchaininstalling)
  - [`toolchain.installed`](https://moonrepo.dev/docs/guides/webhooks#toolchaininstalled)
  - [`task.running`](https://moonrepo.dev/docs/guides/webhooks#taskrunning)
  - [`task.ran`](https://moonrepo.dev/docs/guides/webhooks#taskran)
  - [`workspace.syncing`](https://moonrepo.dev/docs/guides/webhooks#workspacesyncing)
  - [`workspace.synced`](https://moonrepo.dev/docs/guides/webhooks#workspacesynced)