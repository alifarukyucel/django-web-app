from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):  # inherits from models.Model
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # can never be updated if auto_now_add=True
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if a user is deleted, all of its posts are deleted
