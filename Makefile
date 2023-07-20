.PHONY: install format

install:
	pip install -e .[dev]
	pre-commit autoupdate
	pre-commit install

format:
	pycln .
	black .
	isort .