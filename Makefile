format:
	black .
	isort .

test:
	black . --check
	isort . --check-only
	env PYTHONPATH=. pytest --pylint --flake8 --mypy

dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

