[Skip to main content](https://moonrepo.dev/docs/guides/root-project#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Coming from other repositories or task runner, you may be familiar with tasks available at the
repository root, in which one-off, organization, maintenance, or process oriented tasks can be ran.
moon supports this through a concept known as a root-level project.

Begin by adding the root to [`projects`](https://moonrepo.dev/docs/config/workspace#projects) with a source value of `.`
(current directory relative from the workspace).

.moon/workspace.yml

```yaml
# As a map
projects:
  root: '.'

# As a list of globs
projects:
  - '.'
```

> When using globs, the root project's name will be inferred from the repository folder name. Be
> wary of this as it can change based on what a developer has checked out as.

Once added, create a [`moon.*`](https://moonrepo.dev/docs/config/project) in the root of the repository. From here you can
define tasks that can be ran using this new root-level project name, for example,
`moon run root:<task>`.

moon.yml

```yaml
tasks:
  versionCheck:
    command: 'yarn version check'
    inputs: []
    options:
      cache: false
```

And that's it, but there are a few caveats to be aware of...

## Caveats [​](https://moonrepo.dev/docs/guides/root-project\#caveats "Direct link to Caveats")

### Greedy inputs [​](https://moonrepo.dev/docs/guides/root-project\#greedy-inputs "Direct link to Greedy inputs")

warning

In moon v1.24, root-level tasks default to no inputs. In previous versions, inputs defaulted to
`**/*`. This section is only applicable for older moon versions!

Task [`inputs`](https://moonrepo.dev/docs/config/project#inputs) default to `**/*`, which would result in root-level tasks
scanning _all_ files in the repository. This will be a very expensive operation! We suggest
restricting inputs to a very succinct whitelist, or disabling inputs entirely.

moon.yml

```yaml
tasks:
  oneOff:
    # ...
    inputs: []
```

### Inherited tasks [​](https://moonrepo.dev/docs/guides/root-project\#inherited-tasks "Direct link to Inherited tasks")

Because a root project is still a project in the workspace, it will inherit all tasks defined in
[`.moon/tasks/**/*`](https://moonrepo.dev/docs/config/tasks), which may be unexpected. To mitigate this, you can exclude
some or all of these tasks in the root config with
[`workspace.inheritedTasks`](https://moonrepo.dev/docs/config/project#inheritedtasks).

moon.yml

```yaml
workspace:
  inheritedTasks:
    include: []
```

- [Caveats](https://moonrepo.dev/docs/guides/root-project#caveats)
  - [Greedy inputs](https://moonrepo.dev/docs/guides/root-project#greedy-inputs)
  - [Inherited tasks](https://moonrepo.dev/docs/guides/root-project#inherited-tasks)