# Celery Demo

## Steps

### Dockers

- Run RabbitMQ

```
    docker run --rm --name rabbit -d -p 5672:5672 -p 15672:15672 -e RABBITMQ_NODENAME=rabbit@celery -e RABBITMQ_DEFAULT_USER=rabbit -e RABBITMQ_DEFAULT_PASS=rabbit  rabbitmq:3-management

    # Can add also into docker run: -e RABBITMQ_DEFAULT_VHOST=my_vhost
    # should also change the config to: BROKER_URL='amqp://rabbit:rabbit@127.0.0.1:5672/my_vhost/'
```

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