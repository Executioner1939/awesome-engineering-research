[Skip to main content](https://moonrepo.dev/docs/guides/daemon#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.2.0

As workspaces grow in size, the time spent building
[project and task graphs](https://moonrepo.dev/docs/how-it-works/project-graph) becomes a noticeable bottleneck. Every
`moon` CLI invocation rebuilds these graphs from scratch, even when nothing has changed since the
last run. The daemon solves this by running a background server process that keeps the workspace
graph hot in memory, watches for file changes, and rebuilds only when necessary. This eliminates
redundant work and significantly improves CLI response times, especially in larger workspaces with
hundreds or thousands of projects/tasks.

caution

This feature is currently **unstable** and must be explicitly enabled. Its behavior and
configuration may change in future releases.

## Enabling the daemon [​](https://moonrepo.dev/docs/guides/daemon\#enabling-the-daemon "Direct link to Enabling the daemon")

To enable the daemon, set the [`unstable_daemon`](https://moonrepo.dev/docs/config/workspace#daemon) setting in
[`.moon/workspace.yml`](https://moonrepo.dev/docs/config/workspace).

.moon/workspace.yml

```yaml
unstable_daemon: true
```

Alternatively, you can enable it via the `MOON_DAEMON` environment variable without modifying your
configuration. This is useful for trying it out before committing to the change.

```shell
MOON_DAEMON=true moon run :build
```

## How it works [​](https://moonrepo.dev/docs/guides/daemon\#how-it-works "Direct link to How it works")

### Background server [​](https://moonrepo.dev/docs/guides/daemon\#background-server "Direct link to Background server")

When the daemon is enabled, the first `moon` CLI command you run automatically spawns a background
server process. This process detaches from the terminal and continues running after the command
completes. Subsequent CLI invocations connect to the running daemon instead of starting fresh.

The daemon communicates with CLI processes over a local IPC channel — Unix domain sockets on
macOS/Linux, and named pipes on Windows. All daemon files (PID, socket, and logs) are stored in
`.moon/cache/daemon`.

If the daemon fails to start or is unavailable, the CLI falls back to building graphs in-process as
it normally would without the daemon. You won't see an error — the CLI simply proceeds without the
performance benefit.

### File watching [​](https://moonrepo.dev/docs/guides/daemon\#file-watching "Direct link to File watching")

To keep the in-memory graph up to date, the daemon watches the workspace root recursively for file
system changes. Events are debounced (coalesced within a short window) to avoid redundant rebuilds
during rapid edits.

The following directories are always ignored by the watcher:

- `.git`, `.svn`, `node_modules`
- `.moon/cache`, `.moon/docker`

Changes to the following files and directories trigger an asynchronous graph rebuild:

- [`.prototools`](https://moonrepo.dev/docs/proto/config) — reloads toolchain configuration
- `.moon/workspace.*` — reloads workspace settings
- `.moon/toolchains.*` — reloads toolchain plugins
- `.moon/extensions.*` — reloads extension plugins
- `.moon/tasks/**/*` — reloads task inheritance
- `moon.*` config files in project directories — reloads project configuration
- Creation or removal of project directories matching configured
[project sources](https://moonrepo.dev/docs/config/workspace#projects)

Because rebuilds happen asynchronously in the background, the daemon remains responsive to new CLI
connections while a rebuild is in progress.

## Managing the daemon [​](https://moonrepo.dev/docs/guides/daemon\#managing-the-daemon "Direct link to Managing the daemon")

The [`moon daemon`](https://moonrepo.dev/docs/commands/daemon) command provides subcommands for managing the daemon's
lifecycle. In most cases you won't need these — the daemon starts automatically and stays out of the
way — but they're useful for debugging or manual control.

### Starting [​](https://moonrepo.dev/docs/guides/daemon\#starting "Direct link to Starting")

```shell
$ moon daemon start
```

Starts the daemon if it's not already running. If a daemon is already running for this workspace,
the existing process is reused. You typically don't need to run this manually, as the daemon
auto-starts with any `moon` command when enabled. See
[`moon daemon start`](https://moonrepo.dev/docs/commands/daemon/start).

### Stopping [​](https://moonrepo.dev/docs/guides/daemon\#stopping "Direct link to Stopping")

```shell
$ moon daemon stop
```

Stops the daemon gracefully. If the daemon does not shut down within a few seconds, it will be
forcefully killed. Daemon files (PID, socket) are cleaned up automatically. See
[`moon daemon stop`](https://moonrepo.dev/docs/commands/daemon/stop).

### Restarting [​](https://moonrepo.dev/docs/guides/daemon\#restarting "Direct link to Restarting")

```shell
$ moon daemon restart
```

Stops the running daemon and starts a new one. This is useful after manual configuration changes, or
if the daemon's cached state seems stale. See [`moon daemon restart`](https://moonrepo.dev/docs/commands/daemon/restart).

### Checking status [​](https://moonrepo.dev/docs/guides/daemon\#checking-status "Direct link to Checking status")

```shell
$ moon daemon status
```

Displays information about the running daemon, including its process ID, uptime, socket/pipe
endpoint, and file paths for the PID and log files. See
[`moon daemon status`](https://moonrepo.dev/docs/commands/daemon/status).

### Viewing logs [​](https://moonrepo.dev/docs/guides/daemon\#viewing-logs "Direct link to Viewing logs")

```shell
$ moon daemon logs
```

Tails the daemon's log file in real time. The daemon must be running for this command to work. The
log file is located at `.moon/cache/daemon/server.log` and contains detailed trace-level output. See
[`moon daemon logs`](https://moonrepo.dev/docs/commands/daemon/logs).

## Troubleshooting [​](https://moonrepo.dev/docs/guides/daemon\#troubleshooting "Direct link to Troubleshooting")

### The daemon won't start [​](https://moonrepo.dev/docs/guides/daemon\#the-daemon-wont-start "Direct link to The daemon won't start")

- Verify the daemon is enabled: check that `unstable_daemon: true` is set in
[`.moon/workspace.yml`](https://moonrepo.dev/docs/config/workspace), or that the `MOON_DAEMON` environment variable is
set.
- Check if a daemon is already running with [`moon daemon status`](https://moonrepo.dev/docs/commands/daemon/status).
- If the daemon crashed previously, a stale PID file may be blocking startup. Delete
`.moon/cache/daemon` and try again.

### The graph seems stale [​](https://moonrepo.dev/docs/guides/daemon\#the-graph-seems-stale "Direct link to The graph seems stale")

If tasks or projects appear to be missing or outdated despite config changes, the file watcher may
have missed an event. Run [`moon daemon restart`](https://moonrepo.dev/docs/commands/daemon/restart) to force a fresh graph
build.

### Where are the logs? [​](https://moonrepo.dev/docs/guides/daemon\#where-are-the-logs "Direct link to Where are the logs?")

The daemon writes detailed logs to `.moon/cache/daemon/server.log`. Use
[`moon daemon logs`](https://moonrepo.dev/docs/commands/daemon/logs) to tail this file, or open it directly in an editor.

### After upgrading moon [​](https://moonrepo.dev/docs/guides/daemon\#after-upgrading-moon "Direct link to After upgrading moon")

After upgrading moon to a new version, restart the daemon with
[`moon daemon restart`](https://moonrepo.dev/docs/commands/daemon/restart). A running daemon from a previous version may
behave unexpectedly or return stale data. We'll attempt to automate this when applicable.

### CI environments [​](https://moonrepo.dev/docs/guides/daemon\#ci-environments "Direct link to CI environments")

The daemon is designed for local development where a persistent background process can be reused
across multiple CLI invocations. In CI environments, where each run starts fresh, the daemon
provides no benefit since there's no long-lived process to connect to. Enabling it in CI won't cause
harm, but it won't improve performance either.

## Limitations [​](https://moonrepo.dev/docs/guides/daemon\#limitations "Direct link to Limitations")

- This feature is **unstable** and may change in future releases. Behavior, configuration, and CLI
commands are subject to change.
- Each workspace runs its own daemon process. If you work across multiple workspaces, each will have
a separate daemon.
- On Windows, the daemon uses named pipes instead of Unix domain sockets. The behavior is
equivalent, but the underlying IPC mechanism differs.

- [Enabling the daemon](https://moonrepo.dev/docs/guides/daemon#enabling-the-daemon)
- [How it works](https://moonrepo.dev/docs/guides/daemon#how-it-works)
  - [Background server](https://moonrepo.dev/docs/guides/daemon#background-server)
  - [File watching](https://moonrepo.dev/docs/guides/daemon#file-watching)
- [Managing the daemon](https://moonrepo.dev/docs/guides/daemon#managing-the-daemon)
  - [Starting](https://moonrepo.dev/docs/guides/daemon#starting)
  - [Stopping](https://moonrepo.dev/docs/guides/daemon#stopping)
  - [Restarting](https://moonrepo.dev/docs/guides/daemon#restarting)
  - [Checking status](https://moonrepo.dev/docs/guides/daemon#checking-status)
  - [Viewing logs](https://moonrepo.dev/docs/guides/daemon#viewing-logs)
- [Troubleshooting](https://moonrepo.dev/docs/guides/daemon#troubleshooting)
  - [The daemon won't start](https://moonrepo.dev/docs/guides/daemon#the-daemon-wont-start)
  - [The graph seems stale](https://moonrepo.dev/docs/guides/daemon#the-graph-seems-stale)
  - [Where are the logs?](https://moonrepo.dev/docs/guides/daemon#where-are-the-logs)
  - [After upgrading moon](https://moonrepo.dev/docs/guides/daemon#after-upgrading-moon)
  - [CI environments](https://moonrepo.dev/docs/guides/daemon#ci-environments)
- [Limitations](https://moonrepo.dev/docs/guides/daemon#limitations)