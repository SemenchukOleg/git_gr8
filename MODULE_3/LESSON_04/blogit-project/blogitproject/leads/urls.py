from django.urls import path

from leads import views

urlpatterns = [
    path('', views.contact_page, name='contact_page'),
]