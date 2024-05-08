install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install build package-install
