# template-python

[Copier](https://copier.readthedocs.io/) template for Python projects, built on `uv`.

## What you get

- `src/` layout with `uv_build`, pydantic-settings configuration (`settings.py`), logging setup (`log.py`)
  and a minimal `__main__.py` wiring them together
- Ruff (lint, import sorting, format), `ty` type checking, pytest with coverage
- pre-commit (hygiene hooks, ruff, `uv-lock`, gitleaks, `ty`)
- GitHub Actions CI (lint plus a Python 3.13 / 3.14 test matrix) and Dependabot for `uv` and Actions
- `Makefile`, `.editorconfig`, `.env.example`, `CLAUDE.md`

## Create a project

```bash
uvx copier copy --trust gh:matthiaszeller/template-python my-project
```

`--trust` is required because the template runs post-generation tasks (`git init`, `uv sync`,
`pre-commit install`, `pre-commit autoupdate`; see `copier.yml`).

## Update an existing project

```bash
uvx copier update --trust
```

Copier uses the latest git tag of the template, so **tag a release** (`git tag v0.1.0`) after changing it.

## Working on the template

The repo root is only the template's own scaffolding; everything that gets generated lives in `template/`.
Files ending in `.jinja` are rendered, all others are copied as is. The CI workflow generates a project and runs
its checks (`.github/workflows/test-template.yml`).

To try it locally:

```bash
uvx copier copy --trust --vcs-ref=HEAD "$PWD" /tmp/demo
```
