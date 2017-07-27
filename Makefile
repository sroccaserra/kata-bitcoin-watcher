.PHONY: clean lint test_end_to_end test_unit run

PYTEST ?= pytest
FLASK ?= flask
FLAKE8 ?= flake8

clean:<
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

lint:
	@$(FLAKE8) app.py domain infrastructure test

test_end_to_end:
	$(PYTEST) -m end_to_end test

test_unit:
	$(PYTEST) -m 'not end_to_end' test

run:
	FLASK_APP=app.py $(FLASK) run
