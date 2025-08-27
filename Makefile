lint: 
	@for py in *.py; do \
	 echo "flake8 $$py"; \
	 flake8 $$py; \
	 echo "pylint $$py"; \
	 pylint $$py; \
	 done
unit-test:
	cd tests/unit && pytest
integration-test:
	cd tests/integration && pytest
run:
	PYTHONPATH=src python main.py