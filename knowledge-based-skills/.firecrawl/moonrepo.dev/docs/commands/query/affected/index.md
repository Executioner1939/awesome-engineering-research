[Skip to main content](https://moonrepo.dev/docs/commands/query/affected#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v2.0.0

Use the `moon query affected` sub-command to query for all affected projects and tasks based on the
state of the workspace and VCS.

```shell
# Return affected
$ moon query affected

# Return affected including dependency relationships
$ moon query affected --upstream deep
```

This will output a map of projects and tasks as JSON. The output has the following structure:

```ts
{
	projects: Record<Id, AffectedState>,
	tasks: Record<Target, AffectedState>,
}
```

### Options [​](https://moonrepo.dev/docs/commands/query/affected\#options "Direct link to Options")

- `--downstream` \- Include downstream dependents. Supports "none" (default), "direct", "deep".
- `--upstream` \- Include upstream dependencies. Supports "none" (default), "direct", "deep".

- [Options](https://moonrepo.dev/docs/commands/query/affected#options)