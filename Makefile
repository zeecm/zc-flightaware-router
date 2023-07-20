.PHONY: install format check test

PACKAGE = "zc_flightaware_router"

install:
	pip install -e .[dev]
	pre-commit autoupdate
	pre-commit install

check:
	-pylint $(PACKAGE)
	pyright $(PACKAGE)

test:
	pytest --cov=$(PACKAGE) tests/

format:
	pycln .
	black .
	isort .