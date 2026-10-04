.PHONY: help sync fmt lint typecheck test check upgrade
.DEFAULT_GOAL := help

help: ## Show this help
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-10s %s\n", $$1, $$2}'

sync: ## Install dependencies from uv.lock
	uv sync --locked

fmt: ## Auto-fix lint issues and format code
	uv run ruff check --fix .
	uv run ruff format .

lint: ## Check lint and formatting
	uv run ruff check .
	uv run ruff format --check .

typecheck: ## Run the type checker
	uv run ty check

test: ## Run tests with coverage
	uv run pytest --cov

check: lint typecheck test ## Lint, type check and test

upgrade: ## Upgrade all dependencies and pre-commit hooks
	uv lock --upgrade
	uv sync
	uv run pre-commit autoupdate --jobs 4
