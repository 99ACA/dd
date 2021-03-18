import celery
from celery import Celery
from kombu import Exchange, Queue
from celery.exceptions import Reject

from config.celery import BROKER_URL
from config.service import SERVICE_NAME

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-task_publish_retry

app = Celery(
    SERVICE_NAME, 
    broker=BROKER_URL,
    broker_transport_options={
        'visibility_timeout': 1, # in sec
        'max_retries': 5
    },
)

app.autodiscover_tasks(["tasks"])


default_exchange_name = 'event-bus'
default_routing_key = 'default'
default_queue_name = 'default'

default_exchange = Exchange(default_exchange_name, type='topic')

queue_name = 'srv-2-notify'
app.conf.task_queues = (
    Queue(queue_name,  default_exchange, routing_key='publish.notify.email',queue_arguments={'x-queue-name': queue_name}),
)


# Disable Celery log - https://docs.celeryproject.org/en/stable/userguide/tasks.html#logging
# https://www.distributedpython.com/2018/08/28/celery-logging/
# Change the log - https://wdicc.com/logging-in-celery-and-django/
# ------------------------
# @celery.signals.setup_logging.connect
# def on_setup_logging(**kwargs):
#     pass



if __name__ == '__main__':
    import os 

    # https://docs.celeryproject.org/en/stable/reference/celery.worker.html#celery.worker.WorkController.setup_defaults
    worker = app.Worker(
        hostname=f"topic-2@{os.getpid()}",
        loglevel='INFO', #  ! Verify - it is working
        redirect_stdouts=False, # ?
        hijack_root_logger=False, # ?
        log_color=False, #  ! Verify - it is working
    )

    worker.start()