build-docs:
	cd docs && make.bat html

test:
	cd tests
	pytest