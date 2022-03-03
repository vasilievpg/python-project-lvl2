install:
	poetry install

gendiff:
	poetry run gendiff

gendiff_files_json:
	poetry run gendiff ./tests/fixtures/file1.json ./tests/fixtures/file2.json

gendiff_files_yaml:
	poetry run gendiff ./tests/fixtures/file1.yaml ./tests/fixtures/file2.yml

build: check
	poetry build

lint:
	poetry run flake8 gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-uninstall:
	python3 -m pip uninstall dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall --no-warn-script-location

test:
	poetry run pytest -svv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build