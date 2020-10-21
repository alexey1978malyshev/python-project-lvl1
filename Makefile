install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
	
.PHONY: instsall brain-games build package-install

