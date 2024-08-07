from django.db import models
from dashboard.models import BlogPost

class Comment(models.Model):
    title = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    user = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.comment[:50]