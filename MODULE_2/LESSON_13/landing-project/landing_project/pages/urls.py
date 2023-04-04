from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_lead', views.create_lead, name='create_lead'),
    ]