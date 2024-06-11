PYTHON=./.venv/bin/python

PHONY = help run

help:
	@echo "---------------HELP-----------------"
	@echo "Iniciar o servidor -> make run"
	@echo "------------------------------------"

run:
	python -m uvicorn adapters.web.server:app --host 0.0.0.0 --port 8000 --reload