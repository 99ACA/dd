import celery
from celery import Celery
from kombu import Queue


from config.celery import BROKER_URL
from config.service import SERVICE_NAME

from celery.signals import worker_ready

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
app.conf.task_default_queue = f'{SERVICE_NAME}-queue'


# Disable Celery log - https://docs.celeryproject.org/en/stable/userguide/tasks.html#logging
# https://www.distributedpython.com/2018/08/28/celery-logging/
# Change the log - https://wdicc.com/logging-in-celery-and-django/
# ------------------------
# @celery.signals.setup_logging.connect
# def on_setup_logging(**kwargs):
#     pass



if __name__ == '__main__':
    # https://docs.celeryproject.org/en/stable/reference/celery.worker.html#celery.worker.WorkController.setup_defaults
    worker = app.Worker(
        hostname=f'{SERVICE_NAME}-host-name', # ! Verify - The workers node name 
        loglevel='INFO', #  ! Verify - it is working
        redirect_stdouts=False, # ?
        hijack_root_logger=False, # ?
        log_color=False, #  ! Verify - it is working
    )

    worker.start()