init:
	pip3 install -r requirements.txt

test:
	nose2

install:
	pip3 install --editable .

.PHONY: init test