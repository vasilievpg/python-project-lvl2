install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

lint:
	poetry run flake8 scripts

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-uninstall:
	python3 -m pip uninstall dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall --no-warn-script-location