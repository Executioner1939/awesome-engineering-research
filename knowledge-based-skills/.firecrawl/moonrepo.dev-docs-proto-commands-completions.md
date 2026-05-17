[Skip to main content](https://moonrepo.dev/docs/proto/commands/completions#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `proto completions` command will generate proto command and argument completions for your
current shell. This command will write to stdout, which can then be redirected to a file of your
choice.

```shell
$ proto completions > ./path/to/write/to
```

### Options [​](https://moonrepo.dev/docs/proto/commands/completions\#options "Direct link to Options")

- `--shell` \- Shell to explicitly generate for.

### Examples [​](https://moonrepo.dev/docs/proto/commands/completions\#examples "Direct link to Examples")

- Bash
- Fish
- Zsh

If using [bash-completion](https://github.com/scop/bash-completion).

```shell
mkdir -p ~/.bash_completion.d
proto completions > ~/.bash_completion.d/proto.sh
```

Otherwise write the file to a common location, and source it in your profile.

```shell
mkdir -p ~/.bash_completions
proto completions > ~/.bash_completions/proto.sh

# In your profile
source ~/.bash_completions/proto.sh
```

Write the file to Fish's completions directory.

```shell
mkdir -p ~/.config/fish/completions
proto completions > ~/.config/fish/completions/proto.fish
```

If using [oh-my-zsh](https://ohmyz.sh/) (the `_` prefix is required).

```shell
mkdir -p ~/.oh-my-zsh/completions
proto completions > ~/.oh-my-zsh/completions/_proto

# Reload shell (or restart terminal)
omz reload
```

- [Options](https://moonrepo.dev/docs/proto/commands/completions#options)
- [Examples](https://moonrepo.dev/docs/proto/commands/completions#examples)