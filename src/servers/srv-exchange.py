from celery import Celery
from kombu import Exchange, Queue
from celery.exceptions import Reject



default_exchange = Exchange(default_exchange_name, type='direct')
default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key)