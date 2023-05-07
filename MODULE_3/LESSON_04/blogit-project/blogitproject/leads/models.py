
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from blogitproject.settings import EMAIL_HOST_USER


# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_unswered = models.BooleanField(default=False)

@receiver(post_save, sender=Lead)
def send_email_to_staff(sender, instance, crated, *arg, **kwargs):
    if crated:
        subject = instance.subject
        message = instance.message + '\n from {0} with email {1}.'.format(instance.name, instance.email)
        recipient_list = [user.email for user in User.objects.filter(is_staff=True)]
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=recipient_list,
                fail_silently=False,
            )
        except Exception as err :
            print('Email erroe', err)