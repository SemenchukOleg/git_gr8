from django.urls import path
from demoapi import views

urlpatterns = [
    #test data
    path('test/', views.test)
]