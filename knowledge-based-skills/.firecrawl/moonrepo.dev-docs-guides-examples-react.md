[Skip to main content](https://moonrepo.dev/docs/guides/examples/react#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

React is an application or library concern, and not a build system one, since the bundling of React
is abstracted away through another tool like webpack. Because of this, moon has no guidelines around
utilizing React directly. You can use React however you wish!

However, with that being said, we do suggest the following:

- Add `react` and related dependencies to each project, not the root. This includes `@types/react`
as well. This will ensure accurate [hashing](https://moonrepo.dev/docs/concepts/cache#hashing).

- Yarn
- Yarn (classic)
- npm
- pnpm
- Bun

```shell
yarn workspace <project> add react
```

```shell
yarn workspace <project> add react
```

```shell
npm install --workspace <project> react
```

```shell
pnpm add --filter <project> react
```

```shell
bun install react
```

- Configure Babel with the `@babel/preset-react` preset.
- Configure [TypeScript](https://moonrepo.dev/docs/guides/examples/typescript) compiler options with `"jsx": "react-jsx"`.