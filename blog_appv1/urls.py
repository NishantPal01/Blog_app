from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<slug:url>',views.post, name="post")
]