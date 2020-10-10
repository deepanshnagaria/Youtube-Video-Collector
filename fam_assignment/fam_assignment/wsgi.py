"""
WSGI config for fam_assignment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from video_collector.background import collect
from datetime import datetime, timedelta
from background_task.models import Task

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fam_assignment.settings')

application = get_wsgi_application()

test_datetime=datetime.utcnow()+timedelta(seconds=10)
collect(repeat=60)
