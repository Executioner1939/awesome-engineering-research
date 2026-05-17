[Skip to main content](https://moonrepo.dev/docs/guides/ci#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

All companies and projects rely on continuous integration (CI) to ensure high quality code and to
avoid regressions. Because this is such a critical piece of every developer's workflow, we wanted to
support it as a first-class feature within moon, and we do just that with the
[`moon ci`](https://moonrepo.dev/docs/commands/ci) command.

## How it works [​](https://moonrepo.dev/docs/guides/ci\#how-it-works "Direct link to How it works")

The `ci` command does all the heavy lifting necessary for effectively running jobs. It achieves this
by automatically running the following steps:

- Determines changed files by comparing the current HEAD against a base.
- Determines all [targets](https://moonrepo.dev/docs/concepts/target) that need to run based on changed files.
- Additionally runs affected [targets](https://moonrepo.dev/docs/concepts/target) dependencies _and_ dependents.
- Generates an action and dependency graph.
- Installs the toolchain and applicable dependencies.
- Runs all actions within the graph using a thread pool.
- Displays stats about all passing, failed, and invalid actions.

## Configuring tasks [​](https://moonrepo.dev/docs/guides/ci\#configuring-tasks "Direct link to Configuring tasks")

By default, _all tasks_ run in CI, as you should always be building, linting, typechecking, testing,
so on and so forth. However, this isn't always true, so this can be disabled on a per-task basis
through the [`runInCI`](https://moonrepo.dev/docs/config/project#runinci) option.

```yaml
tasks:
  dev:
    command: 'webpack server'
    options:
      runInCI: false
```

caution

This option _must_ be set to false for tasks that spawn a long-running or never-ending process, like
HTTP or development servers. To help mitigate this, tasks named `dev`, `start`, or `serve` are false
by default.

## Integrating [​](https://moonrepo.dev/docs/guides/ci\#integrating "Direct link to Integrating")

The following examples can be referenced for setting up moon and its CI workflow in popular
providers. For GitHub, we're using our
[`setup-toolchain` action](https://github.com/moonrepo/setup-toolchain) to install moon. For other
providers, we assume moon is an npm dependency and must be installed with Node.js.

- GitHub
- Buildkite
- CircleCI
- TravisCI

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
    runs-on: 'ubuntu-latest'
    steps:
      - uses: 'actions/checkout@v4'
        with:
          fetch-depth: 0
      - uses: 'moonrepo/setup-toolchain@v0'
      - run: 'moon ci'
```

.buildkite/pipeline.yml

```yaml
steps:
  - label: 'CI'
    commands:
      - 'moon ci'
```

.circleci/config.yml

```yaml
version: 2.1
jobs:
  ci:
    docker:
      - image: 'cimg/base:stable'
    steps:
      - 'checkout'
      - run: 'moon ci'
workflows:
  pipeline:
    jobs:
      - 'ci'
```

.travis.yml

```yaml
language: 'node_js'
script: 'moon ci'
```

## Choosing targetsv1.14.0 [​](https://moonrepo.dev/docs/guides/ci\#choosing-targets "Direct link to choosing-targets")

By default `moon ci` will run _all_ tasks from _all_ projects that are affected by changed files and
have the [`runInCI`](https://moonrepo.dev/docs/config/project#runinci) task option enabled. This is a great catch-all
solution, but may not vibe with your workflow or requirements.

If you'd prefer more control, you can pass a list of targets to `moon ci`, instead of moon
attempting to detect them. When providing targets, `moon ci` will still only run them if affected by
changed files, but will still filter with the `runInCI` option.

```shell
# Run all builds
$ moon ci :build

# In another job, run tests
$ moon ci :test :lint
```

## Comparing revisions [​](https://moonrepo.dev/docs/guides/ci\#comparing-revisions "Direct link to Comparing revisions")

By default the command will attempt to detect the base and head revisions automatically based on the
current CI provider (powered by the [`ci_env`](https://github.com/milesj/rust-cicd-env) Rust crate).
If nothing was detected, this will fallback to the configured
[`vcs.defaultBranch`](https://moonrepo.dev/docs/config/workspace#defaultbranch) for the base revision, and `HEAD` for the
head revision.

These values can be customized with the `--base` and `--head` command line options, or the
`MOON_BASE` and `MOON_HEAD` environment variables, which takes highest precedence.

```shell
$ moon ci --base <BRANCH> --head <SHA>
# Or
$ MOON_BASE=<BRANCH> MOON_HEAD=<SHA> moon ci
```

## Parallelizing tasks [​](https://moonrepo.dev/docs/guides/ci\#parallelizing-tasks "Direct link to Parallelizing tasks")

If your CI environment supports sharding across multiple jobs, then you can utilize moon's built in
parallelism by passing `--job-total` and `--job` options. The `--job-total` option is an integer of
the total number of jobs available, and `--job` is the current index (0 based) amongst the total.

When these options are passed, moon will only run affected [targets](https://moonrepo.dev/docs/concepts/target) based on
the current job slice.

- GitHub
- Buildkite
- CircleCI
- TravisCI

GitHub Actions do not support native parallelism, but it can be emulated using it's matrix.

.github/workflows/ci.yml

```yaml
# ...
jobs:
  ci:
    # ...
    strategy:
      matrix:
        index: [0, 1]
    steps:
      # ...
      - run: 'moon ci --job ${{ matrix.index }} --job-total 2'
```

- [Documentation](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)

.buildkite/pipeline.yml

```yaml
# ...
steps:
  - label: 'CI'
    parallelism: 10
    commands:
      # ...
      - 'moon ci --job $$BUILDKITE_PARALLEL_JOB --job-total $$BUILDKITE_PARALLEL_JOB_COUNT'
```

- [Documentation](https://buildkite.com/docs/tutorials/parallel-builds#parallel-jobs)

.circleci/config.yml

```yaml
# ...
jobs:
  ci:
    # ...
    parallelism: 10
    steps:
      # ...
      - run: 'moon ci --job $CIRCLE_NODE_INDEX --job-total $CIRCLE_NODE_TOTAL'
```

- [Documentation](https://circleci.com/docs/2.0/parallelism-faster-jobs/)

TravisCI does not support native parallelism, but it can be emulated using it's matrix.

.travis.yml

```yaml
# ...
env:
  global:
    - TRAVIS_JOB_TOTAL=2
  jobs:
    - TRAVIS_JOB_INDEX=0
    - TRAVIS_JOB_INDEX=1
script: 'moon ci --job $TRAVIS_JOB_INDEX --job-total $TRAVIS_JOB_TOTAL'
```

- [Documentation](https://docs.travis-ci.com/user/speeding-up-the-build/)

> Your CI environment may provide environment variables for these 2 values.

## Caching artifacts [​](https://moonrepo.dev/docs/guides/ci\#caching-artifacts "Direct link to Caching artifacts")

When a CI pipeline reaches a certain scale, its run times increase, tasks are unnecessarily ran, and
build artifacts are not shared. To combat this, we support [remote caching](https://moonrepo.dev/docs/guides/remote-cache), a
mechanism where we store build artifacts in the cloud, and sync these artifacts to machines on
demand.

### Manual persistence [​](https://moonrepo.dev/docs/guides/ci\#manual-persistence "Direct link to Manual persistence")

If you'd prefer to _not use_ remote caching at this time, you can cache artifacts yourself, by
persisting the `.moon/cache/{hashes,outputs}` directories. All other files and folders in
`.moon/cache` _should not_ be persisted, as they are not safe/portable across machines.

However, because tasks can generate a different hash each run, you'll need to manually invalidate
your cache. Blindly storing the `hashes` and `outputs` directories without a mechanism to invalidate
will simply not work, as the contents will drastically change between CI runs. This is the primary
reason why the remote caching service exists.

## Reporting run results [​](https://moonrepo.dev/docs/guides/ci\#reporting-run-results "Direct link to Reporting run results")

If you're using GitHub Actions as your CI provider, we suggest using our
[`moonrepo/run-report-action`](https://github.com/marketplace/actions/moon-ci-run-reports). This
action will report the results of a [`moon ci`](https://moonrepo.dev/docs/commands/ci) run to a pull request as a comment
and workflow summary.

.github/workflows/ci.yml

```yaml
# ...
jobs:
  ci:
    name: 'CI'
    runs-on: 'ubuntu-latest'
    steps:
      # ...
      - run: 'moon ci'
      - uses: 'moonrepo/run-report-action@v1'
        if: success() || failure()
        with:
          access-token: ${{ secrets.GITHUB_TOKEN }}
```

The report looks something like the following:

![](https://moonrepo.dev/assets/images/run-report-41cffa17cd530ab8cca5cef47b38dcfd.png)

### Community offerings [​](https://moonrepo.dev/docs/guides/ci\#community-offerings "Direct link to Community offerings")

The following GitHub actions are provided by the community:

- [`appthrust/moon-ci-retrospect`](https://github.com/appthrust/moon-ci-retrospect) \- Displays the
results of a `moon ci` run in a more readable fashion.
- [`kymckay/moon-ci-booster`](https://github.com/kymckay/moon-ci-booster) \- Displays failing
`moon ci` tasks as comments with error logs directly on your pull request.

- [How it works](https://moonrepo.dev/docs/guides/ci#how-it-works)
- [Configuring tasks](https://moonrepo.dev/docs/guides/ci#configuring-tasks)
- [Integrating](https://moonrepo.dev/docs/guides/ci#integrating)
- [Choosing targets](https://moonrepo.dev/docs/guides/ci#choosing-targets)
- [Comparing revisions](https://moonrepo.dev/docs/guides/ci#comparing-revisions)
- [Parallelizing tasks](https://moonrepo.dev/docs/guides/ci#parallelizing-tasks)
- [Caching artifacts](https://moonrepo.dev/docs/guides/ci#caching-artifacts)
  - [Manual persistence](https://moonrepo.dev/docs/guides/ci#manual-persistence)
- [Reporting run results](https://moonrepo.dev/docs/guides/ci#reporting-run-results)
  - [Community offerings](https://moonrepo.dev/docs/guides/ci#community-offerings)