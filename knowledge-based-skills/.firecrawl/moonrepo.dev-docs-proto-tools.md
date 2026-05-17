[Skip to main content](https://moonrepo.dev/docs/proto/tools#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

## Built-in [​](https://moonrepo.dev/docs/proto/tools\#built-in "Direct link to Built-in")

The following tools are supported natively in proto's toolchain.

[WASM](https://github.com/moonrepo/plugins)

##### [Bun](https://bun.sh/)

Bun is an all-in-one runtime and toolset for JavaScript and TypeScript, powered by Zig and Webkit.

```shell
proto install bun
```

Available bins: `bun`, `bunx`

Globals directory: `~/.bun/bin`

Detection sources: [`.bumrc`](https://github.com/owenizedd/bum), `.bun-version`, `package.json` volta, engines, packageManager

[WASM](https://github.com/moonrepo/plugins)

##### [Deno](https://deno.land/)

Deno is a secure runtime for JavaScript and TypeScript, powered by Rust and Chrome's V8 engine.

```shell
proto install deno
```

Available bins: `deno`

Globals directory: `$DENO_INSTALL_ROOT/bin`, `$DENO_HOME/bin`, `~/.deno/bin`

Detection sources: [`.dvmrc`](https://github.com/justjavac/dvm)

[WASM](https://github.com/moonrepo/plugins)

##### [Go](https://go.dev/)

Go is a simple, secure, and fast systems language.

```shell
proto install go
```

Available bins: `go`, `gofmt`

Globals directory: `$GOBIN`, `$GOROOT/bin`, `$GOPATH/bin`, `~/go/bin`

Detection sources: [`go.work`](https://go.dev/doc/tutorial/workspaces), [`go.mod`](https://go.dev/doc/modules/gomod-ref)

[WASM](https://github.com/moonrepo/plugins)

##### [moon](https://moonrepo.dev/moon)

moon is a multi-language build system and codebase management tool.

```shell
proto install moon
```

Available bins: `moon`

[WASM](https://github.com/moonrepo/plugins)

##### [Node.js](https://nodejs.org/)

Node.js is a JavaScript runtime built on Chrome's V8 engine.

```shell
proto install node
```

Available bins: `node`

Globals directory: `~/.proto/tools/node/globals/bin`

Detection sources: [`.nvmrc`](https://github.com/nvm-sh/nvm), [`.node-version`](https://github.com/nodenv/nodenv), `package.json` volta, engines

[WASM](https://github.com/moonrepo/plugins)

##### [npm](https://github.com/moonrepo/plugins)

A Node.js package manager.

```shell
proto install npm
```

Available bins: `npm`, `npx`, `node-gyp`

Globals directory: `~/.proto/tools/node/globals/bin`

Detection sources: `package.json` volta, engines, packageManager

[WASM](https://github.com/moonrepo/plugins)

##### [pnpm](https://github.com/moonrepo/plugins)

A Node.js package manager.

```shell
proto install pnpm
```

Available bins: `pnpm`, `pnpx`

Globals directory: `~/.proto/tools/node/globals/bin`

Detection sources: `package.json` volta, engines, packageManager

[WASM](https://github.com/python-poetry/poetry)

##### [Poetry](https://python-poetry.org/)

Python packaging and dependency management made easy.

```shell
proto install poetry
```

Available bins: `poetry`

Detection sources: `.poetry-version`

[WASM](https://github.com/moonrepo/plugins)

##### [Python](https://www.python.org/)

Python is a high-level, general-purpose programming language.

```shell
proto install python
```

Available bins: `python`, `pip`

Globals directory: `~/.proto/tools/python/x.x.x/install/bin`

Detection sources: [`.python-version`](https://github.com/pyenv/pyenv)

[WASM](https://github.com/moonrepo/plugins)

##### [Ruby](https://www.ruby-lang.org/en/)

A dynamic, open source programming language with a focus on simplicity and productivity.

```shell
proto install ruby
```

Available bins: `ruby`, `rake`, `gem`, `bundle`, `irb`

Detection sources: [`.ruby-version`](https://github.com/rbenv/rbenv)

[WASM](https://github.com/moonrepo/plugins)

##### [Rust](https://www.rust-lang.org/)

Rust is a blazingly fast and memory-efficient systems language.

```shell
proto install rust
```

Globals directory: `$CARGO_INSTALL_ROOT/bin`, `$CARGO_HOME/bin`, `~/.cargo/bin`

Detection sources: `rust-toolchain.toml`, `rust-toolchain`

[WASM](https://github.com/astral-sh/uv)

##### [uv](https://docs.astral.sh/uv)

An extremely fast Python package and project manager.

```shell
proto install uv
```

Available bins: `uv`, `uvx`

Detection sources: [`uv.toml`](https://docs.astral.sh/uv/reference/settings/#required-version), `pyproject.toml`

[WASM](https://github.com/moonrepo/plugins)

##### [Yarn](https://github.com/moonrepo/plugins)

A Node.js package manager.

```shell
proto install yarn
```

Available bins: `yarn`, `yarnpkg`

Globals directory: `~/.proto/tools/node/globals/bin`

Detection sources: `package.json` volta, engines, packageManager

## Third-party [​](https://moonrepo.dev/docs/proto/tools\#third-party "Direct link to Third-party")

[Add tool](https://github.com/moonrepo/proto/tree/master/registry)

Additional tools can be supported through [plugins](https://moonrepo.dev/docs/proto/plugins).

[TOML](https://github.com/theomessin/proto-toml-plugins/blob/master/act.toml)

##### [act](https://github.com/nektos/act)(theomessin)

Run your GitHub Actions locally.

```shell
proto plugin add act "https://raw.githubusercontent.com/theomessin/proto-toml-plugins/master/act.toml"
proto install act
```

Available bins: `act`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [actionlint](https://github.com/rhysd/actionlint)(Phault)

Static checker for GitHub Actions workflow files.

```shell
proto plugin add actionlint "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/actionlint/plugin.toml"
proto install actionlint
```

Available bins: `actionlint`

[TOML](https://github.com/jamesukiyo/proto-plugins)

##### [air](https://github.com/air-verse/air)(jamesukiyo)

Live reload for Go apps

```shell
proto plugin add air "https://raw.githubusercontent.com/jamesukiyo/proto-plugins/master/air.toml"
proto install air
```

Available bins: `air`

[WASM](https://github.com/archgate/proto-plugin)

##### [Archgate](https://cli.archgate.dev/)(archgate)

Enforce Architecture Decision Records as executable rules.

```shell
proto plugin add archgate "github://archgate/proto-plugin"
proto install archgate
```

Available bins: `archgate`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/argo)

##### [Argo CLI](https://github.com/appthrust/proto-toml-plugins)(appthrust)

argo is the command line interface to Argo.

```shell
proto plugin add argo "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/argo/plugin.toml"
proto install argo
```

Available bins: `argo`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/argocd)

##### [argocd](https://github.com/appthrust/proto-toml-plugins)(appthrust)

argocd controls a Argo CD server.

```shell
proto plugin add argocd "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/argocd/plugin.toml"
proto install argocd
```

Available bins: `argocd`

[TOML](https://github.com/crashdump/proto-tools)

##### [atlas](https://atlasgo.io/)(crashdump)

manage your database schema as code.

```shell
proto plugin add atlas "https://raw.githubusercontent.com/crashdump/proto-tools/refs/heads/main/toml-plugins/atlas/plugin.toml"
proto install atlas
```

Available bins: `atlas`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Bazel](https://bazel.build/)(Phault)

A fast, scalable, multi-language and extensible build system.

```shell
proto plugin add bazel "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/bazel/plugin.toml"
proto install bazel
```

Available bins: `bazel`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Biome](https://biomejs.dev/)(Phault)

A performant toolchain for web projects, aiming to provide developer tools to maintain the health of said projects.

```shell
proto plugin add biome "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/biome/plugin.toml"
proto install biome
```

Available bins: `biome`

[TOML](https://github.com/appthrust/proto-toml-plugins)

##### [Black](https://black.readthedocs.io/en/stable/)(appthrust)

The uncompromising Python code formatter.

```shell
proto plugin add black "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/black/plugin.toml"
proto install black
```

Available bins: `black`

[TOML](https://github.com/yuhua99/proto-toml-plugins)

##### [bottom](https://bottom.pages.dev/)(yuhua99)

A customizable cross-platform graphical process/system monitor for the terminal.

```shell
proto plugin add bottom "https://raw.githubusercontent.com/yuhua99/proto-toml-plugins/refs/heads/main/bottom/bottom.toml"
proto install bottom
```

Available bins: `btm`

[TOML](https://github.com/stk0vrfl0w/proto-toml-plugins/blob/main/plugins/buf.toml)

##### [buf](https://buf.build/)(stk0vrfl0w)

A new way of working with Protocol Buffers.

```shell
proto plugin add buf "https://raw.githubusercontent.com/stk0vrfl0w/proto-toml-plugins/main/plugins/buf.toml"
proto install buf
```

Available bins: `buf`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/buildifier)

##### [buildifier](https://github.com/bazelbuild/buildtools)(appthrust)

A bazel BUILD file formatter and editor

```shell
proto plugin add buildifier "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/buildifier/plugin.toml"
proto install buildifier
```

Available bins: `buildifier`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Caddy](https://caddyserver.com/)(Phault)

Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS.

```shell
proto plugin add caddy "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/caddy/plugin.toml"
proto install caddy
```

Available bins: `caddy`

[TOML](https://github.com/chester-lang/chester)

##### [chester](https://github.com/chester-lang/chester)(mio-19)

Chester is a programming language.

```shell
proto plugin add chester "https://github.com/chester-lang/chester/raw/refs/heads/main/proto.toml"
proto install chester
```

Available bins: `chester`, `chester-lsp`

[WASM](https://github.com/BarretoTech/proto-claude-code-plugin)

##### [Claude Code](https://github.com/anthropics/claude-code)(BarretoTech)

An agentic coding tool that lives in your terminal.

```shell
proto plugin add claude-code "github://BarretoTech/proto-claude-code-plugin"
proto install claude-code
```

Available bins: `claude`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [CMake](https://cmake.org/)(Phault)

CMake is a cross-platform, open-source build system generator.

```shell
proto plugin add cmake "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/cmake/plugin.toml"
proto install cmake
```

Available bins: `cmake`

[TOML](https://github.com/ageha734/proto-plugins)

##### [commitlint](https://github.com/conventionalcommit/commitlint)(ageha734)

A linter that checks whether commit messages comply with standards.

```shell
proto plugin add commitlint "https://raw.githubusercontent.com/ageha734/proto-plugins/refs/heads/master/toml/commitlint.toml"
proto install commitlint
```

Available bins: `commitlint`

[WASM](https://github.com/KonstantinKai/proto-composer-plugin)

##### [Composer](https://getcomposer.org/)(Konstantin Kai)

A dependency manager for PHP.

```shell
proto plugin add composer "github://KonstantinKai/proto-composer-plugin"
proto install composer
```

Available bins: `composer`

Globals directory: `$COMPOSER_HOME/vendor/bin`, `$HOME/.composer/vendor/bin`

[TOML](https://github.com/isaac10334/conan-proto)

##### [Conan](https://conan.io/)(isaac10334)

An open-source C and C++ package manager.

```shell
proto plugin add conan "https://raw.githubusercontent.com/isaac10334/conan-proto/main/conan.toml"
proto install conan
```

Available bins: `conan`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Cosign](https://github.com/sigstore/cosign)(Phault)

Code signing and transparency for containers and binaries.

```shell
proto plugin add cosign "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/cosign/plugin.toml"
proto install cosign
```

Available bins: `cosign`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/cue)

##### [CUE](https://github.com/appthrust/proto-toml-plugins)(appthrust)

CUE makes it easy to validate data, write schemas, and ensure configurations align with policies.

```shell
proto plugin add cue "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/cue/plugin.toml"
proto install cue
```

Available bins: `cue`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Dagger](https://dagger.io/)(Phault)

Powerful, programmable open source CI/CD engine that runs your pipelines in containers.

```shell
proto plugin add dagger "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/dagger/plugin.toml"
proto install dagger
```

Available bins: `dagger`

[WASM](https://github.com/KonstantinKai/proto-dart-plugin)

##### [Dart](https://dart.dev/)(Konstantin Kai)

An approachable, portable, and productive language for high-quality apps on any platform

```shell
proto plugin add dart "github://KonstantinKai/proto-dart-plugin"
proto install dart
```

Available bins: `dart`, `dartaotruntime`

Globals directory: `$PUB_CACHE/bin`, `$HOME/.pub-cache/bin`

Detection sources: [`pubspec.yaml`](https://dart.dev/tools/pub/pubspec)

[TOML](https://github.com/risk1996/proto-plugins)

##### [dbmate](https://github.com/amacneil/dbmate)(risk1996)

A lightweight, framework-agnostic database migration tool.

```shell
proto plugin add dbmate "https://raw.githubusercontent.com/risk1996/proto-plugins/refs/heads/main/dbmate/plugin.toml"
proto install dbmate
```

Available bins: `dbmate`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/direnv)

##### [direnv](https://github.com/appthrust/proto-toml-plugins)(appthrust)

direnv is an extension for your shell. It augments existing shells with a new feature that can load and unload environment variables depending on the current directory.

```shell
proto plugin add direnv "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/direnv/plugin.toml"
proto install direnv
```

Available bins: `direnv`

[TOML](https://gist.github.com/alexbepple/9740643dbe1b2d423490b1fee21af807)

##### [dotenvx](https://dotenvx.com/)(alexbepple)

Inject your env at runtime. A better dotenv – from the creator of dotenv.

```shell
proto plugin add dotenvx "https://gist.githubusercontent.com/alexbepple/9740643dbe1b2d423490b1fee21af807/raw/e2d85b647da191d339dfbf3e3e1cefb21616e7c7/dotenvx.toml"
proto install dotenvx
```

Available bins: `dotenvx`

[TOML](https://github.com/RemiKalbe/proto-dotnet-plugin)

##### [.NET](https://dotnet.microsoft.com/)(RemiKalbe)

.NET is the free, open-source, cross-platform framework for building modern apps and powerful cloud services.

```shell
proto plugin add dotnet "https://raw.githubusercontent.com/RemiKalbe/proto-dotnet-plugin/main/plugin.toml"
proto install dotnet
```

Available bins: `dotnet`

Detection sources: [`global.json`](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json)

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [dprint](https://dprint.dev/)(Phault)

A pluggable and configurable code formatting platform written in Rust.

```shell
proto plugin add dprint "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/dprint/plugin.toml"
proto install dprint
```

Available bins: `dprint`

[TOML](https://github.com/theomessin/proto-toml-plugins/blob/master/earthly.toml)

##### [earthly](https://earthly.dev/)(theomessin)

Like Dockerfile and Makefile had a baby.

```shell
proto plugin add earthly "https://raw.githubusercontent.com/theomessin/proto-toml-plugins/master/earthly.toml"
proto install earthly
```

Available bins: `earthly`

[WASM](https://github.com/KonstantinKai/proto-flutter-plugin)

##### [Flutter](https://flutter.dev/)(Konstantin Kai)

Flutter is an open source framework for building beautiful, natively compiled, multi-platform applications from a single codebase.

```shell
proto plugin add flutter "github://KonstantinKai/proto-flutter-plugin"
proto install flutter
```

Available bins: `flutter`, `dart`

Globals directory: `$FLUTTER_ROOT/bin`

Detection sources: [`pubspec.yaml`](https://dart.dev/tools/pub/pubspec)

[TOML](https://github.com/b4nst/proto-plugins/blob/main/toml/flux.toml)

##### [flux](https://fluxcd.io/)(b4nst)

Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible.

```shell
proto plugin add flux "https://raw.githubusercontent.com/b4nst/proto-plugins/refs/heads/main/toml/flux.toml"
proto install flux
```

Available bins: `flux`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [flyctl](https://github.com/superfly/flyctl)(Phault)

A command-line interface for fly.io.

```shell
proto plugin add fly "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/flyctl/plugin.toml"
proto install fly
```

Available bins: `fly`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/fzf)

##### [fzf](https://github.com/appthrust/proto-toml-plugins)(appthrust)

fzf is a general-purpose command-line fuzzy finder.

```shell
proto plugin add fzf "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/fzf/plugin.toml"
proto install fzf
```

Available bins: `fzf`

[WASM](https://github.com/ageha734/proto-gcloud)

##### [Goocle Cloud SDK](https://cloud.google.com/sdk/docs)(ageha734)

The primary command-line tool for creating and managing Google Cloud resources.

```shell
proto plugin add gcloud "github://ageha734/proto-gcloud"
proto install gcloud
```

Available bins: `gcloud`

##### [GeoIPUpdate](https://dev.maxmind.com/geoip)(maxmind)

Updater for GeoIP2 and GeoLite databases.

```shell
proto plugin add geoipupdate "https://raw.githubusercontent.com/maxmind/geoipupdate/main/proto.yaml"
proto install geoipupdate
```

Available bins: `geoipupdate`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/gh)

##### [GitHub CLI](https://github.com/appthrust/proto-toml-plugins)(appthrust)

gh is GitHub on the command line.

```shell
proto plugin add gh "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/gh/plugin.toml"
proto install gh
```

Available bins: `gh`

[TOML](https://github.com/remenoscodes/git-native-issue)

##### [git-native-issue](https://github.com/remenoscodes/git-native-issue)(remenoscodes)

Distributed issue tracking embedded in Git — track issues locally, sync anywhere.

```shell
proto plugin add git-issue "https://raw.githubusercontent.com/remenoscodes/git-native-issue/main/proto/plugin.toml"
proto install git-issue
```

Available bins: `git-issue`

[WASM](https://github.com/muuvmuuv/proto-plugins)

##### [Gitleaks](https://github.com/gitleaks/gitleaks)(muuvmuuv)

A fast, light-weight, portable, and open-source secret scanner for Git repositories, files, and directories.

```shell
proto plugin add gitleaks "github://muuvmuuv/proto-plugins/gitleaks_tool"
proto install gitleaks
```

Available bins: `gitleaks`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Gitleaks](https://gitleaks.io/)(Phault)

A fast, light-weight, portable, and open-source secret scanner for Git repositories, files, and directories.

```shell
proto plugin add gitleaks "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/gitleaks/plugin.toml"
proto install gitleaks
```

Available bins: `gitleaks`

[TOML](https://github.com/vancegillies/proto-gleam-plugin/blob/main/gleam.toml)

##### [gleam](https://gleam.run/)(vancegillies)

A statically typed language for the Erlang VM and JavaScript.

```shell
proto plugin add gleam "https://raw.githubusercontent.com/vancegillies/proto-gleam-plugin/main/gleam.toml"
proto install gleam
```

Available bins: `gleam`

[TOML](https://github.com/stk0vrfl0w/proto-toml-plugins/blob/main/plugins/gojq.toml)

##### [gojq](https://github.com/itchyny/gojq)(stk0vrfl0w)

Pure Go implementation of jq.

```shell
proto plugin add gojq "https://raw.githubusercontent.com/stk0vrfl0w/proto-toml-plugins/main/plugins/gojq.toml"
proto install gojq
```

Available bins: `gojq`

[TOML](https://github.com/b4nst/proto-plugins/blob/main/toml/golangci-lint.toml)

##### [golangci-lint](https://golangci-lint.run/)(b4nst)

Fast linters runner for Go.

```shell
proto plugin add golangci-lint "https://raw.githubusercontent.com/b4nst/proto-plugins/refs/heads/main/toml/golangci-lint.toml"
proto install golangci-lint
```

Available bins: `golangci-lint`

[TOML](https://github.com/eplightning/openjdk-adoptium-proto-plugin/blob/main/build-plugins/gradle.toml)

##### [gradle](https://gradle.org/)(eplightning)

Gradle is the open source build system of choice for Java, Android, and Kotlin developers.

```shell
proto plugin add gradle "https://raw.githubusercontent.com/eplightning/openjdk-adoptium-proto-plugin/main/build-plugins/gradle.toml"
proto install gradle
```

Available bins: `gradle`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Gum](https://github.com/charmbracelet/gum)(Phault)

A tool for glamorous shell scripts.

```shell
proto plugin add gum "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/gum/plugin.toml"
proto install gum
```

Available bins: `gum`

[TOML](https://github.com/stk0vrfl0w/proto-toml-plugins/blob/main/plugins/helm.toml)

##### [helm](https://helm.sh/)(stk0vrfl0w)

The Kubernetes package manager.

```shell
proto plugin add helm "https://raw.githubusercontent.com/stk0vrfl0w/proto-toml-plugins/main/plugins/helm.toml"
proto install helm
```

Available bins: `helm`

[TOML](https://github.com/stk0vrfl0w/proto-toml-plugins/blob/main/plugins/helmfile.toml)

##### [helmfile](https://helmfile.readthedocs.io/en/latest)(stk0vrfl0w)

Deploy Kubernetes helm charts.

```shell
proto plugin add helmfile "https://raw.githubusercontent.com/stk0vrfl0w/proto-toml-plugins/main/plugins/helmfile.toml"
proto install helmfile
```

Available bins: `helmfile`

[TOML](https://github.com/z0rrn/proto-plugins)

##### [Hugo Standard](https://gohugo.io/)(z0rrn)

The world's fastest framework for building websites - standard version.

```shell
proto plugin add hugo "https://raw.githubusercontent.com/z0rrn/proto-plugins/main/hugo/plugin-standard.toml"
proto install hugo
```

Available bins: `hugo`

[TOML](https://github.com/z0rrn/proto-plugins)

##### [Hugo Extended](https://gohugo.io/)(z0rrn)

The world's fastest framework for building websites - extended version.

```shell
proto plugin add hugo "https://raw.githubusercontent.com/z0rrn/proto-plugins/main/hugo/plugin-extended.toml"
proto install hugo
```

Available bins: `hugo`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Hurl](https://hurl.dev/)(Phault)

A command line tool that runs HTTP requests defined in a simple plain text format.

```shell
proto plugin add hurl "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/hurl/plugin.toml"
proto install hurl
```

Available bins: `hurl`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [hyperfine](https://github.com/sharkdp/hyperfine)(Phault)

A command-line benchmarking tool.

```shell
proto plugin add hyperfine "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/hyperfine/plugin.toml"
proto install hyperfine
```

Available bins: `hyperfine`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Infisical](https://infisical.com/)(Phault)

The command-line interface for the open source secret management platform Infisical.

```shell
proto plugin add infisical "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/infisical/plugin.toml"
proto install infisical
```

Available bins: `infisical`

[TOML](https://github.com/Infisical/cli)

##### [Infisical CLI](https://infisical.com/)(9:06 PM)

The official Infisical CLI: Inject secrets into applications and manage your Infisical infrastructure.

```shell
proto plugin add infisical-cli "https://raw.githubusercontent.com/edocli/proto-plugins/main/infisical/plugin.toml"
proto install infisical-cli
```

Available bins: `infisical`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [JiraCLI](https://github.com/ankitpokhrel/jira-cli)(Phault)

An interactive command line tool for Atlassian Jira.

```shell
proto plugin add jira "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/jira/plugin.toml"
proto install jira
```

Available bins: `jira`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/jnv)

##### [jnv](https://github.com/appthrust/proto-toml-plugins)(appthrust)

jnv is designed for navigating JSON, offering an interactive JSON viewer and jq filter editor.

```shell
proto plugin add jnv "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/jnv/plugin.toml"
proto install jnv
```

Available bins: `jnv`

[WASM](https://github.com/muuvmuuv/proto-plugins)

##### [jq](https://jqlang.github.io/jq/)(muuvmuuv)

A lightweight and flexible command-line JSON processor.

```shell
proto plugin add jq "github://muuvmuuv/proto-plugins/jq_tool"
proto install jq
```

Available bins: `jq`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/jq)

##### [jq](https://github.com/appthrust/proto-toml-plugins)(appthrust)

jq is a lightweight and flexible command-line JSON processor akin to sed,awk,grep, and friends for JSON data.

```shell
proto plugin add jq "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/jq/plugin.toml"
proto install jq
```

Available bins: `jq`

[WASM](https://github.com/muuvmuuv/proto-plugins)

##### [just](https://github.com/casey/just)(muuvmuuv)

A handy way to save and run project-specific commands.

```shell
proto plugin add just "github://muuvmuuv/proto-plugins/just_tool"
proto install just
```

Available bins: `just`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [just](https://github.com/casey/just)(Phault)

A handy way to save and run project-specific commands.

```shell
proto plugin add just "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/just/plugin.toml"
proto install just
```

Available bins: `just`

[TOML](https://github.com/appthrust/proto-toml-plugins)

##### [k3d](https://k3d.io/)(appthrust)

k3d is a lightweight wrapper to run k3s (Rancher Lab's minimal Kubernetes distribution) in Docker.

```shell
proto plugin add k3d "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/k3d/plugin.toml"
proto install k3d
```

Available bins: `k3d`

[TOML](https://github.com/appthrust/proto-toml-plugins)

##### [k6](https://k6.io/)(appthrust)

Grafana k6 is an open-source load testing tool that makes performance testing easy and productive for engineering teams.

```shell
proto plugin add k6 "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/k6/plugin.toml"
proto install k6
```

Available bins: `k6`

[TOML](https://github.com/appthrust/proto-toml-plugins)

##### [k9s](https://k9scli.io/)(appthrust)

K9s provides a terminal UI to interact with your Kubernetes clusters.

```shell
proto plugin add k9s "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/k9s/plugin.toml"
proto install k9s
```

Available bins: `k9s`

[TOML](https://github.com/firleaf/proto-toml-plugins)

##### [kompose](https://kompose.io/)(firleaf)

Go from Docker Compose to Kubernetes.

```shell
proto plugin add kompose "https://raw.githubusercontent.com/firleaf/proto-toml-plugins/main/plugins/kompose.toml"
proto install kompose
```

Available bins: `kompose`

[TOML](https://github.com/trillion-labs/proto-plugins)

##### [kubectl](https://kubernetes.io/)(Trillion Labs)

Kubernetes command line tool.

```shell
proto plugin add kubectl "https://raw.githubusercontent.com/trillion-labs/proto-plugins/refs/heads/main/kubectl.toml"
proto install kubectl
```

Available bins: `kubectl`

[TOML](https://github.com/firleaf/proto-toml-plugins)

##### [kubeseal](https://github.com/bitnami-labs/sealed-secrets)(firleaf)

Sealed Secrets CLI.

```shell
proto plugin add kubeseal "https://raw.githubusercontent.com/firleaf/proto-toml-plugins/main/plugins/kubeseal.toml"
proto install kubeseal
```

Available bins: `kubeseal`

[TOML](https://github.com/ageha734/proto-plugins)

##### [kustomize](https://kustomize.io/)(ageha734)

A tool for customizing Kubernetes YAML files without using templates.

```shell
proto plugin add kustomize "https://raw.githubusercontent.com/ageha734/proto-plugins/refs/heads/master/toml/kustomize.toml"
proto install kustomize
```

Available bins: `kustomize`

[TOML](https://github.com/ageha734/proto-plugins)

##### [lefthook](https://lefthook.dev/)(ageha734)

A fast, multilingual Git hook manager.

```shell
proto plugin add lefthook "https://raw.githubusercontent.com/ageha734/proto-plugins/refs/heads/master/toml/lefthook.toml"
proto install lefthook
```

Available bins: `lefthook`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Mage](https://magefile.org/)(Phault)

A make/rake-like build tool using Go.

```shell
proto plugin add mage "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/mage/plugin.toml"
proto install mage
```

Available bins: `mage`

[TOML](https://github.com/jamesukiyo/proto-plugins)

##### [migrate](https://github.com/golang-migrate/migrate)(jamesukiyo)

Database migrations. CLI and Golang library.

```shell
proto plugin add migrate "https://raw.githubusercontent.com/jamesukiyo/proto-plugins/master/migrate.toml"
proto install migrate
```

Available bins: `migrate`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/mise)

##### [mise](https://mise.jdx.dev/)(appthrust)

dev tools, env vars, task runner

```shell
proto plugin add mise "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/mise/plugin.toml"
proto install mise
```

Available bins: `mise`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [mkcert](https://github.com/FiloSottile/mkcert)(Phault)

A simple zero-config tool to make locally trusted development certificates with any names you'd like.

```shell
proto plugin add mkcert "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/mkcert/plugin.toml"
proto install mkcert
```

Available bins: `mkcert`

[TOML](https://github.com/crashdump/proto-tools)

##### [mockery](https://github.com/vektra/mockery)(crashdump)

Mockery is a mock code autogenerator for Go.

```shell
proto plugin add mockery "https://raw.githubusercontent.com/crashdump/proto-tools/main/toml-plugins/mockery/plugin.toml"
proto install mockery
```

Available bins: `mockery`

[TOML](https://github.com/yuhua99/proto-toml-plugins)

##### [Neovim](https://neovim.io/)(yuhua99)

Hyperextensible Vim-based text editor.

```shell
proto plugin add neovim "https://raw.githubusercontent.com/yuhua99/proto-toml-plugins/refs/heads/main/neovim/neovim.toml"
proto install neovim
```

Available bins: `nvim`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Ninja](https://ninja-build.org/)(Phault)

A small build system with a focus on speed.

```shell
proto plugin add ninja "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/ninja/plugin.toml"
proto install ninja
```

Available bins: `ninja`

[WASM](https://github.com/Hebilicious/proto-nu)

##### [Nushell](https://www.nushell.sh/)(Hebilicious)

A modern shell written in Rust with structured data pipelines.

```shell
proto plugin add nu "github://Hebilicious/proto-nu"
proto install nu
```

Available bins: `nu`, `nu_plugin_custom_values`, `nu_plugin_example`, `nu_plugin_formats`, `nu_plugin_gstat`, `nu_plugin_inc`, `nu_plugin_polars`, `nu_plugin_query`, `nu_plugin_stress_internals`

Detection sources: `.nu-version`, `.nushell-version`

[WASM](https://github.com/Hebilicious/proto-ocaml)

##### [OCaml](https://ocaml.org/)(Hebilicious)

The OCaml compiler toolchain, powered by opam and dune.

```shell
proto plugin add ocaml "github://Hebilicious/proto-ocaml"
proto install ocaml
```

Available bins: `dune`, `ocaml`, `ocamlc`, `ocamldep`, `ocamlopt`, `opam`

Detection sources: `.ocaml-version`, [`dune-project`](https://dune.readthedocs.io/en/stable/reference/dune-project/index.html)

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Octopus CLI](https://octopus.com/)(Phault)

Command line interface for Octopus Deploy.

```shell
proto plugin add octopus "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/octopus/plugin.toml"
proto install octopus
```

Available bins: `octopus`

[TOML](https://github.com/ngoldack/proto-tools)

##### [openapi-changes](https://github.com/pb33f/openapi-changes)(ngoldack)

The world's sexiest OpenAPI breaking changes detector. Discover what changed between two OpenAPI specs, or a single spec over time. Supports OpenAPI 3.1, 3.0 and Swagger.

```shell
proto plugin add openapi-changes "https://raw.githubusercontent.com/ngoldack/proto-tools/main/tools/openapi-changes/openapi-changes.toml"
proto install openapi-changes
```

Available bins: `openapi-changes`

[TOML](https://github.com/crashdump/proto-tools)

##### [openfga](https://openfga.dev/)(crashdump)

OpenFGA is an open-source authorization solution that allows developers to build granular access control.

```shell
proto plugin add openfga "https://raw.githubusercontent.com/crashdump/proto-tools/main/toml-plugins/openfga/plugin.toml"
proto install openfga
```

Available bins: `openfga`

[WASM](https://github.com/eplightning/openjdk-adoptium-proto-plugin)

##### [Eclipse Adoptium OpenJDK](https://adoptium.net/)(eplightning)

Eclipse Adoptium OpenJDK is an open-source distribution of the Java Development Kit.

```shell
proto plugin add openjdk "github://eplightning/openjdk-adoptium-proto-plugin"
proto install openjdk
```

Available bins: `java`, `javac`, `jar`, `javadoc`, `keytool`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [oxlint](https://oxc-project.github.io/)(Phault)

Oxlint is a JavaScript linter designed to catch erroneous or useless code without requiring any configurations by default.

```shell
proto plugin add oxlint "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/oxlint/plugin.toml"
proto install oxlint
```

Available bins: `oxlint`

[TOML](https://github.com/b4nst/proto-plugins/blob/main/toml/packer.toml)

##### [packer](https://www.packer.io/)(b4nst)

Create identical images for multiple platforms from a single source configuration.

```shell
proto plugin add packer "https://raw.githubusercontent.com/b4nst/proto-plugins/main/toml/packer.toml"
proto install packer
```

Available bins: `packer`

[WASM](https://github.com/KonstantinKai/proto-php-plugin)

##### [PHP](https://www.php.net/)(Konstantin Kai)

A popular general-purpose scripting language that is especially suited to web development.

```shell
proto plugin add php "github://KonstantinKai/proto-php-plugin"
proto install php
```

Available bins: `php`

Detection sources: `.php-version`, [`composer.json`](https://getcomposer.org/doc/04-schema.md#require)

[TOML](https://github.com/milesj/proto-plugins/blob/master/pkl.toml)

##### [pkl](https://pkl-lang.org/)(milesj)

Configuration that is Programmable, Scalable, and Safe.

```shell
proto plugin add pkl "https://raw.githubusercontent.com/milesj/proto-plugins/refs/heads/master/pkl.toml"
proto install pkl
```

Available bins: `pkl`

[TOML](https://github.com/b4nst/proto-plugins/blob/main/toml/protoc.toml)

##### [protoc](https://github.com/protocolbuffers/protobuf)(b4nst)

Protocol Buffers - Google's data interchange format.

```shell
proto plugin add protoc "https://raw.githubusercontent.com/b4nst/proto-plugins/refs/heads/main/toml/protoc.toml"
proto install protoc
```

Available bins: `protoc`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [rattler-build](https://prefix-dev.github.io/rattler-build/)(Phault)

A fast Conda package builder.

```shell
proto plugin add rattler-build "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/rattler-build/plugin.toml"
proto install rattler-build
```

Available bins: `rattler-build`

[TOML](https://github.com/restatedev/restate)

##### [restate](https://github.com/restatedev/restate)(jacobdrury)

A command-line tool for interacting with Restate

```shell
proto plugin add restate "https://raw.githubusercontent.com/jacobdrury/proto-plugins/refs/heads/master/restate.toml"
proto install restate
```

Available bins: `restate`

[TOML](https://github.com/restatedev/restate)

##### [restate-server](https://github.com/restatedev/restate)(jacobdrury)

A command-line tool for running a Restate server locally

```shell
proto plugin add restate-server "https://raw.githubusercontent.com/jacobdrury/proto-plugins/refs/heads/master/restate-server.toml"
proto install restate-server
```

Available bins: `restate-server`

[TOML](https://github.com/restatedev/restate)

##### [restatectl](https://github.com/restatedev/restate)(jacobdrury)

A command-line tool for managing Restate clusters.

```shell
proto plugin add restatectl "https://raw.githubusercontent.com/jacobdrury/proto-plugins/refs/heads/master/restatectl.toml"
proto install restatectl
```

Available bins: `restatectl`

[TOML](https://github.com/risk1996/proto-plugins)

##### [Ruff](https://docs.astral.sh/ruff/)(risk1996)

An extremely fast Python linter and code formatter, written in Rust.

```shell
proto plugin add ruff "https://raw.githubusercontent.com/risk1996/proto-plugins/refs/heads/main/ruff/plugin.toml"
proto install ruff
```

Available bins: `ruff`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Ruff](https://docs.astral.sh/ruff/)(Phault)

An extremely fast Python linter and code formatter.

```shell
proto plugin add ruff "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/ruff/plugin.toml"
proto install ruff
```

Available bins: `ruff`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/rye)

##### [Rye](https://github.com/appthrust/proto-toml-plugins)(appthrust)

Rye is a comprehensive project and package management solution for Python.

```shell
proto plugin add rye "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/rye/plugin.toml"
proto install rye
```

Available bins: `rye`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/sccache)

##### [sccache](https://github.com/mozilla/sccache)(appthrust)

Sccache is a ccache-like tool. It is used as a compiler wrapper and avoids compilation when possible. Sccache has the capability to utilize caching in remote storage environments, including various cloud storage options, or alternatively, in local storage.

```shell
proto plugin add sccache "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/sccache/plugin.toml"
proto install sccache
```

Available bins: `sccache`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [ShellCheck](https://github.com/koalaman/shellcheck)(Phault)

A static analysis tool for shell scripts.

```shell
proto plugin add shellcheck "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/shellcheck/plugin.toml"
proto install shellcheck
```

Available bins: `shellcheck`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [shfmt](https://github.com/mvdan/sh)(Phault)

A shell formatter for POSIX Shell, Bash and mksh.

```shell
proto plugin add shfmt "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/shfmt/plugin.toml"
proto install shfmt
```

Available bins: `shfmt`

[TOML](https://github.com/stk0vrfl0w/proto-toml-plugins/blob/main/plugins/sops.toml)

##### [sops](https://github.com/getsops/sops)(stk0vrfl0w)

Simple and flexible tool for managing secrets.

```shell
proto plugin add sops "https://raw.githubusercontent.com/stk0vrfl0w/proto-toml-plugins/main/plugins/sops.toml"
proto install sops
```

Available bins: `sops`

[TOML](https://github.com/jamesukiyo/proto-plugins)

##### [sqlc](https://github.com/sqlc-dev/sqlc)(jamesukiyo)

Generate type-safe code from SQL

```shell
proto plugin add sqlc "https://raw.githubusercontent.com/jamesukiyo/proto-plugins/master/sqlc.toml"
proto install sqlc
```

Available bins: `sqlc`

[TOML](https://github.com/T0rvadaL/proto-plugins)

##### [sqruff](https://github.com/quarylabs/sqruff)(T0rvadaL)

Fast SQL formatter/linter.

```shell
proto plugin add sqruff "https://raw.githubusercontent.com/T0rvadaL/proto-plugins/main/sqruff.toml"
proto install sqruff
```

Available bins: `sqruff`

[TOML](https://github.com/crashdump/proto-tools)

##### [staticcheck](https://staticcheck.dev/)(crashdump)

Staticcheck is a state of the art linter for the Go programming language. Using static analysis, it finds bugs and performance issues, offers simplifications, and enforces style rules.

```shell
proto plugin add staticcheck "https://raw.githubusercontent.com/crashdump/proto-tools/main/toml-plugins/staticcheck/plugin.toml"
proto install staticcheck
```

Available bins: `staticcheck`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/stern)

##### [stern](https://github.com/appthrust/proto-toml-plugins)(appthrust)

Stern allows you to tail multiple pods on Kubernetes and multiple containers within the pod.

```shell
proto plugin add stern "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/stern/plugin.toml"
proto install stern
```

Available bins: `stern`

[TOML](https://github.com/T0rvadaL/proto-plugins)

##### [Strawberry Perl](https://strawberryperl.com/)(T0rvadaL)

The Perl for MS Windows, free of charge!

```shell
proto plugin add strawberry-perl "https://github.com/T0rvadaL/proto-plugins/blob/main/strawberry-perl.toml"
proto install strawberry-perl
```

Available bins: `perl`, `cpan`, `perldoc`, `prove`, `portableshell`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Task](https://taskfile.dev/)(Phault)

Task is a task runner / build tool that aims to be simpler and easier to use than, for example, GNU Make.

```shell
proto plugin add task "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/task/plugin.toml"
proto install task
```

Available bins: `task`

[TOML](https://github.com/theomessin/proto-toml-plugins/blob/master/terraform.toml)

##### [terraform](https://www.terraform.io/)(theomessin)

Provision & Manage any Infrastructure.

```shell
proto plugin add terraform "https://raw.githubusercontent.com/theomessin/proto-toml-plugins/master/terraform.toml"
proto install terraform
```

Available bins: `terraform`

Detection sources: [`.terraform-version`](https://github.com/tfutils/tfenv#terraform-version-file)

[TOML](https://github.com/ageha734/proto-plugins)

##### [terraform-docs](https://terraform-docs.io/)(ageha734)

A utility to generate Terraform module documentation in various formats.

```shell
proto plugin add terraform-docs "https://raw.githubusercontent.com/ageha734/proto-plugins/refs/heads/master/toml/terraform-docs.toml"
proto install terraform-docs
```

Available bins: `terraform-docs`

[TOML](https://github.com/stk0vrfl0w/proto-toml-plugins/blob/main/plugins/terragrunt.toml)

##### [terragrunt](https://terragrunt.gruntwork.io/)(stk0vrfl0w)

Thin wrapper that provides extra tools for keeping your terraform configurations DRY.

```shell
proto plugin add terragrunt "https://raw.githubusercontent.com/stk0vrfl0w/proto-toml-plugins/main/plugins/terragrunt.toml"
proto install terragrunt
```

Available bins: `terragrunt`

[TOML](https://github.com/crashdump/proto-tools)

##### [tflint](https://github.com/terraform-linters/tflint)(crashdump)

A Pluggable Terraform Linter.

```shell
proto plugin add tflint "https://raw.githubusercontent.com/crashdump/proto-tools/refs/heads/main/toml-plugins/tflint/plugin.toml"
proto install tflint
```

Available bins: `tflint`

[TOML](https://github.com/appthrust/proto-toml-plugins)

##### [tilt](https://tilt.dev/)(appthrust)

A toolkit for fixing the pains of microservice development.

```shell
proto plugin add tilt "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/tilt/plugin.toml"
proto install tilt
```

Available bins: `tilt`

[TOML](https://github.com/stefanprodan/timoni)

##### [timoni](https://timoni.sh/)(b4nst)

Distribution and lifecycle management for cloud-native applications.

```shell
proto plugin add timoni "https://raw.githubusercontent.com/stefanprodan/timoni/main/proto-plugin.toml"
proto install timoni
```

Available bins: `timoni`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/tofu)

##### [OpenTofu](https://opentofu.org/)(appthrust)

OpenTofu lets you declaratively manage your cloud infrastructure.

```shell
proto plugin add tofu "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/tofu/plugin.toml"
proto install tofu
```

Available bins: `tofu`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Traefik](https://traefik.io/)(Phault)

A modern HTTP reverse proxy and load balancer that makes deploying microservices easy.

```shell
proto plugin add traefik "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/traefik/plugin.toml"
proto install traefik
```

Available bins: `traefik`

[TOML](https://github.com/ageha734/proto-plugins)

##### [trivy](https://trivy.dev/)(ageha734)

A comprehensive security scanner that detects vulnerabilities and misconfigurations in container images, file systems, Git repositories, and more.

```shell
proto plugin add trivy "https://raw.githubusercontent.com/ageha734/proto-plugins/refs/heads/master/toml/trivy.toml"
proto install trivy
```

Available bins: `trivy`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [TruffleHog](https://github.com/trufflesecurity/trufflehog)(Phault)

Find and verify credentials.

```shell
proto plugin add trufflehog "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/trufflehog/plugin.toml"
proto install trufflehog
```

Available bins: `trufflehog`

[TOML](https://github.com/yuhua99/proto-toml-plugins)

##### [ty](https://docs.astral.sh/ty/)(yuhua99)

An extremely fast Python type checker and language server, written in Rust.

```shell
proto plugin add ty "https://raw.githubusercontent.com/yuhua99/proto-toml-plugins/refs/heads/main/ty/ty.toml"
proto install ty
```

Available bins: `ty`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [uv](https://github.com/astral-sh/uv)(Phault)

An extremely fast Python package installer and resolver.

```shell
proto plugin add uv "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/uv/plugin.toml"
proto install uv
```

Available bins: `uv`

[TOML](https://github.com/risk1996/proto-plugins)

##### [vale](https://vale.sh/)(risk1996)

Vale is an open-source, command-line tool that brings your editorial style guide to life.

```shell
proto plugin add vale "https://raw.githubusercontent.com/risk1996/proto-plugins/refs/heads/main/vale/plugin.toml"
proto install vale
```

Available bins: `vale`

[TOML](https://github.com/isaac10334/wasmtime-proto)

##### [Wasmtime](https://wasmtime.dev/)(isaac10334)

A lightweight WebAssembly runtime that is fast, secure, and standards-compliant.

```shell
proto plugin add wasmtime "https://raw.githubusercontent.com/isaac10334/wasmtime-proto/master/wasmtime.toml"
proto install wasmtime
```

Available bins: `wasmtime`

[TOML](https://github.com/ngoldack/proto-tools)

##### [wiretap](https://github.com/pb33f/wiretap)(ngoldack)

The world's coolest API Validation and compliance tool. Validate APIs against OpenAPI specifications and much more.

```shell
proto plugin add wiretap "https://raw.githubusercontent.com/ngoldack/proto-tools/main/tools/wiretap/wiretap.toml"
proto install wiretap
```

Available bins: `wiretap`

[TOML](https://github.com/Phault/proto-toml-plugins)

##### [Wizer](https://github.com/bytecodealliance/wizer)(Phault)

The WebAssembly Pre-Initializer.

```shell
proto plugin add wizer "https://raw.githubusercontent.com/Phault/proto-toml-plugins/main/wizer/plugin.toml"
proto install wizer
```

Available bins: `wizer`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/xcodes)

##### [xcodes](https://github.com/XcodesOrg/xcodes)(appthrust)

xcodes is the command-line tool to install and switch between multiple versions of Xcode.

```shell
proto plugin add xcodes "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/xcodes/plugin.toml"
proto install xcodes
```

Available bins: `xcodes`

[TOML](https://github.com/davearel/proto-plugins/tree/main/xurl)

##### [xurl](https://github.com/xdevplatform/xurl)(davearel)

A curl-like command-line tool for interacting with the X (formerly Twitter) API, with built in authentication.

```shell
proto plugin add xurl "https://raw.githubusercontent.com/davearel/proto-plugins/main/xurl/plugin.toml"
proto install xurl
```

Available bins: `xurl`

[WASM](https://github.com/muuvmuuv/proto-plugins)

##### [yq](https://github.com/mikefarah/yq)(muuvmuuv)

A portable command-line YAML, JSON, XML, CSV, TOML, and properties processor.

```shell
proto plugin add yq "github://muuvmuuv/proto-plugins/yq_tool"
proto install yq
```

Available bins: `yq`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/yq)

##### [yq](https://mikefarah.gitbook.io/yq/)(appthrust)

yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor

```shell
proto plugin add yq "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/yq/plugin.toml"
proto install yq
```

Available bins: `yq`

[TOML](https://github.com/appthrust/proto-toml-plugins/tree/main/zellij)

##### [Zellij](https://github.com/appthrust/proto-toml-plugins)(appthrust)

Zellij is a terminal workspace.

```shell
proto plugin add zellij "https://raw.githubusercontent.com/appthrust/proto-toml-plugins/main/zellij/plugin.toml"
proto install zellij
```

Available bins: `zellij`

[TOML](https://github.com/stk0vrfl0w/proto-toml-plugins/blob/main/plugins/zig.toml)

##### [Zig](https://ziglang.org/)(stk0vrfl0w)

Zig is a general-purpose programming language and toolchain.

```shell
proto plugin add zig "https://raw.githubusercontent.com/stk0vrfl0w/proto-toml-plugins/main/plugins/zig.toml"
proto install zig
```

Available bins: `zig`

[WASM](https://github.com/konomae/zig-plugin)

##### [Zig](https://ziglang.org/)(konomae)

Zig is a general-purpose programming language and toolchain.

```shell
proto plugin add zig "github://konomae/zig-plugin"
proto install zig
```

Available bins: `zig`

[WASM](https://github.com/konomae/zls-plugin)

##### [zls](https://github.com/zigtools/zls)(konomae)

The Zig language server for all your Zig editor.

```shell
proto plugin add zls "github://konomae/zls-plugin"
proto install zls
```

Available bins: `zls`

- [Built-in](https://moonrepo.dev/docs/proto/tools#built-in)
- [Third-party](https://moonrepo.dev/docs/proto/tools#third-party)