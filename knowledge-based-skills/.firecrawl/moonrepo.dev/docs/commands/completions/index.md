[Skip to main content](https://moonrepo.dev/docs/commands/completions#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `moon completions` command will generate moon command and argument completions for your current
shell. This command will write to stdout, which can then be redirected to a file of your choice.

```shell
$ moon completions > ./path/to/write/to
```

### Options [​](https://moonrepo.dev/docs/commands/completions\#options "Direct link to Options")

- `--shell` \- Shell to explicitly generate for.

### Examples [​](https://moonrepo.dev/docs/commands/completions\#examples "Direct link to Examples")

- Bash
- Fish
- Zsh

If using [bash-completion](https://github.com/scop/bash-completion).

```shell
mkdir -p ~/.bash_completion.d
moon completions > ~/.bash_completion.d/moon.sh
```

Otherwise write the file to a common location, and source it in your profile.

```shell
mkdir -p ~/.bash_completions
moon completions > ~/.bash_completions/moon.sh

# In your profile
source ~/.bash_completions/moon.sh
```

Write the file to Fish's completions directory.

```shell
mkdir -p ~/.config/fish/completions
moon completions > ~/.config/fish/completions/moon.fish
```

If using [oh-my-zsh](https://ohmyz.sh/) (the `_` prefix is required).

```shell
mkdir -p ~/.oh-my-zsh/completions
moon completions > ~/.oh-my-zsh/completions/_moon

# Reload shell (or restart terminal)
omz reload
```

- [Options](https://moonrepo.dev/docs/commands/completions#options)
- [Examples](https://moonrepo.dev/docs/commands/completions#examples)