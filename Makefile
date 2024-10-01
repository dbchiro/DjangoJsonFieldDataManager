MANAGE = poetry run python -m manage


install :
	poetry install

build :
	poetry build

runserver:
	$(MANAGE) runserver
