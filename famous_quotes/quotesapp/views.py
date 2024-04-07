from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag, Author, Quote
from .forms import TagForm, AuthorForm, QuoteForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.

per_page = 10


def index(request, page=1):
    quotes = Quote.objects.all()
    tags = Tag.objects.annotate(
        tag_count=Count("quote")).order_by("-tag_count")[:10]
    paginator = Paginator(quotes, per_page=per_page)
    quotes_on_page = paginator.page(page)
    context = {'quotes': quotes_on_page, 'tags': tags}
    return render(request, 'quotes/index.html', context=context)


def author(request, author_url):
    fullname = author_url.replace('-', ' ')
    author = Author.objects.get(fullname=fullname)
    context = {'author': author}
    return render(request, 'quotes/author.html', context=context)


def tag(request, tag, page=1):
    tag_id = Tag.objects.get(tag=tag)
    quotes = Quote.objects.filter(tags__in=[tag_id])
    tags = Tag.objects.annotate(
        tag_count=Count("quote")).order_by("-tag_count")[:10]
    paginator = Paginator(quotes, per_page=per_page)
    quotes_on_page = paginator.page(page)
    context = {'quotes': quotes_on_page, 'selected_tag': tag, 'tags': tags}
    return render(request, 'quotes/tags.html', context=context)


@login_required
def new_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotes/new_tag.html', {'form': form})
    return render(request, 'quotes/new_tag.html', {'form': TagForm()})


@login_required
def new_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotes/new_author.html', {'form': form})
    return render(request, 'quotes/new_author.html', {'form': AuthorForm()})


@login_required
def new_quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():

            new_quote = form.save(commit=False)

            new_quote.author = Author.objects.get(
                fullname=request.POST.get('author'))
            new_quote.save()

            # choise_tags = Tag.objects.filter(
            #     tag__in=request.POST.getlist('tags'))
            # for tag in choise_tags.iterator():
            #     print(tag, tag.id)
            #     new_quote.tags.add(tag.id)
            tags = form.cleaned_data['tags']
            print(tags)
            new_quote.tags.add(*tags)



            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotes/new_quote.html', {'form': form, 'tags': tags, 'authors': authors})
    return render(request, 'quotes/new_quote.html', {'form': QuoteForm(), 'tags': tags, 'authors': authors})
