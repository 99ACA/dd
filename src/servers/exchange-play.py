from celery import Celery
from kombu import Exchange, Queue
from celery.exceptions import Reject

default_queue_name = 'default'
default_exchange_name = 'default'
default_routing_key = 'default'

sunshine_queue_name = 'sunshine'
sunshine_routing_key = 'sunshine'

moon_queue_name = 'moon'
moon_routing_key = 'moon'

app = Celery(
    'tasks',
    broker='amqp://guest@localhost:5672//',
    backend='redis://localhost:6379/0')

default_exchange = Exchange(default_exchange_name, type='direct')
default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key)

sunshine_queue = Queue(
    sunshine_queue_name,
    default_exchange,
    routing_key=sunshine_routing_key)

moon_queue = Queue(
    moon_queue_name,
    default_exchange,
    routing_key=moon_queue_name)

app.conf.task_queues = (default_queue, sunshine_queue, moon_queue)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key