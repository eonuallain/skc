.ONESHELL:

.DEFAULT_GOAL := run

PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip

venv/bin/activate : requirements.txt
	${PYTHON} -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	${PIP} install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate
run: venv 
	${PYTHON} src/main.py

clean:
	rm -rf __pycache__
	rm -rf venv

