from django.urls import path
from profiles import views

urlpatterns = [
    path('<slug:username>', views.get_user_profile, name='get_user_profile'),
    path('<slug:username>/edit', views.edit_user_profile, name='edit_user_profile'),
]