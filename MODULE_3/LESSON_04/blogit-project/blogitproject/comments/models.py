from django.db import models
from profiles.models import Profile


# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(default='', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.user.username(self.id)}'
