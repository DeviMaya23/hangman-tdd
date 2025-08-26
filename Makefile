lint: 
	@for py in *.py; do \
	 echo "flake8 $$py"; \
	 flake8 $$py; \
	 echo "pylint $$py"; \
	 pylint $$py; \
	 done