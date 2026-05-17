[Skip to main content](https://moonrepo.dev/docs/guides/codeowners#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.8.0

Code owners enables companies to define individuals, teams, or groups that are responsible for code
in a repository. This is useful in ensuring that pull/merge requests are reviewed and approved by a
specific set of contributors, before the branch is merged into the base branch.

With that being said, moon _does not_ implement a custom code owners solution, and instead builds
upon the popular `CODEOWNERS` integration in VCS providers, like GitHub, GitLab, and Bitbucket.

## Defining owners [​](https://moonrepo.dev/docs/guides/codeowners\#defining-owners "Direct link to Defining owners")

With moon, you _do not_ modify a `CODEOWNERS` file directly. Instead you define owners _per project_
with [`moon.*`](https://moonrepo.dev/docs/config/project), or globally with [`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace).
These owners are then aggregated and automatically
[synced to a `CODEOWNERS` file](https://moonrepo.dev/docs/guides/codeowners#generating-codeowners).

info

An owner is a user, team, or group unique to your VCS provider. Please refer to your provider's
documentation for the correct format in which to define owners.

### Project-level [​](https://moonrepo.dev/docs/guides/codeowners\#project-level "Direct link to Project-level")

For projects, we support an [`owners`](https://moonrepo.dev/docs/config/project#owners) setting in
[`moon.*`](https://moonrepo.dev/docs/config/project) that accepts file patterns/paths and their owners (contributors
required to review), as well as operational settings for minimum required approvals, custom groups,
and more.

Paths configured here are relative from the project root, and will be prefixed with the project
source (path from workspace root to project root) when the file is synced.

packages/components/moon.yml

```yaml
owners:
  requiredApprovals: 2
  paths:
    'src/': ['@frontend', '@design-system']
    '*.config.js': ['@frontend-infra']
    '*.json': ['@frontend-infra']
```

The configuration above would generate the following:

- GitHub
- GitLab
- Bitbucket

.github/CODEOWNERS

```shell
# components
/packages/components/src/ @frontend @design-system
/packages/components/*.config.js @frontend-infra
/packages/components/*.json @frontend-infra
```

.gitlab/CODEOWNERS

```shell
# components
[components][2]
/packages/components/src/ @frontend @design-system
/packages/components/*.config.js @frontend-infra
/packages/components/*.json @frontend-infra
```

CODEOWNERS

```shell
# components
/packages/components/src/ @frontend @design-system
/packages/components/*.config.js @frontend-infra
/packages/components/*.json @frontend-infra
```

### Workspace-level [​](https://moonrepo.dev/docs/guides/codeowners\#workspace-level "Direct link to Workspace-level")

Project scoped owners are great but sometimes you need to define owners for files that span across
all projects, or files at any depth within the repository. With the
[`codeowners.globalPaths`](https://moonrepo.dev/docs/config/workspace#globalpaths) setting in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace), you can do just that.

Paths configured here are used as-is, allowing for full control of what ownership is applied.

.moon/workspace.yml

```yaml
codeowners:
  globalPaths:
    # All files
    '*': ['@admins']
    # Config folder at any depth
    'config/': ['@app-platform']
    # GitHub folder at the root
    '/.github/': ['@infra']
```

The configuration above would generate the following at the top of the file (is the same for all
providers):

- GitHub
- GitLab
- Bitbucket

.github/CODEOWNERS

```shell
# (workspace)
* @admins
config/ @app-platform
/.github/ @infra
```

.gitlab/CODEOWNERS

```shell
# (workspace)
* @admins
config/ @app-platform
/.github/ @infra
```

CODEOWNERS

```shell
# (workspace)
* @admins
config/ @app-platform
/.github/ @infra
```

## Generating `CODEOWNERS` [​](https://moonrepo.dev/docs/guides/codeowners\#generating-codeowners "Direct link to generating-codeowners")

Code owners is an opt-in feature, and as such, the `CODEOWNERS` file can be generated in a few ways.
The first is manually, with the [`moon sync codeowners`](https://moonrepo.dev/docs/commands/sync/code-owners) command.

```shell
$ moon sync codeowners
```

While this works, it is a manual process, and can easily be forgotten, resulting in an out-of-date
file.

An alternative solution is the [`codeowners.sync`](https://moonrepo.dev/docs/config/workspace#sync) setting in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace#codeowners), that when enabled, moon will automatically
generate a `CODEOWNERS` file when a [target](https://moonrepo.dev/docs/concepts/target) is ran.

.moon/workspace.yml

```yaml
codeowners:
  sync: true
```

> The format and location of the `CODEOWNERS` file is based on the
> [`vcs.provider`](https://moonrepo.dev/docs/config/workspace#provider) setting.

## FAQ [​](https://moonrepo.dev/docs/guides/codeowners\#faq "Direct link to FAQ")

### What providers or formats are supported? [​](https://moonrepo.dev/docs/guides/codeowners\#what-providers-or-formats-are-supported "Direct link to What providers or formats are supported?")

The following providers are supported, based on the [`vcs.provider`](https://moonrepo.dev/docs/config/workspace#provider)
setting.

- [Bitbucket](https://marketplace.atlassian.com/apps/1218598/code-owners-for-bitbucket?tab=overview&hosting=cloud)
(via a 3rd-party app)
- [GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitLab](https://docs.gitlab.com/ee/user/project/codeowners/reference.html)
- Other (very basic syntax)

### Where does the `CODEOWNERS` file get created? [​](https://moonrepo.dev/docs/guides/codeowners\#where-does-the-codeowners-file-get-created "Direct link to where-does-the-codeowners-file-get-created")

The location of the file is dependent on the configured provider.

- GitHub -> `.github/CODEOWNERS`
- GitLab -> `.gitlab/CODEOWNERS`
- Everything else -> `CODEOWNERS`

### Why are owners defined in `moon.*` and not an alternative like `OWNERS`? [​](https://moonrepo.dev/docs/guides/codeowners\#why-are-owners-defined-in-moon-and-not-an-alternative-like-owners "Direct link to why-are-owners-defined-in-moon-and-not-an-alternative-like-owners")

A very popular pattern for defining owners is through an `OWNERS` file, which can appear in any
folder, at any depth, within the repository. All of these files are then aggregated into a single
`CODEOWNERS` file.

While this is useful for viewing ownership of a folder at a glance, it incurs a massive performance
hit as we'd have to constantly glob the _entire_ repository to find all `OWNERS` files. We found it
best to define owners in `moon.*` instead for the following reasons:

- No performance hit, as we're already loading and parsing these config files.
- Co-locates owners with the rest of moon's configuration.
- Ownership is now a part of the project graph, enabling future features.

- [Defining owners](https://moonrepo.dev/docs/guides/codeowners#defining-owners)
  - [Project-level](https://moonrepo.dev/docs/guides/codeowners#project-level)
  - [Workspace-level](https://moonrepo.dev/docs/guides/codeowners#workspace-level)
- [Generating `CODEOWNERS`](https://moonrepo.dev/docs/guides/codeowners#generating-codeowners)
- [FAQ](https://moonrepo.dev/docs/guides/codeowners#faq)
  - [What providers or formats are supported?](https://moonrepo.dev/docs/guides/codeowners#what-providers-or-formats-are-supported)
  - [Where does the `CODEOWNERS` file get created?](https://moonrepo.dev/docs/guides/codeowners#where-does-the-codeowners-file-get-created)
  - [Why are owners defined in `moon.*` and not an alternative like `OWNERS`?](https://moonrepo.dev/docs/guides/codeowners#why-are-owners-defined-in-moon-and-not-an-alternative-like-owners)