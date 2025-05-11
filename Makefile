VENV_NAME := .inephany-env

venv:
	python3.12 -m venv ${VENV_NAME} && \
	. ${VENV_NAME}/bin/activate && \
	python -m pip install --upgrade pip setuptools wheel build

.PHONY: install-auxiliary
install-auxiliary:
	@if [ -f auxiliary_requirements.txt ]; then \
		echo "Installing auxiliary requirements..."; \
		python -m pip install -r auxiliary_requirements.txt; \
	fi

.PHONY: install
install:
	. ${VENV_NAME}/bin/activate && \
	python -m pip install -e .

.PHONY: run
run:
	PYTHONPATH=src ${VENV_NAME}/bin/uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload