lint:
	PYTHONPATH=src flake8 src tests main.py
	PYTHONPATH=src pylint src tests main.py
unit-test:
	cd tests/unit && pytest
integration-test:
	cd tests/integration && pytest
test-coverage:
	pytest --cov=src
run:
	PYTHONPATH=src python main.py