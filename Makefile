install:
	poetry install

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	python3 manage.py shell

makemig:
	poetry run python3 manage.py makemigrations

mig:
	poetry run python3 manage.py migrate

parsetrans:
	django-admin makemessages --ignore="static" --ignore=".env"  -l ru

trans:
	django-admin compilemessages

lint:
	poetry run flake8 --ignore=E501 task_manager

tests:
	poetry run python3 manage.py test

setup:
	poetry install
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi