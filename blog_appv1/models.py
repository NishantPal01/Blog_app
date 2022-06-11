from distutils.command.upload import upload
from django.db import models
from django.forms import DateField

# Create your models here.

#create category model

class Category(models.Model):

    cat_id = models.AutoField(primary_key=True)
    cate_title = models.CharField(max_length=100)
    cate_desc = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)



#post Model

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'post/')