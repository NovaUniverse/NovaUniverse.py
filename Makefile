build-clean-docs:
	cd docs && make.bat clean && make.bat html

build-docs:
	cd docs && make.bat html

test:
	ruff .
	cd tests && pytest -v

test-v:
	cd tests && pytest -vv

build:
	python -m build