from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from blog_appv1.models import Category, Post

# Create your views here.

def index(request):
    posts=Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts' : posts,
        'cats' : cats
    }
    return render(request, 'home.html' , data)



def post(request,url):
    posts=Post.objects.get(url=url)

    return render(request, 'posts.html', {'posts' : posts})