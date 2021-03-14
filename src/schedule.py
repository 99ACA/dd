# https://docs.celeryproject.org/en/stable/reference/celery.beat.html
# https://docs.celeryproject.org/en/stable/reference/celery.beat.html#celery.beat.Scheduler.schedule

from celery import Celery
from celery.schedules import crontab

from config.celery import BROKER_URL
from config.service import SERVICE_NAME

app = Celery(
    SERVICE_NAME, 
    broker=BROKER_URL,
    broker_transport_options={
        'visibility_timeout': 1, # in sec
        'max_retries': 5
    },
)

app.autodiscover_tasks(["tasks"])

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        5.0,
        test.s('Happy Mondays!'),
    )

@app.task(name="test")
def test(arg):
    print(f"------    {arg}           -----------------")

if __name__ == '__main__':
    app.add_periodic_task(5.0, test.s('hello'), name='add every 10 *******')

    beat = app.Beat(
        loglevel='INFO',
        # beat_sync_every = 10,
        # beat_max_loop_interval = 1,
    )

    beat.run()
