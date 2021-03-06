import celery
from celery import Celery

from config.celery import BROKER_URL
from config.service import SERVICE_NAME

app = Celery(
    SERVICE_NAME, 
    broker=BROKER_URL,
)

app.autodiscover_tasks(["tasks"])

app.conf.task_routes = {'msg-echo.tasks.*': {'queue': f'{SERVICE_NAME}-queue'}}

# Disable log
# ------------------------
# @celery.signals.setup_logging.connect
# def on_setup_logging(**kwargs):
#     pass


if __name__ == '__main__':
    # https://docs.celeryproject.org/en/stable/reference/celery.worker.html#celery.worker.WorkController.setup_defaults
    worker = app.Worker(
        loglevel='INFO',
    )

    # print(app.control.inspect().registered())

    worker.start()