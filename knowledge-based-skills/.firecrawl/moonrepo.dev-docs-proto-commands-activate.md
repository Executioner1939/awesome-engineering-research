[Skip to main content](https://moonrepo.dev/docs/proto/commands/activate#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v0.38.0

The `proto activate <shell>` command will activate proto for the current shell session, by exporting
environment variables and prepending `PATH` for each tool configured in the current directory.
Activation is ran each time the current directory changes using a shell hook.

info

Learn more about
[shell activation in the official workflow documentation](https://moonrepo.dev/docs/proto/workflows#shell-activation)!

### Arguments [​](https://moonrepo.dev/docs/proto/commands/activate\#arguments "Direct link to Arguments")

- `<shell>` \- The shell to activate for.

### Options [​](https://moonrepo.dev/docs/proto/commands/activate\#options "Direct link to Options")

- `--export` \- Print the activate instructions in shell-specific syntax.
- `--json` \- Print the activate instructions in JSON format.
- `--no-bin` \- Do not include `~/.proto/bin` when appending `PATH`.
- `--no-shim` \- Do not include `~/.proto/shims` when prepending `PATH`.
- `--no-init` \- Do not trigger activation when initialized in the shell, and instead wait for a
cd/prompt change. v0.50.0

### Caveats [​](https://moonrepo.dev/docs/proto/commands/activate\#caveats "Direct link to Caveats")

- Only tools that have a [version configured in `.prototools`](https://moonrepo.dev/docs/proto/config#pinning-versions) will be
activated.
- Tool versions configured in the global `~/.proto/.prototools` are _not_ included by default. Pass
`--config-mode all` during activation to include them.
  - Do note that this will worsen performance depending on the number of tools.

### Setup [​](https://moonrepo.dev/docs/proto/commands/activate\#setup "Direct link to Setup")

The following activation steps should be added _after_ all environment variable and `PATH`
modifications have happened in your shell, typically at the end of your shell profile.

#### Bash [​](https://moonrepo.dev/docs/proto/commands/activate\#bash "Direct link to Bash")

Add the following line to the end of your `~/.bashrc` or `~/.bash_profile`.

```shell
eval "$(proto activate bash)"
```

#### Elvish [​](https://moonrepo.dev/docs/proto/commands/activate\#elvish "Direct link to Elvish")

Generate the hook:

```shell
proto activate elvish > ~/.elvish/lib/proto-hook.elv
```

Then add the following line to your `~/.elvish/rc.elv` file.

```shell
use proto-hook
```

#### Fish [​](https://moonrepo.dev/docs/proto/commands/activate\#fish "Direct link to Fish")

Add the following line to the end of your `~/.config/fish/config.fish`.

```shell
proto activate fish | source
```

#### Murex [​](https://moonrepo.dev/docs/proto/commands/activate\#murex "Direct link to Murex")

Add the following line to the end of your `~/.murex_profile`.

```shell
proto activate murex -> source
```

#### Nu [​](https://moonrepo.dev/docs/proto/commands/activate\#nu "Direct link to Nu")

Generate the hook:

```shell
(proto activate nu) | save ~/.config/nushell/proto-hook.nu
```

Then add the following line to your `~/.config/nushell/config.nu` file.

```shell
use proto-hook.nu
```

#### Pwsh [​](https://moonrepo.dev/docs/proto/commands/activate\#pwsh "Direct link to Pwsh")

Add the following line to the end of your profile (`$PROFILE`).

```shell
proto activate pwsh | Out-String | Invoke-Expression
```

#### Zsh [​](https://moonrepo.dev/docs/proto/commands/activate\#zsh "Direct link to Zsh")

Add the following line to the end of your `~/.zshrc`.

```shell
eval "$(proto activate zsh)"
```

- [Arguments](https://moonrepo.dev/docs/proto/commands/activate#arguments)
- [Options](https://moonrepo.dev/docs/proto/commands/activate#options)
- [Caveats](https://moonrepo.dev/docs/proto/commands/activate#caveats)
- [Setup](https://moonrepo.dev/docs/proto/commands/activate#setup)
  - [Bash](https://moonrepo.dev/docs/proto/commands/activate#bash)
  - [Elvish](https://moonrepo.dev/docs/proto/commands/activate#elvish)
  - [Fish](https://moonrepo.dev/docs/proto/commands/activate#fish)
  - [Murex](https://moonrepo.dev/docs/proto/commands/activate#murex)
  - [Nu](https://moonrepo.dev/docs/proto/commands/activate#nu)
  - [Pwsh](https://moonrepo.dev/docs/proto/commands/activate#pwsh)
  - [Zsh](https://moonrepo.dev/docs/proto/commands/activate#zsh)