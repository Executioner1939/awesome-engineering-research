[Skip to main content](https://moonrepo.dev/docs/commands/task-graph#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.30.0

The `moon task-graph [target]` (or `moon tg`) command will generate and serve a visual graph of all
configured tasks as nodes, with dependencies between as edges, and can also output the graph in
[Graphviz DOT format](https://graphviz.org/doc/info/lang.html).

```shell
# Run the visualizer locally
$ moon task-graph

# Export to DOT format
$ moon task-graph --dot > graph.dot
```

> A task target can be passed to focus the graph to only that task and its dependencies. For
> example, `moon task-graph app:build`.

### Arguments [​](https://moonrepo.dev/docs/commands/task-graph\#arguments "Direct link to Arguments")

- `[target]` \- Optional target of task to focus.

### Options [​](https://moonrepo.dev/docs/commands/task-graph\#options "Direct link to Options")

- `--dependents` \- Include direct dependents of the focused task.
- `--dot` \- Print the graph in DOT format.
- `--host` \- The host address. Defaults to `127.0.0.1`. v1.36.0
- `--json` \- Print the graph in JSON format.
- `--port` \- The port to bind to. Defaults to a random port. v1.36.0

## Example output [​](https://moonrepo.dev/docs/commands/task-graph\#example-output "Direct link to Example output")

The following output is an example of the graph in DOT format.

```dot
digraph {
    0 [ label="types:build" style=filled, shape=oval, fillcolor=gray, fontcolor=black]
    1 [ label="runtime:build" style=filled, shape=oval, fillcolor=gray, fontcolor=black]
    2 [ label="website:build" style=filled, shape=oval, fillcolor=gray, fontcolor=black]
    1 -> 0 [ label="required" arrowhead=box, arrowtail=box]
    2 -> 1 [ label="required" arrowhead=box, arrowtail=box]
    2 -> 0 [ label="required" arrowhead=box, arrowtail=box]
}
```

- [Arguments](https://moonrepo.dev/docs/commands/task-graph#arguments)
- [Options](https://moonrepo.dev/docs/commands/task-graph#options)
- [Example output](https://moonrepo.dev/docs/commands/task-graph#example-output)