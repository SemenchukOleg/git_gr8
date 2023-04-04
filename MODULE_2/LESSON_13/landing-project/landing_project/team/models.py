from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=100, blank=False)
    twitter = models.CharField(max_length=100, blank=True, default='#')
    instagram = models.CharField(max_length=100, blank=True, default='#')
    facebook = models.CharField(max_length=100, blank=True, default='#')
    linkedin = models.CharField(max_length=100, blank=True, default='#')
    image = models.ImageField(blank=False, upload_to='team/', default='team\default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
