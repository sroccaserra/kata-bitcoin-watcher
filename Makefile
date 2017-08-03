.PHONY: clean lint test_all test_unit run

PYTEST ?= pytest
FLASK ?= flask
FLAKE8 ?= flake8

clean:
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

lint:
	@$(FLAKE8) app.py domaine infrastructure test

test_all:
	@$(PYTEST) test

test_unit:
	@$(PYTEST) -m 'not end_to_end' test

run:
	@FLASK_APP=infrastructure/application/app.py $(FLASK) run
