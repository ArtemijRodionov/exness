# Test assignment from exness.com
[![Build Status](https://travis-ci.org/artemiy312/exness.svg?branch=master)](https://travis-ci.org/artemiy312/exness)

## Result
Finished application on [heroku](https://nameless-dawn-30374.herokuapp.com/).

## Development
```bash
docker-compose up -d
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic --noinput
```
