install:
	poetry install

build:
	poetry build

pack-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: install build pack-install
