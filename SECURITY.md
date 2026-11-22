# Security policy

This policy covers every repository in [Data Engineering for Multimodal AI](https://github.com/Data-Engineering-for-Multimodal-AI).

## Report a vulnerability

Please report security problems privately, not in a public issue:

1. Open the repository the problem is in.
2. Go to the **Security** tab and click **Report a vulnerability**.
3. Describe what you found, how to reproduce it, and what it affects.

You'll get a reply in that private thread. Fixes are released on the default branch, and the report is published after the fix if that helps other readers.

## What is covered

- The code on each repository's default branch.
- The `first-edition` tag keeps the code as it was when the book was published, so readers can follow the printed pages. It is not patched; use the default branch for anything you run beyond the book.

The playbooks are learning projects that run on your own machine. Before you run something like them for real, read each README's "Before production" checklist: it lists what the code does not do yet, such as authentication.

## Secrets

Never commit API keys or passwords. Every repository blocks pushes that contain known secret formats, and each README says which settings it reads from the environment.
