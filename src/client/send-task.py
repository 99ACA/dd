from celery import Celery

from config.celery import BROKER_URL

app = Celery(
    broker=BROKER_URL,
    # task_publish_retry=True, # Retried in the case of connection loss or other connection errors
    # task_publish_retry_policy={
    #     'max_retries': 3, # Maximum number of retries before giving up
    #     'interval_step': 0.2, # This number will be added to the retry delay
    #     'interval_max': 0.2, # Maximum number of seconds to wait between retries
    # },
    timezone="UTC"
)

taskId = app.send_task(
    ignore_result=True,
    # correlation_id='11',
    name="msg-echo.task",
    args=["Send args"]
)

print(f"Message had been sent {taskId}")