---
id: convention-math
title: Math
type: convention
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# Math

KaTeX-compatible LaTeX is the standard. GitHub renders since 2022; Obsidian, Quartz, MkDocs Material, mdBook (via `mdbook-katex`), Docusaurus, and Pandoc all support it with default or one-line config.

## Inline

Wrap in single dollar signs:

```markdown
The throughput is bounded by $\lambda = \min(\lambda_{\text{producer}}, \lambda_{\text{consumer}})$.
```

## Block

Wrap in double dollar signs on their own lines:

```markdown
$$
p_{99} \;=\; F^{-1}(0.99)
$$
```

## What to use math for

Research that touches latency, throughput, concurrency limits, sampling, probability, complexity bounds — write the expression rather than the prose. The expression is denser, less ambiguous, and survives translation between renderers.

## What not to use math for

Pseudocode. Use a fenced code block. Math notation for control flow is harder to read than the equivalent code.
