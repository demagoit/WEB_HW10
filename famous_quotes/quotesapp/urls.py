"""
URL configuration for famous_quotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page>', views.index, name='index_paginate'),
    path('author/<str:author_url>', views.author, name='author'),
    path('tag/<str:tag>', views.tag, name='tag'),
    path('tag/<str:tag>/page/<int:page>', views.tag, name='tag_paginator'),
    path('tags/new', views.new_tag, name='new_tag'),
    path('authors/new', views.new_author, name='new_author'),
    path('quotes/new', views.new_quote, name='new_quote'),

]
