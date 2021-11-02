#!/bin/bash

SERVER_PORT=${PORT-:8000}

/usr/local/bin/uvicorn server:app --host 0.0.0.0 --port SERVER_PORT