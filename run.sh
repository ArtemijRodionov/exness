#!/usr/bin/env sh
set -o errexit
set -o nounset

PROJECT_NAME=assignment


cd "$PROJECT_NAME"
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn "$PROJECT_NAME.wsgi:application" -b 0.0.0.0:$PORT --workers=3 --log-file=-

