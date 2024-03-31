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
    path('author/<str:fullname>', views.author, name='author'),
    path('tag/<int:quote_id>', views.tag, name='tag'),

]
