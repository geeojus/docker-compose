import os
import pathlib
import dotenv

from celery import Celery

USE_DOTENV = os.environ.get("USE_DOTENV_PKG")
if str(USE_DOTENV) == "1":
    base_path = pathlib.Path(__file__).resolve().parent.parent.parent
    dotenv.read_dotenv(base_path / ".env-dev")

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dc_compose.settings')

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"

app = Celery('dc_compose')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.broker_url = REDIS_URL
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"