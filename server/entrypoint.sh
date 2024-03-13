#!/bin/bash
cd /app

flask --app migrate db init
flask --app migrate db migrate
flask --app migrate db upgrade

flask --app main run --host 0.0.0.0 --port 8000