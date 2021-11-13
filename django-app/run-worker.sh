#!/bin/bash

/usr/local/bin/celery -A dc_compose worker --beat -S django -l INFO