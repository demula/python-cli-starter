init:
	pip3 install -r requirements.txt

test:
	nose2 -c unittest.cfg

test_coverage:
	nose2 -c unittest.cfg --with-coverage

install:
	pip3 install --editable .

check:
	pylint app

generate_docs:
	$(MAKE) -C docs html

update_requirements:
	pip freeze > requirements.txt

dist:
	python setup.py sdist bdist_wheel

.PHONY: init test