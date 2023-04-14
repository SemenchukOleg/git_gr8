from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, blank=True, default='')
    about = models.TextField(default='', blank=True)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d', default='default/default-profile-logo.png',
    verbose_name='Profile Image', blank=True)
    profile_image_thumbnail = models.ImageField(blank=True, verbose_name='Profile Image Thumbnail')
    is_thumbnailed = models.BooleanField(default=False, help_text='Флаг, который регулирует состояние созданияминиатюры для фото профиля')

    def __str__(self) -> str:
        return self.user.get_username() + '(user_id: {0}, profile_id:{1})'.format(self.user.id, self.id)
    
