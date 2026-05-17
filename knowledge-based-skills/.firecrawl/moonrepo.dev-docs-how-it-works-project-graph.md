[Skip to main content](https://moonrepo.dev/docs/how-it-works/project-graph#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The project graph is a representation of all configured
[projects in the workspace](https://moonrepo.dev/docs/config/workspace#projects) and their relationships between each
other, and is represented internally as a directed acyclic graph (DAG). Below is a visual
representation of a project graph, composed of multiple applications and libraries, where both
project types depend on libraries.

info

The [`moon project-graph`](https://moonrepo.dev/docs/commands/project-graph) command can be used to view the structure of
your workspace.

## Relationships [​](https://moonrepo.dev/docs/how-it-works/project-graph\#relationships "Direct link to Relationships")

A relationship is between a dependent (downstream project) and a dependency/requirement (upstream
project). Relationships are derived from source code and configuration files within the repository,
and fall into 1 of 2 categories:

### Explicit [​](https://moonrepo.dev/docs/how-it-works/project-graph\#explicit "Direct link to Explicit")

These are dependencies that are explicitly defined in a project's [`moon.*`](https://moonrepo.dev/docs/config/project)
config file, using the [`dependsOn`](https://moonrepo.dev/docs/config/project#dependson) setting.

moon.yml

```yaml
dependsOn:
  - 'components'
  - id: 'utils'
    scope: 'peer'
```

### Implicit [​](https://moonrepo.dev/docs/how-it-works/project-graph\#implicit "Direct link to Implicit")

These are dependencies that are implicitly discovered by moon when scanning the repository. How an
implicit dependency is discovered is based on a
[language's platform integration](https://moonrepo.dev/docs/how-it-works/languages#tier-2--platform), and how that language's ecosystem
functions.

package.json

```json
{
  // ...
  "dependencies": {
    "@company/components": "workspace:*"
  },
  "peerDependencies": {
    "@company/utils": "workspace:*"
  }
}
```

caution

If a language is not officially supported by moon, then implicit dependencies will _not_ be
resolved. For unsupported languages, you must explicitly configure dependencies.

### Scopes [​](https://moonrepo.dev/docs/how-it-works/project-graph\#scopes "Direct link to Scopes")

Every relationship is categorized into a scope that describes the type of relationship between the
parent and child. Scopes are currently used for [project syncing](https://moonrepo.dev/docs/commands/sync) and deep Docker
integration.

- **Production** \- Dependency is required in production, _will not be_ pruned in production
environments, and will sync as a production dependency.
- **Development** \- Dependency is required in development and production, _will be_ pruned from
production environments, and will sync as a development-only dependency.
- **Build** \- Dependency is required for building only, and will sync as a build dependency.
- **Peer** \- Dependency is a peer requirement, with language specific semantics. Will sync as a peer
dependency when applicable.

## What is the graph used for? [​](https://moonrepo.dev/docs/how-it-works/project-graph\#what-is-the-graph-used-for "Direct link to What is the graph used for?")

Great question, the project graph is used throughout the codebase to accomplish a variety of
functions, but mainly:

- Is fed into the [task graph](https://moonrepo.dev/docs/how-it-works/task-graph) to determine relationships of tasks between other
tasks, and across projects.
- Powers our [Docker](https://moonrepo.dev/docs/guides/docker) layer caching and scaffolding implementations.
- Utilized for [project syncing](https://moonrepo.dev/docs/commands/sync) to ensure a healthy repository state.
- Determines affected projects in [continuous integration](https://moonrepo.dev/docs/guides/ci) workflows.

- [Relationships](https://moonrepo.dev/docs/how-it-works/project-graph#relationships)
  - [Explicit](https://moonrepo.dev/docs/how-it-works/project-graph#explicit)
  - [Implicit](https://moonrepo.dev/docs/how-it-works/project-graph#implicit)
  - [Scopes](https://moonrepo.dev/docs/how-it-works/project-graph#scopes)
- [What is the graph used for?](https://moonrepo.dev/docs/how-it-works/project-graph#what-is-the-graph-used-for)