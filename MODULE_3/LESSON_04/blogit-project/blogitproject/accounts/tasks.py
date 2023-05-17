
from celery import shared_task
from django.core.mail import send_mail
from blogitproject.settings import EMAIL_HOST_USER

@shared_task
def send_email_reset_password_task(subject, message, email):
    recipient_list = [email]
    send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=recipient_list,
                fail_silently=False,
            )


