
from celery import shared_task
import time

@shared_task(name='long_await')
def long_await(t):
    print(f'Я буду ожидать {t} секунд. ')
    time.sleep(t)
    print(f'Спасибо за долгое ожидание')


