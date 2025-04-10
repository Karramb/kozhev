import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kozhev.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'amqp://guest:guest@rabbitmq:5672//my_vhost'
app.autodiscover_tasks()
