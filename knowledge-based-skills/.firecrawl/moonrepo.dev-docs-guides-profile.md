[Skip to main content](https://moonrepo.dev/docs/guides/profile#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Troubleshooting slow or unperformant tasks? Profile and diagnose them with ease!

caution

Profiling is only supported by `node` based tasks, and is not supported by tasks that are created
through `package.json` inference, or for packages that ship non-JavaScript code (like Rust or Go).

## CPU snapshots [​](https://moonrepo.dev/docs/guides/profile\#cpu-snapshots "Direct link to CPU snapshots")

CPU profiling helps you get a better understanding of which parts of your code require the most CPU
time, and how your code is executed and optimized by Node.js. The profiler will measure code
execution and activities performed by the engine itself, such as compilation, calls of system
libraries, optimization, and garbage collection.

### Record a profile [​](https://moonrepo.dev/docs/guides/profile\#record-a-profile "Direct link to Record a profile")

To record a CPU profile, pass `--profile cpu` to the [`moon run`](https://moonrepo.dev/docs/commands/run) command. When
successful, the profile will be written to
`.moon/cache/states/<project>/<task>/snapshot.cpuprofile`.

```shell
$ moon run --profile cpu app:lint
```

### Analyze in Chrome [​](https://moonrepo.dev/docs/guides/profile\#analyze-in-chrome "Direct link to Analyze in Chrome")

CPU profiles can be reviewed and analyzed with
[Chrome developer tools](https://developer.chrome.com/docs/devtools/) using the following steps.

1. Open Chrome and navigate to `chrome://inspect`.
2. Under "Devices", navigate to "Open dedicated DevTools for Node".
3. The following window will popup. Ensure the "Profiler" tab is selected.

![DevTools Profiler - CPU](https://moonrepo.dev/assets/images/cpu-deb9e0f9310721da8e3394071dbaa637.png)

4. Click "Load" and select the `snapshot.cpuprofile` that was
[previously recorded](https://moonrepo.dev/docs/guides/profile#record-a-profile). If successful, the snapshot will appear in the left
column.

> On macOS, press `command` \+ `shift` \+ `.` to display hidden files and folders, to locate the
> `.moon` folder.

![DevTools Profiler - CPU snapshot loaded](https://moonrepo.dev/assets/images/cpu-loaded-ff6afad307a77cc32e53364c0cd3a597.png)

5. Select the snapshot in the left column. From here, the snapshot can be analyzed and represented
with [Bottom up](https://moonrepo.dev/docs/guides/profile#bottom-up), [Top down](https://moonrepo.dev/docs/guides/profile#top-down), or [Flame chart](https://moonrepo.dev/docs/guides/profile#flame-chart) views.

![DevTools Profiler - CPU snapshot being analyzed through charts](https://moonrepo.dev/assets/images/cpu-selected-febbd2aef4ffaea46979cbeb583bd648.png)

## Heap snapshots [​](https://moonrepo.dev/docs/guides/profile\#heap-snapshots "Direct link to Heap snapshots")

Heap profiling lets you detect memory leaks, dynamic memory problems, and locate the fragments of
code that caused them.

### Record a profile [​](https://moonrepo.dev/docs/guides/profile\#record-a-profile-1 "Direct link to Record a profile")

To record a heap profile, pass `--profile heap` to the [`moon run`](https://moonrepo.dev/docs/commands/run) command. When
successful, the profile will be written to
`.moon/cache/states/<project>/<task>/snapshot.heapprofile`.

```shell
$ moon run --profile heap app:lint
```

### Analyze in Chrome [​](https://moonrepo.dev/docs/guides/profile\#analyze-in-chrome-1 "Direct link to Analyze in Chrome")

Heap profiles can be reviewed and analyzed with
[Chrome developer tools](https://developer.chrome.com/docs/devtools/) using the following steps.

1. Open Chrome and navigate to `chrome://inspect`.
2. Under "Devices", navigate to "Open dedicated DevTools for Node".
3. The following window will popup. Ensure the "Memory" tab is selected.

![DevTools Profiler - Heap](https://moonrepo.dev/assets/images/heap-3451a7088c4f41a89ad4e068d250f6b4.png)

4. Click "Load" and select the `snapshot.heapprofile` that was
[previously recorded](https://moonrepo.dev/docs/guides/profile#record-a-profile-1). If successful, the snapshot will appear in the left
column.

> On macOS, press `command` \+ `shift` \+ `.` to display hidden files and folders, to locate the
> `.moon` folder.

![DevTools Profiler - Heap snapshot loaded](https://moonrepo.dev/assets/images/heap-loaded-4bbbd3b5dd677a0d5bbdce7585ea3286.png)

5. Select the snapshot in the left column. From here, the snapshot can be analyzed and represented
with [Bottom up](https://moonrepo.dev/docs/guides/profile#bottom-up), [Top down](https://moonrepo.dev/docs/guides/profile#top-down), or [Flame chart](https://moonrepo.dev/docs/guides/profile#flame-chart) views.

![DevTools Profiler - Heap snapshot being analyzed through charts](https://moonrepo.dev/assets/images/heap-selected-41365c3cb6e1244aa6dd2382e58b5804.png)

## Views [​](https://moonrepo.dev/docs/guides/profile\#views "Direct link to Views")

Chrome DevTools provide 3 views for analyzing activities within a snapshot. Each view gives you a
different perspective on these activities.

### Bottom up [​](https://moonrepo.dev/docs/guides/profile\#bottom-up "Direct link to Bottom up")

The Bottom up view is helpful if you encounter a heavy function and want to find out where it was
called from.

- The "Self Time" column represents the aggregated time spent directly in that activity, across all
of its occurrences.
- The "Total Time" column represents aggregated time spent in that activity or any of its children.
- The "Function" column is the function that was executed, including source location, and any
children.

![Bottom up profiler view](https://moonrepo.dev/assets/images/bottom-up-2e2e925bb1bd78f49bf29e4f6f848f7c.png)

### Top down [​](https://moonrepo.dev/docs/guides/profile\#top-down "Direct link to Top down")

The Top down view works in a similar fashion to [Bottom up](https://moonrepo.dev/docs/guides/profile#bottom-up), but displays functions
starting from the top-level entry points. These are also known as root activities.

![Top down profiler view](https://moonrepo.dev/assets/images/top-down-409f6e1447d9875d7013017d0c7f643c.png)

### Flame chart [​](https://moonrepo.dev/docs/guides/profile\#flame-chart "Direct link to Flame chart")

DevTools represents main thread activity with a flame chart. The x-axis represents the recording
over time. The y-axis represents the call stack. The events on top cause the events below it.

![Flame chart profiler view](https://moonrepo.dev/assets/images/flame-chart-aa69d1306f8472d449c7d9755e7995e8.png)

- [CPU snapshots](https://moonrepo.dev/docs/guides/profile#cpu-snapshots)
  - [Record a profile](https://moonrepo.dev/docs/guides/profile#record-a-profile)
  - [Analyze in Chrome](https://moonrepo.dev/docs/guides/profile#analyze-in-chrome)
- [Heap snapshots](https://moonrepo.dev/docs/guides/profile#heap-snapshots)
  - [Record a profile](https://moonrepo.dev/docs/guides/profile#record-a-profile-1)
  - [Analyze in Chrome](https://moonrepo.dev/docs/guides/profile#analyze-in-chrome-1)
- [Views](https://moonrepo.dev/docs/guides/profile#views)
  - [Bottom up](https://moonrepo.dev/docs/guides/profile#bottom-up)
  - [Top down](https://moonrepo.dev/docs/guides/profile#top-down)
  - [Flame chart](https://moonrepo.dev/docs/guides/profile#flame-chart)