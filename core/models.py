from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField(blank=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    num_up_vote = models.IntegerField(default=0)
    num_down_vote = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, blank=True)

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
