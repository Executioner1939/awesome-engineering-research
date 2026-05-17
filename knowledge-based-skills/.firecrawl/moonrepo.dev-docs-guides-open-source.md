[Skip to main content](https://moonrepo.dev/docs/guides/open-source#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Although moon was designed for large monorepos, it can also be used for open source projects,
especially when coupled with our [built-in continuous integration support](https://moonrepo.dev/docs/guides/ci).

However, a pain point with moon is that it has an explicitly configured version for each tool in the
[toolchain](https://moonrepo.dev/docs/concepts/toolchain), but open source projects typically need to run checks against
multiple versions! To mitigate this problem, you can set the matrix value as an environment
variable, in the format of `MOON_<TOOLCHAIN>_VERSION`.

.github/workflows/ci.yml

```yaml
name: 'Pipeline'
on:
  push:
    branches:
      - 'master'
  pull_request:
jobs:
  ci:
    name: 'CI'
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: ['ubuntu-latest', 'windows-latest']
        node-version: [20, 22, 24]
    steps:
      # Checkout repository
      - uses: 'actions/checkout@v4'
        with:
          fetch-depth: 0
      # Install Node.js
      - uses: 'actions/setup-node@v6'
      # Install dependencies
      - run: 'yarn install --immutable'
      # Run moon and affected tasks
      - run: 'yarn moon ci'
        env:
          MOON_NODE_VERSION: ${{ matrix.node-version }}
```

info

This example is only for GitHub actions, but the same mechanism can be applied to other CI
environments.

## Reporting run results [​](https://moonrepo.dev/docs/guides/open-source\#reporting-run-results "Direct link to Reporting run results")

We also suggest using our
[`moonrepo/run-report-action`](https://github.com/marketplace/actions/moon-ci-run-reports) GitHub
action. This action will report the results of a [`moon ci`](https://moonrepo.dev/docs/commands/ci) run to a pull request
as a comment and workflow summary.

.github/workflows/ci.yml

```yaml
# ...
jobs:
  ci:
    name: 'CI'
    runs-on: 'ubuntu-latest'
    steps:
      # ...
      - run: 'yarn moon ci'
      - uses: 'moonrepo/run-report-action@v1'
        if: success() || failure()
        with:
          access-token: ${{ secrets.GITHUB_TOKEN }}
```

The report looks something like the following:

![](https://moonrepo.dev/assets/images/run-report-41cffa17cd530ab8cca5cef47b38dcfd.png)

- [Reporting run results](https://moonrepo.dev/docs/guides/open-source#reporting-run-results)