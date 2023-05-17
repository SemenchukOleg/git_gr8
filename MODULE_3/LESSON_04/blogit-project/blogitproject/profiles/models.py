from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.utils import generate_profile_thumbnail
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, blank=True, default='')
    about = models.TextField(default='', blank=True)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d', default='default/default-profile-logo.png',
    verbose_name='Profile Image', blank=True)
    profile_image_thumbnail = models.ImageField(blank=True, verbose_name='Profile Image Thumbnail')
    is_thumbnailed = models.BooleanField(default=False, help_text='Флаг, который регулирует состояние созданияминиатюры для фото профиля')
    reset_password_link_uuid = models.UUIDField(default=uuid.uuid4, blank=True)

    def __str__(self) -> str:
        return self.user.get_username() + '(user_id: {0}, profile_id:{1})'.format(self.user.id, self.id)
    

    def change_profile_image_thumbnail(self):
        self.profile_image_thumbnail = generate_profile_thumbnail(self.id, self.profile_image.name, w=200, h=200)

    def save(self, *args, **kwargs):
        print("Идет сохранение профиля {}".format(self)) 
        super(Profile, self).save(*args, **kwargs)

@receiver (post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        print('Сигнал вызван')
        profile = Profile.objects.create(
            user=instance,
            reset_password_link_uuid=uuid.uuid4(),
            ) 
        print('Профиль привязан')
        print( 'Profile :', profile)    


@receiver (post_save, sender=Profile)
def creative_profile_image_thumbnail(sender, instance, created, *args, **kwargs):
    if not instance.is_thumbnailed:
        print("Мы внутри сигнала create_profile_image_thumbnail")
        instance.change_profile_image_thumbnail()
        instance.is_thumbnailed = True
        instance.save()