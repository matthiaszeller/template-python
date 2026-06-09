
echo "Installing pre-commit"
uv run pre-commit install

echo "Updating pre-commit hooks"
uv run pre-commit autoupdate --jobs 4
