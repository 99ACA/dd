# Makefile macros (or variables) are defined a little bit differently than traditional bash,
# keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.

############# Macros ########################
VENV_NAME = .venv
VENV_ACTIVATE= . ./$(VENV_NAME)/bin/activate
PIP_CMD ?= pip3
PYTHON ?= python3
############# Macros ########################
SHELL := bash
PYTHONVERSION = $(${SHELL} python -V |  grep ^Python | sed 's/^.* //g')

.DEFAULT_GOAL = help

help:
	@echo "---------------Help---------------"
	@echo "make [test-bdd | test-unit | test-all]"
	@echo "make run"
	@echo "make setup-venv - install the venv and the requirments"
	@echo "make docker-build"
	@echo "----------------------------------"


.SILENT:
.ONESHELL:
setup-venv:  # Setup virtualenv & install
	(test -e  $(VENV_NAME) || ${PYTHON} -m venv ./.venv) && \
	$(VENV_ACTIVATE) && \
	pip3 install --upgrade pip && \
	make install


.ONESHELL:
install:
	$(VENV_ACTIVATE) || echo "No VENV"  && \
	pip3 install -r requirements.txt


# Run the service
run-puller:
	$(VENV_ACTIVATE) || echo "No VENV"  && \
	cd src && \
	${PYTHON} -m puller


# Docker build
docker-build:
	docker build -t boilerplate:latest .