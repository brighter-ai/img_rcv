.PHONY: requirements run

all: requirements run

requirements:
	pipenv install

run:
	FLASK_APP=main.py pipenv run flask run