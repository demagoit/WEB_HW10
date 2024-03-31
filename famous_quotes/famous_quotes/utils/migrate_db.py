import os
import django
import configparser
import mongoengine

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'famous_quotes.settings')
django.setup()

from quotesapp.models import Tag, Author, Quote

config = configparser.ConfigParser()
if os.path.exists('famous_quotes/utils/config_dev.ini'):
    config.read('famous_quotes/utils/config_dev.ini')
else:
    config.read('famous_quotes/utils/config.ini')

mongo = {
    'user': config.get('CLUSTER', 'USER'),
    'pwd': config.get('CLUSTER', 'PWD'),
    'domain': config.get('CLUSTER', 'DOMAIN'),
    'db_name': config.get('BOOKS', 'DB_NAME')
}

uri = f"mongodb+srv://{mongo['user']}:{mongo['pwd']}@{mongo['domain']}/{mongo['db_name']}?retryWrites=true&w=majority"
conn = mongoengine.connect(host=uri, ssl=True)

authors = conn[mongo['db_name']].author.find()

for author in authors:
    Author.objects.get_or_create(
        fullname = author['fullname'],
        born_date = author['born_date'],
        born_location = author['born_location'],
        description = author['description']
    )

quotes = conn[mongo['db_name']].quote.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        st = tag.get('tag')
        tg, _ = Tag.objects.get_or_create(
            tag = st
        )
        tags.append(tg)
    
    quote_exists = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not quote_exists:
        author_mongo = conn[mongo['db_name']].author.find_one({'_id': quote['author']})
        author = Author.objects.get(fullname=author_mongo['fullname'])

        q = Quote.objects.create(
            quote  = quote['quote'],
            author  = author
        )

        for tag in tags:
            q.tags.add(tag)