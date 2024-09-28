from celery import shared_task

@shared_task
def auth_telegram_account():
    return