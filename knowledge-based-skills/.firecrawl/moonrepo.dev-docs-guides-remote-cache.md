[Skip to main content](https://moonrepo.dev/docs/guides/remote-cache#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Is your CI pipeline running slower than usual? Are you tired of running the same build over and over
although nothing has changed? Do you wish to reuse the same local cache across other machines and
environments? These are just a few scenarios that remote caching aims to solve.

Remote caching is a system that shares artifacts to improve performance, reduce unnecessary
computation time, and alleviate resources. It achieves this by uploading hashed artifacts to a cloud
storage provider, like AWS S3 or Google Cloud, and downloading them on demand when a build matches a
derived hash.

To make use of remote caching, we provide 2 solutions.

## Self-hosted v1.30.0 [​](https://moonrepo.dev/docs/guides/remote-cache\#self-hosted- "Direct link to self-hosted-")

This solution allows you to host any remote caching service that is compatible with the
[Bazel Remote Execution v2 API](https://github.com/bazelbuild/remote-apis/tree/main/build/bazel/remote/execution/v2),
such as [`bazel-remote`](https://github.com/buchgr/bazel-remote). When using this solution, the
following RE API features must be enabled:

- Action result caching
- Content addressable storage caching
- SHA256 digest hashing
- gRPC requests

### Host your service [​](https://moonrepo.dev/docs/guides/remote-cache\#host-your-service "Direct link to Host your service")

When you have chosen (or built) a compatible service, host it and make it available through gRPC or
HTTPS. For example, if you plan to use `bazel-remote`, you can do something like the following:

```bash
bazel-remote --dir /path/to/moon-cache --max_size 10 --storage_mode uncompressed --grpc_address 0.0.0.0:9092
```

If you've configured the [`remote.cache.compression`](https://moonrepo.dev/docs/config/workspace#compression) setting to
"zstd", you'll need to run the binary with that storage mode as well.

```bash
bazel-remote --dir /path/to/moon-cache --max_size 10 --storage_mode zstd --grpc_address 0.0.0.0:9092
```

info

View the official [`bazel-remote`](https://github.com/buchgr/bazel-remote#usage) documentation for
all the available options, like storing artifacts in S3, configuring authentication (TLS/mTLS),
proxies, and more.

### Configure remote caching [​](https://moonrepo.dev/docs/guides/remote-cache\#configure-remote-caching "Direct link to Configure remote caching")

Once your service is running, you can enable remote caching by configuring the
[`remote`](https://moonrepo.dev/docs/config/workspace#remote) settings in [`.moon/workspace.*`](https://moonrepo.dev/docs/config/workspace). At
minimum, the only setting that is required is `host`.

.moon/workspace.yml

```yaml
# gRPC
remote:
  host: 'grpc://your-host.com:9092'

# HTTPS
remote:
  api: 'http'
  host: 'https://your-host.com:8080'
```

info

Remote caching can be conditionally enabled by setting the `MOON_REMOTE_HOST` environment variable.

#### TLS and mTLS [​](https://moonrepo.dev/docs/guides/remote-cache\#tls-and-mtls "Direct link to TLS and mTLS")

We have rudimentary support for TLS and mTLS, but it's very unstable, and has not been thoroughly
tested. There's also [many](https://github.com/hyperium/tonic/issues/1652) [many](https://github.com/hyperium/tonic/issues/1989) [issues](https://github.com/hyperium/tonic/issues/1033) around authentication in Tonic.

.moon/workspace.yml

```yaml
# TLS
remote:
  host: 'grpcs://your-host.com:9092'
  tls:
    cert: 'certs/ca.pem'
    domain: 'your-host.com'

# mTLS
remote:
  host: 'grpcs://your-host.com:9092'
  mtls:
    caCert: 'certs/ca.pem'
    clientCert: 'certs/client.pem'
    clientKey: 'certs/client.key'
    domain: 'your-host.com'
```

## Cloud-hosted [​](https://moonrepo.dev/docs/guides/remote-cache\#cloud-hosted "Direct link to Cloud-hosted")

### Depotv1.32.0 [​](https://moonrepo.dev/docs/guides/remote-cache\#depot "Direct link to depot")

If you'd prefer not to host your own solution, you could use
[Depot Cache](https://depot.dev/products/cache), a cloud-based caching solution. To make use of
Depot, follow these steps:

- Create an account on [depot.dev](https://depot.dev/)
- Create an organization
- Go to organization settings -> API tokens
- Create a new API token
- Add the token as a `DEPOT_TOKEN` environment variable to your moon pipelines

Once these steps have been completed, you can enable remote caching in moon with the following
configuration. If your Depot account has more than 1 organization, you'll need to set the
`X-Depot-Org` header.

.moon/workspace.yml

```yaml
remote:
  host: 'grpcs://cache.depot.dev'
  auth:
    token: 'DEPOT_TOKEN'
    headers:
      'X-Depot-Org': '<your-org-id>'
```

## FAQ [​](https://moonrepo.dev/docs/guides/remote-cache\#faq "Direct link to FAQ")

#### What is an artifact? [​](https://moonrepo.dev/docs/guides/remote-cache\#what-is-an-artifact "Direct link to What is an artifact?")

In the context of moon and remote caching, an artifact is the
[outputs of a task](https://moonrepo.dev/docs/config/project#outputs), as well as the stdout and stderr of the task that
generated the outputs. Artifacts are uniquely identified by the
[moon generated hash](https://moonrepo.dev/docs/concepts/cache#hashing).

#### Do I have to use remote caching? [​](https://moonrepo.dev/docs/guides/remote-cache\#do-i-have-to-use-remote-caching "Direct link to Do I have to use remote caching?")

No, remote caching is _optional_. It's intended purpose is to store long lived build artifacts to
speed up CI pipelines, and optionally local development. For the most part,
[`moon ci`](https://moonrepo.dev/docs/commands/ci) does a great job of only running what's affected in pull requests, and
is a great starting point.

#### Does remote caching store source code? [​](https://moonrepo.dev/docs/guides/remote-cache\#does-remote-caching-store-source-code "Direct link to Does remote caching store source code?")

No, remote caching _does not_ store source code. It stores the
[outputs of a task](https://moonrepo.dev/docs/config/project#outputs), which is typically built and compiled code. To
verify this, you can inspect the tar archives in `.moon/cache/outputs`.

#### Does moon collect any personally identifiable information? [​](https://moonrepo.dev/docs/guides/remote-cache\#does-moon-collect-any-personally-identifiable-information "Direct link to Does moon collect any personally identifiable information?")

No, moon does not collect any PII as part of the remote caching process.

#### Are artifacts encrypted? [​](https://moonrepo.dev/docs/guides/remote-cache\#are-artifacts-encrypted "Direct link to Are artifacts encrypted?")

We do not encrypt on moon's side, as encryption is provided by your cloud storage provider.

- [Self-hosted](https://moonrepo.dev/docs/guides/remote-cache#self-hosted-)
  - [Host your service](https://moonrepo.dev/docs/guides/remote-cache#host-your-service)
  - [Configure remote caching](https://moonrepo.dev/docs/guides/remote-cache#configure-remote-caching)
    - [TLS and mTLS](https://moonrepo.dev/docs/guides/remote-cache#tls-and-mtls)
- [Cloud-hosted](https://moonrepo.dev/docs/guides/remote-cache#cloud-hosted)
  - [Depot](https://moonrepo.dev/docs/guides/remote-cache#depot)
- [FAQ](https://moonrepo.dev/docs/guides/remote-cache#faq)
  - [What is an artifact?](https://moonrepo.dev/docs/guides/remote-cache#what-is-an-artifact)
  - [Do I have to use remote caching?](https://moonrepo.dev/docs/guides/remote-cache#do-i-have-to-use-remote-caching)
  - [Does remote caching store source code?](https://moonrepo.dev/docs/guides/remote-cache#does-remote-caching-store-source-code)
  - [Does moon collect any personally identifiable information?](https://moonrepo.dev/docs/guides/remote-cache#does-moon-collect-any-personally-identifiable-information)
  - [Are artifacts encrypted?](https://moonrepo.dev/docs/guides/remote-cache#are-artifacts-encrypted)