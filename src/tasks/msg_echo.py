import celery
from celery import shared_task


@shared_task(bind=True,name="msg-echo.task")
def print_message(self,arg):
    # task.request - https://docs.celeryproject.org/en/stable/userguide/tasks.html#task-request
    print(f"[{self.request.correlation_id}]--{self.request} -  {arg}")