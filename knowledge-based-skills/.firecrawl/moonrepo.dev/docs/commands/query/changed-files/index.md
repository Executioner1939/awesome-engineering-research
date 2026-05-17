[Skip to main content](https://moonrepo.dev/docs/commands/query/changed-files#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Use the `moon query changed-files` sub-command to query for a list of changed files (added,
modified, deleted, etc) using the current VCS state. These are the same queries that
[`moon exec`](https://moonrepo.dev/docs/commands/exec) use under the hood.

Changed files are determined using the following logic:

- If `--defaultBranch` is provided, and the current branch is the
[`vcs.defaultBranch`](https://moonrepo.dev/docs/config/workspace#defaultbranch), then compare against the previous
revision of the default branch (`HEAD~1`). This is what [continuous integration](https://moonrepo.dev/docs/guides/ci)
uses.
- If `--local` is provided, changed files are based on your local index only (`git status`).
- Otherwise, then compare the defined base (`--base`) against head (`--head`).

```shell
# Return all files
$ moon query changed-files

# Return deleted files
$ moon query changed-files --status deleted

# Return all files between 2 revisions
$ moon query changed-files --base <branch> --head <commit>
```

This will output a list of workspace relative files as JSON. The output has the following structure:

```ts
{
	files: string[],
	options: QueryOptions,
}
```

### Options [​](https://moonrepo.dev/docs/commands/query/changed-files\#options "Direct link to Options")

- `--default-branch` \- When on the default branch, compare against the previous revision.
- `--base <rev>` \- Base branch, commit, or revision to compare against. Defaults to
[`vcs.defaultBranch`](https://moonrepo.dev/docs/config/workspace#defaultbranch).
- `--head <rev>` \- Current branch, commit, or revision to compare with. Defaults to `HEAD`.
- `--local` \- Gather files from the local state instead of remote.
- `--remote` \- Gather files from the remote state instead of local.
- `--status <type>`\- Filter files based on a changed status. Can be passed multiple times.
  - Types: `all` (default), `added`, `deleted`, `modified`, `staged`, `unstaged`, `untracked`

### Configuration [​](https://moonrepo.dev/docs/commands/query/changed-files\#configuration "Direct link to Configuration")

- [`vcs`](https://moonrepo.dev/docs/config/workspace#vcs) in `.moon/workspace.*`

- [Options](https://moonrepo.dev/docs/commands/query/changed-files#options)
- [Configuration](https://moonrepo.dev/docs/commands/query/changed-files#configuration)