update-deps:
	pip install --upgrade pip-tools pip setuptools
	pip-compile --upgrade --build-isolation --generate-hashes --output-file requirements.txt requirements.in

init:
	pip install --editable .
	pip install --upgrade -r requirements.in
	rm -rf .tox

update: update-deps init

.PHONY: update-deps init update
