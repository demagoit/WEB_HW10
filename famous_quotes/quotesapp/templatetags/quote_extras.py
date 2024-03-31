from ..models import Author, Tag, Quote
from django import template

register = template.Library()


def author_url(author):
    urlname = author.fullname.replace(' ', '-')
    return urlname


register.filter('author_url', author_url)

# def tags_str(quote_tags):
#     insert = ', '.join([str(name) for name in quote_tags.all()])
#     s = f'<meta class="keywords" itemprop="keywords" content="{insert}"> '
#     return s

# register.filter('tags_2_str', tags_str)
