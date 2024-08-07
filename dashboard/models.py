from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('mypost')