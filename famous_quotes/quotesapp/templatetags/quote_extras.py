from ..models import Author, Tag, Quote
from django import template

register = template.Library()


def author_name(_id):
    fullname = Author.objects.filter(id=_id)
    return fullname


register.filter('author', author_name)
