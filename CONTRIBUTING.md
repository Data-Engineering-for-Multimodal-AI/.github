# Contributing

Thanks for helping. These playbooks are the companion code for *Data Engineering for Multimodal AI* (O'Reilly, 2026). Readers follow them page by page, so a fix has to keep the book's commands working.

## Ways to help

- **Report a bug.** Open an issue with the "Bug in a playbook" form. Paste the command and the full output.
- **Pick up a good first issue.** Each playbook has a few small tasks labeled [`good first issue`](https://github.com/search?q=org%3AData-Engineering-for-Multimodal-AI+label%3A%22good+first+issue%22+state%3Aopen&type=issues). Comment on one to say you're taking it, so two people don't work on the same thing.
- **Run a playbook on your own data** and tell us what broke or what you had to change.
- **Fix a typo or an unclear step** in a README.

## Set up

Every playbook runs the same way:

```bash
git clone https://github.com/Data-Engineering-for-Multimodal-AI/<playbook>.git
cd <playbook>
make setup     # installs dependencies
make smoke     # the fast tests CI runs
make run       # the full example
```

You need [uv](https://docs.astral.sh/uv/) and Python 3.12 or 3.13. Some playbooks also need Docker; the README says which. Or open the playbook in Codespaces, which has everything installed.

## Make a change

1. Fork the repository and create a branch.
2. Make your change. Keep it small and about one thing.
3. Run `make smoke`. If you changed something `make run` uses, run that too.
4. Open a pull request. The template asks what you changed and how you checked it.

CI runs the smoke tests on Python 3.12 and 3.13 for every pull request.

## Rules that protect the book

The printed book points at these repositories. To keep it accurate:

- **Don't rename or move files, commands or outputs the book shows.** Add new things next to them instead.
- **Keep the sample data in place.** The book's steps read it.
- **The `first-edition` tag never changes.** It holds the code as printed. All changes go to the default branch.
- If the default branch now behaves differently from the book, say so in the README. Most READMEs have a "Differences from the printed book" section for this.

## Data and secrets

- Don't commit datasets you don't have the right to share. Each playbook lists its data and licenses in `DATA_SOURCES.md`.
- Don't commit API keys or passwords. Pushes that contain known secret formats are blocked.
- Report security problems privately. See [SECURITY.md](SECURITY.md).

## Code of conduct

Everyone taking part follows the [code of conduct](CODE_OF_CONDUCT.md).
