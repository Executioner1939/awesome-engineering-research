[Skip to main content](https://moonrepo.dev/docs/guides/mcp#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.37.0

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open standard that enables AI
models to interact with external tools and services through a unified interface. The moon CLI
contains an MCP server that you can register with your code editor to allow LLMs to use moon
directly.

## Setup [​](https://moonrepo.dev/docs/guides/mcp\#setup "Direct link to Setup")

### Claude Code [​](https://moonrepo.dev/docs/guides/mcp\#claude-code "Direct link to Claude Code")

To use [MCP servers in Claude Code](https://docs.anthropic.com/en/docs/claude-code/mcp), run the
following command in your terminal:

```shell
claude mcp add moon -s project -e MOON_WORKSPACE_ROOT=/absolute/path/to/your/moon/workspace -- moon mcp
```

Or create an `.mcp.json` file in your project directory.

```json
{
  "mcpServers": {
    "moon": {
      "command": "moon",
      "args": ["mcp"],
      "env": {
        "MOON_WORKSPACE_ROOT": "/absolute/path/to/your/moon/workspace"
      }
    }
  }
}
```

### Cursor [​](https://moonrepo.dev/docs/guides/mcp\#cursor "Direct link to Cursor")

To use [MCP servers in Cursor](https://docs.cursor.com/context/model-context-protocol), create a
`.cursor/mcp.json` file in your project directory, or `~/.cursor/mcp.json` globally, with the
following content:

.cursor/mcp.json

```json
{
  "mcpServers": {
    "moon": {
      "command": "moon",
      "args": ["mcp"],
      "env": {
        "MOON_WORKSPACE_ROOT": "/absolute/path/to/your/moon/workspace"
      }
    }
  }
}
```

Once configured, the moon MCP server should appear in the "Available Tools" section on the MCP
settings page in Cursor.

### VS Code [​](https://moonrepo.dev/docs/guides/mcp\#vs-code "Direct link to VS Code")

To use MCP servers in VS Code, you must have the
[Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat) extension installed.
Once installed, create a `.vscode/mcp.json` file with the following content:

.vscode/mcp.json

```json
{
  "servers": {
    "moon": {
      "type": "stdio",
      "command": "moon",
      "args": ["mcp"],
      // >= 1.102 (June 2025)
      "cwd": "${workspaceFolder}",
      // Older versions
      "env": {
        "MOON_WORKSPACE_ROOT": "${workspaceFolder}"
      }
    }
  }
}
```

Once your MCP server is configured, you can use it with
[GitHub Copilot’s agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode):

- Open the Copilot Chat view in VS Code
- Enable agent mode using the mode select dropdown
- Toggle on moon's MCP tools using the "Tools" button

### Zed [​](https://moonrepo.dev/docs/guides/mcp\#zed "Direct link to Zed")

To use [MCP servers in Zed](https://zed.dev/docs/ai/mcp), create a `.zed/settings.json` file in your
project directory, or `~/.config/zed/settings.json` globally, with the following content:

.zed/settings.json

```json
{
  "context_servers": {
    "moon": {
      "command": {
        "path": "moon",
        "args": ["mcp"],
        "env": {
          "MOON_WORKSPACE_ROOT": "/absolute/path/to/your/moon/workspace"
        }
      }
    }
  }
}
```

Once your MCP server is configured, you'll need to enable the tools using the following steps:

- Open the Agent panel in Zed
- Click the Write/Ask toggle button and go to "Configure Profiles"
- Click "Customize" in the Ask section
- Click "Configure MCP Tools"
- Enable each tool under the "moon" section

## Available tools [​](https://moonrepo.dev/docs/guides/mcp\#available-tools "Direct link to Available tools")

The following tools are available in the moon MCP server and can be executed by LLMs using agent
mode.

- `get_project` \- Get a project and its tasks by `id`.
- `get_projects` \- Get all projects.
- `get_task` \- Get a task by `target`.
- `get_tasks` \- Get all tasks.
- `get_changed_files` \- Gets changed files between base and head revisions.v1.38.0
- `sync_projects` \- Runs the `SyncProject` action for one or many projects by `id`.v1.38.0
- `sync_workspace` \- Runs the `SyncWorkspace` action. v1.38.0

info

The
[request and response shapes](https://github.com/moonrepo/moon/blob/master/packages/types/src/mcp.ts)
for these tools are defined as TypeScript types in the
[`@moonrepo/types`](https://www.npmjs.com/package/@moonrepo/types) package.

- [Setup](https://moonrepo.dev/docs/guides/mcp#setup)
  - [Claude Code](https://moonrepo.dev/docs/guides/mcp#claude-code)
  - [Cursor](https://moonrepo.dev/docs/guides/mcp#cursor)
  - [VS Code](https://moonrepo.dev/docs/guides/mcp#vs-code)
  - [Zed](https://moonrepo.dev/docs/guides/mcp#zed)
- [Available tools](https://moonrepo.dev/docs/guides/mcp#available-tools)