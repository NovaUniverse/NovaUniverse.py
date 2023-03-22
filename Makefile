build-clean-docs:
	cd docs && make.bat clean && make.bat html

build-docs:
	cd docs && make.bat html

test:
	cd tests
	pytest