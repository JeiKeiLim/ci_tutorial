format:
	black .
	isort .

test:
	black . --check
	isort . --check-only
	env PYTHONPATH=. pytest --pylint --flake8 --mypy --ignore tests
	env PYTHONPATH=. pytest tests --cov=src --cov-report term-missing --cov-report html

dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

