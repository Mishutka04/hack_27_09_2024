import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rutube_app.settings')

app = Celery('service')
app.config_from_object('django.conf:settings')
app.conf.broker_url = 'redis://redis:6379/0'
app.autodiscover_tasks()