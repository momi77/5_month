import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_api.settings')


app = Celery('shop_api')  


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'users.tasks.add',  
        'schedule': 10.0,           
        'args': (4, 5),
    },
    'add-every-monday-9am': {
        'task': 'users.tasks.add',
        'schedule': crontab(hour=9, minute=0, day_of_week=1),  
        'args': (10, 20),
    },
}
