install:
	poetry install

build:
	poetry build

pack-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

.PHONY: install build pack-install publish gendiff lint test
