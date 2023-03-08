from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit', views.edit, name='edit'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    ]