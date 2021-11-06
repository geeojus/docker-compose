#!/bin/bash

python manage.py migrate --noinput

python manage.py createsuperuser --noinput

SERVER_PORT=${PORT:-7000}
/usr/local/bin/gunicorn dc_compose.wsgi:application --bind "0.0.0.0:${SERVER_PORT}"