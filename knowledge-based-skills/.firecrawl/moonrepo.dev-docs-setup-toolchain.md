[Skip to main content](https://moonrepo.dev/docs/setup-toolchain#__docusaurus_skipToContent_fallback)

BunDenoGoNode.jsPHPPythonRubyRust

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

5 min

One of moon's most powerful features is the [toolchain](https://moonrepo.dev/docs/concepts/toolchain), which automatically
manages, downloads, and installs Node.js and other languages behind the scenes using
[proto](https://moonrepo.dev/proto). It also enables [advanced functionality](https://moonrepo.dev/docs/how-it-works/languages#tier-2--platform)
for task running based on the platform (language and environment combination) it runs in.

The toolchain is configured with [`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain).

tip

Change the language dropdown at the top right to switch the examples!

## How it works [​](https://moonrepo.dev/docs/setup-toolchain\#how-it-works "Direct link to How it works")

For more information on the toolchain, our tier based support, and how languages integrate into
moon, refer to the official ["how it works" language guide](https://moonrepo.dev/docs/how-it-works/languages) and the
[toolchain concept](https://moonrepo.dev/docs/concepts/toolchain) documentation!

info

The toolchain is optional but helps to solve an array of issues that developers face in their
day-to-day.

## Enabling a toolchain [​](https://moonrepo.dev/docs/setup-toolchain\#enabling-a-toolchain "Direct link to Enabling a toolchain")

By default all tasks run through the
[system toolchain](https://moonrepo.dev/docs/how-it-works/languages#system-language-and-toolchain) and inherit _no_ special
functionality. If you want to take advantage of this functionality, like dependency hashing, package
shorthand execution, and lockfile management, you'll need to enable the toolchain in
[`.moon/toolchains.*`](https://moonrepo.dev/docs/config/toolchain). Otherwise, you can skip to the
[create a task](https://moonrepo.dev/docs/create-task) guide.

Begin by declaring the necessary configuration block, even if an empty object! This configuration
can also be injected using the [`moon toolchain add <toolchain>`](https://moonrepo.dev/docs/commands/toolchain/add) command
(doesn't support all languages).

.moon/toolchains.yml

```yaml
javascript:
  packageManager: 'yarn'

node: {}

yarn: {}
```

Although we've enabled the toolchain, language binaries must exist on `PATH` for task execution to
function correctly. Continue reading to learn how to automate this flow using tier 3 support.

## Automatically installing a tool [​](https://moonrepo.dev/docs/setup-toolchain\#automatically-installing-a-tool "Direct link to Automatically installing a tool")

One of the best features of moon is its integrated toolchain and automatic download and installation
of programming languages (when supported), for all developers and machines that moon runs on. This
feature solves the following pain points:

- Developers running tasks using different versions of languages.
- Version drift of languages between machines.
- Languages being installed through different version managers or install scripts.
- Language binaries not existing on `PATH`.
- How shell profiles should be configured.

If you have dealt with any of these pain points before and would like to eliminate them for you and
all your developers, you can try enabling moon's tier 3 support for supported tools. This is easily
done by defining the `version` field for each toolchain.

.moon/toolchains.yml

```yaml
javascript:
  packageManager: 'yarn'

node:
  version: '20.0.0'

yarn:
  version: '4.0.0'
```

When the `version` field is configured, moon will download and install the tool when a related task
is executed for the first time! It will also set the correct `PATH` lookups and environment
variables automatically. Amazing right?

## Next steps [​](https://moonrepo.dev/docs/setup-toolchain\#next-steps "Direct link to Next steps")

[Create a task](https://moonrepo.dev/docs/create-task) [Configure `.moon/toolchains.yml` further](https://moonrepo.dev/docs/config/toolchain) [Learn about the toolchain](https://moonrepo.dev/docs/concepts/toolchain)

- [How it works](https://moonrepo.dev/docs/setup-toolchain#how-it-works)
- [Enabling a toolchain](https://moonrepo.dev/docs/setup-toolchain#enabling-a-toolchain)
- [Automatically installing a tool](https://moonrepo.dev/docs/setup-toolchain#automatically-installing-a-tool)
- [Next steps](https://moonrepo.dev/docs/setup-toolchain#next-steps)