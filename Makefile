FLASKIP = --host 10.92.21.104
FLASKPORT = --port 8008
TESTAPP = _app
VENVNAME = env
APPNAME = app
setup:
	python3 -m venv ${VENVNAME}
	${VENVNAME}/bin/pip install -r requirements.txt

clean:
	rm -r ${VENVNAME}
	rm -r __pycache__

test: test${TESTAPP}.py
	pytest

run: ${APPNAME}.py
	flask run ${FLASKIP} ${FLASKPORT}
