from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag, Author, Quote

from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    template = loader.get_template('index.html')
    context = {'quotes': quotes}

    return HttpResponse(template.render(context=context, request=request))

def author(request):
    pass

def tag(request):
    pass