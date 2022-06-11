from turtle import title
from unicodedata import category
from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('cate_title', 'cate_desc', 'url', 'add_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)