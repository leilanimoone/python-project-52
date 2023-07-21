MANAGE := poetry run python manage.py

install: .env
	@poetry install

make-migration:
	@$(MANAGE) makemigrations
	
migrate: make-migration
	@$(MANAGE) migrate

build: install migrate

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	gunicorn task_manager.wsgi

trans:
	django-admin compilemessages

lint:
	poetry run flake8 --ignore=E501 task_manager

tests:
	poetry run python3 manage.py test