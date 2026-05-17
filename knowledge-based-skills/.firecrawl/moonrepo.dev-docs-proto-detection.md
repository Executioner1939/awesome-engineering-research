[Skip to main content](https://moonrepo.dev/docs/proto/detection#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

2 min

The most powerful feature in proto is its contextual version detection, that is triggered with
[`proto run`](https://moonrepo.dev/docs/proto/commands/run), [`proto bin`](https://moonrepo.dev/docs/proto/commands/bin), or when a shim is executed. So what
does this mean exactly? Before a tool in proto's toolchain can be executed, we need to determine the
version of the tool to execute with. If a detected version exists locally, we proceed using that
binary, otherwise we fail with a missing installation error.

When detecting a version, the following steps are checked, in the order as listed:

#### 1\. Version is explicitly passed as a command line argument [​](https://moonrepo.dev/docs/proto/detection\#1-version-is-explicitly-passed-as-a-command-line-argument "Direct link to 1. Version is explicitly passed as a command line argument")

```shell
$ proto run node 24.0.0
```

#### 2\. Version is provided with the `PROTO_*_VERSION` environment variable [​](https://moonrepo.dev/docs/proto/detection\#2-version-is-provided-with-the-proto__version-environment-variable "Direct link to 2-version-is-provided-with-the-proto__version-environment-variable")

```shell
$ PROTO_NODE_VERSION=24.0.0 proto run node
```

#### 3\. Version is located by traversing the file system [​](https://moonrepo.dev/docs/proto/detection\#3-version-is-located-by-traversing-the-file-system "Direct link to 3. Version is located by traversing the file system")

This step will attempt to find a configuration or manifest file in the current working directory,
and traverse upwards through parent directories (stops at the user's home directory) until a file is
found.

##### 3.1. Version is defined locally in `.prototools` [​](https://moonrepo.dev/docs/proto/detection\#31-version-is-defined-locally-in-prototools "Direct link to 31-version-is-defined-locally-in-prototools")

A `.prototools` file was found and a version entry exists for the current tool. This is also known
as a "local version" and can be created with [`proto pin`](https://moonrepo.dev/docs/proto/commands/pin).

.prototools

```toml
node = "24.0.0"
```

##### 3.2. Version is defined in the tool's ecosystem [​](https://moonrepo.dev/docs/proto/detection\#32-version-is-defined-in-the-tools-ecosystem "Direct link to 3.2. Version is defined in the tool's ecosystem")

Depending on the tool, a version is extracted from a found file unique to that tool's ecosystem.
This includes version manager configs (`.nvmrc`, etc), manifest files (`package.json`, etc), and
more.

.nvmrc

```text
24.0.0
```

package.json

```json
{
  "devEngines": {
    "runtime": {
      "name": "node",
      "version": "24.0.0"
    },
    "packageManager": {
      "name": "npm",
      "version": "11.0.0"
    }
  }
}
```

#### 4\. Version is defined globally [​](https://moonrepo.dev/docs/proto/detection\#4-version-is-defined-globally "Direct link to 4. Version is defined globally")

As the last check, we look for a "global version" that was pinned with
[`proto pin --global`](https://moonrepo.dev/docs/proto/commands/pin) or [`proto install --pin`](https://moonrepo.dev/docs/proto/commands/install). This version
is stored at `~/.proto/.prototools` (`%USERPROFILE%\.proto\.prototools` on Windows).

#### 5\. Version _could not_ be detected [​](https://moonrepo.dev/docs/proto/detection\#5-version-could-not-be-detected "Direct link to 5-version-could-not-be-detected")

If all the previous steps have failed, then we could not detect an applicable version, and the
process will fail.

- [1\. Version is explicitly passed as a command line argument](https://moonrepo.dev/docs/proto/detection#1-version-is-explicitly-passed-as-a-command-line-argument)
- [2\. Version is provided with the `PROTO_*_VERSION` environment variable](https://moonrepo.dev/docs/proto/detection#2-version-is-provided-with-the-proto__version-environment-variable)
- [3\. Version is located by traversing the file system](https://moonrepo.dev/docs/proto/detection#3-version-is-located-by-traversing-the-file-system)
  - [3.1. Version is defined locally in `.prototools`](https://moonrepo.dev/docs/proto/detection#31-version-is-defined-locally-in-prototools)
  - [3.2. Version is defined in the tool's ecosystem](https://moonrepo.dev/docs/proto/detection#32-version-is-defined-in-the-tools-ecosystem)
- [4\. Version is defined globally](https://moonrepo.dev/docs/proto/detection#4-version-is-defined-globally)
- [5\. Version _could not_ be detected](https://moonrepo.dev/docs/proto/detection#5-version-could-not-be-detected)