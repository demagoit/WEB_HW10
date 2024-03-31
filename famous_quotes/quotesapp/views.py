from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag, Author, Quote
from django.core.paginator import Paginator

from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request, page=1):
    quotes = Quote.objects.all()
    template = loader.get_template('index.html')
    per_page = 10
    paginator = Paginator(quotes, per_page=per_page)
    quotes_on_page = paginator.page(page)
    context = {'quotes': quotes_on_page}
    # return HttpResponse(template.render(context=context, request=request))
    return render(request, 'index.html', context=context)

def author(request, author_url):
    pass

def tag(request, quote_id):
    pass