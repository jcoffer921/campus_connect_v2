from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Discussion(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Reply(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reply by {self.author} on {self.discussion.title}"
