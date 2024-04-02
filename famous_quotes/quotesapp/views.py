from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag, Author, Quote
from .forms import TagForm, AuthorForm, QuoteForm
from django.core.paginator import Paginator

# Create your views here.

per_page = 10

def index(request, page=1):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, per_page=per_page)
    quotes_on_page = paginator.page(page)
    context = {'quotes': quotes_on_page}
    return render(request, 'quotes/index.html', context=context)

def author(request, author_url):
    fullname = author_url.replace('-', ' ')
    author = Author.objects.get(fullname=fullname)
    context = {'author': author}
    return render(request, 'quotes/author.html', context=context)

def tag(request, tag, page=1):
    tag_id = Tag.objects.get(tag=tag)
    quotes = Quote.objects.filter(tags__in=[tag_id])
    paginator = Paginator(quotes, per_page=per_page)
    quotes_on_page = paginator.page(page)
    context = {'quotes': quotes_on_page, 'selected_tag': tag}
    return render(request, 'quotes/tags.html', context=context)

def new_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotes/new_tag.html', {'form': form})
    return render(request, 'quotes/new_tag.html', {'form': TagForm()})

def new_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotes/new_author.html', {'form': form})
    return render(request, 'quotes/new_author.html', {'form': AuthorForm()})