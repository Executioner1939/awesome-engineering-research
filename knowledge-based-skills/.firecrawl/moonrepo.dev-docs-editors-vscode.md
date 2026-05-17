[Skip to main content](https://moonrepo.dev/docs/editors/vscode#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

Enhance your VS Code experience with our integrated moon console! Whether you're a fan of the
command line, or prefer interactive interfaces, our console will be a welcome experience.

> This extension is in its early stages. Expect more advanced features in the future, like
> autocompletion, config validation, and more!

## Views [​](https://moonrepo.dev/docs/editors/vscode\#views "Direct link to Views")

![VS Code - Sidebar icon](<Base64-Image-Removed>)

All views are available within the moon sidebar. Simply click the moon icon in the left activity
bar!

### Projects [​](https://moonrepo.dev/docs/editors/vscode\#projects "Direct link to Projects")

The backbone of moon is the projects view. In this view, all moon configured projects will be
listed, categorized by their [`layer`](https://moonrepo.dev/docs/config/project#layer), [`stack`](https://moonrepo.dev/docs/config/project#stack),
and designated with their [`language`](https://moonrepo.dev/docs/config/project#language).

Each project can then be expanded to view all available tasks. Tasks can be ran by clicking the `▶`
icon, or using the command palette.

> This view is available in both the "Explorer" and "moon" sidebars.

### Tags [​](https://moonrepo.dev/docs/editors/vscode\#tags "Direct link to Tags")

Similar to the projects view, the tags view displays projects grouped by their
[`tags`](https://moonrepo.dev/docs/config/project#tags).

> This view is only available in the "moon" sidebar.

### Last run [​](https://moonrepo.dev/docs/editors/vscode\#last-run "Direct link to Last run")

Information about the last ran task will be displayed in a beautiful table with detailed stats.

This table displays all actions that were ran alongside the primary target(s). They are ordered
topologically via the action graph.

## Features [​](https://moonrepo.dev/docs/editors/vscode\#features "Direct link to Features")

### YAML validation [​](https://moonrepo.dev/docs/editors/vscode\#yaml-validation "Direct link to YAML validation")

To enable accurate validation of our YAML configuration files, you'll need to update the
`yaml.schemas` setting in `.vscode/settings.json` to point to the local schemas at
`.moon/cache/schemas`.

This can be automated by running the "moon: Append YAML schemas configuration to settings" in the
command palette, after the extension has been installed.

## Troubleshooting [​](https://moonrepo.dev/docs/editors/vscode\#troubleshooting "Direct link to Troubleshooting")

View the
[official VS Code marketplace](https://marketplace.visualstudio.com/items?itemName=moonrepo.moon-console)
for more information on the extension, its commands, available settings, and more!

If you encounter a bug, or have a feature request, please submit them to the
[moonrepo/dev](https://github.com/moonrepo/dev/tree/master/packages/vscode-extension) repository!

- [Views](https://moonrepo.dev/docs/editors/vscode#views)
  - [Projects](https://moonrepo.dev/docs/editors/vscode#projects)
  - [Tags](https://moonrepo.dev/docs/editors/vscode#tags)
  - [Last run](https://moonrepo.dev/docs/editors/vscode#last-run)
- [Features](https://moonrepo.dev/docs/editors/vscode#features)
  - [YAML validation](https://moonrepo.dev/docs/editors/vscode#yaml-validation)
- [Troubleshooting](https://moonrepo.dev/docs/editors/vscode#troubleshooting)