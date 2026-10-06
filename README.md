# plinth-reach

> One line saying what this is.

## Getting started

```bash
git clone <this repository>
cd plinth-reach
uv sync --locked   # 1. dependencies, the same command CI runs; the lockfile is used as is
uv run pytest      # 2. tests
```

## Developing

```bash
uv run ruff check . && uv run ruff format .   # lint and format
uv run mypy .                                  # types
uv run pytest                                  # tests
uv build                                       # build
```

CI runs each of these as a separate check, plus a secret scan and CodeQL.
Pass them locally first. The list of required checks is the repository's
ruleset, so it is not repeated here.

## Contributing

[`CONTRIBUTING.md`](CONTRIBUTING.md), in particular the test policy. `main` is
protected; a change lands as a pull request with green checks.

## About this repository

Created from [`coolbress/plinth-template`](https://github.com/coolbress/plinth-template).
The CI checks come from [`coolbress/plinth`](https://github.com/coolbress/plinth).

## First day

- If the merge stays blocked on CodeQL, push once more: `git commit --allow-empty -m 'ci: trigger code scanning' && git push`.
- If your everyday gh token is fine-grained with selected repositories, add `plinth-reach` to it: https://github.com/settings/personal-access-tokens
- Dependabot opens pull requests from the first minute: merge one when every required check is green, or close it. CodeQL does not analyse a head Dependabot pushed; `ci / deps` and the tests run on it, and `main` is analysed after the merge. Its first one usually lands while the door waits for CodeQL, so the door's own pull request is #2. After "Update branch" the merge stays blocked for a minute or two while the required checks and CodeQL run on the new head, and a merge tried then is refused with "the base branch policy prohibits the merge": wait for the state to read clean rather than adding an approval, which a person's own branch update did not need.

Made with [plinth](https://github.com/coolbress/plinth).
