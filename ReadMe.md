# Celery Demo

## Steps

### Dockers

- Run redis docker

### Env

- Create venv `python -m venv .venv && . ./.venv/bin/activate`
- Install `pip install -r requirements.txt`


## Tips

### Auto Import modules

- The `__init__.py` contain code the automatic load modules.

## Issue

- Send in correct message (use self) -> queue stake


## Monitoring

Run the following cmd

```
    cd src
    celery -A puller  inspect  active_queues
```

Clean Queue

```
    celery -A puller purge -Q celery
```