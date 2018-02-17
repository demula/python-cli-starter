init:
	pip3 install -r requirements.txt

test:
	nose2

install:
	pip3 install --editable .

generate_docs:
	$(MAKE) -C docs html

update_requirements:
	pip freeze > requirements.txt

.PHONY: init test