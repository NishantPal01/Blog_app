from distutils.command.upload import upload
from django.db import models
from django.forms import DateField
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.

#create category model

class Category(models.Model):

    cat_id = models.AutoField(primary_key=True)
    cate_title = models.CharField(max_length=100)
    cate_desc = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<image src="/media/{}" style="width:40px;height:40px"    />'.format(self.image))



#post Model

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = HTMLField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'post/')