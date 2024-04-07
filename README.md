# WEB_HW10
Django, Postgres, MongoDB

sudo docker compose up


To migrate from MongoDB to Postgres:
- fill Mongo credentials in famous_quotes/utils/config.ini
- run python3 ./manage.py migrate  (to create shemas in Postgree)
- run python3 -m famous_quotes.utils.migrate_db
- run python3 ./manage.py runserver (to see result on localhost:8000)