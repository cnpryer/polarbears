PYTHON_VERSION=python3.10

clean:
	@rm -rf .venv

venv:
	@$(PYTHON_VERSION) -m venv .venv
	@.venv/bin/pip install -U pip
	@poetry config virtualenvs.path .venv
	@poetry install

test:
	poetry run pytest

fmt:
	.venv/bin/black polarsbear tests
	.venv/bin/isort polarsbear tests

lint:
	.venv/bin/flake8 polarsbear tests