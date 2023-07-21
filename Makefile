MANAGE := poetry run python manage.py

install: .env
	@poetry install

build: 
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

trans:
	django-admin compilemessages

lint:
	poetry run flake8 --ignore=E501 task_manager

tests:
	poetry run python3 manage.py test