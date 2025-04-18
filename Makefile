FLASKIP = --host 0.0.0.0
FLASKPORT = --port 5000
TESTAPP = _app
VENVNAME = env
APPNAME = app
setup:
	python3 -m venv ${VENVNAME}
	${VENVNAME}/bin/pip install -r requirements.txt
	${VENVNAME}/bin/pip install setuptools
clean:
	rm -r ${VENVNAME}
	rm -r __pycache__

test: test${TESTAPP}.py
	pytest

run: ${APPNAME}.py
	flask run ${FLASKIP} ${FLASKPORT}
