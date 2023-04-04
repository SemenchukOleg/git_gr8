from django.db import models

# Create your models here.
class Testimonial(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=100, blank=False)
    feedback = models.TextField(blank=False)
    image = models.ImageField(blank=False, upload_to='testimonial/', default='testimonial\default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)