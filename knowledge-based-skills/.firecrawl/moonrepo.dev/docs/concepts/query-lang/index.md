[Skip to main content](https://moonrepo.dev/docs/concepts/query-lang#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.3.0

moon supports an integrated query language, known as MQL, that can be used to filter and select
projects from the project graph, using an SQL-like syntax. MQL is primarily used by
[`moon run`](https://moonrepo.dev/docs/commands/run) with the `--query` option.

## Syntax [​](https://moonrepo.dev/docs/concepts/query-lang\#syntax "Direct link to Syntax")

### Comparisons [​](https://moonrepo.dev/docs/concepts/query-lang\#comparisons "Direct link to Comparisons")

A comparison (also known as an assignment) is an expression that defines a piece of criteria, and is
a building block of a query. This criteria maps a [field](https://moonrepo.dev/docs/concepts/query-lang#fields) to a value, with an explicit
comparison operator.

#### Equals, Not equals [​](https://moonrepo.dev/docs/concepts/query-lang\#equals-not-equals "Direct link to Equals, Not equals")

The equals (`=`) and not equals (`!=`) comparison operators can be used for _exact_ value matching.

```text
projectLayer=library && language!=javascript
```

You can also define a list of values using square bracket syntax, that will match against one of the
values.

```text
language=[javascript, typescript]
```

#### Like, Not like [​](https://moonrepo.dev/docs/concepts/query-lang\#like-not-like "Direct link to Like, Not like")

The like (`~`) and not like (`!~`) comparison operators can be used for _wildcard_ value matching,
using [glob syntax](https://moonrepo.dev/docs/concepts/file-pattern#globs).

```text
projectSource~packages/* && tag!~*-app
```

> Like comparisons can only be used on non-enum fields.

### Conditions [​](https://moonrepo.dev/docs/concepts/query-lang\#conditions "Direct link to Conditions")

The `&&` and `||` logical operators can be used to combine multiple comparisons into a condition.
The `&&` operator is used to combine comparisons into a logical AND, and the `||` operator is used
for logical OR.

```text
taskToolchain=system || taskToolchain=node
```

For readability concerns, you can also use `AND` or `OR`.

```text
taskToolchain=system OR taskToolchain=node
```

> Mixing both operators in the same condition is not supported.

### Grouping [​](https://moonrepo.dev/docs/concepts/query-lang\#grouping "Direct link to Grouping")

For advanced queries and complex conditions, you can group comparisons using parentheses to create
logical groupings. Groups can also be nested within other groups.

```text
language=javascript && (taskType=test || taskType=build)
```

## Fields [​](https://moonrepo.dev/docs/concepts/query-lang\#fields "Direct link to Fields")

The following fields can be used as criteria, and are related to [task tokens](https://moonrepo.dev/docs/concepts/token#variables).

### `language` [​](https://moonrepo.dev/docs/concepts/query-lang\#language "Direct link to language")

Programming language the project is written in, as defined in
[`moon.*`](https://moonrepo.dev/docs/config/project#language).

```text
language=rust
```

### `project` [​](https://moonrepo.dev/docs/concepts/query-lang\#project "Direct link to project")

Name OR alias of the project.

```text
project=server
```

### `projectAlias` [​](https://moonrepo.dev/docs/concepts/query-lang\#projectalias "Direct link to projectalias")

Alias of the project. For example, the `package.json` name.

```text
projectAlias~@scope/*
```

### `projectLayer`v1.39.0 [​](https://moonrepo.dev/docs/concepts/query-lang\#projectlayer "Direct link to projectlayer")

The project layer, as defined in [`moon.*`](https://moonrepo.dev/docs/config/project#layer).

```text
projectLayer=application
```

### `projectId` [​](https://moonrepo.dev/docs/concepts/query-lang\#projectid "Direct link to projectid")

Name of the project, as defined in [`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace), or `id` in
[`moon.*`](https://moonrepo.dev/docs/config/project#id).

```text
projectId=server
```

### `projectSource` [​](https://moonrepo.dev/docs/concepts/query-lang\#projectsource "Direct link to projectsource")

Relative file path from the workspace root to the project root, as defined in
[`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace).

```text
projectSource~packages/*
```

### `projectStack`v1.22.0 [​](https://moonrepo.dev/docs/concepts/query-lang\#projectstack "Direct link to projectstack")

The project stack, as defined in [`moon.*`](https://moonrepo.dev/docs/config/project#stack).

```text
projectStack=frontend
```

### `tag` [​](https://moonrepo.dev/docs/concepts/query-lang\#tag "Direct link to tag")

A tag within the project, as defined in [`moon.*`](https://moonrepo.dev/docs/config/project#tags).

```text
tag~react-*
```

### `task` [​](https://moonrepo.dev/docs/concepts/query-lang\#task "Direct link to task")

ID/name of a task within the project.

```text
task=[build,test]
```

### `taskToolchain`v1.31.0 [​](https://moonrepo.dev/docs/concepts/query-lang\#tasktoolchain "Direct link to tasktoolchain")

The toolchain a task will run against, as defined in [`moon.*`](https://moonrepo.dev/docs/config/project).

```text
taskToolchain=node
```

### `taskType` [​](https://moonrepo.dev/docs/concepts/query-lang\#tasktype "Direct link to tasktype")

The [type of task](https://moonrepo.dev/docs/concepts/task#types), based on its configured settings.

```text
taskType=build
```

- [Syntax](https://moonrepo.dev/docs/concepts/query-lang#syntax)
  - [Comparisons](https://moonrepo.dev/docs/concepts/query-lang#comparisons)
    - [Equals, Not equals](https://moonrepo.dev/docs/concepts/query-lang#equals-not-equals)
    - [Like, Not like](https://moonrepo.dev/docs/concepts/query-lang#like-not-like)
  - [Conditions](https://moonrepo.dev/docs/concepts/query-lang#conditions)
  - [Grouping](https://moonrepo.dev/docs/concepts/query-lang#grouping)
- [Fields](https://moonrepo.dev/docs/concepts/query-lang#fields)
  - [`language`](https://moonrepo.dev/docs/concepts/query-lang#language)
  - [`project`](https://moonrepo.dev/docs/concepts/query-lang#project)
  - [`projectAlias`](https://moonrepo.dev/docs/concepts/query-lang#projectalias)
  - [`projectLayer`](https://moonrepo.dev/docs/concepts/query-lang#projectlayer)
  - [`projectId`](https://moonrepo.dev/docs/concepts/query-lang#projectid)
  - [`projectSource`](https://moonrepo.dev/docs/concepts/query-lang#projectsource)
  - [`projectStack`](https://moonrepo.dev/docs/concepts/query-lang#projectstack)
  - [`tag`](https://moonrepo.dev/docs/concepts/query-lang#tag)
  - [`task`](https://moonrepo.dev/docs/concepts/query-lang#task)
  - [`taskToolchain`](https://moonrepo.dev/docs/concepts/query-lang#tasktoolchain)
  - [`taskType`](https://moonrepo.dev/docs/concepts/query-lang#tasktype)