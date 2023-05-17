from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register,name='register'),
    path('logout/', views.logout,name='logout'),
    path('forgot_password/', views.forgot_password,name='forgot_password'),
    path('change_password/<slug:reset_password_link_uuid>/', views.change_password,name='change_password'),
] 