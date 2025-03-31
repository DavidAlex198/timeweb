setup:
	python3 -m venv env
	env/bin/pip install -r requirements.txt
	echo Installed Dependencies

clean:
	rm -r env
	rm -r __pycache__

test: test_app.py
	env/bin/python -m pytest

run: app.py
	flask  run --host 10.92.21.104 --port 8008
