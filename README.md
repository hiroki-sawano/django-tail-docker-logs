# django-tail-docker-logs

## Prerequisite

python >= 3.6

## Installation

```
$ python -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## How to use

Access `/<container_name>` to see its container logs.
