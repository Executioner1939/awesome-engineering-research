[Skip to main content](https://moonrepo.dev/docs/proto/commands/setup#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto setup` command will setup proto in your current shell by modifying an applicable profile
file and appending proto's bin directory to `PATH`. If a shell could not be detected, you'll be
prompted to select one.

```shell
$ proto setup
```

During setup, the following profiles will be searched or prompted for.

- Bash
  - `~/.bash_profile`
  - `~/.bashrc`
  - `~/.profile`
- Elvish
  - `~/.elvish/rc.elv`
  - `~/.config/elvish/rc.elv`
- Fish
  - `~/.config/fish/config.fish`
- Ion
  - `~/.config/ion/initrc`
- Murex
  - `~/.murex_preload`
  - `~/.murex_profile`
- Nu
  - `~/.config/nushell/env.nu`
  - `~/.config/nushell/config.nu`
- PowerShell
  - Windows
    - `~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`
    - `~\Documents\PowerShell\Profile.ps1`
  - Unix
    - `~/.config/powershell/Microsoft.PowerShell_profile.ps1`
    - `~/.config/powershell/profile.ps1`
- Xonsh
  - `~/.config/xonsh/rc.xsh`
  - `~/.xonshrc`
- Zsh
  - `~/.zprofile`
  - `~/.zshenv`
  - `~/.zshrc`

### Windows support [​](https://moonrepo.dev/docs/proto/commands/setup\#windows-support "Direct link to Windows support")

In addition to updating a shell profile file (most likely PowerShell), we'll also modify the `PATH`
(or `Path`) system environment variable, by prepending the `~/.proto/shims` and `~/.proto/bin`
paths.

If you would like to opt-out of this behavior, pass the `--no-modify-path` flag.

### Options [​](https://moonrepo.dev/docs/proto/commands/setup\#options "Direct link to Options")

- `--shell` \- Shell to explicitly setup for.
- `--no-modify-profile` / `PROTO_NO_MODIFY_PROFILE` \- Don't update a shell profile file.
- `--no-modify-path` / `PROTO_NO_MODIFY_PATH` \- Don't update the system `PATH` environment variable
(Windows only).
- `--yes` \- Avoid interactive prompts and use defaults.

- [Windows support](https://moonrepo.dev/docs/proto/commands/setup#windows-support)
- [Options](https://moonrepo.dev/docs/proto/commands/setup#options)