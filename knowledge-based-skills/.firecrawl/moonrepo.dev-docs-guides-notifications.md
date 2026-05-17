[Skip to main content](https://moonrepo.dev/docs/guides/notifications#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

v1.38.0

moon is able to send operating system desktop notifications for specific events in the action
pipeline, on behalf of your terminal application. This is useful for continuous feedback loops and
reacting to long-running commands while multi-tasking.

Notifications are opt-in and must be enabled with the
[`notify.terminalNotifications`](https://moonrepo.dev/docs/config/workspace#terminalnotifications) setting.

.moon/workspace.yml

```yaml
notifier:
  terminalNotifications: 'always'
```

## Setup [​](https://moonrepo.dev/docs/guides/notifications\#setup "Direct link to Setup")

Notifications must be enabled at the operating system level.

### Linux [​](https://moonrepo.dev/docs/guides/notifications\#linux "Direct link to Linux")

Linux support is based on the [XDG specification](https://en.wikipedia.org/wiki/XDG) and utilizes
D-BUS APIs, primarily the
[`org.freedesktop.Notifications.Notify`](https://www.galago-project.org/specs/notification/0.9/x408.html#command-notify)
method. Refer to your desktop distribution for more information.

Notifications will be sent using the `moon` application name (the current executable).

### macOS [​](https://moonrepo.dev/docs/guides/notifications\#macos "Direct link to macOS")

- Open "System Settings" or "System Preferences"
- Select "Notifications" in the left sidebar
- Select your terminal application from the list (e.g., "Terminal", "iTerm", etc)
- Ensure "Allow notifications" is enabled
- Customize the other settings as desired

Notifications will be sent from your currently running terminal application, derived from the
`TERM_PROGRAM` environment variable. If we fail to detect the terminal, it will default to "Finder".

### Windows [​](https://moonrepo.dev/docs/guides/notifications\#windows "Direct link to Windows")

Requires Windows 10 or later.

- Open "Settings"
- Go to the "System" panel
- Select "Notifications & Actions" in the left sidebar
- Ensure notifications are enabled

Notifications will be sent from the "Windows Terminal" app if it's currently in use, otherwise from
"Microsoft PowerShell".

- [Setup](https://moonrepo.dev/docs/guides/notifications#setup)
  - [Linux](https://moonrepo.dev/docs/guides/notifications#linux)
  - [macOS](https://moonrepo.dev/docs/guides/notifications#macos)
  - [Windows](https://moonrepo.dev/docs/guides/notifications#windows)