[Skip to main content](https://moonrepo.dev/docs/proto/commands/mcp#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.54.0

The `proto mcp` command starts a [Model Context Protocol](https://modelcontextprotocol.io/) server
over stdio, allowing AI agents and other MCP-compatible clients to interact with proto's toolchain,
configuration, and environment.

```shell
$ proto mcp
```

The server is intended to be launched by an MCP client, not invoked directly. Configure your client
(Claude Code, Cursor, etc) to spawn `proto mcp` as the server command.

### Inspecting the server [​](https://moonrepo.dev/docs/proto/commands/mcp\#inspecting-the-server "Direct link to Inspecting the server")

To see what the server exposes without starting an actual session, pass `--info`. This will print
the server metadata and a list of all available tools and resources.

```shell
$ proto mcp --info
```

### Tools [​](https://moonrepo.dev/docs/proto/commands/mcp\#tools "Direct link to Tools")

The server exposes the following tools to MCP clients:

- `install_tool` \- Install a tool with a specified version.
- `uninstall_tool` \- Uninstall a tool with a specified version.
- `list_tool_versions` \- List available and installed versions for a tool.
- `get_config` \- Get the current proto configuration.

### Resources [​](https://moonrepo.dev/docs/proto/commands/mcp\#resources "Direct link to Resources")

The server also exposes the following resources:

- `proto://config` \- Configuration loaded for the current working directory.
- `proto://env` \- The current proto environment, store paths, variables, and more.
- `proto://tools` \- List of installed tools and their versions.

### Options [​](https://moonrepo.dev/docs/proto/commands/mcp\#options "Direct link to Options")

- `--info` \- Display server information and list available tools and resources, then exit.

- [Inspecting the server](https://moonrepo.dev/docs/proto/commands/mcp#inspecting-the-server)
- [Tools](https://moonrepo.dev/docs/proto/commands/mcp#tools)
- [Resources](https://moonrepo.dev/docs/proto/commands/mcp#resources)
- [Options](https://moonrepo.dev/docs/proto/commands/mcp#options)