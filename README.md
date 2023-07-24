### Hexlet tests and linter status:
[![Actions Status](https://github.com/leilanimoone/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/leilanimoone/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/325bdd121258234800a1/maintainability)](https://codeclimate.com/github/leilanimoone/python-project-52/maintainability)

### Description

This simple web task manager with user, task, label and status models writen on Django. It uses bootsrap and any available DB for Django.

https://task-manager-lt5g.onrender.com - demonstration page.

### Environment variables

It is necessary to create a .env file in the root of the project and write the values of the variables there.
<pre>
SECRET_KEY =
DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
ROLLBAR_TOKEN =
</pre>

### Installation
<pre>
$ git clone https://github.com/leilanimoone/python-project-52.git
$ cd python-project-52
$ make setup
# The site will be available at http://127.0.0.1:8000/ and http://0.0.0.0:8000/
</pre>
