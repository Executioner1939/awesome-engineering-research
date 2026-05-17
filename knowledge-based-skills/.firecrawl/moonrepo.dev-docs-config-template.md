[Skip to main content](https://moonrepo.dev/docs/config/template#__docusaurus_skipToContent_fallback)

info

Documentation is currently for [moon v2](https://moonrepo.dev/blog/moon-v2.0) and latest proto. Documentation for moon v1 has been frozen and can be [found here](https://moonrepo.github.io/website-v1/).

On this page

The `template.*` file configures metadata and variables for a template,
[used by the generator](https://moonrepo.dev/docs/guides/codegen), and must exist at the root of a named template folder.

## `id`v1.23.0 [​](https://moonrepo.dev/docs/config/template\#id "Direct link to id")

Overrides the name (identifier) of the template, instead of inferring the name from the template
folder. Be aware that template names must be unique across the workspace, and across all template
locations that have been configured in [`generator.templates`](https://moonrepo.dev/docs/config/workspace#templates).

template.yml

```yaml
id: 'npm-package'
```

## `title`Required [​](https://moonrepo.dev/docs/config/template\#title "Direct link to title")

A human readable title that will be displayed during the [`moon generate`](https://moonrepo.dev/docs/commands/generate)
process.

template.yml

```yaml
title: 'npm package'
```

## `description`Required [​](https://moonrepo.dev/docs/config/template\#description "Direct link to description")

A description of why the template exists, what its purpose is, and any other relevant information.

template.yml

```yaml
description: |
  Scaffolds the initial structure for an npm package,
  including source and test folders, a package.json, and more.
```

## `destination`v1.19.0 [​](https://moonrepo.dev/docs/config/template\#destination "Direct link to destination")

An optional file path in which this template should be generated into. This provides a mechanism for
standardizing a destination location, and avoids having to manually pass a destination to
[`moon generate`](https://moonrepo.dev/docs/commands/generate).

If the destination is prefixed with `/`, it will be relative from the workspace root, otherwise it
is relative from the current working directory.

template.yml

```yaml
destination: 'packages/[name]'
```

> This setting supports [template variables](https://moonrepo.dev/docs/config/template#variables) through `[varName]` syntax. Learn more in
> the [code generation documentation](https://moonrepo.dev/docs/guides/codegen#interpolation).

## `extends`v1.19.0 [​](https://moonrepo.dev/docs/config/template\#extends "Direct link to extends")

One or many other templates that this template should extend. Will deeply inherit all template files
and variables.

template.yml

```yaml
extends: ['base', 'configs']
```

## `variables` [​](https://moonrepo.dev/docs/config/template\#variables "Direct link to variables")

A mapping of variables that will be interpolated into all template files and file system paths when
[rendering with Tera](https://tera.netlify.app/docs/#variables). The map key is the variable name
(in camelCase or snake\_case), while the value is a configuration object, as described with the
settings below.

template.yml

```yaml
variables:
  name:
    type: 'string'
    default: ''
    required: true
    prompt: 'Package name?'
```

### `type`Required [​](https://moonrepo.dev/docs/config/template\#type "Direct link to type")

The type of value for the variable. Accepts `array`, `boolean`, `string`, `object`, `number`, or
`enum`. Floats _are not supported_, use strings instead.

For arrays and objects, the value of each member must be a JSON compatible type.

### `internal`v1.23.0 [​](https://moonrepo.dev/docs/config/template\#internal "Direct link to internal")

Marks a variable as internal only, which avoids the variable value being overwritten by command line
arguments.

### `order`v1.23.0 [​](https://moonrepo.dev/docs/config/template\#order "Direct link to order")

The order in which the variable will be prompted to the user. By default, variables are prompted in
the order they are defined in the `template.*` file.

### Primitives & collections [​](https://moonrepo.dev/docs/config/template\#primitives--collections "Direct link to Primitives & collections")

Your basic primitives: boolean, numbers, strings, and collections: arrays, objects.

- array
- boolean
- number
- object
- string

template.yml

```yaml
variables:
  type:
    type: 'array'
    prompt: 'Type?'
    default: ['app', 'lib']
```

template.yml

```yaml
variables:
  private:
    type: 'boolean'
    prompt: 'Private?'
    default: false
```

template.yml

```yaml
variables:
  age:
    type: 'number'
    prompt: 'Age?'
    default: 0
    required: true
```

template.yml

```yaml
variables:
  metadata:
    type: 'object'
    prompt: 'Metadata?'
    default:
      type: 'lib'
      dev: true
```

template.yml

```yaml
variables:
  name:
    type: 'string'
    prompt: 'Name?'
    required: true
```

### `default`Required [​](https://moonrepo.dev/docs/config/template\#default "Direct link to default")

The default value of the variable. When `--defaults` is passed to
[`moon generate`](https://moonrepo.dev/docs/commands/generate) or [`prompt`](https://moonrepo.dev/docs/config/template#prompt) is not defined, the default value
will be used, otherwise the user will be prompted to enter a custom value.

### `prompt` [​](https://moonrepo.dev/docs/config/template\#prompt "Direct link to prompt")

When defined, will prompt the user with a message in the terminal to input a custom value, otherwise
[`default`](https://moonrepo.dev/docs/config/template#default) will be used.

For arrays and objects, a valid JSON string must be provided as the value.

### `required` [​](https://moonrepo.dev/docs/config/template\#required "Direct link to required")

Marks the variable as required during _prompting only_. For arrays, strings, and objects, will error
for empty values (`''`). For numbers, will error for zero's (`0`).

### Enums [​](https://moonrepo.dev/docs/config/template\#enums "Direct link to Enums")

An enum is an explicit list of string values that a user can choose from.

template.yml

```yaml
variables:
  color:
    type: 'enum'
    values: ['red', 'green', 'blue', 'purple']
    default: 'purple'
    prompt: 'Favorite color?'
```

### `default` [​](https://moonrepo.dev/docs/config/template\#default-1 "Direct link to default-1")

The default value of the variable. When `--defaults` is passed to
[`moon generate`](https://moonrepo.dev/docs/commands/generate) or [`prompt`](https://moonrepo.dev/docs/config/template#prompt) is not defined, the default value
will be used, otherwise the user will be prompted to enter a custom value.

For enums, the default value can be a string when [`multiple`](https://moonrepo.dev/docs/config/template#multiple) is false, or a string or
an array of strings when `multiple` is true. Furthermore, each default value must exist in the
[`values`](https://moonrepo.dev/docs/config/template#values) list.

template.yml

```yaml
# Single
variables:
  color:
    type: 'enum'
    values: ['red', 'green', 'blue', 'purple']
    default: 'purple'
    prompt: 'Favorite color?'

# Multiple
variables:
  color:
    type: 'enum'
    values: ['red', 'green', 'blue', 'purple']
    default: ['red', 'purple']
    multiple: true
    prompt: 'Favorite color?'
```

### `prompt` [​](https://moonrepo.dev/docs/config/template\#prompt-1 "Direct link to prompt-1")

When defined, will prompt the user with a message in the terminal to input a custom value, otherwise
[`default`](https://moonrepo.dev/docs/config/template#default) will be used.

### `multiple` [​](https://moonrepo.dev/docs/config/template\#multiple "Direct link to multiple")

Allows multiple values to be chosen during prompting. In the template, an array or strings will be
rendered, otherwise when not-multiple, a single string will be.

### `values`Required [​](https://moonrepo.dev/docs/config/template\#values "Direct link to values")

List of explicit values to choose from. Can either be defined with a string, which acts as a value
and label, or as an object, which defines an explicit value and label.

template.yml

```yaml
variables:
  color:
    type: 'enum'
    values:
      - 'red'
      # OR
      - value: 'red'
        label: 'Red 🔴'
    # ...
```

## Frontmatter [​](https://moonrepo.dev/docs/config/template\#frontmatter "Direct link to Frontmatter")

The following settings _are not_ available in `template.*`, but can be defined as frontmatter at the
top of a template file. View the [code generation guide](https://moonrepo.dev/docs/guides/codegen#frontmatter) for more
information.

### `force` [​](https://moonrepo.dev/docs/config/template\#force "Direct link to force")

When enabled, will always overwrite a file of the same name at the destination path, and will bypass
any prompting in the terminal.

```twig
---
force: true
---

Some template content!
```

### `to` [​](https://moonrepo.dev/docs/config/template\#to "Direct link to to")

Defines a custom file path, relative from the destination root, in which to create the file. This
will override the file path within the template folder, and allow for conditional rendering and
engine filters to be used.

```twig
{% set component_name = name | pascal_case %}

---
to: components/{{ component_name }}.tsx
---

export function {{ component_name }}() {
  return <div />;
}
```

### `skip` [​](https://moonrepo.dev/docs/config/template\#skip "Direct link to skip")

When enabled, the template file will be skipped while writing to the destination path. This setting
can be used to conditionally render a file.

```twig
---
skip: {{ name == "someCondition" }}
---

Some template content!
```

- [`id`](https://moonrepo.dev/docs/config/template#id)
- [`title`](https://moonrepo.dev/docs/config/template#title)
- [`description`](https://moonrepo.dev/docs/config/template#description)
- [`destination`](https://moonrepo.dev/docs/config/template#destination)
- [`extends`](https://moonrepo.dev/docs/config/template#extends)
- [`variables`](https://moonrepo.dev/docs/config/template#variables)
  - [`type`](https://moonrepo.dev/docs/config/template#type)
  - [`internal`](https://moonrepo.dev/docs/config/template#internal)
  - [`order`](https://moonrepo.dev/docs/config/template#order)
  - [Primitives & collections](https://moonrepo.dev/docs/config/template#primitives--collections)
  - [`default`](https://moonrepo.dev/docs/config/template#default)
  - [`prompt`](https://moonrepo.dev/docs/config/template#prompt)
  - [`required`](https://moonrepo.dev/docs/config/template#required)
  - [Enums](https://moonrepo.dev/docs/config/template#enums)
  - [`default`](https://moonrepo.dev/docs/config/template#default-1)
  - [`prompt`](https://moonrepo.dev/docs/config/template#prompt-1)
  - [`multiple`](https://moonrepo.dev/docs/config/template#multiple)
  - [`values`](https://moonrepo.dev/docs/config/template#values)
- [Frontmatter](https://moonrepo.dev/docs/config/template#frontmatter)
  - [`force`](https://moonrepo.dev/docs/config/template#force)
  - [`to`](https://moonrepo.dev/docs/config/template#to)
  - [`skip`](https://moonrepo.dev/docs/config/template#skip)